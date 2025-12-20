#!/usr/bin/env python3
"""Command-line interface for whitespace steganography."""

import argparse
import sys

from whitespace_stego import encode, decode
from whitespace_stego.errors import StegoError


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Encode and decode messages using invisible Unicode characters"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Encode command
    encode_parser = subparsers.add_parser("encode", help="Encode a message")
    encode_parser.add_argument(
        "message",
        nargs="?",
        help="Message to encode (use '-' or -i/--input to read from stdin/file)",
    )
    encode_parser.add_argument(
        "-i",
        "--input",
        help="Input file (use '-' for stdin)",
        type=str,
        default=None,
    )
    encode_parser.add_argument(
        "-c",
        "--carrier",
        help="Carrier text to embed the encoded message in",
        default=None,
    )
    encode_parser.add_argument(
        "-p",
        "--password",
        help="Password for encryption",
        default=None,
    )
    encode_parser.add_argument(
        "-o",
        "--output",
        help="Output file (default: stdout)",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
    )

    # Decode command
    decode_parser = subparsers.add_parser("decode", help="Decode a message")
    decode_parser.add_argument(
        "encoded",
        nargs="?",
        help="Encoded text to decode (use '-' or -i/--input to read from stdin/file)",
    )
    decode_parser.add_argument(
        "-i",
        "--input",
        help="Input file (use '-' for stdin)",
        type=str,
        default=None,
    )
    decode_parser.add_argument(
        "-p",
        "--password",
        help="Password for decryption",
        default=None,
    )
    decode_parser.add_argument(
        "-o",
        "--output",
        help="Output file (default: stdout)",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "encode":
            # Read message from input file, stdin, or positional argument
            if args.input is not None:
                if args.input == "-":
                    message = sys.stdin.read()
                else:
                    with open(args.input, "r", encoding="utf-8") as f:
                        message = f.read()
            elif args.message is not None:
                if args.message == "-":
                    message = sys.stdin.read()
                else:
                    message = args.message
            else:
                print("Error: message required (provide as argument, -i/--input, or '-' for stdin)", file=sys.stderr)
                sys.exit(1)

            # Encode
            encoded = encode(message, carrier=args.carrier, password=args.password)
            args.output.write(encoded)
            if args.output != sys.stdout:
                args.output.write("\n")

        elif args.command == "decode":
            # Read encoded text from input file, stdin, or positional argument
            if args.input is not None:
                if args.input == "-":
                    encoded_text = sys.stdin.read()
                else:
                    with open(args.input, "r", encoding="utf-8") as f:
                        encoded_text = f.read()
            elif args.encoded is not None:
                if args.encoded == "-":
                    encoded_text = sys.stdin.read()
                else:
                    encoded_text = args.encoded
            else:
                print("Error: encoded text required (provide as argument, -i/--input, or '-' for stdin)", file=sys.stderr)
                sys.exit(1)

            # Decode
            decoded = decode(encoded_text, password=args.password)
            args.output.write(decoded)
            if args.output != sys.stdout:
                args.output.write("\n")

    except StegoError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

