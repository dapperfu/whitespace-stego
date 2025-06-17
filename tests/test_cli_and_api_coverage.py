import pytest
import sys
import types
from pathlib import Path
from whitespace_stego import encode as encode_mod, decode as decode_mod
from whitespace_stego import cli as cli_mod
import click

# --- CLI backend selection and error handling ---
def test_cli_get_backend_python(monkeypatch):
    py_encode, py_decode = cli_mod.get_backend_implementation("python")
    assert callable(py_encode)
    assert callable(py_decode)

def test_cli_get_backend_rust_importerror(monkeypatch):
    sys_modules_backup = sys.modules.copy()
    sys.modules["whitespace_stego_backend"] = None
    with pytest.raises(SystemExit):
        cli_mod.get_backend_implementation("rust")
    sys.modules = sys_modules_backup

def test_cli_get_backend_c_importerror(monkeypatch):
    sys_modules_backup = sys.modules.copy()
    sys.modules["whitespace_stego.c_backend"] = None
    with pytest.raises(SystemExit):
        cli_mod.get_backend_implementation("c")
    sys.modules = sys_modules_backup

def test_cli_get_backend_unknown():
    with pytest.raises(ValueError):
        cli_mod.get_backend_implementation("unknown")

# --- Encode/Decode backend selection ---
def test_encode_message_unknown_backend(monkeypatch):
    ctx = click.Context(click.Command("encode"))
    ctx.obj = {"backend": "unknown"}
    monkeypatch.setattr(click, "get_current_context", lambda: ctx)
    with pytest.raises(ValueError):
        encode_mod.encode_message("msg", "carrier")

def test_decode_message_unknown_backend(monkeypatch):
    ctx = click.Context(click.Command("decode"))
    ctx.obj = {"backend": "unknown"}
    monkeypatch.setattr(click, "get_current_context", lambda: ctx)
    with pytest.raises(ValueError):
        decode_mod.decode_message("carrier")

# --- Directly test _encode_python/_decode_python error branches ---
def test__decode_python_missing_markers():
    with pytest.raises(ValueError):
        decode_mod._decode_python("no markers here")

def test__decode_python_no_binary():
    # Valid markers but no ONE_BIT or ZERO_BIT between
    text = encode_mod.START_MARKER + "" + encode_mod.END_MARKER
    with pytest.raises(ValueError):
        decode_mod._decode_python(text)

def test__decode_python_short_binary():
    # 10 bits only, not enough for length prefix
    bits = encode_mod.ZERO_BIT * 10
    text = encode_mod.START_MARKER + bits + encode_mod.END_MARKER
    with pytest.raises(ValueError):
        decode_mod._decode_python(text)

def test__decode_python_truncated_message():
    # 32 bits for length, but not enough bits for message
    length_bits = "00000000000000000000000000101000"  # 40 bits
    bits = "".join(encode_mod.ZERO_BIT if b == "0" else encode_mod.ONE_BIT for b in length_bits)
    text = encode_mod.START_MARKER + bits + encode_mod.END_MARKER
    with pytest.raises(ValueError):
        decode_mod._decode_python(text)

def test__decode_python_corrupted_base64():
    # Test with corrupted base64 data that could actually occur
    # Create a valid message first, then corrupt the base64 data
    import base64
    msg = "Hello"
    b64 = base64.b64encode(msg.encode("utf-8"))
    # Corrupt the base64 by changing some bits
    corrupted_b64 = bytearray(b64)
    corrupted_b64[0] = corrupted_b64[0] ^ 0xFF  # Flip all bits in first byte
    
    # Convert to binary
    binary = ''.join(format(b, '08b') for b in corrupted_b64)
    length_binary = format(len(binary), '032b')
    all_binary = length_binary + binary
    bits = ''.join(encode_mod.ONE_BIT if b == '1' else encode_mod.ZERO_BIT for b in all_binary)
    text = encode_mod.START_MARKER + bits + encode_mod.END_MARKER
    
    # Should raise ValueError due to corrupted base64
    with pytest.raises(ValueError):
        decode_mod._decode_python(text)

def test__decode_python_password_xor(monkeypatch):
    # Valid base64, with password, test xor branch
    import base64
    msg = "secret"
    b64 = base64.b64encode(msg.encode("utf-8"))
    # Encrypt with password
    password = "pw"
    encrypted = bytearray()
    pw_bytes = password.encode("utf-8")
    for i, b in enumerate(b64):
        encrypted.append(b ^ pw_bytes[i % len(pw_bytes)])
    # Convert to binary
    binary = ''.join(format(b, '08b') for b in encrypted)
    length_binary = format(len(binary), '032b')
    all_binary = length_binary + binary
    bits = ''.join(encode_mod.ONE_BIT if b == '1' else encode_mod.ZERO_BIT for b in all_binary)
    text = encode_mod.START_MARKER + bits + encode_mod.END_MARKER
    # Should decode with correct password
    assert decode_mod._decode_python(text, password) == msg
    # Should fail with wrong password
    with pytest.raises(ValueError):
        decode_mod._decode_python(text, "wrong")

def test__encode_python_and_decode_python_roundtrip():
    msg = "roundtrip"
    carrier = "carrier"
    password = "pw"
    encoded = encode_mod._encode_python(msg, carrier, password)
    decoded = decode_mod._decode_python(encoded, password)
    assert decoded == msg 