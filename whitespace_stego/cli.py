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
from .core import BadPasswordError

# Set up logger to only write to stderr, not stdout
logger = setup_logger(__name__)


def disable_logging_during_cli():
    """Disable logging during CLI execution to prevent interference with Click's output streams."""
    # Disable all loggers to prevent them from writing to stderr during CLI execution
    logging.getLogger().setLevel(logging.CRITICAL)
    for name in logging.root.manager.loggerDict:
        logging.getLogger(name).setLevel(logging.CRITICAL)


def read_file(file_path: str) -> str:
    """Read content from a file."""
    return Path(file_path).read_text()


def write_file(file_path: str, content: str) -> None:
    """Write content to a file."""
    Path(file_path).write_text(content)


def get_backend_implementation(backend: str, ctx=None):
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
            msg = "Rust backend not available. Please ensure it is installed."
            if ctx is not None:
                click.secho(msg, err=True, fg="red")
                ctx.exit(1)
            else:
                raise click.ClickException(msg)
    elif backend == "c":
        try:
            from whitespace_stego.c_backend import (
                encode as c_encode,
                decode as c_decode,
            )
            return c_encode, c_decode
        except ImportError:
            msg = "C backend not available. Please ensure it is installed."
            if ctx is not None:
                click.secho(msg, err=True, fg="red")
                ctx.exit(1)
            else:
                raise click.ClickException(msg)
    else:
        raise click.UsageError(f"Unknown backend: {backend}")


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
@click.pass_context
def cli(ctx, verbose: bool, backend: str) -> None:
    """Whitespace steganography tool for encoding and decoding messages."""
    global logger
    if verbose:
        logger = setup_logger(__name__, level=logging.DEBUG, verbose=True)
    else:
        # Disable logging during CLI execution to prevent interference with Click's output
        disable_logging_during_cli()
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
@click.pass_context
def encode(ctx, message: Optional[str], message_file: Optional[Path], carrier: Optional[str], carrier_file: Optional[Path], output: Optional[Path], password: Optional[str]):
    """Encode a message into a carrier using whitespace steganography."""
    try:
        if message is None and message_file is None:
            raise click.UsageError(
                "Either --message/-m or --message-file/-mf must be provided."
            )
        if message is not None and message_file is not None:
            raise click.UsageError(
                "--message/-m and --message-file/-mf are mutually exclusive."
            )
        if carrier is not None and carrier_file is not None:
            raise click.UsageError(
                "--carrier/-c and --carrier-file/-cf are mutually exclusive."
            )
        if message_file is not None:
            message_content = message_file.read_text(encoding="utf-8")
        else:
            message_content = message
        if not message_content:
            raise click.UsageError("🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!")
        if carrier_file is not None:
            carrier_content = carrier_file.read_text(encoding="utf-8")
        else:
            carrier_content = carrier or ""
        # Use backend from context
        backend = ctx.obj.get("backend", "python")
        encode_func, _ = get_backend_implementation(backend, ctx)
        encoded = encode_func(message_content, carrier_content, password)
        if output is None or str(output) == "-":
            # Output encoded result to stdout
            click.echo(encoded)
        else:
            # Output to file
            output.write_text(encoded, encoding="utf-8")
            # Success message to stdout
            click.secho(f"Message successfully encoded into {output}", fg="green")
    except click.ClickException as e:
        raise
    except Exception as e:
        # Error message to stderr
        click.secho(f"Error encoding message: {str(e)}", err=True, fg="red")
        ctx.exit(1)


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
@click.pass_context
def decode(ctx, carrier: Optional[str], carrier_file: Optional[Path], output: Optional[Path], password: Optional[str]):
    """Decode a message from a carrier using whitespace steganography."""
    try:
        if carrier is None and carrier_file is None:
            raise click.UsageError(
                "Either --carrier/-c or --carrier-file/-cf must be provided."
            )
        if carrier is not None and carrier_file is not None:
            raise click.UsageError(
                "--carrier/-c and --carrier-file/-cf are mutually exclusive."
            )
        if carrier_file is not None:
            carrier_content = carrier_file.read_text(encoding="utf-8")
        else:
            carrier_content = carrier
        backend = ctx.obj.get("backend", "python")
        _, decode_func = get_backend_implementation(backend, ctx)
        try:
            decoded_messages = decode_func(carrier_content, password)
        except BadPasswordError:
            # Error message to stderr
            click.secho("invalid password", err=True, fg="red")
            ctx.exit(1)
        if isinstance(decoded_messages, str):
            decoded_output = decoded_messages
            message_count_text = "Message"
        else:
            decoded_output = "[\n" + "\n".join(f'  "{msg}"' for msg in decoded_messages) + "\n]"
            message_count_text = f"{len(decoded_messages)} messages"
        if output is None or str(output) == "-":
            # Output decoded result to stdout
            click.echo(decoded_output)
        else:
            # Output to file
            output.write_text(decoded_output, encoding="utf-8")
            # Success message to stdout
            click.secho(f"{message_count_text} successfully decoded to {output}", fg="green")
    except click.ClickException as e:
        raise
    except Exception as e:
        # Error message to stderr
        click.secho(f"Error decoding message: {str(e)}", err=True, fg="red")
        ctx.exit(1)


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
