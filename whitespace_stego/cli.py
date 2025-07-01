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


class MutuallyExclusiveOption(click.Option):
    """Custom option class to handle mutually exclusive options."""

    def __init__(self, *args, **kwargs):
        self.mutually_exclusive = set(kwargs.pop("mutually_exclusive", []))
        help = kwargs.get("help", "")
        if self.mutually_exclusive:
            ex_str = ", ".join(self.mutually_exclusive)
            kwargs["help"] = help + (
                " NOTE: This option is mutually exclusive with "
                " options: [" + ex_str + "]."
            )
        super(MutuallyExclusiveOption, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        if self.mutually_exclusive.intersection(opts) and self.name in opts:
            raise click.UsageError(
                f"Illegal usage: `{self.name}` is mutually exclusive with "
                f"options {self.mutually_exclusive}."
            )

        return super(MutuallyExclusiveOption, self).handle_parse_result(ctx, opts, args)


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option(
    "--backend",
    "-b",
    type=click.Choice(["python", "rust", "c"]),
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
    "--message",
    "-m",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["message_file"],
    help="Message to encode (mutually exclusive with --message-file)",
)
@click.option(
    "--message-file",
    "-mf",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["message"],
    type=click.Path(exists=True, path_type=Path),
    help="Path to the file containing the message to encode (mutually exclusive with --message)",
)
@click.option(
    "--carrier",
    "-c",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["carrier_file"],
    help="Carrier text to encode into (mutually exclusive with --carrier-file)",
)
@click.option(
    "--carrier-file",
    "-cf",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["carrier"],
    type=click.Path(exists=True, path_type=Path),
    help="Path to the carrier file (mutually exclusive with --carrier)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Path where the encoded file will be saved (use '-' for stdout, omit for stdout)",
)
@click.option("--password", "-p", help="Optional password for encryption")
def encode(
    message: Optional[str],
    message_file: Optional[Path],
    carrier: Optional[str],
    carrier_file: Optional[Path],
    output: Optional[Path],
    password: Optional[str],
):
    """Encode a message into a carrier using whitespace steganography."""
    try:
        # Validate that exactly one message option is provided
        if message is None and message_file is None:
            raise click.UsageError(
                "Either --message/-m or --message-file/-mf must be provided."
            )
        if message is not None and message_file is not None:
            raise click.UsageError(
                "--message/-m and --message-file/-mf are mutually exclusive."
            )

        # Validate that exactly one carrier option is provided
        if carrier is None and carrier_file is None:
            raise click.UsageError(
                "Either --carrier/-c or --carrier-file/-cf must be provided."
            )
        if carrier is not None and carrier_file is not None:
            raise click.UsageError(
                "--carrier/-c and --carrier-file/-cf are mutually exclusive."
            )

        # Get the message content
        if message_file is not None:
            message_content = message_file.read_text(encoding="utf-8")
            logger.debug("Reading message from file: %s", message_file)
        else:
            message_content = message
            logger.debug("Using message from command line")

        # Get the carrier content
        if carrier_file is not None:
            carrier_content = carrier_file.read_text(encoding="utf-8")
            logger.debug("Reading carrier from file: %s", carrier_file)
        else:
            carrier_content = carrier
            logger.debug("Using carrier from command line")

        logger.debug("Using password: %s", password if password else "None")

        # Encode the message
        encoded = encode_message(message_content, carrier_content, password)

        logger.debug("Message successfully encoded")

        # Output the encoded result
        if output is None or str(output) == "-":
            # Output to stdout
            click.echo(encoded)
            logger.debug("Message output to stdout")
        else:
            # Output to file
            output.write_text(encoded, encoding="utf-8")
            click.echo(f"Message successfully encoded into {output}")
    except Exception as e:
        click.echo(f"Error encoding message: {str(e)}", err=True)
        raise click.Abort()


@cli.command()
@click.option(
    "--carrier",
    "-c",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["carrier_file"],
    help="Carrier text containing the encoded message (mutually exclusive with --carrier-file)",
)
@click.option(
    "--carrier-file",
    "-cf",
    cls=MutuallyExclusiveOption,
    mutually_exclusive=["carrier"],
    type=click.Path(exists=True, path_type=Path),
    help="Path to the encoded carrier file (mutually exclusive with --carrier)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Path where the decoded message will be saved (use '-' for stdout, omit for stdout)",
)
@click.option("--password", "-p", help="Optional password for decryption")
def decode(
    carrier: Optional[str],
    carrier_file: Optional[Path],
    output: Optional[Path],
    password: Optional[str],
):
    """Decode a message from a carrier using whitespace steganography."""
    try:
        # Validate that exactly one carrier option is provided
        if carrier is None and carrier_file is None:
            raise click.UsageError(
                "Either --carrier/-c or --carrier-file/-cf must be provided."
            )
        if carrier is not None and carrier_file is not None:
            raise click.UsageError(
                "--carrier/-c and --carrier-file/-cf are mutually exclusive."
            )

        # Get the carrier content
        if carrier_file is not None:
            carrier_content = carrier_file.read_text(encoding="utf-8")
            logger.debug("Reading carrier from file: %s", carrier_file)
        else:
            carrier_content = carrier
            logger.debug("Using carrier from command line")

        logger.debug("Using password: %s", password if password else "None")

        # Decode the message
        decoded = decode_message(carrier_content, password)

        logger.debug("Message successfully decoded")

        # Output the decoded result
        if output is None or str(output) == "-":
            # Output to stdout
            click.echo(decoded)
            logger.debug("Message output to stdout")
        else:
            # Output to file
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
