xdg-o # Whitespace Steganography Project Specification

## Overview

This project implements a steganography technique using zero-width Unicode whitespace characters. The encoder uses **four** distinct zero-width characters:

- **2 control characters**: denote the **start** and **end** of the hidden message.
- **2 data characters**: encode binary digits **0** and **1**.

Before binary encoding, the input message is **base64-encoded** to ensure consistent handling of Unicode characters. For example, the emoji 😀 becomes `8J+YgA==`.

## Encoding Rules

- **Zero-character carrier**: Return the whitespace-encoded message directly.
- **Non-zero carrier**: Embed the whitespace message **after the first character** of the carrier text.

## Deliverables

### Command-Line Interfaces

Three tools will be provided:

1. **Python CLI (pure)**:
   - `whitespace-stego` with `--backend python`

2. **Rust-backed Python CLI** (via PyO3 + maturin):
   - `whitespace-stego` with `--backend rust`

3. **Pure Rust CLI**:
   - `whitespace-stego-rs`

### CLI Arguments

- `-m/--message`, `-mf/--message-file`: Message input
- `-c/--carrier`, `-cf/--carrier-file`: Carrier input
- `-p/--password`, `-pf/--password-file`: Optional password protection
- `-o/--output`: Output location. `-o -` writes to stdout

### Examples

```bash
whitespace-stego encode --backend python --message "Hello" --carrier "Hi"
whitespace-stego encode --backend rust --message "Hello" --carrier "Hi"
whitespace-stego-rs encode --message "Hello" --carrier "Hi"
```

## Features

- Base64 encoding ensures proper Unicode handling
- Message can be embedded even in an empty carrier
- Password-based encryption (if provided)
- CLI and file-based I/O

## Testing

The Python implementation must include a comprehensive test suite using `pytest` and parameterization.

### Example Test

```python
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("password", PASSWORDS)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_stego_encode_decode(message: str, password: str | None, carrier: str) -> None:
    ...
```

## Notes

- Use secure encryption algorithms for password-protected encoding.
- Ensure consistent handling of emojis, multilingual text, and special characters.
- All implementations must be interoperable (e.g., encode in Python, decode in Rust).
