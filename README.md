![Project Logo](39e228c0-fefd-4bc1-82bf-fe581329754b.png)

# Whitespace Steganography

A modern, multi-language tool for hiding secret messages in text using zero-width Unicode characters. Supports Python, Rust, C, and WebAssembly (browser) backends.

---

## Features
- **Multi-language:** Python, Rust, C, and WASM implementations
- **CLI & Web UI:** Powerful command-line and browser interfaces
- **Unicode & Emoji:** Works with any text, any language
- **Password Protection:** Optional encryption for hidden messages
- **Cross-compatibility:** Encode in one backend, decode in another
- **Comprehensive Testing:** 1300+ tests, CI, and notebooks

---

## Quick Start

### 1. Install (Python, Rust, C, WASM)

```bash
git clone <repo-url>
cd whitespace-stego3
make install  # Python + Rust backend
make rust     # Rust CLI
make c        # C CLI
make wasi-web # WebAssembly (browser UI)
```

### 2. Encode/Decode (Python CLI)

```bash
# Encode
python3 -m whitespace_stego.cli encode --message "Secret" --carrier "Innocent text" --output encoded.txt
# Decode
python3 -m whitespace_stego.cli decode --carrier-file encoded.txt
```

### 3. Try the Web UI

```bash
make wasi-web
# Open http://localhost:8000 in your browser
```

---

## Documentation

- [Usage & CLI/API Examples](docs/USAGE.md)
- [Testing & Quality Assurance](docs/TESTING.md)
- [Jupyter Notebooks Guide](docs/NOTEBOOKS.md)
- [Security Notes](docs/SECURITY.md)
- [Contributing](docs/CONTRIBUTING.md)

---

## License
MIT License. See [LICENSE](LICENSE).