"""Tests for the core steganography functionality."""

import pytest

from whitespace_stego.core import (
    decode,
    encode,
    extract_encoded,
    START_MARKER,
    END_MARKER,
)

# Test data
MESSAGES = [
    "Hello, World!",
    "Test message with emoji 😀",
    "Multilingual text: 你好, 世界!",
    "Special chars: !@#$%^&*()",
    "",  # Empty message
]

PASSWORDS = [
    None,  # No password
    "simple_password",
    "complex_password_123!@#",
    "",  # Empty password
]

CARRIERS = [
    "",  # Empty carrier
    "Simple carrier text",
    "Carrier with emoji 🎉",
    "Multilingual carrier: 你好",
]


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("password", PASSWORDS)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_encode_decode(message: str, password: str | None, carrier: str, debug_logger) -> None:
    """Test that encoding and decoding preserves the original message."""
    debug_logger.debug("Testing encode/decode with carrier: %s", carrier)
    debug_logger.debug("Password: %s", password)
    debug_logger.debug("Message: %s", message)
    
    # Encode the message
    encoded = encode(message, carrier, password)
    debug_logger.debug("Encoded result: %s", encoded)
    
    # Decode the message
    decoded = decode(encoded, password)
    debug_logger.debug("Decoded result: %s", decoded)
    
    assert decoded == message
    debug_logger.info("Test passed: encode/decode with %s", 
                     "password" if password else "no password")


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_encode_without_password(message: str, carrier: str) -> None:
    """Test encoding without password."""
    encoded = encode(message, carrier)
    assert START_MARKER in encoded
    assert END_MARKER in encoded


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_encode_with_password(message: str, carrier: str) -> None:
    """Test encoding with password."""
    password = "test_password"
    encoded = encode(message, carrier, password)
    assert START_MARKER in encoded
    assert END_MARKER in encoded


@pytest.mark.parametrize("message", MESSAGES)
def test_empty_carrier(message: str) -> None:
    """Test encoding with empty carrier."""
    encoded = encode(message)
    assert START_MARKER in encoded
    assert END_MARKER in encoded
    assert len(encoded) > len(message)  # Should be longer due to encoding


@pytest.mark.parametrize("carrier", CARRIERS)
def test_invalid_decode(carrier: str) -> None:
    """Test decoding invalid carrier text."""
    with pytest.raises(ValueError):
        decode(carrier)


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_extract_encoded(message: str, carrier: str) -> None:
    """Test extracting encoded message from carrier."""
    encoded = encode(message, carrier)
    extracted, remaining = extract_encoded(encoded)
    assert START_MARKER in extracted
    assert END_MARKER in extracted
    if carrier:
        assert remaining == carrier  # Should be the full original carrier


@pytest.mark.parametrize("carrier", CARRIERS)
def test_extract_encoded_invalid(carrier: str) -> None:
    """Test extracting from invalid carrier text."""
    with pytest.raises(ValueError):
        extract_encoded(carrier)


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("password", PASSWORDS)
def test_password_mismatch(message: str, password: str | None) -> None:
    """Test that wrong password fails to decode."""
    if password is None:
        return  # Skip if no password

    encoded = encode(message, password=password)
    with pytest.raises(ValueError):
        decode(encoded, password="wrong_password")
