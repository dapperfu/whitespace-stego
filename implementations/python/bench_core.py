"""
Benchmark core encode/decode functions for all Python backends (pure Python, C, Rust).

Usage:
    python3 bench_core.py

This script runs encode/decode in a tight loop and prints timing for each backend.
"""
import time
import sys

message = "Secret message" * 100
carrier = "This is the carrier text." * 100
password = None
iterations = 1000

results = []

def bench(fn, name):
    t0 = time.perf_counter()
    for _ in range(iterations):
        encoded = fn(message, carrier, password)
    t1 = time.perf_counter()
    total = t1 - t0
    avg = total / iterations
    print(f"{name:10s} encode: {total*1000:.2f} ms total, {avg*1e6:.2f} us/call")
    return encoded

def bench_decode(fn, name, encoded):
    t0 = time.perf_counter()
    for _ in range(iterations):
        decoded = fn(encoded, password)
    t1 = time.perf_counter()
    total = t1 - t0
    avg = total / iterations
    print(f"{name:10s} decode: {total*1000:.2f} ms total, {avg*1e6:.2f} us/call")
    return decoded

# Pure Python
from whitespace_stego.core import encode as py_encode, decode as py_decode
encoded_py = bench(py_encode, "python")
bench_decode(py_decode, "python", encoded_py)

# C backend
try:
    from whitespace_stego.c_backend import encode as c_encode, decode as c_decode
    encoded_c = bench(c_encode, "cffi-c")
    bench_decode(c_decode, "cffi-c", encoded_c)
except ImportError:
    print("[WARN] C backend not available.")

# Rust backend
try:
    import whitespace_stego_rust
    encoded_rust = bench(whitespace_stego_rust.encode, "rust-pyo3")
    bench_decode(whitespace_stego_rust.decode, "rust-pyo3", encoded_rust)
    
    # Test fast version if available
    if hasattr(whitespace_stego_rust, 'decode_fast'):
        bench_decode(whitespace_stego_rust.decode_fast, "rust-pyo3-fast", encoded_rust)
    else:
        print("[INFO] Rust fast decode not available in Python bindings")
        
except ImportError:
    print("[WARN] Rust backend not available.") 