[![CI](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml)
[![Build & Test](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml)
[![Docker](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml)
[![Nightly](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml)

# Whitespace Steganography - Python Implementation

A high-performance Python implementation of whitespace steganography with multiple backends (Python, Rust, C) for hiding messages in text using invisible Unicode characters.

## Features

- **Multiple Backends**: Python, Rust, and C implementations
- **High Performance**: Optimized for speed with Rust and C backends
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **Comprehensive Testing**: 1300+ tests ensuring reliability
- **Unicode Support**: Full Unicode and emoji compatibility
- **Password Protection**: Optional AES-256 encryption
- **Library Usage**: Can be used as a Python module
- **CLI Interface**: Command-line tool for easy use

## Requirements

- Python 3.8 or later
- pip
- make (optional, for using Makefile)
- Rust (for Rust backend)
- C compiler (for C backend)

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv build-essential libssl-dev make
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### macOS
```bash
brew install python3 make
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Windows
- Download Python from https://python.org/
- Install Make via Chocolatey: `choco install make`
- Download Rust from https://rustup.rs/

## Quick Start

### Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package
pip install -e .

# Build backends
make build-backends
```

### Basic Usage
```bash
# Encode a message
whitespace-stego encode -m "Hello, World!" --carrier-file input.txt -o output.txt

# Decode a message
whitespace-stego decode --carrier-file output.txt -o decoded.txt

# Use specific backend
whitespace-stego -b rust encode -m "secret" --carrier-file input.txt -o output.txt
```

## Project Structure

```
python/
├── whitespace_stego/        # Main package
│   ├── __init__.py         # Package initialization
│   ├── core.py             # Core implementation
│   ├── cli.py              # CLI interface
│   ├── constants.py        # Constants and configuration
│   ├── logger.py           # Logging utilities
│   └── c_backend.py        # C backend integration
├── tests/                  # Test suites
├── setup.py                # Package configuration
├── pyproject.toml          # Modern Python packaging
├── pytest.ini             # pytest configuration
├── Makefile                # Build system
└── README.md               # This file
```

## API Usage

### As a Library

```python
import whitespace_stego

# Encode a message
encoded = whitespace_stego.encode("Hello, World!", "Carrier text", password="secret")
print(f"Encoded: {encoded}")

# Decode a message
decoded = whitespace_stego.decode(encoded, password="secret")
print(f"Decoded: {decoded}")

# Use specific backend
encoded_rust = whitespace_stego.encode("Hello!", "Carrier", backend="rust")
encoded_c = whitespace_stego.encode("Hello!", "Carrier", backend="c")
```

### As a CLI Tool

```bash
# Basic encoding/decoding
whitespace-stego encode -m "secret message" --carrier-file input.txt -o output.txt
whitespace-stego decode --carrier-file output.txt -o decoded.txt

# With password protection
whitespace-stego encode -m "secret" --carrier-file input.txt -p "password" -o output.txt
whitespace-stego decode --carrier-file output.txt -p "password" -o decoded.txt

# Using specific backend
whitespace-stego -b rust encode -m "secret" --carrier-file input.txt -o output.txt
whitespace-stego -b c encode -m "secret" --carrier-file input.txt -o output.txt
```

## Extensive Examples

### Complete Setup and Build Example

```bash
# Navigate to the Python implementation directory
cd implementations/python

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode
pip install -e .

# Build all backends
make build-backends

# Verify installation
whitespace-stego --help
python3 -c "import whitespace_stego; print('✅ Package installed successfully')"
```

### Basic Encoding and Decoding Examples

```bash
# Create test files
echo "This is a secret message that needs to be hidden." > secret_message.txt
echo "This is innocent text that will serve as a carrier for the hidden message. It contains normal content that nobody would suspect contains hidden information." > carrier_text.txt

# Encode a message using command line arguments
whitespace-stego encode -m "Hello, World!" --carrier-file carrier_text.txt -o encoded.txt

# Encode a message using input files
whitespace-stego encode -mf secret_message.txt --carrier-file carrier_text.txt -o encoded_with_files.txt

# Decode the message
whitespace-stego decode --carrier-file encoded.txt -o decoded.txt

# View the results
echo "Original message:"
cat secret_message.txt
echo -e "\nEncoded carrier:"
cat encoded.txt
echo -e "\nDecoded message:"
cat decoded.txt
```

### Backend Comparison Examples

```bash
# Test all backends with the same input
echo "Testing all backends..."

# Python backend
whitespace-stego -b python encode -m "Hello from Python!" --carrier-file carrier_text.txt -o encoded_python.txt
whitespace-stego -b python decode --carrier-file encoded_python.txt -o decoded_python.txt

# Rust backend
whitespace-stego -b rust encode -m "Hello from Rust!" --carrier-file carrier_text.txt -o encoded_rust.txt
whitespace-stego -b rust decode --carrier-file encoded_rust.txt -o decoded_rust.txt

# C backend
whitespace-stego -b c encode -m "Hello from C!" --carrier-file carrier_text.txt -o encoded_c.txt
whitespace-stego -b c decode --carrier-file encoded_c.txt -o decoded_c.txt

# Compare results
echo "Backend comparison results:"
echo "Python decoded: $(cat decoded_python.txt)"
echo "Rust decoded: $(cat decoded_rust.txt)"
echo "C decoded: $(cat decoded_c.txt)"
```

### Advanced Usage Examples

```bash
# Encode with password protection
whitespace-stego encode -m "Top secret information" --carrier-file carrier_text.txt -p "mysecretpass" -o protected.txt

# Decode with password
whitespace-stego decode --carrier-file protected.txt -p "mysecretpass" -o decrypted.txt

# Encode a long message
cat > long_message.txt << 'EOF'
This is a very long secret message that contains multiple lines
of sensitive information that needs to be hidden within innocent
text. The message can be quite long and contain various types
of content including numbers, symbols, and special characters.
EOF

cat > long_carrier.txt << 'EOF'
This is a long document that appears to be a normal text file.
It contains various paragraphs and sections that make it look
like legitimate content. Nobody would suspect that this text
contains hidden information encoded using whitespace steganography.
The document continues with more content to provide sufficient
space for hiding the secret message.
EOF

whitespace-stego encode -mf long_message.txt --carrier-file long_carrier.txt -o long_encoded.txt
whitespace-stego decode --carrier-file long_encoded.txt -o long_decoded.txt

# Verify the encoding worked
diff long_message.txt long_decoded.txt && echo "✅ Encoding/decoding successful!"
```

### Unicode and Emoji Examples

```bash
# Create test files with Unicode and emoji
cat > unicode_message.txt << 'EOF'
Hello, 世界! 🌍
This message contains:
- Chinese characters: 你好世界
- Japanese: こんにちは世界
- Korean: 안녕하세요 세계
- Emojis: 🚀 🎉 💻 🔐
- Special symbols: © ® ™ € £ ¥
EOF

cat > unicode_carrier.txt << 'EOF'
This is a document with various Unicode content:
- English: Hello World
- Español: ¡Hola Mundo!
- Français: Bonjour le Monde!
- Deutsch: Hallo Welt!
- Italiano: Ciao Mondo!
- Português: Olá Mundo!
- Русский: Привет Мир!
- العربية: مرحبا بالعالم!
- हिन्दी: नमस्ते दुनिया!
- 中文: 你好世界!
- 日本語: こんにちは世界!
- 한국어: 안녕하세요 세계!
EOF

# Test Unicode support with all backends
whitespace-stego -b python encode -mf unicode_message.txt --carrier-file unicode_carrier.txt -o unicode_encoded_python.txt
whitespace-stego -b rust encode -mf unicode_message.txt --carrier-file unicode_carrier.txt -o unicode_encoded_rust.txt
whitespace-stego -b c encode -mf unicode_message.txt --carrier-file unicode_carrier.txt -o unicode_encoded_c.txt

# Decode and verify
whitespace-stego -b python decode --carrier-file unicode_encoded_python.txt -o unicode_decoded_python.txt
whitespace-stego -b rust decode --carrier-file unicode_encoded_rust.txt -o unicode_decoded_rust.txt
whitespace-stego -b c decode --carrier-file unicode_encoded_c.txt -o unicode_decoded_c.txt

# Verify Unicode preservation
echo "Unicode compatibility test results:"
diff unicode_message.txt unicode_decoded_python.txt && echo "✅ Python backend: Unicode preserved"
diff unicode_message.txt unicode_decoded_rust.txt && echo "✅ Rust backend: Unicode preserved"
diff unicode_message.txt unicode_decoded_c.txt && echo "✅ C backend: Unicode preserved"
```

### Performance Testing Examples

```bash
# Create large test files
dd if=/dev/urandom bs=1M count=10 | tr -dc 'a-zA-Z0-9 ' > large_carrier.txt
echo "Secret message for performance testing" > test_message.txt

# Test encoding performance across all backends
echo "Testing encoding performance..."
echo "Python backend:"
time whitespace-stego -b python encode -mf test_message.txt --carrier-file large_carrier.txt -o large_encoded_python.txt

echo "Rust backend:"
time whitespace-stego -b rust encode -mf test_message.txt --carrier-file large_carrier.txt -o large_encoded_rust.txt

echo "C backend:"
time whitespace-stego -b c encode -mf test_message.txt --carrier-file large_carrier.txt -o large_encoded_c.txt

# Test decoding performance
echo "Testing decoding performance..."
echo "Python backend:"
time whitespace-stego -b python decode --carrier-file large_encoded_python.txt -o large_decoded_python.txt

echo "Rust backend:"
time whitespace-stego -b rust decode --carrier-file large_encoded_rust.txt -o large_decoded_rust.txt

echo "C backend:"
time whitespace-stego -b c decode --carrier-file large_encoded_c.txt -o large_decoded_c.txt

# Verify correctness
echo "Performance test verification:"
diff test_message.txt large_decoded_python.txt && echo "✅ Python backend: Correct"
diff test_message.txt large_decoded_rust.txt && echo "✅ Rust backend: Correct"
diff test_message.txt large_decoded_c.txt && echo "✅ C backend: Correct"
```

### Testing Examples

```bash
# Run all tests
make test
```

### Run with Coverage
```bash
make coverage
```

### Run Specific Test Suites
```bash
pytest tests/test_00_parametrized_core_and_rust.py -v
pytest tests/test_01_multiple_messages.py -v
pytest tests/test_02_whitespace_stego_decode.py -v
pytest tests/test_03_whitespace_stego_encode.py -v
pytest tests/test_04_whitespace_stego_core.py -v
pytest tests/test_05_whitespace_stego_cli.py -v
```

### Cross-Implementation Tests
```bash
pytest tests/test_20_cross_impl_roundtrip.py -v
pytest tests/test_21_unicode_cross_impl.py -v
pytest tests/test_22_comprehensive_encoding_identity.py -v
```

### Security Tests
```bash
pytest tests/test_30_security_and_cryptography.py -v
```

### Property-Based Tests
```bash
pytest tests/test_40_fuzz_and_property.py -v
pytest tests/test_41_protocol_and_constants.py -v
```

## Development

### Development Setup
```bash
pip install -e .
make build-backends
```

### Code Quality
```bash
make lint      # Run linter
make type-check # Run type checker
make check-all  # Run all checks
```

### All Checks
```bash
make check-all
```

## Installation

### Development Installation
```bash
pip install -e .
```

### System-wide Installation
```bash
make install
```

### Uninstall
```bash
make uninstall
```

## Dependencies

This implementation uses:

- **Core Dependencies**: See `setup.py` and `pyproject.toml`
- **Development Dependencies**: See `requirements-dev.txt`
- **Optional Tools**: 
  - `pytest` for testing
  - `pytest-cov` for coverage
  - `mypy` for type checking
  - `black` for code formatting
  - `flake8` for linting

## Building from Source

1. Clone the repository
2. Navigate to the Python directory: `cd python`
3. Create virtual environment: `python3 -m venv venv`
4. Activate environment: `source venv/bin/activate`
5. Install: `pip install -e .`
6. Build backends: `make build-backends`
7. Test: `make test`
8. Install: `make install`

## Performance

The Python implementation is optimized for:
- **Multiple Backends**: Choose the fastest backend for your use case
- **Memory Efficiency**: Efficient memory usage across all backends
- **CPU Performance**: Rust and C backends provide near-native performance
- **Cross-Platform**: Works on all major platforms

## Security

### Password Protection
```bash
# Use AES-256 encryption
whitespace-stego encode -m "secret" --carrier-file input.txt -p "strong_password" -o output.txt
whitespace-stego decode --carrier-file output.txt -p "strong_password" -o decoded.txt
```

### Dependency Auditing
```bash
pip audit
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Check code quality: `make check-all`
7. Submit a pull request

## License

This project is licensed under the same license as the main whitespace-stego project.

## Support

For issues and questions:
- Check the main project documentation
- Review the test files for usage examples
- Run `make help` for available commands
- Check Python version compatibility: `make check-python`
- Generate documentation: `make doc`