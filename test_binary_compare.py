#!/usr/bin/env python3

import subprocess
import sys

# Test the Python binary encoding
from whitespace_stego.core import _encode_binary

# Test data
data = b'SGVsbG8='  # Base64 encoded "Hello"
print("Test data:", data)

# Python encoding
py_encoded = _encode_binary(data)
print("Python encoded (first 50 chars):", repr(py_encoded[:50]))

# Convert to binary string for comparison
binary = "".join(format(b, "08b") for b in data)
print("Binary string:", binary[:50])

# Check character distribution
zero_count = py_encoded.count('\u200b')
one_count = py_encoded.count('\u200d')
start_count = py_encoded.count('\ufeff')
end_count = py_encoded.count('\u200c')

print(f"Character counts in Python output:")
print(f"  ZERO_BIT (\\u200b): {zero_count}")
print(f"  ONE_BIT (\\u200d): {one_count}")
print(f"  START_MARKER (\\ufeff): {start_count}")
print(f"  END_MARKER (\\u200c): {end_count}")

print("\n" + "="*50 + "\n")

# Test Rust encoding
print("Testing Rust encoding...")
try:
    # Create a simple test with the same data
    rust_cmd = [".venv/bin/python", "-m", "whitespace_stego.cli", "--backend", "rust", "encode", "--message", "Hello", "--carrier", "test", "--password", "test"]
    rust_result = subprocess.run(rust_cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
    
    if rust_result.returncode == 0:
        rust_encoded = rust_result.stdout.strip()
        print("Rust encoded (first 50 chars):", repr(rust_encoded[:50]))
        
        # Check character distribution
        zero_count = rust_encoded.count('\u200b')
        one_count = rust_encoded.count('\u200d')
        start_count = rust_encoded.count('\ufeff')
        end_count = rust_encoded.count('\u200c')
        
        print(f"Character counts in Rust output:")
        print(f"  ZERO_BIT (\\u200b): {zero_count}")
        print(f"  ONE_BIT (\\u200d): {one_count}")
        print(f"  START_MARKER (\\ufeff): {start_count}")
        print(f"  END_MARKER (\\u200c): {end_count}")
    else:
        print(f"Rust encode failed: {rust_result.stderr}")
        
except Exception as e:
    print(f"Error testing Rust: {e}") 