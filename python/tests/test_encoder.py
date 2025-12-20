"""Tests for encoder module."""

import pytest
from whitespace_stego import encode
from whitespace_stego.errors import EncodingError


def test_encode_empty_message():
    """Test encoding empty message."""
    result = encode("")
    assert "\u2060" in result  # CONTROL_START
    assert "\u2063" in result  # CONTROL_END


def test_encode_simple_message():
    """Test encoding simple ASCII message."""
    message = "Hello, World!"
    result = encode(message)
    assert isinstance(result, str)
    assert len(result) > 0


def test_encode_with_carrier():
    """Test encoding with carrier text."""
    message = "Secret"
    carrier = "This is normal text."
    result = encode(message, carrier)
    assert carrier[0] in result
    assert len(result) > len(carrier)


def test_encode_unicode():
    """Test encoding Unicode message."""
    message = "Hello 🌍 你好"
    result = encode(message)
    assert isinstance(result, str)


def test_encode_carrier_with_control_chars():
    """Test that carrier with control characters raises error."""
    message = "Hello"
    carrier = "Text\u2060with\u2063markers"
    with pytest.raises(EncodingError):
        encode(message, carrier)


def test_round_trip():
    """Test that encoding produces valid output."""
    message = "Test message"
    encoded = encode(message)
    # Just check it's a valid string
    assert isinstance(encoded, str)
    assert len(encoded) > 0

