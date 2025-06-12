"""Tests for the encode module.

This module contains tests for steganographic encoding functionality.
"""

import pytest
from whitespace_stego.encode import (
    encode_binary,
    encode_message,
    insert_payload,
    encode_and_insert
)
from whitespace_stego.common.charset import START_MARKER, END_MARKER, ZWSP, ZWNJ

def test_encode_binary() -> None:
    """Test binary encoding."""
    # Test encoding
    binary = "0101"
    encoded = encode_binary(binary)
    assert encoded == f"{ZWSP}{ZWNJ}{ZWSP}{ZWNJ}"
    
    # Test empty string
    assert encode_binary("") == ""

def test_encode_message() -> None:
    """Test message encoding."""
    # Test with password
    message = "Hello, 世界! 👋"
    encoded = encode_message(message, "secret")
    assert encoded.startswith(START_MARKER)
    assert encoded.endswith(END_MARKER)
    assert ZWSP in encoded or ZWNJ in encoded
    
    # Test without password
    encoded = encode_message(message)
    assert encoded.startswith(START_MARKER)
    assert encoded.endswith(END_MARKER)
    assert ZWSP in encoded or ZWNJ in encoded

def test_insert_payload() -> None:
    """Test payload insertion."""
    carrier = "Hello world"
    payload = f"{START_MARKER}{ZWSP}{ZWNJ}{END_MARKER}"
    
    # Test insertion at end
    result = insert_payload(carrier, payload)
    assert result == f"{carrier}{payload}"
    
    # Test insertion at position
    result = insert_payload(carrier, payload, 5)
    assert result == f"Hello{payload} world"
    
    # Test invalid carrier
    with pytest.raises(ValueError, match="contains control characters"):
        insert_payload(f"Hello{START_MARKER}world", payload)
    
    # Test invalid position
    with pytest.raises(ValueError, match="Invalid insertion position"):
        insert_payload(carrier, payload, -1)
    with pytest.raises(ValueError, match="Invalid insertion position"):
        insert_payload(carrier, payload, len(carrier) + 1)

def test_encode_and_insert() -> None:
    """Test encode and insert functionality."""
    message = "Hello, 世界! 👋"
    carrier = "The quick brown fox"
    
    # Test with password
    result = encode_and_insert(message, carrier, "secret")
    assert result.startswith(carrier)
    assert START_MARKER in result
    assert END_MARKER in result
    
    # Test without password
    result = encode_and_insert(message, carrier)
    assert result.startswith(carrier)
    assert START_MARKER in result
    assert END_MARKER in result
    
    # Test with position
    result = encode_and_insert(message, carrier, "secret", 4)
    assert result.startswith("The ")
    assert START_MARKER in result
    assert END_MARKER in result
    
    # Test invalid carrier
    with pytest.raises(ValueError):
        encode_and_insert(message, f"Hello{START_MARKER}world", "secret")
    
    # Test invalid position
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier, "secret", -1)
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier, "secret", len(carrier) + 1) 