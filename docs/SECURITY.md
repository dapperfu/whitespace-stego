# Security Notes

## Password Protection
- Optional password encryption (Fernet/AES-128) in Python, Rust, C, and Go backends
- Use `--password` in CLI or `password` argument in API
- Password required to decode encrypted messages
- WASM/browser version does not support password protection (for simplicity)

## Steganographic Security
- Messages are hidden using zero-width Unicode characters
- No metadata or visible markers in carrier text
- Detection is possible by analyzing Unicode character patterns
- Unicode normalization and emoji support across all backends

## Cross-compatibility
- Encoded messages can be decoded by any backend (Python, Rust, C, Go, WASM)
- No backend-specific metadata
- Password-protected messages are compatible across all implementations

## Recommendations
- Use strong, unique passwords for sensitive messages
- Be aware that steganography hides, but does not encrypt, unless password is used
- For high-security use, combine with other encryption tools
- Test cross-compatibility before using in production workflows

---

For more, see [Usage Guide](USAGE.md) and [Testing & Quality Assurance](TESTING.md). 