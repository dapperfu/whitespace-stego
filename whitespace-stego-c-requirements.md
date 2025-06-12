# Design Requirements Document: `whitespace-stego-c`

---

## 🧭 Objective

Develop a feature-complete **C implementation** of the `whitespace-stego` steganographic encoding/decoding tool, matching the Python and Rust versions in both functionality and behavior.

The C codebase shall follow **MISRA-C** coding standards with all deviations explicitly documented. The project must be modular (multiple `.c` and `.h` files), testable, and maintainable.

---

## 📁 Directory Structure

The C implementation will live in its own subdirectory:

```
whitespace-stego/
├── c_backend/
│   ├── src/
│   │   ├── main.c
│   │   ├── encode.c
│   │   ├── decode.c
│   │   ├── utils.c
│   │   ├── encode.h
│   │   ├── decode.h
│   │   ├── utils.h
│   ├── tests/
│   │   ├── test_main.c
│   ├── Makefile
```

---

## 📦 Build System

### Compiler

- Use `clang` for strict standards compliance and static analysis tooling.

### Makefile Targets

| Target        | Description                                  |
|---------------|----------------------------------------------|
| `make`        | Build the binary using `clang`               |
| `make test`   | Build and run all unit tests                 |
| `make clean`  | Remove all build artifacts                   |

---

## 🧪 Testing Requirements

- Tests must cover:
  - ASCII, Unicode, and emoji messages
  - All carrier sizes (zero, one, many)
  - Roundtrip encoding/decoding
  - Password protection edge cases (empty, NULL, set)
  - Cross-validation with reference output from Python or Rust
- Use assertions and predictable test vectors

---

## 🛠 Functional Requirements

- The binary shall produce exactly the same output as `whitespace_stego` and `whitespace_stego_rs`.
- Functions must handle:
  - Base64 encoding/decoding
  - Zero-width whitespace mapping
  - Start/stop character framing
  - Carrier insertion logic
  - Optional password-based XOR or AES encryption (if added)

### CLI Usage

```
$ ./whitespace_stego_c encode -m "Hello" -c "Text" -o out.txt
$ ./whitespace_stego_c decode -i out.txt
```

| Flag           | Description                                  |
|----------------|----------------------------------------------|
| `-m`           | Message to hide                              |
| `-c`           | Carrier string                               |
| `--carrier-file` | Read carrier from file                     |
| `-o`           | Output file                                  |
| `-i`           | Input file to decode                         |
| `-p`           | Optional password                            |

---

## 🧩 Module Breakdown

| File          | Responsibility                                 |
|---------------|------------------------------------------------|
| `main.c`      | CLI argument parsing, I/O                      |
| `encode.c/h`  | Encoding logic                                 |
| `decode.c/h`  | Decoding logic                                 |
| `utils.c/h`   | Zero-width mappings, base64, helper functions  |
| `test_main.c` | Tests using standard `assert()` or custom harness |

---

## 🔐 MISRA-C Compliance

- Code must comply with MISRA-C:2012
- Use `clang-tidy` and `cppcheck` for validation
- Any deviations from MISRA must be documented in comments like:
  ```c
  // MISRA Deviation: Rule 13.2 - Intentional use of logical short-circuit for validation
  ```

---

## ✅ Completion Criteria

- Compiles cleanly with `clang` and passes all tests
- All tests show 100% consistency with Python and Rust implementations
- MISRA-C compliance validated with documented deviations
- All functionality (carrier handling, roundtrip, unicode, password) implemented
- Readable, maintainable, modular C code

---

## 🔚 Final Note

This implementation is meant for performance, portability, and auditability. C allows full control and transparency of memory and logic, making it suitable for embedded or constrained environments where Python and Rust may be infeasible.
