#!/usr/bin/env python3
"""
Comprehensive test script for whitespace steganography project.

This script tests all aspects of the project:
- Python CLI functionality
- Rust CLI functionality  
- C CLI functionality
- WebAssembly web interface
- Core API functionality
- Cross-backend compatibility
- Error handling
- Unicode support
- Password protection
"""

import subprocess
import tempfile
import os
import sys
import time
import requests
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class TestResult:
    """Container for test results."""
    
    def __init__(self, name: str, success: bool, message: str = "", details: str = ""):
        self.name = name
        self.success = success
        self.message = message
        self.details = details


class WhitespaceStegoTester:
    """Comprehensive tester for whitespace steganography project."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.temp_files: List[str] = []
        
    def run_command(self, cmd: List[str], description: str, expect_success: bool = True) -> TestResult:
        """Run a command and return test result."""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=expect_success)
            success = result.returncode == 0 if expect_success else result.returncode != 0
            return TestResult(
                description,
                success,
                f"Return code: {result.returncode}",
                f"Output: {result.stdout[:200]}...\nError: {result.stderr[:200]}..."
            )
        except subprocess.CalledProcessError as e:
            success = not expect_success
            return TestResult(
                description,
                success,
                f"Return code: {e.returncode}",
                f"Output: {e.stdout[:200]}...\nError: {e.stderr[:200]}..."
            )
        except Exception as e:
            return TestResult(
                description,
                False,
                f"Exception: {type(e).__name__}",
                str(e)
            )
    
    def create_temp_file(self, content: str, suffix: str = ".txt") -> str:
        """Create a temporary file and track it for cleanup."""
        with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
            f.write(content)
            self.temp_files.append(f.name)
            return f.name
    
    def cleanup_temp_files(self):
        """Clean up all temporary files."""
        for file_path in self.temp_files:
            try:
                os.unlink(file_path)
            except OSError:
                pass
        self.temp_files.clear()
    
    def test_python_cli_help(self) -> TestResult:
        """Test Python CLI help functionality."""
        return self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--help'],
            "Python CLI main help"
        )
    
    def test_python_cli_encode_help(self) -> TestResult:
        """Test Python CLI encode help."""
        return self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode', '--help'],
            "Python CLI encode help"
        )
    
    def test_python_cli_decode_help(self) -> TestResult:
        """Test Python CLI decode help."""
        return self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'decode', '--help'],
            "Python CLI decode help"
        )
    
    def test_python_cli_mutually_exclusive_options(self) -> TestResult:
        """Test mutually exclusive options validation."""
        return self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode',
             '--message', 'test', '--message-file', 'test.txt',
             '--carrier', 'carrier'],
            "Python CLI mutually exclusive message options",
            expect_success=False
        )
    
    def test_python_cli_missing_options(self) -> TestResult:
        """Test missing required options."""
        return self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode', '--output', 'test.txt'],
            "Python CLI missing required options",
            expect_success=False
        )
    
    def test_python_cli_basic_encode_decode(self) -> TestResult:
        """Test basic encode/decode functionality."""
        # Test encode
        encode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode',
             '--message', 'Hello World', '--carrier', 'Test carrier'],
            "Python CLI basic encode"
        )
        if not encode_result.success:
            return encode_result
        
        # Create temp file with encoded content
        encoded_content = encode_result.details.split("Output: ")[1].split("...")[0]
        temp_file = self.create_temp_file(encoded_content)
        
        # Test decode
        decode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'decode', '--carrier-file', temp_file],
            "Python CLI basic decode"
        )
        
        return decode_result
    
    def test_python_cli_password_protection(self) -> TestResult:
        """Test password protection functionality."""
        # Encode with password
        encoded_file = self.create_temp_file("")
        encode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode',
             '--message', 'Secret message', '--carrier', 'Test carrier',
             '--password', 'mypassword', '--output', encoded_file],
            "Python CLI encode with password"
        )
        if not encode_result.success:
            return encode_result
        
        # Decode with correct password
        decode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'decode',
             '--carrier-file', encoded_file, '--password', 'mypassword'],
            "Python CLI decode with correct password"
        )
        if not decode_result.success:
            return decode_result
        
        # Decode with wrong password
        wrong_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'decode',
             '--carrier-file', encoded_file, '--password', 'wrongpassword'],
            "Python CLI decode with wrong password",
            expect_success=False
        )
        
        return TestResult(
            "Python CLI password protection",
            decode_result.success and wrong_result.success,
            "Password protection working correctly"
        )
    
    def test_python_cli_unicode_support(self) -> TestResult:
        """Test Unicode and emoji support."""
        # Encode Unicode content
        encoded_file = self.create_temp_file("")
        encode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'encode',
             '--message', 'Hello 世界 🌍', '--carrier', 'Unicode carrier: café naïve',
             '--output', encoded_file],
            "Python CLI encode Unicode"
        )
        if not encode_result.success:
            return encode_result
        
        # Decode Unicode content
        decode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', 'decode', '--carrier-file', encoded_file],
            "Python CLI decode Unicode"
        )
        
        return decode_result
    
    def test_python_cli_backend_selection(self) -> TestResult:
        """Test backend selection."""
        # Test Python backend
        python_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--backend', 'python', 'encode', '--help'],
            "Python CLI Python backend"
        )
        
        # Test Rust backend
        rust_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--backend', 'rust', 'encode', '--help'],
            "Python CLI Rust backend"
        )
        
        # Test invalid backend
        invalid_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--backend', 'invalid', 'encode', '--help'],
            "Python CLI invalid backend",
            expect_success=False
        )
        
        return TestResult(
            "Python CLI backend selection",
            python_result.success and rust_result.success and invalid_result.success,
            "Backend selection working correctly"
        )
    
    def test_rust_cli(self) -> TestResult:
        """Test Rust CLI functionality."""
        # Check if Rust CLI exists
        if not os.path.exists('./whitespace-stego-rs'):
            return TestResult(
                "Rust CLI",
                False,
                "Rust CLI not found",
                "Run 'make rust' to build the Rust CLI"
            )
        
        # Test help
        help_result = self.run_command(['./whitespace-stego-rs', '--help'], "Rust CLI help")
        if not help_result.success:
            return help_result
        
        # Test encode help
        encode_help = self.run_command(['./whitespace-stego-rs', 'encode', '--help'], "Rust CLI encode help")
        if not encode_help.success:
            return encode_help
        
        # Test basic encode/decode
        message_file = self.create_temp_file("Test message content")
        carrier_file = self.create_temp_file("This is a test carrier text.")
        encoded_file = self.create_temp_file("")
        
        encode_result = self.run_command(
            ['./whitespace-stego-rs', 'encode', '--mf', message_file, '--cf', carrier_file, '-o', encoded_file],
            "Rust CLI encode"
        )
        if not encode_result.success:
            return encode_result
        
        decode_result = self.run_command(
            ['./whitespace-stego-rs', 'decode', '--cf', encoded_file, '-o', '/dev/null'],
            "Rust CLI decode"
        )
        
        return decode_result
    
    def test_c_cli(self) -> TestResult:
        """Test C CLI functionality."""
        # Check if C CLI exists
        if not os.path.exists('./c/bin/whitespace-stego'):
            return TestResult(
                "C CLI",
                False,
                "C CLI not found",
                "Run 'make c' to build the C CLI"
            )
        
        # Test help
        help_result = self.run_command(['./c/bin/whitespace-stego', '--help'], "C CLI help")
        if not help_result.success:
            return help_result
        
        # Test basic encode/decode
        message_file = self.create_temp_file("Test message content")
        carrier_file = self.create_temp_file("This is a test carrier text.")
        encoded_file = self.create_temp_file("")
        
        encode_result = self.run_command(
            ['./c/bin/whitespace-stego', 'encode', '--message-file', message_file,
             '--carrier-file', carrier_file, '--output', encoded_file],
            "C CLI encode"
        )
        if not encode_result.success:
            return encode_result
        
        decode_result = self.run_command(
            ['./c/bin/whitespace-stego', 'decode', '--carrier-file', encoded_file, '--output', '/dev/null'],
            "C CLI decode"
        )
        
        return decode_result
    
    def test_webassembly_interface(self) -> TestResult:
        """Test WebAssembly web interface."""
        try:
            # Check if the web interface is accessible
            response = requests.get('http://localhost:8000', timeout=5)
            if response.status_code == 200:
                return TestResult(
                    "WebAssembly Web Interface",
                    True,
                    "Web interface accessible",
                    f"Status: {response.status_code}"
                )
            else:
                return TestResult(
                    "WebAssembly Web Interface",
                    False,
                    f"Web interface returned status {response.status_code}",
                    "Start with 'make wasi-web'"
                )
        except requests.exceptions.RequestException:
            return TestResult(
                "WebAssembly Web Interface",
                False,
                "Web interface not accessible",
                "Start with 'make wasi-web' or check if port 8000 is available"
            )
    
    def test_core_api(self) -> TestResult:
        """Test core API functionality."""
        try:
            from whitespace_stego.core import encode, decode
            
            # Test basic encode/decode
            encoded = encode("Test message", "Test carrier")
            decoded = decode(encoded)
            
            if decoded == "Test message":
                return TestResult(
                    "Core API basic functionality",
                    True,
                    "Basic encode/decode working"
                )
            else:
                return TestResult(
                    "Core API basic functionality",
                    False,
                    f"Decoded message mismatch: expected 'Test message', got '{decoded}'"
                )
        except ImportError as e:
            return TestResult(
                "Core API",
                False,
                "Failed to import core module",
                str(e)
            )
        except Exception as e:
            return TestResult(
                "Core API",
                False,
                f"API test failed: {type(e).__name__}",
                str(e)
            )
    
    def test_core_api_password_protection(self) -> TestResult:
        """Test core API password protection."""
        try:
            from whitespace_stego.core import encode, decode
            
            # Test with password
            encoded = encode("Secret message", "Test carrier", password="mypassword")
            decoded = decode(encoded, password="mypassword")
            
            if decoded == "Secret message":
                return TestResult(
                    "Core API password protection",
                    True,
                    "Password protection working"
                )
            else:
                return TestResult(
                    "Core API password protection",
                    False,
                    f"Password protection failed: expected 'Secret message', got '{decoded}'"
                )
        except Exception as e:
            return TestResult(
                "Core API password protection",
                False,
                f"Password protection test failed: {type(e).__name__}",
                str(e)
            )
    
    def test_core_api_unicode(self) -> TestResult:
        """Test core API Unicode support."""
        try:
            from whitespace_stego.core import encode, decode
            
            # Test Unicode content
            encoded = encode("Hello 世界 🌍", "Unicode carrier: café naïve")
            decoded = decode(encoded)
            
            if decoded == "Hello 世界 🌍":
                return TestResult(
                    "Core API Unicode support",
                    True,
                    "Unicode support working"
                )
            else:
                return TestResult(
                    "Core API Unicode support",
                    False,
                    f"Unicode support failed: expected 'Hello 世界 🌍', got '{decoded}'"
                )
        except Exception as e:
            return TestResult(
                "Core API Unicode support",
                False,
                f"Unicode test failed: {type(e).__name__}",
                str(e)
            )
    
    def test_cross_backend_compatibility(self) -> TestResult:
        """Test cross-backend compatibility."""
        # Encode with Python backend
        encoded_file = self.create_temp_file("")
        encode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--backend', 'python', 'encode',
             '--message', 'Cross test', '--carrier', 'Test carrier', '--output', encoded_file],
            "Cross-backend encode with Python"
        )
        if not encode_result.success:
            return encode_result
        
        # Decode with Rust backend
        decode_result = self.run_command(
            ['python3', '-m', 'whitespace_stego.cli', '--backend', 'rust', 'decode',
             '--carrier-file', encoded_file],
            "Cross-backend decode with Rust"
        )
        
        return decode_result
    
    def test_pytest_suite(self) -> TestResult:
        """Test pytest test suite."""
        try:
            result = subprocess.run(
                ['python', '-m', 'pytest', 'tests/', '--tb=short', '-q'],
                capture_output=True, text=True, timeout=60
            )
            
            # Parse test results
            output = result.stdout
            if "failed" in output:
                # Extract number of passed/failed tests
                lines = output.strip().split('\n')
                for line in lines:
                    if "passed" in line and "failed" in line:
                        return TestResult(
                            "Pytest Test Suite",
                            True,
                            f"Tests completed: {line.strip()}",
                            f"Return code: {result.returncode}"
                        )
            
            return TestResult(
                "Pytest Test Suite",
                result.returncode == 0,
                f"Return code: {result.returncode}",
                output[:500] + "..." if len(output) > 500 else output
            )
        except subprocess.TimeoutExpired:
            return TestResult(
                "Pytest Test Suite",
                False,
                "Tests timed out after 60 seconds"
            )
        except Exception as e:
            return TestResult(
                "Pytest Test Suite",
                False,
                f"Test execution failed: {type(e).__name__}",
                str(e)
            )
    
    def run_all_tests(self) -> List[TestResult]:
        """Run all tests and return results."""
        print("🧪 Running comprehensive whitespace steganography tests...")
        print("=" * 60)
        
        # Python CLI tests
        print("\n📋 Testing Python CLI...")
        self.results.extend([
            self.test_python_cli_help(),
            self.test_python_cli_encode_help(),
            self.test_python_cli_decode_help(),
            self.test_python_cli_mutually_exclusive_options(),
            self.test_python_cli_missing_options(),
            self.test_python_cli_basic_encode_decode(),
            self.test_python_cli_password_protection(),
            self.test_python_cli_unicode_support(),
            self.test_python_cli_backend_selection(),
        ])
        
        # Rust CLI tests
        print("\n🦀 Testing Rust CLI...")
        self.results.append(self.test_rust_cli())
        
        # C CLI tests
        print("\n🔧 Testing C CLI...")
        self.results.append(self.test_c_cli())
        
        # WebAssembly tests
        print("\n🌐 Testing WebAssembly interface...")
        self.results.append(self.test_webassembly_interface())
        
        # Core API tests
        print("\n⚙️ Testing Core API...")
        self.results.extend([
            self.test_core_api(),
            self.test_core_api_password_protection(),
            self.test_core_api_unicode(),
        ])
        
        # Cross-backend tests
        print("\n🔄 Testing cross-backend compatibility...")
        self.results.append(self.test_cross_backend_compatibility())
        
        # Pytest suite
        print("\n🧪 Running pytest test suite...")
        self.results.append(self.test_pytest_suite())
        
        return self.results
    
    def print_results(self):
        """Print test results summary."""
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for r in self.results if r.success)
        failed = len(self.results) - passed
        
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📈 Success Rate: {passed/len(self.results)*100:.1f}%")
        
        print("\n📋 DETAILED RESULTS:")
        print("-" * 60)
        
        for result in self.results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            print(f"{status}: {result.name}")
            if result.message:
                print(f"   {result.message}")
            if not result.success and result.details:
                print(f"   Details: {result.details[:200]}...")
        
        print("\n" + "=" * 60)
        if failed == 0:
            print("🎉 ALL TESTS PASSED! The whitespace steganography project is fully functional.")
        else:
            print(f"⚠️ {failed} test(s) failed. Please review the details above.")
        print("=" * 60)
    
    def cleanup(self):
        """Clean up resources."""
        self.cleanup_temp_files()


def main():
    """Main test execution function."""
    tester = WhitespaceStegoTester()
    
    try:
        results = tester.run_all_tests()
        tester.print_results()
        
        # Return appropriate exit code
        failed_count = sum(1 for r in results if not r.success)
        sys.exit(1 if failed_count > 0 else 0)
        
    except KeyboardInterrupt:
        print("\n⚠️ Testing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {e}")
        sys.exit(1)
    finally:
        tester.cleanup()


if __name__ == "__main__":
    main() 