# Whitespace Steganography - C Implementation

A high-performance C implementation of whitespace steganography for hiding messages in text using invisible Unicode characters.

## Features

- **High Performance**: Optimized C implementation for speed and efficiency
- **Cross-Platform**: Works on Linux, macOS, and Windows
- **Comprehensive Testing**: Multiple test frameworks (Unity, custom tests, coverage)
- **Shared Library**: Can be used as a library in other applications
- **Memory Safe**: Proper memory management and error handling
- **Coverage Reports**: Detailed test coverage analysis

## Requirements

- GCC or Clang compiler
- OpenSSL development libraries
- Make
- CMake (optional, for CMake builds)
- lcov and gcov (for coverage reports)

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev make cmake lcov
```

### macOS
```bash
brew install openssl make cmake lcov
```

### Windows
- Install MinGW-w64 or Visual Studio
- Install OpenSSL development libraries
- Install Make (via Chocolatey: `choco install make`)

## Quick Start

### Build
```bash
make
```

### Run Tests
```bash
make test-all
```

### Install
```bash
make install
```

### Usage
```bash
# Encode a message
whitespace-stego-c encode --message "Hello, World!" --carrier "This is innocent text." --output encoded.txt

# Decode a message
whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt
```

## Makefile Targets

Run `make help` to see all available targets:

- `make all` - Build binary and shared library (default)
- `make build` - Build binary only
- `make shared` - Build shared library only
- `make install` - Install to /usr/local/bin
- `make uninstall` - Remove from /usr/local/bin
- `make test` - Run basic tests
- `make test-c` - Run C implementation tests
- `make test-unity` - Run Unity framework tests
- `make test-coverage` - Run coverage tests
- `make test-all` - Run all tests
- `make coverage-report` - Generate HTML coverage report
- `make dev` - Build with debug flags
- `make debug` - Build with debug flags and symbols
- `make release` - Build optimized release version
- `make clean` - Remove all build artifacts
- `make distclean` - Remove all build artifacts and dependencies

## Project Structure

```
c/
├── include/           # Header files
│   ├── crypto.h      # Cryptographic functions
│   ├── utils.h       # Utility functions
│   └── whitespace_stego.h  # Main API
├── src/              # Source files
│   ├── crypto.c      # Cryptographic implementation
│   ├── utils.c       # Utility implementation
│   ├── whitespace_stego.c  # Main implementation
│   └── main.c        # CLI entry point
├── test/             # Test files
│   ├── test-c.c      # Custom test suite
│   ├── test_unity.c  # Unity framework tests
│   ├── test_gcov.c   # Coverage tests
│   └── run_tests.sh  # Test runner script
├── bin/              # Build output (created)
├── obj/              # Object files (created)
├── lib/              # Shared library (created)
├── coverage/         # Coverage reports (created)
├── Makefile          # Build system
└── README.md         # This file
```

## API Usage

### As a Library

```c
#include "whitespace_stego.h"

// Encode a message
char* encoded = encode_message("Hello, World!", "Carrier text", "password");
printf("Encoded: %s\n", encoded);
free(encoded);

// Decode a message
char* decoded = decode_message("Encoded text", "password");
printf("Decoded: %s\n", decoded);
free(decoded);
```

### As a Shared Library

```bash
# Build shared library
make shared

# Use in your application
gcc -L./lib -lwhitespace_stego your_app.c -o your_app
```

## Testing

### Run All Tests
```bash
make test-all
```

### Individual Test Suites
```bash
make test          # Basic functionality tests
make test-c        # C implementation tests
make test-unity    # Unity framework tests
make test-coverage # Coverage tests
```

### Coverage Analysis
```bash
make coverage-report
# Open coverage/html/index.html in your browser
```

### CMake Tests
```bash
make cmake-build
make cmake-test
```

## Development

### Debug Build
```bash
make debug
```

### Release Build
```bash
make release
```

### Development Build
```bash
make dev
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

- **OpenSSL**: For cryptographic functions (AES encryption, SHA-256 hashing)
- **Unity**: For unit testing (automatically downloaded)
- **gcov/lcov**: For coverage analysis

## Building from Source

1. Clone the repository
2. Navigate to the C directory: `cd c`
3. Install dependencies (see Requirements section)
4. Build: `make`
5. Test: `make test-all`
6. Install: `make install`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test-all`
6. Check coverage: `make coverage-report`
7. Submit a pull request

## License

This project is licensed under the same license as the main whitespace-stego project.

## Support

For issues and questions:
- Check the main project documentation
- Review the test files for usage examples
- Run `make help` for available commands 