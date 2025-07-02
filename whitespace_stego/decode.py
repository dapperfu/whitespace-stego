"""Decode messages using whitespace steganography."""

from typing import Optional, List, Union
import click
from whitespace_stego.core import decode as core_decode
import base64
from whitespace_stego_rust import decode_all as rust_decode_all
from whitespace_stego_rust import decode as rust_decode
from whitespace_stego.c_backend import decode as c_decode

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


def decode_message(encoded_text: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """
    Decode messages from text containing whitespace steganography.

    Args:
        encoded_text: The text containing the hidden messages
        password: Optional password for decryption

    Returns:
        A single decoded message as string, or a list of decoded messages if multiple

    Raises:
        ValueError: If no valid message is found or if the message is corrupted
    """
    # Get the backend from CLI context
    try:
        ctx = click.get_current_context()
        backend = ctx.obj.get("backend", "python") if ctx.obj else "python"
    except RuntimeError:
        # No click context available, default to python backend
        backend = "python"

    if backend == "python":
        # Use the core Python implementation
        return core_decode(encoded_text, password)
    elif backend == "rust":
        # Use the Rust backend
        try:
            messages = rust_decode_all(encoded_text, password)
            # Return string for single message, list for multiple messages (matching Python behavior)
            if len(messages) == 1:
                return messages[0]
            else:
                return messages
        except ImportError:
            # Fallback to old decode function if decode_all is not available
            return rust_decode(encoded_text, password)
    elif backend == "c":
        # Use the C backend
        return c_decode(encoded_text, password)
    else:
        raise ValueError(f"Unknown backend: {backend}")


def _decode_python(encoded_text: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Original Python implementation - now uses core implementation for consistency."""
    # Use the core implementation to ensure consistency across all backends
    return core_decode(encoded_text, password)
