# Whitespace Steganography - Rust Implementation

A high-performance, memory-safe Rust implementation of whitespace steganography for hiding messages in text using invisible Unicode characters.

## Features

- **Memory Safety**: Rust's ownership system prevents memory leaks and data races
- **High Performance**: Zero-cost abstractions and efficient memory management
- **Cross-Platform**: Single binary that works on Linux, macOS, and Windows
- **Comprehensive Testing**: Unit tests, integration tests, and property-based testing
- **Documentation**: Auto-generated documentation with examples
- **Coverage Reports**: Detailed test coverage analysis with HTML and XML output
- **Linting**: Advanced static analysis with clippy
- **Benchmarks**: Performance benchmarking capabilities

## Requirements

- Rust 1.70 or later
- Cargo (included with Rust)
- Make (optional, for using Makefile)

### Ubuntu/Debian
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
sudo apt-get install make
```

### macOS
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
brew install make
```

### Windows
- Download Rust from https://rustup.rs/
- Install Make via Chocolatey: `choco install make`

## Quick Start

### Build
```bash
make
```

### Run Tests
```bash
make test
```

### Install
```bash
make install
```

### Usage
```bash
# Encode a message
whitespace-stego-rs encode --message "Hello, World!" --carrier "This is innocent text." --output encoded.txt

# Decode a message
whitespace-stego-rs decode --carrier-file encoded.txt --output decoded.txt

# Show help
whitespace-stego-rs --help
```

## Makefile Targets

Run `make help` to see all available targets:

- `make all` - Build the binary (default)
- `make build` - Build the binary
- `make dev` - Build with development profile
- `make debug` - Build with debug profile
- `make release` - Build optimized release version
- `make install` - Install to /usr/local/bin
- `make uninstall` - Remove from /usr/local/bin
- `make test` - Run tests
- `make test-verbose` - Run tests with verbose output
- `make test-all` - Run all tests including integration
- `make coverage` - Run tests with coverage
- `make coverage-html` - Generate HTML coverage report
- `make coverage-xml` - Generate XML coverage report
- `make lint` - Run clippy linter
- `make fmt` - Format code
- `make clippy` - Run clippy with all checks
- `make bench` - Run benchmarks
- `make check` - Check code without building
- `make check-all` - Run all checks (fmt, clippy, test)
- `make doc` - Generate documentation
- `make doc-open` - Generate and open documentation
- `make clean` - Clean build artifacts
- `make distclean` - Clean all artifacts and dependencies

## Project Structure

```
rust/
├── src/
│   ├── main.rs        # CLI entry point
│   ├── lib.rs         # Library entry point
│   ├── encode.rs      # Encoding implementation
│   ├── decode.rs      # Decoding implementation
│   ├── crypto.rs      # Cryptographic functions
│   ├── constants.rs   # Constants and configuration
│   └── error.rs       # Error handling
├── tests/             # Integration tests
├── benches/           # Benchmarks
├── target/            # Build output (created)
├── coverage/          # Coverage reports (created)
├── Cargo.toml         # Rust project configuration
├── Cargo.lock         # Dependency lock file
├── Makefile           # Build system
└── README.md          # This file
```

## API Usage

### As a Library

```rust
use whitespace_stego_rust::{encode, decode};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Encode a message
    let encoded = encode("Hello, World!", "Carrier text", Some("password"))?;
    println!("Encoded: {}", encoded);

    // Decode a message
    let decoded = decode(&encoded, Some("password"))?;
    println!("Decoded: {}", decoded);

    Ok(())
}
```

### As a Binary

```bash
# Build
make

# Run
./target/release/whitespace-stego-rs --help
./target/release/whitespace-stego-rs encode -m "Secret message" -cf input.txt -o output.txt
./target/release/whitespace-stego-rs decode -cf output.txt -o decoded.txt
```

## Testing

### Run All Tests
```bash
make test
```

### Verbose Tests
```bash
make test-verbose
```

### All Test Types
```bash
make test-all
```

### Coverage Analysis
```bash
make coverage-html
# Open coverage/tarpaulin-report.html in your browser
```

### XML Coverage Report
```bash
make coverage-xml
# Generates coverage/tarpaulin.xml for CI/CD integration
```

### Benchmarks
```bash
make bench
```

## Development

### Development Build
```bash
make dev
```

### Debug Build
```bash
make debug
```

### Release Build
```bash
make release
```

### Code Quality
```bash
make fmt      # Format code
make clippy   # Run clippy linter
make lint     # Run basic linting
```

### All Checks
```bash
make check-all
```

## Installation

### System-wide Installation
```bash
make install
```

### Uninstall
```bash
make uninstall
```

## Dependencies

This implementation uses Rust's ecosystem:

- **Standard Library**: Core Rust functionality
- **External Crates**: See `Cargo.toml` for dependencies
- **Optional Tools**: 
  - `cargo-tarpaulin` for coverage (install with `cargo install cargo-tarpaulin`)
  - `cargo-audit` for security audits (install with `cargo install cargo-audit`)
  - `cross` for cross-compilation (install with `cargo install cross`)

## Building from Source

1. Clone the repository
2. Navigate to the Rust directory: `cd rust`
3. Ensure Rust 1.70+ is installed: `rustc --version`
4. Build: `make`
5. Test: `make test`
6. Install: `make install`

## Cross-Platform Building

### Native Cross-Compilation
```bash
make build-linux    # Build for Linux
make build-macos    # Build for macOS
make build-windows  # Build for Windows
```

### Using Cross (Docker-based)
```bash
# Install cross
cargo install cross

# Cross-compile
make cross-linux
make cross-macos
make cross-windows
```

## Documentation

### Generate Documentation
```bash
make doc
```

### View Documentation
```bash
make doc-open
```

## Performance

The Rust implementation is optimized for:
- **Memory Safety**: Zero-cost abstractions with compile-time guarantees
- **CPU Performance**: Efficient algorithms and data structures
- **Concurrency**: Safe concurrent access with Rust's ownership system
- **Binary Size**: Optimized release builds with minimal dependencies

## Security

### Dependency Auditing
```bash
make audit
```

### Update Dependencies
```bash
make update
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Check code quality: `make check-all`
7. Check coverage: `make coverage-html`
8. Submit a pull request

## License

This project is licensed under the same license as the main whitespace-stego project.

## Support

For issues and questions:
- Check the main project documentation
- Review the test files for usage examples
- Run `make help` for available commands
- Check Rust version compatibility: `make check-rust`
- Generate documentation: `make doc` 