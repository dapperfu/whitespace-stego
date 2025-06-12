"""Tests for the whitespace steganography package."""

import pytest
from whitespace_stego import encode, decode
import logging

logging.basicConfig(level=logging.DEBUG)

# Test data sets
MESSAGES = [
    "hello",                    # ASCII
    "こんにちは",               # Japanese
    "👋🌍",                     # Emoji
    "💡⚡🚀",                   # Multiple emoji
    "Hello, 世界!",            # Mixed ASCII and Unicode
    "Test\nwith\nnewlines",    # Special characters
    "",                         # Empty string
    "A" * 100,                 # Long string
]

PASSWORDS = [
    "secret",                   # ASCII password
    "秘密",                     # Unicode password
    "",                         # Empty password
    None,                       # No password
    "A" * 32,                  # Long password
]

CARRIERS = [
    "",                         # Empty carrier
    "A",                        # Single character
    "AB",                       # Two characters
    "The quick brown fox jumps over the lazy dog",  # Long ASCII
    "🌸",                       # Single emoji
    "Hello, 世界!",            # Mixed ASCII and Unicode
    "A" * 100,                 # Long carrier
]

@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("password", PASSWORDS)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_stego_encode_decode(message: str, password: str | None, carrier: str) -> None:
    """Test encoding and decoding with various inputs.
    
    This test creates a full matrix of all possible combinations of:
    - Different message types (ASCII, Unicode, emoji, etc.)
    - Different password types (ASCII, Unicode, empty, None)
    - Different carrier types (empty, short, long, mixed)
    
    Parameters
    ----------
    message : str
        The message to encode/decode
    password : str | None
        Optional password for encryption
    carrier : str
        The carrier text to hide the message in
    """
    logging.debug(f"Testing with message={message!r}, carrier={carrier!r}, password={password!r}")
    encoded = encode(message, carrier=carrier, password=password)
    decoded_message, _ = decode(encoded, password=password)
    assert decoded_message == message 