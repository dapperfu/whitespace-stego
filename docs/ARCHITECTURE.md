# System Architecture

This document describes the architecture of the whitespace steganography toolkit, including component relationships, data flow, and design decisions.

## Overview

The whitespace steganography toolkit is designed as a multi-language, multi-backend system that provides consistent steganography capabilities across different platforms and use cases.

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interfaces                          │
├─────────────────────────────────────────────────────────────┤
│  CLI (Python)  │  CLI (Rust)  │  CLI (C)  │  CLI (Go)      │
│  Web (WASM)    │  Jupyter     │  API      │  Docker        │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Core Libraries                           │
├─────────────────────────────────────────────────────────────┤
│  Python Core   │  Rust Core   │  C Core    │  Go Core       │
│  (whitespace_  │  (whitespace-│  (whitespace│  (whitespace-  │
│   stego)       │  -stego-core)│  _stego.c)  │  stego-go)     │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Backend Services                         │
├─────────────────────────────────────────────────────────────┤
│  Python Backend│  Rust Backend│  C Backend  │  WASM Backend │
│  (Pure Python) │  (PyO3)      │  (ctypes)   │  (WebAssembly)│
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Core Libraries

Each language implementation provides the same core functionality:

#### Python Core (`whitespace_stego/`)
- **Location**: `whitespace_stego/core.py`
- **Purpose**: Pure Python implementation of steganography algorithms
- **Features**: 
  - Zero-width Unicode character encoding/decoding
  - Base64 encoding/decoding
  - Fernet encryption/decryption
  - UTF-8 text handling
  - Multiple message support
  - Message counting and extraction

#### Rust Core (`whitespace-stego-core/`)
- **Location**: `whitespace-stego-core/src/`
- **Purpose**: High-performance Rust implementation
- **Features**:
  - Same functionality as Python core
  - Memory-safe implementation
  - Cross-platform compilation
  - Used by Python backend via PyO3
  - Comprehensive error handling
  - Property-based testing

#### C Core (`c/src/`)
- **Location**: `c/src/whitespace_stego.c`
- **Purpose**: C implementation for systems programming
- **Features**:
  - Minimal dependencies
  - Static linking capability
  - Cross-platform compilation
  - Shared library support
  - Memory management utilities

#### Go Core (`go/src/`)
- **Location**: `go/src/core.go`
- **Purpose**: Go implementation for cloud and web services
- **Features**:
  - Native Go performance
  - Cross-platform compilation
  - Simple deployment
  - Standard library integration

#### WASM Core (`wasi/src/`)
- **Location**: `wasi/src/lib.rs`
- **Purpose**: WebAssembly implementation for browsers
- **Features**:
  - Browser-compatible cryptography
  - JavaScript bindings
  - No server dependencies
  - Interactive web interface

### 2. CLI Applications

#### Python CLI (`whitespace_stego/cli.py`)
- **Location**: `whitespace_stego/cli.py`
- **Purpose**: Primary command-line interface
- **Features**:
  - Multiple backend support
  - File and stdin/stdout handling
  - Interactive mode
  - Verbose logging
  - Cross-platform compatibility

#### Rust CLI (`whitespace-stego-cli/`)
- **Location**: `whitespace-stego-cli/src/`
- **Purpose**: High-performance command-line interface
- **Features**:
  - Subcommand architecture (encode, decode, analyze, extract)
  - Progress indicators
  - Interactive mode
  - Comprehensive error reporting
  - File streaming support

#### C CLI (`c/src/main.c`)
- **Location**: `c/src/main.c`
- **Purpose**: Lightweight command-line interface
- **Features**:
  - Minimal dependencies
  - Fast execution
  - File-based operations
  - Simple argument parsing

#### Go CLI (`go/src/main.go`)
- **Location**: `go/src/main.go`
- **Purpose**: Go-based command-line interface
- **Features**:
  - Native Go performance
  - Simple deployment
  - Standard flag parsing
  - Cross-platform binaries

### 3. Backend Services

#### Python Backend
- **Type**: Pure Python implementation
- **Use Case**: Development, testing, cross-platform compatibility
- **Performance**: Moderate (interpreted)
- **Dependencies**: `cryptography`, `click`

#### Rust Backend (PyO3)
- **Type**: Rust extension for Python
- **Use Case**: High-performance Python applications
- **Performance**: Excellent (compiled)
- **Dependencies**: `maturin`, `pyo3`
- **Location**: `whitespace-stego-rust/`

#### C Backend (ctypes)
- **Type**: C shared library accessed via ctypes
- **Use Case**: High-performance Python applications
- **Performance**: Excellent (compiled)
- **Dependencies**: `ctypes`, compiled C library
- **Location**: `whitespace_stego/c_backend.py`

#### WASM Backend
- **Type**: WebAssembly module
- **Use Case**: Browser-based applications
- **Performance**: Good (compiled, sandboxed)
- **Dependencies**: `wasm-pack`, `web-sys`

## Data Flow

### Encoding Process
```
Input Message → Base64 Encode → (Optional) Encrypt → Zero-width Encode → Insert into Carrier
```

### Decoding Process
```
Carrier Text → Extract Zero-width → Decode Binary → (Optional) Decrypt → Base64 Decode → Original Message
```

### Multiple Message Support
```
Carrier Text → Extract All Zero-width → Decode Each → (Optional) Decrypt Each → Multiple Messages
```

### Cross-Backend Compatibility
```
Python Encode → Rust Decode ✓
Rust Encode → C Decode ✓
C Encode → Go Decode ✓
Go Encode → WASM Decode ✓
WASM Encode → Python Decode ✓
```

## Implementation Details

### Zero-width Unicode Characters

The system uses four specific Unicode characters for steganography:

| Character | Unicode | Name | Purpose |
|-----------|---------|------|---------|
| `\uFEFF` | U+FEFF | Zero-width no-break space | Start marker |
| `\u200C` | U+200C | Zero-width non-joiner | End marker |
| `\u200B` | U+200B | Zero-width space | Binary 0 |
| `\u200D` | U+200D | Zero-width joiner | Binary 1 |

### Encryption

When password protection is enabled:
- **Algorithm**: Fernet (AES-128 in CBC mode with PKCS7 padding)
- **Key Derivation**: PBKDF2 with SHA256
- **Compatibility**: All backends use the same encryption scheme

### Error Handling

Each implementation provides consistent error handling:
- **Invalid input**: Graceful degradation with clear error messages
- **Corrupted data**: Detection and reporting of steganographic corruption
- **Password mismatch**: Secure failure without information leakage
- **Multiple messages**: Support for extracting multiple embedded messages

## Build System

### Makefile Architecture
```
Makefile (Root)
├── Python targets (venv, install, test, coverage)
├── Rust targets (maturin-develop, rust, rust-cli)
├── C targets (c, c-shared)
├── Go targets (go)
├── WASM targets (wasi-web)
└── Docker targets (python-binary-docker)
```

### Cargo Workspace
```
Cargo.toml (Workspace Root)
├── whitespace-stego-core (shared library)
├── whitespace-stego-cli (Rust CLI)
├── whitespace-stego-rust (Python bindings)
├── whitespace-stego-python (alternative bindings)
├── rust (legacy CLI)
└── wasi (WebAssembly)
```

### Go Module
```
go/
├── go.mod (module definition)
├── go.sum (dependency checksums)
├── src/ (source code)
└── bin/ (compiled binaries)
```

## Testing Architecture

### Test Categories
1. **Unit Tests**: Individual function testing
2. **Integration Tests**: Cross-backend compatibility
3. **CLI Tests**: Command-line interface validation
4. **Cross-Implementation Tests**: Round-trip testing between languages
5. **Unicode Tests**: Multi-language and emoji support
6. **Performance Tests**: Benchmarking and optimization
7. **WASM Tests**: Browser-based functionality

### Test Coverage
- **Python**: >95% coverage with pytest
- **Rust**: Property-based testing with proptest
- **C**: Unit tests with custom test framework
- **Go**: Standard Go testing
- **WASM**: Browser automation with Selenium

### Cross-Implementation Testing
- **Round-trip tests**: Encode in one language, decode in another
- **Unicode compatibility**: Test with various languages and emojis
- **Performance benchmarks**: Compare implementations
- **Error handling**: Consistent error behavior across languages

## Security Considerations

### Cryptographic Security
- **Key Derivation**: PBKDF2 with sufficient iterations
- **Random Number Generation**: Cryptographically secure RNG
- **Memory Management**: Secure memory clearing where applicable
- **Input Validation**: Comprehensive input sanitization

### Steganographic Security
- **Detection Resistance**: No obvious patterns in encoded text
- **Capacity**: Efficient encoding to minimize carrier size
- **Robustness**: Error detection and correction capabilities
- **Multiple Messages**: Support for layered steganography

## Performance Characteristics

### Benchmarks (approximate)
| Backend | Encode (1KB) | Decode (1KB) | Memory Usage |
|---------|-------------|-------------|--------------|
| Python | 5ms | 3ms | 2MB |
| Rust | 1ms | 0.5ms | 1MB |
| C | 0.8ms | 0.4ms | 0.8MB |
| Go | 1.2ms | 0.6ms | 1.2MB |
| WASM | 2ms | 1ms | 1.5MB |

### Optimization Strategies
- **Rust**: Zero-copy operations, efficient memory management
- **C**: Direct memory manipulation, minimal overhead
- **Python**: Cython-like optimizations via PyO3
- **Go**: Native compilation, efficient garbage collection
- **WASM**: Optimized compilation for browser execution

## Deployment Options

### Development
- **Local**: Full development environment with all backends
- **Docker**: Isolated build environment
- **CI/CD**: Automated testing and deployment
- **Jupyter**: Interactive development and demonstration

### Production
- **Python**: PyPI package distribution
- **Rust**: Cargo crate distribution
- **C**: Static binary distribution
- **Go**: Go module distribution
- **WASM**: CDN-hosted web application

### Binary Distribution
- **Location**: `bin/` directory
- **Platforms**: Linux, macOS, Windows
- **Architectures**: x86_64, ARM64
- **Dependencies**: Minimal runtime dependencies

## Future Architecture

### Planned Enhancements
1. **Plugin System**: Extensible backend architecture
2. **Cloud Integration**: Server-side processing capabilities
3. **Mobile Support**: Native mobile applications
4. **Advanced Cryptography**: Post-quantum cryptography support
5. **Streaming Support**: Large file processing
6. **Compression**: Efficient encoding for large messages

### Scalability Considerations
- **Horizontal Scaling**: Stateless design enables load balancing
- **Vertical Scaling**: Efficient resource utilization
- **Caching**: Intelligent caching of frequently used operations
- **Monitoring**: Comprehensive metrics and logging
- **Parallel Processing**: Multi-threaded encoding/decoding

## Contributing to Architecture

When contributing to the architecture:

1. **Maintain Compatibility**: Ensure cross-backend compatibility
2. **Follow Patterns**: Use established patterns for new components
3. **Document Changes**: Update this document for architectural changes
4. **Test Thoroughly**: Include tests for all new functionality
5. **Consider Performance**: Benchmark new implementations
6. **Cross-Language Testing**: Ensure new features work across all implementations

For detailed implementation guides, see:
- [Rust Implementation](RUST.md)
- [Testing Strategy](TESTING.md)
- [API Reference](API_REFERENCE.md)
- [Usage Guide](USAGE.md) 