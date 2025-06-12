"""Tests for the crypto module.

This module contains tests for cryptographic utilities.
"""

import pytest
from whitespace_stego.crypto import (
    derive_key,
    encrypt_message,
    decrypt_message
)

def test_derive_key() -> None:
    """Test key derivation."""
    # Test with new salt
    key1, salt1 = derive_key("password")
    assert len(key1) == 32  # 256 bits
    assert len(salt1) == 16
    
    # Test with same password and salt
    key2, salt2 = derive_key("password", salt1)
    assert key1 == key2
    assert salt1 == salt2
    
    # Test with different password
    key3, _ = derive_key("different", salt1)
    assert key1 != key3

def test_encrypt_message() -> None:
    """Test message encryption."""
    message = "Hello, 世界! 👋"
    
    # Test without password (base64 only)
    encrypted = encrypt_message(message)
    assert encrypted != message
    decrypted = decrypt_message(encrypted)
    assert decrypted == message
    
    # Test with password
    encrypted = encrypt_message(message, "secret")
    assert encrypted != message
    decrypted = decrypt_message(encrypted, "secret")
    assert decrypted == message
    
    # Test with wrong password
    with pytest.raises(ValueError):
        decrypt_message(encrypted, "wrong")

def test_decrypt_message() -> None:
    """Test message decryption."""
    message = "Hello, 世界! 👋"
    
    # Test without password (base64 only)
    encrypted = encrypt_message(message)
    decrypted = decrypt_message(encrypted)
    assert decrypted == message
    
    # Test with password
    encrypted = encrypt_message(message, "secret")
    decrypted = decrypt_message(encrypted, "secret")
    assert decrypted == message
    
    # Test with wrong password
    with pytest.raises(ValueError):
        decrypt_message(encrypted, "wrong")
    
    # Test with invalid base64
    with pytest.raises(ValueError):
        decrypt_message("invalid base64", "secret")
    
    # Test with invalid encrypted data
    with pytest.raises(ValueError):
        decrypt_message("aGVsbG8=", "secret")  # Valid base64 but invalid encrypted data 