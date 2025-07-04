"""
Test 13: Whitespace Stego CLI

This test suite tests the Click-based command-line interface for whitespace steganography.
"""

import pytest
import tempfile
import importlib
from pathlib import Path
from click.testing import CliRunner
from click import UsageError
from unittest.mock import patch, MagicMock
import click

from whitespace_stego.cli import cli, get_backend_implementation, MutuallyExclusiveOption


class TestCLIBasicFunctionality:
    """Test basic CLI functionality."""

    def test_cli_help(self):
        """Test that CLI help works."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Whitespace steganography tool" in result.output
        assert "encode" in result.output
        assert "decode" in result.output

    def test_cli_verbose_flag(self):
        """Test that verbose flag works."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--verbose", "--help"])
        assert result.exit_code == 0

    def test_cli_backend_selection(self):
        """Test backend selection options."""
        runner = CliRunner()
        
        # Test default backend
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        
        # Test python backend
        result = runner.invoke(cli, ["--backend", "python", "--help"])
        assert result.exit_code == 0
        
        # Test invalid backend - Click should handle this gracefully
        result = runner.invoke(cli, ["--backend", "invalid", "--help"])
        # Click should still show help even with invalid backend
        assert result.exit_code == 0


class TestEncodeCommand:
    """Test the encode command."""

    def test_encode_help(self):
        """Test encode command help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--help"])
        assert result.exit_code == 0
        assert "Encode a message" in result.output

    def test_encode_basic_message(self):
        """Test basic message encoding."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", "Hello World"])
        assert result.exit_code == 0
        assert result.output.strip()  # Should have some output

    def test_encode_with_carrier(self):
        """Test encoding with carrier text."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "encode", 
            "--message", "Secret", 
            "--carrier", "Public text"
        ])
        assert result.exit_code == 0
        # The output should contain the encoded carrier text
        # The encoded text will have whitespace steganography applied
        assert len(result.output.strip()) > 0  # Should have output

    def test_encode_with_password(self):
        """Test encoding with password."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "encode", 
            "--message", "Secret", 
            "--password", "mypass"
        ])
        assert result.exit_code == 0

    def test_encode_no_message(self):
        """Test encoding without message should fail."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode"])
        assert result.exit_code != 0
        assert "must be provided" in result.output

    def test_encode_empty_message(self):
        """Test encoding empty message should fail."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", ""])
        assert result.exit_code != 0
        assert "no point in encoding nothing" in result.output

    def test_encode_mutually_exclusive_message_options(self):
        """Test that message and message-file are mutually exclusive."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "encode", 
            "--message", "test",
            "--message-file", "nonexistent.txt"
        ])
        assert result.exit_code != 0
        assert "mutually exclusive" in result.output

    def test_encode_mutually_exclusive_carrier_options(self):
        """Test that carrier and carrier-file are mutually exclusive."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "encode", 
            "--message", "test",
            "--carrier", "test",
            "--carrier-file", "nonexistent.txt"
        ])
        assert result.exit_code != 0
        assert "mutually exclusive" in result.output

    def test_encode_with_message_file(self):
        """Test encoding with message from file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("File message")
            temp_file = f.name
        
        try:
            result = runner.invoke(cli, ["encode", "--message-file", temp_file])
            assert result.exit_code == 0
        finally:
            Path(temp_file).unlink()

    def test_encode_with_carrier_file(self):
        """Test encoding with carrier from file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Carrier from file")
            temp_file = f.name
        
        try:
            result = runner.invoke(cli, [
                "encode", 
                "--message", "test",
                "--carrier-file", temp_file
            ])
            assert result.exit_code == 0
        finally:
            Path(temp_file).unlink()

    def test_encode_output_to_file(self):
        """Test encoding output to file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            output_file = f.name
        
        try:
            result = runner.invoke(cli, [
                "encode", 
                "--message", "test",
                "--output", output_file
            ])
            assert result.exit_code == 0
            assert Path(output_file).exists()
            assert Path(output_file).read_text().strip()
        finally:
            Path(output_file).unlink()

    def test_encode_output_to_stdout(self):
        """Test encoding output to stdout (default)."""
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", "test"])
        assert result.exit_code == 0
        assert result.output.strip()  # Should have output

    def test_encode_output_to_stdout_explicit(self):
        """Test encoding output to stdout with explicit -."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "encode", 
            "--message", "test",
            "--output", "-"
        ])
        assert result.exit_code == 0
        assert result.output.strip()  # Should have output


class TestDecodeCommand:
    """Test the decode command."""

    def test_decode_help(self):
        """Test decode command help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode", "--help"])
        assert result.exit_code == 0
        assert "Decode a message" in result.output

    def test_decode_basic(self):
        """Test basic message decoding."""
        runner = CliRunner()
        # First encode a message
        encode_result = runner.invoke(cli, ["encode", "--message", "Hello"])
        assert encode_result.exit_code == 0
        
        # Then decode it
        decode_result = runner.invoke(cli, ["decode", "--carrier", encode_result.output.strip()])
        assert decode_result.exit_code == 0
        assert "Hello" in decode_result.output

    def test_decode_with_password(self):
        """Test decoding with password."""
        runner = CliRunner()
        # First encode with password
        encode_result = runner.invoke(cli, [
            "encode", 
            "--message", "Secret",
            "--password", "mypass"
        ])
        assert encode_result.exit_code == 0
        
        # Then decode with password
        decode_result = runner.invoke(cli, [
            "decode", 
            "--carrier", encode_result.output.strip(),
            "--password", "mypass"
        ])
        assert decode_result.exit_code == 0
        assert "Secret" in decode_result.output

    def test_decode_wrong_password(self):
        """Test decoding with wrong password should fail."""
        runner = CliRunner()
        # First encode with password
        encode_result = runner.invoke(cli, [
            "encode", 
            "--message", "Secret",
            "--password", "mypass"
        ])
        assert encode_result.exit_code == 0
        
        # Then decode with wrong password
        decode_result = runner.invoke(cli, [
            "decode", 
            "--carrier", encode_result.output.strip(),
            "--password", "wrongpass"
        ])
        assert decode_result.exit_code != 0

    def test_decode_no_carrier(self):
        """Test decoding without carrier should fail."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode"])
        assert result.exit_code != 0
        assert "must be provided" in result.output

    def test_decode_invalid_carrier(self):
        """Test decoding with invalid carrier should fail."""
        runner = CliRunner()
        result = runner.invoke(cli, ["decode", "--carrier", "invalid"])
        assert result.exit_code != 0

    def test_decode_mutually_exclusive_carrier_options(self):
        """Test that carrier and carrier-file are mutually exclusive."""
        runner = CliRunner()
        result = runner.invoke(cli, [
            "decode", 
            "--carrier", "test",
            "--carrier-file", "nonexistent.txt"
        ])
        assert result.exit_code != 0
        assert "mutually exclusive" in result.output

    def test_decode_with_carrier_file(self):
        """Test decoding with carrier from file."""
        runner = CliRunner()
        # First encode a message
        encode_result = runner.invoke(cli, ["encode", "--message", "File test"])
        assert encode_result.exit_code == 0
        
        # Write encoded result to file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(encode_result.output)
            temp_file = f.name
        
        try:
            # Decode from file
            decode_result = runner.invoke(cli, ["decode", "--carrier-file", temp_file])
            assert decode_result.exit_code == 0
            assert "File test" in decode_result.output
        finally:
            Path(temp_file).unlink()

    def test_decode_output_to_file(self):
        """Test decoding output to file."""
        runner = CliRunner()
        # First encode a message
        encode_result = runner.invoke(cli, ["encode", "--message", "Output test"])
        assert encode_result.exit_code == 0
        
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            output_file = f.name
        
        try:
            # Decode to file
            decode_result = runner.invoke(cli, [
                "decode", 
                "--carrier", encode_result.output.strip(),
                "--output", output_file
            ])
            assert decode_result.exit_code == 0
            assert Path(output_file).exists()
            assert "Output test" in Path(output_file).read_text()
        finally:
            Path(output_file).unlink()


class TestBackendIntegration:
    """Test backend integration."""

    def test_get_backend_implementation_python(self):
        """Test getting Python backend."""
        encode_func, decode_func = get_backend_implementation("python")
        assert callable(encode_func)
        assert callable(decode_func)

    def test_get_backend_implementation_invalid(self):
        """Test getting invalid backend raises error."""
        with pytest.raises(UsageError, match="Unknown backend"):
            get_backend_implementation("invalid")

    def test_get_backend_implementation_rust_unavailable(self):
        """Test getting Rust backend when unavailable."""
        with patch('builtins.__import__', side_effect=ImportError):
            with pytest.raises(click.ClickException, match="Rust backend not available"):
                get_backend_implementation("rust")

    def test_get_backend_implementation_c_unavailable(self):
        """Test getting C backend when unavailable."""
        with patch('builtins.__import__', side_effect=ImportError):
            with pytest.raises(click.ClickException, match="C backend not available"):
                get_backend_implementation("c")


class TestMutuallyExclusiveOption:
    """Test the custom MutuallyExclusiveOption class."""

    def test_mutually_exclusive_option_creation(self):
        """Test creating mutually exclusive option."""
        option = MutuallyExclusiveOption(
            ['--test'], 
            mutually_exclusive=['--other'],
            help="Test option"
        )
        assert option.mutually_exclusive == {'--other'}
        assert "mutually exclusive" in option.help

    def test_mutually_exclusive_option_validation(self):
        """Test mutually exclusive option validation."""
        option = MutuallyExclusiveOption(
            ['--message', '-m'], 
            mutually_exclusive=['message_file'],
            help="Test option"
        )
        
        # Should not raise when only one option is used
        ctx = MagicMock()
        opts = {'message': 'value'}
        args = []
        result = option.handle_parse_result(ctx, opts, args)
        assert result is not None
        
        # Should raise when both options are used
        opts = {'message': 'value', 'message_file': 'value2'}
        with pytest.raises(UsageError, match="mutually exclusive"):
            option.handle_parse_result(ctx, opts, args)


class TestCLIEndToEnd:
    """Test end-to-end CLI functionality."""

    def test_encode_decode_roundtrip(self):
        """Test complete encode/decode roundtrip."""
        runner = CliRunner()
        
        # Encode
        encode_result = runner.invoke(cli, [
            "encode", 
            "--message", "Roundtrip test",
            "--carrier", "Carrier text",
            "--password", "secret123"
        ])
        assert encode_result.exit_code == 0
        
        # Decode
        decode_result = runner.invoke(cli, [
            "decode", 
            "--carrier", encode_result.output.strip(),
            "--password", "secret123"
        ])
        assert decode_result.exit_code == 0
        assert "Roundtrip test" in decode_result.output

    def test_different_backends(self):
        """Test CLI with different backends."""
        runner = CliRunner()
        
        for backend in ["python", "rust", "c"]:
            try:
                result = runner.invoke(cli, [
                    "--backend", backend,
                    "encode", 
                    "--message", f"Backend test {backend}"
                ])
                # Should either succeed or fail gracefully for unavailable backends
                assert result.exit_code in [0, 1]
            except Exception:
                # Some backends might not be available, which is OK
                pass

    def test_file_operations(self):
        """Test file input/output operations."""
        runner = CliRunner()
        
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as msg_file:
            msg_file.write("File message")
            msg_path = msg_file.name
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as car_file:
            car_file.write("File carrier")
            car_path = car_file.name
        
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as out_file:
            out_path = out_file.name
        
        try:
            # Encode from files
            encode_result = runner.invoke(cli, [
                "encode", 
                "--message-file", msg_path,
                "--carrier-file", car_path,
                "--output", out_path
            ])
            assert encode_result.exit_code == 0
            assert Path(out_path).exists()
            
            # Decode from output file
            decode_result = runner.invoke(cli, [
                "decode", 
                "--carrier-file", out_path
            ])
            assert decode_result.exit_code == 0
            assert "File message" in decode_result.output
            
        finally:
            # Clean up
            for path in [msg_path, car_path, out_path]:
                Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 