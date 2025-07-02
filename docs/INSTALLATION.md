# Installation Guide

This guide covers installation of the whitespace steganography toolkit across different platforms and use cases.

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Rust**: Latest stable version (for Rust backend and CLI)
- **C Compiler**: GCC/Clang (for C implementation)
- **Node.js**: 18+ (for WASM development, optional)
- **Docker**: (for portable binary builds, optional)

### Platform-Specific Requirements

#### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y build-essential python3-dev git curl

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# Install Python dependencies
python3 -m pip install --upgrade pip
```

#### macOS
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 rust git

# Install Python dependencies
python3 -m pip install --upgrade pip
```

#### Windows
```bash
# Install Rust
# Download and run rustup-init.exe from https://rustup.rs/

# Install Python from https://python.org/

# Install Visual Studio Build Tools for C compilation
# Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

## Installation Methods

### 1. Full Development Setup (Recommended)

Clone the repository and set up the complete development environment:

```bash
git clone <repository-url>
cd whitespace-stego3

# Create virtual environment and install everything
make install

# Build all implementations
make rust     # Rust CLI
make c        # C CLI  
make wasi-web # WebAssembly UI
```

This installs:
- Python package with Rust backend
- Development dependencies
- All CLI implementations
- WebAssembly interface

### 2. Python-Only Installation

For users who only need the Python implementation:

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python package
pip install -e .

# Install Rust backend (optional, for performance)
cd whitespace-stego-backend
maturin develop --release
cd ..
```

### 3. Rust-Only Installation

For users who prefer the Rust implementation:

```bash
# Build Rust CLI
cargo build --release --manifest-path rust/Cargo.toml

# Copy to convenient location
cp rust/target/release/whitespace-stego-rs ~/.local/bin/
```

### 4. Docker Installation

For portable, isolated builds:

```bash
# Build portable Python binary
make python-binary-docker

# The binary is now available at dist/whitespace-stego-py
# This binary works on most Linux distributions
```

### 5. WebAssembly Installation

For browser-based usage:

```bash
# Build WASM interface
make wasi-web

# Serve locally
cd wasi/pkg && python3 -m http.server 8000
# Open http://localhost:8000 in your browser
```

## Verification

After installation, verify everything works:

```bash
# Test Python CLI
python3 -m whitespace_stego.cli --help

# Test Rust CLI
./whitespace-stego-rs --help

# Test C CLI
./whitespace-stego-c --help

# Test WebAssembly (if built)
# Open http://localhost:8000 and try encoding/decoding
```

## Troubleshooting

### Common Issues

#### Rust Installation Problems
```bash
# Update Rust
rustup update

# Check Rust version
rustc --version
cargo --version
```

#### Python Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf .venv
make venv
make install
```

#### C Compilation Issues
```bash
# On Ubuntu/Debian
sudo apt-get install build-essential

# On macOS
xcode-select --install

# On Windows
# Ensure Visual Studio Build Tools are installed
```

#### WASM Build Issues
```bash
# Install wasm-pack
cargo install wasm-pack

# Clean and rebuild
cd wasi
rm -rf pkg/ target/
./build.sh
```

### Platform-Specific Issues

#### Windows
- Ensure PATH includes Python and Rust binaries
- Use PowerShell or Git Bash for better compatibility
- Install Visual Studio Build Tools for C compilation

#### macOS
- Use Homebrew for dependency management
- Ensure Xcode Command Line Tools are installed
- Use `python3` instead of `python`

#### Linux
- Use system package manager for dependencies
- Ensure user has write permissions to installation directories
- Consider using `pyenv` for Python version management

## Development Dependencies

For contributors, additional dependencies are needed:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install additional tools
pip install ruff mypy black

# For testing
pip install pytest pytest-cov pytest-xdist selenium
```

## Environment Variables

Optional environment variables for customization:

```bash
# Python virtual environment location
export VENV=.venv

# Rust target directory
export CARGO_TARGET_DIR=target

# Test configuration
export PYTEST_ADDOPTS="-v --tb=short"
```

## Next Steps

After installation:
1. Read the [Usage Guide](USAGE.md) for examples
2. Check [Testing Guide](TESTING.md) to run tests
3. Explore [Jupyter Notebooks](NOTEBOOKS.md) for interactive examples
4. Review [Security Notes](SECURITY.md) for best practices

For development:
1. Read [Contributing Guide](CONTRIBUTING.md)
2. Check [Rust Implementation Details](RUST.md)
3. Review [Testing Strategy](TESTING.md) 