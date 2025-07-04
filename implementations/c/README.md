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
- ccache (optional, for faster builds)

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install build-essential libssl-dev make cmake lcov ccache
```

### macOS
```bash
brew install openssl make cmake lcov ccache
```

### Windows
- Install MinGW-w64 or Visual Studio
- Install OpenSSL development libraries
- Install Make (via Chocolatey: `choco install make`)
- Install ccache (optional, for faster builds)

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

## Build Acceleration with ccache

The C implementation includes automatic ccache integration for significantly faster builds. ccache caches compiled object files, so subsequent builds are much faster when source files haven't changed.

### Setup ccache
```bash
# Install ccache (if not already installed)
sudo apt-get install ccache  # Ubuntu/Debian
brew install ccache          # macOS

# Setup ccache for the project
make ccache-setup
```

### Using ccache
```bash
# First build (normal speed)
make clean
make all

# Subsequent builds (much faster due to caching)
make all

# Check ccache statistics
make ccache-stats

# Show ccache configuration
make ccache-show

# Clean ccache if needed
make ccache-clean
```

### ccache Configuration
The Makefile automatically configures ccache with:
- **Cache directory**: `.ccache` (local to project)
- **Max cache size**: 1GB
- **Compression**: Enabled
- **Automatic detection**: Falls back to regular compiler if ccache not available

## Makefile Targets

Run `make help` to see all available targets:

### Build Acceleration
- `make ccache-setup` - Setup ccache for faster builds
- `make ccache-stats` - Show ccache statistics
- `make ccache-clean` - Clean ccache
- `make ccache-show` - Show ccache configuration

### Build Targets
- `make all` - Build binary and shared library (default)
- `make build` - Build binary only
- `make shared` - Build shared library only
- `make dev` - Build with debug flags
- `make debug` - Build with debug flags and symbols
- `make release` - Build optimized release version

### Installation
- `make install` - Install to /usr/local/bin
- `make uninstall` - Remove from /usr/local/bin

### Testing
- `make test` - Run basic tests
- `make test-c` - Run C implementation tests
- `make test-unity` - Run Unity framework tests
- `make test-coverage` - Run coverage tests
- `make test-all` - Run all tests
- `make coverage-report` - Generate HTML coverage report

### Maintenance
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

## Extensive Examples

### Complete Setup and Build Example

```bash
# Clone and navigate to the C implementation directory
cd implementations/c

# Install dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install build-essential libssl-dev make cmake lcov ccache

# Setup ccache for faster builds
make ccache-setup

# Build the implementation
make clean
make all

# Verify the binary was created
ls -la bin/whitespace-stego-c

# Check ccache statistics
make ccache-stats
```

### Basic Encoding and Decoding Examples

```bash
# Create test files
echo "This is a secret message that needs to be hidden." > secret_message.txt
echo "This is innocent text that will serve as a carrier for the hidden message. It contains normal content that nobody would suspect contains hidden information." > carrier_text.txt

# Encode a message using command line arguments
./bin/whitespace-stego-c encode --message "Hello, World!" --carrier "This is innocent text." --output encoded.txt

# Encode a message using input files
./bin/whitespace-stego-c encode --message-file secret_message.txt --carrier-file carrier_text.txt --output encoded_with_files.txt

# Decode the message
./bin/whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt

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
./bin/whitespace-stego-c encode --message "Top secret information" --carrier "Public document content" --password "mysecretpass" --output protected.txt

# Decode with password
./bin/whitespace-stego-c decode --carrier-file protected.txt --password "mysecretpass" --output decrypted.txt

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

./bin/whitespace-stego-c encode --message-file long_message.txt --carrier-file long_carrier.txt --output long_encoded.txt
./bin/whitespace-stego-c decode --carrier-file long_encoded.txt --output long_decoded.txt

# Verify the encoding worked
diff long_message.txt long_decoded.txt && echo "✅ Encoding/decoding successful!"
```

### Testing Examples

```bash
# Run all tests
make test-all

# Run specific test suites
make test          # Basic functionality tests
make test-c        # C implementation tests
make test-unity    # Unity framework tests
make test-coverage # Coverage tests

# Generate and view coverage report
make coverage-report
# Open coverage/html/index.html in your browser
firefox coverage/html/index.html  # or your preferred browser

# Run CMake tests
make cmake-build
make cmake-test
```

### Build Acceleration Examples

```bash
# Setup ccache for faster builds
make ccache-setup

# First build (normal speed)
make clean
time make all

# Subsequent builds (much faster due to caching)
time make all

# Check ccache effectiveness
make ccache-stats

# Show ccache configuration
make ccache-show

# Test different build profiles with ccache
make clean && time make debug
make clean && time make release
make clean && time make dev

# Clean ccache if needed
make ccache-clean
```

### Development Examples

```bash
# Build with different profiles
make debug         # Debug build with symbols
make release       # Optimized release build
make dev           # Development build

# Install system-wide
sudo make install

# Test the installed binary
whitespace-stego-c --help
whitespace-stego-c encode --help
whitespace-stego-c decode --help

# Uninstall
sudo make uninstall
```

### Library Usage Examples

```bash
# Build shared library
make shared

# Create a simple test program
cat > test_lib.c << 'EOF'
#include <stdio.h>
#include <stdlib.h>
#include "include/whitespace_stego.h"

int main() {
    // Encode a message
    char* encoded = encode_message("Hello from library!", "Carrier text", NULL);
    if (encoded) {
        printf("Encoded: %s\n", encoded);
        
        // Decode the message
        char* decoded = decode_message(encoded, NULL);
        if (decoded) {
            printf("Decoded: %s\n", decoded);
            free(decoded);
        }
        free(encoded);
    }
    return 0;
}
EOF

# Compile and link with the library
gcc -I./include -L./lib -lwhitespace_stego test_lib.c -o test_lib

# Run the test program
./test_lib
```

### Performance Testing Examples

```bash
# Test encoding performance with large files
dd if=/dev/urandom bs=1M count=10 | tr -dc 'a-zA-Z0-9 ' > large_carrier.txt
echo "Secret message" > test_message.txt

# Time the encoding process
time ./bin/whitespace-stego-c encode --message-file test_message.txt --carrier-file large_carrier.txt --output large_encoded.txt

# Time the decoding process
time ./bin/whitespace-stego-c decode --carrier-file large_encoded.txt --output large_decoded.txt

# Verify correctness
diff test_message.txt large_decoded.txt && echo "✅ Large file test passed!"
```

### Cross-Platform Examples

```bash
# On macOS
brew install openssl make cmake lcov
make clean && make all

# On Windows (using MinGW)
# First install MinGW and OpenSSL, then:
mingw32-make clean
mingw32-make all

# On Linux with different compilers
# Using Clang
CC=clang make clean && make all

# Using GCC with specific flags
CFLAGS="-O3 -march=native" make clean && make all
```

### Error Handling Examples

```bash
# Test with invalid inputs
./bin/whitespace-stego-c encode --message "" --carrier "test" --output test.txt
./bin/whitespace-stego-c encode --message "test" --carrier "" --output test.txt
./bin/whitespace-stego-c decode --carrier-file nonexistent.txt --output test.txt

# Test with very long inputs
python3 -c "print('A' * 10000)" > very_long_message.txt
./bin/whitespace-stego-c encode --message-file very_long_message.txt --carrier "test" --output test.txt
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
    
    ./bin/whitespace-stego-c encode \
        --message-file "message_$i.txt" \
        --carrier-file "carrier_$i.txt" \
        --output "encoded_$i.txt"
    
    ./bin/whitespace-stego-c decode \
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