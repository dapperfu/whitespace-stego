#!/usr/bin/env python3
"""
Comprehensive benchmarking script for all whitespace steganography implementations.

This script benchmarks:
- Python CLI with Python backend
- Python CLI with Rust backend  
- Python CLI with C backend
- Standalone Python binary
- Standalone Rust binary
- Standalone C binary
- Standalone Go binary

Tests encode/decode operations with a long message repeated multiple times.
"""

import subprocess
import time
import tempfile
import os
import statistics
import json
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from pathlib import Path

@dataclass
class BenchmarkResult:
    """Results from a single benchmark run."""
    implementation: str
    backend: str
    operation: str
    iterations: int
    total_time: float
    avg_time: float
    throughput: float  # operations per second
    std_dev: float
    message_length: int
    carrier_length: int

class WhitespaceStegoBenchmark:
    """Comprehensive benchmark for all whitespace steganography implementations."""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.results: List[BenchmarkResult] = []
        
        # Test configuration - reduced iterations for faster testing
        self.iterations = 100  # Reduced from 1000 to keep under 1 minute
        self.long_message = self._generate_long_message()
        self.carrier = "This is a carrier text for benchmarking purposes. " * 10
        
        # Implementation configurations with corrected command formats
        self.implementations = {
            'python-cli-python': {
                'path': self.base_dir / '.venv' / 'bin' / 'whitespace-stego',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'python', 'encode', '-mf', msg_file, 
                    '-cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'python', 'decode', '-cf', carrier_file, 
                    '-o', output_file
                ]
            },
            'python-cli-rust': {
                'path': self.base_dir / '.venv' / 'bin' / 'whitespace-stego',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'rust', 'encode', '-mf', msg_file, 
                    '-cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'rust', 'decode', '-cf', carrier_file, 
                    '-o', output_file
                ]
            },
            'python-cli-c': {
                'path': self.base_dir / '.venv' / 'bin' / 'whitespace-stego',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'c', 'encode', '-mf', msg_file, 
                    '-cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / '.venv' / 'bin' / 'whitespace-stego'),
                    '-b', 'c', 'decode', '-cf', carrier_file, 
                    '-o', output_file
                ]
            },
            'python-standalone': {
                'path': self.base_dir / 'bin' / 'whitespace-stego-py',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-py'),
                    'encode', '-mf', msg_file, 
                    '-cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-py'),
                    'decode', '-cf', carrier_file, '-o', output_file
                ]
            },
            'rust-standalone': {
                'path': self.base_dir / 'bin' / 'whitespace-stego-rs',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-rs'),
                    'encode', '-m', msg_file, '--cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-rs'),
                    'decode', '--cf', carrier_file, '-o', output_file
                ]
            },
            'c-standalone': {
                'path': self.base_dir / 'bin' / 'whitespace-stego-c',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-c'),
                    'encode', '--message-file', msg_file, 
                    '--carrier-file', carrier_file, '--output', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-c'),
                    'decode', '--carrier-file', carrier_file, '--output', output_file
                ]
            },
            'go-standalone': {
                'path': self.base_dir / 'bin' / 'whitespace-stego-go',
                'encode_cmd': lambda msg_file, carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-go'),
                    'encode', '-m', msg_file, '-cf', carrier_file, '-o', output_file
                ],
                'decode_cmd': lambda carrier_file, output_file: [
                    str(self.base_dir / 'bin' / 'whitespace-stego-go'),
                    'decode', '-cf', carrier_file, '-o', output_file
                ]
            }
        }
    
    def _generate_long_message(self) -> str:
        """Generate a long message for benchmarking."""
        base_message = (
            "This is a comprehensive benchmark message designed to test the performance "
            "of various whitespace steganography implementations. It includes various "
            "types of content including numbers (123456789), symbols (!@#$%^&*()), "
            "emojis (😀🎉🚀), and unicode characters (你好世界). "
            "The message is designed to be long enough to stress test the encoding "
            "and decoding algorithms while remaining realistic for real-world usage. "
            "This benchmark will help identify performance bottlenecks and compare "
            "the efficiency of different language implementations."
        )
        # Repeat to make it longer
        return base_message * 2  # Reduced from 3 to 2 for faster testing
    
    def _check_implementation_available(self, impl_name: str) -> bool:
        """Check if an implementation is available."""
        impl_config = self.implementations[impl_name]
        return impl_config['path'].exists()
    
    def _run_benchmark(self, impl_name: str, operation: str) -> BenchmarkResult:
        """Run a single benchmark for encode or decode operation with timing samples."""
        impl_config = self.implementations[impl_name]
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            
            # Prepare files
            message_file = tmp_path / 'message.txt'
            carrier_file = tmp_path / 'carrier.txt'
            output_file = tmp_path / 'output.txt'
            encoded_file = tmp_path / 'encoded.txt'
            
            # Write test data
            with open(message_file, 'w', encoding='utf-8') as f:
                f.write(self.long_message)
            
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(self.carrier)
            
            # Pre-encode if we're testing decode
            if operation == 'decode':
                encode_cmd = impl_config['encode_cmd'](message_file, carrier_file, encoded_file)
                subprocess.run(encode_cmd, check=True, capture_output=True)
                input_file = encoded_file
            else:
                input_file = carrier_file
            
            # Run benchmark with individual timing samples
            times = []
            
            for _ in range(self.iterations):
                if operation == 'encode':
                    cmd = impl_config['encode_cmd'](message_file, input_file, output_file)
                else:  # decode
                    cmd = impl_config['decode_cmd'](input_file, output_file)
                
                start_time = time.time()
                result = subprocess.run(cmd, capture_output=True, text=True)
                end_time = time.time()
                
                if result.returncode != 0:
                    print(f"Warning: {impl_name} {operation} failed: {result.stderr}")
                    continue
                
                times.append(end_time - start_time)
            
            if not times:
                raise Exception(f"No successful runs for {impl_name} {operation}")
            
            # Calculate metrics
            total_time = sum(times)
            avg_time = total_time / len(times)
            throughput = len(times) / total_time
            std_dev = statistics.stdev(times) if len(times) > 1 else 0.0
            
            # Determine backend name
            if 'python-cli' in impl_name:
                backend = impl_name.split('-')[-1]
            else:
                backend = 'standalone'
            
            return BenchmarkResult(
                implementation=impl_name,
                backend=backend,
                operation=operation,
                iterations=len(times),
                total_time=total_time,
                avg_time=avg_time,
                throughput=throughput,
                std_dev=std_dev,
                message_length=len(self.long_message),
                carrier_length=len(self.carrier)
            )
    
    def run_all_benchmarks(self) -> List[BenchmarkResult]:
        """Run benchmarks for all available implementations."""
        print("Starting comprehensive whitespace steganography benchmark...")
        print(f"Message length: {len(self.long_message)} characters")
        print(f"Carrier length: {len(self.carrier)} characters")
        print(f"Iterations per test: {self.iterations}")
        print()
        
        available_impls = []
        for impl_name in self.implementations:
            if self._check_implementation_available(impl_name):
                available_impls.append(impl_name)
                print(f"✓ {impl_name} available")
            else:
                print(f"✗ {impl_name} not available")
        
        print(f"\nRunning benchmarks for {len(available_impls)} implementations...")
        print("=" * 80)
        
        for impl_name in available_impls:
            print(f"\nBenchmarking {impl_name}...")
            
            # Test encode
            try:
                encode_result = self._run_benchmark(impl_name, 'encode')
                self.results.append(encode_result)
                print(f"  Encode: {encode_result.throughput:.1f} ops/sec "
                      f"({encode_result.avg_time*1000:.2f} ms/op ± {encode_result.std_dev*1000:.2f} ms)")
            except Exception as e:
                print(f"  Encode failed: {e}")
            
            # Test decode
            try:
                decode_result = self._run_benchmark(impl_name, 'decode')
                self.results.append(decode_result)
                print(f"  Decode: {decode_result.throughput:.1f} ops/sec "
                      f"({decode_result.avg_time*1000:.2f} ms/op ± {decode_result.std_dev*1000:.2f} ms)")
            except Exception as e:
                print(f"  Decode failed: {e}")
        
        return self.results
    
    def print_summary(self):
        """Print a comprehensive summary of benchmark results."""
        if not self.results:
            print("No benchmark results available.")
            return
        
        print("\n" + "=" * 80)
        print("BENCHMARK SUMMARY")
        print("=" * 80)
        
        # Group by operation
        encode_results = [r for r in self.results if r.operation == 'encode']
        decode_results = [r for r in self.results if r.operation == 'decode']
        
        # Encode summary
        if encode_results:
            print("\nENCODE PERFORMANCE (operations per second):")
            print("-" * 70)
            print(f"{'Implementation':<20} {'Backend':<10} {'Throughput':<12} {'Avg Time':<12} {'Std Dev':<10}")
            print("-" * 70)
            encode_results.sort(key=lambda x: x.throughput, reverse=True)
            for result in encode_results:
                print(f"{result.implementation:<20} {result.backend:<10} "
                      f"{result.throughput:<12.1f} {result.avg_time*1000:<12.2f} {result.std_dev*1000:<10.2f}")
        
        # Decode summary
        if decode_results:
            print("\nDECODE PERFORMANCE (operations per second):")
            print("-" * 70)
            print(f"{'Implementation':<20} {'Backend':<10} {'Throughput':<12} {'Avg Time':<12} {'Std Dev':<10}")
            print("-" * 70)
            decode_results.sort(key=lambda x: x.throughput, reverse=True)
            for result in decode_results:
                print(f"{result.implementation:<20} {result.backend:<10} "
                      f"{result.throughput:<12.1f} {result.avg_time*1000:<12.2f} {result.std_dev*1000:<10.2f}")
        
        # Overall fastest
        if self.results:
            fastest_encode = max(encode_results, key=lambda x: x.throughput) if encode_results else None
            fastest_decode = max(decode_results, key=lambda x: x.throughput) if decode_results else None
            
            print("\nFASTEST IMPLEMENTATIONS:")
            print("-" * 30)
            if fastest_encode:
                print(f"Encode: {fastest_encode.implementation} ({fastest_encode.backend}) "
                      f"- {fastest_encode.throughput:.1f} ops/sec")
            if fastest_decode:
                print(f"Decode: {fastest_decode.implementation} ({fastest_decode.backend}) "
                      f"- {fastest_decode.throughput:.1f} ops/sec")
        
        # Performance ratios
        if encode_results and len(encode_results) > 1:
            fastest_encode_throughput = encode_results[0].throughput
            print(f"\nENCODE PERFORMANCE RATIOS (relative to fastest):")
            print("-" * 55)
            for result in encode_results:
                ratio = result.throughput / fastest_encode_throughput
                print(f"{result.implementation:20} {result.backend:10} {ratio:6.2f}x")
        
        if decode_results and len(decode_results) > 1:
            fastest_decode_throughput = decode_results[0].throughput
            print(f"\nDECODE PERFORMANCE RATIOS (relative to fastest):")
            print("-" * 55)
            for result in decode_results:
                ratio = result.throughput / fastest_decode_throughput
                print(f"{result.implementation:20} {result.backend:10} {ratio:6.2f}x")
    
    def save_results(self, filename: str = "benchmark_results.json"):
        """Save benchmark results to JSON file."""
        results_dict = []
        for result in self.results:
            results_dict.append({
                'implementation': result.implementation,
                'backend': result.backend,
                'operation': result.operation,
                'iterations': result.iterations,
                'total_time': result.total_time,
                'avg_time': result.avg_time,
                'throughput': result.throughput,
                'std_dev': result.std_dev,
                'message_length': result.message_length,
                'carrier_length': result.carrier_length
            })
        
        with open(filename, 'w') as f:
            json.dump(results_dict, f, indent=2)
        
        print(f"\nResults saved to {filename}")

def main():
    """Main benchmark execution."""
    benchmark = WhitespaceStegoBenchmark()
    
    try:
        results = benchmark.run_all_benchmarks()
        benchmark.print_summary()
        benchmark.save_results()
        
        total_time = sum(r.total_time for r in results)
        print(f"\nTotal benchmark time: {total_time:.1f} seconds")
        
    except KeyboardInterrupt:
        print("\nBenchmark interrupted by user.")
    except Exception as e:
        print(f"\nBenchmark failed: {e}")
        raise

if __name__ == "__main__":
    main()
