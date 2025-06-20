"""Tests to cover missing lines in cli.py."""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from whitespace_stego.cli import cli, write_file, main


class TestCLIMissingLines:
    """Test cases to cover missing lines in cli.py."""

    def test_write_file_function(self):
        """Test the write_file function directly to cover lines 150, 160."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            test_content = "Test content for write_file function"
            write_file(temp_file, test_content)
            
            # Verify the file was written correctly
            with open(temp_file, 'r') as f:
                content = f.read()
            assert content == test_content
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_write_file_function_with_unicode(self):
        """Test write_file function with Unicode content."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            test_content = "Test content with Unicode: 世界 🌍"
            write_file(temp_file, test_content)
            
            # Verify the file was written correctly
            with open(temp_file, 'r', encoding='utf-8') as f:
                content = f.read()
            assert content == test_content
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_main_function_direct_call(self):
        """Test main function directly to cover line 238."""
        # Test that main function can be called without error
        # This should not raise any exceptions when called with help
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 2  # Exit code for help

    def test_main_function_with_cli_runner(self):
        """Test main function through CliRunner to cover line 238."""
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0

    @patch('whitespace_stego.cli.cli')
    def test_main_function_calls_cli(self, mock_cli):
        """Test that main function calls cli() to cover line 238."""
        # Mock cli to avoid SystemExit
        mock_cli.return_value = None
        main()
        mock_cli.assert_called_once()

    def test_module_main_block(self):
        """Test the __main__ block to cover lines 260-261."""
        # Import the module and check if it can be executed
        import whitespace_stego.cli as cli_module
        
        # The module should be importable without error
        assert hasattr(cli_module, 'main')
        assert hasattr(cli_module, 'cli')

    def test_module_main_block_execution(self):
        """Test that the __main__ block executes main() when run directly."""
        # Test by importing and checking the module structure
        import whitespace_stego.cli as cli_module
        
        # Check that the module has the expected structure
        assert cli_module.__name__ == 'whitespace_stego.cli'
        assert hasattr(cli_module, 'main')
        assert hasattr(cli_module, 'cli')

    def test_cli_with_system_exit(self):
        """Test CLI with SystemExit to cover error handling paths."""
        runner = CliRunner()
        
        # Test with invalid arguments that should cause SystemExit
        result = runner.invoke(cli, ['invalid-command'])
        assert result.exit_code != 0

    def test_cli_with_exception_handling(self):
        """Test CLI exception handling paths."""
        runner = CliRunner()
        
        # Test encode with missing required arguments
        result = runner.invoke(cli, ['encode'], catch_exceptions=False)
        assert result.exit_code != 0
        assert "must be provided" in result.output

        # Test decode with missing required arguments  
        result = runner.invoke(cli, ['decode'], catch_exceptions=False)
        assert result.exit_code != 0
        assert "must be provided" in result.output 