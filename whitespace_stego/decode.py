"""Decode messages using whitespace steganography."""

from typing import Optional
import click
from whitespace_stego.core import decode as core_decode
import base64

# Zero-width Unicode characters for encoding
ZWSP = '\u200B'  # Zero-width space
ZWJ = '\u200D'   # Zero-width joiner
ZWNJ = '\u200C'  # Zero-width non-joiner
ZWNBSP = '\uFEFF'  # Zero-width no-break space

# Control characters for message boundaries
START_MARKER = ZWSP + ZWJ
END_MARKER = ZWNJ + ZWNBSP

# Data characters for binary encoding
ZERO_BIT = ZWSP
ONE_BIT = ZWJ

def decode_message(encoded_text: str, password: Optional[str] = None) -> str:
    """
    Decode a message from text containing whitespace steganography.
    
    Args:
        encoded_text: The text containing the hidden message
        password: Optional password for decryption
        
    Returns:
        The decoded message
        
    Raises:
        ValueError: If no valid message is found or if the message is corrupted
    """
    # Get the backend from CLI context
    ctx = click.get_current_context()
    backend = ctx.obj.get('backend', 'python') if ctx.obj else 'python'
    
    if backend == 'python':
        # Use the core Python implementation
        return core_decode(encoded_text, password)
    elif backend == 'rust':
        # Use the Rust backend
        from whitespace_stego_backend import decode as rust_decode
        return rust_decode(encoded_text, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")

def _decode_python(encoded_text: str, password: Optional[str] = None) -> str:
    """Original Python implementation."""
    # Find the start and end markers
    try:
        start_idx = encoded_text.index(START_MARKER)
        end_idx = encoded_text.index(END_MARKER, start_idx + len(START_MARKER))
    except ValueError:
        raise ValueError("No valid message found in the text")
    
    # Extract the encoded data between markers
    encoded_data = encoded_text[start_idx + len(START_MARKER):end_idx]
    
    # Convert zero-width characters back to binary
    binary = ''
    for char in encoded_data:
        if char == ONE_BIT:
            binary += '1'
        elif char == ZERO_BIT:
            binary += '0'
        else:
            # Skip any other characters that might be in the text
            continue
    
    if not binary:
        raise ValueError("No valid binary data found between markers")
    
    # Extract length prefix (first 32 bits)
    if len(binary) < 32:
        raise ValueError("Message is too short to contain valid length prefix")
    
    length_binary = binary[:32]
    message_length = int(length_binary, 2)
    
    # Verify we have enough bits for the message
    if len(binary) < 32 + message_length:
        raise ValueError("Message is truncated or corrupted")
    
    # Extract the message binary
    message_binary = binary[32:32 + message_length]
    
    # Verify message binary length is a multiple of 8 (valid for base64)
    if len(message_binary) % 8 != 0:
        raise ValueError("Message binary length is not a multiple of 8")
    
    # Convert binary string to bytes
    message_bytes = bytearray()
    for i in range(0, len(message_binary), 8):
        if i + 8 <= len(message_binary):
            byte = int(message_binary[i:i+8], 2)
            message_bytes.append(byte)
    
    try:
        # Decrypt if password was used
        if password:
            password_bytes = password.encode('utf-8')
            decrypted = bytearray()
            for i, b in enumerate(message_bytes):
                decrypted.append(b ^ password_bytes[i % len(password_bytes)])
            message_bytes = bytes(decrypted)
        
        # Decode base64 to get original message bytes
        try:
            decoded_bytes = base64.b64decode(message_bytes)
            message = decoded_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Failed to decode message: {str(e)}")
        return message
    except Exception as e:
        raise ValueError(f"Failed to decode message: {str(e)}") 