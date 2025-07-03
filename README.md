[![CI](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/ci.yml)
[![Build & Test](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/build-and-test.yml)
[![Docker](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/docker.yml)
[![Nightly](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml/badge.svg)](https://github.com/${{GITHUB_REPOSITORY}}/actions/workflows/nightly-binaries.yml)

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

## 🚀 Quick Start

### Installation

```bash
git clone <repo-url>
cd whitespace-stego3
make install  # Python + Rust backend
make rust     # Rust CLI
make c        # C CLI
make go       # Go CLI
make python-binary  # Python standalone CLI
make wasi-web # WebAssembly (browser UI)
```

### Basic Usage

**Python CLI:**
```bash
# Encode a secret message
python3 -m whitespace_stego.cli encode --message "Secret" --carrier "Innocent text" --output encoded.txt

# Decode the message
python3 -m whitespace_stego.cli decode --carrier-file encoded.txt
```

**Web Interface:**
```bash
make wasi-web
# Open http://localhost:8000 in your browser
```

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