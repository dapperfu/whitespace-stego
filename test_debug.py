#!/usr/bin/env python3
import whitespace_stego_rust

# Test with Unicode characters
test_input = "test input \uFEFF marker"
print(f"Testing with input: {repr(test_input)}")

try:
    whitespace_stego_rust.decode_debug_log_only_py(test_input)
    print("Debug function completed successfully")
except Exception as e:
    print(f"Error: {e}")

# Check if log file was created
import os
if os.path.exists("/tmp/rust_decode_debug.txt"):
    print("Log file created:")
    with open("/tmp/rust_decode_debug.txt", "r") as f:
        print(f.read())
else:
    print("No log file created") 