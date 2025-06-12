# Design Specification: `whitespace_stego_rs` Command Line Tool

---

## 🎯 Purpose

To create a standalone **Rust binary CLI tool** named `whitespace_stego_rs` that mirrors the functionality and interface of the existing Python CLI tool `whitespace_stego`.

The Rust CLI must use the same core logic and library shared with the PyO3 module to ensure consistent behavior and full round-trip compatibility.

---

## 🏗️ Binary Name

```
whitespace_stego_rs
```

---

## 📁 Directory Structure

```
rust_backend/
├── src/
│   ├── main.rs           # CLI entrypoint using `clap`
│   ├── lib.rs            # Core logic exposed to both CLI and PyO3
│   ├── encoder.rs        # Encoding logic
│   ├── decoder.rs        # Decoding logic
│   ├── utils.rs          # Utility functions
│   └── cli.rs            # Optionally, subcommand dispatcher
├── Cargo.toml
```

---

## 🔧 CLI Syntax

```
USAGE:
    whitespace_stego_rs encode -m <MESSAGE> -c <CARRIER> -o <OUTFILE>
    whitespace_stego_rs encode -m <MESSAGE> -o <OUTFILE>
    whitespace_stego_rs encode -m <MESSAGE> --carrier-file <FILE> -o <OUTFILE>

    whitespace_stego_rs decode -i <INFILE>
```

### ✅ Arguments

| Argument        | Long Form         | Required | Description                              |
|----------------|-------------------|----------|------------------------------------------|
| `-m`           | `--message`       | Yes (encode) | Secret message to hide                   |
| `-c`           | `--carrier`       | No       | Carrier text                             |
| `--carrier-file` |                  | No       | File containing carrier content          |
| `-o`           | `--output`        | Yes (encode) | File to write stego message             |
| `-i`           | `--input`         | Yes (decode) | Input file with hidden message         |
| `-p`           | `--password`      | No       | Optional password for encryption         |

---

## 🔁 Example Roundtrip

```
$ whitespace_stego encode -m "Hello World" -c "Carrier" -o secret.txt
$ whitespace_stego_rs decode -i secret.txt
Hello World
```

---

## 📦 Requirements

- Use [`clap`](https://crates.io/crates/clap) crate for argument parsing
- Use shared logic from `lib.rs` (also used in PyO3)
- Ensure I/O supports both UTF-8 and extended Unicode characters
- Error handling must provide user-friendly CLI messages
- Output should match Python's exactly, including whitespace formatting and newline behavior

---

## 🧪 Testing Criteria

- CLI encodes and decodes messages exactly like Python CLI
- Rust CLI can decode messages created by Python CLI and vice versa
- Supports all encoding targets:
  - Plain string carrier
  - Carrier from file
  - Zero-length carrier
- Supports all message types:
  - ASCII
  - Unicode
  - Emojis
- Respects optional password flag
- Input/output is validated and properly escaped
- Binary `whitespace_stego_rs` is buildable via `cargo build --release`

---

## 🛠️ Build Instructions

```bash
cd rust_backend
cargo build --release
./target/release/whitespace_stego_rs encode -m "Hidden" -c "Visible" -o out.txt
```

---

## ✅ Completion Criteria

- `whitespace_stego_rs` is installable via Cargo
- Produces output that decodes identically to Python implementation
- Command-line argument interface matches Python CLI
- Passes round-trip and cross-implementation tests
