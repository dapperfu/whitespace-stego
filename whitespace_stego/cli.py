"""Command-line interface for whitespace steganography."""

import sys
from typing import Optional

import click

from whitespace_stego.core import decode, encode

@click.group()
def cli() -> None:
    """Zero-width whitespace steganography tool."""
    pass

@cli.command()
@click.option("-m", "--message", help="Message to encode")
@click.option("-mf", "--message-file", type=click.Path(exists=True), help="File containing message to encode")
@click.option("-c", "--carrier", help="Carrier text")
@click.option("-cf", "--carrier-file", type=click.Path(exists=True), help="File containing carrier text")
@click.option("-p", "--password", help="Password for encryption")
@click.option("-pf", "--password-file", type=click.Path(exists=True), help="File containing password")
@click.option("-o", "--output", type=click.Path(), help="Output file (default: stdout)")
def encode_cmd(
    message: Optional[str],
    message_file: Optional[str],
    carrier: Optional[str],
    carrier_file: Optional[str],
    password: Optional[str],
    password_file: Optional[str],
    output: Optional[str],
) -> None:
    """Encode a message into carrier text."""
    # Read message
    if message_file:
        with open(message_file, "r") as f:
            message = f.read().strip()
    if not message:
        raise click.UsageError("Message is required (--message or --message-file)")

    # Read carrier
    if carrier_file:
        with open(carrier_file, "r") as f:
            carrier = f.read().strip()
    if not carrier:
        carrier = ""

    # Read password
    if password_file:
        with open(password_file, "r") as f:
            password = f.read().strip()

    # Encode message
    result = encode(message, carrier, password)

    # Write output
    if output:
        with open(output, "w") as f:
            f.write(result)
    else:
        click.echo(result)

@cli.command()
@click.option("-c", "--carrier", help="Carrier text")
@click.option("-cf", "--carrier-file", type=click.Path(exists=True), help="File containing carrier text")
@click.option("-p", "--password", help="Password for decryption")
@click.option("-pf", "--password-file", type=click.Path(exists=True), help="File containing password")
@click.option("-o", "--output", type=click.Path(), help="Output file (default: stdout)")
def decode_cmd(
    carrier: Optional[str],
    carrier_file: Optional[str],
    password: Optional[str],
    password_file: Optional[str],
    output: Optional[str],
) -> None:
    """Decode a message from carrier text."""
    # Read carrier
    if carrier_file:
        with open(carrier_file, "r") as f:
            carrier = f.read().strip()
    if not carrier:
        raise click.UsageError("Carrier is required (--carrier or --carrier-file)")

    # Read password
    if password_file:
        with open(password_file, "r") as f:
            password = f.read().strip()

    try:
        # Decode message
        result = decode(carrier, password)

        # Write output
        if output:
            with open(output, "w") as f:
                f.write(result)
        else:
            click.echo(result)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    cli() 