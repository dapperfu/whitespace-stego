# Security Notes

## Password Protection
- Optional password encryption (Fernet/AES-128) in Python, Rust, and C backends
- Use `--password` in CLI or `password` argument in API
- Password required to decode encrypted messages

## Steganographic Security
- Messages are hidden using zero-width Unicode characters
- No metadata or visible markers in carrier text
- Detection is possible by analyzing Unicode character patterns
- WASM/browser version does not support password protection (for simplicity)

## Cross-compatibility
- Encoded messages can be decoded by any backend (Python, Rust, C, WASM)
- No backend-specific metadata

## Recommendations
- Use strong, unique passwords for sensitive messages
- Be aware that steganography hides, but does not encrypt, unless password is used
- For high-security use, combine with other encryption tools

---

For more, see [Usage Guide](USAGE.md) and [Testing & Quality Assurance](TESTING.md). 