# Testing & Quality Assurance

## Test Strategy

- **Pytest suite:** 1300+ tests for all features
- **Cross-backend:** Encode/decode between Python, Rust, C, Go, WASM
- **CLI tests:** Python, Rust, C, and Go command-line interfaces
- **WebAssembly:** Browser-based tests for WASM UI
- **Jupyter notebooks:** Interactive, executable examples
- **Cross-implementation:** Round-trip and Unicode tests for all backends

## Running Tests

### All tests (recommended)
```bash
make test-all
```

### Pytest (parallelized)
```bash
make test
# or
python -m pytest -n auto --dist loadfile
```

### CLI shell tests
```bash
bash tests/test_cli_shell.sh
```

### WASM web tests
```bash
make test-wasm
```

### Individual implementation tests
```bash
python3 -m whitespace_stego.cli --help
./bin/whitespace-stego-c --help
./bin/whitespace-stego-rs --help
./bin/whitespace-stego-go --help
```

### Cross-implementation tests
```bash
python tests/test_20_cross_impl_roundtrip.py
python tests/test_21_unicode_cross_impl.py
python tests/test_22_comprehensive_encoding_identity.py
```

### Comprehensive Security & Edge Case Test Suite

The script `comprehensive_security_test_suite.py` provides a thorough, automated test suite covering:
- Edge cases (empty messages, single characters, very long messages)
- Security scenarios (malicious inputs, memory exhaustion attempts)
- Unicode and encoding edge cases
- Cross-implementation compatibility (C, C++, Go, Python core, Python CFFI, Python PyO3)
- Protocol robustness
- Performance under stress

**How to run:**
```bash
python3 comprehensive_security_test_suite.py
```

**Outputs:**
- `comprehensive_test_report.md` — Human-readable Markdown summary of all results
- `comprehensive_test_results.json` — Raw machine-readable results for further analysis

This suite is the most comprehensive way to validate all implementations and edge cases in one go. See the generated Markdown report for a summary and per-implementation breakdown.

## Test Coverage
- >95% for core functionality
- Unicode, emoji, password, error handling, and pipeline support
- Cross-compatibility: encode in one backend, decode in another (Python, Rust, C, Go, WASM)
- CLI, API, and web interface coverage

## Troubleshooting
- Ensure all dependencies are installed: `make install`
- Build all implementations: `make rust`, `make c`, `make go`
- For WASM: ensure port 8000 is free, run `make wasi-web`
- For detailed logs: add `--verbose` to CLI or `-v` to pytest
- Run failing tests individually for debugging
- For Go: ensure Go is installed and in PATH

## Continuous Integration
- All tests run in GitHub Actions on push/PR
- Parallelized pytest for fast feedback
- WASM, Go, and CLI tests included in CI
- Cross-implementation and Unicode tests included in CI

## Manual Testing
- See [examples/practical_use_cases.md](../examples/practical_use_cases.md) for manual test scenarios

---

For notebook-based testing and demos, see [Jupyter Notebooks Guide](NOTEBOOKS.md). 