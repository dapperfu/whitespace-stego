# whitespace-stego-python

Python bindings for whitespace steganography using zero-width Unicode characters, powered by a high-performance Rust backend.

## Features
- Encode and decode messages using invisible Unicode whitespace
- Optional password-based encryption (Fernet, compatible with Python)
- Fast, safe, and cross-platform (Rust core)
- Easy to use from Python

## Installation

```sh
pip install maturin
maturin develop  # or maturin build && pip install target/wheels/...
```

## Usage

```python
import whitespace_stego_python as ws

encoded = ws.encode("Secret", "Carrier text", password="mypassword")
decoded = ws.decode(encoded, password="mypassword")
print(decoded)
```

## CLI Integration

This package can be used as a backend for the whitespace-stego CLI with the `--backend rust` flag. 