"""C backend for whitespace steganography using ctypes.

This module provides a Python interface to the C implementation of whitespace
steganography using ctypes to call the shared library functions.
"""

import ctypes
import ctypes.util
import os
import sys
from typing import Optional, Union, List
from pathlib import Path

from .logger import setup_logger

# Create logger instance
logger = setup_logger(__name__)

# Load the shared library
def _load_library():
    """Load the whitespace steganography shared library.
    
    Returns
    -------
    ctypes.CDLL
        The loaded shared library.
        
    Raises
    ------
    OSError
        If the library cannot be loaded.
    """
    # Try to find the library in common locations
    lib_paths = [
        # When installed via pip (bundled with package)
        Path(__file__).parent / "libwhitespace_stego.so",
        # Development environment (relative to current file)
        Path(__file__).parent.parent / "c" / "lib" / "libwhitespace_stego.so",
        # System library path
        "libwhitespace_stego.so",
        # With lib prefix
        "libwhitespace_stego",
    ]
    
    for lib_path in lib_paths:
        try:
            if isinstance(lib_path, Path):
                if lib_path.exists():
                    return ctypes.CDLL(str(lib_path))
            else:
                # Try ctypes.util.find_library for system paths
                found_lib = ctypes.util.find_library(lib_path)
                if found_lib:
                    return ctypes.CDLL(found_lib)
        except OSError:
            continue
    
    raise OSError("Could not find libwhitespace_stego.so. Please ensure the C library is built.")

# Load the library
try:
    _lib = _load_library()
    _C_BACKEND_AVAILABLE = True
except OSError as e:
    logger.warning(f"C backend not available: {e}")
    _C_BACKEND_AVAILABLE = False
    _lib = None

# Define function signatures
if _C_BACKEND_AVAILABLE:
    # whitespace_stego_encode
    _lib.whitespace_stego_encode.argtypes = [
        ctypes.c_char_p,  # carrier
        ctypes.c_size_t,  # carrier_len
        ctypes.c_char_p,  # message
        ctypes.c_char_p,  # password (can be NULL)
        ctypes.POINTER(ctypes.c_char_p),  # result
    ]
    _lib.whitespace_stego_encode.restype = ctypes.c_bool
    
    # whitespace_stego_decode
    _lib.whitespace_stego_decode.argtypes = [
        ctypes.c_char_p,  # carrier
        ctypes.c_size_t,  # carrier_len
        ctypes.c_char_p,  # password (can be NULL)
        ctypes.POINTER(ctypes.c_char_p),  # result
    ]
    _lib.whitespace_stego_decode.restype = ctypes.c_bool
    
    # whitespace_stego_decode_all
    _lib.whitespace_stego_decode_all.argtypes = [
        ctypes.c_char_p,  # carrier
        ctypes.c_size_t,  # carrier_len
        ctypes.c_char_p,  # password (can be NULL)
        ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),  # results
        ctypes.POINTER(ctypes.c_size_t),  # result_count
    ]
    _lib.whitespace_stego_decode_all.restype = ctypes.c_bool
    
    # whitespace_stego_free
    _lib.whitespace_stego_free.argtypes = [ctypes.c_char_p]
    _lib.whitespace_stego_free.restype = None
    
    # whitespace_stego_free_all
    _lib.whitespace_stego_free_all.argtypes = [
        ctypes.POINTER(ctypes.c_char_p),  # results
        ctypes.c_size_t,  # count
    ]
    _lib.whitespace_stego_free_all.restype = None
    
    # whitespace_stego_last_error
    _lib.whitespace_stego_last_error.restype = ctypes.c_char_p


def encode(message: str, carrier: str = "", password: Optional[str] = None) -> str:
    """Encode a message into carrier text using the C backend.
    
    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str, optional
        The carrier text to encode into. Defaults to empty string.
    password : str, optional
        Optional password for encryption. Defaults to None.
        
    Returns
    -------
    str
        The encoded carrier text with the message hidden.
        
    Raises
    ------
    RuntimeError
        If the C backend is not available or encoding fails.
    """
    if not _C_BACKEND_AVAILABLE:
        raise RuntimeError("C backend not available. Please ensure the C library is built.")
    
    # Convert strings to UTF-8 bytes
    carrier_bytes = carrier.encode('utf-8')
    message_bytes = message.encode('utf-8')
    password_bytes = password.encode('utf-8') if password else None
    
    # Prepare result pointer
    result_ptr = ctypes.c_char_p()
    
    # Call C function
    success = _lib.whitespace_stego_encode(
        carrier_bytes,
        len(carrier_bytes),
        message_bytes,
        password_bytes,
        ctypes.byref(result_ptr)
    )
    
    if not success:
        error_msg = _lib.whitespace_stego_last_error()
        if error_msg:
            error_str = error_msg.decode('utf-8')
        else:
            error_str = "Unknown encoding error"
        raise RuntimeError(f"Encoding failed: {error_str}")
    
    # Get result and convert back to string
    result = result_ptr.value.decode('utf-8')
    
    # Free the allocated memory
    _lib.whitespace_stego_free(result_ptr)
    
    return result


def decode(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode a message from carrier text using the C backend.
    
    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded message.
    password : str, optional
        Optional password for decryption. Defaults to None.
        
    Returns
    -------
    Union[str, List[str]]
        The decoded message(s). Returns a string for single message,
        list of strings for multiple messages.
        
    Raises
    ------
    RuntimeError
        If the C backend is not available or decoding fails.
    """
    if not _C_BACKEND_AVAILABLE:
        raise RuntimeError("C backend not available. Please ensure the C library is built.")
    
    # Convert strings to UTF-8 bytes
    carrier_bytes = carrier.encode('utf-8')
    password_bytes = password.encode('utf-8') if password else None
    
    # Try decode_all first to see if there are multiple messages
    results_ptr = ctypes.POINTER(ctypes.c_char_p)()
    result_count = ctypes.c_size_t()
    
    success = _lib.whitespace_stego_decode_all(
        carrier_bytes,
        len(carrier_bytes),
        password_bytes,
        ctypes.byref(results_ptr),
        ctypes.byref(result_count)
    )
    
    if success:
        if result_count.value > 0:
            # Multiple messages found
            messages = []
            for i in range(result_count.value):
                msg_ptr = results_ptr[i]
                if msg_ptr:
                    messages.append(msg_ptr.decode('utf-8'))
            
            # Free the allocated memory
            _lib.whitespace_stego_free_all(results_ptr, result_count.value)
            
            # Return string for single message, list for multiple
            if len(messages) == 1:
                return messages[0]
            else:
                return messages
        else:
            # decode_all succeeded but returned 0 messages
            # This happens in multi-recipient scenarios when the password can't decrypt any messages
            if password:
                # For multi-recipient scenarios with wrong password, return empty result
                # This matches Python's behavior
                return ""
            else:
                # No password and no messages found - this is an error
                error_msg = _lib.whitespace_stego_last_error()
                if error_msg:
                    error_str = error_msg.decode('utf-8')
                else:
                    error_str = "No valid messages found in carrier text"
                raise RuntimeError(f"Decoding failed: {error_str}")
    
    # Try single message decode
    result_ptr = ctypes.c_char_p()
    
    success = _lib.whitespace_stego_decode(
        carrier_bytes,
        len(carrier_bytes),
        password_bytes,
        ctypes.byref(result_ptr)
    )
    
    if not success:
        error_msg = _lib.whitespace_stego_last_error()
        if error_msg:
            error_str = error_msg.decode('utf-8')
        else:
            error_str = "Unknown decoding error"
        raise RuntimeError(f"Decoding failed: {error_str}")
    
    # Get result and convert back to string
    result = result_ptr.value.decode('utf-8')
    
    # Free the allocated memory
    _lib.whitespace_stego_free(result_ptr)
    
    return result


def is_available() -> bool:
    """Check if the C backend is available.
    
    Returns
    -------
    bool
        True if the C backend is available, False otherwise.
    """
    return _C_BACKEND_AVAILABLE


def count_messages(carrier: str) -> int:
    """Count the number of messages embedded in the carrier text.
    
    This function counts the number of complete start/end marker pairs,
    which represents the number of messages that have been embedded.
    
    Parameters
    ----------
    carrier : str
        The carrier text to analyze.
        
    Returns
    -------
    int
        The number of messages embedded in the carrier text.
    """
    if not _C_BACKEND_AVAILABLE:
        raise RuntimeError("C backend not available. Please ensure the C library is built.")
    
    # Use the same markers as the Python implementation
    START_MARKER = "\ufeff"  # Zero-width no-break space
    END_MARKER = "\u200c"    # Zero-width non-joiner
    
    start_count = carrier.count(START_MARKER)
    end_count = carrier.count(END_MARKER)
    return min(start_count, end_count) 