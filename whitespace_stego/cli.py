"""Command-line interface for whitespace steganography."""

import sys
from pathlib import Path
from typing import Optional

import click

from whitespace_stego.core import decode, encode

def read_file_or_stdin(file_path: Optional[str]) -> str:
    """Read content from a file or stdin.
    
    Parameters
    ----------
    file_path : Optional[str]
        Path to the file to read, or None for stdin.
        
    Returns
    -------
    str
        The content read from the file or stdin.
    """
    if file_path is None:
        return sys.stdin.read()
    return Path(file_path).read_text()

def write_file_or_stdout(content: str, file_path: Optional[str]) -> None:
    """Write content to a file or stdout.
    
    Parameters
    ----------
    content : str
        The content to write.
    file_path : Optional[str]
        Path to the file to write to, or None for stdout.
    """
    if file_path is None or file_path == "-":
        sys.stdout.write(content)
        sys.stdout.flush()
    else:
        Path(file_path).write_text(content)

@click.group()
def main() -> None:
    """Whitespace steganography tool."""
    pass

@main.command()
@click.option("--message", "-m", help="Message to encode")
@click.option("--message-file", "-mf", help="File containing message to encode")
@click.option("--carrier", "-c", help="Carrier text")
@click.option("--carrier-file", "-cf", help="File containing carrier text")
@click.option("--password", "-p", help="Password for encryption")
@click.option("--password-file", "-pf", help="File containing password")
@click.option("--output", "-o", help="Output file (use - for stdout)")
@click.option("--backend", type=click.Choice(["python", "rust"]), default="python", help="Backend to use")
def encode_cmd(
    message: Optional[str],
    message_file: Optional[str],
    carrier: Optional[str],
    carrier_file: Optional[str],
    password: Optional[str],
    password_file: Optional[str],
    output: Optional[str],
    backend: str,
) -> None:
    """Encode a message into carrier text."""
    # Read message
    if message and message_file:
        raise click.UsageError("Cannot specify both --message and --message-file")
    message_content = message or read_file_or_stdin(message_file)
    
    # Read carrier
    if carrier and carrier_file:
        raise click.UsageError("Cannot specify both --carrier and --carrier-file")
    carrier_content = carrier or read_file_or_stdin(carrier_file) or ""
    
    # Read password
    if password and password_file:
        raise click.UsageError("Cannot specify both --password and --password-file")
    password_content = password or read_file_or_stdin(password_file)
    
    # Encode message
    if backend == "rust":
        # TODO: Implement Rust backend
        raise click.UsageError("Rust backend not yet implemented")
    
    encoded = encode(message_content, carrier_content, password_content)
    write_file_or_stdout(encoded, output)

@main.command()
@click.option("--carrier", "-c", help="Carrier text")
@click.option("--carrier-file", "-cf", help="File containing carrier text")
@click.option("--password", "-p", help="Password for decryption")
@click.option("--password-file", "-pf", help="File containing password")
@click.option("--output", "-o", help="Output file (use - for stdout)")
@click.option("--backend", type=click.Choice(["python", "rust"]), default="python", help="Backend to use")
def decode_cmd(
    carrier: Optional[str],
    carrier_file: Optional[str],
    password: Optional[str],
    password_file: Optional[str],
    output: Optional[str],
    backend: str,
) -> None:
    """Decode a message from carrier text."""
    # Read carrier
    if carrier and carrier_file:
        raise click.UsageError("Cannot specify both --carrier and --carrier-file")
    carrier_content = carrier or read_file_or_stdin(carrier_file)
    
    # Read password
    if password and password_file:
        raise click.UsageError("Cannot specify both --password and --password-file")
    password_content = password or read_file_or_stdin(password_file)
    
    # Decode message
    if backend == "rust":
        # TODO: Implement Rust backend
        raise click.UsageError("Rust backend not yet implemented")
    
    try:
        decoded = decode(carrier_content, password_content)
        write_file_or_stdout(decoded, output)
    except ValueError as e:
        raise click.ClickException(str(e))

if __name__ == "__main__":
    main() 