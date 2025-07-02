"""Whitespace steganography package.

Available backends:
- Pure Python (default)
- Rust (via PyO3, if installed)
- C (via ctypes, if built)
"""

from .core import encode as py_encode, decode as py_decode, count_messages as py_count_messages
from .encode import encode_message
from .decode import decode_message

# Optionally import C backend
try:
    from .c_backend import encode as c_encode, decode as c_decode, is_available as c_available, count_messages as c_count_messages
except ImportError:
    c_encode = c_decode = c_count_messages = None
    def c_available():
        return False

# Optionally import Rust backend
try:
    from whitespace_stego_backend import encode as rust_encode, decode as rust_decode, count_messages as rust_count_messages
    def rust_available():
        return True
except ImportError:
    rust_encode = rust_decode = rust_count_messages = None
    def rust_available():
        return False

__all__ = [
    "encode_message",
    "decode_message",
    "py_encode",
    "py_decode",
    "py_count_messages",
    "c_encode",
    "c_decode",
    "c_available",
    "c_count_messages",
    "rust_encode",
    "rust_decode",
    "rust_available",
    "rust_count_messages",
] 