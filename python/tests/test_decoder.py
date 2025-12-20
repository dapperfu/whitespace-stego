"""Tests for decoder module."""

import pytest
from whitespace_stego import encode, decode
from whitespace_stego.errors import (
    DecodingError,
    MissingMarkerError,
    InvalidPayloadError,
)


def test_decode_empty_message():
    """Test decoding empty encoded message."""
    encoded = encode("")
    result = decode(encoded)
    assert result == ""


def test_round_trip_simple():
    """Test round-trip encoding and decoding."""
    message = "Hello, World!"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_round_trip_unicode():
    """Test round-trip with Unicode."""
    message = "Hello 🌍 你好"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_round_trip_with_carrier():
    """Test round-trip with carrier text."""
    message = "Secret message"
    carrier = "This is normal text."
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message


def test_decode_missing_start_marker():
    """Test decoding text without start marker."""
    with pytest.raises(MissingMarkerError):
        decode("Some text\u2063")


def test_decode_missing_end_marker():
    """Test decoding text without end marker."""
    with pytest.raises(MissingMarkerError):
        decode("\u2060Some text")


def test_decode_invalid_payload():
    """Test decoding with invalid payload characters."""
    # Create invalid payload (not just BIT_0 and BIT_1)
    invalid = "\u2060Invalid\u2063"
    with pytest.raises(InvalidPayloadError):
        decode(invalid)


def test_round_trip_with_password():
    """Test round-trip encoding and decoding with password."""
    message = "Secret message"
    password = "mypassword"
    encoded = encode(message, password=password)
    decoded = decode(encoded, password=password)
    assert decoded == message


def test_decode_wrong_password():
    """Test that wrong password produces incorrect decoding."""
    message = "Secret message"
    password = "correctpassword"
    wrong_password = "wrongpassword"
    encoded = encode(message, password=password)
    decoded = decode(encoded, password=wrong_password)
    # Should decode to something, but not the original message
    assert decoded != message


def test_round_trip_password_unicode():
    """Test round-trip with password and Unicode."""
    message = "Hello 🌍 你好"
    password = "密码123"
    encoded = encode(message, password=password)
    decoded = decode(encoded, password=password)
    assert decoded == message


def test_round_trip_password_with_carrier():
    """Test round-trip with password and carrier text."""
    message = "Secret message"
    password = "mypassword"
    carrier = "This is normal text."
    encoded = encode(message, carrier=carrier, password=password)
    decoded = decode(encoded, password=password)
    assert decoded == message


def test_backward_compatibility_no_password():
    """Test that messages encoded without password can be decoded without password."""
    message = "Test message"
    encoded = encode(message)  # No password
    decoded = decode(encoded)  # No password
    assert decoded == message

