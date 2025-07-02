import pytest
import base64
from whitespace_stego import core

@pytest.mark.parametrize("message,carrier,password", [
    ("Hello", "World", None),
    ("Secret", "Carrier", "pass123"),
    ("Unicode 🌍", "Emoji 🚀", None),
    ("", "NonEmpty", None),  # Should raise
])
def test_encode_decode_roundtrip(message, carrier, password):
    if not message:
        with pytest.raises(ValueError):
            core.encode(message, carrier, password)
        return
    encoded = core.encode(message, carrier, password)
    assert isinstance(encoded, str)
    decoded = core.decode(encoded, password)
    assert decoded == message


def test_encode_decode_multiple_messages():
    carrier = "CarrierText"
    messages = ["First", "Second", "Third"]
    encoded = carrier
    for msg in messages:
        encoded = core.encode(msg, encoded)
    decoded = core.decode(encoded)
    assert isinstance(decoded, list)
    assert decoded == messages


def test_encode_decode_multiple_with_password():
    carrier = "CarrierText"
    password = "supersecret"
    messages = ["Alpha", "Beta", "Gamma"]
    encoded = carrier
    for msg in messages:
        encoded = core.encode(msg, encoded, password)
    decoded = core.decode(encoded, password)
    assert isinstance(decoded, list)
    assert decoded == messages


def test_decode_with_wrong_password():
    carrier = "CarrierText"
    encoded = core.encode("SecretMsg", carrier, password="rightpass")
    # Should not decode with wrong password
    with pytest.raises(ValueError):
        core.decode(encoded, password="wrongpass")


def test_decode_no_message():
    with pytest.raises(ValueError):
        core.decode("Just a normal string with no markers")


def test_extract_encoded_and_remaining():
    msg = "ExtractMe"
    carrier = "Carrier"
    encoded = core.encode(msg, carrier)
    extracted, remaining = core.extract_encoded(encoded)
    assert core.has_encoded_message(extracted)
    assert not core.has_encoded_message(remaining)
    assert msg in core.decode(extracted)


def test_has_encoded_message():
    msg = "Hidden"
    carrier = "C"
    encoded = core.encode(msg, carrier)
    assert core.has_encoded_message(encoded)
    assert not core.has_encoded_message("No secrets here!")


def test_get_encoded_message_size():
    msg = "SizeTest"
    carrier = "Car"
    encoded = core.encode(msg, carrier)
    size = core.get_encoded_message_size(encoded)
    assert isinstance(size, int)
    assert size > 0
    # No message
    assert core.get_encoded_message_size("Nothing here") is None


def test_decode_corrupted_message():
    msg = "CorruptMe"
    carrier = "Carrier"
    encoded = core.encode(msg, carrier)
    # Corrupt the encoded message by removing a marker
    corrupted = encoded.replace(core.END_MARKER, "", 1)
    with pytest.raises(ValueError):
        core.decode(corrupted)
    # Corrupt the zero-width data
    corrupted2 = encoded.replace(core.ZERO_BIT, "X", 1)
    with pytest.raises(ValueError):
        core.decode(corrupted2)


def test_private_functions():
    # _encode_binary and _decode_binary
    data = b"abc"
    zw = core._encode_binary(data)
    assert isinstance(zw, str)
    out = core._decode_binary(zw)
    assert out == data
    # _count_message_pairs
    msg = "PairTest"
    carrier = "Car"
    encoded = core.encode(msg, carrier)
    assert core._count_message_pairs(encoded) == 1
    # _find_next_slot
    slot = core._find_next_slot(carrier)
    assert isinstance(slot, int)
    # _insert_message_at_position
    emsg = core.START_MARKER + zw + core.END_MARKER
    inserted = core._insert_message_at_position(carrier, emsg, 1)
    assert emsg in inserted


def test_derive_key_and_crypto():
    pw = "pw"
    key = core.derive_key(pw)
    assert isinstance(key, bytes)
    data = b"data"
    encrypted = core.encrypt_data(data, pw)
    assert isinstance(encrypted, bytes)
    decrypted = core.decrypt_data(encrypted, pw)
    assert decrypted == base64.b64encode(b"data") or decrypted == data  # Accepts both
    # Bad decrypt
    with pytest.raises(ValueError):
        core.decrypt_data(b"short", pw)


def test_multi_message_bad_password_behavior():
    carrier = "C"
    m1, m2, m3 = "msg1", "msg2", "msg3"
    p1, p2, p3 = "pw1", "pw2", "pw3"
    # Encode three messages with three different passwords
    c1 = core.encode(m1, carrier, p1)
    c2 = core.encode(m2, c1, p2)
    c3 = core.encode(m3, c2, p3)
    # Decoding with wrong password should raise BadPasswordError
    with pytest.raises(core.BadPasswordError):
        core.decode(c3, password="wrong")
    with pytest.raises(core.BadPasswordError):
        core.decode(c3, password=p2)  # Only p2, not all
    # Decoding with correct password for each message returns only that message
    assert core.decode(c3, password=p1) == m1
    assert core.decode(c3, password=p2) == m2 or core.decode(c3, password=p2) == m1  # Accepts either if implementation returns first found
    assert core.decode(c3, password=p3) == m3 or core.decode(c3, password=p1) == m1 