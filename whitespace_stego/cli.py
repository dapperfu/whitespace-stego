"""Command-line interface for whitespace steganography.

This module provides a command-line interface for encoding and decoding
hidden messages in text using zero-width Unicode characters.
"""

import argparse
import sys
from typing import Optional, TextIO, Any
from pathlib import Path
from .encode import encode_and_insert as py_encode_and_insert
from .decode import decode_and_remove as py_decode_and_remove
from . import rust_bridge

def read_text_source(source: Optional[Path], stdin: Optional[TextIO] = None) -> str:
    """Read text from a file or stdin.
    
    Parameters
    ----------
    source : Optional[Path]
        Path to the file to read, or None for stdin.
    stdin : Optional[TextIO]
        Stream to read from if source is None or '-'.
    
    Returns
    -------
    str
        The contents of the file or stdin.
    """
    if source is None or str(source) == "-":
        return (stdin or sys.stdin).read()
    return source.read_text()

# Re-export read_text_source as read_file for compatibility with tests
read_file = read_text_source

def write_text_sink(sink: Optional[Path], content: str, stdout: Optional[TextIO] = None) -> None:
    """Write text to a file or stdout.
    
    Parameters
    ----------
    sink : Optional[Path]
        Path to the file to write, or None for stdout.
    content : str
        The content to write.
    stdout : Optional[TextIO]
        Stream to write to if sink is None or '-'.
    """
    if sink is None or str(sink) == "-":
        (stdout or sys.stdout).write(content)
        if not content.endswith("\n"):
            (stdout or sys.stdout).write("\n")
    else:
        sink.write_text(content)

# Re-export write_text_sink as write_file for compatibility with tests
write_file = write_text_sink

def encode_command(args: argparse.Namespace) -> None:
    """Handle the encode command.
    
    Parameters
    ----------
    args : argparse.Namespace
        Command-line arguments.
    """
    message = read_text_source(getattr(args, "message_file", None), sys.stdin) if getattr(args, "message_file", None) else getattr(args, "message", "")
    carrier = read_text_source(getattr(args, "carrier_file", None), sys.stdin) if getattr(args, "carrier_file", None) else getattr(args, "carrier", "")
    backend = getattr(args, "backend", "python")
    try:
        if backend == "rust":
            if not rust_bridge.RUST_AVAILABLE:
                print("Error: Rust backend is not available.", file=sys.stderr)
                sys.exit(1)
            result = rust_bridge.encode_and_insert(
                message=message,
                carrier=carrier,
                password=getattr(args, "password", None),
                position=getattr(args, "position", None)
            )
        else:
            result = py_encode_and_insert(
                message=message,
                carrier=carrier,
                password=getattr(args, "password", None),
                position=getattr(args, "position", None)
            )
        write_text_sink(getattr(args, "output_file", None), result, sys.stdout)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def decode_command(args: argparse.Namespace) -> None:
    """Handle the decode command.
    
    Parameters
    ----------
    args : argparse.Namespace
        Command-line arguments.
    """
    text = read_text_source(getattr(args, "input_file", None), sys.stdin) if getattr(args, "input_file", None) else getattr(args, "input", "")
    backend = getattr(args, "backend", "python")
    try:
        if backend == "rust":
            if not rust_bridge.RUST_AVAILABLE:
                print("Error: Rust backend is not available.", file=sys.stderr)
                sys.exit(1)
            message, carrier = rust_bridge.decode_and_remove(text, getattr(args, "password", None))
        else:
            message, carrier = py_decode_and_remove(text, getattr(args, "password", None))
        write_text_sink(getattr(args, "output_file", None), message, sys.stdout)
        if getattr(args, "carrier_output_file", None):
            write_text_sink(getattr(args, "carrier_output_file", None), carrier, sys.stdout)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    """Main entry point for the CLI.
    
    Parses command-line arguments and dispatches to the appropriate command handler.
    """
    parser = argparse.ArgumentParser(
        description="Hide messages in text using zero-width Unicode characters"
    )
    parser.add_argument(
        "--backend",
        choices=["python", "rust"],
        default="python",
        help="Backend to use for encoding/decoding (default: python)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode a message")
    encode_parser.add_argument("-m", "--message", type=str, help="Message as a string")
    encode_parser.add_argument("-mf", "--message-file", type=Path, help="Message file ('-' for stdin)")
    encode_parser.add_argument("-c", "--carrier", type=str, help="Carrier text as a string")
    encode_parser.add_argument("-cf", "--carrier-file", type=Path, help="Carrier text file ('-' for stdin)")
    encode_parser.add_argument("-p", "--password", help="Encryption password")
    encode_parser.add_argument("-o", "--output", dest="output_file", type=Path, help="Output file ('-' for stdout)")
    encode_parser.add_argument("--output-file", dest="output_file_long", type=Path, help="Output file (long option, '-' for stdout)")
    encode_parser.add_argument(
        "--position", type=int,
        help="Position to insert the message (default: end)"
    )
    encode_parser.set_defaults(func=encode_command)
    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode a message")
    decode_parser.add_argument("-i", "--input", type=str, help="Input as a string")
    decode_parser.add_argument("-if", "--input-file", type=Path, help="Input file ('-' for stdin)")
    decode_parser.add_argument("-p", "--password", help="Decryption password")
    decode_parser.add_argument("-o", "--output", dest="output_file", type=Path, help="Output file ('-' for stdout)")
    decode_parser.add_argument("--output-file", dest="output_file_long", type=Path, help="Output file (long option, '-' for stdout)")
    decode_parser.add_argument("--carrier-output", dest="carrier_output_file", type=Path, help="Output file for carrier text ('-' for stdout)")
    decode_parser.set_defaults(func=decode_command)
    # Parse arguments
    args = parser.parse_args()
    # Handle output file aliases
    if hasattr(args, "output_file_long") and args.output_file_long is not None:
        args.output_file = args.output_file_long
    # Execute command
    args.func(args)

if __name__ == "__main__":
    main() 