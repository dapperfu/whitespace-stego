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

## Extensive Examples

### Complete Setup and Build Example

```bash
# Navigate to the Rust implementation directory
cd implementations/rust

# Verify Rust installation
rustc --version
cargo --version

# Build the implementation
cargo clean
cargo build --release

# Verify the binary was created
ls -la target/release/whitespace-stego-rs
```

### Basic Encoding and Decoding Examples

```bash
# Create test files
echo "This is a secret message that needs to be hidden." > secret_message.txt
echo "This is innocent text that will serve as a carrier for the hidden message. It contains normal content that nobody would suspect contains hidden information." > carrier_text.txt

# Encode a message using command line arguments
./target/release/whitespace-stego-rs encode --message "Hello, World!" --carrier "This is innocent text." --output encoded.txt

# Encode a message using input files
./target/release/whitespace-stego-rs encode --message-file secret_message.txt --carrier-file carrier_text.txt --output encoded_with_files.txt

# Decode the message
./target/release/whitespace-stego-rs decode --carrier-file encoded.txt --output decoded.txt

# View the results
echo "Original message:"
cat secret_message.txt
echo -e "\nEncoded carrier:"
cat encoded.txt
echo -e "\nDecoded message:"
cat decoded.txt
```

### Advanced Usage Examples

```bash
# Encode with password protection
./target/release/whitespace-stego-rs encode --message "Top secret information" --carrier "Public document content" --password "mysecretpass" --output protected.txt

# Decode with password
./target/release/whitespace-stego-rs decode --carrier-file protected.txt --password "mysecretpass" --output decrypted.txt

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

./target/release/whitespace-stego-rs encode --message-file long_message.txt --carrier-file long_carrier.txt --output long_encoded.txt
./target/release/whitespace-stego-rs decode --carrier-file long_encoded.txt --output long_decoded.txt

# Verify the encoding worked
diff long_message.txt long_decoded.txt && echo "✅ Encoding/decoding successful!"
```

### Testing Examples

```bash
# Run all tests
cargo test

# Run tests with verbose output
cargo test --verbose

# Run specific test modules
cargo test encode
cargo test decode
cargo test crypto

# Run integration tests
cargo test --test integration_tests

# Run property-based tests
cargo test --test test_core_prop

# Run benchmarks
cargo bench

# Run tests with coverage (requires cargo-tarpaulin)
cargo install cargo-tarpaulin
cargo tarpaulin --out Html --output-dir coverage
cargo tarpaulin --out Xml --output-dir coverage

# View coverage report
firefox coverage/tarpaulin-report.html  # or your preferred browser
```

### Development Examples

```bash
# Build with different profiles
cargo build --profile dev      # Development profile
cargo build                    # Debug profile
cargo build --release          # Release profile

# Install system-wide
sudo make install

# Test the installed binary
whitespace-stego-rs --help
whitespace-stego-rs encode --help
whitespace-stego-rs decode --help

# Uninstall
sudo make uninstall
```

### Library Usage Examples

```bash
# Create a simple test program
cat > test_lib.rs << 'EOF'
use whitespace_stego_rust::{encode, decode};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Encode a message
    let encoded = encode("Hello from library!", "Carrier text", None)?;
    println!("Encoded: {}", encoded);

    // Decode the message
    let decoded = decode(&encoded, None)?;
    println!("Decoded: {}", decoded);

    Ok(())
}
EOF

# Add dependency to Cargo.toml
echo 'whitespace-stego-rust = { path = "." }' >> Cargo.toml

# Run the test program
cargo run --bin test_lib
```

### Performance Testing Examples

```bash
# Test encoding performance with large files
dd if=/dev/urandom bs=1M count=10 | tr -dc 'a-zA-Z0-9 ' > large_carrier.txt
echo "Secret message" > test_message.txt

# Time the encoding process
time ./target/release/whitespace-stego-rs encode --message-file test_message.txt --carrier-file large_carrier.txt --output large_encoded.txt

# Time the decoding process
time ./target/release/whitespace-stego-rs decode --carrier-file large_encoded.txt --output large_decoded.txt

# Verify correctness
diff test_message.txt large_decoded.txt && echo "✅ Large file test passed!"

# Run performance benchmarks
cargo bench --bench performance
```

### Cross-Platform Building Examples

```bash
# Build for current platform
cargo build --release

# Build for multiple platforms
cargo build --release --target x86_64-unknown-linux-gnu
cargo build --release --target x86_64-apple-darwin
cargo build --release --target x86_64-pc-windows-gnu

# Build for ARM architectures
cargo build --release --target aarch64-unknown-linux-gnu
cargo build --release --target aarch64-apple-darwin

# Using cross for Docker-based cross-compilation
cargo install cross
cross build --release --target x86_64-unknown-linux-gnu
cross build --release --target x86_64-apple-darwin
cross build --release --target x86_64-pc-windows-gnu
```

### Code Quality Examples

```bash
# Format code
cargo fmt

# Run clippy linter
cargo clippy

# Run clippy with all checks
cargo clippy -- -D warnings

# Run all code quality checks
cargo fmt -- --check
cargo clippy -- -D warnings
cargo test
```

### Documentation Examples

```bash
# Generate documentation
cargo doc --no-deps

# Generate and open documentation
cargo doc --no-deps --open

# Generate documentation for all dependencies
cargo doc --open

# Check documentation
cargo doc --no-deps --document-private-items
```

### Error Handling Examples

```bash
# Test with invalid inputs
./target/release/whitespace-stego-rs encode --message "" --carrier "test" --output test.txt
./target/release/whitespace-stego-rs encode --message "test" --carrier "" --output test.txt
./target/release/whitespace-stego-rs decode --carrier-file nonexistent.txt --output test.txt

# Test with very long inputs
python3 -c "print('A' * 10000)" > very_long_message.txt
./target/release/whitespace-stego-rs encode --message-file very_long_message.txt --carrier "test" --output test.txt

# Test with special characters
./target/release/whitespace-stego-rs encode --message "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?" --carrier "test" --output special.txt
./target/release/whitespace-stego-rs decode --carrier-file special.txt --output special_decoded.txt
```

### Integration Examples

```bash
# Create a shell script for batch processing
cat > batch_encode.sh << 'EOF'
#!/bin/bash
# Batch encoding script

for i in {1..5}; do
    echo "Processing file $i..."
    echo "Secret message $i" > "message_$i.txt"
    echo "Carrier text for file $i" > "carrier_$i.txt"
    
    ./target/release/whitespace-stego-rs encode \
        --message-file "message_$i.txt" \
        --carrier-file "carrier_$i.txt" \
        --output "encoded_$i.txt"
    
    ./target/release/whitespace-stego-rs decode \
        --carrier-file "encoded_$i.txt" \
        --output "decoded_$i.txt"
    
    # Verify
    if diff "message_$i.txt" "decoded_$i.txt" > /dev/null; then
        echo "✅ File $i: Success"
    else
        echo "❌ File $i: Failed"
    fi
done
EOF

chmod +x batch_encode.sh
./batch_encode.sh
```

### Web Integration Examples

```bash
# Create a simple web server using actix-web
cat > web_server/Cargo.toml << 'EOF'
[package]
name = "whitespace-stego-web"
version = "0.1.0"
edition = "2021"

[dependencies]
actix-web = "4.0"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
whitespace-stego-rust = { path = ".." }
EOF

cat > web_server/src/main.rs << 'EOF'
use actix_web::{web, App, HttpServer, Result};
use serde::{Deserialize, Serialize};
use whitespace_stego_rust::{encode, decode};

#[derive(Deserialize)]
struct EncodeRequest {
    message: String,
    carrier: String,
    password: Option<String>,
}

#[derive(Serialize)]
struct EncodeResponse {
    encoded: String,
    error: Option<String>,
}

async fn encode_handler(req: web::Json<EncodeRequest>) -> Result<web::Json<EncodeResponse>> {
    match encode(&req.message, &req.carrier, req.password.as_deref()) {
        Ok(encoded) => Ok(web::Json(EncodeResponse {
            encoded,
            error: None,
        })),
        Err(e) => Ok(web::Json(EncodeResponse {
            encoded: String::new(),
            error: Some(e.to_string()),
        })),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Server starting on :8080");
    HttpServer::new(|| {
        App::new()
            .service(web::resource("/encode").route(web::post().to(encode_handler)))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
EOF

# Build and run the web server
cd web_server
cargo build --release
./target/release/whitespace-stego-web &

# Test the web server
curl -X POST http://localhost:8080/encode \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello from web!","carrier":"Innocent text","password":null}'

# Stop the server
pkill -f whitespace-stego-web
cd ..
```

### Docker Integration Examples

```bash
# Create a Dockerfile
cat > Dockerfile << 'EOF'
FROM rust:1.70 as builder

WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:bullseye-slim
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /root/
COPY --from=builder /app/target/release/whitespace-stego-rs .
CMD ["./whitespace-stego-rs"]
EOF

# Build Docker image
docker build -t whitespace-stego-rs .

# Run in Docker
docker run --rm whitespace-stego-rs --help
docker run --rm -v $(pwd):/data whitespace-stego-rs encode --message "Hello from Docker!" --carrier-file /data/carrier_text.txt --output /data/docker_encoded.txt
```

### Security Examples

```bash
# Audit dependencies for security vulnerabilities
cargo audit

# Update dependencies
cargo update

# Check for outdated dependencies
cargo outdated

# Run security-focused tests
cargo test --features security
```

### CI/CD Integration Examples

```bash
# Run all checks for CI
cargo fmt -- --check
cargo clippy -- -D warnings
cargo test
cargo build --release

# Generate coverage for CI
cargo install cargo-tarpaulin
cargo tarpaulin --out Xml --output-dir coverage
cargo tarpaulin --out Html --output-dir coverage

# Run benchmarks for performance regression testing
cargo bench --bench performance
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