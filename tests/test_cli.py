"""Tests for the CLI module.

This module contains tests for the command-line interface functionality,
including file operations, command handling, and error cases.
"""

import pytest
from pathlib import Path
from typing import Generator
import sys
from io import StringIO
from whitespace_stego.cli import (
    read_file,
    write_file,
    encode_command,
    decode_command,
    main
)
import logging

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def temp_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Create a temporary directory for test files.
    
    Parameters
    ----------
    tmp_path : Path
        Pytest's temporary directory fixture.
        
    Yields
    ------
    Path
        Path to the temporary directory.
    """
    yield tmp_path

@pytest.fixture
def message_file(temp_dir: Path) -> Path:
    """Create a temporary message file.
    
    Parameters
    ----------
    temp_dir : Path
        Path to the temporary directory.
        
    Returns
    -------
    Path
        Path to the message file.
    """
    file_path = temp_dir / "message.txt"
    file_path.write_text("Hello, 世界! 👋")
    return file_path

@pytest.fixture
def carrier_file(temp_dir: Path) -> Path:
    """Create a temporary carrier file.
    
    Parameters
    ----------
    temp_dir : Path
        Path to the temporary directory.
        
    Returns
    -------
    Path
        Path to the carrier file.
    """
    file_path = temp_dir / "carrier.txt"
    file_path.write_text("The quick brown fox jumps over the lazy dog")
    return file_path

def test_read_file_success(temp_dir: Path) -> None:
    """Test successful file reading."""
    logging.debug(f"Running {__name__}.test_read_file_success")
    file_path = temp_dir / "test.txt"
    content = "Test content"
    file_path.write_text(content)
    assert read_file(file_path) == content

def test_read_file_not_found(temp_dir: Path) -> None:
    """Test file reading with non-existent file."""
    logging.debug(f"Running {__name__}.test_read_file_not_found")
    file_path = temp_dir / "nonexistent.txt"
    with pytest.raises(SystemExit) as exc_info:
        read_file(file_path)
    assert exc_info.value.code == 1

def test_write_file(temp_dir: Path) -> None:
    """Test file writing."""
    logging.debug(f"Running {__name__}.test_write_file")
    file_path = temp_dir / "output.txt"
    content = "Test output"
    write_file(file_path, content)
    assert file_path.read_text() == content

def test_encode_command_with_files(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test encode command with file inputs."""
    logging.debug(f"Running {__name__}.test_encode_command_with_files")
    output_file = temp_dir / "encoded.txt"
    args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": output_file,
        "position": None
    })
    
    encode_command(args)
    assert output_file.exists()
    content = output_file.read_text()
    assert len(content) > 0

def test_encode_command_with_stdin(
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test encode command with stdin input."""
    logging.debug(f"Running {__name__}.test_encode_command_with_stdin")
    output_file = temp_dir / "encoded.txt"
    args = type("Args", (), {
        "message": None,
        "carrier": carrier_file,
        "password": "secret",
        "output": output_file,
        "position": None
    })
    
    # Mock stdin input
    sys.stdin = StringIO("Hello from stdin")
    encode_command(args)
    sys.stdin = sys.__stdin__
    
    assert output_file.exists()
    content = output_file.read_text()
    assert len(content) > 0

def test_encode_command_with_stdout(
    message_file: Path,
    carrier_file: Path
) -> None:
    """Test encode command with stdout output."""
    logging.debug(f"Running {__name__}.test_encode_command_with_stdout")
    args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": None,
        "position": None
    })
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    encode_command(args)
    sys.stdout = sys.__stdout__
    
    assert len(captured_output.getvalue()) > 0

def test_decode_command_with_files(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test decode command with file inputs."""
    logging.debug(f"Running {__name__}.test_decode_command_with_files")
    # First encode a message
    encoded_file = temp_dir / "encoded.txt"
    encode_args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": encoded_file,
        "position": None
    })
    encode_command(encode_args)
    
    # Then decode it
    output_file = temp_dir / "decoded.txt"
    carrier_output_file = temp_dir / "carrier_output.txt"
    decode_args = type("Args", (), {
        "input": encoded_file,
        "password": "secret",
        "output": output_file,
        "carrier_output": carrier_output_file
    })
    
    decode_command(decode_args)
    assert output_file.exists()
    assert carrier_output_file.exists()
    assert output_file.read_text() == message_file.read_text()
    assert carrier_output_file.read_text() == carrier_file.read_text()

def test_decode_command_with_stdout(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test decode command with stdout output."""
    logging.debug(f"Running {__name__}.test_decode_command_with_stdout")
    # First encode a message
    encoded_file = temp_dir / "encoded.txt"
    encode_args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": encoded_file,
        "position": None
    })
    encode_command(encode_args)
    
    # Then decode it
    decode_args = type("Args", (), {
        "input": encoded_file,
        "password": "secret",
        "output": None,
        "carrier_output": None
    })
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    decode_command(decode_args)
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "Decoded message:" in output
    assert message_file.read_text() in output

def test_encode_command_invalid_position(
    message_file: Path,
    carrier_file: Path
) -> None:
    """Test encode command with invalid position."""
    logging.debug(f"Running {__name__}.test_encode_command_invalid_position")
    args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": None,
        "position": 999  # Invalid position
    })
    
    with pytest.raises(SystemExit) as exc_info:
        encode_command(args)
    assert exc_info.value.code == 1

def test_decode_command_invalid_password(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test decode command with invalid password."""
    logging.debug(f"Running {__name__}.test_decode_command_invalid_password")
    # First encode a message
    encoded_file = temp_dir / "encoded.txt"
    encode_args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": encoded_file,
        "position": None
    })
    encode_command(encode_args)
    
    # Then try to decode with wrong password
    decode_args = type("Args", (), {
        "input": encoded_file,
        "password": "wrong",
        "output": None,
        "carrier_output": None
    })
    
    with pytest.raises(SystemExit) as exc_info:
        decode_command(decode_args)
    assert exc_info.value.code == 1

def test_main_encode_command(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test main function with encode command."""
    logging.debug(f"Running {__name__}.test_main_encode_command")
    output_file = temp_dir / "encoded.txt"
    sys.argv = [
        "whitespace-stego",
        "encode",
        "-m", str(message_file),
        "-c", str(carrier_file),
        "-p", "secret",
        "-o", str(output_file)
    ]
    
    main()
    assert output_file.exists()
    assert len(output_file.read_text()) > 0

def test_main_decode_command(
    message_file: Path,
    carrier_file: Path,
    temp_dir: Path
) -> None:
    """Test main function with decode command."""
    logging.debug(f"Running {__name__}.test_main_decode_command")
    # First encode a message
    encoded_file = temp_dir / "encoded.txt"
    encode_args = type("Args", (), {
        "message": message_file,
        "carrier": carrier_file,
        "password": "secret",
        "output": encoded_file,
        "position": None
    })
    encode_command(encode_args)
    
    # Then decode it
    output_file = temp_dir / "decoded.txt"
    sys.argv = [
        "whitespace-stego",
        "decode",
        "-i", str(encoded_file),
        "-p", "secret",
        "-o", str(output_file)
    ]
    
    main()
    assert output_file.exists()
    assert output_file.read_text() == message_file.read_text() 