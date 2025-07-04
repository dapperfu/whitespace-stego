# Implementations

This directory contains all language-specific implementations of the whitespace steganography algorithm.

## Structure

- **python/** - Python implementation with multiple backends (Python, Rust, C)
- **rust/** - Standalone Rust CLI implementation
- **go/** - Standalone Go CLI implementation  
- **c/** - Standalone C CLI implementation

## Python Implementation

The Python implementation is the most feature-rich, providing:
- Multiple backends (Python, Rust, C)
- CLI interface via `whitespace-stego` command
- Library usage via `whitespace_stego` module
- Unicode support and password protection

## Standalone Implementations

Each standalone implementation provides:
- Single executable binary
- Consistent CLI interface
- Cross-platform compatibility
- Optimized performance for their respective language

## Building

Use the top-level Makefile to build all implementations:

```bash
make all          # Build all binaries
make rust         # Build Rust binary only
make go           # Build Go binary only
make c            # Build C binary only
``` 