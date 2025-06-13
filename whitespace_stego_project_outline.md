# 📦 Project Outline: `whitespace-stego`

## 🧠 Purpose

A zero-width Unicode steganography toolkit that hides base64-encoded (and optionally encrypted) messages invisibly within a carrier text. The system encodes binary data into invisible whitespace characters and embeds them between start and stop delimiters in any string.

---

## ⚙️ How It Works

### 1. **Password Protection (Optional)**

- If a password is provided:
  - Use AES-256 encryption with PBKDF2 or scrypt-derived keys.
  - The encrypted message is base64-encoded.
- If no password:
  - The message is base64-encoded directly.

### 2. **Base64 Encoding**

- Ensures the binary representation uses ASCII-safe characters.

### 3. **Zero-width Binary Encoding**

- `U+200B` (Zero Width Space) → `0`
- `U+200C` (Zero Width Non-Joiner) → `1`

Each 8-bit character becomes 8 zero-width characters.

### 4. **Framing**

- `U+2060` (Word Joiner) → Start of payload (`<`)
- `U+2061` (Function Application) → End of payload (`>`)

The binary message is wrapped in delimiters, e.g., `<|>`, where `|` is the encoded binary data.

### 5. **Embedding in Carrier**

| Carrier Length | Output Example          |
|----------------|--------------------------|
| 0              | `<|>`                    |
| 1              | `A<|>`                   |
| 2+             | `A<|>BCDEFG...`          |

Payload is inserted after the first character of the carrier text.

---

## 🧩 Project Structure

### 1. **Pure Python Backend**

- `whitespace_stego/core.py`
- Handles:
  - Encryption/decryption
  - Encoding/decoding to zero-width
  - Framing and unframing

### 2. **Rust Backend with PyO3**

- Directory: `rust_py_backend/`
- PyO3-exposed functions:
  - `encode_rs()`
  - `decode_rs()`

### 3. **Pure Rust Backend**

- Directory: `rust_backend/`
- CLI via `clap`
- Standalone binary: `whitespace_stego_rs`

---

## 🖥 CLI Interfaces

### Python CLI

- CLI Tool: `whitespace_stego_py`
- Uses: `click`
- Backend: Selectable (`--backend python` or `--backend rust`)
- Example:
  ```bash
  whitespace_stego_py encode -m "Message" -c "Carrier" -p "Passwd" -o -
  whitespace_stego_py encode --backend rust -m "Message" -c "Carrier" -p "Passwd" -o -
  ```

- Flags:
  - `-m`, `--message`
  - `-mf`, `--message-file`
  - `-c`, `--carrier`
  - `-cf`, `--carrier-file`
  - `-p`, `--password`
  - `-pf`, `--password-file`
  - `-o`, `--output`

### Rust CLI

- CLI Tool: `whitespace_stego_rs`
- Example:
  ```bash
  whitespace_stego_rs encode -m "Message" -c "Carrier" -p "Passwd" -o -
  ```

---

## 📁 File Layout

```
whitespace-stego/
├── whitespace_stego/           # Python source
│   ├── __init__.py
│   ├── cli.py                  # Click CLI
│   ├── core.py                 # Python backend logic
│   └── rust_bridge.py          # Rust bindings
├── rust_py_backend/            # PyO3-based Rust bindings
│   ├── Cargo.toml
│   └── src/
├── rust_backend/               # Pure Rust CLI
│   ├── Cargo.toml
│   └── src/
├── tests/
│   ├── test_core.py
│   └── test_cross_impl.py
├── pyproject.toml
├── Makefile
└── README.md
```

---

## 🛠 Makefile

### Python Build & Test

```make
venv:
	python3 -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -e .[dev]

test:
	.venv/bin/pytest --html=report.html --cov=whitespace_stego

install: venv

run:
	.venv/bin/whitespace_stego_py
```

### Rust Build

```make
rust-py:
	cd rust_py_backend && maturin develop

rust-cli:
	cd rust_backend && cargo build --release

rust-test:
	cd rust_backend && cargo test
```

---

## 🧪 Testing Requirements

- All Python modules tested with `pytest`, `pytest-html`, `pytest-cov`
- CLI tests ensure `encode` → `decode` roundtrip across:
  - Python CLI → Python decode
  - Python CLI → Rust decode
  - Rust CLI → Python decode
- Files: `tests/test_cross_impl.py`, `tests/test_core.py`

---

## 📦 pyproject.toml Requirements

```toml
[project]
name = "whitespace-stego"
version = "0.1.0"
description = "Zero-width whitespace steganography"
dependencies = [
  "click",
  "cryptography"
]

[project.optional-dependencies]
dev = [
  "pytest",
  "pytest-html",
  "pytest-cov"
]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

Let me know if you want this zipped into a starter project with scaffold code.
