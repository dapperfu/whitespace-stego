"""
Test 06: Rust PyO3 Backend Interface Testing

This test verifies that the Rust PyO3 backend interface works correctly with various
input methods, output formats, and error conditions.
"""

import pytest
import whitespace_stego_backend


def run_rust_encode(message, carrier=None, password=None):
    """Encode a message using Rust PyO3 backend."""
    try:
        # Handle None vs empty string for carrier and password
        carrier_param = carrier if carrier is not None else ""
        password_param = password if password is not None else ""
        
        return whitespace_stego_backend.encode(message, carrier_param, password_param)
    except Exception as e:
        raise RuntimeError(f"Rust encode failed: {e}")


def run_rust_decode(encoded_text, password=None):
    """Decode a message using Rust PyO3 backend."""
    try:
        # Handle None vs empty string for password
        password_param = password if password is not None else ""
        
        return whitespace_stego_backend.decode(encoded_text, password_param)
    except Exception as e:
        raise RuntimeError(f"Rust decode failed: {e}")


def test_rust_backend_encode_basic():
    """Test basic encode functionality."""
    encoded = run_rust_encode("Hello, World!")
    assert encoded  # Should have output
    # Check that output contains zero-width characters
    assert any(ord(c) > 0x7F for c in encoded)


def test_rust_backend_encode_with_carrier():
    """Test encode with carrier text."""
    encoded = run_rust_encode("Secret", "Public text")
    # The encoded text should start with the first character of the carrier and end with the rest
    assert encoded.startswith("P")  # Should start with first character of carrier
    assert encoded.endswith("text")  # Should end with rest of carrier text


def test_rust_backend_encode_with_password():
    """Test encode with password."""
    encoded = run_rust_encode("Secret", password="mypass")
    assert encoded  # Should have output


def test_rust_backend_encode_with_carrier_and_password():
    """Test encode with both carrier and password."""
    encoded = run_rust_encode("Secret", "Public", "mypass")
    # The encoded text should start with the first character of the carrier and end with the rest
    assert encoded.startswith("P")  # Should start with first character of carrier
    assert encoded.endswith("ublic")  # Should end with rest of carrier text


def test_rust_backend_decode_basic():
    """Test basic decode functionality."""
    # First encode a message
    encoded = run_rust_encode("Hello, World!")
    
    # Then decode it
    decoded = run_rust_decode(encoded)
    assert decoded == "Hello, World!"


def test_rust_backend_decode_with_password():
    """Test decode with password."""
    # First encode with password
    encoded = run_rust_encode("Secret", password="mypass")
    
    # Then decode with password
    decoded = run_rust_decode(encoded, "mypass")
    assert decoded == "Secret"


def test_rust_backend_decode_wrong_password():
    """Test decode with wrong password."""
    # First encode with password
    encoded = run_rust_encode("Secret", password="correct")
    
    # Then decode with wrong password
    with pytest.raises(RuntimeError):
        run_rust_decode(encoded, "wrong")


def test_rust_backend_encode_empty_message():
    """Test encode with empty message."""
    with pytest.raises(RuntimeError):
        run_rust_encode("")


def test_rust_backend_decode_empty_input():
    """Test decode with empty input."""
    with pytest.raises(RuntimeError):
        run_rust_decode("")


def test_rust_backend_decode_no_markers():
    """Test decode with text that has no markers."""
    with pytest.raises(RuntimeError):
        run_rust_decode("No markers here")


def test_rust_backend_unicode_message():
    """Test encode/decode with Unicode message."""
    # Encode Unicode message
    encoded = run_rust_encode("Hello 世界! 🌍")
    
    # Decode Unicode message
    decoded = run_rust_decode(encoded)
    assert decoded == "Hello 世界! 🌍"


def test_rust_backend_unicode_carrier():
    """Test encode with Unicode carrier."""
    encoded = run_rust_encode("Test", "Carrier with 中文 and emoji 🚀")
    assert "中文" in encoded  # Should contain Unicode carrier text


def test_rust_backend_special_characters():
    """Test encode/decode with special characters."""
    special_message = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    
    # Encode special characters
    encoded = run_rust_encode(special_message)
    
    # Decode special characters
    decoded = run_rust_decode(encoded)
    assert decoded == special_message


def test_rust_backend_newlines_in_message():
    """Test encode/decode with newlines in message."""
    message_with_newlines = "Line 1\nLine 2\nLine 3"
    
    # Encode message with newlines
    encoded = run_rust_encode(message_with_newlines)
    
    # Decode message with newlines
    decoded = run_rust_decode(encoded)
    assert decoded == message_with_newlines


def test_rust_backend_long_message():
    """Test encode/decode with long message."""
    long_message = "A" * 1000
    
    # Encode long message
    encoded = run_rust_encode(long_message)
    
    # Decode long message
    decoded = run_rust_decode(encoded)
    assert decoded == long_message


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 