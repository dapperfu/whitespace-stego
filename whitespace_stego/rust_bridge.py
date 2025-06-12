"""Python interface to Rust functions for whitespace steganography.

This module provides a Python interface to the Rust implementation
of the core encoding/decoding logic.
"""

from typing import Optional, Tuple, Union
import importlib.util
import os
import sys
from pathlib import Path

# Try to import the Rust module
try:
    import whitespace_stego_rs
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

def _get_rust_module() -> Optional[object]:
    """Get the Rust module if available.
    
    Returns
    -------
    Optional[object]
        The Rust module if available, None otherwise.
    """
    if not RUST_AVAILABLE:
        return None
        
    return whitespace_stego_rs

def encode_binary(binary_str: str) -> str:
    """Encode a binary string using zero-width characters.
    
    Parameters
    ----------
    binary_str : str
        A string of '0's and '1's to encode.
        
    Returns
    -------
    str
        The encoded string using zero-width characters.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.encode_binary_rs(binary_str)
    raise ImportError("Rust module not available")

def encode_message(message: str, password: Optional[str] = None) -> str:
    """Encode a message into a steganographic payload.
    
    Parameters
    ----------
    message : str
        The message to encode.
    password : Optional[str]
        Optional password for encryption before encoding.
        
    Returns
    -------
    str
        The encoded steganographic payload.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.encode_message_rs(message, password)
    raise ImportError("Rust module not available")

def insert_payload(carrier: str, payload: str, position: Optional[int] = None) -> str:
    """Insert a steganographic payload into carrier text.
    
    Parameters
    ----------
    carrier : str
        The carrier text to insert the payload into.
    payload : str
        The encoded steganographic payload.
    position : Optional[int]
        Position to insert the payload. If None, inserts at the end.
        
    Returns
    -------
    str
        The carrier text with the payload inserted.
        
    Raises
    ------
    ValueError
        If the carrier text contains control characters or
        if the position is invalid.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.insert_payload_rs(carrier, payload, position)
    raise ImportError("Rust module not available")

def encode_and_insert(
    message: str,
    carrier: str,
    password: Optional[str] = None,
    position: Optional[int] = None
) -> str:
    """Encode a message and insert it into carrier text.
    
    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str
        The carrier text to insert the encoded message into.
    password : Optional[str]
        Optional password for encryption.
    position : Optional[int]
        Position to insert the payload. If None, inserts at the end.
        
    Returns
    -------
    str
        The carrier text with the encoded message inserted.
        
    Raises
    ------
    ValueError
        If the carrier text contains control characters or
        if the position is invalid.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.encode_and_insert_rs(message, carrier, password, position)
    raise ImportError("Rust module not available")

def decode_binary(encoded: str) -> str:
    """Decode zero-width characters back to binary string.
    
    Parameters
    ----------
    encoded : str
        The encoded string using zero-width characters.
        
    Returns
    -------
    str
        The decoded binary string.
        
    Raises
    ------
    ValueError
        If the encoded string contains invalid characters.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.decode_binary_rs(encoded)
    raise ImportError("Rust module not available")

def decode_message(text: str, password: Optional[str] = None) -> str:
    """Decode a hidden message from text.
    
    Parameters
    ----------
    text : str
        The text containing the hidden message.
    password : Optional[str]
        Optional password for decryption.
        
    Returns
    -------
    str
        The decoded message.
        
    Raises
    ------
    ValueError
        If no valid payload is found or if decoding fails.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.decode_message_rs(text, password)
    raise ImportError("Rust module not available")

def decode_and_remove(text: str, password: Optional[str] = None) -> Tuple[str, str]:
    """Decode a hidden message and remove it from the carrier text.
    
    Parameters
    ----------
    text : str
        The text containing the hidden message.
    password : Optional[str]
        Optional password for decryption.
        
    Returns
    -------
    Tuple[str, str]
        A tuple containing (decoded_message, carrier_text)
        
    Raises
    ------
    ValueError
        If no valid payload is found or if decoding fails.
    """
    rust = _get_rust_module()
    if rust is not None:
        return rust.decode_and_remove_rs(text, password)
    raise ImportError("Rust module not available") 