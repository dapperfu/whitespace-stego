"""Command-line interface for whitespace steganography."""

import sys
from pathlib import Path
from typing import Optional

import click
import base64
import logging

from whitespace_stego.logger import setup_logger

logger = setup_logger(__name__)

def read_file(file_path: str) -> str:
    """Read content from a file."""
    return Path(file_path).read_text()

def write_file(file_path: str, content: str) -> None:
    """Write content to a file."""
    Path(file_path).write_text(content)

def get_backend_implementation(backend: str):
    """Get the appropriate backend implementation."""
    if backend == "python":
        from whitespace_stego.core import encode as py_encode, decode as py_decode
        return py_encode, py_decode
    elif backend == "rust":
        try:
            from whitespace_stego_backend import encode as rust_encode, decode as rust_decode
            return rust_encode, rust_decode
        except ImportError:
            logger.error("Rust backend not available. Please ensure it is installed.")
            sys.exit(1)
    elif backend == "c":
        try:
            from whitespace_stego.c_backend import encode as c_encode, decode as c_decode
            return c_encode, c_decode
        except ImportError:
            logger.error("C backend not available. Please ensure it is installed.")
            sys.exit(1)
    else:
        raise ValueError(f"Unknown backend: {backend}")

@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--backend", "-b", type=click.Choice(["python", "c", "rust"]), default="python", help="Backend implementation to use")
def cli(verbose: bool, backend: str) -> None:
    """Whitespace steganography tool."""
    if verbose:
        logger.setLevel(logging.DEBUG)
    logger.debug("Using backend: %s", backend)
    # Store backend in context
    ctx = click.get_current_context()
    ctx.ensure_object(dict)
    ctx.obj['backend'] = backend

@cli.command()
@click.option("--message", "-m", help="Message to encode")
@click.option("--message-file", "-mf", help="File containing message to encode")
@click.option("--carrier", "-c", help="Carrier text (optional)")
@click.option("--carrier-file", "-cf", help="File containing carrier text (optional)")
@click.option("--password", "-p", help="Password for encryption")
@click.option("--output", "-o", help="Output file (default: stdout)")
@click.pass_context
def encode_command(ctx, message: Optional[str], message_file: Optional[str], 
                  carrier: Optional[str], carrier_file: Optional[str],
                  password: Optional[str], output: Optional[str]) -> None:
    """Encode a message into carrier text."""
    # Get message
    if message and message_file:
        raise click.UsageError("Cannot specify both --message and --message-file")
    if not message and not message_file:
        raise click.UsageError("Must specify either --message or --message-file")
    
    message_text = message if message else read_file(message_file)
    logger.debug("Encoding message: %s", message_text)
    
    # Get carrier (optional)
    carrier_text = ""
    if carrier and carrier_file:
        raise click.UsageError("Cannot specify both --carrier and --carrier-file")
    if carrier:
        carrier_text = carrier
    elif carrier_file:
        carrier_text = read_file(carrier_file)
    
    logger.debug("Using carrier: %s", carrier_text if carrier_text else "None")
    logger.debug("Using password: %s", password if password else "None")
    
    # Get backend implementation
    encode_func, _ = get_backend_implementation(ctx.obj['backend'])
    
    # Encode message
    try:
        result = encode_func(message_text, carrier_text, password)
        logger.debug("Base64 encoded string: %s", 
                    base64.b64encode(message_text.encode("utf-8")).decode("utf-8"))
        logger.debug("Final encoded message: %s", result)
        
        if output:
            write_file(output, result)
        else:
            click.echo(result)
    except Exception as e:
        logger.error("Failed to encode message: %s", str(e))
        sys.exit(1)

@cli.command()
@click.option("--carrier", "-c", help="Carrier text")
@click.option("--carrier-file", "-cf", help="File containing carrier text")
@click.option("--password", "-p", help="Password for decryption")
@click.option("--output", "-o", help="Output file (default: stdout)")
@click.pass_context
def decode_command(ctx, carrier: Optional[str], carrier_file: Optional[str],
                  password: Optional[str], output: Optional[str]) -> None:
    """Decode a message from carrier text."""
    # Get carrier
    if carrier and carrier_file:
        raise click.UsageError("Cannot specify both --carrier and --carrier-file")
    if not carrier and not carrier_file:
        raise click.UsageError("Must specify either --carrier or --carrier-file")
    
    carrier_text = carrier if carrier else read_file(carrier_file)
    logger.debug("Decoding carrier: %s", carrier_text)
    logger.debug("Using password: %s", password if password else "None")
    
    # Get backend implementation
    _, decode_func = get_backend_implementation(ctx.obj['backend'])
    
    # Decode message
    try:
        result = decode_func(carrier_text, password)
        logger.debug("Decoded message: %s", result)
        
        if output:
            write_file(output, result)
        else:
            click.echo(result)
    except Exception as e:
        logger.error("Failed to decode message: %s", str(e))
        sys.exit(1)

def main() -> None:
    """Entry point for the CLI."""
    cli()

if __name__ == "__main__":
    main()
