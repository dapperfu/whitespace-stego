"""Whitespace steganography library.

This library provides functionality for encoding and decoding messages
using zero-width Unicode characters in carrier text.
"""

import sys
from typing import List, Optional

from .core import encode, decode, BadPasswordError

# Try to import Rust backend for better performance
try:
    from whitespace_stego_rust import encode as rust_encode, decode as rust_decode, count_messages as rust_count_messages
    rust_available = True
except ImportError:
    rust_available = False

# Try to import C backend for better performance
try:
    from .c_backend import encode as c_encode, decode as c_decode, count_messages as c_count_messages
    c_available = True
except ImportError:
    c_available = False

__version__ = "0.1.0"
__all__ = [
    "encode", "decode", "count_messages",
    "rust_available", "c_available",
    "rust_encode", "rust_decode", "rust_count_messages",
    "c_encode", "c_decode", "c_count_messages",
] 