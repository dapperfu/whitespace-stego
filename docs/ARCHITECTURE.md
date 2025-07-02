# System Architecture

This document describes the architecture of the whitespace steganography toolkit, including component relationships, data flow, and design decisions.

## Overview

The whitespace steganography toolkit is designed as a multi-language, multi-backend system that provides consistent steganography capabilities across different platforms and use cases.

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interfaces                          │
├─────────────────────────────────────────────────────────────┤
│  CLI (Python)  │  CLI (Rust)  │  CLI (C)  │  Web (WASM)    │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Core Libraries                           │
├─────────────────────────────────────────────────────────────┤
│  Python Core   │  Rust Core   │  C Core    │  WASM Core     │
│  (whitespace_  │  (whitespace-│  (whitespace│  (whitespace-  │
│   stego)       │  -stego-core)│  _stego.c)  │  stego-wasi)   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Backend Services                         │
├─────────────────────────────────────────────────────────────┤
│  Python Backend│  Rust Backend│  C Backend  │  WASM Backend │
│  (Pure Python) │  (PyO3)      │  (Native)   │  (WebAssembly)│
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

#### Rust Core (`whitespace-stego-core/`)
- **Location**: `whitespace-stego-core/src/`
- **Purpose**: High-performance Rust implementation
- **Features**:
  - Same functionality as Python core
  - Memory-safe implementation
  - Cross-platform compilation
  - Used by Python backend via PyO3

#### C Core (`c/src/`)
- **Location**: `c/src/whitespace_stego.c`
- **Purpose**: C implementation for systems programming
- **Features**:
  - Minimal dependencies
  - Static linking capability
  - Cross-platform compilation

#### WASM Core (`wasi/src/`)
- **Location**: `wasi/src/lib.rs`
- **Purpose**: WebAssembly implementation for browsers
- **Features**:
  - Browser-compatible cryptography
  - JavaScript bindings
  - No server dependencies

### 2. Backend Services

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

#### C Backend
- **Type**: Native C implementation
- **Use Case**: Systems programming, embedded systems
- **Performance**: Excellent (compiled)
- **Dependencies**: `libcrypto`, `libssl`

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

### Cross-Backend Compatibility
```
Python Encode → Rust Decode ✓
Rust Encode → C Decode ✓
C Encode → WASM Decode ✓
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

## Build System

### Makefile Architecture
```
Makefile (Root)
├── Python targets (venv, install, test)
├── Rust targets (maturin-develop, rust)
├── C targets (c)
├── WASM targets (wasi-web)
└── Docker targets (python-binary-docker)
```

### Cargo Workspace
```
Cargo.toml (Workspace Root)
├── whitespace-stego-core (shared library)
├── whitespace-stego-cli (Rust CLI)
├── whitespace-stego-backend (Python bindings)
├── whitespace-stego-python (alternative bindings)
├── rust (legacy CLI)
└── wasi (WebAssembly)
```

## Testing Architecture

### Test Categories
1. **Unit Tests**: Individual function testing
2. **Integration Tests**: Cross-backend compatibility
3. **CLI Tests**: Command-line interface validation
4. **WASM Tests**: Browser-based functionality
5. **Performance Tests**: Benchmarking and optimization

### Test Coverage
- **Python**: >95% coverage with pytest
- **Rust**: Property-based testing with proptest
- **C**: Unit tests with custom test framework
- **WASM**: Browser automation with Selenium

## Security Considerations

### Cryptographic Security
- **Key Derivation**: PBKDF2 with sufficient iterations
- **Random Number Generation**: Cryptographically secure RNG
- **Memory Management**: Secure memory clearing where applicable

### Steganographic Security
- **Detection Resistance**: No obvious patterns in encoded text
- **Capacity**: Efficient encoding to minimize carrier size
- **Robustness**: Error detection and correction capabilities

## Performance Characteristics

### Benchmarks (approximate)
| Backend | Encode (1KB) | Decode (1KB) | Memory Usage |
|---------|-------------|-------------|--------------|
| Python | 5ms | 3ms | 2MB |
| Rust | 1ms | 0.5ms | 1MB |
| C | 0.8ms | 0.4ms | 0.8MB |
| WASM | 2ms | 1ms | 1.5MB |

### Optimization Strategies
- **Rust**: Zero-copy operations, efficient memory management
- **C**: Direct memory manipulation, minimal overhead
- **Python**: Cython-like optimizations via PyO3
- **WASM**: Optimized compilation for browser execution

## Deployment Options

### Development
- **Local**: Full development environment with all backends
- **Docker**: Isolated build environment
- **CI/CD**: Automated testing and deployment

### Production
- **Python**: PyPI package distribution
- **Rust**: Cargo crate distribution
- **C**: Static binary distribution
- **WASM**: CDN-hosted web application

## Future Architecture

### Planned Enhancements
1. **Plugin System**: Extensible backend architecture
2. **Cloud Integration**: Server-side processing capabilities
3. **Mobile Support**: Native mobile applications
4. **Advanced Cryptography**: Post-quantum cryptography support

### Scalability Considerations
- **Horizontal Scaling**: Stateless design enables load balancing
- **Vertical Scaling**: Efficient resource utilization
- **Caching**: Intelligent caching of frequently used operations
- **Monitoring**: Comprehensive metrics and logging

## Contributing to Architecture

When contributing to the architecture:

1. **Maintain Compatibility**: Ensure cross-backend compatibility
2. **Follow Patterns**: Use established patterns for new components
3. **Document Changes**: Update this document for architectural changes
4. **Test Thoroughly**: Include tests for all new functionality
5. **Consider Performance**: Benchmark new implementations

For detailed implementation guides, see:
- [Rust Implementation](RUST.md)
- [Testing Strategy](TESTING.md)
- [Contributing Guide](CONTRIBUTING.md) 