import base64
from typing import Optional

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

def encode_message(message: str, carrier: str, password: Optional[str] = None) -> str:
    """
    Encode a message into carrier text using zero-width Unicode characters.
    
    Args:
        message: The message to encode
        carrier: The carrier text to encode into (can be empty)
        password: Optional password for encryption
        
    Returns:
        The encoded carrier text with the message hidden using zero-width characters
    """
    # Convert message to base64 for binary-safe encoding
    message_bytes = message.encode('utf-8')
    message_b64 = base64.b64encode(message_bytes).decode('utf-8')
    
    # If password is provided, use it to encrypt the base64 message
    if password:
        # Simple XOR encryption with password
        password_bytes = password.encode('utf-8')
        encrypted = bytearray()
        for i, b in enumerate(message_bytes):
            encrypted.append(b ^ password_bytes[i % len(password_bytes)])
        message_b64 = base64.b64encode(encrypted).decode('utf-8')
    
    # Convert base64 to binary string
    binary = ''.join(format(ord(c), '08b') for c in message_b64)
    
    # Add length prefix (32 bits) to know how many bits to decode
    length_binary = format(len(binary), '032b')
    binary = length_binary + binary
    
    # Encode binary data into zero-width characters
    encoded_data = ''.join(ONE_BIT if bit == '1' else ZERO_BIT for bit in binary)
    
    # Add start and end markers
    encoded_message = START_MARKER + encoded_data + END_MARKER
    
    # Handle zero-length carrier case
    if not carrier:
        return encoded_message
    
    # For non-zero carrier, insert after first character
    if len(carrier) == 1:
        return carrier + encoded_message
    return carrier[0] + encoded_message + carrier[1:] 