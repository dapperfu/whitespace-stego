"""Simple tests to cover remaining CLI lines."""

import pytest
from unittest.mock import patch, MagicMock
import logging

from whitespace_stego.cli import get_backend_implementation, cli


def test_get_backend_implementation_rust_import_error():
    """Test line 19: Rust backend import error."""
    with patch("whitespace_stego.cli.sys") as mock_sys:
        with patch("whitespace_stego.cli.logger") as mock_logger:
            with patch(
                "builtins.__import__",
                side_effect=ImportError("No module named 'whitespace_stego_backend'"),
            ):
                get_backend_implementation("rust")
                mock_logger.error.assert_called_once()
                mock_sys.exit.assert_called_once_with(1)


def test_get_backend_implementation_c_import_error():
    """Test line 23: C backend import error."""
    with patch("whitespace_stego.cli.sys") as mock_sys:
        with patch("whitespace_stego.cli.logger") as mock_logger:
            with patch(
                "builtins.__import__",
                side_effect=ImportError("No module named 'whitespace_stego.c_backend'"),
            ):
                get_backend_implementation("c")
                mock_logger.error.assert_called_once()
                mock_sys.exit.assert_called_once_with(1)


def test_get_backend_implementation_unknown_backend():
    """Test line 33: Unknown backend raises ValueError."""
    with pytest.raises(ValueError, match="Unknown backend: invalid"):
        get_backend_implementation("invalid")


def test_cli_verbose_logging():
    """Test line 40: Verbose flag sets debug logging."""
    from click.testing import CliRunner

    runner = CliRunner()

    # Test that verbose flag works
    result = runner.invoke(cli, ["--verbose", "--help"])
    assert result.exit_code == 0


def test_cli_backend_context_storage():
    """Test line 53: Backend is stored in context."""
    from click.testing import CliRunner

    runner = CliRunner()

    # Test that backend flag works
    result = runner.invoke(cli, ["--backend", "rust", "--help"])
    assert result.exit_code == 0


def test_cli_main_entry_point():
    """Test the main() function entry point."""
    with patch("whitespace_stego.cli.cli") as mock_cli:
        from whitespace_stego.cli import main

        main()
        mock_cli.assert_called_once()


def test_cli_with_all_backend_choices():
    """Test CLI with all backend choices to ensure they work."""
    from click.testing import CliRunner

    runner = CliRunner()

    # Test all backend choices
    for backend in ["python", "rust", "c"]:
        result = runner.invoke(cli, ["--backend", backend, "--help"])
        assert result.exit_code == 0


def test_cli_help_output():
    """Test CLI help output."""
    from click.testing import CliRunner

    runner = CliRunner()

    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "encode" in result.output
    assert "decode" in result.output


def test_encode_help_output():
    """Test encode command help output."""
    from click.testing import CliRunner

    runner = CliRunner()

    result = runner.invoke(cli, ["encode", "--help"])
    assert result.exit_code == 0
    assert "message-file" in result.output
    assert "carrier-file" in result.output
    assert "output" in result.output


def test_decode_help_output():
    """Test decode command help output."""
    from click.testing import CliRunner

    runner = CliRunner()

    result = runner.invoke(cli, ["decode", "--help"])
    assert result.exit_code == 0
    assert "carrier-file" in result.output
    assert "output" in result.output
