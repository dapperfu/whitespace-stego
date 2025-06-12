"""Whitespace steganography package."""

from .encode import encode_and_insert as encode
from .decode import decode_and_remove as decode

__all__ = ['encode', 'decode'] 