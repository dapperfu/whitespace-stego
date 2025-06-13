"""Tests for the core steganography functionality."""

import pytest

from whitespace_stego.core import decode, encode

def test_encode_decode_no_carrier() -> None:
    """Test encoding and decoding without a carrier."""
    message = "Hello, World!"
    encoded = encode(message, "")
    decoded = decode(encoded)
    assert decoded == message

def test_encode_decode_with_carrier() -> None:
    """Test encoding and decoding with a carrier."""
    message = "Secret message"
    carrier = "This is a normal text"
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message
    assert encoded.startswith(carrier[0])

def test_encode_decode_with_password() -> None:
    """Test encoding and decoding with password protection."""
    message = "Top secret"
    carrier = "Public text"
    password = "mysecretpassword"
    encoded = encode(message, carrier, password)
    decoded = decode(encoded, password)
    assert decoded == message

def test_decode_invalid_carrier() -> None:
    """Test decoding an invalid carrier."""
    with pytest.raises(ValueError, match="No valid message found in carrier"):
        decode("Invalid carrier text")

def test_encode_decode_special_chars() -> None:
    """Test encoding and decoding messages with special characters."""
    message = "Special chars: !@#$%^&*()_+{}|:<>?~`"
    carrier = "Normal text"
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message

def test_encode_decode_unicode() -> None:
    """Test encoding and decoding Unicode messages."""
    message = "Unicode: 你好世界 🌍"
    carrier = "English text"
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message 