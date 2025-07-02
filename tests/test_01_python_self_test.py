"""
Test 01: Python Implementation Self-Test

This test verifies that the Python implementation can encode and decode
messages correctly with itself in all combinations using parametrized tests.
"""

import pytest
from whitespace_stego.core import encode, decode, START_MARKER, END_MARKER


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
    ("A" * 1000, None, None),  # Long message
    ("!@#$%^&*()_+-=[]{}|;':\",./<>?", None, None),  # Special chars
    ("Line 1\nLine 2\nLine 3", None, None),  # Newlines
    ("Tab\tseparated\tvalues", None, None),  # Tabs
    
    # Edge cases
    ("Single char", None, None),
    ("", "Carrier only", None),  # Empty message with carrier
    ("Message", "", "password"),  # Empty carrier with password
    ("Message", None, ""),  # Empty password
])
def test_encode_decode_roundtrip(message, carrier, password):
    """Test encode/decode roundtrip with various combinations."""
    # Handle None vs empty string for carrier and password
    carrier_param = carrier if carrier is not None else ""
    password_param = password if password is not None else ""
    
    # Encode
    if message:  # Only encode if message is not empty
        encoded = encode(message, carrier_param, password_param)
        # Decode
        decoded = decode(encoded, password_param)
        assert decoded == message
    else:
        # Test empty message error
        with pytest.raises(ValueError):
            encode(message, carrier_param, password_param)


# Test cases for error conditions
@pytest.mark.parametrize("test_input,expected_error", [
    # Empty message error
    ("", ValueError),
    
    # Wrong password error
    (("Secret", "correct", "wrong"), ValueError),
    
    # Missing markers errors
    ("This text has no markers", ValueError),
    (f"This text has {START_MARKER} but no end marker", ValueError),
    (f"This text has {END_MARKER} but no start marker", ValueError),
])
def test_error_conditions(test_input, expected_error):
    """Test various error conditions."""
    if isinstance(test_input, tuple):
        # Wrong password test case
        message, correct_password, wrong_password = test_input
        encoded = encode(message, password=correct_password)
        with pytest.raises(expected_error):
            decode(encoded, wrong_password)
    else:
        # Other error test cases
        if test_input == "":
            # Empty message
            with pytest.raises(expected_error):
                encode(test_input)
        else:
            # Missing markers
            with pytest.raises(expected_error):
                decode(test_input)


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 