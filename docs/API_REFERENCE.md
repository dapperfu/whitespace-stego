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

#### `whitespace_stego.core.extract_encoded(carrier)`

Extracts the encoded message and remaining carrier text separately.

**Parameters:**
- `carrier` (str): The carrier text containing the hidden message

**Returns:**
- `tuple[str, str]`: (encoded_message, remaining_carrier)

**Raises:**
- `ValueError`: If no hidden message is found

**Example:**
```python
from whitespace_stego.core import extract_encoded

encoded_part, remaining = extract_encoded(encoded_text)
print(f"Encoded: {encoded_part}")
print(f"Remaining: {remaining}")
```

#### `whitespace_stego.core.count_messages(carrier)`

Counts the number of messages embedded in carrier text.

**Parameters:**
- `carrier` (str): The carrier text to analyze

**Returns:**
- `int`: Number of embedded messages

**Example:**
```python
from whitespace_stego.core import count_messages

count = count_messages(encoded_text)
print(f"Found {count} embedded messages")
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

#### `whitespace_stego_core::decode_all(carrier: &str, password: Option<&str>) -> Result<Vec<String>, StegoError>`

Decodes all messages from carrier text.

**Parameters:**
- `carrier`: The carrier text containing hidden messages
- `password`: Optional password for decryption

**Returns:**
- `Result<Vec<String>, StegoError>`: Vector of decoded messages or error

**Example:**
```rust
use whitespace_stego_core::{decode_all, StegoError};

fn main() -> Result<(), StegoError> {
    let messages = decode_all(&encoded_text, None)?;
    for message in messages {
        println!("{}", message);
    }
    Ok(())
}
```

#### `whitespace_stego_core::extract_encoded(carrier: &str) -> Result<(String, String), StegoError>`

Extracts encoded message and remaining carrier text.

**Parameters:**
- `carrier`: The carrier text containing the hidden message

**Returns:**
- `Result<(String, String), StegoError>`: (encoded_message, remaining_carrier) or error

**Example:**
```rust
use whitespace_stego_core::{extract_encoded, StegoError};

fn main() -> Result<(), StegoError> {
    let (encoded, remaining) = extract_encoded(&carrier_text)?;
    println!("Encoded: {}", encoded);
    println!("Remaining: {}", remaining);
    Ok(())
}
```

#### `whitespace_stego_core::count_messages(carrier: &str) -> usize`

Counts embedded messages in carrier text.

**Parameters:**
- `carrier`: The carrier text to analyze

**Returns:**
- `usize`: Number of embedded messages

**Example:**
```rust
use whitespace_stego_core::count_messages;

let count = count_messages(&carrier_text);
println!("Found {} messages", count);
```

### Error Types

#### `StegoError`

Enumeration of possible steganography errors.

```rust
#[derive(Error, Debug, Clone, PartialEq)]
pub enum StegoError {
    /// Invalid carrier text (no markers found, malformed data, etc.)
    #[error("Invalid carrier text: {message}")]
    InvalidCarrier { message: String },

    /// Decryption failed (wrong password, corrupted data, etc.)
    #[error("Decryption failed: {message}")]
    DecryptionFailed { message: String },

    /// Encoding failed (invalid input, encryption error, etc.)
    #[error("Encoding failed: {message}")]
    EncodingFailed { message: String },

    /// Base64 encoding/decoding error
    #[error("Base64 error: {message}")]
    Base64Error { message: String },

    /// UTF-8 encoding/decoding error
    #[error("UTF-8 error: {message}")]
    Utf8Error { message: String },

    /// Invalid key for encryption/decryption
    #[error("Invalid key: {message}")]
    InvalidKey { message: String },

    /// No encoded message found in carrier text
    #[error("No encoded message found in carrier text")]
    NoMessageFound,

    /// Invalid binary data (wrong length, malformed bits, etc.)
    #[error("Invalid binary data: {message}")]
    InvalidBinaryData { message: String },
}
```

### CLI Interface

#### `whitespace-stego-cli`

Main CLI entry point for Rust implementation.

**Usage:**
```bash
whitespace-stego encode -m "message" -c "carrier" -o output.txt
whitespace-stego decode -c "encoded_text" -o decoded.txt
whitespace-stego analyze -t "text_to_analyze"
whitespace-stego extract -c "encoded_text" -o output_dir
```

**Commands:**
- `encode`: Encode a message into carrier text
- `decode`: Decode a message from carrier text
- `analyze`: Analyze text for encoded messages
- `extract`: Extract encoded message and remaining carrier

**Options:**
- `-m, --message`: Inline message
- `-f, --message-file`: Message file
- `-c, --carrier`: Inline carrier
- `-F, --carrier-file`: Carrier file
- `-o, --output`: Output file (or `-` for stdout)
- `-p, --password`: Password
- `-i, --interactive`: Interactive mode
- `--verbose`: Verbose logging
- `--quiet`: Quiet mode
- `--progress`: Show progress indicators

## C API

### Core Functions

#### `bool whitespace_stego_encode(const char* message, const char* carrier, const char* password, char** result)`

Encodes a message into carrier text.

**Parameters:**
- `message`: The secret message to hide
- `carrier`: The carrier text where the message will be hidden
- `password`: Optional password for encryption (can be NULL)
- `result`: Pointer to store the encoded result

**Returns:**
- `bool`: `true` on success, `false` on failure

**Example:**
```c
#include "whitespace_stego.h"

char* result;
if (whitespace_stego_encode("Secret", "Hello world!", "password", &result)) {
    printf("Encoded: %s\n", result);
    whitespace_stego_free(result);
}
```

#### `bool whitespace_stego_decode(const char* carrier, const char* password, char** result)`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier`: The carrier text containing the hidden message
- `password`: Optional password for decryption (can be NULL)
- `result`: Pointer to store the decoded result

**Returns:**
- `bool`: `true` on success, `false` on failure

**Example:**
```c
#include "whitespace_stego.h"

char* result;
if (whitespace_stego_decode(encoded_text, "password", &result)) {
    printf("Decoded: %s\n", result);
    whitespace_stego_free(result);
}
```

#### `void whitespace_stego_free(char* ptr)`

Frees memory allocated by the C API.

**Parameters:**
- `ptr`: Pointer to memory allocated by whitespace_stego functions

### CLI Interface

#### `whitespace-stego-c`

Main CLI entry point for C implementation.

**Usage:**
```bash
whitespace-stego-c encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt
```

**Options:**
- `--message-file`: File containing message to encode
- `--carrier-file`: File containing carrier text
- `--output`: Output file
- `--password`: Password for encryption/decryption

#### `whitespace-stego-py`

Standalone Python CLI (PyInstaller build).

**Usage:**
```bash
whitespace-stego-py encode --message "Secret" --carrier "text" --output encoded.txt
whitespace-stego-py decode --carrier-file encoded.txt --output decoded.txt
```

**Options:**
- Same as Python CLI above
- **Self-contained:** No Python installation required
- **All backends:** Python, Rust, and C backends included

## WebAssembly API

### JavaScript Interface

#### `whitespace_stego_wasi.encode(message, carrier, password)`

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
const encoded = encode("Secret message", "Hello world!", "password");
console.log(encoded);
```

#### `whitespace_stego_wasi.decode(carrier, password)`

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
const message = decode(encoded_text, "password");
console.log(message);
```

## Go API

### Core Functions

#### `stego.Encode(message, carrier, password)`

Encodes a message into carrier text.

**Parameters:**
- `message` (string): The secret message to hide
- `carrier` (string): The carrier text where the message will be hidden
- `password` (string): Optional password for encryption

**Returns:**
- `string`: The encoded carrier text
- `error`: Error if encoding fails

**Example:**
```go
package main

import (
    "fmt"
    "whitespace-stego-go/src/stego"
)

func main() {
    encoded, err := stego.Encode("Secret message", "Hello world!", "password")
    if err != nil {
        panic(err)
    }
    fmt.Println(encoded)
}
```

#### `stego.Decode(carrier, password)`

Decodes a hidden message from carrier text.

**Parameters:**
- `carrier` (string): The carrier text containing the hidden message
- `password` (string): Optional password for decryption

**Returns:**
- `string`: The decoded message
- `error`: Error if decoding fails

**Example:**
```go
package main

import (
    "fmt"
    "whitespace-stego-go/src/stego"
)

func main() {
    messages, err := stego.Decode(encoded_text, "password")
    if err != nil {
        panic(err)
    }
    // Go returns a slice of strings (multiple messages)
    for _, message := range messages {
        fmt.Println(message)
    }
}
```

### CLI Interface

#### `whitespace-stego-go`

Main CLI entry point for Go implementation.

**Usage:**
```bash
whitespace-stego-go encode -m "message" -cf carrier.txt -o output.txt
whitespace-stego-go decode -cf encoded.txt -o decoded.txt
```

**Options:**
- `-m, -message`: Message to encode (mutually exclusive with -mf/-message-file)
- `-mf, -message-file`: Message file path (mutually exclusive with -m/-message)
- `-cf, -carrier-file`: Carrier file path
- `-o, -output`: Output file path (default: stdout)
- `-p, -password`: Password for encryption/decryption

## Cross-Language Compatibility

All implementations are designed to be cross-compatible. You can encode a message in Python and decode it in Rust, or encode in C and decode in Go. The encoding format is consistent across all language implementations.

### Unicode Support

All implementations support full Unicode text, including:
- Multi-byte characters (UTF-8)
- Emojis and symbols
- Right-to-left languages
- Combining characters

### Encryption Compatibility

Password-protected messages are compatible across all implementations using the same Fernet encryption standard.

## Performance Characteristics

| Implementation | Encoding Speed | Decoding Speed | Memory Usage |
|----------------|----------------|----------------|--------------|
| Rust           | Very Fast      | Very Fast      | Low          |
| C              | Fast           | Fast           | Very Low     |
| Python         | Medium         | Medium         | Medium       |
| Go             | Fast           | Fast           | Low          |
| WebAssembly    | Medium         | Medium         | Low          |

## Error Handling

All implementations provide consistent error handling:

- **Empty messages**: Rejected with appropriate error
- **Invalid carriers**: Clear error messages
- **Wrong passwords**: Cryptographic errors
- **Malformed data**: Graceful degradation with error reporting
- **Missing dependencies**: Clear installation instructions 