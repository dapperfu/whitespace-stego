# 🧪 GitHub Actions CI Requirements Document

## 🎯 Objective

Set up a comprehensive GitHub Actions CI pipeline for `whitespace-stego` that performs the following across every push and pull request:

1. Build and test:
   - Python implementation
   - Python CLI via Typer
   - Rust implementation with PyO3 bindings
   - Rust CLI (if present)
   - C implementation with CLI (if present)
2. Verify roundtrip interoperability between Python and Rust implementations
3. Generate pytest HTML reports for Python tests

---

## 📂 Project Structure Expectations

```
whitespace-stego/
├── .github/workflows/
```

---

## 🧪 Testing Requirements by Component

### ✅ Python

- Use `python:3.10+`
- Run:
  - `make`
  - `make test`
- Generate `report.html` from pytest
- Upload report as an artifact

### ✅ Python CLI

- Validate CLI entry points
- Run `python -m whitespace_stego.cli.main encode`

### ✅ Rust (via PyO3)

- Build using `maturin` or `setuptools-rust`
- Run:
  - `cargo build`
  - `cargo test`
  - Python tests that call `_rs` functions

### ✅ Rust CLI (Optional)

- Build: `cargo build --manifest-path rust_cli/Cargo.toml`
- Test: `cargo test --manifest-path rust_cli/Cargo.toml`

### ✅ C CLI (Optional)

- Must include a `Makefile` for `c_cli/`
- Run `make -C c_cli`
- Execute CLI with sample input and verify output

---

## 📤 CI Output

- Upload `report.html` as artifact
- Upload `pytest.log` as artifact (optional)
- Fail fast on linting or build errors

---

## ✅ Completion Criteria

- Workflow must pass on clean checkout with no artifacts checked in
- All builds complete within 10 minutes
- Interoperability tests pass between Python ↔ Rust
