"""Core implementation of whitespace steganography.

This module provides the core functionality for encoding and decoding messages
using zero-width Unicode whitespace characters.
"""

import base64
from typing import Optional, Tuple

# Zero-width characters for encoding
START_MARKER = "\u200B"  # Zero-width space
END_MARKER = "\u200C"    # Zero-width non-joiner
ZERO_BIT = "\u200D"      # Zero-width joiner
ONE_BIT = "\uFEFF"       # Zero-width no-break space

def _encode_binary(data: bytes) -> str:
    """Convert bytes to a string of zero-width characters.
    
    Parameters
    ----------
    data : bytes
        The binary data to encode.
        
    Returns
    -------
    str
        A string containing zero-width characters representing the binary data.
    """
    binary = ''.join(format(byte, '08b') for byte in data)
    return ''.join(ONE_BIT if bit == '1' else ZERO_BIT for bit in binary)

def _decode_binary(encoded: str) -> bytes:
    """Convert a string of zero-width characters back to bytes.
    
    Parameters
    ----------
    encoded : str
        The string containing zero-width characters.
        
    Returns
    -------
    bytes
        The decoded binary data.
    """
    binary = ''.join('1' if char == ONE_BIT else '0' for char in encoded)
    return bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))

def encode(message: str, carrier: str = "", password: Optional[str] = None) -> str:
    """Encode a message into a carrier text using zero-width characters.
    
    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str, optional
        The carrier text to embed the message in. If empty, returns just the encoded message.
    password : str, optional
        Optional password for encryption.
        
    Returns
    -------
    str
        The carrier text with the encoded message embedded.
    """
    # Base64 encode the message
    encoded = base64.b64encode(message.encode('utf-8'))
    
    # Add password encryption if provided
    if password:
        from cryptography.fernet import Fernet
        key = base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])
        f = Fernet(key)
        encoded = f.encrypt(encoded)
    
    # Convert to zero-width characters
    zero_width = _encode_binary(encoded)
    
    # Add markers
    encoded_message = START_MARKER + zero_width + END_MARKER
    
    # Return just the encoded message if no carrier
    if not carrier:
        return encoded_message
    
    # Embed in carrier after first Unicode character
    chars = list(carrier)
    if len(chars) > 1:
        return chars[0] + encoded_message + ''.join(chars[1:])
    else:
        return carrier + encoded_message

def decode(carrier: str, password: Optional[str] = None) -> str:
    """Decode a message from carrier text containing zero-width characters.
    
    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded message.
    password : str, optional
        Optional password for decryption.
        
    Returns
    -------
    str
        The decoded message.
        
    Raises
    ------
    ValueError
        If no valid message is found in the carrier text.
    """
    # Find the encoded message between markers
    start = carrier.find(START_MARKER)
    end = carrier.find(END_MARKER)
    
    if start == -1 or end == -1:
        raise ValueError("No valid message found in carrier text")
    
    # Extract the encoded message
    encoded = carrier[start + 1:end]
    
    # Convert from zero-width characters to bytes
    data = _decode_binary(encoded)
    
    # Decrypt if password provided
    if password:
        from cryptography.fernet import Fernet, InvalidToken
        key = base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])
        f = Fernet(key)
        try:
            data = f.decrypt(data)
        except InvalidToken:
            raise ValueError("Invalid password or corrupted data")
    
    # Base64 decode and convert to string
    try:
        return base64.b64decode(data).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Failed to decode message: {str(e)}")

def extract_encoded(carrier: str) -> Tuple[str, str]:
    """Extract the encoded message and remaining carrier text.
    
    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded message.
        
    Returns
    -------
    Tuple[str, str]
        A tuple containing (encoded_message, remaining_carrier)
        
    Raises
    ------
    ValueError
        If no valid message is found in the carrier text.
    """
    start = carrier.find(START_MARKER)
    end = carrier.find(END_MARKER)
    
    if start == -1 or end == -1:
        raise ValueError("No valid message found in carrier text")
    
    encoded = carrier[start:end + 1]
    remaining = carrier[:start] + carrier[end + 1:]
    
    return encoded, remaining 