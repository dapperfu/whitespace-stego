"""Decode messages using whitespace steganography."""

from typing import Optional
import click
from whitespace_stego.core import decode as core_decode
import base64

# Zero-width Unicode characters for encoding
ZWSP = "\u200b"  # Zero-width space
ZWJ = "\u200d"  # Zero-width joiner
ZWNJ = "\u200c"  # Zero-width non-joiner
ZWNBSP = "\ufeff"  # Zero-width no-break space

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
    backend = ctx.obj.get("backend", "python") if ctx.obj else "python"

    if backend == "python":
        # Use the core Python implementation
        return core_decode(encoded_text, password)
    elif backend == "rust":
        # Use the Rust backend
        from whitespace_stego_backend import decode as rust_decode

        return rust_decode(encoded_text, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")


def _decode_python(encoded_text: str, password: Optional[str] = None) -> str:
    """Original Python implementation - now uses core implementation for consistency."""
    # Use the core implementation to ensure consistency across all backends
    return core_decode(encoded_text, password)
