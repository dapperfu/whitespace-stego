"""Tests for the Rust bridge implementation."""

import pytest
from whitespace_stego.rust_bridge import (
    encode_binary,
    encode_message,
    insert_payload,
    encode_and_insert,
    decode_binary,
    decode_message,
    decode_and_remove,
    RUST_AVAILABLE
)

pytestmark = pytest.mark.skipif(not RUST_AVAILABLE, reason="Rust module not available")

def test_encode_decode_binary():
    """Test binary encoding and decoding."""
    binary = "01010101"
    encoded = encode_binary(binary)
    decoded = decode_binary(encoded)
    assert decoded == binary

def test_encode_decode_message():
    """Test message encoding and decoding."""
    message = "Hello, World!"
    encoded = encode_message(message)
    decoded = decode_message(encoded)
    assert decoded == message

def test_encode_decode_message_with_password():
    """Test message encoding and decoding with password."""
    message = "Secret message"
    password = "test123"
    encoded = encode_message(message, password)
    decoded = decode_message(encoded, password)
    assert decoded == message

def test_insert_payload():
    """Test payload insertion."""
    carrier = "This is a test message."
    payload = "Hidden payload"
    position = 5
    result = insert_payload(carrier, payload, position)
    assert result[:position] == carrier[:position]
    assert result[position:position + len(payload)] == payload
    assert result[position + len(payload):] == carrier[position:]

def test_encode_and_insert():
    """Test message encoding and insertion."""
    message = "Hidden message"
    carrier = "This is a test message."
    result = encode_and_insert(message, carrier)
    decoded, carrier_out = decode_and_remove(result)
    assert decoded == message
    assert carrier_out == carrier

def test_encode_and_insert_with_password():
    """Test message encoding and insertion with password."""
    message = "Secret message"
    carrier = "This is a test message."
    password = "test123"
    result = encode_and_insert(message, carrier, password)
    decoded, carrier_out = decode_and_remove(result, password)
    assert decoded == message
    assert carrier_out == carrier

def test_invalid_carrier():
    """Test invalid carrier text."""
    carrier = "This is a test message with \u2060 control character."
    message = "Hidden message"
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier)

def test_invalid_position():
    """Test invalid insertion position."""
    carrier = "This is a test message."
    message = "Hidden message"
    with pytest.raises(ValueError):
        encode_and_insert(message, carrier, position=100)

def test_unicode_support():
    """Test Unicode support."""
    message = "Hello, 世界! 👋"
    carrier = "This is a test message."
    result = encode_and_insert(message, carrier)
    decoded, carrier_out = decode_and_remove(result)
    assert decoded == message
    assert carrier_out == carrier 