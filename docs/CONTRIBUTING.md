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
make wasi-web # WebAssembly UI
```

### 2. Run Tests
```bash
# Run all tests
make test-all

# Run specific test suites
make test        # Python tests
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
- **Documentation**: Use `///` for doc comments
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
 * @param carrier The carrier text (can be NULL for empty carrier)
 * @param carrier_len Length of carrier text
 * @param message The secret message to hide
 * @param password Optional password for encryption (can be NULL)
 * @param result Pointer to store the encoded result
 * @return true on success, false on failure
 */
bool whitespace_stego_encode(const char* carrier, size_t carrier_len, 
                            const char* message, const char* password, 
                            char** result);
```

### Testing Requirements

#### Python Tests
- **Coverage**: Maintain >95% coverage
- **Style**: Use pytest with fixtures
- **Categories**: Unit, integration, CLI, cross-backend
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
```

#### Rust Tests
- **Style**: Use standard Rust testing
- **Property Testing**: Use proptest for comprehensive testing
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
```

#### C Tests
- **Style**: Use custom test framework
- **Running**: `cd c && make test`

```c
void test_encode_basic() {
    char* result;
    assert(whitespace_stego_encode("Hello world!", 12, "Secret", NULL, &result));
    assert(strstr(result, "Hello world!") != NULL);
    whitespace_stego_free(result);
}
```

### Cross-Backend Compatibility

All implementations must be compatible:
- **Encoding**: Any backend can encode messages
- **Decoding**: Any backend can decode messages from any other backend
- **Password Protection**: All backends use the same encryption scheme
- **Error Handling**: Consistent error messages across backends

### Documentation Requirements

#### Code Documentation
- **Functions**: Document all public functions
- **Classes**: Document all classes and their methods
- **Examples**: Include usage examples in docstrings
- **Parameters**: Document all parameters and return values

#### User Documentation
- **Installation**: Update [Installation Guide](INSTALLATION.md) for new dependencies
- **Usage**: Update [Usage Guide](USAGE.md) for new features
- **API**: Update [API Reference](API_REFERENCE.md) for new functions
- **Architecture**: Update [Architecture](ARCHITECTURE.md) for structural changes

#### Commit Messages

Use conventional commit format:
```
type(scope): description

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

- Add get_available_backends() function
- Add set_default_backend() function
- Update CLI to show available backends

Closes #123
```

```
fix(rust): handle empty carrier text correctly

The Rust implementation now properly handles empty carrier text
by inserting the encoded message at the beginning.

Fixes #456
```

### Pull Request Process

1. **Fork and Clone**: Fork the repository and clone your fork
2. **Create Branch**: Create a feature branch from `main`
3. **Make Changes**: Implement your changes following the guidelines
4. **Add Tests**: Include tests for all new functionality
5. **Update Docs**: Update relevant documentation
6. **Run Tests**: Ensure all tests pass
7. **Submit PR**: Create a pull request with clear description

#### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Cross-backend compatibility verified
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added and passing
- [ ] No breaking changes (or documented)
- [ ] Cross-backend compatibility maintained
```

## Development Tools

### Required Tools
- **Python**: 3.8+
- **Rust**: Latest stable
- **C Compiler**: GCC/Clang
- **Docker**: For portable builds
- **Git**: Version control

### Recommended Tools
- **IDE**: VS Code with Rust/Python extensions
- **Terminal**: iTerm2, Alacritty, or similar
- **Git Hooks**: Pre-commit hooks for formatting

### Development Commands

```bash
# Setup development environment
make install

# Run tests
make test-all

# Format code
make format

# Build all implementations
make rust c wasi-web

# Create portable binary
make python-binary-docker

# Clean everything
make clean
```

## Getting Help

### Resources
- [Architecture Documentation](ARCHITECTURE.md) - System design overview
- [API Reference](API_REFERENCE.md) - Complete API documentation
- [Testing Guide](TESTING.md) - Testing strategies and procedures
- [Issue Tracker](https://github.com/your-repo/issues) - Report bugs and request features

### Communication
- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Code Review**: All PRs require review before merging

## Code of Conduct

Be respectful and constructive in all interactions:
- **Respect**: Treat all contributors with respect
- **Constructive**: Provide constructive feedback
- **Inclusive**: Welcome contributors from all backgrounds
- **Professional**: Maintain professional communication

---

For more information, see:
- [Testing & Quality Assurance](TESTING.md)
- [Usage Guide](USAGE.md)
- [Installation Guide](INSTALLATION.md)
- [Architecture](ARCHITECTURE.md) 