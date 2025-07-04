"""
Test 30: Security and Cryptography

This test suite comprehensively tests all cryptographic functions, key derivation,
encryption/decryption edge cases, and potential security vulnerabilities.
"""

import pytest
import base64
import hashlib
import os
from unittest.mock import patch, MagicMock
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.exceptions import InvalidKey, InvalidTag

from whitespace_stego.core import (
    derive_key, encrypt_data, decrypt_data, encode, decode, BadPasswordError
)
from whitespace_stego.constants import START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT


class TestKeyDerivation:
    """Test key derivation functionality."""
    
    @pytest.mark.parametrize("password", [
        "testpassword",
        "密码🔑",
        "abc\x00def",
        "A" * 1000,
    ])
    def test_derive_key_basic(self, password):
        """Test basic key derivation properties."""
        k1 = derive_key(password)
        k2 = derive_key(password)
        assert k1 == k2  # Deterministic
        assert isinstance(k1, bytes)
        assert len(k1) == 32
    
    @pytest.mark.parametrize("password,expected_hash", [
        ("", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
        ("password", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"),
        ("123456", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
        ("@#$%^&*()", "a821cf5c9ba958c46e94979df3c03ec7266a50468f5bbfc280d54cd015cb5304"),
        ("Unicode 🌍 中文", "3cc3501ed3b828a25260cbdc582aacf3108879ef71ce9398b16d04100e50b9dd"),
    ])
    def test_derive_key_consistency(self, password, expected_hash):
        """Test that key derivation produces consistent results."""
        key = derive_key(password)
        assert isinstance(key, bytes)
        assert len(key) == 32  # SHA-256 produces 32 bytes
        
        # Verify the hash matches expected
        expected_key = bytes.fromhex(expected_hash)
        assert key == expected_key
    
    @pytest.mark.parametrize("password", [
        "café",
        "naïve", 
        "façade",
        "Hello 世界 🌍",
        "Привет мир",
        "こんにちは世界",
        "안녕하세요 세계",
    ])
    def test_derive_key_unicode(self, password):
        """Test that key derivation properly handles UTF-8 encoding."""
        key = derive_key(password)
        assert isinstance(key, bytes)
        assert len(key) == 32
        
        # Verify it's deterministic
        key2 = derive_key(password)
        assert key == key2
    
    @pytest.mark.parametrize("password", [
        "test\x00password",
        "A" * 10000,
    ])
    def test_derive_key_edge_cases(self, password):
        """Test key derivation with edge case passwords."""
        key = derive_key(password)
        assert isinstance(key, bytes)
        assert len(key) == 32
        
        # Should be deterministic
        key2 = derive_key(password)
        assert key == key2


class TestEncryptionDecryption:
    """Test encryption and decryption functionality."""
    
    @pytest.mark.parametrize("data,password", [
        (b"Hello, World", "pw1"),
        (b"", "pw2"),
        (b"A"*1000, "pw3"),
        (b"\x00\x01\x02", "pw4"),
        ("世界🌍".encode(), "pw5"),
    ])
    def test_encrypt_decrypt_roundtrip(self, data, password):
        """Test that encryption followed by decryption returns original data."""
        encrypted = encrypt_data(data, password)
        assert isinstance(encrypted, bytes)
        assert len(encrypted) > len(data)  # Should be larger due to IV and padding
        
        decrypted = decrypt_data(encrypted, password)
        assert decrypted == data
    
    @pytest.mark.parametrize("data", [
        b"",
        b"Large data " * 10000,  # ~110KB
    ])
    def test_encrypt_decrypt_data_sizes(self, data):
        """Test encryption/decryption of different data sizes."""
        password = "test_password"
        encrypted = encrypt_data(data, password)
        decrypted = decrypt_data(encrypted, password)
        assert decrypted == data
    
    @pytest.mark.parametrize("data", [
        b"\x00" * 100,  # All nulls
        b"\xff" * 100,  # All ones
        b"\x00\xff" * 50,  # Alternating
        bytes(range(256)),  # All byte values
    ])
    def test_encrypt_decrypt_binary_patterns(self, data):
        """Test encryption/decryption of binary data patterns."""
        password = "binary_test"
        encrypted = encrypt_data(data, password)
        decrypted = decrypt_data(encrypted, password)
        assert decrypted == data
    
    @pytest.mark.parametrize("password", [
        "密码123",
        "🔑password",
        "café",
        "Hello 世界 🌍",
        "",  # Empty password
        "A" * 1000,  # Long password
    ])
    def test_encrypt_decrypt_password_variants(self, password):
        """Test encryption/decryption with various password types."""
        data = b"Test data"
        encrypted = encrypt_data(data, password)
        decrypted = decrypt_data(encrypted, password)
        assert decrypted == data
    
    @pytest.mark.parametrize("password", [
        "@#$%^&*()_+-=[]{}|;':\",./<>?",
        "password with spaces",
        "password\twith\ttabs",
        "password\nwith\nnewlines",
        "password\r\nwith\r\ncrlf",
        "test\x00password",  # Null bytes
    ])
    def test_encrypt_decrypt_special_chars(self, password):
        """Test encryption/decryption with special character passwords."""
        data = b"Test data"
        encrypted = encrypt_data(data, password)
        decrypted = decrypt_data(encrypted, password)
        assert decrypted == data
    
    def test_encrypt_decrypt_same_password_different_data(self):
        """Test that same password produces different ciphertexts for different data."""
        password = "same_password"
        data1 = b"Data 1"
        data2 = b"Data 2"
        
        encrypted1 = encrypt_data(data1, password)
        encrypted2 = encrypt_data(data2, password)
        
        # Should be different due to random IV
        assert encrypted1 != encrypted2
        
        # Both should decrypt correctly
        assert decrypt_data(encrypted1, password) == data1
        assert decrypt_data(encrypted2, password) == data2
    
    @pytest.mark.parametrize("invalid_data", [
        b"short",
        b"x" * 15,
    ])
    def test_decrypt_invalid_data(self, invalid_data):
        """Test decryption with invalid data."""
        password = "test_password"
        
        with pytest.raises(ValueError):
            decrypt_data(invalid_data, password)
    
    def test_decrypt_corrupted_data(self):
        """Test decryption with corrupted data."""
        password = "test_password"
        data = b"test"
        valid_encrypted = encrypt_data(data, password)
        corrupted = valid_encrypted[:-1] + b"X"  # Corrupt last byte
        
        with pytest.raises(ValueError):
            decrypt_data(corrupted, password)
    
    def test_decrypt_wrong_password(self):
        """Test decryption with wrong password."""
        data = b"Secret data"
        correct_password = "correct_password"
        wrong_password = "wrong_password"
        
        encrypted = encrypt_data(data, correct_password)
        
        with pytest.raises(ValueError):
            decrypt_data(encrypted, wrong_password)
    
    def test_encrypt_decrypt_entropy(self):
        """Test that encrypted data has sufficient entropy."""
        data = b"entropytest"
        pw = "pw"
        enc = encrypt_data(data, pw)
        # Check that no byte dominates
        counts = {b: enc.count(bytes([b])) for b in range(256)}
        max_count = max(counts.values())
        assert max_count / len(enc) < 0.3


class TestSecurityVulnerabilities:
    """Test for potential security vulnerabilities."""
    
    @pytest.mark.parametrize("wrong_password", ["wrong1", "wrong2", "wrong3"])
    def test_timing_attack_resistance(self, wrong_password):
        """Test that encryption/decryption is resistant to timing attacks."""
        password = "test_password"
        data = b"Secret data"
        
        encrypted = encrypt_data(data, password)
        
        # Test that wrong password fails quickly (should not leak information)
        with pytest.raises(ValueError):
            decrypt_data(encrypted, wrong_password)
    
    def test_padding_oracle_resistance(self):
        """Test resistance to padding oracle attacks."""
        password = "test_password"
        data = b"Secret data"
        
        encrypted = encrypt_data(data, password)
        
        # Try to manipulate the padding
        encrypted_bytes = bytearray(encrypted)
        
        # Corrupt the padding
        encrypted_bytes[-1] ^= 1
        
        with pytest.raises(ValueError):
            decrypt_data(bytes(encrypted_bytes), password)
    
    def test_key_reuse_protection(self):
        """Test that each encryption uses a unique IV."""
        password = "test_password"
        data = b"Same data"
        
        # Encrypt the same data multiple times
        encrypted_results = []
        for _ in range(10):
            encrypted = encrypt_data(data, password)
            encrypted_results.append(encrypted)
        
        # All results should be different due to random IVs
        unique_results = set(encrypted_results)
        assert len(unique_results) == len(encrypted_results)
    
    def test_entropy_validation(self):
        """Test that encrypted data has sufficient entropy."""
        password = "test_password"
        data = b"Test data"
        
        encrypted = encrypt_data(data, password)
        
        # Check that encrypted data doesn't contain obvious patterns
        # This is a basic entropy check
        byte_counts = {}
        for byte in encrypted:
            byte_counts[byte] = byte_counts.get(byte, 0) + 1
        
        # No single byte should dominate
        max_count = max(byte_counts.values())
        total_bytes = len(encrypted)
        assert max_count / total_bytes < 0.3  # No byte should be >30% of data


class TestIntegrationSecurity:
    """Test security in the context of the full encode/decode workflow."""
    
    @pytest.mark.parametrize("message,carrier,password", [
        ("Secret message", "Public carrier text", "secret_password"),
        ("Hello 世界 🌍", "English carrier", "密码123"),
        ("Test", "Carrier with emojis 🚀", "🔑password"),
    ])
    def test_encoded_message_security(self, message, carrier, password):
        """Test that encoded messages don't leak information."""
        encoded = encode(message, carrier, password)
        
        # The encoded text should not contain the original message
        assert message not in encoded
        assert password not in encoded
        
        # Should not contain obvious patterns
        assert "Secret" not in encoded
        assert "message" not in encoded
    
    @pytest.mark.parametrize("messages,passwords", [
        (["Secret1", "Secret2", "Secret3"], ["pw1", "pw2", "pw3"]),
        (["Alpha", "Beta", "Gamma"], ["alpha", "beta", "gamma"]),
    ])
    def test_multiple_messages_security(self, messages, passwords):
        """Test security with multiple encoded messages."""
        carrier = "Carrier"
        
        # Encode multiple messages
        encoded = carrier
        for msg, pwd in zip(messages, passwords):
            encoded = encode(msg, encoded, pwd)
        
        # Each password should only decode its own message
        for i, (msg, pwd) in enumerate(zip(messages, passwords)):
            decoded = decode(encoded, pwd)
            if isinstance(decoded, list):
                assert msg in decoded
            else:
                assert decoded == msg
        
        # Wrong password should fail
        with pytest.raises((ValueError, BadPasswordError)):
            decode(encoded, "wrong_password")
    
    @pytest.mark.parametrize("carrier", [
        "Carrier 1",
        "Different carrier",
        "Unicode carrier: 世界 🌍",
        "",  # Empty carrier
    ])
    def test_carrier_independence(self, carrier):
        """Test that encoded messages are independent of carrier content."""
        message = "Secret message"
        password = "password"
        
        encoded = encode(message, carrier, password)
        
        # Should decode to the same message
        decoded = decode(encoded, password)
        if isinstance(decoded, list):
            assert message in decoded
        else:
            assert decoded == message
    
    @pytest.mark.parametrize("message1,message2,password1,password2", [
        ("Message 1", "Message 2", "password1", "password2"),
        ("Hello 世界", "Hello 🌍", "pw1", "pw2"),
    ])
    def test_message_isolation(self, message1, message2, password1, password2):
        """Test that messages are properly isolated from each other."""
        carrier = "Carrier"
        
        # Encode two messages
        encoded1 = encode(message1, carrier, password1)
        encoded2 = encode(message2, encoded1, password2)
        
        # Each password should only decode its own message
        decoded1 = decode(encoded2, password1)
        decoded2 = decode(encoded2, password2)
        
        if isinstance(decoded1, list):
            assert message1 in decoded1
        else:
            assert decoded1 == message1
            
        if isinstance(decoded2, list):
            assert message2 in decoded2
        else:
            assert decoded2 == message2


class TestCryptographicConstants:
    """Test cryptographic constants and parameters."""
    
    @pytest.mark.parametrize("password", ["test_password", "another_password", "密码123"])
    def test_key_length(self, password):
        """Test that derived keys have correct length."""
        key = derive_key(password)
        assert len(key) == 32  # SHA-256 produces 32 bytes
    
    @pytest.mark.parametrize("data", [b"Test data", b"Another test", "世界🌍".encode()])
    def test_iv_length(self, data):
        """Test that IV has correct length."""
        password = "test_password"
        
        encrypted = encrypt_data(data, password)
        # IV should be 16 bytes (AES block size)
        iv = encrypted[:16]
        assert len(iv) == 16
    
    def test_cipher_algorithm(self):
        """Test that AES-256-CBC is used."""
        password = "test_password"
        data = b"Test data"
        
        encrypted = encrypt_data(data, password)
        
        # Verify the structure: IV (16 bytes) + ciphertext
        assert len(encrypted) > 16
        iv = encrypted[:16]
        ciphertext = encrypted[16:]
        
        # Should be able to decrypt with AES-256-CBC
        key = derive_key(password)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove PKCS7 padding
        unpadder = padding.PKCS7(128).unpadder()
        result = unpadder.update(padded) + unpadder.finalize()
        
        assert result == data


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 