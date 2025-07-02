#!/usr/bin/env python3
"""Test script for the C backend."""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_c_backend():
    """Test the C backend functionality."""
    print("Testing C backend...")
    
    try:
        from whitespace_stego.c_backend import encode, decode, is_available
        
        if not is_available():
            print("❌ C backend is not available")
            return False
        
        print("✅ C backend is available")
        
        # Test basic encoding/decoding
        message = "Hello, World!"
        carrier = "This is a test carrier text."
        password = "test_password"
        
        print(f"Original message: {message}")
        print(f"Carrier: {carrier}")
        print(f"Password: {password}")
        
        # Encode
        encoded = encode(message, carrier, password)
        print(f"Encoded length: {len(encoded)}")
        print(f"Encoded (first 50 chars): {repr(encoded[:50])}")
        
        # Decode
        decoded = decode(encoded, password)
        print(f"Decoded: {decoded}")
        
        if decoded == message:
            print("✅ Basic encoding/decoding test passed")
        else:
            print(f"❌ Basic encoding/decoding test failed: expected '{message}', got '{decoded}'")
            return False
        
        # Test without password
        encoded_no_pw = encode(message, carrier)
        decoded_no_pw = decode(encoded_no_pw)
        
        if decoded_no_pw == message:
            print("✅ No password encoding/decoding test passed")
        else:
            print(f"❌ No password encoding/decoding test failed: expected '{message}', got '{decoded_no_pw}'")
            return False
        
        # Test empty carrier
        encoded_empty = encode(message, "")
        decoded_empty = decode(encoded_empty)
        
        if decoded_empty == message:
            print("✅ Empty carrier encoding/decoding test passed")
        else:
            print(f"❌ Empty carrier encoding/decoding test failed: expected '{message}', got '{decoded_empty}'")
            return False
        
        print("✅ All C backend tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ C backend test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_c_backend()
    sys.exit(0 if success else 1) 