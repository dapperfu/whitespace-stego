# Whitespace Steganography

This project implements a whitespace steganography tool that encodes messages using zero-width Unicode whitespace characters. It supports both Python and Rust implementations, with a CLI interface for each.

## Installation

### Python

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

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

### Rust

1. Ensure you have Rust and Cargo installed. If not, install them from [rustup.rs](https://rustup.rs/).

2. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd whitespace-stego3
   ```

3. Build the Rust project:
   ```bash
   cargo build --release
   ```

## Compilation

### Python

No additional compilation is required for the Python implementation. Simply install the package as described in the installation section.

### Rust

To compile the Rust implementation, run:
```bash
cargo build --release
```

The compiled binary will be available at `target/release/whitespace_stego`.

## Usage

### Python CLI

Encode a message:
```bash
whitespace-stego encode --message "Hello, World!" --carrier "This is a carrier text."
```

Decode a message:
```bash
whitespace-stego decode --carrier "This is a carrier text with an encoded message."
```

### Rust CLI

Encode a message:
```bash
./target/release/whitespace_stego encode --message "Hello, World!" --carrier "This is a carrier text."
```

Decode a message:
```bash
./target/release/whitespace_stego decode --carrier "This is a carrier text with an encoded message."
```

## Features

- Unicode support
- Password protection
- Command-line interface for both Python and Rust
- Comprehensive test suite

## License

This project is licensed under the MIT License - see the LICENSE file for details. 