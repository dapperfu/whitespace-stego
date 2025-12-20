"""Whitespace steganography using invisible Unicode characters.

This module provides encoding and decoding functions for hiding messages
in text using invisible Unicode control characters.
"""

from whitespace_stego.encoder import encode
from whitespace_stego.decoder import decode
from whitespace_stego.errors import (
    StegoError,
    EncodingError,
    DecodingError,
    InvalidPayloadError,
    MissingMarkerError,
    InvalidBase64Error,
    InvalidUTF8Error,
)

__all__ = [
    "encode",
    "decode",
    "StegoError",
    "EncodingError",
    "DecodingError",
    "InvalidPayloadError",
    "MissingMarkerError",
    "InvalidBase64Error",
    "InvalidUTF8Error",
]

__version__ = "0.1.0"

