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

def decode_message(encoded_text: str, password: Optional[str] = None) -> str:
    """
    Decode a message from text containing zero-width Unicode steganography.
    
    Args:
        encoded_text: The text containing the hidden message
        password: Optional password for decryption
        
    Returns:
        The decoded message
        
    Raises:
        ValueError: If no valid message is found or if the message is corrupted
    """
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
        message = base64.b64decode(message_bytes).decode('utf-8')
        return message
    except Exception as e:
        raise ValueError(f"Failed to decode message: {str(e)}") 