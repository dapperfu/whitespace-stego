"""Core functionality for zero-width whitespace steganography.

This module provides the core functionality for encoding and decoding messages
using zero-width Unicode characters as a steganographic carrier.
"""

import base64
from typing import Optional, Tuple

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Unicode characters used for encoding
ZERO_WIDTH_SPACE = "\u200B"  # 0
ZERO_WIDTH_NON_JOINER = "\u200C"  # 1
WORD_JOINER = "\u2060"  # Start delimiter
FUNCTION_APPLICATION = "\u2061"  # End delimiter

def _derive_key(password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """Derive an encryption key from a password using PBKDF2.
    
    Args:
        password: The password to derive the key from
        salt: Optional salt for key derivation. If None, a new salt is generated.
        
    Returns:
        A tuple of (key, salt) where key is the derived key and salt is the used salt.
    """
    if salt is None:
        salt = b"whitespace_stego_salt"  # In production, use a random salt
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def _encrypt_message(message: str, password: Optional[str] = None) -> str:
    """Encrypt a message using AES-256 if a password is provided.
    
    Args:
        message: The message to encrypt
        password: Optional password for encryption
        
    Returns:
        The encrypted and base64-encoded message
    """
    if not password:
        return base64.b64encode(message.encode()).decode()
    
    key, _ = _derive_key(password)
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def _decrypt_message(encrypted_message: str, password: Optional[str] = None) -> str:
    """Decrypt a message using AES-256 if a password is provided.
    
    Args:
        encrypted_message: The encrypted and base64-encoded message
        password: Optional password for decryption
        
    Returns:
        The decrypted message
    """
    if not password:
        return base64.b64decode(encrypted_message.encode()).decode()
    
    key, _ = _derive_key(password)
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

def _binary_to_zero_width(binary: str) -> str:
    """Convert a binary string to zero-width characters.
    
    Args:
        binary: A string of 0s and 1s
        
    Returns:
        A string of zero-width characters
    """
    return binary.replace("0", ZERO_WIDTH_SPACE).replace("1", ZERO_WIDTH_NON_JOINER)

def _zero_width_to_binary(zero_width: str) -> str:
    """Convert zero-width characters back to binary.
    
    Args:
        zero_width: A string of zero-width characters
        
    Returns:
        A string of 0s and 1s
    """
    return zero_width.replace(ZERO_WIDTH_SPACE, "0").replace(ZERO_WIDTH_NON_JOINER, "1")

def encode(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode a message into a carrier text using zero-width characters.
    
    Args:
        message: The message to encode
        carrier: The carrier text to embed the message in
        password: Optional password for encryption
        
    Returns:
        The carrier text with the encoded message embedded
    """
    # Encrypt and encode the message
    encrypted = _encrypt_message(message, password)
    binary = "".join(format(ord(c), "08b") for c in encrypted)
    zero_width = _binary_to_zero_width(binary)
    
    # Frame the encoded message
    framed = f"{WORD_JOINER}{zero_width}{FUNCTION_APPLICATION}"
    
    # Insert after first character if carrier exists
    if carrier:
        return carrier[0] + framed + carrier[1:]
    return framed

def decode(carrier: str, password: Optional[str] = None) -> str:
    """Decode a message from carrier text.
    
    Args:
        carrier: The carrier text containing the encoded message
        password: Optional password for decryption
        
    Returns:
        The decoded message
        
    Raises:
        ValueError: If no valid message is found in the carrier
    """
    # Find the framed message
    start = carrier.find(WORD_JOINER)
    end = carrier.find(FUNCTION_APPLICATION)
    
    if start == -1 or end == -1 or start >= end:
        raise ValueError("No valid message found in carrier")
    
    # Extract and decode the message
    zero_width = carrier[start + 1:end]
    binary = _zero_width_to_binary(zero_width)
    
    # Convert binary back to string
    encrypted = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]
        encrypted += chr(int(byte, 2))
    
    return _decrypt_message(encrypted, password) 