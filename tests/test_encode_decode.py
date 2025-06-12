"""Tests for the core encoding and decoding functionality."""

import pytest
from whitespace_stego.encode import encode_and_insert
from whitespace_stego.decode import decode_and_remove

def test_basic_encode_decode() -> None:
    """Test basic encoding and decoding without password."""
    message = "Hello, World!"
    carrier = "This is a test message."
    
    # Encode the message
    encoded = encode_and_insert(message, carrier)
    
    # Decode the message
    decoded_message, decoded_carrier = decode_and_remove(encoded)
    
    assert decoded_message == message
    assert decoded_carrier == carrier

def test_password_protection() -> None:
    """Test encoding and decoding with password protection."""
    message = "Secret message"
    carrier = "Public text"
    password = "test123"
    
    # Encode with password
    encoded = encode_and_insert(message, carrier, password=password)
    
    # Try decoding without password (should fail)
    with pytest.raises(ValueError):
        decode_and_remove(encoded)
    
    # Decode with correct password
    decoded_message, decoded_carrier = decode_and_remove(encoded, password=password)
    
    assert decoded_message == message
    assert decoded_carrier == carrier

def test_custom_position() -> None:
    """Test encoding with custom position."""
    message = "Hidden"
    carrier = "Hello World"
    position = 5
    
    # Encode at specific position
    encoded = encode_and_insert(message, carrier, position=position)
    
    # Decode
    decoded_message, decoded_carrier = decode_and_remove(encoded)
    
    assert decoded_message == message
    assert decoded_carrier == carrier

def test_empty_carrier() -> None:
    """Test encoding with empty carrier text."""
    message = "Test message"
    carrier = ""
    
    # Encode
    encoded = encode_and_insert(message, carrier)
    
    # Decode
    decoded_message, decoded_carrier = decode_and_remove(encoded)
    
    assert decoded_message == message
    assert decoded_carrier == carrier

def test_invalid_carrier() -> None:
    """Test encoding with invalid carrier text."""
    message = "Test message"
    carrier = "Hello\u2060World"  # Contains control character
    
    # Should raise ValueError
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier)

def test_invalid_position() -> None:
    """Test encoding with invalid position."""
    message = "Test message"
    carrier = "Hello World"
    
    # Should raise ValueError for negative position
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier, position=-1)
    
    # Should raise ValueError for position beyond carrier length
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier, position=len(carrier) + 1) 