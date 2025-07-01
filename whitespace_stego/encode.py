"""Encode messages using whitespace steganography."""

from typing import Optional
import click
from whitespace_stego.core import encode as core_encode
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


def encode_message(message: str, carrier: str, password: Optional[str] = None) -> str:
    """
    Encode a message into carrier text using whitespace steganography.

    Args:
        message: The message to encode
        carrier: The carrier text to encode into (can be empty)
        password: Optional password for encryption

    Returns:
        The encoded carrier text with the message hidden using zero-width characters
    """
    # Get the backend from CLI context
    ctx = click.get_current_context()
    backend = ctx.obj.get("backend", "python") if ctx.obj else "python"

    if backend == "python":
        # Use the core Python implementation
        return core_encode(message, carrier, password)
    elif backend == "rust":
        # Use the Rust backend
        from whitespace_stego_backend import encode as rust_encode

        return rust_encode(message, carrier, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")


def _encode_python(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Original Python implementation - now uses core implementation for consistency."""
    # Use the core implementation to ensure consistency across all backends
    return core_encode(message, carrier, password)
