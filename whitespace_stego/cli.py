"""Command-line interface for whitespace steganography."""

import sys
from pathlib import Path
from typing import Optional

import click
import base64
import logging

from whitespace_stego.logger import setup_logger
from .encode import encode_message
from .decode import decode_message

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
            from whitespace_stego_backend import (
                encode as rust_encode,
                decode as rust_decode,
            )

            return rust_encode, rust_decode
        except ImportError:
            logger.error("Rust backend not available. Please ensure it is installed.")
            sys.exit(1)
    elif backend == "c":
        try:
            from whitespace_stego.c_backend import (
                encode as c_encode,
                decode as c_decode,
            )

            return c_encode, c_decode
        except ImportError:
            logger.error("C backend not available. Please ensure it is installed.")
            sys.exit(1)
    else:
        raise ValueError(f"Unknown backend: {backend}")


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option(
    "--backend",
    "-b",
    type=click.Choice(["python", "c", "rust"]),
    default="python",
    help="Backend implementation to use",
)
def cli(verbose: bool, backend: str) -> None:
    """Whitespace steganography tool for encoding and decoding messages."""
    global logger
    if verbose:
        logger = setup_logger(__name__, level=logging.DEBUG, verbose=True)
    logger.debug("Using backend: %s", backend)
    # Store backend in context
    ctx = click.get_current_context()
    ctx.ensure_object(dict)
    ctx.obj["backend"] = backend


@cli.command()
@click.option(
    "--message-file",
    "-m",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to the file containing the message to encode",
)
@click.option(
    "--carrier-file",
    "-c",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to the carrier file",
)
@click.option(
    "--output",
    "-o",
    required=True,
    type=click.Path(path_type=Path),
    help="Path where the encoded file will be saved",
)
@click.option("--password", "-p", help="Optional password for encryption")
def encode(message_file: Path, carrier_file: Path, output: Path, password: str | None):
    """Encode a message into a carrier file using whitespace steganography."""
    try:
        # Read the message and carrier files
        message = message_file.read_text(encoding="utf-8")
        carrier = carrier_file.read_text(encoding="utf-8")

        logger.debug("Encoding message from file: %s", message_file)
        logger.debug("Using carrier from file: %s", carrier_file)
        logger.debug("Using password: %s", password if password else "None")

        # Encode the message
        encoded = encode_message(message, carrier, password)

        logger.debug("Message successfully encoded")

        # Write the encoded result
        output.write_text(encoded, encoding="utf-8")
        click.echo(f"Message successfully encoded into {output}")
    except Exception as e:
        click.echo(f"Error encoding message: {str(e)}", err=True)
        raise click.Abort()


@cli.command()
@click.option(
    "--carrier-file",
    "-c",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to the encoded carrier file",
)
@click.option(
    "--output",
    "-o",
    required=True,
    type=click.Path(path_type=Path),
    help="Path where the decoded message will be saved",
)
@click.option("--password", "-p", help="Optional password for decryption")
def decode(carrier_file: Path, output: Path, password: str | None):
    """Decode a message from a carrier file using whitespace steganography."""
    try:
        # Read the carrier file
        carrier = carrier_file.read_text(encoding="utf-8")

        logger.debug("Decoding carrier from file: %s", carrier_file)
        logger.debug("Using password: %s", password if password else "None")

        # Decode the message
        decoded = decode_message(carrier, password)

        logger.debug("Message successfully decoded")

        # Write the decoded result
        output.write_text(decoded, encoding="utf-8")
        click.echo(f"Message successfully decoded to {output}")
    except Exception as e:
        click.echo(f"Error decoding message: {str(e)}", err=True)
        raise click.Abort()


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
