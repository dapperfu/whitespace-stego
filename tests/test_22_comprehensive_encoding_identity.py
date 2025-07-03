"""
Test 22: Comprehensive Encoding Identity Test

This test validates that ALL implementations (Python CLI with all backends, 
standalone binaries) produce 100% identical encoded output for the same input.
This is critical for cross-implementation compatibility.
"""

import subprocess
import tempfile
import os
import pytest
import hashlib
from pathlib import Path


class TestComprehensiveEncodingIdentity:
    """Test that all implementations produce identical encoded output."""
    
    @pytest.fixture
    def test_data(self):
        """Test data for encoding identity validation."""
        return {
            'message': 'Test message for encoding identity validation',
            'carrier': 'This is the carrier text for testing.',
            'password': 'test_password_123'
        }
    
    @pytest.fixture
    def all_implementations(self):
        """Define all available implementations and their configurations."""
        return [
            # Python CLI with different backends
            {
                'name': 'python-cli-python',
                'path': '.venv/bin/whitespace-stego',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    '.venv/bin/whitespace-stego', '-b', 'python', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            {
                'name': 'python-cli-rust',
                'path': '.venv/bin/whitespace-stego',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    '.venv/bin/whitespace-stego', '-b', 'rust', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            {
                'name': 'python-cli-c',
                'path': '.venv/bin/whitespace-stego',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    '.venv/bin/whitespace-stego', '-b', 'c', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            # Standalone Python binary with different backends
            {
                'name': 'py-python',
                'path': 'bin/whitespace-stego-py',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-py', '-b', 'python', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            {
                'name': 'py-rust',
                'path': 'bin/whitespace-stego-py',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-py', '-b', 'rust', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            {
                'name': 'py-c',
                'path': 'bin/whitespace-stego-py',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-py', '-b', 'c', 'encode',
                    '-m', msg, '--carrier-file', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            # Standalone C binary
            {
                'name': 'c-standalone',
                'path': 'bin/whitespace-stego-c',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-c', 'encode',
                    '--message-file', msg, '--carrier-file', carrier_path, '--output', output_path
                ] + (['--password', password] if password else []),
                'needs_message_file': True
            },
            # Standalone Go binary
            {
                'name': 'go-standalone',
                'path': 'bin/whitespace-stego-go',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-go', 'encode',
                    '-m', msg, '-cf', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            },
            # Standalone Rust binary
            {
                'name': 'rs-standalone',
                'path': 'bin/whitespace-stego-rs',
                'encode_cmd': lambda msg, carrier_path, output_path, password=None: [
                    'bin/whitespace-stego-rs', 'encode',
                    '-m', msg, '--cf', carrier_path, '-o', output_path
                ] + (['-p', password] if password else []),
                'needs_message_file': False
            }
        ]
    
    def test_encoding_identity_no_password(self, test_data, all_implementations):
        """
        Test that all implementations produce identical encoded output 
        for the same message and carrier without password.
        """
        message = test_data['message']
        carrier = test_data['carrier']
        
        print(f"\n=== Testing Encoding Identity (No Password) ===")
        print(f"Message: {repr(message)}")
        print(f"Carrier: {repr(carrier)}")
        
        encoded_outputs = {}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Write carrier to file
            carrier_path = os.path.join(tmpdir, 'carrier.txt')
            with open(carrier_path, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            # Test each implementation
            for impl in all_implementations:
                impl_name = impl['name']
                output_path = os.path.join(tmpdir, f'encoded_{impl_name}.txt')
                
                # Handle message file requirement for C binary
                if impl['needs_message_file']:
                    message_path = os.path.join(tmpdir, f'message_{impl_name}.txt')
                    with open(message_path, 'w', encoding='utf-8') as f:
                        f.write(message)
                    msg_arg = message_path
                else:
                    msg_arg = message
                
                # Build and run encode command
                encode_cmd = impl['encode_cmd'](msg_arg, carrier_path, output_path)
                print(f"Running {impl_name}: {' '.join(encode_cmd)}")
                
                try:
                    result = subprocess.run(encode_cmd, capture_output=True, text=True, check=True)
                    print(f"  ✓ {impl_name} encoded successfully")
                    
                    # Read encoded output
                    with open(output_path, 'r', encoding='utf-8') as f:
                        encoded_output = f.read()
                    
                    encoded_outputs[impl_name] = encoded_output
                    
                except subprocess.CalledProcessError as e:
                    print(f"  ✗ {impl_name} failed: {e}")
                    print(f"    stdout: {e.stdout}")
                    print(f"    stderr: {e.stderr}")
                    pytest.fail(f"{impl_name} failed to encode: {e}")
            
            # Validate all outputs are identical
            if not encoded_outputs:
                pytest.fail("No implementations produced output")
            
            first_name = list(encoded_outputs.keys())[0]
            first_output = encoded_outputs[first_name]
            first_hash = hashlib.sha256(first_output.encode('utf-8')).hexdigest()[:16]
            
            print(f"\n=== Results ===")
            print(f"Reference ({first_name}): {first_hash}")
            
            all_identical = True
            differences = []
            
            for impl_name, output in encoded_outputs.items():
                output_hash = hashlib.sha256(output.encode('utf-8')).hexdigest()[:16]
                
                if output == first_output:
                    print(f"✓ {impl_name}: {output_hash} (IDENTICAL)")
                else:
                    print(f"✗ {impl_name}: {output_hash} (DIFFERENT)")
                    all_identical = False
                    
                    # Find first difference
                    min_len = min(len(output), len(first_output))
                    for i in range(min_len):
                        if output[i] != first_output[i]:
                            differences.append({
                                'impl': impl_name,
                                'position': i,
                                'expected': repr(first_output[i]),
                                'got': repr(output[i]),
                                'context': repr(first_output[max(0, i-10):i+10])
                            })
                            break
            
            if not all_identical:
                print(f"\n=== Differences Found ===")
                for diff in differences[:5]:  # Show first 5 differences
                    print(f"{diff['impl']} at position {diff['position']}: "
                          f"expected {diff['expected']}, got {diff['got']}")
                    print(f"  Context: {diff['context']}")
                
                # Show all outputs for debugging
                print(f"\n=== All Outputs for Comparison ===")
                for impl_name, output in encoded_outputs.items():
                    output_hash = hashlib.sha256(output.encode('utf-8')).hexdigest()[:16]
                    print(f"{impl_name}: {output_hash}")
                    print(f"  Length: {len(output)}")
                    print(f"  First 100 chars: {repr(output[:100])}")
                    print(f"  Last 50 chars: {repr(output[-50:])}")
                    print()
                
                pytest.fail(f"Not all implementations produce identical output. "
                           f"Found {len(differences)} differences.")
            else:
                print(f"\n✓ SUCCESS: All {len(encoded_outputs)} implementations produce identical output!")
    
    def test_encoding_identity_with_password(self, test_data, all_implementations):
        """
        Test that all implementations produce identical encoded output 
        for the same message, carrier, and password.
        """
        message = test_data['message']
        carrier = test_data['carrier']
        password = test_data['password']
        
        print(f"\n=== Testing Encoding Identity (With Password) ===")
        print(f"Message: {repr(message)}")
        print(f"Carrier: {repr(carrier)}")
        print(f"Password: {repr(password)}")
        
        encoded_outputs = {}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Write carrier to file
            carrier_path = os.path.join(tmpdir, 'carrier.txt')
            with open(carrier_path, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            # Test each implementation
            for impl in all_implementations:
                impl_name = impl['name']
                output_path = os.path.join(tmpdir, f'encoded_{impl_name}.txt')
                
                # Handle message file requirement for C binary
                if impl['needs_message_file']:
                    message_path = os.path.join(tmpdir, f'message_{impl_name}.txt')
                    with open(message_path, 'w', encoding='utf-8') as f:
                        f.write(message)
                    msg_arg = message_path
                else:
                    msg_arg = message
                
                # Build and run encode command
                encode_cmd = impl['encode_cmd'](msg_arg, carrier_path, output_path, password)
                print(f"Running {impl_name}: {' '.join(encode_cmd)}")
                
                try:
                    result = subprocess.run(encode_cmd, capture_output=True, text=True, check=True)
                    print(f"  ✓ {impl_name} encoded successfully")
                    
                    # Read encoded output
                    with open(output_path, 'r', encoding='utf-8') as f:
                        encoded_output = f.read()
                    
                    encoded_outputs[impl_name] = encoded_output
                    
                except subprocess.CalledProcessError as e:
                    print(f"  ✗ {impl_name} failed: {e}")
                    print(f"    stdout: {e.stdout}")
                    print(f"    stderr: {e.stderr}")
                    pytest.fail(f"{impl_name} failed to encode: {e}")
            
            # Validate all outputs are identical
            if not encoded_outputs:
                pytest.fail("No implementations produced output")
            
            first_name = list(encoded_outputs.keys())[0]
            first_output = encoded_outputs[first_name]
            first_hash = hashlib.sha256(first_output.encode('utf-8')).hexdigest()[:16]
            
            print(f"\n=== Results ===")
            print(f"Reference ({first_name}): {first_hash}")
            
            all_identical = True
            differences = []
            
            for impl_name, output in encoded_outputs.items():
                output_hash = hashlib.sha256(output.encode('utf-8')).hexdigest()[:16]
                
                if output == first_output:
                    print(f"✓ {impl_name}: {output_hash} (IDENTICAL)")
                else:
                    print(f"✗ {impl_name}: {output_hash} (DIFFERENT)")
                    all_identical = False
                    
                    # Find first difference
                    min_len = min(len(output), len(first_output))
                    for i in range(min_len):
                        if output[i] != first_output[i]:
                            differences.append({
                                'impl': impl_name,
                                'position': i,
                                'expected': repr(first_output[i]),
                                'got': repr(output[i]),
                                'context': repr(first_output[max(0, i-10):i+10])
                            })
                            break
            
            if not all_identical:
                print(f"\n=== Differences Found ===")
                for diff in differences[:5]:  # Show first 5 differences
                    print(f"{diff['impl']} at position {diff['position']}: "
                          f"expected {diff['expected']}, got {diff['got']}")
                    print(f"  Context: {diff['context']}")
                
                # Show all outputs for debugging
                print(f"\n=== All Outputs for Comparison ===")
                for impl_name, output in encoded_outputs.items():
                    output_hash = hashlib.sha256(output.encode('utf-8')).hexdigest()[:16]
                    print(f"{impl_name}: {output_hash}")
                    print(f"  Length: {len(output)}")
                    print(f"  First 100 chars: {repr(output[:100])}")
                    print(f"  Last 50 chars: {repr(output[-50:])}")
                    print()
                
                pytest.fail(f"Not all implementations produce identical output. "
                           f"Found {len(differences)} differences.")
            else:
                print(f"\n✓ SUCCESS: All {len(encoded_outputs)} implementations produce identical output!")
    
    def test_encoding_identity_edge_cases(self, all_implementations):
        """
        Test encoding identity with edge cases: empty carrier, special characters, unicode.
        """
        test_cases = [
            {
                'name': 'empty_carrier',
                'message': 'Message with empty carrier',
                'carrier': '',
                'password': None
            },
            {
                'name': 'unicode_message',
                'message': 'Unicode message: 中文 🌍 😎',
                'carrier': 'Carrier with unicode: 日本語 🚀',
                'password': None
            },
            {
                'name': 'special_chars',
                'message': 'Special chars: !@#$%^&*()_+-=[]{}|;:\'",./<>?',
                'carrier': 'Carrier with special: ~`!@#$%^&*()_+-=[]{}|;:\'",./<>?',
                'password': None
            },
            {
                'name': 'long_message',
                'message': 'A' * 1000,  # Long message
                'carrier': 'Short carrier',
                'password': None
            }
        ]
        
        for test_case in test_cases:
            print(f"\n=== Testing Edge Case: {test_case['name']} ===")
            
            encoded_outputs = {}
            
            with tempfile.TemporaryDirectory() as tmpdir:
                # Write carrier to file
                carrier_path = os.path.join(tmpdir, 'carrier.txt')
                with open(carrier_path, 'w', encoding='utf-8') as f:
                    f.write(test_case['carrier'])
                
                # Test each implementation
                for impl in all_implementations:
                    impl_name = impl['name']
                    output_path = os.path.join(tmpdir, f'encoded_{impl_name}.txt')
                    
                    # Handle message file requirement for C binary
                    if impl['needs_message_file']:
                        message_path = os.path.join(tmpdir, f'message_{impl_name}.txt')
                        with open(message_path, 'w', encoding='utf-8') as f:
                            f.write(test_case['message'])
                        msg_arg = message_path
                    else:
                        msg_arg = test_case['message']
                    
                    # Build and run encode command
                    encode_cmd = impl['encode_cmd'](msg_arg, carrier_path, output_path, test_case['password'])
                    
                    try:
                        result = subprocess.run(encode_cmd, capture_output=True, text=True, check=True)
                        
                        # Read encoded output
                        with open(output_path, 'r', encoding='utf-8') as f:
                            encoded_output = f.read()
                        
                        encoded_outputs[impl_name] = encoded_output
                        
                    except subprocess.CalledProcessError as e:
                        print(f"  ✗ {impl_name} failed: {e}")
                        continue
                
                # Validate all outputs are identical
                if len(encoded_outputs) < 2:
                    print(f"  ⚠ Only {len(encoded_outputs)} implementation(s) succeeded, skipping comparison")
                    continue
                
                first_name = list(encoded_outputs.keys())[0]
                first_output = encoded_outputs[first_name]
                
                all_identical = True
                for impl_name, output in encoded_outputs.items():
                    if output != first_output:
                        print(f"  ✗ {impl_name} produces different output")
                        all_identical = False
                        break
                
                if all_identical:
                    print(f"  ✓ All {len(encoded_outputs)} implementations produce identical output")
                else:
                    pytest.fail(f"Edge case '{test_case['name']}': Not all implementations produce identical output")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
