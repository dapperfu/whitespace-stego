#!/usr/bin/env python3

import subprocess
import sys
import os

# Test the Python implementation
from whitespace_stego.core import encode as py_encode, decode as py_decode

# Test message and carrier
message = "Hello"
carrier = "carrier"
password = "test"

print("Testing Python implementation...")
py_result = py_encode(message, carrier, password)
print(f"Python encoded length: {len(py_result)}")
print(f"Python encoded (first 100 chars): {repr(py_result[:100])}")

# Test Python decode
py_decoded = py_decode(py_result, password)
print(f"Python decoded: {py_decoded}")
print(f"Python decode success: {py_decoded == message}")

print("\n" + "="*50 + "\n")

# Test the Rust implementation via CLI
print("Testing Rust implementation...")
try:
    # Use the Rust CLI if available
    rust_cmd = [".venv/bin/python", "-m", "whitespace_stego.cli", "--backend", "rust", "encode", "--message", message, "--carrier", carrier, "--password", password]
    rust_result = subprocess.run(rust_cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
    
    if rust_result.returncode == 0:
        rust_encoded = rust_result.stdout.strip()
        print(f"Rust encoded length: {len(rust_encoded)}")
        print(f"Rust encoded (first 100 chars): {repr(rust_encoded[:100])}")
        
        # Test Rust decode
        rust_decode_cmd = [".venv/bin/python", "-m", "whitespace_stego.cli", "--backend", "rust", "decode", "--carrier", rust_encoded, "--password", password]
        rust_decode_result = subprocess.run(rust_decode_cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
        
        if rust_decode_result.returncode == 0:
            rust_decoded = rust_decode_result.stdout.strip()
            print(f"Rust decoded: {rust_decoded}")
            print(f"Rust decode success: {rust_decoded == message}")
        else:
            print(f"Rust decode failed: {rust_decode_result.stderr}")
    else:
        print(f"Rust encode failed: {rust_result.stderr}")
        
except Exception as e:
    print(f"Error testing Rust: {e}")

print("\n" + "="*50 + "\n")

# Test cross-implementation
print("Testing cross-implementation...")
try:
    # Python encode, Rust decode
    print("Python encode -> Rust decode:")
    rust_decode_cmd = [".venv/bin/python", "-m", "whitespace_stego.cli", "--backend", "rust", "decode", "--carrier", py_result, "--password", password]
    cross_result = subprocess.run(rust_decode_cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
    
    if cross_result.returncode == 0:
        cross_decoded = cross_result.stdout.strip()
        print(f"Cross decoded: {cross_decoded}")
        print(f"Cross decode success: {cross_decoded == message}")
    else:
        print(f"Cross decode failed: {cross_result.stderr}")
        
    # Rust encode, Python decode
    print("\nRust encode -> Python decode:")
    if rust_result.returncode == 0:
        py_cross_decoded = py_decode(rust_encoded, password)
        print(f"Cross decoded: {py_cross_decoded}")
        print(f"Cross decode success: {py_cross_decoded == message}")
    else:
        print("Skipping Rust encode -> Python decode test due to Rust encode failure")
        
except Exception as e:
    print(f"Error testing cross-implementation: {e}") 