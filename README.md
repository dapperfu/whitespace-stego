# Whitespace Steganography

This project implements a whitespace steganography tool that encodes messages using zero-width Unicode whitespace characters. It supports Python, Rust, and C implementations, with a CLI interface for each. The tool can hide secret messages within seemingly innocent text using invisible Unicode characters.

## Features

- **Multi-language support**: Python, Rust, and C implementations
- **Unicode support**: Works with any text including emojis and international characters
- **Password protection**: Optional encryption for your hidden messages
- **Cross-compatibility**: Messages encoded with one implementation can be decoded with another
- **Comprehensive testing**: 743+ tests ensuring reliability
- **Command-line interface**: Easy-to-use CLI for all implementations

## Installation

### Python Implementation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd whitespace-stego3
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies and build the Rust backend:
   ```bash
   make install
   ```

4. Install the Python package in development mode:
   ```bash
   pip install -e .
   ```

### Rust Implementation

1. Ensure you have Rust and Cargo installed. If not, install them from [rustup.rs](https://rustup.rs/).

2. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd whitespace-stego3
   ```

3. Build the Rust CLI:
   ```bash
   make rust
   ```

### C Implementation

1. Ensure you have a C compiler (gcc/clang) and make installed.

2. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd whitespace-stego3
   ```

3. Build the C CLI:
   ```bash
   make c
   ```

## Quick Start Examples

### Basic Usage

#### Python CLI

**Encode a simple message:**
```bash
python -m whitespace_stego.cli encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
```

**Decode the message:**
```bash
python -m whitespace_stego.cli decode --carrier-file encoded.txt --output decoded.txt
```

#### Rust CLI

**Encode a simple message:**
```bash
./rust/target/release/whitespace-stego-rs encode --mf message.txt --cf carrier.txt -o encoded.txt
```

**Decode the message:**
```bash
./rust/target/release/whitespace-stego-rs decode --cf encoded.txt -o decoded.txt
```

#### C CLI

**Encode a simple message:**
```bash
./c/bin/whitespace-stego encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
```

**Decode the message:**
```bash
./c/bin/whitespace-stego decode --carrier-file encoded.txt --output decoded.txt
```

### Advanced Examples

#### 1. Unicode and Emoji Support

**Python CLI:**
```bash
# Encode with emojis and international text
python -m whitespace_stego.cli encode \
  --message-file international_message.txt \
  --carrier-file carrier.txt \
  --output international_encoded.txt

# Decode
python -m whitespace_stego.cli decode \
  --carrier-file international_encoded.txt \
  --output international_decoded.txt
```

**Rust CLI:**
```bash
# Encode with emojis and international text
./rust/target/release/whitespace-stego-rs encode \
  --mf international_message.txt \
  --cf carrier.txt \
  -o international_encoded.txt

# Decode
./rust/target/release/whitespace-stego-rs decode \
  --cf international_encoded.txt \
  -o international_decoded.txt
```

**C CLI:**
```bash
# Encode with emojis and international text
./c/bin/whitespace-stego encode \
  --message-file international_message.txt \
  --carrier-file carrier.txt \
  --output international_encoded.txt

# Decode
./c/bin/whitespace-stego decode \
  --carrier-file international_encoded.txt \
  --output international_decoded.txt
```

#### 2. Password Protection

**Python CLI:**
```bash
# Encode with password
python -m whitespace_stego.cli encode \
  --message-file secret_message.txt \
  --carrier-file meeting_notes.txt \
  --password "mysecretpassword" \
  --output secret_encoded.txt

# Decode with password
python -m whitespace_stego.cli decode \
  --carrier-file secret_encoded.txt \
  --password "mysecretpassword" \
  --output secret_decoded.txt
```

**Rust CLI:**
```bash
# Encode with password
./rust/target/release/whitespace-stego-rs encode \
  --mf secret_message.txt \
  --cf meeting_notes.txt \
  -p "mysecretpassword" \
  -o secret_encoded.txt

# Decode with password
./rust/target/release/whitespace-stego-rs decode \
  --cf secret_encoded.txt \
  -p "mysecretpassword" \
  -o secret_decoded.txt
```

**C CLI:**
```bash
# Encode with password
./c/bin/whitespace-stego encode \
  --message-file secret_message.txt \
  --carrier-file meeting_notes.txt \
  --password "mysecretpassword" \
  --output secret_encoded.txt

# Decode with password
./c/bin/whitespace-stego decode \
  --carrier-file secret_encoded.txt \
  --password "mysecretpassword" \
  --output secret_decoded.txt
```

#### 3. Backend Selection (Python CLI)

The Python CLI supports multiple backends:

```bash
# Use Python backend (default)
python -m whitespace_stego.cli --backend python encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output python_encoded.txt

# Use Rust backend
python -m whitespace_stego.cli --backend rust encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output rust_encoded.txt

# Use C backend
python -m whitespace_stego.cli --backend c encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output c_encoded.txt
```

#### 4. Cross-Implementation Compatibility

Messages encoded with one implementation can be decoded with another:

```bash
# Encode with Python CLI using Rust backend
python -m whitespace_stego.cli --backend rust encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output cross_encoded.txt

# Decode with Rust CLI
./rust/target/release/whitespace-stego-rs decode --cf cross_encoded.txt -o cross_decoded.txt

# Decode with C CLI
./c/bin/whitespace-stego decode --carrier-file cross_encoded.txt --output cross_decoded_c.txt
```

#### 5. Inline Text Input (Rust CLI)

The Rust CLI supports inline text input in addition to file input:

```bash
# Encode with inline text
./rust/target/release/whitespace-stego-rs encode \
  -m "Secret message" \
  -c "This is innocent text" \
  -o encoded.txt

# Decode with inline text
./rust/target/release/whitespace-stego-rs decode \
  -c "$(cat encoded.txt)" \
  -o decoded.txt
```

#### 6. Output to stdout

All implementations support output to stdout:

**Python CLI:**
```bash
python -m whitespace_stego.cli encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output -
```

**Rust CLI:**
```bash
./rust/target/release/whitespace-stego-rs encode \
  --mf message.txt \
  --cf carrier.txt \
  -o -
```

**C CLI:**
```bash
./c/bin/whitespace-stego encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output -
```

#### 7. Verbose Output

All implementations support verbose output for debugging:

**Python CLI:**
```bash
python -m whitespace_stego.cli --verbose encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output encoded.txt
```

**Rust CLI:**
```bash
./rust/target/release/whitespace-stego-rs --verbose encode \
  --mf message.txt \
  --cf carrier.txt \
  -o encoded.txt
```

**C CLI:**
```bash
./c/bin/whitespace-stego --verbose encode \
  --message-file message.txt \
  --carrier-file carrier.txt \
  --output encoded.txt
```

## API Usage

### Python API

```python
from whitespace_stego.core import encode, decode

# Encode a message
carrier = "This is innocent text."
message = "Secret message"
encoded = encode(message, carrier)
print(f"Encoded: {encoded}")

# Decode a message
decoded = decode(encoded)
print(f"Decoded: {decoded}")

# With password protection
encoded_secure = encode(message, carrier, password="secret123")
decoded_secure = decode(encoded_secure, password="secret123")
```

### Rust API

```rust
use whitespace_stego_core::{encode, decode};

fn main() {
    let carrier = "This is innocent text.";
    let message = "Secret message";
    
    // Encode a message
    let encoded = encode(message, carrier, None).unwrap();
    println!("Encoded: {}", encoded);
    
    // Decode a message
    let decoded = decode(&encoded, None).unwrap();
    println!("Decoded: {}", decoded);
    
    // With password protection
    let encoded_secure = encode(message, carrier, Some("secret123")).unwrap();
    let decoded_secure = decode(&encoded_secure, Some("secret123")).unwrap();
}
```

## Command Line Options

### Python CLI

```bash
python -m whitespace_stego.cli --help
```

**Global options:**
- `--verbose, -v`: Enable verbose output
- `--backend, -b`: Backend implementation to use (python, c, rust)
- `--help`: Show help message

**Encode command:**
```bash
python -m whitespace_stego.cli encode --help
```

- `--message-file, -m`: Path to file containing message to encode **[required]**
- `--carrier-file, -c`: Path to carrier file **[required]**
- `--output, -o`: Output file path **[required]**
- `--password, -p`: Optional password for encryption
- `--help`: Show help message

**Decode command:**
```bash
python -m whitespace_stego.cli decode --help
```

- `--carrier-file, -c`: Path to encoded carrier file **[required]**
- `--output, -o`: Output file path **[required]**
- `--password, -p`: Password for decryption (if used during encoding)
- `--help`: Show help message

### Rust CLI

```bash
./rust/target/release/whitespace-stego-rs --help
```

**Global options:**
- `--help, -h`: Show help message
- `--version, -V`: Show version information

**Encode command:**
```bash
./rust/target/release/whitespace-stego-rs encode --help
```

- `--message, -m`: Message to encode (inline text)
- `--mf`: File containing message to encode
- `--carrier, -c`: Carrier text (inline text)
- `--cf`: File containing carrier text
- `--output, -o`: Output file (default: stdout)
- `--password, -p`: Password for encryption
- `--help, -h`: Show help message
- `--version, -V`: Show version information

**Decode command:**
```bash
./rust/target/release/whitespace-stego-rs decode --help
```

- `--carrier, -c`: Carrier text (inline text)
- `--cf`: File containing carrier text
- `--output, -o`: Output file (default: stdout)
- `--password, -p`: Password for decryption
- `--help, -h`: Show help message
- `--version, -V`: Show version information

### C CLI

```bash
./c/bin/whitespace-stego --help
```

**Global options:**
- `--verbose, -v`: Enable verbose output
- `--help, -h`: Show help message

**Encode command:**
```bash
./c/bin/whitespace-stego help encode
```

- `--message-file, -m`: Path to file containing message to encode **[required]**
- `--carrier-file, -c`: Path to carrier file **[required]**
- `--output, -o`: Path where encoded file will be saved **[required]**
- `--password, -p`: Optional password for encryption
- `--help, -h`: Show help message

**Decode command:**
```bash
./c/bin/whitespace-stego help decode
```

- `--carrier-file, -c`: Path to encoded carrier file **[required]**
- `--output, -o`: Path where decoded message will be saved **[required]**
- `--password, -p`: Password for decryption (if used during encoding)
- `--help, -h`: Show help message

## Testing

Run the comprehensive test suite:

```bash
make test
```

This will run 743+ tests covering:
- Basic encoding/decoding
- Unicode and emoji support
- Password protection
- Cross-backend compatibility
- Cross-tool roundtrips
- CLI functionality

## How It Works

The tool uses zero-width Unicode characters to hide binary data within text:

- **Zero-width space** (`\u200B`): Used for binary encoding
- **Zero-width joiner** (`\u200D`): Used for binary encoding
- **Zero-width non-joiner** (`\u200C`): Used as end marker
- **Zero-width no-break space** (`\uFEFF`): Used as end marker

The message is:
1. Converted to UTF-8 bytes
2. Base64 encoded
3. Optionally encrypted with a password
4. Converted to binary
5. Encoded using zero-width characters
6. Embedded in the carrier text

## Security Notes

- **Password protection**: Uses Fernet encryption for password-protected messages
- **Steganographic security**: Messages are hidden using invisible characters
- **Cross-compatibility**: Messages work across Python, Rust, and C implementations
- **No metadata**: No additional information is stored about the hidden message

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite: `make test`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 