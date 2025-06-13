"""Whitespace steganography library.

This package provides functionality for hiding messages in text using zero-width characters.
"""

from . import encode, decode, crypto, common
from .benchmark import benchmark_encryption, benchmark_compression

__version__ = "0.1.0"
__all__ = [
    'encode',
    'decode',
    'crypto',
    'common',
    'benchmark_encryption',
    'benchmark_compression'
] 