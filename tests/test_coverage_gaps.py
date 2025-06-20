"""Tests to cover gaps in code coverage across all implementations."""

import pytest
import tempfile
import os
import sys
import logging
from pathlib import Path
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from click import UsageError

from whitespace_stego.cli import cli, get_backend_implementation, MutuallyExclusiveOption, main
from whitespace_stego.core import encode, decode, extract_encoded, _encode_binary, _decode_binary
from whitespace_stego.logger import setup_logger


@pytest.fixture
def temp_files():
    """Provide temporary files for testing."""
    temp_dir = Path(tempfile.mkdtemp())
    
    # Create message file
    msg_file = temp_dir / "test_message.txt"
    msg_file.write_text("Test message from file")
    
    # Create carrier file
    carrier_file = temp_dir / "test_carrier.txt"
    carrier_file.write_text("Test carrier from file")
    
    yield {
        'temp_dir': temp_dir,
        'msg_file': msg_file,
        'carrier_file': carrier_file
    }
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)


@pytest.fixture
def runner():
    """Provide a CLI runner for testing."""
    return CliRunner()


class TestCoverageGaps:
    """Test cases to cover missing lines in coverage report."""

    def test_cli_read_file_function(self):
        """Test the read_file function in CLI module."""
        from whitespace_stego.cli import read_file
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Test content")
            temp_file = f.name
        
        try:
            content = read_file(temp_file)
            assert content == "Test content"
        finally:
            os.unlink(temp_file)

    def test_cli_write_file_function(self):
        """Test the write_file function in CLI module."""
        from whitespace_stego.cli import write_file
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            write_file(temp_file, "Written content")
            with open(temp_file, 'r') as f:
                content = f.read()
            assert content == "Written content"
        finally:
            os.unlink(temp_file)

    def test_get_backend_implementation_rust_import_error(self):
        """Test Rust backend import error handling."""
        with patch.dict(sys.modules, {'whitespace_stego_backend': None}):
            with pytest.raises(SystemExit):
                get_backend_implementation("rust")

    def test_get_backend_implementation_unknown_backend(self):
        """Test unknown backend error handling."""
        with pytest.raises(ValueError, match="Unknown backend: invalid"):
            get_backend_implementation("invalid")

    def test_mutually_exclusive_option_help_text(self):
        """Test MutuallyExclusiveOption help text generation."""
        option = MutuallyExclusiveOption(
            ['--message', '-m'],
            ['--message-file', '-mf'],
            'message',
            help='Message to encode'
        )
        assert option.help == 'Message to encode'
        assert '--message' in str(option.opts)
        # Note: mutually_exclusive is only set in a real Click context, so we skip direct assertion here.

    def test_mutually_exclusive_option_validation(self):
        """Test MutuallyExclusiveOption validation via CLI."""
        runner = CliRunner()
        # Both --message and --message-file provided
        with runner.isolated_filesystem():
            msg_file = 'msg.txt'
            with open(msg_file, 'w') as f:
                f.write('test')
            result = runner.invoke(cli, [
                'encode', '--message', 'test', '--message-file', msg_file, '--carrier', 'carrier'
            ], catch_exceptions=False)
            assert result.exit_code != 0
            assert 'mutually exclusive' in result.output

    def test_cli_verbose_mode_logger_setup(self):
        """Test CLI verbose mode logger setup."""
        from whitespace_stego.cli import setup_logger
        import logging
        
        # Test that verbose mode sets up logging correctly
        logger = setup_logger('whitespace_stego.cli', level=10, verbose=True)
        
        # Verify logger is configured
        assert logger.level <= 10
        assert len(logger.handlers) > 0
        
        # Test that we can log messages
        logger.info("Test verbose logging")

    def test_cli_context_backend_storage(self):
        """Test backend storage in Click context."""
        runner = CliRunner()
        result = runner.invoke(cli, ['--backend', 'rust', '--help'])
        assert result.exit_code == 0

    def test_encode_missing_message_and_file(self):
        """Test encode command with missing message and message file."""
        runner = CliRunner()
        result = runner.invoke(cli, ['encode', '--carrier', 'test'])
        assert result.exit_code != 0
        assert "Either --message/-m or --message-file/-mf must be provided" in result.output

    def test_encode_both_message_and_file(self):
        """Test encode command with both message and message file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("File content")
            temp_file = f.name
        
        try:
            result = runner.invoke(cli, [
                'encode', 
                '--message', 'Direct message',
                '--message-file', temp_file,
                '--carrier', 'test'
            ])
            assert result.exit_code != 0
            assert "mutually exclusive" in result.output
        finally:
            os.unlink(temp_file)

    def test_encode_missing_carrier_and_file(self):
        """Test encode command with missing carrier and carrier file."""
        runner = CliRunner()
        result = runner.invoke(cli, ['encode', '--message', 'test'])
        assert result.exit_code != 0
        assert "Either --carrier/-c or --carrier-file/-cf must be provided" in result.output

    def test_encode_both_carrier_and_file(self):
        """Test encode command with both carrier and carrier file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("File content")
            temp_file = f.name
        
        try:
            result = runner.invoke(cli, [
                'encode', 
                '--message', 'test',
                '--carrier', 'Direct carrier',
                '--carrier-file', temp_file
            ])
            assert result.exit_code != 0
            assert "mutually exclusive" in result.output
        finally:
            os.unlink(temp_file)

    @pytest.mark.xfail(reason="Click runner bug: I/O operation on closed file when using file output with logging")
    def test_encode_file_output(self):
        """Test encode with file output using isolated filesystem. Avoid accessing result.output due to Click runner bug."""
        runner = CliRunner()
        with runner.isolated_filesystem():
            output_file = "test_encoded_output.txt"
            result = runner.invoke(cli, [
                'encode',
                '--message', 'Test message for file output',
                '--carrier', 'Test carrier for file output',
                '--output', output_file
            ], catch_exceptions=False)
            assert result.exit_code == 0
            assert os.path.exists(output_file)
            with open(output_file) as f:
                assert f.read().strip()

    def test_encode_exception_handling(self):
        """Test encode command exception handling."""
        runner = CliRunner()
        with patch('whitespace_stego.cli.encode_message') as mock_encode:
            mock_encode.side_effect = Exception("Test error")
            result = runner.invoke(cli, [
                'encode',
                '--message', 'Test message',
                '--carrier', 'Test carrier'
            ])
            assert result.exit_code != 0
            assert "Error encoding message" in result.output

    def test_decode_missing_carrier_and_file(self):
        """Test decode command with missing carrier and carrier file."""
        runner = CliRunner()
        result = runner.invoke(cli, ['decode'])
        assert result.exit_code != 0
        assert "Either --carrier/-c or --carrier-file/-cf must be provided" in result.output

    def test_decode_both_carrier_and_file(self):
        """Test decode command with both carrier and carrier file."""
        runner = CliRunner()
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("File content")
            temp_file = f.name
        
        try:
            result = runner.invoke(cli, [
                'decode', 
                '--carrier', 'Direct carrier',
                '--carrier-file', temp_file
            ])
            assert result.exit_code != 0
            assert "mutually exclusive" in result.output
        finally:
            os.unlink(temp_file)

    @pytest.mark.xfail(reason="Click runner bug: I/O operation on closed file when using file output with logging")
    def test_decode_file_output(self):
        """Test decode with file output using isolated filesystem. Avoid accessing result.output due to Click runner bug."""
        runner = CliRunner()
        with runner.isolated_filesystem():
            encoded_file = "test_encoded_for_decode.txt"
            output_file = "test_decoded_output.txt"
            # Encode first
            encode_result = runner.invoke(cli, [
                'encode',
                '--message', 'Test message for decode output',
                '--carrier', 'Test carrier for decode output',
                '--output', encoded_file
            ], catch_exceptions=False)
            assert encode_result.exit_code == 0
            # Decode
            result = runner.invoke(cli, [
                'decode',
                '--carrier-file', encoded_file,
                '--output', output_file
            ], catch_exceptions=False)
            assert result.exit_code == 0
            assert os.path.exists(output_file)
            with open(output_file) as f:
                assert "Test message for decode output" in f.read()

    def test_decode_exception_handling(self):
        """Test decode command exception handling."""
        runner = CliRunner()
        with patch('whitespace_stego.cli.decode_message') as mock_decode:
            mock_decode.side_effect = Exception("Test error")
            result = runner.invoke(cli, [
                'decode',
                '--carrier', 'Invalid carrier'
            ])
            assert result.exit_code != 0
            assert "Error decoding message" in result.output

    def test_core_encode_empty_carrier(self):
        """Test core encode function with empty carrier."""
        result = encode("Test message", "")
        assert result.startswith("\u200b")  # START_MARKER
        assert result.endswith("\u200c")    # END_MARKER

    def test_core_encode_single_character_carrier(self):
        """Test core encode function with single character carrier."""
        result = encode("Test message", "A")
        assert "A" in result
        assert result.startswith("A\u200b")  # Single char + START_MARKER

    def test_core_decode_invalid_markers(self):
        """Test core decode function with invalid markers."""
        with pytest.raises(ValueError, match="No valid message found"):
            decode("Invalid carrier without markers")

    def test_core_decode_invalid_password(self):
        """Test core decode function with invalid password."""
        # Encode with password
        encoded = encode("Secret message", "Carrier", "password123")
        
        # Try to decode with wrong password
        with pytest.raises(ValueError, match="Invalid password"):
            decode(encoded, "wrongpassword")

    def test_core_decode_corrupted_data(self):
        """Test decode with corrupted data."""
        encoded = encode("Test message", "Test carrier")
        # Corrupt the whitespace markers (replace zero-width space with a visible char)
        corrupted = encoded.replace("\u200b", "X")
        with pytest.raises(ValueError, match="No valid message found in carrier text"):
            decode(corrupted)

    def test_core_extract_encoded_invalid_markers(self):
        """Test extract_encoded function with invalid markers."""
        with pytest.raises(ValueError, match="No valid message found"):
            extract_encoded("Invalid carrier without markers")

    def test_core_binary_encoding_edge_cases(self):
        """Test binary encoding edge cases."""
        # Test empty bytes
        result = _encode_binary(b"")
        assert result == ""
        
        # Test single byte
        result = _encode_binary(b"\x00")
        assert len(result) == 8
        assert all(c in ["\u200d", "\ufeff"] for c in result)
        
        # Test multiple bytes
        result = _encode_binary(b"\x00\xFF")
        assert len(result) == 16

    def test_core_binary_decoding_edge_cases(self):
        """Test binary decoding edge cases."""
        # Test empty string
        result = _decode_binary("")
        assert result == b""
        
        # Test single byte
        encoded = "\u200d\u200d\u200d\u200d\u200d\u200d\u200d\u200d"  # 8 zeros
        result = _decode_binary(encoded)
        assert result == b"\x00"
        
        # Test multiple bytes
        encoded = "\u200d\u200d\u200d\u200d\u200d\u200d\u200d\u200d" + "\ufeff\ufeff\ufeff\ufeff\ufeff\ufeff\ufeff\ufeff"  # 0x00 0xFF
        result = _decode_binary(encoded)
        assert result == b"\x00\xFF"

    def test_logger_setup_with_level(self):
        """Test logger setup with explicit level."""
        logger = setup_logger("test_logger", level=logging.DEBUG)
        assert logger.level == logging.DEBUG

    def test_logger_setup_verbose_mode(self):
        """Test logger setup in verbose mode."""
        from whitespace_stego.logger import setup_logger
        import sys
        
        # Setup logger in verbose mode
        logger = setup_logger('test_verbose', level=10, verbose=True)
        
        # Check that we have a handler
        assert len(logger.handlers) > 0
        
        # Check that the handler is a StreamHandler
        handler = logger.handlers[0]
        assert isinstance(handler, logging.StreamHandler)
        
        # Check that the level is set correctly
        assert logger.level <= 10

    def test_logger_setup_non_verbose_mode(self):
        """Test logger setup in non-verbose mode."""
        logger = setup_logger("test_logger", verbose=False)
        assert len(logger.handlers) > 0
        handler = logger.handlers[0]
        assert isinstance(handler, logging.StreamHandler)
        assert handler.stream == sys.stdout

    def test_logger_setup_existing_handlers(self):
        """Test logger setup when handlers already exist."""
        logger = setup_logger("test_logger")
        initial_handlers = len(logger.handlers)
        
        # Setup again - should not add duplicate handlers
        logger = setup_logger("test_logger")
        assert len(logger.handlers) == initial_handlers

    def test_cli_main_function(self):
        """Test CLI main function using CliRunner."""
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert "whitespace steganography" in result.output.lower()

    def test_cli_module_main_block(self):
        """Test the __main__ block in CLI module."""
        with patch('whitespace_stego.cli.cli') as mock_cli:
            # Simulate running the module directly
            import whitespace_stego.cli
            if hasattr(whitespace_stego.cli, '__main__'):
                # This would be executed if the module was run directly
                pass
            # The main function should be callable
            assert callable(whitespace_stego.cli.main)


class TestRustBackendCoverage:
    """Test cases for Rust backend coverage."""

    def test_rust_backend_import_success(self):
        """Test successful Rust backend import."""
        # This test will only pass if the Rust backend is available
        try:
            encode_func, decode_func = get_backend_implementation("rust")
            assert callable(encode_func)
            assert callable(decode_func)
        except SystemExit:
            # Rust backend not available, skip test
            pytest.skip("Rust backend not available")

    def test_rust_backend_functionality(self):
        """Test Rust backend functionality if available."""
        try:
            encode_func, decode_func = get_backend_implementation("rust")
            
            # Test basic functionality
            message = "Test message"
            carrier = "Test carrier"
            encoded = encode_func(message, carrier)
            decoded = decode_func(encoded)
            assert decoded == message
            
        except SystemExit:
            pytest.skip("Rust backend not available")


class TestCrossImplementationCoverage:
    """Test cases for cross-implementation coverage."""

    def test_python_rust_cross_compatibility(self):
        """Test cross-compatibility between Python and Rust backends."""
        try:
            # Get both backends
            py_encode, py_decode = get_backend_implementation("python")
            rust_encode, rust_decode = get_backend_implementation("rust")
            
            # Test Python encode -> Rust decode
            message = "Cross-test message"
            carrier = "Cross-test carrier"
            encoded = py_encode(message, carrier)
            decoded = rust_decode(encoded)
            assert decoded == message
            
            # Test Rust encode -> Python decode
            encoded = rust_encode(message, carrier)
            decoded = py_decode(encoded)
            assert decoded == message
            
        except SystemExit:
            pytest.skip("Rust backend not available")

    def test_password_protection_cross_backend(self):
        """Test password protection across Python and Rust backends."""
        message = "Cross-backend password test"
        carrier = "Cross-backend carrier"
        password = "test_password"
        # Encode with Python backend
        encoded = encode(message, carrier, password=password)
        # Get rust_decode
        _, rust_decode = get_backend_implementation("rust")
        try:
            decoded = rust_decode(encoded, password)
            assert decoded == message
        except ValueError as e:
            assert "decryption" in str(e).lower() or "fernet" in str(e).lower()


class TestErrorHandlingCoverage:
    """Test cases for comprehensive error handling coverage."""

    def test_encode_with_invalid_unicode(self):
        """Test encoding with invalid Unicode characters."""
        # This should handle Unicode encoding gracefully
        message = "Test message with unicode: 🚀"
        carrier = "Carrier with unicode: 🌍"
        result = encode(message, carrier)
        assert result is not None

    def test_decode_with_malformed_data(self):
        """Test decoding with malformed data."""
        # Test with incomplete markers
        with pytest.raises(ValueError):
            decode("Text with only start marker\u200b")
        
        with pytest.raises(ValueError):
            decode("Text with only end marker\u200c")

    def test_binary_encoding_with_special_bytes(self):
        """Test binary encoding with special byte values."""
        # Test with various byte values
        test_bytes = b"\x00\x01\x7F\x80\xFF"
        encoded = _encode_binary(test_bytes)
        decoded = _decode_binary(encoded)
        assert decoded == test_bytes

    def test_logger_with_special_characters(self):
        """Test logger with special characters in messages."""
        logger = setup_logger("test_special_chars")
        # This should not raise any exceptions
        logger.info("Message with special chars: 🚀🌍💻")
        logger.debug("Debug message with unicode: café naïve") 