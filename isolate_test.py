#!/usr/bin/env python3
"""Isolate the failing test to understand the exception type."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'whitespace_stego'))

from whitespace_stego.core import encrypt_data, decrypt_data
from cryptography.exceptions import InvalidKey, InvalidTag

def test_timing_attack_resistance():
    """Test that encryption/decryption is resistant to timing attacks."""
    password = "test_password"
    wrong_password = "wrong1"
    data = b"Secret data"
    
    print(f"Encrypting data with password: {password}")
    encrypted = encrypt_data(data, password)
    print(f"Encrypted data length: {len(encrypted)}")
    
    print(f"Attempting to decrypt with wrong password: {wrong_password}")
    try:
        result = decrypt_data(encrypted, wrong_password)
        print(f"Unexpected success! Result: {result}")
        return False
    except ValueError as e:
        print(f"ValueError raised: {e}")
        return True
    except InvalidKey as e:
        print(f"InvalidKey raised: {e}")
        return True
    except InvalidTag as e:
        print(f"InvalidTag raised: {e}")
        return True
    except Exception as e:
        print(f"Unexpected exception raised: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    print("Testing timing attack resistance...")
    success = test_timing_attack_resistance()
    if success:
        print("Test passed - exception was raised as expected")
    else:
        print("Test failed - no exception was raised") 