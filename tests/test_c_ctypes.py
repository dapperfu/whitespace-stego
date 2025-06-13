"""Tests for the C backend using ctypes."""

import os
import pytest
import ctypes
from typing import Optional, Tuple

# Load the shared library
LIB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                       "c_backend/lib/libwhitespace_stego.so")

try:
    lib = ctypes.CDLL(LIB_PATH)
except OSError:
    pytest.skip("C shared library not found. Run 'make shared' in c_backend directory first.")

# Define function signatures
lib.encode_message.argtypes = [
    ctypes.c_char_p,  # message
    ctypes.c_char_p,  # carrier
    ctypes.c_char_p,  # password (can be NULL)
    ctypes.c_char_p,  # output buffer
    ctypes.c_size_t,  # output buffer size
]
lib.encode_message.restype = ctypes.c_int

lib.decode_message.argtypes = [
    ctypes.c_char_p,  # encoded message
    ctypes.c_char_p,  # password (can be NULL)
    ctypes.c_char_p,  # output buffer
    ctypes.c_size_t,  # output buffer size
]
lib.decode_message.restype = ctypes.c_int

lib.insert_payload.argtypes = [
    ctypes.c_char_p,  # carrier
    ctypes.c_char_p,  # payload
    ctypes.c_size_t,  # position
    ctypes.c_char_p,  # output buffer
    ctypes.c_size_t,  # output buffer size
]
lib.insert_payload.restype = ctypes.c_int

lib.decode_and_remove.argtypes = [
    ctypes.c_char_p,  # encoded text
    ctypes.c_char_p,  # password (can be NULL)
    ctypes.c_char_p,  # message output buffer
    ctypes.c_size_t,  # message buffer size
    ctypes.c_char_p,  # carrier output buffer
    ctypes.c_size_t,  # carrier buffer size
]
lib.decode_and_remove.restype = ctypes.c_int

@pytest.fixture
def c_lib():
    """Fixture to provide the C library."""
    return lib

def test_encode_decode_message(c_lib):
    """Test basic message encoding and decoding."""
    message = b"Hello, World!"
    carrier = b"A" * 1000
    password = None
    
    # Encode
    output_size = 2000
    output = ctypes.create_string_buffer(output_size)
    result = c_lib.encode_message(message, carrier, password, output, output_size)
    assert result == 0
    
    # Decode
    decoded_size = 1000
    decoded = ctypes.create_string_buffer(decoded_size)
    result = c_lib.decode_message(output, password, decoded, decoded_size)
    assert result == 0
    assert decoded.value == message

def test_encode_decode_with_password(c_lib):
    """Test message encoding and decoding with password."""
    message = b"Secret message"
    carrier = b"A" * 1000
    password = b"test123"
    
    # Encode
    output_size = 2000
    output = ctypes.create_string_buffer(output_size)
    result = c_lib.encode_message(message, carrier, password, output, output_size)
    assert result == 0
    
    # Decode
    decoded_size = 1000
    decoded = ctypes.create_string_buffer(decoded_size)
    result = c_lib.decode_message(output, password, decoded, decoded_size)
    assert result == 0
    assert decoded.value == message

def test_insert_payload(c_lib):
    """Test payload insertion."""
    carrier = b"This is a test message."
    payload = b"Hidden payload"
    position = 5
    
    output_size = 1000
    output = ctypes.create_string_buffer(output_size)
    result = c_lib.insert_payload(carrier, payload, position, output, output_size)
    assert result == 0
    
    # Verify the result
    result_str = output.value
    assert result_str[:position] == carrier[:position]
    assert result_str[position:position + len(payload)] == payload
    assert result_str[position + len(payload):] == carrier[position:]

def test_decode_and_remove(c_lib):
    """Test decoding and removing payload."""
    message = b"Hidden message"
    carrier = b"This is a test message."
    password = None
    
    # First encode and insert
    encoded_size = 2000
    encoded = ctypes.create_string_buffer(encoded_size)
    result = c_lib.encode_message(message, carrier, password, encoded, encoded_size)
    assert result == 0
    
    # Then decode and remove
    message_size = 1000
    carrier_size = 1000
    decoded_message = ctypes.create_string_buffer(message_size)
    decoded_carrier = ctypes.create_string_buffer(carrier_size)
    
    result = c_lib.decode_and_remove(
        encoded, password,
        decoded_message, message_size,
        decoded_carrier, carrier_size
    )
    assert result == 0
    assert decoded_message.value == message
    assert decoded_carrier.value == carrier

def test_invalid_carrier(c_lib):
    """Test invalid carrier text."""
    carrier = b"This is a test message with \xe2\x81\xa0 control character."
    message = b"Hidden message"
    output_size = 2000
    output = ctypes.create_string_buffer(output_size)
    
    result = c_lib.encode_message(message, carrier, None, output, output_size)
    assert result != 0  # Should return error

def test_buffer_overflow(c_lib):
    """Test buffer overflow protection."""
    message = b"Hello, World!"
    carrier = b"A" * 1000
    output_size = 10  # Too small buffer
    output = ctypes.create_string_buffer(output_size)
    
    result = c_lib.encode_message(message, carrier, None, output, output_size)
    assert result != 0  # Should return error 