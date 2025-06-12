"""Tests for the whitespace steganography package."""

import pytest
from whitespace_stego import encode, decode

@pytest.mark.parametrize("message,password,carrier", [
    # ASCII tests
    ("hello", "secret", ""),              # password with empty carrier
    ("hello", "", ""),                    # empty password
    ("hello", None, ""),                  # None password
    ("hello", "secret", "A"),             # one-character carrier
    ("hello", "", "A"),                   # empty password, one-char carrier
    ("hello", None, "A"),                 # None password, one-char carrier
    ("hello", "secret", "AB"),            # two-char carrier
    ("hello", "", "AB"),                  # empty password, two-char carrier
    ("hello", None, "AB"),                # None password, two-char carrier
    ("hello", "secret", "The quick brown fox jumps"), # long carrier
    ("hello", "", "The quick brown fox jumps"),
    ("hello", None, "The quick brown fox jumps"),

    # Unicode and emoji tests
    ("こんにちは", "秘密", "🌸"),                # Japanese with emoji carrier
    ("👋🌍", "", "Hello World"),             # emoji message with ASCII carrier
    ("💡⚡🚀", None, "Start here:"),         # emoji message with sentence carrier
])
def test_stego_encode_decode(message, password, carrier):
    """Test encoding and decoding with various inputs."""
    encoded = encode(message, carrier=carrier, password=password)
    decoded_message, _ = decode(encoded, password=password)
    assert decoded_message == message 