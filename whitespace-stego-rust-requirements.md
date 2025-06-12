# **Design Requirements Document**
## Rust Backend Integration for `whitespace-stego`

---

### 📌 Objective

To add a Rust implementation of the core encoding/decoding logic to the existing Python project using PyO3, providing a high-performance backend while maintaining full interoperability with the Python codebase.

The Rust functions will mirror the Python interface and be exposed to Python via PyO3 using `_rs` suffixes (e.g., `encode_rs`, `decode_rs`).

---

## 📁 Directory Structure

The Rust implementation will live in a self-contained module directory within the Python project repo:

```
whitespace-stego/
├── rust_backend/
│   ├── Cargo.toml
│   └── src/
│       ├── lib.rs           # PyO3 bindings and core interface
│       ├── encoder.rs       # Zero-width encoding logic
│       ├── decoder.rs       # Zero-width decoding logic
│       └── utils.rs         # Shared helper functions
├── whitespace_stego/
│   └── rust_bridge.py       # Python interface to Rust functions
├── tests/
│   └── test_rust_bridge.py  # Round-trip compatibility tests
```

---

## 🦀 Rust Design Requirements

### Language & Tools
- Language: Rust 2021 Edition
- PyO3 crate for bindings
- Optional: `maturin` for building and packaging if CLI/CI integration is desired

### Core Functional Requirements

The Rust module shall expose the following functions with `_rs` suffixes to avoid naming collisions in Python:

| Python Function     | Rust Equivalent |
|---------------------|-----------------|
| `encode`            | `encode_rs`     |
| `decode`            | `decode_rs`     |
| `to_zero_width`     | `to_zero_width_rs` |
| `from_zero_width`   | `from_zero_width_rs` |
| `wrap_payload`      | `wrap_payload_rs` |
| `unwrap_payload`    | `unwrap_payload_rs` |

These shall be exposed via `#[pyfunction]` and registered in a `#[pymodule]`.

### Encoding/Decoding Behavior

- Identical to the Python version:
  - Use `U+200B` for `0`, `U+200C` for `1`
  - Wrap payload with `U+2060` (start) and `U+2061` (end)
  - Insert encoded string into carrier message at appropriate position

### Performance Target

- Aim to be 3x–10x faster than the pure Python implementation on medium-length messages (10KB+).
- Benchmark results optional but recommended.

---

## 🔄 Interoperability Requirements

### Python ↔ Rust Integration

- Rust functions must accept and return `str`-compatible Python types
- Encoding a message in Rust then decoding in Python must yield the original message
- Decoding a message encoded in Python using the Rust backend must also yield the original

---

## 🧪 Testing Strategy

### Rust Unit Tests
Each core module (`encoder.rs`, `decoder.rs`, `utils.rs`) shall include `#[cfg(test)]` unit tests to validate:

- Correct base64 → binary encoding
- Proper zero-width character substitution
- Accurate start/stop framing
- Full encode/decode roundtrip

### Python ↔ Rust Compatibility Tests
A pytest test file (`test_rust_bridge.py`) will validate:

- `encode` (Python) + `decode_rs` (Rust) roundtrip
- `encode_rs` (Rust) + `decode` (Python) roundtrip
- Cross-compatibility for:
  - ASCII
  - Unicode
  - Emojis
  - Password-protected messages (if encryption is ported to Rust)

---

## 🛠️ Build & Setup Instructions

### Rust Side
- `cargo build` for development
- `cargo test` for Rust-only tests

### Python Side
- Build Rust shared library via `maturin` or `setuptools-rust`
- Auto-detect `rust_backend` module in `rust_bridge.py`
- Fall back to Python implementation if Rust module fails to import

---

## 🚧 Future Considerations

- Optional: Add feature flag to select backend (`RUST_BACKEND=1`)
- Optional: Add benchmarking harness to compare Python vs Rust
- Optional: Expand Rust to handle encryption via RustCrypto if Python crypto is also ported

---

## ✅ Completion Criteria

- All Python-side unit tests pass with Rust backend
- Rust unit tests pass
- Roundtrip tests validate bidirectional compatibility
- Rust functions exposed cleanly with `_rs` suffix
- No degradation in Python-only behavior or packaging
