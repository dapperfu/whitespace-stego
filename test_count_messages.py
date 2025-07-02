#!/usr/bin/env python3
"""Test script to verify count_messages functions work correctly."""

import whitespace_stego

def test_count_messages():
    """Test count_messages functions for all backends."""
    
    # Test data
    carrier = "Hello world"
    message1 = "Secret message 1"
    message2 = "Secret message 2"
    
    print("Testing count_messages functions...")
    
    # Test Python backend
    print(f"Python backend available: {whitespace_stego.py_count_messages is not None}")
    if whitespace_stego.py_count_messages is not None:
        # Encode one message
        encoded1 = whitespace_stego.py_encode(message1, carrier)
        count1 = whitespace_stego.py_count_messages(encoded1)
        print(f"Python: 1 message encoded -> count: {count1}")
        
        # Encode second message
        encoded2 = whitespace_stego.py_encode(message2, encoded1)
        count2 = whitespace_stego.py_count_messages(encoded2)
        print(f"Python: 2 messages encoded -> count: {count2}")
    
    # Test C backend
    print(f"C backend available: {whitespace_stego.c_available()}")
    if whitespace_stego.c_available():
        # Encode one message
        encoded1 = whitespace_stego.c_encode(message1, carrier)
        count1 = whitespace_stego.c_count_messages(encoded1)
        print(f"C: 1 message encoded -> count: {count1}")
        
        # Encode second message
        encoded2 = whitespace_stego.c_encode(message2, encoded1)
        count2 = whitespace_stego.c_count_messages(encoded2)
        print(f"C: 2 messages encoded -> count: {count2}")
    
    # Test Rust backend
    print(f"Rust backend available: {whitespace_stego.rust_available()}")
    if whitespace_stego.rust_available():
        # Encode one message
        encoded1 = whitespace_stego.rust_encode(message1, carrier)
        count1 = whitespace_stego.rust_count_messages(encoded1)
        print(f"Rust: 1 message encoded -> count: {count1}")
        
        # Encode second message
        encoded2 = whitespace_stego.rust_encode(message2, encoded1)
        count2 = whitespace_stego.rust_count_messages(encoded2)
        print(f"Rust: 2 messages encoded -> count: {count2}")
    
    print("All count_messages tests completed!")

if __name__ == "__main__":
    test_count_messages() 