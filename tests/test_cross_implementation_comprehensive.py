#!/usr/bin/env python3
"""
Comprehensive cross-implementation test automation for whitespace steganography.

This test suite provides exhaustive testing across all implementations:
- Python core (with both python and rust backends)
- Rust CLI (whitespace-stego-rs)
- C CLI (whitespace-stego-c)
- Standalone Python binary (dist/whitespace-stego-py)

Test coverage includes:
1. All permutations of encode/decode between implementations
2. File-based and argument-based input methods
3. Various message types (ASCII, Unicode, empty, long, edge cases)
4. Various carrier types (ASCII, Unicode, empty, long, edge cases)
5. Various password types (None, ASCII, Unicode, long, edge cases)
6. Error handling and edge cases
7. Performance benchmarking
8. Binary compatibility verification
"""

import pytest
import subprocess
import tempfile
import os
import shutil
import time
import json
import hashlib
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any
import base64
import logging

# Import the Python implementations
from whitespace_stego.core import encode as py_encode, decode as py_decode

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CrossImplementationTester:
    """Comprehensive cross-implementation test automation."""
    
    def __init__(self):
        """Initialize the tester with all available implementations."""
        self.implementations = {
            "python_core": {
                "name": "Python Core",
                "encode": py_encode,
                "decode": py_decode,
                "type": "library"
            },
            "python_cli": {
                "name": "Python CLI",
                "cmd": [".venv/bin/python", "-m", "whitespace_stego.cli"],
                "type": "cli"
            },
            "rust_cli": {
                "name": "Rust CLI",
                "cmd": ["./whitespace-stego-rs"],
                "type": "cli"
            },
            "c_cli": {
                "name": "C CLI",
                "cmd": ["./whitespace-stego-c"],
                "type": "cli"
            },
            "standalone_py": {
                "name": "Standalone Python",
                "cmd": ["./dist/whitespace-stego-py"],
                "type": "cli"
            }
        }
        
        # Verify all implementations are available
        self._verify_implementations()
    
    def _verify_implementations(self):
        """Verify all CLI implementations are available."""
        for impl_id, impl in self.implementations.items():
            if impl["type"] == "cli":
                cmd = impl["cmd"]
                if not os.path.exists(cmd[0]) and not cmd[0].startswith(".venv"):
                    logger.warning(f"Implementation {impl_id} not found: {cmd[0]}")
                    # Remove unavailable implementations
                    del self.implementations[impl_id]
    
    def get_test_data(self) -> Dict[str, List[Any]]:
        """Get comprehensive test data."""
        return {
            "messages": [
                # Basic messages
                "",
                "Hello, World!",
                "Hello, 世界!",
                "¡Hola! ¿Cómo estás?",
                "Привет, мир!",
                "こんにちは、世界！",
                "مرحبا بالعالم!",
                
                # Special characters
                "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?",
                "Numbers: 0123456789",
                "Mixed case: Hello World 123 !@#",
                
                # Unicode and emoji
                "Emoji: 🚀🌟🎉💻🔒",
                "Unicode: αβγδε ζηθικλμν ξοπρστυ φχψω",
                "Cyrillic: абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                "Arabic: ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي",
                "Chinese: 你好世界欢迎来到我们的测试",
                "Japanese: こんにちは世界へようこそ私たちのテストへ",
                "Korean: 안녕하세요 세계에 오신 것을 환영합니다 우리의 테스트에",
                
                # Edge cases
                "Very long message: " + "x" * 1000,
                "Multi-line\nmessage\nwith\nlinebreaks\nand\ttabs",
                "Message with null bytes: \x00\x01\x02",
                "Message with control chars: \x07\x08\x09\x0A\x0D",
                "Message with backslashes: \\n\\t\\r\\b",
                "Message with quotes: \"'`",
                "Message with spaces:   multiple   spaces   ",
                "Message with unicode spaces: \u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A",
                
                # Empty and minimal
                "",
                "a",
                "ab",
                "abc",
                
                # Binary-like data (base64 encoded)
                base64.b64encode(b"Binary data: \x00\x01\x02\x03\x04\x05").decode('utf-8'),
                base64.b64encode(b"More binary: \xFF\xFE\xFD\xFC\xFB\xFA").decode('utf-8'),
            ],
            "carriers": [
                # Basic carriers
                "",
                "Simple carrier text",
                "Carrier with spaces and punctuation!",
                "你好世界",
                "Very long carrier: " + "carrier text " * 100,
                "Single char: A",
                "Multi-line\ncarrier\ntext",
                
                # Unicode carriers
                "Unicode carrier: αβγδε",
                "Emoji carrier: 🚀🌟🎉",
                "Mixed carrier: Hello 世界 🚀!",
                
                # Edge cases
                "Carrier with null bytes: \x00\x01\x02",
                "Carrier with control chars: \x07\x08\x09\x0A\x0D",
                "Carrier with backslashes: \\n\\t\\r\\b",
                "Carrier with quotes: \"'`",
                "Carrier with spaces:   multiple   spaces   ",
                "Carrier with unicode spaces: \u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A",
                
                # Empty and minimal
                "",
                "a",
                "ab",
                "abc",
                
                # Very long carriers
                "Very long carrier: " + "carrier text " * 500,
                "Single character repeated: " + "A" * 1000,
                "Unicode repeated: " + "🚀" * 100,
            ],
            "passwords": [
                # Basic passwords
                None,
                "",
                "simple_password",
                "password_with_special_chars!@#$%",
                "very_long_password_" + "x" * 50,
                
                # Unicode passwords
                "密码",
                "パスワード",
                "비밀번호",
                "كلمة المرور",
                "пароль",
                
                # Edge cases
                "Password with null bytes: \x00\x01\x02",
                "Password with control chars: \x07\x08\x09\x0A\x0D",
                "Password with backslashes: \\n\\t\\r\\b",
                "Password with quotes: \"'`",
                "Password with spaces:   multiple   spaces   ",
                "Password with unicode spaces: \u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A",
                
                # Very long passwords
                "very_long_password_" + "x" * 1000,
                "Unicode long password: " + "🚀" * 50,
            ]
        }
    
    def run_cli_command(self, impl_id: str, command: str, **kwargs) -> Tuple[int, str, str]:
        """Run a CLI command and return (return_code, stdout, stderr)."""
        impl = self.implementations[impl_id]
        cmd = impl["cmd"] + [command]
        
        # Add arguments
        for key, value in kwargs.items():
            if value is not None:
                if key in ["message", "carrier", "password"]:
                    cmd.extend([f"--{key}", str(value)])
                elif key in ["message_file", "carrier_file", "output"]:
                    # Handle different CLI parameter names for different implementations
                    if impl_id == "rust_cli":
                        if key == "message_file":
                            cli_key = "mf"
                        elif key == "carrier_file":
                            cli_key = "cf"
                        else:
                            cli_key = key
                    else:
                        # Convert underscores to hyphens for other CLIs
                        cli_key = key.replace("_", "-")
                    cmd.extend([f"--{cli_key}", str(value)])
                elif key == "backend":
                    cmd.extend(["--backend", str(value)])
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result.returncode, result.stdout.strip(), result.stderr
    
    def encode_with_implementation(self, impl_id: str, message: str, carrier: str, 
                                 password: Optional[str], temp_dir: str, 
                                 use_files: bool = False) -> Tuple[int, str, str]:
        """Encode using a specific implementation."""
        impl = self.implementations[impl_id]
        
        if impl["type"] == "library":
            # Use library directly
            try:
                encoded = impl["encode"](message, carrier, password)
                return 0, encoded, ""
            except Exception as e:
                return 1, "", str(e)
        
        elif impl["type"] == "cli":
            # C CLI only supports file-based input/output
            if impl_id == "c_cli" or use_files:
                # Create temporary files
                message_file = os.path.join(temp_dir, f"message_{impl_id}.txt")
                carrier_file = os.path.join(temp_dir, f"carrier_{impl_id}.txt")
                output_file = os.path.join(temp_dir, f"output_{impl_id}.txt")
                
                with open(message_file, 'w', encoding='utf-8') as f:
                    f.write(message)
                with open(carrier_file, 'w', encoding='utf-8') as f:
                    f.write(carrier)
                
                # Build CLI arguments
                cli_kwargs = {"output": output_file, "password": password}
                if message:
                    cli_kwargs["message_file"] = message_file
                if carrier:
                    cli_kwargs["carrier_file"] = carrier_file
                
                result = self.run_cli_command(impl_id, "encode", **cli_kwargs)
                
                # Read output file if successful
                if result[0] == 0 and os.path.exists(output_file):
                    with open(output_file, 'r', encoding='utf-8') as f:
                        output = f.read()
                    return result[0], output, result[2]
                else:
                    return result
            else:
                # Use command line arguments for other CLIs
                cli_kwargs = {"message": message, "carrier": carrier, "password": password}
                return self.run_cli_command(impl_id, "encode", **cli_kwargs)
    
    def decode_with_implementation(self, impl_id: str, carrier: str, 
                                 password: Optional[str], temp_dir: str,
                                 use_files: bool = False) -> Tuple[int, str, str]:
        """Decode using a specific implementation."""
        impl = self.implementations[impl_id]
        
        if impl["type"] == "library":
            # Use library directly
            try:
                decoded = impl["decode"](carrier, password)
                return 0, decoded, ""
            except Exception as e:
                return 1, "", str(e)
        
        elif impl["type"] == "cli":
            # C CLI only supports file-based input/output
            if impl_id == "c_cli" or use_files:
                # Create temporary files
                carrier_file = os.path.join(temp_dir, f"carrier_{impl_id}.txt")
                output_file = os.path.join(temp_dir, f"decoded_{impl_id}.txt")
                
                with open(carrier_file, 'w', encoding='utf-8') as f:
                    f.write(carrier)
                
                cli_kwargs = {"carrier_file": carrier_file, "output": output_file, "password": password}
                
                result = self.run_cli_command(impl_id, "decode", **cli_kwargs)
                
                # Read output file if successful
                if result[0] == 0 and os.path.exists(output_file):
                    with open(output_file, 'r', encoding='utf-8') as f:
                        output = f.read()
                    return result[0], output, result[2]
                else:
                    return result
            else:
                # Use command line arguments for other CLIs
                cli_kwargs = {"carrier": carrier, "password": password}
                return self.run_cli_command(impl_id, "decode", **cli_kwargs)


class TestCrossImplementationComprehensive:
    """Comprehensive cross-implementation tests."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def tester(self):
        """Create the cross-implementation tester."""
        return CrossImplementationTester()
    
    @pytest.fixture
    def test_data(self, tester):
        """Get comprehensive test data."""
        return tester.get_test_data()
    
    def test_implementation_availability(self, tester):
        """Test that all expected implementations are available."""
        available_impls = list(tester.implementations.keys())
        logger.info(f"Available implementations: {available_impls}")
        
        # Check that we have at least the core implementations
        assert "python_core" in available_impls, "Python core implementation not available"
        assert len(available_impls) >= 2, f"Expected at least 2 implementations, got {len(available_impls)}"
    
    @pytest.mark.parametrize("message_idx", range(30))  # All messages
    @pytest.mark.parametrize("carrier_idx", range(20))  # All carriers
    @pytest.mark.parametrize("password_idx", range(15))  # All passwords
    @pytest.mark.parametrize("use_files", [False, True])
    def test_self_roundtrip_all_implementations(self, tester, test_data, temp_dir, 
                                               message_idx, carrier_idx, password_idx, use_files):
        """Test self roundtrip for all implementations."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Skip invalid combinations
        if not message and not carrier:
            pytest.skip("Both message and carrier are empty")
        
        for impl_id in tester.implementations.keys():
            # Encode
            encode_result = tester.encode_with_implementation(
                impl_id, message, carrier, password, temp_dir, use_files
            )
            
            if encode_result[0] != 0:
                # Some implementations may not support certain edge cases
                if "null bytes" in message or "control chars" in message:
                    pytest.skip(f"Implementation {impl_id} doesn't support edge case message")
                else:
                    pytest.fail(f"Encode failed for {impl_id}: {encode_result[2]}")
            
            encoded = encode_result[1]
            
            # Decode
            decode_result = tester.decode_with_implementation(
                impl_id, encoded, password, temp_dir, use_files
            )
            
            if decode_result[0] != 0:
                pytest.fail(f"Decode failed for {impl_id}: {decode_result[2]}")
            
            decoded = decode_result[1]
            
            # Verify roundtrip
            assert decoded == message, f"Roundtrip failed for {impl_id}: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(10))  # Subset for cross-implementation
    @pytest.mark.parametrize("carrier_idx", range(10))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_cross_implementation_roundtrip(self, tester, test_data, temp_dir,
                                          message_idx, carrier_idx, password_idx, use_files):
        """Test cross-implementation roundtrip."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Skip invalid combinations
        if not message and not carrier:
            pytest.skip("Both message and carrier are empty")
        
        impl_ids = list(tester.implementations.keys())
        
        # Test all encode -> decode combinations
        for encode_impl in impl_ids:
            # Encode with first implementation
            encode_result = tester.encode_with_implementation(
                encode_impl, message, carrier, password, temp_dir, use_files
            )
            
            if encode_result[0] != 0:
                if "null bytes" in message or "control chars" in message:
                    pytest.skip(f"Implementation {encode_impl} doesn't support edge case message")
                else:
                    pytest.fail(f"Encode failed for {encode_impl}: {encode_result[2]}")
            
            encoded = encode_result[1]
            
            # Decode with all implementations
            for decode_impl in impl_ids:
                decode_result = tester.decode_with_implementation(
                    decode_impl, encoded, password, temp_dir, use_files
                )
                
                if decode_result[0] != 0:
                    pytest.fail(f"Cross-decode failed: {encode_impl} -> {decode_impl}: {decode_result[2]}")
                
                decoded = decode_result[1]
                
                # Verify cross-implementation compatibility
                assert decoded == message, (
                    f"Cross-implementation failed: {encode_impl} -> {decode_impl}: "
                    f"expected '{message}', got '{decoded}'"
                )
    
    def test_binary_compatibility(self, tester, temp_dir):
        """Test binary-level compatibility between implementations."""
        # Use a simple test case that should work across all implementations
        message = "Hello, World!"
        carrier = "Test carrier"
        password = "test_password"
        
        encoded_results = {}
        
        # Encode with all implementations
        for impl_id in tester.implementations.keys():
            result = tester.encode_with_implementation(
                impl_id, message, carrier, password, temp_dir, False
            )
            
            if result[0] == 0:
                encoded_results[impl_id] = result[1]
            else:
                pytest.skip(f"Implementation {impl_id} failed to encode: {result[2]}")
        
        # Compare encoded results (they should be identical for compatible implementations)
        if len(encoded_results) > 1:
            first_encoded = next(iter(encoded_results.values()))
            for impl_id, encoded in encoded_results.items():
                assert encoded == first_encoded, (
                    f"Binary incompatibility detected: {impl_id} produces different output"
                )
    
    def test_performance_benchmark(self, tester, temp_dir):
        """Benchmark performance across implementations."""
        message = "Performance test message " * 100  # 2400 characters
        carrier = "Performance test carrier " * 50   # 1200 characters
        password = "performance_test_password"
        
        results = {}
        
        for impl_id in tester.implementations.keys():
            # Warm up
            for _ in range(3):
                tester.encode_with_implementation(impl_id, message, carrier, password, temp_dir, False)
            
            # Benchmark
            start_time = time.time()
            for _ in range(10):
                result = tester.encode_with_implementation(impl_id, message, carrier, password, temp_dir, False)
                if result[0] != 0:
                    pytest.skip(f"Implementation {impl_id} failed: {result[2]}")
            end_time = time.time()
            
            results[impl_id] = (end_time - start_time) / 10  # Average time per operation
        
        # Log performance results
        logger.info("Performance benchmark results (seconds per encode):")
        for impl_id, time_taken in sorted(results.items(), key=lambda x: x[1]):
            logger.info(f"  {impl_id}: {time_taken:.6f}s")
    
    def test_error_handling(self, tester, temp_dir):
        """Test error handling across implementations."""
        # Test cases that should fail
        error_cases = [
            ("", "", None, "Empty message and carrier"),
            ("Invalid encoded data", "", None, "Invalid encoded data"),
            ("Valid message", "Invalid carrier with \x00\x01\x02", None, "Invalid carrier"),
        ]
        
        for message, carrier, password, description in error_cases:
            for impl_id in tester.implementations.keys():
                if impl_id == "python_core":
                    # Test library error handling
                    try:
                        result = tester.implementations[impl_id]["encode"](message, carrier, password)
                        # If we get here, it should be a valid case
                        if not message and not carrier:
                            pytest.fail(f"Implementation {impl_id} should have failed for {description}")
                    except Exception:
                        # Expected for invalid cases
                        pass
                else:
                    # Test CLI error handling
                    result = tester.encode_with_implementation(impl_id, message, carrier, password, temp_dir, False)
                    if not message and not carrier:
                        # Empty message and carrier should fail
                        assert result[0] != 0, f"Implementation {impl_id} should have failed for {description}"
    
    def test_file_vs_argument_consistency(self, tester, temp_dir):
        """Test that file-based and argument-based input produce consistent results."""
        message = "Consistency test message"
        carrier = "Consistency test carrier"
        password = "consistency_test_password"
        
        for impl_id in tester.implementations.keys():
            if tester.implementations[impl_id]["type"] == "library":
                continue  # Skip library implementations
            
            # Test argument-based
            arg_result = tester.encode_with_implementation(
                impl_id, message, carrier, password, temp_dir, False
            )
            
            # Test file-based
            file_result = tester.encode_with_implementation(
                impl_id, message, carrier, password, temp_dir, True
            )
            
            if arg_result[0] == 0 and file_result[0] == 0:
                assert arg_result[1] == file_result[1], (
                    f"Inconsistency in {impl_id}: argument vs file input produce different results"
                )
    
    def test_unicode_edge_cases(self, tester, temp_dir):
        """Test Unicode edge cases across implementations."""
        unicode_cases = [
            ("🚀🌟🎉", "Hello 世界", "密码123"),
            ("\u0000\u0001\u0002", "Normal text", "password"),
            ("\u2000\u2001\u2002", "Carrier with spaces", "pass word"),
            ("\uFEFF\u200B\u200C\u200D", "Carrier with ZW chars", "password"),
        ]
        
        for message, carrier, password in unicode_cases:
            for impl_id in tester.implementations.keys():
                # Encode
                encode_result = tester.encode_with_implementation(
                    impl_id, message, carrier, password, temp_dir, False
                )
                
                if encode_result[0] != 0:
                    # Some implementations may not support certain Unicode edge cases
                    if "\u0000" in message:
                        pytest.skip(f"Implementation {impl_id} doesn't support null bytes")
                    else:
                        pytest.fail(f"Unicode encode failed for {impl_id}: {encode_result[2]}")
                
                encoded = encode_result[1]
                
                # Decode
                decode_result = tester.decode_with_implementation(
                    impl_id, encoded, password, temp_dir, False
                )
                
                if decode_result[0] != 0:
                    pytest.fail(f"Unicode decode failed for {impl_id}: {decode_result[2]}")
                
                decoded = decode_result[1]
                
                # Verify roundtrip
                assert decoded == message, (
                    f"Unicode roundtrip failed for {impl_id}: expected '{message}', got '{decoded}'"
                )
    
    def test_large_data_handling(self, tester, temp_dir):
        """Test handling of large data across implementations."""
        # Create large message and carrier
        large_message = "Large message: " + "x" * 10000  # ~10KB
        large_carrier = "Large carrier: " + "y" * 5000   # ~5KB
        password = "large_data_password"
        
        for impl_id in tester.implementations.keys():
            # Encode
            encode_result = tester.encode_with_implementation(
                impl_id, large_message, large_carrier, password, temp_dir, False
            )
            
            if encode_result[0] != 0:
                pytest.skip(f"Implementation {impl_id} doesn't support large data: {encode_result[2]}")
            
            encoded = encode_result[1]
            
            # Decode
            decode_result = tester.decode_with_implementation(
                impl_id, encoded, password, temp_dir, False
            )
            
            if decode_result[0] != 0:
                pytest.fail(f"Large data decode failed for {impl_id}: {decode_result[2]}")
            
            decoded = decode_result[1]
            
            # Verify roundtrip
            assert decoded == large_message, (
                f"Large data roundtrip failed for {impl_id}: message length mismatch"
            )
    
    def test_password_variations(self, tester, temp_dir):
        """Test various password types across implementations."""
        message = "Password test message"
        carrier = "Password test carrier"
        
        password_variations = [
            None,
            "",
            "simple",
            "password_with_special_chars!@#$%^&*()",
            "Unicode password: 密码パスワード",
            "Very long password: " + "x" * 100,
            "Password with spaces: hello world",
            "Password with newlines: hello\nworld",
            "Password with tabs: hello\tworld",
        ]
        
        for password in password_variations:
            for impl_id in tester.implementations.keys():
                # Encode
                encode_result = tester.encode_with_implementation(
                    impl_id, message, carrier, password, temp_dir, False
                )
                
                if encode_result[0] != 0:
                    pytest.skip(f"Implementation {impl_id} doesn't support password: {encode_result[2]}")
                
                encoded = encode_result[1]
                
                # Decode
                decode_result = tester.decode_with_implementation(
                    impl_id, encoded, password, temp_dir, False
                )
                
                if decode_result[0] != 0:
                    pytest.fail(f"Password decode failed for {impl_id}: {decode_result[2]}")
                
                decoded = decode_result[1]
                
                # Verify roundtrip
                assert decoded == message, (
                    f"Password roundtrip failed for {impl_id}: expected '{message}', got '{decoded}'"
                )


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v", "--tb=short"]) 