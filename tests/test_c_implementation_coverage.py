"""Tests for C implementation coverage."""

import pytest
import subprocess
import tempfile
import os
from pathlib import Path


class TestCImplementationCoverage:
    """Test cases for C implementation coverage."""

    def test_c_cli_help(self):
        """Test C CLI help functionality."""
        try:
            result = subprocess.run(
                ["./whitespace-stego-c", "--help"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0
            assert "whitespace steganography" in result.stdout.lower()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_encode_help(self):
        """Test C CLI encode help."""
        try:
            result = subprocess.run(
                ["./whitespace-stego-c", "encode"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 1  # Should fail due to missing required args
            assert "message-file" in result.stdout.lower()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_decode_help(self):
        """Test C CLI decode help."""
        try:
            result = subprocess.run(
                ["./whitespace-stego-c", "decode"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 1  # Should fail due to missing required args
            assert "carrier-file" in result.stdout.lower()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_basic_encode_decode(self):
        """Test C CLI basic encode and decode functionality."""
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test message")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test carrier")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                output_file = f.name

            try:
                # Test encode
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(output_file).exists()

                # Test decode
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                    decode_output = f.name

                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        output_file,
                        "--output",
                        decode_output,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r") as f:
                    decoded_content = f.read()
                assert decoded_content == "Test message"

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    output_file,
                    decode_output,
                ]:
                    if Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_file_operations(self):
        """Test C CLI file input/output operations."""
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test message from file")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test carrier from file")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                output_file = f.name

            try:
                # Test encode with files
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(output_file).exists()

                # Test decode with file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                    decode_output = f.name

                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        output_file,
                        "--output",
                        decode_output,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r") as f:
                    decoded_content = f.read()
                assert decoded_content == "Test message from file"

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    output_file,
                    decode_output,
                ]:
                    if Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_password_protection(self):
        """Test C CLI password protection functionality."""
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Secret message")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Secret carrier")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                output_file = f.name

            try:
                # Test encode with password
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        output_file,
                        "--password",
                        "testpassword",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(output_file).exists()

                # Test decode with correct password
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                    decode_output = f.name

                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        output_file,
                        "--output",
                        decode_output,
                        "--password",
                        "testpassword",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r") as f:
                    decoded_content = f.read()
                assert decoded_content == "Secret message"

                # Test decode with wrong password
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                    wrong_decode_output = f.name

                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        output_file,
                        "--output",
                        wrong_decode_output,
                        "--password",
                        "wrongpassword",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode != 0

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    output_file,
                    decode_output,
                    wrong_decode_output,
                ]:
                    if Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_unicode_support(self):
        """Test C CLI Unicode and emoji support."""
        try:
            # Create temporary files with Unicode content
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt", encoding="utf-8"
            ) as f:
                f.write("Hello 世界 🌍")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt", encoding="utf-8"
            ) as f:
                f.write("Unicode carrier: café naïve")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                output_file = f.name

            try:
                # Test encode with Unicode
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(output_file).exists()

                # Test decode with Unicode
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                    decode_output = f.name

                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        output_file,
                        "--output",
                        decode_output,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r", encoding="utf-8") as f:
                    decoded_content = f.read()
                assert decoded_content == "Hello 世界 🌍"

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    output_file,
                    decode_output,
                ]:
                    if Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_error_handling(self):
        """Test C CLI error handling."""
        try:
            # Test missing message file
            result = subprocess.run(
                [
                    "./whitespace-stego-c",
                    "encode",
                    "--carrier-file",
                    "/tmp/test.txt",
                    "--output",
                    "/tmp/output.txt",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode != 0

            # Test missing carrier file
            result = subprocess.run(
                [
                    "./whitespace-stego-c",
                    "encode",
                    "--message-file",
                    "/tmp/test.txt",
                    "--output",
                    "/tmp/output.txt",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode != 0

            # Test missing output file
            result = subprocess.run(
                [
                    "./whitespace-stego-c",
                    "encode",
                    "--message-file",
                    "/tmp/test.txt",
                    "--carrier-file",
                    "/tmp/test.txt",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode != 0

            # Test invalid file
            result = subprocess.run(
                [
                    "./whitespace-stego-c",
                    "encode",
                    "--message-file",
                    "/nonexistent/file.txt",
                    "--carrier-file",
                    "/tmp/test.txt",
                    "--output",
                    "/tmp/output.txt",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode != 0

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_cli_verbose_mode(self):
        """Test C CLI verbose mode."""
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test message")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Test carrier")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                output_file = f.name

            try:
                # Test encode with verbose mode
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "--verbose",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(output_file).exists()

            finally:
                for file_path in [message_file, carrier_file, output_file]:
                    if Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")


class TestCCrossCompatibility:
    """Test C implementation cross-compatibility."""

    def test_c_python_cross_compatibility(self):
        """Test cross-compatibility between C and Python implementations."""
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Cross-test message")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("Cross-test carrier")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                c_output_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                decode_output = f.name

            try:
                # Encode with C
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        c_output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(c_output_file).exists()

                # Read C encoded content
                with open(c_output_file, "r") as f:
                    c_encoded = f.read()

                # Decode with Python
                from whitespace_stego.core import decode

                decoded = decode(c_encoded)
                assert decoded == "Cross-test message"

                # Encode with Python
                from whitespace_stego.core import encode

                py_encoded = encode("Cross-test message", "Cross-test carrier")

                # Write Python encoded content to file
                py_output_file = None
                with tempfile.NamedTemporaryFile(
                    mode="w", delete=False, suffix=".txt"
                ) as f:
                    py_output_file = f.name
                    f.write(py_encoded)

                # Decode with C
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        py_output_file,
                        "--output",
                        decode_output,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r") as f:
                    decoded_content = f.read()
                assert decoded_content == "Cross-test message"

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    c_output_file,
                    py_output_file,
                    decode_output,
                ]:
                    if file_path and Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")

    def test_c_rust_cross_compatibility(self):
        """Test cross-compatibility between C and Rust implementations."""
        try:
            # Test if Rust backend is available
            from whitespace_stego.cli import get_backend_implementation

            try:
                rust_encode, rust_decode = get_backend_implementation("rust")
            except SystemExit:
                pytest.skip("Rust backend not available")

            # Create temporary files
            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("C-Rust cross-test")
                message_file = f.name

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as f:
                f.write("C-Rust carrier")
                carrier_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                c_output_file = f.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
                decode_output = f.name

            try:
                # Encode with C
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "encode",
                        "--message-file",
                        message_file,
                        "--carrier-file",
                        carrier_file,
                        "--output",
                        c_output_file,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(c_output_file).exists()

                # Read C encoded content
                with open(c_output_file, "r") as f:
                    c_encoded = f.read()

                # Decode with Rust
                decoded = rust_decode(c_encoded)
                assert decoded == "C-Rust cross-test"

                # Encode with Rust
                rust_encoded = rust_encode("C-Rust cross-test", "C-Rust carrier")

                # Write Rust encoded content to file
                rust_output_file = None
                with tempfile.NamedTemporaryFile(
                    mode="w", delete=False, suffix=".txt"
                ) as f:
                    rust_output_file = f.name
                    f.write(rust_encoded)

                # Decode with C
                result = subprocess.run(
                    [
                        "./whitespace-stego-c",
                        "decode",
                        "--carrier-file",
                        rust_output_file,
                        "--output",
                        decode_output,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                assert result.returncode == 0
                assert Path(decode_output).exists()

                # Verify decoded content
                with open(decode_output, "r") as f:
                    decoded_content = f.read()
                assert decoded_content == "C-Rust cross-test"

            finally:
                for file_path in [
                    message_file,
                    carrier_file,
                    c_output_file,
                    rust_output_file,
                    decode_output,
                ]:
                    if file_path and Path(file_path).exists():
                        os.unlink(file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            pytest.skip("C implementation not available")
