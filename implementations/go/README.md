# Whitespace Steganography - Go Implementation

A high-performance Go implementation of whitespace steganography for hiding messages in text using invisible Unicode characters.

## Features

- **High Performance**: Optimized Go implementation with efficient memory usage
- **Cross-Platform**: Single binary that works on Linux, macOS, and Windows
- **Comprehensive Testing**: Unit tests, race detection, and coverage analysis
- **Memory Safe**: Go's built-in memory safety and garbage collection
- **Easy Deployment**: Single static binary with no external dependencies
- **Coverage Reports**: Detailed test coverage analysis with HTML and XML output

## Requirements

- Go 1.21 or later
- Make (optional, for using Makefile)

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install golang-go make
```

### macOS
```bash
brew install go make
```

### Windows
- Download Go from https://golang.org/dl/
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
whitespace-stego-go encode -m "Hello, World!" -cf carrier.txt -o encoded.txt

# Decode a message
whitespace-stego-go decode -cf encoded.txt -o decoded.txt

# Show help
whitespace-stego-go help
```

## Makefile Targets

Run `make help` to see all available targets:

- `make all` - Build the binary (default)
- `make build` - Build the binary
- `make dev` - Build with development flags
- `make debug` - Build with debug flags
- `make release` - Build optimized release version
- `make install` - Install to /usr/local/bin
- `make uninstall` - Remove from /usr/local/bin
- `make test` - Run tests
- `make test-verbose` - Run tests with verbose output
- `make test-race` - Run tests with race detection
- `make coverage` - Run tests with coverage
- `make coverage-html` - Generate HTML coverage report
- `make coverage-xml` - Generate XML coverage report
- `make lint` - Run linter
- `make fmt` - Format code
- `make vet` - Run go vet
- `make bench` - Run benchmarks
- `make clean` - Clean build artifacts
- `make distclean` - Clean all artifacts and dependencies

## Project Structure

```
go/
├── src/
│   ├── main.go        # CLI entry point
│   └── stego/         # Core implementation
│       ├── constants.go  # Constants and configuration
│       ├── core.go       # Main steganography logic
│       └── crypto.go     # Cryptographic functions
├── bin/               # Build output (created)
├── go.mod             # Go module definition
├── go.sum             # Go module checksums
├── Makefile           # Build system
└── README.md          # This file
```

## API Usage

### As a Library

```go
package main

import (
    "fmt"
    "log"
    "./src/stego"
)

func main() {
    // Encode a message
    encoded, err := stego.Encode("Hello, World!", "Carrier text", "password")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Encoded: %s\n", encoded)

    // Decode a message
    decoded, err := stego.Decode(encoded, "password")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Decoded: %s\n", decoded)
}
```

### As a Binary

```bash
# Build
make

# Run
./bin/whitespace-stego-go help
./bin/whitespace-stego-go encode -m "Secret message" -cf input.txt -o output.txt
./bin/whitespace-stego-go decode -cf output.txt -o decoded.txt
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

### Race Detection
```bash
make test-race
```

### Coverage Analysis
```bash
make coverage-html
# Open coverage.html in your browser
```

### XML Coverage Report
```bash
make coverage-xml
# Generates coverage.xml for CI/CD integration
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
make fmt    # Format code
make vet    # Run go vet
make lint   # Run linter (if available)
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

This implementation has minimal external dependencies:

- **Standard Library**: Uses only Go standard library packages
- **Optional Tools**: 
  - `golint` for linting (install with `go install golang.org/x/lint/golint@latest`)
  - `gocover-cobertura` for XML coverage (install with `go install github.com/t-yuki/gocover-cobertura@latest`)

## Building from Source

1. Clone the repository
2. Navigate to the Go directory: `cd go`
3. Ensure Go 1.21+ is installed: `go version`
4. Build: `make`
5. Test: `make test`
6. Install: `make install`

## Cross-Platform Building

```bash
# Build for multiple platforms
GOOS=linux GOARCH=amd64 make build
GOOS=darwin GOARCH=amd64 make build
GOOS=windows GOARCH=amd64 make build
```

## Performance

The Go implementation is optimized for:
- **Memory Efficiency**: Minimal memory allocations
- **CPU Performance**: Efficient algorithms and data structures
- **Concurrency**: Safe for concurrent use
- **Binary Size**: Small, statically linked binaries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Check coverage: `make coverage-html`
7. Format code: `make fmt`
8. Submit a pull request

## License

This project is licensed under the same license as the main whitespace-stego project.

## Support

For issues and questions:
- Check the main project documentation
- Review the test files for usage examples
- Run `make help` for available commands
- Check Go version compatibility: `make check-go` 