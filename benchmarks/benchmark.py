#!/usr/bin/env python3
"""Benchmark suite for whitespace steganography implementations."""

import time
import sys
from pathlib import Path

# Add python module to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python"))

try:
    from whitespace_stego import encode, decode
except ImportError:
    print("Error: Could not import whitespace_stego")
    sys.exit(1)


def benchmark_python(message: str, iterations: int = 1000):
    """Benchmark Python implementation."""
    print(f"Benchmarking Python with {len(message)} char message, {iterations} iterations...")
    
    # Encode benchmark
    start = time.perf_counter()
    for _ in range(iterations):
        encoded = encode(message)
    encode_time = time.perf_counter() - start
    
    # Decode benchmark
    encoded = encode(message)  # Get encoded once
    start = time.perf_counter()
    for _ in range(iterations):
        decoded = decode(encoded)
    decode_time = time.perf_counter() - start
    
    print(f"  Encode: {encode_time/iterations*1000:.3f} ms/op")
    print(f"  Decode: {decode_time/iterations*1000:.3f} ms/op")
    print(f"  Total: {(encode_time + decode_time)/iterations*1000:.3f} ms/op")
    
    return {
        "encode_time": encode_time / iterations,
        "decode_time": decode_time / iterations,
        "total_time": (encode_time + decode_time) / iterations,
    }


def main():
    """Run benchmarks."""
    print("Whitespace Steganography Benchmarks")
    print("=" * 50)
    print()
    
    test_cases = [
        ("Small", "Hello"),
        ("Medium", "The quick brown fox jumps over the lazy dog." * 10),
        ("Large", "A" * 1000),
        ("Unicode", "Hello 🌍 你好 " * 50),
    ]
    
    results = {}
    
    for name, message in test_cases:
        print(f"\n{name} message ({len(message)} chars):")
        results[name] = benchmark_python(message, iterations=100)
    
    print("\n" + "=" * 50)
    print("Benchmark complete!")


if __name__ == "__main__":
    main()

