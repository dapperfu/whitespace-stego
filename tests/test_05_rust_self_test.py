"""
Test 05: Rust PyO3 Backend Self-Test

This test verifies that the Rust PyO3 backend can encode and decode
messages correctly with itself in all combinations using parametrized tests.
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


# Test cases for successful encode/decode operations
@pytest.mark.parametrize("message,carrier,password", [
    # Basic cases
    ("Hello, World!", None, None),
    ("Hello, World!", "", None),
    ("Secret message", "This is some carrier text", None),
    ("Top secret", None, "mypassword123"),
    ("Very secret message", "Public carrier text", "securepass"),
    
    # Unicode cases
    ("Hello 世界! 🌍", None, None),
    ("Test", "Carrier with 中文 and emoji 🚀", None),
    
    # Special content cases
    ("A" * 100, None, None),  # Long message (reduced for CLI)
    ("!@#$%^&*()_+-=[]{}|;':\",./<>?", None, None),  # Special chars
    ("Line 1\nLine 2\nLine 3", None, None),  # Newlines
    ("Tab\tseparated\tvalues", None, None),  # Tabs
    
    # Edge cases
    ("Single char", None, None),
    ("Message", "", "password"),  # Empty carrier with password
    ("Message", None, ""),  # Empty password
])
def test_rust_encode_decode_roundtrip(message, carrier, password):
    """Test Rust encode/decode roundtrip with various combinations."""
    # Handle None vs empty string for carrier and password
    carrier_param = carrier if carrier is not None else ""
    password_param = password if password is not None else ""
    
    # Encode
    if message:  # Only encode if message is not empty
        encoded = run_rust_encode(message, carrier_param, password_param)
        # Decode
        decoded = run_rust_decode(encoded, password_param)
        assert decoded == message
    else:
        # Test empty message error
        with pytest.raises(RuntimeError):
            run_rust_encode(message, carrier_param, password_param)


# Test cases for error conditions
@pytest.mark.parametrize("test_input,expected_error", [
    # Empty message error
    ("", RuntimeError),
    
    # Wrong password error
    (("Secret", "correct", "wrong"), RuntimeError),
    
    # Missing markers errors
    ("This text has no markers", RuntimeError),
    ("This text has \ufeff but no end marker", RuntimeError),
    ("This text has \u200c but no start marker", RuntimeError),
])
def test_rust_error_conditions(test_input, expected_error):
    """Test various error conditions with Rust implementation."""
    if isinstance(test_input, tuple):
        # Wrong password test case
        message, correct_password, wrong_password = test_input
        encoded = run_rust_encode(message, password=correct_password)
        with pytest.raises(expected_error):
            run_rust_decode(encoded, wrong_password)
    else:
        # Other error test cases
        if test_input == "":
            # Empty message
            with pytest.raises(expected_error):
                run_rust_encode(test_input)
        else:
            # Missing markers
            with pytest.raises(expected_error):
                run_rust_decode(test_input)


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 