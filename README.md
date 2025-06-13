# Whitespace Steganography

A zero-width Unicode steganography toolkit that hides base64-encoded (and optionally encrypted) messages invisibly within a carrier text.

## Installation

```bash
# Create and activate virtual environment
make venv
source .venv/bin/activate
```

## Usage

### Command Line Interface

```bash
# Encode a message
whitespace_stego_py encode -m "Secret message" -c "Public text" -p "password"

# Decode a message
whitespace_stego_py decode -c "Public text" -p "password"
```

### Python API

```python
from whitespace_stego.core import encode, decode

# Encode a message
encoded = encode("Secret message", "Public text", password="password")

# Decode a message
decoded = decode(encoded, password="password")
```

## Development

```bash
# Run tests
make test

# Clean up
make clean
```

## Features

- Zero-width character encoding
- Optional AES-256 encryption
- Base64 encoding for binary data
- Command-line interface
- Python API
