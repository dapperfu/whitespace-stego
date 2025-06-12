# whitespace-stego

A steganographic encoding system that hides messages in text using zero-width Unicode characters. Messages can be optionally password-protected using AES-256 encryption.

## Features

- Hide messages invisibly in any text using zero-width Unicode characters
- Optional password protection using AES-256 encryption
- Command-line interface for easy use
- Support for file input/output
- Flexible message placement in carrier text

## Installation

```bash
pip install whitespace-stego
```

## Usage

### Encoding a Message

```bash
# Basic usage
whitespace-stego encode -m message.txt -c carrier.txt -o output.txt

# With password protection
whitespace-stego encode -m message.txt -c carrier.txt -p "secret" -o output.txt

# Interactive mode (no files)
whitespace-stego encode
```

### Decoding a Message

```bash
# Basic usage
whitespace-stego decode -i stego.txt

# With password protection
whitespace-stego decode -i stego.txt -p "secret"

# Save decoded message to file
whitespace-stego decode -i stego.txt -o message.txt

# Save carrier text without the message
whitespace-stego decode -i stego.txt --carrier-output carrier.txt
```

### Command-line Options

#### Encode Command

- `-m, --message`: Message file (optional, can enter interactively)
- `-c, --carrier`: Carrier text file (optional)
- `-p, --password`: Encryption password (optional)
- `-o, --output`: Output file (optional, prints to stdout if not specified)
- `--position`: Position to insert the message (optional, defaults to end)

#### Decode Command

- `-i, --input`: Input file containing the steganographic message
- `-p, --password`: Decryption password (optional)
- `-o, --output`: Output file for decoded message (optional)
- `--carrier-output`: Output file for carrier text without the message (optional)

## How It Works

1. The message is optionally encrypted using AES-256 if a password is provided
2. The message is base64 encoded to ensure compatibility
3. Each base64 character is converted to its 8-bit binary representation
4. The binary is encoded using zero-width Unicode characters:
   - `U+200B` (Zero-Width Space) → bit 0
   - `U+200C` (Zero-Width Non-Joiner) → bit 1
5. The encoded message is wrapped with control characters:
   - Start: `U+2060` (Word Joiner)
   - End: `U+2061` (Function Application)
6. The encoded message is inserted into the carrier text

## Security Notes

- The steganographic method itself is not secure - it only provides concealment
- Security comes from the optional AES-256 encryption
- The presence of zero-width characters can be detected by tools that scan for them
- Use password protection for sensitive messages

## License

MIT License 