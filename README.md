[![CI](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml)
[![Build & Test](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml)
[![Docker](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml)
[![Nightly](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml)

# Whitespace Steganography

A multi-language implementation of whitespace steganography with support for Python, Rust, Go, and C.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/dapperfu/whitespace-stego.git
cd whitespace-stego

# Set up the environment
make venv
make install

# Run tests
make test

# Build all binaries
make all
```

## 📁 Project Structure

```
whitespace-stego/
├── implementations/          # Language-specific implementations
│   ├── python/              # Python implementation with multiple backends
│   ├── rust/                # Rust CLI implementation
│   ├── go/                  # Go CLI implementation
│   └── c/                   # C CLI implementation
├── bin/                     # Compiled binaries (created by make all)
├── tests/                   # Test suites
├── docs/                    # Documentation
├── examples/                # Usage examples
├── notebooks/               # Jupyter notebooks for exploration
└── scripts/                 # Utility scripts
```

## 🛠️ Build System

The project uses a unified Makefile for all operations:

```bash
# Core targets
make venv                    # Create Python virtual environment
make install                 # Install Python package and dependencies
make test                    # Run all tests
make all                     # Build all binaries (Go, Rust, C, Python)

# Language-specific builds
make rust                    # Build Rust binary
make go                      # Build Go binary
make c                       # Build C binary

# Coverage and testing
make coverage                # Run coverage for all languages
make cov-python              # Python tests with coverage
make cov-rust                # Rust tests with coverage
make cov-go                  # Go tests with coverage
make cov-c                   # C tests with coverage
```

## 🔧 Implementations

### Python Implementation
- **Multiple backends**: Python, Rust, and C
- **CLI interface**: `whitespace-stego` command
- **Library usage**: Import `whitespace_stego` module
- **Features**: Unicode support, password protection, multiple message encoding

### Rust Implementation
- **Standalone binary**: `whitespace-stego-rs`
- **High performance**: Optimized for speed
- **Cross-platform**: Works on Linux, macOS, Windows

### Go Implementation
- **Standalone binary**: `whitespace-stego-go`
- **Simple deployment**: Single executable
- **Fast compilation**: Quick development cycle

### C Implementation
- **Standalone binary**: `whitespace-stego-c`
- **Minimal dependencies**: Only standard C library
- **Portable**: Works on any system with a C compiler

## 📖 Usage

### Python CLI
```bash
# Encode a message
whitespace-stego encode -m "secret message" --carrier-file input.txt -o output.txt

# Decode a message
whitespace-stego decode --carrier-file output.txt -o decoded.txt

# Use specific backend
whitespace-stego -b rust encode -m "secret" --carrier-file input.txt -o output.txt
```

### Standalone Binaries
```bash
# Rust
./bin/whitespace-stego-rs encode -m "secret" --cf input.txt -o output.txt

# Go
./bin/whitespace-stego-go encode -m "secret" -cf input.txt -o output.txt

# C
./bin/whitespace-stego-c encode --message-file message.txt --carrier-file input.txt --output output.txt
```

## 🎯 Extensive Examples

### Complete Setup and Build Example

```bash
# Clone and set up the project
git clone https://github.com/dapperfu/whitespace-stego.git
cd whitespace-stego

# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install build-essential libssl-dev make cmake lcov golang-go

# Set up Python environment
make venv
source .venv/bin/activate
make install

# Build all implementations
make all

# Verify all binaries were created
ls -la bin/
```

### Basic Encoding and Decoding Examples

```bash
# Create test files
echo "This is a secret message that needs to be hidden." > secret_message.txt
echo "This is innocent text that will serve as a carrier for the hidden message. It contains normal content that nobody would suspect contains hidden information." > carrier_text.txt

# Python CLI examples
whitespace-stego encode -m "Hello, World!" --carrier-file carrier_text.txt -o python_encoded.txt
whitespace-stego decode --carrier-file python_encoded.txt -o python_decoded.txt

# Rust CLI examples
./bin/whitespace-stego-rs encode --message "Hello, World!" --carrier-file carrier_text.txt --output rust_encoded.txt
./bin/whitespace-stego-rs decode --carrier-file rust_encoded.txt --output rust_decoded.txt

# Go CLI examples
./bin/whitespace-stego-go encode -m "Hello, World!" -cf carrier_text.txt -o go_encoded.txt
./bin/whitespace-stego-go decode -cf go_encoded.txt -o go_decoded.txt

# C CLI examples
./bin/whitespace-stego-c encode --message "Hello, World!" --carrier-file carrier_text.txt --output c_encoded.txt
./bin/whitespace-stego-c decode --carrier-file c_encoded.txt --output c_decoded.txt

# View the results
echo "Original message:"
cat secret_message.txt
echo -e "\nPython decoded:"
cat python_decoded.txt
echo -e "\nRust decoded:"
cat rust_decoded.txt
echo -e "\nGo decoded:"
cat go_decoded.txt
echo -e "\nC decoded:"
cat c_decoded.txt
```

### Advanced Usage Examples

```bash
# Encode with password protection (Python)
whitespace-stego encode -m "Top secret information" --carrier-file carrier_text.txt -p "mysecretpass" -o protected.txt
whitespace-stego decode --carrier-file protected.txt -p "mysecretpass" -o decrypted.txt

# Encode with password protection (Rust)
./bin/whitespace-stego-rs encode --message "Top secret information" --carrier-file carrier_text.txt --password "mysecretpass" --output protected_rust.txt
./bin/whitespace-stego-rs decode --carrier-file protected_rust.txt --password "mysecretpass" --output decrypted_rust.txt

# Encode with password protection (Go)
./bin/whitespace-stego-go encode -m "Top secret information" -cf carrier_text.txt -p "mysecretpass" -o protected_go.txt
./bin/whitespace-stego-go decode -cf protected_go.txt -p "mysecretpass" -o decrypted_go.txt

# Encode with password protection (C)
./bin/whitespace-stego-c encode --message "Top secret information" --carrier-file carrier_text.txt --password "mysecretpass" --output protected_c.txt
./bin/whitespace-stego-c decode --carrier-file protected_c.txt --password "mysecretpass" --output decrypted_c.txt
```

### Cross-Language Compatibility Examples

```bash
# Encode with Python, decode with Rust
whitespace-stego encode -m "Cross-language test" --carrier-file carrier_text.txt -o cross_test.txt
./bin/whitespace-stego-rs decode --carrier-file cross_test.txt --output cross_decoded_rust.txt

# Encode with Rust, decode with Go
./bin/whitespace-stego-rs encode --message "Cross-language test" --carrier-file carrier_text.txt --output cross_test_rust.txt
./bin/whitespace-stego-go decode -cf cross_test_rust.txt -o cross_decoded_go.txt

# Encode with Go, decode with C
./bin/whitespace-stego-go encode -m "Cross-language test" -cf carrier_text.txt -o cross_test_go.txt
./bin/whitespace-stego-c decode --carrier-file cross_test_go.txt --output cross_decoded_c.txt

# Encode with C, decode with Python
./bin/whitespace-stego-c encode --message "Cross-language test" --carrier-file carrier_text.txt --output cross_test_c.txt
whitespace-stego decode --carrier-file cross_test_c.txt -o cross_decoded_python.txt

# Verify all cross-language tests
echo "Cross-language compatibility test results:"
diff cross_decoded_rust.txt cross_decoded_go.txt && echo "✅ Rust ↔ Go: Compatible"
diff cross_decoded_go.txt cross_decoded_c.txt && echo "✅ Go ↔ C: Compatible"
diff cross_decoded_c.txt cross_decoded_python.txt && echo "✅ C ↔ Python: Compatible"
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

# Test Unicode support across all implementations
whitespace-stego encode -mf unicode_message.txt --carrier-file unicode_carrier.txt -o unicode_encoded_python.txt
./bin/whitespace-stego-rs encode --message-file unicode_message.txt --carrier-file unicode_carrier.txt --output unicode_encoded_rust.txt
./bin/whitespace-stego-go encode -mf unicode_message.txt -cf unicode_carrier.txt -o unicode_encoded_go.txt
./bin/whitespace-stego-c encode --message-file unicode_message.txt --carrier-file unicode_carrier.txt --output unicode_encoded_c.txt

# Decode and verify
whitespace-stego decode --carrier-file unicode_encoded_python.txt -o unicode_decoded_python.txt
./bin/whitespace-stego-rs decode --carrier-file unicode_encoded_rust.txt --output unicode_decoded_rust.txt
./bin/whitespace-stego-go decode -cf unicode_encoded_go.txt -o unicode_decoded_go.txt
./bin/whitespace-stego-c decode --carrier-file unicode_encoded_c.txt --output unicode_decoded_c.txt

# Verify Unicode preservation
echo "Unicode compatibility test results:"
diff unicode_message.txt unicode_decoded_python.txt && echo "✅ Python: Unicode preserved"
diff unicode_message.txt unicode_decoded_rust.txt && echo "✅ Rust: Unicode preserved"
diff unicode_message.txt unicode_decoded_go.txt && echo "✅ Go: Unicode preserved"
diff unicode_message.txt unicode_decoded_c.txt && echo "✅ C: Unicode preserved"
```

### Performance Testing Examples

```bash
# Create large test files
dd if=/dev/urandom bs=1M count=10 | tr -dc 'a-zA-Z0-9 ' > large_carrier.txt
echo "Secret message for performance testing" > test_message.txt

# Test encoding performance across all implementations
echo "Testing encoding performance..."
echo "Python:"
time whitespace-stego encode -mf test_message.txt --carrier-file large_carrier.txt -o large_encoded_python.txt

echo "Rust:"
time ./bin/whitespace-stego-rs encode --message-file test_message.txt --carrier-file large_carrier.txt --output large_encoded_rust.txt

echo "Go:"
time ./bin/whitespace-stego-go encode -mf test_message.txt -cf large_carrier.txt -o large_encoded_go.txt

echo "C:"
time ./bin/whitespace-stego-c encode --message-file test_message.txt --carrier-file large_carrier.txt --output large_encoded_c.txt

# Test decoding performance
echo "Testing decoding performance..."
echo "Python:"
time whitespace-stego decode --carrier-file large_encoded_python.txt -o large_decoded_python.txt

echo "Rust:"
time ./bin/whitespace-stego-rs decode --carrier-file large_encoded_rust.txt --output large_decoded_rust.txt

echo "Go:"
time ./bin/whitespace-stego-go decode -cf large_encoded_go.txt -o large_decoded_go.txt

echo "C:"
time ./bin/whitespace-stego-c decode --carrier-file large_encoded_c.txt --output large_decoded_c.txt

# Verify correctness
echo "Performance test verification:"
diff test_message.txt large_decoded_python.txt && echo "✅ Python: Correct"
diff test_message.txt large_decoded_rust.txt && echo "✅ Rust: Correct"
diff test_message.txt large_decoded_go.txt && echo "✅ Go: Correct"
diff test_message.txt large_decoded_c.txt && echo "✅ C: Correct"
```

### Testing Examples

```bash
# Run all tests
make test

# Run specific language tests
make cov-python
make cov-rust
make cov-go
make cov-c

# Run cross-language integration tests
bash scripts/test_scripts/test_cross_roundtrip.sh

# Run standalone binary tests
bash scripts/test_scripts/test_standalone_binaries.sh

# Run comprehensive tests
bash scripts/test_scripts/comprehensive_test.sh
```

### Development Examples

```bash
# Build individual implementations
make rust
make go
make c

# Build with different profiles
cd implementations/rust && make debug && cd ../..
cd implementations/go && make debug && cd ../..
cd implementations/c && make debug && cd ../..

# Install system-wide
sudo make install

# Test installed binaries
whitespace-stego --help
./bin/whitespace-stego-rs --help
./bin/whitespace-stego-go help
./bin/whitespace-stego-c --help
```

### Library Usage Examples

```bash
# Python library usage
python3 -c "
import whitespace_stego
encoded = whitespace_stego.encode('Hello from library!', 'Carrier text', password='secret')
decoded = whitespace_stego.decode(encoded, password='secret')
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
"

# Test different backends
python3 -c "
import whitespace_stego
# Test Python backend
encoded_py = whitespace_stego.encode('Hello!', 'Carrier', backend='python')
# Test Rust backend
encoded_rs = whitespace_stego.encode('Hello!', 'Carrier', backend='rust')
# Test C backend
encoded_c = whitespace_stego.encode('Hello!', 'Carrier', backend='c')
print('All backends work!')
"
```

### Error Handling Examples

```bash
# Test with invalid inputs
whitespace-stego encode -m "" --carrier-file carrier_text.txt -o test.txt
whitespace-stego encode -m "test" --carrier-file nonexistent.txt -o test.txt
whitespace-stego decode --carrier-file nonexistent.txt -o test.txt

# Test with very long inputs
python3 -c "print('A' * 10000)" > very_long_message.txt
whitespace-stego encode -mf very_long_message.txt --carrier-file carrier_text.txt -o test.txt

# Test with special characters
whitespace-stego encode -m "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?" --carrier-file carrier_text.txt -o special.txt
whitespace-stego decode --carrier-file special.txt -o special_decoded.txt
```

### Integration Examples

```bash
# Create a shell script for batch processing
cat > batch_encode.sh << 'EOF'
#!/bin/bash
# Batch encoding script using all implementations

for i in {1..3}; do
    echo "Processing file $i..."
    echo "Secret message $i" > "message_$i.txt"
    echo "Carrier text for file $i" > "carrier_$i.txt"
    
    # Encode with all implementations
    whitespace-stego encode -mf "message_$i.txt" --carrier-file "carrier_$i.txt" -o "encoded_python_$i.txt"
    ./bin/whitespace-stego-rs encode --message-file "message_$i.txt" --carrier-file "carrier_$i.txt" --output "encoded_rust_$i.txt"
    ./bin/whitespace-stego-go encode -mf "message_$i.txt" -cf "carrier_$i.txt" -o "encoded_go_$i.txt"
    ./bin/whitespace-stego-c encode --message-file "message_$i.txt" --carrier-file "carrier_$i.txt" --output "encoded_c_$i.txt"
    
    # Decode with all implementations
    whitespace-stego decode --carrier-file "encoded_python_$i.txt" -o "decoded_python_$i.txt"
    ./bin/whitespace-stego-rs decode --carrier-file "encoded_rust_$i.txt" --output "decoded_rust_$i.txt"
    ./bin/whitespace-stego-go decode -cf "encoded_go_$i.txt" -o "decoded_go_$i.txt"
    ./bin/whitespace-stego-c decode --carrier-file "encoded_c_$i.txt" --output "decoded_c_$i.txt"
    
    # Verify all implementations
    if diff "message_$i.txt" "decoded_python_$i.txt" > /dev/null && \
       diff "message_$i.txt" "decoded_rust_$i.txt" > /dev/null && \
       diff "message_$i.txt" "decoded_go_$i.txt" > /dev/null && \
       diff "message_$i.txt" "decoded_c_$i.txt" > /dev/null; then
        echo "✅ File $i: All implementations successful"
    else
        echo "❌ File $i: Some implementations failed"
    fi
done
EOF

chmod +x batch_encode.sh
./batch_encode.sh
```

## 🧪 Testing

The project includes comprehensive test suites:

- **Unit tests**: Language-specific test suites
- **Integration tests**: Cross-implementation compatibility
- **Property-based tests**: Automated edge case discovery
- **Performance benchmarks**: Speed and memory usage tests

```bash
# Run all tests
make test

# Run specific test suites
make cov-python
make cov-rust
make cov-go
make cov-c
```

## 📊 Performance

Performance benchmarks are available in the `notebooks/` directory:

- **Speed comparison**: All implementations
- **Memory usage**: Resource consumption analysis
- **Scalability**: Performance with large files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [Documentation](docs/)
- [Examples](examples/)
- [API Reference](docs/API_REFERENCE.md)
- [Architecture](docs/ARCHITECTURE.md)

# 🕵️‍♂️ Whitespace Steganography

> *"The best place to hide a tree is in a forest. The best place to hide a secret is in plain sight."* 🌲

A modern, multi-language toolkit for hiding secret messages in text using **invisible Unicode characters**. Supports Python 🐍, Rust 🦀, C ⚡, Go 🐹, and WebAssembly 🌐 backends.

---

## 🎯 What is Whitespace Steganography?

Whitespace steganography hides secret messages in plain text using **zero-width Unicode characters** — invisible characters that don't appear to human readers but can be detected and decoded by the right tools. It's like having a conversation in a crowded room where only you and your friend know you're actually speaking in code! 🕵️‍♀️

---

## ✨ Key Features

- **🔄 Multi-language Support:** Python (with Rust/C backends), Rust, C, Go, and WebAssembly implementations
- **🖥️ Multiple Interfaces:** Command-line tools and web browser interface
- **🌍 Unicode & Emoji Friendly:** Works with any text, language, or emoji
- **🔐 Password Protection:** Optional AES-256 encryption for sensitive messages
- **🤝 Cross-compatibility:** Encode in one language, decode in another
- **🧪 Comprehensive Testing:** 1300+ tests ensuring reliability
- **📚 MISRA C Compliant:** C implementation follows safety-critical coding standards

---

## 📝 How It Works

The toolkit converts your secret message into binary data, then embeds it using invisible Unicode characters:

- **U+FEFF** (Zero-width no-break space) - Start marker
- **U+200B** (Zero-width space) - Represents binary 0
- **U+200D** (Zero-width joiner) - Represents binary 1
- **U+200C** (Zero-width non-joiner) - End marker

**Example:**
```
Original: "Hello, World!"
Carrier:  "This is innocent text."
Encoded:  "T[invisible data]his is innocent text."
```

The encoded text looks completely normal but contains your hidden message!

---

## 🥚 Easter Egg Challenge

Try decoding this innocent-looking "Hello World" message:

```bash
# Save this text to a file:
H​‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍﻿‍‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍﻿‍‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍‍﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍‍﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿﻿‍﻿‍﻿‍‍‍﻿‍﻿﻿‍﻿‍﻿﻿‍﻿‍‍‍﻿‍﻿‍‍﻿﻿﻿﻿‍﻿‌ello World

# Then decode it:
python3 -m whitespace_stego.cli decode --carrier-file your_file.txt
```

*Hint: It's a classic gaming reference! 🎮*

---

## 📚 Documentation

### Getting Started
- **[📖 Usage Guide](docs/USAGE.md)** - Complete CLI and API examples
- **[🔧 Installation Guide](docs/INSTALLATION.md)** - Setup for all platforms
- **[🐳 Docker Guide](docs/DOCKER.md)** - Containerized deployment

### Technical Details
- **[🏗️ Architecture](docs/ARCHITECTURE.md)** - System design and components
- **[📋 API Reference](docs/API_REFERENCE.md)** - Complete API documentation
- **[🔒 Security](docs/SECURITY.md)** - Security considerations
- **[🦀 Rust Implementation](docs/RUST.md)** - Rust-specific details

### Development
- **[🧪 Testing](docs/TESTING.md)** - Testing strategy and coverage
- **[📓 Notebooks](docs/NOTEBOOKS.md)** - Interactive examples
- **[🤝 Contributing](docs/CONTRIBUTING.md)** - How to contribute

### Advanced Topics
- **[📈 Coverage Analysis](docs/COVERAGE.md)** - Test coverage metrics
- **[⚡ Parallel Testing](docs/COVERAGE_PARALLELIZATION.md)** - Performance optimization
- **[🔍 Test Failure Analysis](docs/PARALLEL_TEST_FAILURE_ANALYSIS.md)** - Debugging guide

---

## 🎭 Use Cases

- **👥 Corporate Communication:** Hide sensitive notes in routine messages
- **💕 Personal Messages:** Send romantic notes that look like ordinary text
- **🎮 Gaming:** Hide cheat codes or strategies in forum posts
- **📝 Journaling:** Conceal personal thoughts in public documents
- **🔐 Secure Communication:** Add an extra layer of message protection

---

## 🔧 C Backend (High Performance)

A high-performance C backend is available for Python via ctypes, featuring MISRA C:2012 compliance for safety-critical applications.

### Building the C Backend

```bash
cd c
make shared  # Creates lib/libwhitespace_stego.so
```

### Using the C Backend

```python
from whitespace_stego.c_backend import encode, decode, is_available

if is_available():
    encoded = encode("my message", "my carrier", password="secret")
    decoded = decode(encoded, password="secret")
    print(decoded)
else:
    print("C backend not available!")
```

Use `--backend c` in the CLI to select the C backend.

---

## 🐹 Go Backend (Cross-platform)

A cross-platform Go implementation is available, providing excellent performance and easy deployment across different operating systems.

### Building the Go Backend

```bash
cd go
make build  # Creates bin/whitespace-stego-go
```

### Using the Go Backend

```bash
# Direct usage
./go/bin/whitespace-stego-go encode -m "secret message" -c "carrier text"
./go/bin/whitespace-stego-go decode -c "encoded text"

# Note: Go is a standalone CLI, not integrated with Python CLI backend system
```

The Go implementation provides:
- **🚀 Fast Performance:** Efficient string processing and memory management
- **🌍 Cross-platform:** Single binary for Linux, macOS, and Windows
- **🔧 Simple Deployment:** No external dependencies required
- **📦 Easy Distribution:** Self-contained executable

## 🔧 Backend Architecture

The project supports multiple implementation approaches:

- **Python CLI with Backends:** The Python CLI can use Python, Rust, or C backends via `--backend` option
- **Standalone CLIs:** Python (PyInstaller), Rust, C, and Go each have their own standalone CLI tools
- **WebAssembly:** Browser-based interface for web applications

All implementations are cross-compatible - you can encode in one language and decode in another.

---

## 🐍 Python Standalone CLI (PyInstaller)

A standalone Python executable is available, providing a self-contained version of the Python CLI with all backends included.

### Building the Python Standalone CLI

```bash
make python-binary  # Creates bin/whitespace-stego-py
```

### Using the Python Standalone CLI

```bash
# Direct usage (same as Python CLI but standalone)
./bin/whitespace-stego-py encode --message "secret" --carrier "text" --backend rust
./bin/whitespace-stego-py decode --carrier-file encoded.txt --backend c

# All Python CLI features available
./bin/whitespace-stego-py --help
```

The Python standalone CLI provides:
- **📦 Self-contained:** No Python installation required on target system
- **🔄 All Backends:** Includes Python, Rust, and C backends
- **🌍 Cross-platform:** Works on Linux, macOS, and Windows
- **🔧 Same Interface:** Identical to `python -m whitespace_stego.cli`

---

## ⚠️ Disclaimer

This tool is for educational and legitimate purposes only. Users are responsible for complying with applicable laws and regulations.

---

## 📄 License

MIT License. See [LICENSE](LICENSE).

---

## 🌟 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

*"In a world full of visible secrets, be the invisible one."* ✨