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
    ctypes.c_size_t,  # message_len
    ctypes.c_char_p,  # carrier
    ctypes.c_size_t,  # carrier_len
    ctypes.c_char_p,  # output
    ctypes.c_size_t,  # output_len
    ctypes.c_char_p,  # password (can be NULL)
    ctypes.c_size_t,  # password_len
]
lib.encode_message.restype = ctypes.c_size_t

lib.decode_message.argtypes = [
    ctypes.c_char_p,  # input
    ctypes.c_size_t,  # input_len
    ctypes.c_char_p,  # output
    ctypes.c_size_t,  # output_len
    ctypes.c_char_p,  # password (can be NULL)
    ctypes.c_size_t,  # password_len
]
lib.decode_message.restype = ctypes.c_size_t

lib.calculate_encoded_size.argtypes = [
    ctypes.c_size_t,  # message_len
    ctypes.c_size_t,  # carrier_len
]
lib.calculate_encoded_size.restype = ctypes.c_size_t

lib.calculate_decoded_size.argtypes = [
    ctypes.c_size_t,  # input_len
]
lib.calculate_decoded_size.restype = ctypes.c_size_t

@pytest.fixture
def c_lib():
    """Fixture to provide the C library."""
    return lib

def test_encode_decode_message(c_lib):
    """Test basic message encoding and decoding."""
    message = b"Hello, World!"
    carrier = b"A" * 1000
    password = None
    
    # Calculate required buffer size
    output_size = c_lib.calculate_encoded_size(len(message), len(carrier))
    assert output_size > 0
    
    # Encode
    output = ctypes.create_string_buffer(output_size)
    encoded_len = c_lib.encode_message(
        message, len(message),
        carrier, len(carrier),
        output, output_size,
        password, 0
    )
    assert encoded_len > 0
    
    # Calculate decoded size
    decoded_size = c_lib.calculate_decoded_size(encoded_len)
    assert decoded_size > 0
    
    # Decode
    decoded = ctypes.create_string_buffer(decoded_size)
    decoded_len = c_lib.decode_message(
        output, encoded_len,
        decoded, decoded_size,
        password, 0
    )
    assert decoded_len > 0
    assert decoded.value[:decoded_len] == message

def test_encode_decode_with_password(c_lib):
    """Test message encoding and decoding with password."""
    message = b"Secret message"
    carrier = b"A" * 1000
    password = b"test123"
    
    # Calculate required buffer size
    output_size = c_lib.calculate_encoded_size(len(message), len(carrier))
    assert output_size > 0
    
    # Encode
    output = ctypes.create_string_buffer(output_size)
    encoded_len = c_lib.encode_message(
        message, len(message),
        carrier, len(carrier),
        output, output_size,
        password, len(password)
    )
    assert encoded_len > 0
    
    # Calculate decoded size
    decoded_size = c_lib.calculate_decoded_size(encoded_len)
    assert decoded_size > 0
    
    # Decode
    decoded = ctypes.create_string_buffer(decoded_size)
    decoded_len = c_lib.decode_message(
        output, encoded_len,
        decoded, decoded_size,
        password, len(password)
    )
    assert decoded_len > 0
    assert decoded.value[:decoded_len] == message

def test_invalid_carrier(c_lib):
    """Test invalid carrier text."""
    carrier = b"This is a test message with \xe2\x81\xa0 control character."
    message = b"Hidden message"
    
    # Calculate required buffer size
    output_size = c_lib.calculate_encoded_size(len(message), len(carrier))
    assert output_size > 0
    
    # Try to encode
    output = ctypes.create_string_buffer(output_size)
    encoded_len = c_lib.encode_message(
        message, len(message),
        carrier, len(carrier),
        output, output_size,
        None, 0
    )
    assert encoded_len == 0  # Should return error

def test_buffer_overflow(c_lib):
    """Test buffer overflow protection."""
    message = b"Hello, World!"
    carrier = b"A" * 1000
    output_size = 10  # Too small buffer
    output = ctypes.create_string_buffer(output_size)
    
    encoded_len = c_lib.encode_message(
        message, len(message),
        carrier, len(carrier),
        output, output_size,
        None, 0
    )
    assert encoded_len == 0  # Should return error 