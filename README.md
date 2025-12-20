# whitespace-stego

![Logo](39e228c0-fefd-4bc1-82bf-fe581329754b.png)

**Hide secrets in plain sight using invisible Unicode characters!** 🕵️

🌐 **[Try the live demo on GitHub Pages](https://whitespace-stego.github.io/whitespace-stego/)** - Encode and decode messages directly in your browser!

Ever wanted to send a message that looks like normal text but actually contains hidden data? Well, now you can! This project implements whitespace steganography across **7 different programming languages** - because why choose one when you can have them all?

## What is this?

`whitespace-stego` encodes messages using invisible Unicode control characters that are completely undetectable when viewing text normally. Your secret message is hidden right there in the whitespace - but you'd never know it!

### How it works

1. Your message gets converted to UTF-8 → Base64 → binary bits
2. Each bit becomes an invisible Unicode character (zero-width space or zero-width non-joiner)
3. The whole thing gets wrapped with invisible markers
4. Optionally, it gets embedded in "carrier" text that looks completely normal

The result? Text that looks identical to normal text, but contains your hidden message! 🎭

## Implementations

We've got implementations in:
- 🐍 **Python** - Easy to use, great for scripting
- 🦀 **Rust** - Fast and safe
- 🌐 **Rust-WASM** - For the web (both wasm32-unknown-unknown and wasm32-wasi)
- 🔧 **C** - Classic, manual memory management
- 🐹 **Go** - Simple and idiomatic
- ⚡ **C++** - Object-oriented with RAII
- 💻 **x86_64 Assembly** - Because why not?

All implementations are **fully cross-compatible** - encode with Python, decode with Rust, mix and match however you want!

## Quick Start

### Python

```bash
cd python
pip install -e .
python -m whitespace_stego.cli encode "Hello, secret world!"
python -m whitespace_stego.cli decode "<encoded_output>"
```

### Rust

```bash
cd rust
cargo run --example cli -- encode "Hello, secret world!"
cargo run --example cli -- decode "<encoded_output>"
```

### Go

```bash
cd go
go run cmd/cli/main.go encode "Hello, secret world!"
go run cmd/cli/main.go decode "<encoded_output>"
```

### Web (WASM)

🌐 **[Try the live demo](https://whitespace-stego.github.io/whitespace-stego/)** - No installation needed!

Or run locally:

```bash
# First, install wasm-pack (if not already installed):
# curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
# Or: cargo install wasm-pack

# Build and serve the web demo locally
make serve
# Then open http://localhost:8000 in your browser

# Or publish to docs/ for GitHub Pages
make publish-docs
# Then commit and push the docs/ directory to enable GitHub Pages
```

## Building Everything

We've got a unified Makefile that builds all the things:

```bash
make build-all      # Build all implementations
make build-cli-all  # Build all CLI binaries to bin/ directory
make build-rust-wasm # Build WASM module for web
make serve          # Build WASM and serve web demo (http://localhost:8000)
make publish-docs   # Build WASM and publish to docs/ for GitHub Pages
make test-all       # Run all tests
make verify-all     # Verify all builds work
make clean-all      # Clean up build artifacts
```

### Using the CLI Binaries

After running `make build-cli-all`, all CLI binaries are available in the `bin/` directory:

```bash
./bin/whitespace-stego-python encode "Hello, secret world!"
./bin/whitespace-stego-c encode "Hello, secret world!"
./bin/whitespace-stego-rust encode "Hello, secret world!"
./bin/whitespace-stego-go encode "Hello, secret world!"
./bin/whitespace-stego-cpp encode "Hello, secret world!"
```

**Note:** The Python binary requires PyInstaller to be installed. If it's not available, the build will skip it but other binaries will still be built.

## Testing

Cross-language compatibility is tested to ensure any message encoded by one language can be decoded by any other:

```bash
./tests/test_runner.sh              # Run all tests
python3 tests/cross_lang_test.py    # Cross-language compatibility tests
```

## Project Structure

```
whitespace-stego/
├── bin/             # CLI binaries (after make build-cli-all)
│   ├── whitespace-stego-python
│   ├── whitespace-stego-c
│   ├── whitespace-stego-rust
│   ├── whitespace-stego-go
│   └── whitespace-stego-cpp
├── python/          # Python implementation
├── rust/            # Rust implementation
├── rust-wasm/       # WASM bindings
├── c/               # C implementation
├── go/              # Go implementation
├── cpp/             # C++ implementation
├── asm/             # x86_64 assembly
├── tests/           # Cross-language test infrastructure
├── benchmarks/      # Performance benchmarks
└── profilers/       # Profiling tools
```

## Unicode Characters Used

- **U+2060** (Word Joiner) - Start marker
- **U+2063** (Invisible Separator) - End marker
- **U+200B** (Zero Width Space) - Binary bit 0
- **U+200C** (Zero Width Non-Joiner) - Binary bit 1

All completely invisible when rendered! 👻

## Requirements

See `requirements.sdoc` for the full specification. The algorithm is language-agnostic and follows RFC 4648 Base64 encoding.

## License

MIT License - hide secrets freely! 🎉

---

**Remember:** This is for fun and learning. Don't use this for actual security-critical applications. The invisible characters can be detected if someone knows what to look for!
