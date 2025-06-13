"""Cryptographic utilities for password-protected steganography.

This module provides functions for encrypting and decrypting messages
using AES-256 with password-based key derivation.
"""

import base64
from typing import Optional, Tuple
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Constants for key derivation
SALT_LENGTH: int = 16
KEY_LENGTH: int = 32  # 256 bits
ITERATIONS: int = 100000

def derive_key(password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """Derive an encryption key from a password using PBKDF2.
    
    Parameters
    ----------
    password : str
        The password to derive the key from.
    salt : Optional[bytes]
        Optional salt for key derivation. If None, a new salt is generated.
        
    Returns
    -------
    Tuple[bytes, bytes]
        A tuple containing (key, salt)
    """
    if salt is None:
        salt = os.urandom(SALT_LENGTH)
        
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    
    key = kdf.derive(password.encode())
    return key, salt

def encrypt_message(message: str, password: Optional[str] = None) -> str:
    """Encrypt a message with optional password protection.
    
    Parameters
    ----------
    message : str
        The message to encrypt.
    password : Optional[str]
        Optional password for encryption. If None, message is only base64 encoded.
        
    Returns
    -------
    str
        The encrypted and base64-encoded message.
        
    Notes
    -----
    If no password is provided, the message is only base64 encoded.
    If a password is provided, the message is encrypted with AES-256-GCM
    before being base64 encoded.
    """
    if password is None:
        return base64.b64encode(message.encode()).decode()
        
    # Generate a random IV
    iv = os.urandom(12)
    
    # Derive key and get salt
    key, salt = derive_key(password)
    
    # Create cipher
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # Encrypt the message
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    
    # Combine salt + iv + tag + ciphertext and base64 encode
    encrypted_data = salt + iv + encryptor.tag + ciphertext
    return base64.b64encode(encrypted_data).decode()

def decrypt_message(encrypted_message: str, password: Optional[str] = None) -> str:
    """Decrypt a message that was encrypted with optional password protection.
    
    Parameters
    ----------
    encrypted_message : str
        The base64-encoded encrypted message.
    password : Optional[str]
        Optional password for decryption. If None, message is only base64 decoded.
        
    Returns
    -------
    str
        The decrypted message.
        
    Raises
    ------
    ValueError
        If decryption fails or the message format is invalid.
    """
    try:
        if password is None:
            return base64.b64decode(encrypted_message.encode()).decode('utf-8')
            
        # Decode the base64 message
        encrypted_data = base64.b64decode(encrypted_message.encode())
        
        # Extract salt, iv, tag, and ciphertext
        salt = encrypted_data[:SALT_LENGTH]
        iv = encrypted_data[SALT_LENGTH:SALT_LENGTH + 12]
        tag = encrypted_data[SALT_LENGTH + 12:SALT_LENGTH + 28]
        ciphertext = encrypted_data[SALT_LENGTH + 28:]
        
        # Derive key using the stored salt
        key, _ = derive_key(password, salt)
        
        # Create cipher
        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(iv, tag),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        
        # Decrypt the message
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
        
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}") 