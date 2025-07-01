#!/usr/bin/env python3
"""
Comprehensive cross-implementation tests for whitespace steganography.

This test suite covers:
1. All permutations of encode/decode between Python, Rust, and C implementations
2. Both file-based and argument-based input methods
3. Various message types (ASCII, Unicode, empty, long)
4. Various carrier types (ASCII, Unicode, empty, long)
5. Various password types (None, ASCII, Unicode, long)
"""

import pytest
import subprocess
import tempfile
import os
import shutil
from pathlib import Path
from typing import List, Tuple, Optional
import base64

# Import the Python implementations
from whitespace_stego.core import encode as py_encode, decode as py_decode


class TestComprehensiveCrossImplementation:
    """Comprehensive cross-implementation tests."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def test_data(self):
        """Test data combinations."""
        return {
            "messages": [
                "",  # Empty message
                "Hello, World!",  # Simple ASCII
                "Hello, 世界!",  # Unicode
                "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?",  # Special characters
                "Numbers: 0123456789",  # Numbers
                "Mixed case: Hello World 123 !@#",  # Mixed content
                "Very long message: " + "x" * 1000,  # Long message
                "Multi-line\nmessage\nwith\nlinebreaks",  # Multi-line
            ],
            "carriers": [
                "",  # Empty carrier
                "Simple carrier text",  # Simple ASCII
                "Carrier with spaces and punctuation!",  # With punctuation
                "你好世界",  # Unicode carrier
                "Very long carrier: " + "carrier text " * 100,  # Long carrier
                "Single char: A",  # Single character
                "Multi-line\ncarrier\ntext",  # Multi-line
            ],
            "passwords": [
                None,  # No password
                "simple_password",  # Simple ASCII
                "password_with_special_chars!@#$%",  # Special characters
                "密码",  # Unicode password
                "very_long_password_" + "x" * 50,  # Long password
            ]
        }
    
    def run_cli_command(self, backend: str, command: str, **kwargs) -> Tuple[int, str, str]:
        """Run a CLI command and return (return_code, stdout, stderr)."""
        cmd = [".venv/bin/python", "-m", "whitespace_stego.cli", "--backend", backend, command]
        
        # Add arguments
        for key, value in kwargs.items():
            if value is not None:
                if key in ["message", "carrier", "password"]:
                    cmd.extend([f"--{key}", str(value)])
                elif key in ["message_file", "carrier_file", "output"]:
                    cmd.extend([f"--{key}", str(value)])
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
        return result.returncode, result.stdout.strip(), result.stderr
    
    def run_c_cli_command(self, command: str, **kwargs) -> Tuple[int, str, str]:
        """Run the C CLI command and return (return_code, stdout, stderr)."""
        cmd = ["./c/bin/whitespace-stego-c", command]
        
        # Add arguments
        for key, value in kwargs.items():
            if value is not None:
                if key == "message":
                    cmd.extend(["--message", str(value)])
                elif key == "carrier":
                    cmd.extend(["--carrier", str(value)])
                elif key == "password":
                    cmd.extend(["--password", str(value)])
                elif key == "message_file":
                    cmd.extend(["--message-file", str(value)])
                elif key == "carrier_file":
                    cmd.extend(["--carrier-file", str(value)])
                elif key == "output":
                    cmd.extend(["--output", str(value)])
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd="/projects/whitespace-stego3")
        return result.returncode, result.stdout.strip(), result.stderr
    
    def encode_with_backend(self, backend: str, message: str, carrier: str, password: Optional[str], 
                           temp_dir: str, use_files: bool = False) -> Tuple[int, str, str]:
        """Encode using a specific backend with either files or arguments."""
        if use_files:
            # Create temporary files
            message_file = os.path.join(temp_dir, "message.txt")
            carrier_file = os.path.join(temp_dir, "carrier.txt")
            output_file = os.path.join(temp_dir, "output.txt")
            
            with open(message_file, 'w', encoding='utf-8') as f:
                f.write(message)
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            # Only pass --message-file if message is non-empty
            # Only pass --carrier-file if carrier is non-empty
            cli_kwargs = {"output": output_file, "password": password}
            if message:
                cli_kwargs["message-file"] = message_file
            if carrier:
                cli_kwargs["carrier-file"] = carrier_file
            if not message and not carrier:
                pytest.skip("Both message and carrier are empty; skipping invalid CLI case.")
            if backend == "c":
                return self.run_c_cli_command("encode", 
                                            message_file=message_file if message else None,
                                            carrier_file=carrier_file if carrier else None,
                                            output=output_file,
                                            password=password)
            else:
                return self.run_cli_command(backend, "encode", **cli_kwargs)
        else:
            # Use command line arguments
            if backend == "c":
                return self.run_c_cli_command("encode",
                                            message=message,
                                            carrier=carrier,
                                            password=password)
            else:
                return self.run_cli_command(backend, "encode",
                                          message=message,
                                          carrier=carrier,
                                          password=password)
    
    def decode_with_backend(self, backend: str, carrier: str, password: Optional[str],
                           temp_dir: str, use_files: bool = False) -> Tuple[int, str, str]:
        """Decode using a specific backend with either files or arguments."""
        if use_files:
            # Create temporary files
            carrier_file = os.path.join(temp_dir, "carrier.txt")
            output_file = os.path.join(temp_dir, "decoded.txt")
            
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            if backend == "c":
                return self.run_c_cli_command("decode",
                                            carrier_file=carrier_file,
                                            output=output_file,
                                            password=password)
            else:
                return self.run_cli_command(backend, "decode",
                                          **{"carrier-file": carrier_file,
                                             "output": output_file,
                                             "password": password})
        else:
            # Use command line arguments
            if backend == "c":
                return self.run_c_cli_command("decode",
                                            carrier=carrier,
                                            password=password)
            else:
                return self.run_cli_command(backend, "decode",
                                          carrier=carrier,
                                          password=password)
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_python_self_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test Python encode -> Python decode roundtrip."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Encode with Python
        if use_files:
            # Skip invalid case: both message and carrier are empty
            if not message and not carrier:
                pytest.skip("Both message and carrier are empty; skipping invalid CLI case.")
            message_file = os.path.join(temp_dir, "message.txt")
            carrier_file = os.path.join(temp_dir, "carrier.txt")
            output_file = os.path.join(temp_dir, "output.txt")
            
            with open(message_file, 'w', encoding='utf-8') as f:
                f.write(message)
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(carrier)
            
            returncode, stdout, stderr = self.run_cli_command("python", "encode",
                                                            **{"message-file": message_file,
                                                               "carrier-file": carrier_file,
                                                               "output": output_file,
                                                               "password": password})
        else:
            returncode, stdout, stderr = self.run_cli_command("python", "encode",
                                                            message=message,
                                                            carrier=carrier,
                                                            password=password)
        
        assert returncode == 0, f"Python encode failed: {stderr}"
        encoded = stdout if not use_files else Path(output_file).read_text(encoding='utf-8')
        
        # Decode with Python
        if use_files:
            carrier_file = os.path.join(temp_dir, "encoded_carrier.txt")
            output_file = os.path.join(temp_dir, "decoded.txt")
            
            with open(carrier_file, 'w', encoding='utf-8') as f:
                f.write(encoded)
            
            returncode, stdout, stderr = self.run_cli_command("python", "decode",
                                                            **{"carrier-file": carrier_file,
                                                               "output": output_file,
                                                               "password": password})
        else:
            returncode, stdout, stderr = self.run_cli_command("python", "decode",
                                                            carrier=encoded,
                                                            password=password)
        
        assert returncode == 0, f"Python decode failed: {stderr}"
        decoded = stdout if not use_files else Path(output_file).read_text(encoding='utf-8')
        
        assert decoded == message, f"Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_rust_self_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test Rust encode -> Rust decode roundtrip."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Encode with Rust
        returncode, stdout, stderr = self.encode_with_backend("rust", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"Rust encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        # Decode with Rust
        returncode, stdout, stderr = self.decode_with_backend("rust", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"Rust decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_c_self_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test C encode -> C decode roundtrip."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Encode with C
        returncode, stdout, stderr = self.encode_with_backend("c", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"C encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        # Decode with C
        returncode, stdout, stderr = self.decode_with_backend("c", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"C decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_python_rust_cross_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test Python encode -> Rust decode and Rust encode -> Python decode."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Skip invalid case: both message and carrier are empty for CLI
        if use_files and not message and not carrier:
            pytest.skip("Both message and carrier are empty; skipping invalid CLI case.")
        
        # Test Python encode -> Rust decode
        returncode, stdout, stderr = self.encode_with_backend("python", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"Python encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("rust", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"Rust decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Python->Rust: Message mismatch: expected '{message}', got '{decoded}'"
        
        # Test Rust encode -> Python decode
        returncode, stdout, stderr = self.encode_with_backend("rust", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"Rust encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("python", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"Python decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Rust->Python: Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_python_c_cross_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test Python encode -> C decode and C encode -> Python decode."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Skip invalid case: both message and carrier are empty for CLI
        if use_files and not message and not carrier:
            pytest.skip("Both message and carrier are empty; skipping invalid CLI case.")
        
        # Test Python encode -> C decode
        returncode, stdout, stderr = self.encode_with_backend("python", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"Python encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("c", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"C decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Python->C: Message mismatch: expected '{message}', got '{decoded}'"
        
        # Test C encode -> Python decode
        returncode, stdout, stderr = self.encode_with_backend("c", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"C encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("python", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"Python decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"C->Python: Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    @pytest.mark.parametrize("use_files", [False, True])
    def test_rust_c_cross_roundtrip(self, test_data, temp_dir, message_idx, carrier_idx, password_idx, use_files):
        """Test Rust encode -> C decode and C encode -> Rust decode."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Skip invalid case: both message and carrier are empty for CLI
        if use_files and not message and not carrier:
            pytest.skip("Both message and carrier are empty; skipping invalid CLI case.")
        
        # Test Rust encode -> C decode
        returncode, stdout, stderr = self.encode_with_backend("rust", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"Rust encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("c", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"C decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"Rust->C: Message mismatch: expected '{message}', got '{decoded}'"
        
        # Test C encode -> Rust decode
        returncode, stdout, stderr = self.encode_with_backend("c", message, carrier, password, temp_dir, use_files)
        assert returncode == 0, f"C encode failed: {stderr}"
        encoded = stdout if not use_files else Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        returncode, stdout, stderr = self.decode_with_backend("rust", encoded, password, temp_dir, use_files)
        assert returncode == 0, f"Rust decode failed: {stderr}"
        decoded = stdout if not use_files else Path(os.path.join(temp_dir, "decoded.txt")).read_text(encoding='utf-8')
        
        assert decoded == message, f"C->Rust: Message mismatch: expected '{message}', got '{decoded}'"
    
    @pytest.mark.parametrize("message_idx", range(8))
    @pytest.mark.parametrize("carrier_idx", range(7))
    @pytest.mark.parametrize("password_idx", range(5))
    def test_all_implementations_consistency(self, test_data, temp_dir, message_idx, carrier_idx, password_idx):
        """Test that all implementations produce consistent results."""
        message = test_data["messages"][message_idx]
        carrier = test_data["carriers"][carrier_idx]
        password = test_data["passwords"][password_idx]
        
        # Encode with all implementations
        results = {}
        
        for backend in ["python", "rust", "c"]:
            returncode, stdout, stderr = self.encode_with_backend(backend, message, carrier, password, temp_dir, False)
            assert returncode == 0, f"{backend} encode failed: {stderr}"
            results[backend] = stdout
        
        # All encoded results should be identical (for same input)
        python_result = results["python"]
        assert results["rust"] == python_result, "Rust and Python results differ"
        assert results["c"] == python_result, "C and Python results differ"
    
    def test_file_vs_argument_consistency(self, temp_dir):
        """Test that file-based and argument-based input produce identical results."""
        message = "Test message with Unicode: 你好世界"
        carrier = "Test carrier with Unicode: こんにちは"
        password = "Test password with Unicode: пароль"
        
        # Test with arguments
        returncode, stdout, stderr = self.encode_with_backend("python", message, carrier, password, temp_dir, False)
        assert returncode == 0, f"Python encode with arguments failed: {stderr}"
        arg_result = stdout
        
        # Test with files
        returncode, stdout, stderr = self.encode_with_backend("python", message, carrier, password, temp_dir, True)
        assert returncode == 0, f"Python encode with files failed: {stderr}"
        file_result = Path(os.path.join(temp_dir, "output.txt")).read_text(encoding='utf-8')
        
        # Results should be identical
        assert arg_result == file_result, "File-based and argument-based results differ"
    
    def test_error_handling(self, temp_dir):
        """Test error handling for invalid inputs."""
        # Test with non-existent files
        returncode, stdout, stderr = self.run_cli_command("python", "encode",
                                                        message_file="/nonexistent/file.txt",
                                                        carrier="test",
                                                        password=None)
        assert returncode != 0, "Should fail with non-existent file"
        
        # Test with invalid password
        returncode, stdout, stderr = self.run_cli_command("python", "decode",
                                                        carrier="invalid_carrier",
                                                        password="wrong_password")
        assert returncode != 0, "Should fail with invalid carrier"
        
        # Test with missing required arguments
        returncode, stdout, stderr = self.run_cli_command("python", "encode",
                                                        carrier="test",
                                                        password=None)
        assert returncode != 0, "Should fail with missing message" 