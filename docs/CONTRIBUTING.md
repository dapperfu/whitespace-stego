# Contributing

Thank you for your interest in contributing to the whitespace steganography toolkit! This guide will help you get started with development and contribution.

## Quick Start

### 1. Setup Development Environment
```bash
# Clone and setup
git clone <repository-url>
cd whitespace-stego3
make install

# Build all implementations
make rust     # Rust CLI
make c        # C CLI
make go       # Go CLI
make wasi-web # WebAssembly UI
```

### 2. Run Tests
```bash
# Run all tests
make test-all

# Run specific test suites
make test        # Python tests
make test-rust   # Rust tests
make test-c      # C tests
make test-go     # Go tests
make test-wasm   # WebAssembly tests
```

### 3. Make Changes
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make your changes
# Add tests
# Update documentation

# Test your changes
make test
```

## Development Guidelines

### Code Style

#### Python
- **Formatting**: Use `ruff format` (configured in pyproject.toml)
- **Linting**: Use `ruff` for linting
- **Type Hints**: Full mypy typing required
- **Docstrings**: NumPy style docstrings
- **Line Length**: 88 characters (Black default)

```python
def encode_message(message: str, carrier: str, password: Optional[str] = None) -> str:
    """
    Encode a message into carrier text using whitespace steganography.
    
    Parameters
    ----------
    message : str
        The secret message to hide
    carrier : str
        The carrier text where the message will be hidden
    password : str, optional
        Password for encryption. If provided, message is encrypted using Fernet
        
    Returns
    -------
    str
        The carrier text with the hidden message embedded
        
    Raises
    ------
    ValueError
        If message is empty or invalid
    RuntimeError
        If backend is not available
    """
```

#### Rust
- **Formatting**: Use `cargo fmt`
- **Linting**: Use `cargo clippy`
- **Documentation**: Use `///` for doc comments following Microsoft Project Mu conventions
- **Error Handling**: Use `thiserror` for custom errors

```rust
/// Encode a message into carrier text using whitespace steganography.
///
/// # Arguments
///
/// * `message` - The secret message to hide
/// * `carrier` - The carrier text where the message will be hidden
/// * `password` - Optional password for encryption
///
/// # Returns
///
/// The encoded carrier text or an error
///
/// # Errors
///
/// Returns `StegoError::EncodingFailed` if encoding fails
/// Returns `StegoError::InvalidCarrier` if carrier is invalid
///
/// # Examples
///
/// ```
/// use whitespace_stego_core::encode;
///
/// let encoded = encode("Secret", "Hello world!", None)?;
/// ```
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Implementation
}
```

#### C
- **Formatting**: Use consistent indentation (4 spaces)
- **Naming**: Use snake_case for functions and variables
- **Documentation**: Use Doxygen-style comments
- **Error Handling**: Return boolean with error message function

```c
/**
 * Encode a message into carrier text using whitespace steganography.
 *
 * @param message The secret message to hide
 * @param carrier The carrier text where the message will be hidden
 * @param password Optional password for encryption (can be NULL)
 * @param result Pointer to store the encoded result
 * @return true on success, false on failure
 */
bool whitespace_stego_encode(const char* message, const char* carrier, 
                            const char* password, char** result);
```

#### Go
- **Formatting**: Use `gofmt`
- **Linting**: Use `golint` and `golangci-lint`
- **Documentation**: Use standard Go documentation format
- **Error Handling**: Return error values

```go
// Encode encodes a message into carrier text using whitespace steganography.
//
// Parameters:
//   - message: The secret message to hide
//   - carrier: The carrier text where the message will be hidden
//   - password: Optional password for encryption
//
// Returns:
//   - The encoded carrier text
//   - Error if encoding fails
func Encode(message, carrier, password string) (string, error) {
    // Implementation
}
```

### Testing Requirements

#### Python Tests
- **Coverage**: Maintain >95% coverage
- **Style**: Use pytest with fixtures
- **Categories**: Unit, integration, CLI, cross-backend, unicode
- **Running**: `pytest tests/ -v`

```python
def test_encode_basic():
    """Test basic encoding functionality."""
    result = encode("Secret", "Hello world!")
    assert "Hello world!" in result
    assert decode(result) == "Secret"

def test_encode_with_password():
    """Test encoding with password protection."""
    result = encode("Secret", "Hello world!", password="test")
    assert decode(result, password="test") == "Secret"
    with pytest.raises(ValueError):
        decode(result, password="wrong")

def test_unicode_support():
    """Test Unicode and emoji support."""
    result = encode("Secret 😎", "Hello 🌍 world!")
    assert decode(result) == "Secret 😎"
```

#### Rust Tests
- **Style**: Use standard Rust testing
- **Property Testing**: Use proptest for comprehensive testing
- **Integration Tests**: Test cross-backend compatibility
- **Running**: `cargo test`

```rust
#[test]
fn test_encode_basic() {
    let result = encode("Secret", "Hello world!", None).unwrap();
    assert!(result.contains("Hello world!"));
    assert_eq!(decode(&result, None).unwrap(), "Secret");
}

#[test]
fn test_encode_with_password() {
    let result = encode("Secret", "Hello world!", Some("test")).unwrap();
    assert_eq!(decode(&result, Some("test")).unwrap(), "Secret");
    assert!(decode(&result, Some("wrong")).is_err());
}

#[test]
fn test_unicode_support() {
    let result = encode("Secret 😎", "Hello 🌍 world!", None).unwrap();
    assert_eq!(decode(&result, None).unwrap(), "Secret 😎");
}
```

#### C Tests
- **Style**: Use custom test framework
- **Running**: `cd c && make test`

```c
void test_encode_basic() {
    char* result;
    assert(whitespace_stego_encode("Secret", "Hello world!", NULL, &result));
    assert(strstr(result, "Hello world!") != NULL);
    whitespace_stego_free(result);
}
```

#### Go Tests
- **Style**: Use standard Go testing
- **Running**: `cd go && go test ./...`

```go
func TestEncodeBasic(t *testing.T) {
    result, err := Encode("Secret", "Hello world!", "")
    if err != nil {
        t.Fatal(err)
    }
    if !strings.Contains(result, "Hello world!") {
        t.Error("Result should contain carrier text")
    }
}
```

### Cross-Implementation Testing

All implementations must be compatible:
- **Encoding**: Any implementation can encode messages
- **Decoding**: Any implementation can decode messages from any other
- **Password Protection**: All implementations use the same encryption scheme
- **Error Handling**: Consistent error messages across implementations
- **Unicode Support**: Full Unicode compatibility across all implementations

### Cross-Implementation Test Files
- `tests/test_20_cross_impl_roundtrip.py` - Round-trip compatibility tests
- `tests/test_21_unicode_cross_impl.py` - Unicode compatibility tests
- `tests/test_22_comprehensive_encoding_identity.py` - Comprehensive identity tests

## Documentation Requirements

### Code Documentation
- **Functions**: Document all public functions
- **Classes**: Document all classes and their methods
- **Examples**: Include usage examples in docstrings
- **Parameters**: Document all parameters and return values
- **Errors**: Document all possible error conditions

### User Documentation
- **Installation**: Update [Installation Guide](INSTALLATION.md) for new dependencies
- **Usage**: Update [Usage Guide](USAGE.md) for new features
- **API**: Update [API Reference](API_REFERENCE.md) for new functions
- **Architecture**: Update [Architecture](ARCHITECTURE.md) for structural changes
- **Benchmarks**: Update [Benchmarks](BENCHMARKS.md) for performance changes

### Commit Messages

Use conventional commit format with detailed technical attribution:

```
type(scope): description

/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2024-12-19T10:30:00Z
 * Context: Brief description of what this code does
 * 
 * Technical details:
 * - LLM: Claude 3.5 Sonnet (2024-10-22)
 * - IDE: Cursor (cursor.sh)
 * - Generation method: AI-assisted pair programming
 * - Code style: Language-specific style guide
 * - Dependencies: Key dependencies
 */

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

**Examples:**
```
feat(python): add new backend selection API

/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2024-12-19T10:30:00Z
 * Context: Added backend selection API for Python implementation
 * 
 * Technical details:
 * - LLM: Claude 3.5 Sonnet (2024-10-22)
 * - IDE: Cursor (cursor.sh)
 * - Generation method: AI-assisted pair programming
 * - Code style: Python with full mypy typing
 * - Dependencies: whitespace_stego, cryptography
 */

- Add get_available_backends() function
- Add set_default_backend() function
- Update CLI to show available backends

Closes #123
```

## Project Structure

### Core Components
- `whitespace_stego/` - Python implementation
- `whitespace-stego-core/` - Rust core library
- `whitespace-stego-cli/` - Rust CLI application
- `whitespace-stego-rust/` - Python bindings for Rust
- `c/` - C implementation
- `go/` - Go implementation
- `wasi/` - WebAssembly implementation

### Testing Structure
- `tests/` - Python test suite
- `whitespace-stego-core/tests/` - Rust tests
- `c/test/` - C tests
- `go/` - Go tests (integrated)

### Documentation Structure
- `docs/` - User documentation
- `notebooks/` - Jupyter notebooks
- `examples/` - Usage examples

## Build System

### Makefile Targets
- `make install` - Install Python package
- `make rust` - Build Rust CLI
- `make c` - Build C implementation
- `make go` - Build Go implementation
- `make wasi-web` - Build WebAssembly UI
- `make test-all` - Run all tests
- `make coverage` - Generate coverage reports

### Cargo Workspace
- `whitespace-stego-core` - Core library
- `whitespace-stego-cli` - CLI application
- `whitespace-stego-rust` - Python bindings
- `wasi` - WebAssembly module

## Performance Considerations

### Benchmarking
- Run benchmarks before and after changes
- Compare performance across implementations
- Document performance impacts
- Update benchmark documentation

### Optimization Guidelines
- **Rust**: Focus on zero-copy operations
- **C**: Minimize memory allocations
- **Python**: Use efficient data structures
- **Go**: Leverage standard library optimizations

## Security Guidelines

### Cryptographic Security
- Use cryptographically secure random number generation
- Implement proper key derivation
- Clear sensitive memory when possible
- Validate all inputs

### Steganographic Security
- Ensure no obvious patterns in encoded text
- Maintain consistent encoding across implementations
- Test with various text types and languages

## Release Process

### Version Management
- Follow semantic versioning
- Update version numbers in all implementations
- Tag releases in git
- Update documentation for new features

### Distribution
- **Python**: PyPI package
- **Rust**: Cargo crates
- **C**: Static binaries
- **Go**: Go modules
- **WASM**: Web distribution

## Getting Help

### Communication Channels
- GitHub Issues for bug reports
- GitHub Discussions for questions
- Pull Requests for contributions

### Resources
- [Architecture Documentation](ARCHITECTURE.md)
- [API Reference](API_REFERENCE.md)
- [Testing Guide](TESTING.md)
- [Benchmarks](BENCHMARKS.md)

Thank you for contributing to the whitespace steganography toolkit! 