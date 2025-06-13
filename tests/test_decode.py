"""Tests for the decode module.

This module contains tests for steganographic decoding functionality.
"""

import pytest
from whitespace_stego.decode import (
    extract_payload,
    decode_binary,
    binary_to_base64,
    decode_message,
    decode_and_remove
)
from whitespace_stego.common.charset import START_MARKER, END_MARKER, ZWSP, ZWNJ
from whitespace_stego.encode import encode_message
import logging

logging.basicConfig(level=logging.DEBUG)

def test_extract_payload() -> None:
    """Test payload extraction."""
    logging.debug(f"Running {__name__}.test_extract_payload")
    # Valid payload
    text = f"Hello{START_MARKER}{ZWSP}{ZWNJ}{END_MARKER}world"
    payload, start_pos, end_pos = extract_payload(text)
    assert payload == f"{ZWSP}{ZWNJ}"
    assert start_pos == 5
    assert end_pos == 8
    
    # No start marker
    with pytest.raises(ValueError, match="No start marker found"):
        extract_payload("Hello world")
    
    # No end marker
    with pytest.raises(ValueError, match="No end marker found"):
        extract_payload(f"Hello{START_MARKER}world")

def test_decode_binary() -> None:
    """Test binary decoding."""
    logging.debug(f"Running {__name__}.test_decode_binary")
    # Valid binary
    encoded = f"{ZWSP}{ZWNJ}{ZWSP}"
    binary = decode_binary(encoded)
    assert binary == "010"
    
    # Invalid character
    with pytest.raises(ValueError, match="Invalid character"):
        decode_binary("invalid")

def test_binary_to_base64() -> None:
    """Test binary to base64 conversion."""
    logging.debug(f"Running {__name__}.test_binary_to_base64")
    # Valid binary (8 bits = 1 byte)
    binary = "01000001"  # ASCII 'A'
    base64_bytes = binary_to_base64(binary)
    assert base64_bytes == b'A'
    
    # Invalid length
    with pytest.raises(ValueError, match="must be a multiple of 8"):
        binary_to_base64("01")

def test_decode_message() -> None:
    """Test message decoding."""
    logging.debug(f"Running {__name__}.test_decode_message")
    # Test with password
    message = "Hello, 世界! 👋"
    password = "secret"
    encoded = encode_message(message, password)
    decoded = decode_message(encoded, password)
    assert decoded == message

    # Test without password
    encoded = encode_message(message)
    decoded = decode_message(encoded)
    assert decoded == message

    # Test invalid payload
    with pytest.raises(ValueError):
        decode_message("invalid")

def test_decode_and_remove() -> None:
    """Test decode and remove functionality."""
    logging.debug(f"Running {__name__}.test_decode_and_remove")
    carrier = "Hello world"
    message = "Secret message"
    password = "secret"
    # With password
    payload = encode_message(message, password)
    encoded = carrier + payload
    decoded_message, decoded_carrier = decode_and_remove(encoded, password)
    assert decoded_message == message
    assert decoded_carrier == carrier

    # Without password
    payload = encode_message(message)
    encoded = carrier + payload
    decoded_message, decoded_carrier = decode_and_remove(encoded)
    assert decoded_message == message
    assert decoded_carrier == carrier

    # Test invalid payload
    with pytest.raises(ValueError):
        decode_and_remove("invalid") 