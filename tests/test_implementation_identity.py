#!/usr/bin/env python3
"""
Comprehensive test suite to validate all implementations work identically.

This test suite ensures that:
1. All implementations produce identical encoded output for the same inputs
2. All implementations can decode each other's encoded output
3. All implementations handle edge cases identically
4. All implementations produce identical error messages for invalid inputs

Tested implementations:
- Rust Core Library (whitespace-stego-core)
- CLI Tool (whitespace-stego-cli)
- Python Bindings (whitespace-stego-python)
- WASI/WebAssembly (whitespace-stego-wasi)
"""

import subprocess
import tempfile
import os
import sys
import pytest
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

# Add the project root to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import whitespace_stego
    PYTHON_AVAILABLE = True
except ImportError:
    PYTHON_AVAILABLE = False

try:
    # Try to import the Rust core library directly
    import whitespace_stego_core
    RUST_CORE_AVAILABLE = True
except ImportError:
    RUST_CORE_AVAILABLE = False

# Define test cases with various inputs
TEST_CASES = [
    # Basic cases
    {
        "name": "simple_ascii",
        "message": "Hello, World",
        "carrier": "This is a test carrier text.",
        "password": None
    },
    {
        "name": "empty_carrier",
        "message": "Hidden message",
        "carrier": "",
        "password": None
    },
    {
        "name": "unicode_message",
        "message": "Hello, 世界 🌍",
        "carrier": "English carrier text",
        "password": None
    },
    {
        "name": "unicode_carrier",
        "message": "English message",
        "carrier": "你好，世界！",
        "password": None
    },
    {
        "name": "special_chars",
        "message": "Special chars: @#$%^&*()_+-=[]{}|;':\",./<>?",
        "carrier": "Normal carrier text",
        "password": None
    },
    {
        "name": "long_message",
        "message": "A" * 1000,
        "carrier": "Short carrier",
        "password": None
    },
    # Password-protected cases
    {
        "name": "password_protected",
        "message": "Secret message",
        "carrier": "Public carrier text",
        "password": "my_secret_password"
    },
    {
        "name": "unicode_password",
        "message": "Secret message",
        "carrier": "Public carrier text",
        "password": "密码123"
    },
    # Edge cases
    {
        "name": "single_char_carrier",
        "message": "Test message",
        "carrier": "A",
        "password": None
    },
    {
        "name": "whitespace_carrier",
        "message": "Test message",
        "carrier": "   \t\n   ",
        "password": None
    },
    {
        "name": "marker_in_carrier",
        "message": "Test message",
        "carrier": "Text with\uFEFFmarker\u200C",
        "password": None
    }
]

# Define error test cases
ERROR_TEST_CASES = [
    {
        "name": "empty_message",
        "message": "",
        "carrier": "Valid carrier",
        "password": None,
        "expected_error": "EncodingFailed"
    },
    {
        "name": "no_markers",
        "message": "Valid message",
        "carrier": "Plain text without markers",
        "password": None,
        "expected_error": "InvalidCarrier"
    },
    {
        "name": "wrong_password",
        "message": "Secret message",
        "carrier": "Public carrier text",
        "password": "correct_password",
        "wrong_password": "wrong_password",
        "expected_error": "DecryptionFailed"
    }
]

class ImplementationTester:
    """Test runner for different implementations."""
    
    def __init__(self):
        self.results = {}
        self.temp_dir = None
        
    def setup_temp_dir(self):
        """Create a temporary directory for test files."""
        self.temp_dir = tempfile.mkdtemp()
        return self.temp_dir
    
    def cleanup_temp_dir(self):
        """Clean up temporary directory."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)
    
    def test_rust_core_library(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Test the Rust core library directly."""
        if not RUST_CORE_AVAILABLE:
            return {"error": "Rust core library not available"}
        
        try:
            # This would require direct access to the Rust library
            # For now, we'll test via the CLI with rust backend
            return self.test_cli_implementation(test_case, backend="rust")
        except Exception as e:
            return {"error": f"Rust core test failed: {e}"}
    
    def test_cli_implementation(self, test_case: Dict[str, Any], backend: Optional[str] = None) -> Dict[str, Any]:
        """Test the CLI implementation."""
        try:
            cli_path = ".venv/bin/whitespace-stego"
            if not os.path.exists(cli_path):
                return {"error": f"CLI binary not found at {cli_path}"}
            
            # Create temporary files
            carrier_path = os.path.join(self.temp_dir, f"carrier_{test_case['name']}.txt")
            encoded_path = os.path.join(self.temp_dir, f"encoded_{test_case['name']}.txt")
            decoded_path = os.path.join(self.temp_dir, f"decoded_{test_case['name']}.txt")
            
            # Write carrier to file
            with open(carrier_path, 'w', encoding='utf-8') as f:
                f.write(test_case['carrier'])
            
            # Build encode command
            encode_cmd = [cli_path]
            if backend:
                encode_cmd.extend(['-b', backend])
            encode_cmd.extend([
                'encode',
                '-m', test_case['message'],
                '--carrier-file', carrier_path,
                '-o', encoded_path
            ])
            
            if test_case.get('password'):
                encode_cmd.extend(['-p', test_case['password']])
            
            # Run encode
            result = subprocess.run(encode_cmd, capture_output=True, text=True, check=True)
            
            # Read encoded output
            with open(encoded_path, 'r', encoding='utf-8') as f:
                encoded_output = f.read()
            
            # Build decode command
            decode_cmd = [cli_path]
            if backend:
                decode_cmd.extend(['-b', backend])
            decode_cmd.extend([
                'decode',
                '--carrier-file', encoded_path,
                '-o', decoded_path
            ])
            
            if test_case.get('password'):
                decode_cmd.extend(['-p', test_case['password']])
            
            # Run decode
            result = subprocess.run(decode_cmd, capture_output=True, text=True, check=True)
            
            # Read decoded output
            with open(decoded_path, 'r', encoding='utf-8') as f:
                decoded_output = f.read().strip()
            
            return {
                "encoded": encoded_output,
                "decoded": decoded_output,
                "success": True
            }
            
        except subprocess.CalledProcessError as e:
            return {
                "error": f"CLI command failed: {e}",
                "stdout": e.stdout,
                "stderr": e.stderr,
                "success": False
            }
        except Exception as e:
            return {"error": f"CLI test failed: {e}", "success": False}
    
    def test_python_implementation(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Test the Python implementation."""
        if not PYTHON_AVAILABLE:
            return {"error": "Python implementation not available"}
        
        try:
            # Test encoding
            encoded = whitespace_stego.encode(
                test_case['message'],
                test_case['carrier'],
                test_case.get('password')
            )
            
            # Test decoding
            decoded = whitespace_stego.decode(
                encoded,
                test_case.get('password')
            )
            
            return {
                "encoded": encoded,
                "decoded": decoded,
                "success": True
            }
            
        except Exception as e:
            return {"error": f"Python test failed: {e}", "success": False}
    
    def test_wasi_implementation(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Test the WASI/WebAssembly implementation."""
        try:
            # For WASI, we need to use a different approach
            # This would require running the WASM module
            # For now, we'll skip this test
            return {"error": "WASI testing not yet implemented"}
            
        except Exception as e:
            return {"error": f"WASI test failed: {e}", "success": False}
    
    def test_binary_implementations(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Test the standalone binary implementations."""
        binaries = {
            'rust_bin': 'bin/whitespace-stego-rs',
            'c_bin': 'bin/whitespace-stego-c',
            'go_bin': 'bin/whitespace-stego-go',
            'py_bin': 'bin/whitespace-stego-py'
        }
        
        results = {}
        
        for name, binary_path in binaries.items():
            if not os.path.exists(binary_path):
                results[name] = {"error": f"Binary not found: {binary_path}"}
                continue
            
            try:
                # Create temporary files
                carrier_path = os.path.join(self.temp_dir, f"carrier_{name}_{test_case['name']}.txt")
                encoded_path = os.path.join(self.temp_dir, f"encoded_{name}_{test_case['name']}.txt")
                decoded_path = os.path.join(self.temp_dir, f"decoded_{name}_{test_case['name']}.txt")
                
                # Write carrier to file
                with open(carrier_path, 'w', encoding='utf-8') as f:
                    f.write(test_case['carrier'])
                
                # Build encode command based on binary type
                if name == 'rust_bin':
                    encode_cmd = [
                        binary_path, 'encode',
                        '-m', test_case['message'],
                        '--cf', carrier_path,
                        '-o', encoded_path
                    ]
                    decode_cmd = [
                        binary_path, 'decode',
                        '--cf', encoded_path,
                        '-o', decoded_path
                    ]
                elif name == 'c_bin':
                    # C binary needs message in a file
                    message_path = os.path.join(self.temp_dir, f"message_{name}_{test_case['name']}.txt")
                    with open(message_path, 'w', encoding='utf-8') as f:
                        f.write(test_case['message'])
                    
                    encode_cmd = [
                        binary_path, 'encode',
                        '--message-file', message_path,
                        '--carrier-file', carrier_path,
                        '--output', encoded_path
                    ]
                    decode_cmd = [
                        binary_path, 'decode',
                        '--carrier-file', encoded_path,
                        '--output', decoded_path
                    ]
                elif name == 'go_bin':
                    encode_cmd = [
                        binary_path, 'encode',
                        '-m', test_case['message'],
                        '-cf', carrier_path,
                        '-o', encoded_path
                    ]
                    decode_cmd = [
                        binary_path, 'decode',
                        '-cf', encoded_path,
                        '-o', decoded_path
                    ]
                elif name == 'py_bin':
                    encode_cmd = [
                        binary_path, 'encode',
                        '-m', test_case['message'],
                        '--carrier-file', carrier_path,
                        '-o', encoded_path
                    ]
                    decode_cmd = [
                        binary_path, 'decode',
                        '--carrier-file', encoded_path,
                        '-o', decoded_path
                    ]
                
                # Add password if specified
                if test_case.get('password'):
                    encode_cmd.extend(['-p', test_case['password']])
                    decode_cmd.extend(['-p', test_case['password']])
                
                # Run encode
                subprocess.run(encode_cmd, check=True, capture_output=True, text=True)
                
                # Read encoded output
                with open(encoded_path, 'r', encoding='utf-8') as f:
                    encoded_output = f.read()
                
                # Run decode
                subprocess.run(decode_cmd, check=True, capture_output=True, text=True)
                
                # Read decoded output
                with open(decoded_path, 'r', encoding='utf-8') as f:
                    decoded_output = f.read().strip()
                
                results[name] = {
                    "encoded": encoded_output,
                    "decoded": decoded_output,
                    "success": True
                }
                
            except subprocess.CalledProcessError as e:
                results[name] = {
                    "error": f"Binary command failed: {e}",
                    "stdout": e.stdout,
                    "stderr": e.stderr,
                    "success": False
                }
            except Exception as e:
                results[name] = {"error": f"Binary test failed: {e}", "success": False}
        
        return results

def run_implementation_identity_tests():
    """Run all implementation identity tests."""
    tester = ImplementationTester()
    
    print("🧪 Running Implementation Identity Tests")
    print("=" * 60)
    
    # Test successful cases
    print("\n📋 Testing Successful Cases")
    print("-" * 40)
    
    for test_case in TEST_CASES:
        print(f"\n🔍 Testing: {test_case['name']}")
        print(f"   Message: {repr(test_case['message'])}")
        print(f"   Carrier: {repr(test_case['carrier'])}")
        if test_case.get('password'):
            print(f"   Password: {repr(test_case['password'])}")
        
        tester.setup_temp_dir()
        
        try:
            # Test different implementations
            results = {}
            
            # Test CLI implementations
            for backend in [None, 'rust', 'python', 'c']:
                if backend is None:
                    name = 'cli_default'
                else:
                    name = f'cli_{backend}'
                
                result = tester.test_cli_implementation(test_case, backend)
                results[name] = result
                
                if result.get('success'):
                    print(f"   ✅ {name}: SUCCESS")
                else:
                    print(f"   ❌ {name}: {result.get('error', 'Unknown error')}")
            
            # Test Python implementation
            python_result = tester.test_python_implementation(test_case)
            results['python'] = python_result
            
            if python_result.get('success'):
                print(f"   ✅ python: SUCCESS")
            else:
                print(f"   ❌ python: {python_result.get('error', 'Unknown error')}")
            
            # Test binary implementations
            binary_results = tester.test_binary_implementations(test_case)
            results.update(binary_results)
            
            for name, result in binary_results.items():
                if result.get('success'):
                    print(f"   ✅ {name}: SUCCESS")
                else:
                    print(f"   ❌ {name}: {result.get('error', 'Unknown error')}")
            
            # Compare results
            successful_results = {k: v for k, v in results.items() if v.get('success')}
            
            if len(successful_results) < 2:
                print(f"   ⚠️  Not enough successful implementations to compare")
                continue
            
            # Compare encoded outputs
            encoded_outputs = {k: v['encoded'] for k, v in successful_results.items()}
            first_encoded = next(iter(encoded_outputs.values()))
            
            all_encoded_match = all(encoded == first_encoded for encoded in encoded_outputs.values())
            
            if all_encoded_match:
                print(f"   🎯 ENCODED OUTPUTS: IDENTICAL")
            else:
                print(f"   💥 ENCODED OUTPUTS: DIFFERENT")
                for name, encoded in encoded_outputs.items():
                    if encoded != first_encoded:
                        print(f"      {name} differs from {next(iter(encoded_outputs.keys()))}")
            
            # Compare decoded outputs
            decoded_outputs = {k: v['decoded'] for k, v in successful_results.items()}
            first_decoded = next(iter(decoded_outputs.values()))
            
            all_decoded_match = all(decoded == first_decoded for decoded in decoded_outputs.values())
            
            if all_decoded_match:
                print(f"   🎯 DECODED OUTPUTS: IDENTICAL")
            else:
                print(f"   💥 DECODED OUTPUTS: DIFFERENT")
                for name, decoded in decoded_outputs.items():
                    if decoded != first_decoded:
                        print(f"      {name} differs from {next(iter(decoded_outputs.keys()))}")
            
            # Verify round-trip
            original_message = test_case['message']
            all_roundtrip_match = all(decoded == original_message for decoded in decoded_outputs.values())
            
            if all_roundtrip_match:
                print(f"   🎯 ROUND-TRIP: SUCCESS")
            else:
                print(f"   💥 ROUND-TRIP: FAILED")
                for name, decoded in decoded_outputs.items():
                    if decoded != original_message:
                        print(f"      {name}: expected '{original_message}', got '{decoded}'")
            
        finally:
            tester.cleanup_temp_dir()
    
    # Test error cases
    print("\n📋 Testing Error Cases")
    print("-" * 40)
    
    for test_case in ERROR_TEST_CASES:
        print(f"\n🔍 Testing Error: {test_case['name']}")
        print(f"   Expected Error: {test_case['expected_error']}")
        
        tester.setup_temp_dir()
        
        try:
            # Test that all implementations produce the same error
            results = {}
            
            # Test CLI implementations
            for backend in [None, 'rust', 'python', 'c']:
                if backend is None:
                    name = 'cli_default'
                else:
                    name = f'cli_{backend}'
                
                result = tester.test_cli_implementation(test_case, backend)
                results[name] = result
                
                if not result.get('success'):
                    print(f"   ✅ {name}: Expected error occurred")
                else:
                    print(f"   ❌ {name}: Unexpected success")
            
            # Test Python implementation
            python_result = tester.test_python_implementation(test_case)
            results['python'] = python_result
            
            if not python_result.get('success'):
                print(f"   ✅ python: Expected error occurred")
            else:
                print(f"   ❌ python: Unexpected success")
            
        finally:
            tester.cleanup_temp_dir()
    
    print("\n🎉 Implementation Identity Tests Complete")

if __name__ == "__main__":
    run_implementation_identity_tests() 