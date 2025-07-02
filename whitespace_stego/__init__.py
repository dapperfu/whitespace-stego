"""Whitespace steganography package.

Available backends:
- Pure Python (default)
- Rust (via PyO3, if installed)
- C (via ctypes, if built)
"""

from .core import encode as py_encode, decode as py_decode
from .encode import encode_message
from .decode import decode_message

# Optionally import C backend
try:
    from .c_backend import encode as c_encode, decode as c_decode, is_available as c_is_available
except ImportError:
    c_encode = c_decode = None
    def c_is_available():
        return False

# Optionally import Rust backend
try:
    from whitespace_stego_backend import encode as rust_encode, decode as rust_decode
    def rust_is_available():
        return True
except ImportError:
    rust_encode = rust_decode = None
    def rust_is_available():
        return False

__all__ = [
    "encode_message",
    "decode_message",
    "py_encode",
    "py_decode",
    "c_encode",
    "c_decode",
    "c_is_available",
    "rust_encode",
    "rust_decode",
    "rust_is_available",
] 