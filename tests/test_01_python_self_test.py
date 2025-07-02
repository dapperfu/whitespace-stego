"""
Test 01: Python Implementation Self-Test

This test verifies that the Python implementation can encode and decode
messages correctly with itself in all combinations.
"""

import pytest
from whitespace_stego.core import encode, decode


def test_basic_encode_decode():
    """Test basic encode/decode without carrier."""
    message = "Hello, World!"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_encode_decode_with_carrier():
    """Test encode/decode with carrier text."""
    message = "Secret message"
    carrier = "This is some carrier text"
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message


def test_encode_decode_with_password():
    """Test encode/decode with password protection."""
    message = "Top secret"
    password = "mypassword123"
    encoded = encode(message, password=password)
    decoded = decode(encoded, password=password)
    assert decoded == message


def test_encode_decode_with_carrier_and_password():
    """Test encode/decode with both carrier and password."""
    message = "Very secret message"
    carrier = "Public carrier text"
    password = "securepass"
    encoded = encode(message, carrier, password)
    decoded = decode(encoded, password)
    assert decoded == message


def test_empty_carrier():
    """Test encode/decode with empty carrier."""
    message = "Test message"
    encoded = encode(message, "")
    decoded = decode(encoded)
    assert decoded == message


def test_unicode_message():
    """Test encode/decode with Unicode message."""
    message = "Hello 世界! 🌍"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_unicode_carrier():
    """Test encode/decode with Unicode carrier."""
    message = "Test"
    carrier = "Carrier with 中文 and emoji 🚀"
    encoded = encode(message, carrier)
    decoded = decode(encoded)
    assert decoded == message


def test_long_message():
    """Test encode/decode with long message."""
    message = "A" * 1000
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_special_characters():
    """Test encode/decode with special characters."""
    message = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_newlines_in_message():
    """Test encode/decode with newlines in message."""
    message = "Line 1\nLine 2\nLine 3"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_tabs_in_message():
    """Test encode/decode with tabs in message."""
    message = "Tab\tseparated\tvalues"
    encoded = encode(message)
    decoded = decode(encoded)
    assert decoded == message


def test_empty_message_error():
    """Test that empty message raises error."""
    with pytest.raises(ValueError):
        encode("")


def test_wrong_password_error():
    """Test that wrong password raises error."""
    message = "Secret"
    password = "correct"
    wrong_password = "wrong"
    encoded = encode(message, password=password)
    with pytest.raises(ValueError):
        decode(encoded, wrong_password)


def test_no_markers_error():
    """Test that text without markers raises error."""
    with pytest.raises(ValueError):
        decode("This text has no markers")


def test_only_start_marker_error():
    """Test that text with only start marker raises error."""
    from whitespace_stego.core import START_MARKER
    with pytest.raises(ValueError):
        decode(f"This text has {START_MARKER} but no end marker")


def test_only_end_marker_error():
    """Test that text with only end marker raises error."""
    from whitespace_stego.core import END_MARKER
    with pytest.raises(ValueError):
        decode(f"This text has {END_MARKER} but no start marker")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 