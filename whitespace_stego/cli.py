"""Command-line interface for whitespace steganography."""

import sys
from pathlib import Path
from typing import Optional

import click
import base64
import logging

from whitespace_stego.core import decode, encode
from whitespace_stego.logger import setup_logger

logger = setup_logger(__name__)

def read_file(file_path: str) -> str:
    """Read content from a file."""
    return Path(file_path).read_text()

def write_file(file_path: str, content: str) -> None:
    """Write content to a file."""
    Path(file_path).write_text(content)

@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--backend", "-b", type=click.Choice(["python", "c", "rust"]), default="python", help="Backend implementation to use")
def cli(verbose: bool, backend: str) -> None:
    """Whitespace steganography tool."""
    if verbose:
        logger.setLevel(logging.DEBUG)
    logger.debug("Using backend: %s", backend)

@cli.command()
@click.option("--message", "-m", help="Message to encode")
@click.option("--message-file", "-mf", help="File containing message to encode")
@click.option("--carrier", "-c", help="Carrier text")
@click.option("--carrier-file", "-cf", help="File containing carrier text")
@click.option("--password", "-p", help="Password for encryption")
@click.option("--output", "-o", help="Output file (default: stdout)")
def encode_command(message: Optional[str], message_file: Optional[str], 
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
    
    # Get carrier
    if carrier and carrier_file:
        raise click.UsageError("Cannot specify both --carrier and --carrier-file")
    if not carrier and not carrier_file:
        raise click.UsageError("Must specify either --carrier or --carrier-file")
    
    carrier_text = carrier if carrier else read_file(carrier_file)
    logger.debug("Using carrier: %s", carrier_text)
    logger.debug("Using password: %s", password if password else "None")
    
    # Encode message
    try:
        result = encode(message_text, carrier_text, password)
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
def decode_command(carrier: Optional[str], carrier_file: Optional[str],
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
    
    # Decode message
    try:
        result = decode(carrier_text, password)
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
