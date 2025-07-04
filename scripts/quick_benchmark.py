#!/usr/bin/env python3
"""
Quick benchmark script for whitespace steganography implementations.
Runs only 10 iterations for fast performance comparison.
"""

import subprocess
import time
import tempfile
import statistics
from typing import List
from dataclasses import dataclass
from pathlib import Path

@dataclass
class QuickResult:
    """Results from a quick benchmark run."""
    implementation: str
    backend: str
    operation: str
    iterations: int
    total_time: float
    avg_time: float
    throughput: float
    std_dev: float

def quick_benchmark():
    """Run a quick benchmark with 10 iterations."""
    base_dir = Path(__file__).parent
    iterations = 10
    message = "Quick benchmark test message with emoji 😀 and unicode 你好世界"
    carrier = "This is a carrier text for quick benchmarking."
    
    implementations = {
        'go': {
            'path': base_dir / 'bin' / 'whitespace-stego-go',
            'encode_cmd': lambda msg_file, carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-go'),
                'encode', '-m', msg_file, '-cf', carrier_file, '-o', output_file
            ],
            'decode_cmd': lambda carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-go'),
                'decode', '-cf', carrier_file, '-o', output_file
            ]
        },
        'c': {
            'path': base_dir / 'bin' / 'whitespace-stego-c',
            'encode_cmd': lambda msg_file, carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-c'),
                'encode', '--message-file', msg_file, 
                '--carrier-file', carrier_file, '--output', output_file
            ],
            'decode_cmd': lambda carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-c'),
                'decode', '--carrier-file', carrier_file, '--output', output_file
            ]
        },
        'rust': {
            'path': base_dir / 'bin' / 'whitespace-stego-rs',
            'encode_cmd': lambda msg_file, carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-rs'),
                'encode', '-m', msg_file, '--cf', carrier_file, '-o', output_file
            ],
            'decode_cmd': lambda carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-rs'),
                'decode', '--cf', carrier_file, '-o', output_file
            ]
        },
        'python': {
            'path': base_dir / 'bin' / 'whitespace-stego-py',
            'encode_cmd': lambda msg_file, carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-py'),
                'encode', '-mf', msg_file, '-cf', carrier_file, '-o', output_file
            ],
            'decode_cmd': lambda carrier_file, output_file: [
                str(base_dir / 'bin' / 'whitespace-stego-py'),
                'decode', '-cf', carrier_file, '-o', output_file
            ]
        }
    }
    
    results = []
    
    print("Quick Benchmark - 10 iterations each")
    print("=" * 50)
    print(f"Message: {message}")
    print(f"Carrier: {carrier}")
    print()
    
    for impl_name, impl_config in implementations.items():
        if not impl_config['path'].exists():
            print(f"✗ {impl_name} not available")
            continue
            
        print(f"Testing {impl_name}...")
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            message_file = tmp_path / 'message.txt'
            carrier_file = tmp_path / 'carrier.txt'
            output_file = tmp_path / 'output.txt'
            encoded_file = tmp_path / 'encoded.txt'
            
            # Write test data
            with open(message_file, 'w', encoding='utf-8') as f:
                f.write(message)
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            # Test encode
            try:
                times = []
                for _ in range(iterations):
                    cmd = impl_config['encode_cmd'](message_file, carrier_file, output_file)
                    start = time.time()
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    end = time.time()
                    if result.returncode == 0:
                        times.append(end - start)
                
                if times:
                    total_time = sum(times)
                    avg_time = total_time / len(times)
                    throughput = len(times) / total_time
                    std_dev = statistics.stdev(times) if len(times) > 1 else 0.0
                    
                    results.append(QuickResult(
                        implementation=impl_name,
                        backend='standalone',
                        operation='encode',
                        iterations=len(times),
                        total_time=total_time,
                        avg_time=avg_time,
                        throughput=throughput,
                        std_dev=std_dev
                    ))
                    
                    print(f"  Encode: {throughput:.1f} ops/sec ({avg_time*1000:.1f} ms/op)")
                else:
                    print(f"  Encode: failed")
            except Exception as e:
                print(f"  Encode: error - {e}")
            
            # Pre-encode for decode test
            try:
                encode_cmd = impl_config['encode_cmd'](message_file, carrier_file, encoded_file)
                subprocess.run(encode_cmd, check=True, capture_output=True)
                
                # Test decode
                times = []
                for _ in range(iterations):
                    cmd = impl_config['decode_cmd'](encoded_file, output_file)
                    start = time.time()
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    end = time.time()
                    if result.returncode == 0:
                        times.append(end - start)
                
                if times:
                    total_time = sum(times)
                    avg_time = total_time / len(times)
                    throughput = len(times) / total_time
                    std_dev = statistics.stdev(times) if len(times) > 1 else 0.0
                    
                    results.append(QuickResult(
                        implementation=impl_name,
                        backend='standalone',
                        operation='decode',
                        iterations=len(times),
                        total_time=total_time,
                        avg_time=avg_time,
                        throughput=throughput,
                        std_dev=std_dev
                    ))
                    
                    print(f"  Decode: {throughput:.1f} ops/sec ({avg_time*1000:.1f} ms/op)")
                else:
                    print(f"  Decode: failed")
            except Exception as e:
                print(f"  Decode: error - {e}")
    
    # Print summary
    print("\n" + "=" * 50)
    print("QUICK BENCHMARK SUMMARY")
    print("=" * 50)
    
    encode_results = [r for r in results if r.operation == 'encode']
    decode_results = [r for r in results if r.operation == 'decode']
    
    if encode_results:
        print("\nENCODE (ops/sec):")
        encode_results.sort(key=lambda x: x.throughput, reverse=True)
        for result in encode_results:
            print(f"  {result.implementation}: {result.throughput:.1f}")
    
    if decode_results:
        print("\nDECODE (ops/sec):")
        decode_results.sort(key=lambda x: x.throughput, reverse=True)
        for result in decode_results:
            print(f"  {result.implementation}: {result.throughput:.1f}")
    
    if results:
        fastest_encode = max(encode_results, key=lambda x: x.throughput) if encode_results else None
        fastest_decode = max(decode_results, key=lambda x: x.throughput) if decode_results else None
        
        print(f"\nFASTEST:")
        if fastest_encode:
            print(f"  Encode: {fastest_encode.implementation} ({fastest_encode.throughput:.1f} ops/sec)")
        if fastest_decode:
            print(f"  Decode: {fastest_decode.implementation} ({fastest_decode.throughput:.1f} ops/sec)")
    
    total_time = sum(r.total_time for r in results)
    print(f"\nTotal time: {total_time:.1f} seconds")

if __name__ == "__main__":
    quick_benchmark()
