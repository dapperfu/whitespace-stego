"""Steganographic decoding module for extracting hidden messages.

This module provides functions for extracting and decoding messages
hidden in text using zero-width Unicode characters.
"""

import base64
from typing import Optional, Tuple
from common.charset import (
    START_MARKER, END_MARKER, CHAR_TO_BINARY,
    is_valid_carrier
)
from .crypto import decrypt_message

def extract_payload(text: str) -> Tuple[str, int, int]:
    """Extract the steganographic payload from text.
    
    Parameters
    ----------
    text : str
        The text containing the hidden payload.
        
    Returns
    -------
    Tuple[str, int, int]
        A tuple containing (payload, start_pos, end_pos)
        
    Raises
    ------
    ValueError
        If no valid payload is found in the text.
    """
    start_pos = text.find(START_MARKER)
    if start_pos == -1:
        raise ValueError("No start marker found in text")
        
    end_pos = text.find(END_MARKER, start_pos)
    if end_pos == -1:
        raise ValueError("No end marker found in text")
        
    payload = text[start_pos + 1:end_pos]
    return payload, start_pos, end_pos

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
    try:
        return ''.join(str(CHAR_TO_BINARY[char]) for char in encoded)
    except KeyError as e:
        raise ValueError(f"Invalid character in encoded string: {e}")

def binary_to_base64(binary: str) -> str:
    """Convert a binary string to base64.
    
    Parameters
    ----------
    binary : str
        A string of '0's and '1's representing base64 characters.
        
    Returns
    -------
    str
        The decoded base64 string.
        
    Raises
    ------
    ValueError
        If the binary string length is not a multiple of 8.
    """
    if len(binary) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
        
    # Convert binary to bytes
    bytes_data = bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))
    
    # Convert bytes to base64 string
    return bytes_data.decode()

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
    # Extract the payload
    payload, _, _ = extract_payload(text)
    
    # Decode binary
    binary = decode_binary(payload)
    
    # Convert to base64
    base64_str = binary_to_base64(binary)
    
    # Decrypt/Decode the message
    return decrypt_message(base64_str, password)

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
    # Extract payload and positions
    payload, start_pos, end_pos = extract_payload(text)
    
    # Decode the message
    message = decode_message(text, password)
    
    # Remove the payload from the text
    carrier = text[:start_pos] + text[end_pos + 1:]
    
    return message, carrier 