import pytest
from whitespace_stego.encoder import embed_message
from whitespace_stego.decoder import decode_message

@pytest.mark.parametrize("message", ["Hello", "😀 Test", "秘密"])
@pytest.mark.parametrize("carrier", ["", "Hello!", "Test123"])
def test_roundtrip(message, carrier):
    encoded = embed_message(carrier, message)
    decoded = decode_message(encoded)
    assert decoded == message
