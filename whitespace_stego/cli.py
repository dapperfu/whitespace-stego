"""Command-line interface for whitespace steganography.

This module provides a command-line interface for encoding and decoding
hidden messages in text using zero-width Unicode characters.
"""

import argparse
import sys
from typing import Optional
from pathlib import Path
from .encode import encode_and_insert
from .decode import decode_and_remove

def read_file(path: Path) -> str:
    """Read the contents of a file.
    
    Parameters
    ----------
    path : Path
        Path to the file to read.
        
    Returns
    -------
    str
        The contents of the file.
        
    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    try:
        return path.read_text()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)

def write_file(path: Path, content: str) -> None:
    """Write content to a file.
    
    Parameters
    ----------
    path : Path
        Path to the file to write.
    content : str
        The content to write.
    """
    path.write_text(content)

def encode_command(args: argparse.Namespace) -> None:
    """Handle the encode command.
    
    Parameters
    ----------
    args : argparse.Namespace
        Command-line arguments.
    """
    # Read input files
    message = read_file(args.message) if args.message else input("Enter message: ")
    carrier = read_file(args.carrier) if args.carrier else ""
    
    try:
        # Encode and insert the message
        result = encode_and_insert(
            message=message,
            carrier=carrier,
            password=args.password,
            position=args.position
        )
        
        # Write output
        if args.output:
            write_file(args.output, result)
        else:
            print(result)
            
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
    # Read input file
    text = read_file(args.input)
    
    try:
        # Decode the message
        message, carrier = decode_and_remove(text, args.password)
        
        # Write output
        if args.output:
            write_file(args.output, message)
        else:
            print("Decoded message:", message)
            
        if args.carrier_output:
            write_file(args.carrier_output, carrier)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Hide messages in text using zero-width Unicode characters"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode a message")
    encode_parser.add_argument("-m", "--message", type=Path, help="Message file")
    encode_parser.add_argument("-c", "--carrier", type=Path, help="Carrier text file")
    encode_parser.add_argument("-p", "--password", help="Encryption password")
    encode_parser.add_argument("-o", "--output", type=Path, help="Output file")
    encode_parser.add_argument(
        "--position", type=int,
        help="Position to insert the message (default: end)"
    )
    encode_parser.set_defaults(func=encode_command)
    
    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode a message")
    decode_parser.add_argument("-i", "--input", type=Path, required=True, help="Input file")
    decode_parser.add_argument("-p", "--password", help="Decryption password")
    decode_parser.add_argument("-o", "--output", type=Path, help="Output file")
    decode_parser.add_argument(
        "--carrier-output", type=Path,
        help="Output file for carrier text without the message"
    )
    decode_parser.set_defaults(func=decode_command)
    
    # Parse arguments and run command
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main() 