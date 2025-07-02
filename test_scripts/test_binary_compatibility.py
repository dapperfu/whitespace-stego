#!/usr/bin/env python3
"""Test binary encoding compatibility between Python and Rust implementations."""

import subprocess
import sys

def test_python_binary_encoding():
    """Test Python binary encoding."""
    from whitespace_stego.core import _encode_binary, _decode_binary
    
    # Test with simple data
    test_data = b"Hello"
    print("Python encoding test:")
    print(f"Input: {test_data}")
    
    # Encode
    encoded = _encode_binary(test_data)
    print(f"Encoded: {repr(encoded)}")
    
    # Decode
    decoded = _decode_binary(encoded)
    print(f"Decoded: {decoded}")
    print(f"Round-trip successful: {decoded == test_data}")
    
    # Show binary representation
    binary = "".join("1" if char == "\u200d" else "0" for char in encoded)
    print(f"Binary: {binary}")
    
    return encoded, binary

def test_rust_binary_encoding():
    """Test Rust binary encoding."""
    try:
        # Create test data
        with open("/tmp/test_binary_input.txt", "w") as f:
            f.write("Hello")
        
        # Run Rust encode
        result = subprocess.run([
            "/projects/whitespace-stego3/rust/target/release/whitespace-stego-rs", 
            "encode", 
            "--mf", "/tmp/test_binary_input.txt",
            "--carrier", "",
            "-o", "/tmp/rust_binary_output.txt"
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Rust encode failed: {result.stderr}")
            return None, None
        
        # Read the encoded output
        with open("/tmp/rust_binary_output.txt", "r") as f:
            rust_encoded = f.read()
        
        print("\nRust encoding test:")
        print(f"Encoded: {repr(rust_encoded)}")
        
        # Extract binary representation
        start_marker = "\ufeff"
        end_marker = "\u200c"
        start_idx = rust_encoded.find(start_marker)
        end_idx = rust_encoded.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            data_part = rust_encoded[start_idx + len(start_marker):end_idx]
            binary = "".join("1" if char == "\u200d" else "0" for char in data_part)
            print(f"Binary: {binary}")
            return data_part, binary
        
    except Exception as e:
        print(f"Rust test failed: {e}")
    
    return None, None

if __name__ == "__main__":
    print("Testing binary encoding compatibility...")
    
    # Test Python
    py_encoded, py_binary = test_python_binary_encoding()
    
    # Test Rust
    rust_encoded, rust_binary = test_rust_binary_encoding()
    
    # Compare
    if py_binary and rust_binary:
        print(f"\nComparison:")
        print(f"Python binary: {py_binary}")
        print(f"Rust binary:   {rust_binary}")
        print(f"Match: {py_binary == rust_binary}")
        
        if py_binary != rust_binary:
            print(f"First difference at position: {next((i for i, (p, r) in enumerate(zip(py_binary, rust_binary)) if p != r), -1)}") 