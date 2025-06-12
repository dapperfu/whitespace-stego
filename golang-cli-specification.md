# 🦫 Go CLI Specification for `whitespace-stego`

## 🎯 Objective

Implement a feature-complete CLI for `whitespace-stego` in Go that matches functionality provided by the Rust, Python, and C CLI versions. The Go CLI must support full encode/decode functionality, password handling, and interoperability testing with the Python CLI.

---

## 📁 Folder Structure

```
whitespace-stego/
├── go_cli/
│   ├── cmd/
│   │   └── root.go         # Cobra command entry
│   ├── internal/
│   │   ├── encoder.go      # Encode logic
│   │   ├── decoder.go      # Decode logic
│   │   ├── crypto.go       # Optional password-based encryption
│   │   └── utils.go        # Zero-width mapping helpers
│   ├── main.go
│   ├── go.mod
│   └── go.sum
```

---

## 🛠 Features to Implement

- `encode` subcommand
  - Accepts message, optional password, and optional carrier string
- `decode` subcommand
  - Accepts stego text and optional password
- Input/output via stdin/stdout and file flags
- Encode messages using zero-width characters (`U+200B`, `U+200C`)
- Delimit payload using `U+2060` (start) and `U+2061` (end)

---

## 🔐 Optional: Password Support

Use Go standard libraries or well-tested cryptography libraries for:

- Symmetric encryption (AES-256 in GCM or CBC)
- Password-based key derivation (scrypt or PBKDF2)

---

## 🧪 Testing Strategy

### Go Unit Tests

- Located in `go_cli/internal/*_test.go`
- Test encoding/decoding with:
  - ASCII, Unicode, and emoji messages
  - Optional passwords
  - Edge case carrier lengths (0, 1, >1)

### Python ↔ Go Interop Tests

Located in `tests/test_go_cli_roundtrip.py`:

- Encode with Go CLI, decode with Python CLI
- Encode with Python CLI, decode with Go CLI
- Use subprocesses to call both CLIs
- Assert input == output in all cases

---

## ✅ Completion Criteria

- `go run main.go encode ...` and `decode` commands work with expected flags
- CLI output matches Python CLI behavior
- All unit and interop tests pass
- CI integration via `make go-cli`

---

## 🧱 Makefile Additions

Append to existing Makefile:

```make
go-cli:
	cd go_cli && go build -o ../bin/whitespace-stego-go

test-go-cli:
	pytest tests/test_go_cli_roundtrip.py
```

Ensure `go.mod` is initialized inside `go_cli/` and required modules are added.

---

## 🔄 Example CLI Usage

```bash
# Encode
echo "hello world" | ./bin/whitespace-stego-go encode --password=secret > out.txt

# Decode
cat out.txt | ./bin/whitespace-stego-go decode --password=secret
```

---

## 🚧 Dependencies

- [cobra](https://github.com/spf13/cobra) for CLI scaffolding
- [spf13/viper](https://github.com/spf13/viper) (optional) for future config management
- Standard Go `crypto` for encryption support
