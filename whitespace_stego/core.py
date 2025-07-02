"""Core implementation of whitespace steganography.

This module provides the core functionality for encoding and decoding messages
using zero-width Unicode whitespace characters.
"""

import base64
import logging
from typing import Optional, Tuple
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from cryptography.hazmat.primitives import padding

from .logger import setup_logger

# Create logger instance
logger = setup_logger(__name__)

# Zero-width characters for encoding
ZERO_BIT = "\u200b"  # Zero-width space
ONE_BIT = "\u200d"   # Zero-width joiner
START_MARKER = "\ufeff"  # Zero-width no-break space
END_MARKER = "\u200c"    # Zero-width non-joiner


def _encode_binary(data: bytes) -> str:
    """Encode binary data into zero-width characters.

    Parameters
    ----------
    data : bytes
        The binary data to encode.

    Returns
    -------
    str
        The encoded binary data as zero-width characters.
    """
    binary = "".join(format(b, "08b") for b in data)
    return "".join(ONE_BIT if bit == "1" else ZERO_BIT for bit in binary)


def _decode_binary(encoded: str) -> bytes:
    """Decode zero-width characters back to binary data.

    Parameters
    ----------
    encoded : str
        The encoded binary data as zero-width characters.

    Returns
    -------
    bytes
        The decoded binary data.
    """
    binary = "".join("1" if char == ONE_BIT else "0" for char in encoded)
    return bytes(int(binary[i : i + 8], 2) for i in range(0, len(binary), 8))


def derive_key(password: str) -> bytes:
    """Derive a 32-byte key from password (same as C implementation).
    
    Parameters
    ----------
    password : str
        The password to derive the key from.
        
    Returns
    -------
    bytes
        A 32-byte key derived from the password.
    """
    # Convert password to UTF-8 bytes and hash to get consistent 32-byte key
    import hashlib
    password_bytes = password.encode('utf-8')
    key_hash = hashlib.sha256(password_bytes).digest()
    return key_hash


def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using AES-256-CBC with PKCS7 padding (same as C/Rust implementation).
    
    Parameters
    ----------
    data : bytes
        The data to encrypt.
    password : str
        The password to use for encryption.
        
    Returns
    -------
    bytes
        The encrypted data (IV + ciphertext).
    """
    key = derive_key(password)
    
    # Generate random IV
    iv = os.urandom(16)
    
    # Create cipher with PKCS7 padding (same as C/Rust)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # PKCS7 padder
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Encrypt with automatic PKCS7 padding
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return IV + ciphertext
    return iv + ciphertext


def decrypt_data(data: bytes, password: str) -> bytes:
    """Decrypt data using AES-256-CBC with PKCS7 padding (same as C/Rust implementation).
    
    Parameters
    ----------
    data : bytes
        The encrypted data (IV + ciphertext).
    password : str
        The password to use for decryption.
        
    Returns
    -------
    bytes
        The decrypted data.
    """
    if len(data) < 16:
        raise ValueError("Invalid encrypted data")
    
    key = derive_key(password)
    
    # Extract IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Create cipher with PKCS7 padding (same as C/Rust)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt with automatic PKCS7 padding removal
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # PKCS7 unpadder
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    return data


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
    # Check for empty message with humorous error
    if not message:
        raise ValueError("🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!")
    
    logger.debug("Encoding message: %s", message)
    logger.debug("Using carrier: %s", carrier)
    if password:
        logger.debug("Using password protection")

    # Base64 encode the message
    encoded = base64.b64encode(message.encode("utf-8"))

    # Add password encryption if provided
    if password:
        logger.debug("Using password protection")
        encoded = encrypt_data(encoded, password)

    # Convert to zero-width characters
    zero_width = _encode_binary(encoded)

    # Add markers
    encoded_message = START_MARKER + zero_width + END_MARKER

    # Return just the encoded message if no carrier
    if not carrier:
        logger.info("Message encoded successfully")
        return encoded_message

    # Embed in carrier after first Unicode character
    chars = list(carrier)
    if len(chars) > 1:
        result = chars[0] + encoded_message + "".join(chars[1:])
    else:
        result = carrier + encoded_message

    logger.info("Message encoded successfully")
    return result


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
    logger.debug("Decoding message from text: %s", carrier)
    if password:
        logger.debug("Using password protection")

    # Find the encoded message between markers
    start = carrier.find(START_MARKER)
    end = carrier.find(END_MARKER)
    
    # Check if both markers are found
    if start == -1 or end == -1:
        raise ValueError("No valid message found in carrier text")
    
    # Check if end marker comes after start marker
    if end <= start:
        raise ValueError("Invalid marker order in carrier text")
    
    print(f"[DEBUG] Python decode start: {start}, end: {end}")
    print(f"[DEBUG] Python decode bytes at start: {carrier[start:start+4].encode('utf-8')}")
    print(f"[DEBUG] Python decode bytes at end: {carrier[end:end+4].encode('utf-8')}")
    # Extract the encoded message
    encoded = carrier[start + len(START_MARKER) : end]
    print(f"[DEBUG] Python decode extracted encoded message: {repr(encoded)}")
    print(f"[DEBUG] Python decode extracted length: {len(encoded)}")
    print(f"[DEBUG] Python decode codepoints: {[hex(ord(c)) for c in encoded[:20]]}")
    binary = ''.join('1' if char == ONE_BIT else '0' for char in encoded)
    print(f"[DEBUG] Python decode binary string: {binary[:80]}")
    data = _decode_binary(encoded)

    # Decrypt if password provided
    if password:
        try:
            data = decrypt_data(data, password)
        except Exception as e:
            raise ValueError(f"Invalid password or corrupted data: {e}")

    # Base64 decode and convert to string
    try:
        result = base64.b64decode(data).decode("utf-8")
        logger.info("Message decoded successfully")
        return result
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

    encoded = carrier[start : end + len(END_MARKER)]
    remaining = carrier[:start] + carrier[end + len(END_MARKER) :]

    return encoded, remaining


def has_encoded_message(text: str) -> bool:
    """Check if text contains an encoded message.

    This function checks if the text contains both the start and end markers
    that indicate the presence of an encoded message using zero-width characters.

    Parameters
    ----------
    text : str
        The text to check for encoded messages.

    Returns
    -------
    bool
        True if the text contains both start and end markers, False otherwise.
    """
    return START_MARKER in text and END_MARKER in text


def get_encoded_message_size(text: str) -> Optional[int]:
    """Get the size of an encoded message in bytes.

    This function extracts the encoded message and calculates its size in bytes.
    Note that this is the size of the encoded data, not the original message.

    Parameters
    ----------
    text : str
        The text containing the encoded message.

    Returns
    -------
    Optional[int]
        The size of the encoded message in bytes, or None if no message found.
    """
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    
    if start == -1 or end == -1 or end <= start:
        return None
    
    # Extract the encoded data between markers
    encoded = text[start + len(START_MARKER):end]
    
    # Count only the zero-width characters (ZERO_BIT and ONE_BIT)
    zero_width_count = sum(1 for char in encoded if char in (ZERO_BIT, ONE_BIT))
    
    # Each byte is encoded as 8 zero-width characters
    return zero_width_count // 8 if zero_width_count > 0 else None
