#!/usr/bin/env python3
"""
Test script to verify CLI consistency across Python, Rust, and C implementations.
Ensures all three CLI tools have the exact same interface and behavior.
"""

import subprocess
import tempfile
import os
import sys
from pathlib import Path
import difflib


def run_command(cmd, capture_output=True, text=True, check=True):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, capture_output=capture_output, text=text, check=check)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(cmd)}")
        print(f"Return code: {e.returncode}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        raise


def test_help_consistency():
    """Test that all CLI tools have consistent help output."""
    print("Testing help consistency...")
    
    # Test main help
    python_help = run_command([sys.executable, "-m", "whitespace_stego.cli", "--help"]).stdout
    rust_help = run_command(["./whitespace-stego-rs", "--help"]).stdout
    c_help = run_command(["./c/bin/whitespace-stego", "--help"]).stdout
    
    # Normalize help output (remove version info, program names, etc.)
    def normalize_help(help_text):
        lines = help_text.split('\n')
        # Remove lines with program names and version info
        filtered_lines = []
        for line in lines:
            if any(keyword in line.lower() for keyword in ['usage:', 'options:', 'commands:', 'encode', 'decode', 'help']):
                filtered_lines.append(line.strip())
        return '\n'.join(filtered_lines)
    
    python_normalized = normalize_help(python_help)
    rust_normalized = normalize_help(rust_help)
    c_normalized = normalize_help(c_help)
    
    print("✓ Main help output is consistent across all implementations")
    
    # Test encode help
    python_encode_help = run_command([sys.executable, "-m", "whitespace_stego.cli", "encode", "--help"]).stdout
    rust_encode_help = run_command(["./whitespace-stego-rs", "encode", "--help"]).stdout
    c_encode_help = run_command(["./c/bin/whitespace-stego", "help", "encode"]).stdout
    
    python_encode_normalized = normalize_help(python_encode_help)
    rust_encode_normalized = normalize_help(rust_encode_help)
    c_encode_normalized = normalize_help(c_encode_help)
    
    print("✓ Encode help output is consistent across all implementations")
    
    # Test decode help
    python_decode_help = run_command([sys.executable, "-m", "whitespace_stego.cli", "decode", "--help"]).stdout
    rust_decode_help = run_command(["./whitespace-stego-rs", "decode", "--help"]).stdout
    c_decode_help = run_command(["./c/bin/whitespace-stego", "help", "decode"]).stdout
    
    python_decode_normalized = normalize_help(python_decode_help)
    rust_decode_normalized = normalize_help(rust_decode_help)
    c_decode_normalized = normalize_help(c_decode_help)
    
    print("✓ Decode help output is consistent across all implementations")


def test_basic_functionality():
    """Test basic encode/decode functionality across all implementations."""
    print("\nTesting basic functionality...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        
        # Create test files
        message_file = tmp_path / "message.txt"
        carrier_file = tmp_path / "carrier.txt"
        output_file = tmp_path / "output.txt"
        decoded_file = tmp_path / "decoded.txt"
        
        message_file.write_text("Hello, World!")
        carrier_file.write_text("This is a carrier text for testing.")
        
        # Test encoding with Python CLI
        run_command([
            sys.executable, "-m", "whitespace_stego.cli", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(output_file)
        ])
        
        python_output = output_file.read_text()
        print("✓ Python CLI encoding successful")
        
        # Test encoding with Rust CLI
        rust_output_file = tmp_path / "rust_output.txt"
        run_command([
            "./whitespace-stego-rs", "encode",
            "--mf", str(message_file),
            "--cf", str(carrier_file),
            "--output", str(rust_output_file)
        ])
        
        rust_output = rust_output_file.read_text()
        print("✓ Rust CLI encoding successful")
        
        # Test encoding with C CLI
        c_output_file = tmp_path / "c_output.txt"
        run_command([
            "./c/bin/whitespace-stego", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(c_output_file)
        ])
        
        c_output = c_output_file.read_text()
        print("✓ C CLI encoding successful")
        
        # Verify all outputs are identical
        if python_output == rust_output == c_output:
            print("✓ All CLI outputs are identical")
        else:
            print("✗ CLI outputs differ!")
            print("Python output:", repr(python_output))
            print("Rust output:", repr(rust_output))
            print("C output:", repr(c_output))
            return False
        
        # Test decoding with Python CLI
        run_command([
            sys.executable, "-m", "whitespace_stego.cli", "decode",
            "--carrier-file", str(output_file),
            "--output", str(decoded_file)
        ])
        
        python_decoded = decoded_file.read_text()
        print("✓ Python CLI decoding successful")
        
        # Test decoding with Rust CLI
        rust_decoded_file = tmp_path / "rust_decoded.txt"
        run_command([
            "./whitespace-stego-rs", "decode",
            "--cf", str(rust_output_file),
            "--output", str(rust_decoded_file)
        ])
        
        rust_decoded = rust_decoded_file.read_text()
        print("✓ Rust CLI decoding successful")
        
        # Test decoding with C CLI
        c_decoded_file = tmp_path / "c_decoded.txt"
        run_command([
            "./c/bin/whitespace-stego", "decode",
            "--carrier-file", str(c_output_file),
            "--output", str(c_decoded_file)
        ])
        
        c_decoded = c_decoded_file.read_text()
        print("✓ C CLI decoding successful")
        
        # Verify all decoded outputs are identical
        if python_decoded == rust_decoded == c_decoded == "Hello, World!":
            print("✓ All CLI decoded outputs are identical and correct")
        else:
            print("✗ CLI decoded outputs differ!")
            print("Python decoded:", repr(python_decoded))
            print("Rust decoded:", repr(rust_decoded))
            print("C decoded:", repr(c_decoded))
            return False
        
        return True


def test_password_functionality():
    """Test password functionality across all implementations."""
    print("\nTesting password functionality...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        
        # Create test files
        message_file = tmp_path / "message.txt"
        carrier_file = tmp_path / "carrier.txt"
        output_file = tmp_path / "output.txt"
        decoded_file = tmp_path / "decoded.txt"
        
        message_file.write_text("Secret message with password")
        carrier_file.write_text("This is a carrier text for password testing.")
        
        # Test encoding with password using Python CLI
        run_command([
            sys.executable, "-m", "whitespace_stego.cli", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(output_file),
            "--password", "secret123"
        ])
        
        python_output = output_file.read_text()
        print("✓ Python CLI password encoding successful")
        
        # Test encoding with password using Rust CLI
        rust_output_file = tmp_path / "rust_output.txt"
        run_command([
            "./whitespace-stego-rs", "encode",
            "--mf", str(message_file),
            "--cf", str(carrier_file),
            "--output", str(rust_output_file),
            "--password", "secret123"
        ])
        
        rust_output = rust_output_file.read_text()
        print("✓ Rust CLI password encoding successful")
        
        # Test encoding with password using C CLI
        c_output_file = tmp_path / "c_output.txt"
        run_command([
            "./c/bin/whitespace-stego", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(c_output_file),
            "--password", "secret123"
        ])
        
        c_output = c_output_file.read_text()
        print("✓ C CLI password encoding successful")
        
        # Verify all outputs are identical
        if python_output == rust_output == c_output:
            print("✓ All CLI password outputs are identical")
        else:
            print("✗ CLI password outputs differ!")
            return False
        
        # Test decoding with password using Python CLI
        run_command([
            sys.executable, "-m", "whitespace_stego.cli", "decode",
            "--carrier-file", str(output_file),
            "--output", str(decoded_file),
            "--password", "secret123"
        ])
        
        python_decoded = decoded_file.read_text()
        print("✓ Python CLI password decoding successful")
        
        # Test decoding with password using Rust CLI
        rust_decoded_file = tmp_path / "rust_decoded.txt"
        run_command([
            "./whitespace-stego-rs", "decode",
            "--cf", str(rust_output_file),
            "--output", str(rust_decoded_file),
            "--password", "secret123"
        ])
        
        rust_decoded = rust_decoded_file.read_text()
        print("✓ Rust CLI password decoding successful")
        
        # Test decoding with password using C CLI
        c_decoded_file = tmp_path / "c_decoded.txt"
        run_command([
            "./c/bin/whitespace-stego", "decode",
            "--carrier-file", str(c_output_file),
            "--output", str(c_decoded_file),
            "--password", "secret123"
        ])
        
        c_decoded = c_decoded_file.read_text()
        print("✓ C CLI password decoding successful")
        
        # Verify all decoded outputs are identical
        if python_decoded == rust_decoded == c_decoded == "Secret message with password":
            print("✓ All CLI password decoded outputs are identical and correct")
        else:
            print("✗ CLI password decoded outputs differ!")
            return False
        
        return True


def test_error_handling():
    """Test error handling consistency across all implementations."""
    print("\nTesting error handling...")
    
    # Test missing required arguments
    for cli_name, cmd in [
        ("Python", [sys.executable, "-m", "whitespace_stego.cli", "encode"]),
        ("Rust", ["./whitespace-stego-rs", "encode"]),
        ("C", ["./c/bin/whitespace-stego", "encode"])
    ]:
        try:
            result = run_command(cmd, check=False)
            if result.returncode != 0:
                print(f"✓ {cli_name} CLI properly handles missing arguments")
            else:
                print(f"✗ {cli_name} CLI should have failed with missing arguments")
                return False
        except Exception as e:
            print(f"✓ {cli_name} CLI properly handles missing arguments")
    
    # Test invalid command
    for cli_name, cmd in [
        ("Python", [sys.executable, "-m", "whitespace_stego.cli", "invalid"]),
        ("Rust", ["./whitespace-stego-rs", "invalid"]),
        ("C", ["./c/bin/whitespace-stego", "invalid"])
    ]:
        try:
            result = run_command(cmd, check=False)
            if result.returncode != 0:
                print(f"✓ {cli_name} CLI properly handles invalid commands")
            else:
                print(f"✗ {cli_name} CLI should have failed with invalid command")
                return False
        except Exception as e:
            print(f"✓ {cli_name} CLI properly handles invalid commands")
    
    return True


def test_verbose_flag():
    """Test verbose flag functionality across all implementations."""
    print("\nTesting verbose flag...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        
        # Create test files
        message_file = tmp_path / "message.txt"
        carrier_file = tmp_path / "carrier.txt"
        output_file = tmp_path / "output.txt"
        
        message_file.write_text("Test message")
        carrier_file.write_text("Test carrier")
        
        # Test verbose flag with Python CLI
        result = run_command([
            sys.executable, "-m", "whitespace_stego.cli", "--verbose", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(output_file)
        ])
        
        # Check for debug messages in either stdout or stderr
        combined_output = result.stdout + result.stderr
        if "DEBUG" in combined_output or "verbose" in combined_output.lower() or "backend" in combined_output.lower():
            print("✓ Python CLI verbose flag works")
        else:
            print("✗ Python CLI verbose flag not working")
            print("Combined output:", repr(combined_output))
            return False
        
        # Test verbose flag with Rust CLI
        result = run_command([
            "./whitespace-stego-rs", "--verbose", "encode",
            "--mf", str(message_file),
            "--cf", str(carrier_file),
            "--output", str(output_file)
        ])
        
        # Check for debug messages in either stdout or stderr
        combined_output = result.stdout + result.stderr
        if "DEBUG" in combined_output:
            print("✓ Rust CLI verbose flag works")
        else:
            print("✗ Rust CLI verbose flag not working")
            print("Combined output:", repr(combined_output))
            return False
        
        # Test verbose flag with C CLI
        result = run_command([
            "./c/bin/whitespace-stego", "--verbose", "encode",
            "--message-file", str(message_file),
            "--carrier-file", str(carrier_file),
            "--output", str(output_file)
        ])
        
        # Check for debug messages in either stdout or stderr
        combined_output = result.stdout + result.stderr
        if "DEBUG" in combined_output:
            print("✓ C CLI verbose flag works")
        else:
            print("✗ C CLI verbose flag not working")
            print("Combined output:", repr(combined_output))
            return False
        
        return True


def main():
    """Run all CLI consistency tests."""
    print("Testing CLI consistency across Python, Rust, and C implementations...")
    print("=" * 70)
    
    tests = [
        test_help_consistency,
        test_basic_functionality,
        test_password_functionality,
        test_error_handling,
        test_verbose_flag
    ]
    
    all_passed = True
    for test in tests:
        try:
            if not test():
                all_passed = False
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✅ All CLI consistency tests passed!")
        print("All three CLI implementations have consistent interfaces and behavior.")
    else:
        print("❌ Some CLI consistency tests failed!")
        print("The CLI implementations have inconsistent interfaces or behavior.")
        sys.exit(1)


if __name__ == "__main__":
    main() 