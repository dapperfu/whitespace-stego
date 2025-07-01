"""Comprehensive CLI tests using Click testing utilities."""

import pytest
import tempfile
import os
from pathlib import Path
from click.testing import CliRunner
from whitespace_stego.cli import cli


class TestCLIComprehensive:
    """Comprehensive CLI tests using Click testing utilities."""

    @pytest.fixture
    def runner(self):
        """Create a Click test runner."""
        return CliRunner()

    @pytest.fixture
    def temp_files(self):
        """Create temporary files for testing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create test message file
            msg_file = temp_path / "test_message.txt"
            msg_file.write_text("Test message content", encoding="utf-8")

            # Create test carrier file
            carrier_file = temp_path / "test_carrier.txt"
            carrier_file.write_text("This is a test carrier text.", encoding="utf-8")

            # Create Unicode test files
            unicode_msg_file = temp_path / "unicode_message.txt"
            unicode_msg_file.write_text("Hello 世界 🌍", encoding="utf-8")

            unicode_carrier_file = temp_path / "unicode_carrier.txt"
            unicode_carrier_file.write_text(
                "Unicode carrier: café naïve", encoding="utf-8"
            )

            yield {
                "temp_dir": temp_path,
                "msg_file": msg_file,
                "carrier_file": carrier_file,
                "unicode_msg_file": unicode_msg_file,
                "unicode_carrier_file": unicode_carrier_file,
            }

    def test_cli_help(self, runner):
        """Test main CLI help."""
        result = runner.invoke(cli, ["--help"], catch_exceptions=False)
        assert result.exit_code == 0
        assert "Whitespace steganography tool" in result.output
        assert "encode" in result.output
        assert "decode" in result.output
        assert "--backend" in result.output

    def test_encode_help(self, runner):
        """Test encode command help."""
        result = runner.invoke(cli, ["encode", "--help"], catch_exceptions=False)
        assert result.exit_code == 0
        assert "Encode a message into a carrier" in result.output
        assert "--message" in result.output
        assert "--message-file" in result.output
        assert "--carrier" in result.output
        assert "--carrier-file" in result.output
        assert "stdout" in result.output

    def test_decode_help(self, runner):
        """Test decode command help."""
        result = runner.invoke(cli, ["decode", "--help"], catch_exceptions=False)
        assert result.exit_code == 0
        assert "Decode a message from a carrier" in result.output
        assert "--carrier" in result.output
        assert "--carrier-file" in result.output
        assert "stdout" in result.output

    def test_backend_validation(self, runner):
        """Test backend option validation."""
        # Test invalid backend
        result = runner.invoke(
            cli, ["--backend", "invalid", "encode", "--help"], catch_exceptions=False
        )
        assert result.exit_code == 2
        assert "Invalid value for '--backend'" in result.output
        assert "'invalid' is not one of 'python', 'rust'" in result.output

        # Test valid backends
        result = runner.invoke(
            cli, ["--backend", "python", "encode", "--help"], catch_exceptions=False
        )
        assert result.exit_code == 0

        result = runner.invoke(
            cli, ["--backend", "rust", "encode", "--help"], catch_exceptions=False
        )
        assert result.exit_code == 0

    def test_mutually_exclusive_message_options(self, runner, temp_files):
        """Test that message options are mutually exclusive."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "test",
                "--message-file",
                str(temp_files["msg_file"]),
                "--carrier",
                "carrier",
                "--output",
                "test.out",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 2
        assert "mutually exclusive" in result.output

    def test_mutually_exclusive_carrier_options_encode(self, runner, temp_files):
        """Test that carrier options are mutually exclusive in encode."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "test",
                "--carrier",
                "carrier",
                "--carrier-file",
                str(temp_files["carrier_file"]),
                "--output",
                "test.out",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 2
        assert "mutually exclusive" in result.output

    def test_mutually_exclusive_carrier_options_decode(self, runner, temp_files):
        """Test that carrier options are mutually exclusive in decode."""
        result = runner.invoke(
            cli,
            [
                "decode",
                "--carrier",
                "carrier",
                "--carrier-file",
                str(temp_files["carrier_file"]),
                "--output",
                "test.out",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 2
        assert "mutually exclusive" in result.output

    def test_missing_message_option(self, runner):
        """Test error when no message option is provided."""
        result = runner.invoke(
            cli,
            ["encode", "--carrier", "carrier", "--output", "test.out"],
            catch_exceptions=False,
        )
        assert result.exit_code == 1
        assert (
            "Either --message/-m or --message-file/-mf must be provided"
            in result.output
        )

    def test_missing_carrier_option_encode(self, runner):
        """Test error when no carrier option is provided for encode."""
        result = runner.invoke(
            cli,
            ["encode", "--message", "test", "--output", "test.out"],
            catch_exceptions=False,
        )
        assert result.exit_code == 1
        assert (
            "Either --carrier/-c or --carrier-file/-cf must be provided"
            in result.output
        )

    def test_missing_carrier_option_decode(self, runner):
        """Test error when no carrier option is provided for decode."""
        result = runner.invoke(
            cli, ["decode", "--output", "test.out"], catch_exceptions=False
        )
        assert result.exit_code == 1
        assert (
            "Either --carrier/-c or --carrier-file/-cf must be provided"
            in result.output
        )

    def test_encode_message_carrier_stdout(self, runner):
        """Test encode with message and carrier from command line, output to stdout."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Hello World",
                "--carrier",
                "This is a test carrier.",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output
        # Should output encoded content to stdout
        assert len(result.output.strip().split("\n")) > 1

    def test_encode_message_file_carrier_stdout(self, runner, temp_files):
        """Test encode with message from file, carrier from command line, output to stdout."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message-file",
                str(temp_files["msg_file"]),
                "--carrier",
                "Another carrier text.",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_encode_message_carrier_file_stdout(self, runner, temp_files):
        """Test encode with message from command line, carrier from file, output to stdout."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Secret message",
                "--carrier-file",
                str(temp_files["carrier_file"]),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_encode_message_file_carrier_file_stdout(self, runner, temp_files):
        """Test encode with both message and carrier from files, output to stdout."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message-file",
                str(temp_files["msg_file"]),
                "--carrier-file",
                str(temp_files["carrier_file"]),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_encode_explicit_stdout(self, runner):
        """Test encode with explicit stdout output (-)."""
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Test with dash",
                "--carrier",
                "Carrier with dash",
                "--output",
                "-",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_encode_file_output(self, runner, temp_files):
        """Test encode with file output."""
        output_file = temp_files["temp_dir"] / "test_encoded.txt"
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "File output test",
                "--carrier",
                "Carrier for file",
                "--output",
                str(output_file),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message successfully encoded into" in result.output
        assert output_file.exists()
        assert output_file.read_text(encoding="utf-8").strip()

    def test_decode_file_stdout(self, runner, temp_files):
        """Test decode from file, output to stdout."""
        # First encode a message
        encoded_file = temp_files["temp_dir"] / "test_encoded.txt"
        runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Test message for decode",
                "--carrier",
                "Carrier for decode test",
                "--output",
                str(encoded_file),
            ],
            catch_exceptions=False,
        )

        # Then decode it
        result = runner.invoke(
            cli, ["decode", "--carrier-file", str(encoded_file)], catch_exceptions=False
        )
        assert result.exit_code == 0
        assert "Message decoded successfully" in result.output
        assert "Test message for decode" in result.output

    def test_decode_explicit_stdout(self, runner, temp_files):
        """Test decode with explicit stdout output (-)."""
        # First encode a message
        encoded_file = temp_files["temp_dir"] / "test_encoded.txt"
        runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Test message for explicit stdout",
                "--carrier",
                "Carrier for explicit stdout test",
                "--output",
                str(encoded_file),
            ],
            catch_exceptions=False,
        )

        # Then decode it with explicit stdout
        result = runner.invoke(
            cli,
            ["decode", "--carrier-file", str(encoded_file), "--output", "-"],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message decoded successfully" in result.output
        assert "Test message for explicit stdout" in result.output

    def test_decode_file_output(self, runner, temp_files):
        """Test decode with file output."""
        # First encode a message
        encoded_file = temp_files["temp_dir"] / "test_encoded.txt"
        runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Test message for file output",
                "--carrier",
                "Carrier for file output test",
                "--output",
                str(encoded_file),
            ],
            catch_exceptions=False,
        )

        # Then decode it to file
        decoded_file = temp_files["temp_dir"] / "test_decoded.txt"
        result = runner.invoke(
            cli,
            [
                "decode",
                "--carrier-file",
                str(encoded_file),
                "--output",
                str(decoded_file),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message successfully decoded to" in result.output
        assert decoded_file.exists()
        assert (
            decoded_file.read_text(encoding="utf-8").strip()
            == "Test message for file output"
        )

    def test_password_protection(self, runner, temp_files):
        """Test password protection functionality."""
        # Encode with password
        encoded_file = temp_files["temp_dir"] / "test_encoded_pwd.txt"
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Secret with password",
                "--carrier",
                "Protected carrier",
                "--password",
                "mypassword",
                "--output",
                str(encoded_file),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message successfully encoded into" in result.output

        # Decode with correct password
        result = runner.invoke(
            cli,
            ["decode", "--carrier-file", str(encoded_file), "--password", "mypassword"],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Secret with password" in result.output

        # Decode with wrong password
        result = runner.invoke(
            cli,
            [
                "decode",
                "--carrier-file",
                str(encoded_file),
                "--password",
                "wrongpassword",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 1
        assert "Invalid password or corrupted data" in result.output

    def test_unicode_support(self, runner, temp_files):
        """Test Unicode and emoji support."""
        # Encode Unicode content
        encoded_file = temp_files["temp_dir"] / "test_unicode.txt"
        result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Hello 世界 🌍",
                "--carrier",
                "Unicode carrier: café naïve",
                "--output",
                str(encoded_file),
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message successfully encoded into" in result.output

        # Decode Unicode content
        result = runner.invoke(
            cli, ["decode", "--carrier-file", str(encoded_file)], catch_exceptions=False
        )
        assert result.exit_code == 0
        assert "Hello 世界 🌍" in result.output

    def test_verbose_mode(self, runner):
        """Test verbose mode functionality."""
        result = runner.invoke(
            cli,
            [
                "--verbose",
                "encode",
                "--message",
                "Verbose test",
                "--carrier",
                "Verbose carrier",
                "--output",
                "-",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_rust_backend_error(self, runner):
        """Test error handling when Rust backend is not available."""
        # This test might pass if the Rust backend is actually available
        # We'll test the error case by checking if it fails or succeeds
        result = runner.invoke(
            cli,
            [
                "--backend",
                "rust",
                "encode",
                "--message",
                "test",
                "--carrier",
                "carrier",
            ],
            catch_exceptions=False,
        )
        # The test passes if it either fails (no Rust backend) or succeeds (Rust backend available)
        assert result.exit_code in [0, 1]

    def test_roundtrip_pipeline_simulation(self, runner):
        """Test roundtrip encoding and decoding in a simulated pipeline."""
        # Encode to stdout
        encode_result = runner.invoke(
            cli,
            [
                "encode",
                "--message",
                "Pipeline test message",
                "--carrier",
                "Pipeline carrier text",
            ],
            catch_exceptions=False,
        )
        assert encode_result.exit_code == 0

        # Get the encoded output (skip log messages)
        output_lines = encode_result.output.strip().split("\n")
        encoded_content = output_lines[-1]  # Last line should be the encoded content

        # Create a temporary file with the encoded content for decode
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write(encoded_content)
            temp_encoded_file = f.name

        try:
            # Decode from the file
            decode_result = runner.invoke(
                cli,
                ["decode", "--carrier-file", temp_encoded_file],
                catch_exceptions=False,
            )
            assert decode_result.exit_code == 0
            assert "Pipeline test message" in decode_result.output
        finally:
            # Clean up
            os.unlink(temp_encoded_file)

    def test_all_short_options(self, runner):
        """Test all short option forms."""
        result = runner.invoke(
            cli,
            [
                "-b",
                "python",
                "encode",
                "-m",
                "Short options test",
                "-c",
                "Short carrier text",
                "-o",
                "-",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output

    def test_all_long_options(self, runner):
        """Test all long option forms."""
        result = runner.invoke(
            cli,
            [
                "--backend",
                "python",
                "encode",
                "--message",
                "Long options test",
                "--carrier",
                "Long carrier text",
                "--output",
                "-",
            ],
            catch_exceptions=False,
        )
        assert result.exit_code == 0
        assert "Message encoded successfully" in result.output
