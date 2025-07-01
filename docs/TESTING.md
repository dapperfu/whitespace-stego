# Testing & Quality Assurance

## Test Strategy

- **Pytest suite:** 1300+ tests for all features
- **Cross-backend:** Encode/decode between Python, Rust, C, WASM
- **CLI tests:** Python, Rust, and C command-line interfaces
- **WebAssembly:** Browser-based tests for WASM UI
- **Jupyter notebooks:** Interactive, executable examples

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
./whitespace-stego-c --help
./rust/target/release/whitespace-stego-rs --help
```

## Test Coverage
- >95% for core functionality
- Unicode, emoji, password, error handling, and pipeline support
- Cross-compatibility: encode in one backend, decode in another

## Troubleshooting
- Ensure all dependencies are installed: `make install`
- Build all implementations: `make rust`, `make c`
- For WASM: ensure port 8000 is free, run `make wasi-web`
- For detailed logs: add `--verbose` to CLI or `-v` to pytest
- Run failing tests individually for debugging

## Continuous Integration
- All tests run in GitHub Actions on push/PR
- Parallelized pytest for fast feedback
- WASM and CLI tests included in CI

## Manual Testing
- See [examples/practical_use_cases.md](../examples/practical_use_cases.md) for manual test scenarios

---

For notebook-based testing and demos, see [Jupyter Notebooks Guide](NOTEBOOKS.md). 