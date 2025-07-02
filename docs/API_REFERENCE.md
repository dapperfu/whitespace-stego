# API Reference

This document provides comprehensive API reference for all language implementations of the whitespace steganography toolkit.

## Python API

### Core Functions

#### `whitespace_stego.core.encode(message, carrier, password=None, backend='python')`

Encodes a message into carrier text using whitespace steganography.

**Parameters:**
- `message` (str): The secret message to hide
- `carrier` (str): The carrier text where the message will be hidden
- `password` (str, optional): Password for encryption. If provided, message is encrypted using Fernet
- `backend` (str): Backend to use ('python', 'rust', 'c'). Defaults to 'python'

**Returns:**
- `str`: The carrier text with the hidden message embedded

**Raises:**
- `ValueError`: If message is empty or invalid
- `RuntimeError`: If backend is not available
- `cryptography.fernet.InvalidToken`: If password is incorrect during encryption

**Example:**
```python
from whitespace_stego.core import encode

# Basic encoding
encoded = encode("Secret message", "Hello world!")
print(encoded)  # Looks like "Hello world!" but contains hidden data

# With password protection
encoded = encode("Secret message", "Hello world!", password="mypassword")
```

#### `whitespace_stego.core.decode(carrier, password=None, backend='python')`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier` (str): The carrier text containing the hidden message
- `password` (str, optional): Password for decryption. Required if message was encrypted
- `backend` (str): Backend to use ('python', 'rust', 'c'). Defaults to 'python'

**Returns:**
- `str`: The decoded secret message

**Raises:**
- `ValueError`: If no hidden message is found or carrier is invalid
- `RuntimeError`: If backend is not available
- `cryptography.fernet.InvalidToken`: If password is incorrect

**Example:**
```python
from whitespace_stego.core import decode

# Basic decoding
message = decode(encoded_text)
print(message)  # "Secret message"

# With password protection
message = decode(encoded_text, password="mypassword")
```

### CLI Interface

#### `whitespace_stego.cli.main()`

Main CLI entry point.

**Usage:**
```bash
python -m whitespace_stego.cli encode --message "Secret" --carrier "Hello" --output encoded.txt
python -m whitespace_stego.cli decode --carrier-file encoded.txt
```

**Options:**
- `--message, --message-file`: Message to hide (inline or file)
- `--carrier, --carrier-file`: Carrier text (inline or file)
- `--output`: Output file (or `-` for stdout)
- `--password`: Optional password for encryption
- `--backend`: Choose backend (python, rust, c)
- `--verbose`: Verbose logging

### Backend Management

#### `whitespace_stego.core.get_available_backends()`

Returns list of available backends.

**Returns:**
- `list[str]`: List of available backend names

**Example:**
```python
from whitespace_stego.core import get_available_backends

backends = get_available_backends()
print(backends)  # ['python', 'rust', 'c']
```

#### `whitespace_stego.core.set_default_backend(backend)`

Sets the default backend for encode/decode operations.

**Parameters:**
- `backend` (str): Backend name to set as default

**Raises:**
- `ValueError`: If backend is not available

## Rust API

### Core Functions

#### `whitespace_stego_core::encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError>`

Encodes a message into carrier text.

**Parameters:**
- `message`: The secret message to hide
- `carrier`: The carrier text where the message will be hidden
- `password`: Optional password for encryption

**Returns:**
- `Result<String, StegoError>`: The encoded carrier text or error

**Example:**
```rust
use whitespace_stego_core::{encode, StegoError};

fn main() -> Result<(), StegoError> {
    // Basic encoding
    let encoded = encode("Secret message", "Hello world!", None)?;
    println!("{}", encoded);
    
    // With password
    let encoded = encode("Secret message", "Hello world!", Some("mypassword"))?;
    Ok(())
}
```

#### `whitespace_stego_core::decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError>`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier`: The carrier text containing the hidden message
- `password`: Optional password for decryption

**Returns:**
- `Result<String, StegoError>`: The decoded message or error

**Example:**
```rust
use whitespace_stego_core::{decode, StegoError};

fn main() -> Result<(), StegoError> {
    let message = decode(&encoded_text, None)?;
    println!("{}", message);
    Ok(())
}
```

### Error Types

#### `StegoError`

Enumeration of possible steganography errors.

```rust
#[derive(Debug, thiserror::Error)]
pub enum StegoError {
    #[error("Empty message not allowed")]
    EmptyMessage,
    
    #[error("No hidden message found in carrier")]
    NoMessageFound,
    
    #[error("Invalid carrier text")]
    InvalidCarrier,
    
    #[error("Encryption error: {0}")]
    EncryptionError(String),
    
    #[error("Decryption error: {0}")]
    DecryptionError(String),
    
    #[error("Base64 encoding error: {0}")]
    Base64Error(String),
    
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
}
```

### CLI Interface

#### `whitespace_stego_cli::main()`

Main CLI entry point for Rust implementation.

**Usage:**
```bash
whitespace-stego-rs encode --mf message.txt --cf carrier.txt -o encoded.txt
whitespace-stego-rs decode --cf encoded.txt -o decoded.txt
```

**Options:**
- `-m, --message`: Inline message
- `--mf`: Message file
- `-c, --carrier`: Inline carrier
- `--cf`: Carrier file
- `-o, --output`: Output file (or `-` for stdout)
- `-p, --password`: Password
- `--verbose`: Verbose logging

## C API

### Core Functions

#### `bool whitespace_stego_encode(const char* carrier, size_t carrier_len, const char* message, const char* password, char** result)`

Encodes a message into carrier text.

**Parameters:**
- `carrier`: The carrier text (can be NULL for empty carrier)
- `carrier_len`: Length of carrier text
- `message`: The secret message to hide
- `password`: Optional password for encryption (can be NULL)
- `result`: Pointer to store the encoded result

**Returns:**
- `bool`: `true` on success, `false` on failure

**Example:**
```c
#include "whitespace_stego.h"

char* result;
if (whitespace_stego_encode("Hello world!", 12, "Secret", "password", &result)) {
    printf("Encoded: %s\n", result);
    whitespace_stego_free(result);
}
```

#### `bool whitespace_stego_decode(const char* carrier, size_t carrier_len, const char* password, char** result)`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier`: The carrier text containing the hidden message
- `carrier_len`: Length of carrier text
- `password`: Optional password for decryption (can be NULL)
- `result`: Pointer to store the decoded result

**Returns:**
- `bool`: `true` on success, `false` on failure

**Example:**
```c
#include "whitespace_stego.h"

char* result;
if (whitespace_stego_decode(encoded_text, strlen(encoded_text), "password", &result)) {
    printf("Decoded: %s\n", result);
    whitespace_stego_free(result);
}
```

#### `const char* whitespace_stego_last_error(void)`

Returns the last error message.

**Returns:**
- `const char*`: Error message string

**Example:**
```c
if (!whitespace_stego_encode(...)) {
    printf("Error: %s\n", whitespace_stego_last_error());
}
```

#### `void whitespace_stego_free(char* ptr)`

Frees memory allocated by the library.

**Parameters:**
- `ptr`: Pointer to memory to free

**Example:**
```c
char* result;
if (whitespace_stego_encode(...)) {
    // Use result
    whitespace_stego_free(result);
}
```

### CLI Interface

#### `whitespace-stego-c`

Command-line interface for C implementation.

**Usage:**
```bash
whitespace-stego-c encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt
```

**Options:**
- `--message-file, -m`: Message file
- `--carrier-file, -c`: Carrier file
- `--output, -o`: Output file
- `--password, -p`: Password
- `--verbose, -v`: Verbose output

## WebAssembly API

### JavaScript Interface

#### `encode(message, carrier, password = null)`

Encodes a message into carrier text.

**Parameters:**
- `message` (string): The secret message to hide
- `carrier` (string): The carrier text where the message will be hidden
- `password` (string, optional): Password for encryption

**Returns:**
- `string`: The encoded carrier text

**Example:**
```javascript
import init, { encode } from './whitespace_stego_wasi.js';

await init();
const encoded = encode("Secret message", "Hello world!");
console.log(encoded);
```

#### `decode(carrier, password = null)`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier` (string): The carrier text containing the hidden message
- `password` (string, optional): Password for decryption

**Returns:**
- `string`: The decoded message

**Example:**
```javascript
import init, { decode } from './whitespace_stego_wasi.js';

await init();
const message = decode(encoded_text);
console.log(message);
```

### Web Interface

The WASM implementation includes a complete web interface accessible at `http://localhost:8000` after running `make wasi-web`.

**Features:**
- Real-time encoding/decoding
- Copy-to-clipboard functionality
- Mobile-responsive design
- No server-side processing required

## Error Handling

### Python Errors

```python
from whitespace_stego.core import encode, decode, StegoError

try:
    encoded = encode("", "carrier")  # Empty message
except ValueError as e:
    print(f"Value error: {e}")

try:
    message = decode("invalid", password="wrong")
except ValueError as e:
    print(f"Decode error: {e}")
```

### Rust Errors

```rust
use whitespace_stego_core::{encode, StegoError};

match encode("", "carrier", None) {
    Ok(encoded) => println!("Success: {}", encoded),
    Err(StegoError::EmptyMessage) => println!("Empty message not allowed"),
    Err(e) => println!("Other error: {}", e),
}
```

### C Errors

```c
char* result;
if (!whitespace_stego_encode("carrier", 7, "", "password", &result)) {
    printf("Error: %s\n", whitespace_stego_last_error());
}
```

## Performance Considerations

### Backend Selection

```python
# Use fastest available backend
from whitespace_stego.core import get_available_backends, set_default_backend

backends = get_available_backends()
if 'rust' in backends:
    set_default_backend('rust')  # Fastest
elif 'c' in backends:
    set_default_backend('c')     # Second fastest
else:
    set_default_backend('python')  # Fallback
```

### Memory Management

```c
// Always free allocated memory
char* result;
if (whitespace_stego_encode(...)) {
    // Use result
    whitespace_stego_free(result);
}
```

### Batch Processing

```python
# For multiple operations, reuse backend
from whitespace_stego.core import encode, decode

# Set backend once
import whitespace_stego.core as ws
ws.set_default_backend('rust')

# Process multiple messages
messages = ["msg1", "msg2", "msg3"]
carrier = "Hello world!"
encoded_list = [encode(msg, carrier) for msg in messages]
```

## Cross-Language Compatibility

All implementations are designed to be compatible:

```python
# Encode in Python
encoded = encode("Secret", "Hello", password="pass")

# Decode in Rust
# (Same encoded text works across languages)
```

```rust
// Encode in Rust
let encoded = encode("Secret", "Hello", Some("pass"))?;

// Decode in Python
// (Same encoded text works across languages)
```

## Version Compatibility

### API Versioning

- **Python**: Follows semantic versioning
- **Rust**: Uses workspace versioning
- **C**: ABI-compatible within major versions
- **WASM**: Bundled with web interface

### Breaking Changes

Breaking changes are documented in release notes and may require:
- Updated function signatures
- New error types
- Changed default behaviors
- Deprecated function removal

## Related Documentation

- [Usage Guide](USAGE.md) - Practical usage examples
- [Installation Guide](INSTALLATION.md) - Setup instructions
- [Architecture](ARCHITECTURE.md) - System design overview
- [Testing Guide](TESTING.md) - Testing procedures 