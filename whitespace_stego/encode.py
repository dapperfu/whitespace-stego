"""Steganographic encoding module for hiding messages in text.

This module provides functions for encoding messages using zero-width
Unicode characters and inserting them into carrier text.
"""

import base64
from typing import Optional, Tuple
from .common.charset import (
    START_MARKER, END_MARKER, BINARY_TO_CHAR,
    is_valid_carrier
)
from .crypto import encrypt_message

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
    return ''.join(BINARY_TO_CHAR[int(bit)] for bit in binary_str)

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
        
    Raises
    ------
    ValueError
        If encoding fails.
    """
    if not message:
        raise ValueError("Message must not be empty")
        
    try:
        # First encrypt/encode the message
        encrypted = encrypt_message(message, password)
        
        # Convert to binary
        binary = ''.join(format(ord(c), '08b') for c in encrypted)
        
        # Encode binary using zero-width characters
        encoded = encode_binary(binary)
        
        # Wrap with control characters
        return f"{START_MARKER}{encoded}{END_MARKER}"
    except Exception as e:
        raise ValueError(f"Failed to encode message: {str(e)}")

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
    if not is_valid_carrier(carrier):
        raise ValueError("Carrier text contains control characters")
        
    if position is None:
        position = len(carrier)
    elif position < 0 or position > len(carrier):
        raise ValueError("Invalid insertion position")
        
    return carrier[:position] + payload + carrier[position:]

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
    payload = encode_message(message, password)
    return insert_payload(carrier, payload, position)

def encode(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode a message into carrier text.
    
    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str
        The carrier text to insert the encoded message into.
    password : Optional[str]
        Optional password for encryption.
        
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
    return encode_and_insert(message, carrier, password) 