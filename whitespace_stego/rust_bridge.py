"""Rust backend bridge for whitespace steganography.

This module provides a Python interface to the Rust backend for encoding and decoding
messages using whitespace steganography.
"""

from typing import Optional

from whitespace_stego_rs import encode_message_rs as rust_encode_message
from whitespace_stego_rs import decode_message as rust_decode_message
from whitespace_stego_rs import encode_binary_rs
from whitespace_stego_rs import insert_payload_rs
from whitespace_stego_rs import encode_and_insert_rs
from whitespace_stego_rs import decode_binary_rs
from whitespace_stego_rs import decode_and_remove_rs

RUST_AVAILABLE = True

def encode_message(
    message: str,
    carrier: str,
    password: Optional[str] = None,
) -> str:
    """Encode a message into a carrier text using the Rust backend.

    Args:
        message: The message to encode.
        carrier: The carrier text to encode the message into.
        password: Optional password for encryption.

    Returns:
        The encoded carrier text.

    Raises:
        ValueError: If encoding fails.
    """
    return rust_encode_message(message, carrier, password)

def encode_binary(binary_str: str) -> str:
    """Encode a binary string using zero-width characters via Rust backend."""
    return encode_binary_rs(binary_str)

def insert_payload(carrier: str, payload: str, position: Optional[int] = None) -> str:
    """Insert a steganographic payload into carrier text via Rust backend."""
    return insert_payload_rs(carrier, payload, position)

def encode_and_insert(
    message: str,
    carrier: str,
    password: Optional[str] = None,
    position: Optional[int] = None
) -> str:
    """Encode a message and insert it into carrier text via Rust backend."""
    return encode_and_insert_rs(message, carrier, password, position)

def decode_message(
    encoded_text: str,
    password: Optional[str] = None,
) -> str:
    """Decode a message from encoded text using the Rust backend.

    Args:
        encoded_text: The encoded text to decode.
        password: Optional password for decryption.

    Returns:
        The decoded message.

    Raises:
        ValueError: If decoding fails.
    """
    return rust_decode_message(encoded_text, password)

def decode_binary(encoded: str) -> str:
    """Decode zero-width characters back to binary string via Rust backend."""
    return decode_binary_rs(encoded)

def decode_and_remove(text: str, password: Optional[str] = None):
    """Decode a hidden message and remove it from the carrier text via Rust backend."""
    return decode_and_remove_rs(text, password) 