"""Core implementation of whitespace steganography.

This module provides the core functionality for encoding and decoding messages
using zero-width Unicode whitespace characters.
"""

import base64
import logging
from typing import Optional, Tuple, List, Union
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from cryptography.hazmat.primitives import padding
import re
from .constants import ZERO_BIT, ONE_BIT, START_MARKER, END_MARKER, BITS_PER_CHAR
from .logger import setup_logger

# Create logger instance
logger = setup_logger(__name__)

# Zero-width characters for encoding

# --- Binary encoding/decoding helpers ---
def _bytes_to_bitstring(data: bytes) -> str:
    """Convert bytes to a bitstring (MSB first)."""
    return "".join(format(b, "08b") for b in data)

def _bitstring_to_bytes(bitstring: str) -> bytes:
    """Convert a bitstring to bytes (truncate to multiple of 8)."""
    if len(bitstring) % 8 != 0:
        logger.warning(f"Bitstring length {len(bitstring)} is not a multiple of 8, truncating")
        bitstring = bitstring[:-(len(bitstring) % 8)]
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

def _encode_binary(data: bytes) -> str:
    """Encode binary data into zero-width characters."""
    return "".join(ONE_BIT if bit == "1" else ZERO_BIT for bit in _bytes_to_bitstring(data))

def _decode_binary(encoded: str) -> bytes:
    """Decode zero-width characters back to binary data."""
    filtered = ''.join(c for c in encoded if c in (ZERO_BIT, ONE_BIT))
    bitstring = ''.join('1' if c == ONE_BIT else '0' for c in filtered)
    return _bitstring_to_bytes(bitstring)

# --- Key derivation and encryption ---
def derive_key(password: str) -> bytes:
    """Derive a 32-byte key from password (UTF-8, SHA-256)."""
    import hashlib
    return hashlib.sha256(password.encode('utf-8')).digest()

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using AES-256-CBC with PKCS7 padding."""
    key = derive_key(password)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return iv + ciphertext

def decrypt_data(data: bytes, password: str) -> bytes:
    """Decrypt data using AES-256-CBC with PKCS7 padding."""
    if len(data) < 16:
        raise ValueError("Invalid encrypted data")
    key = derive_key(password)
    iv, ciphertext = data[:16], data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()

# --- Message embedding/extraction helpers ---
def _count_message_pairs(carrier: str) -> int:
    """Count the number of start/end marker pairs in the carrier text."""
    return min(carrier.count(START_MARKER), carrier.count(END_MARKER))

def _find_next_slot(carrier: str) -> int:
    """Find the next available slot for encoding a message."""
    pattern = re.compile(f"{START_MARKER}.*?{END_MARKER}")
    cleaned = pattern.sub("", carrier)
    existing = _count_message_pairs(carrier)
    if existing == 0:
        return 1 if len(cleaned) > 1 else 0
    if existing < len(cleaned) - 1:
        return existing + 1
    return len(cleaned) - 1

def _insert_message_at_position(carrier: str, encoded_message: str, position: int) -> str:
    pattern = re.compile(f"{START_MARKER}.*?{END_MARKER}")
    cleaned = pattern.sub("", carrier)
    if position == 0:
        new_carrier = encoded_message + cleaned
    elif position >= len(cleaned):
        new_carrier = cleaned + encoded_message
    else:
        new_carrier = cleaned[:position] + encoded_message + cleaned[position:]
    # Re-insert previously encoded messages at their original positions
    result = new_carrier
    matches = list(pattern.finditer(carrier))
    offset = 0
    for match in matches:
        pre = carrier[:match.start()]
        cleaned_pre = pattern.sub("", pre)
        insert_pos = len(cleaned_pre) + offset
        result = result[:insert_pos] + match.group(0) + result[insert_pos:]
        offset += len(match.group(0))
    return result

# --- Main encode/decode API ---
def encode(message: str, carrier: str = "", password: Optional[str] = None) -> str:
    """Encode a message into carrier text using whitespace steganography."""
    if not message:
        raise ValueError("Message must not be empty.")
    
    if password:
        # Encrypt the original message first
        encrypted = encrypt_data(message.encode('utf-8'), password)
        # Base64 encode the encrypted data to convert random bytes to safe ASCII
        import base64
        payload = base64.b64encode(encrypted)
    else:
        # For non-password messages, base64 encode the original message
        import base64
        payload = base64.b64encode(message.encode('utf-8'))
    
    zw = _encode_binary(payload)
    encoded_message = START_MARKER + zw + END_MARKER
    if not carrier:
        return encoded_message
    pos = _find_next_slot(carrier)
    return _insert_message_at_position(carrier, encoded_message, pos)

class BadPasswordError(ValueError):
    pass

def decode(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode a message from carrier text using whitespace steganography."""
    # Find all start/end marker pairs
    pattern = re.compile(f"{START_MARKER}(.*?){END_MARKER}")
    matches = list(pattern.finditer(carrier))
    if not matches:
        raise ValueError("No valid messages found in carrier text")
    results = []
    password_errors = 0
    for match in matches:
        zw = match.group(1)
        try:
            data = _decode_binary(zw)
            if password:
                import base64
                try:
                    # Base64 decode the data to get encrypted bytes
                    encrypted = base64.b64decode(data)
                    # Decrypt the encrypted bytes
                    decoded = decrypt_data(encrypted, password)
                except Exception:
                    password_errors += 1
                    continue
                results.append(decoded.decode('utf-8'))
            else:
                # Base64 decode the data directly
                import base64
                decoded = base64.b64decode(data)
                results.append(decoded.decode('utf-8'))
        except Exception as e:
            logger.warning(f"Failed to decode message: {e}")
            continue
    if not results:
        if password and password_errors > 0:
            raise BadPasswordError("Invalid password or no valid messages found in carrier text")
        else:
            raise ValueError("No valid messages found in carrier text")
    return results[0] if len(results) == 1 else results

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

def count_messages(carrier: str) -> int:
    """Count the number of messages embedded in the carrier text.
    
    This function counts the number of complete start/end marker pairs,
    which represents the number of messages that have been embedded.
    
    Parameters
    ----------
    carrier : str
        The carrier text to analyze.
        
    Returns
    -------
    int
        The number of messages embedded in the carrier text.
    """
    return _count_message_pairs(carrier)


# --- Backend selection and main API ---
def _get_backend():
    """Get the current backend from click context."""
    try:
        import click
        ctx = click.get_current_context()
        return ctx.obj.get("backend", "python")
    except (RuntimeError, AttributeError):
        return "python"


def _encode_python(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode using Python backend."""
    return _encode_python_impl(message, carrier, password)


def _encode_python_impl(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Internal implementation for Python backend encoding."""
    return encode(message, carrier, password)


def _decode_python(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode using Python backend."""
    return _decode_python_impl(carrier, password)


def _decode_python_impl(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Internal implementation for Python backend decoding."""
    return decode(carrier, password)


def _encode_rust(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode using Rust backend."""
    try:
        import whitespace_stego_rust
        return whitespace_stego_rust.encode_py(message, carrier, password)
    except ImportError:
        raise ValueError("Rust backend not available")


def _decode_rust(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode using Rust backend."""
    try:
        import whitespace_stego_rust
        return whitespace_stego_rust.decode_py(carrier, password)
    except ImportError:
        raise ValueError("Rust backend not available")


def _decode_rust_single(carrier: str, password: Optional[str] = None) -> str:
    """Decode single message using Rust backend."""
    try:
        import whitespace_stego_rust
        result = whitespace_stego_rust.decode_py(carrier, password)
        if isinstance(result, list):
            return result[0] if result else ""
        return result
    except ImportError:
        raise ValueError("Rust backend not available")


def _encode_c(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode using C backend."""
    try:
        from .c_backend import encode as c_encode
        return c_encode(message, carrier, password)
    except ImportError:
        raise ValueError("C backend not available")


def _decode_c(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode using C backend."""
    try:
        from .c_backend import decode as c_decode
        return c_decode(carrier, password)
    except ImportError:
        raise ValueError("C backend not available")


def encode_message(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode a message into carrier text using the selected backend.
    
    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str
        The carrier text to encode into.
    password : Optional[str], optional
        Password for encryption, by default None
        
    Returns
    -------
    str
        The carrier text with the encoded message.
        
    Raises
    ------
    ValueError
        If the backend is unknown or unavailable.
    """
    backend = _get_backend()
    
    if backend == "python":
        return _encode_python(message, carrier, password)
    elif backend == "rust":
        return _encode_rust(message, carrier, password)
    elif backend == "c":
        return _encode_c(message, carrier, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")


def decode_message(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode a message from carrier text using the selected backend.
    
    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded message.
    carrier : str
        The carrier text containing the encoded message.
    password : Optional[str], optional
        Password for decryption, by default None
        
    Returns
    -------
    Union[str, List[str]]
        The decoded message(s).
        
    Raises
    ------
    ValueError
        If the backend is unknown or unavailable, or if no valid messages are found.
    """
    backend = _get_backend()
    
    if backend == "python":
        return _decode_python(carrier, password)
    elif backend == "rust":
        return _decode_rust(carrier, password)
    elif backend == "c":
        return _decode_c(carrier, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")
