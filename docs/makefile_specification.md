# Makefile Specification for Whitespace Steganography Project

## Overview

This Makefile manages the development environment and build process for Python, Rust, Go, and C components of the project. It handles virtual environments, installation, testing, and compilation, ensuring consistent development workflows across all implementations, including Docker and WASM.

---

## Targets

### `help`
- Lists all available Makefile targets with a short description.

---

### `venv`
- Creates a Python virtual environment in a directory called `.venv`.
- Command: `python3 -m venv .venv`

---

### `install`
- Activates the virtual environment.
- Installs the Python module in **editable mode**:
  ```bash
  .venv/bin/pip install -e .
  ```
- Installs test and development dependencies from `requirements-dev.txt`.

---

### `test`
- Runs tests using `pytest` inside the virtual environment.
- Command: `.venv/bin/pytest`

---

### `test-all`
- Runs all tests for Python, Rust, Go, C, WASM, and cross-implementation.
- Command: `python scripts/run_coverage.py --all`

---

### `maturin-develop`
- Compiles and installs the PyO3 Rust extension into the Python environment.
- Command: `maturin develop`

---

### `maturin-build`
- Builds a Python wheel from the Rust extension.
- Command: `maturin build --release`

---

### `cargo-build`
- Builds the pure Rust CLI binary.
- Command: `cargo build --release --manifest-path whitespace-stego-cli/Cargo.toml`

---

### `cargo-clean`
- Cleans up Rust build artifacts.
- Command: `cargo clean`

---

### `go`
- Builds the Go CLI binary.
- Command: `cd go/src && go build -o ../../bin/whitespace-stego-go main.go`

---

### `c`
- Builds the C CLI binary.
- Command: `cd c && make`

---

### `wasi-web`
- Builds the WebAssembly UI and package.
- Command: `cd wasi && ./build.sh`

---

### `python-binary-docker`
- Builds a portable Python binary using Docker.
- Command: `docker build -t whitespace-stego-py-builder .`

---

### `all-binaries-docker`
- Builds all CLI binaries (Python, Rust, C, Go) using Docker.
- Command: `make all-binaries-docker`

---

### `coverage`
- Runs all tests with coverage reporting for all implementations.
- Command: `make coverage`

---

### `clean`
- Removes:
  - `.venv/`
  - `target/`
  - `build/`
  - `dist/`
  - `*.egg-info/` directories
  - `bin/` (compiled binaries)

---

## Assumptions

- `maturin`, `cargo`, `go`, and `docker` are installed and available in the system's PATH.
- `requirements-dev.txt` includes all necessary test dependencies.
- Python 3 is available as `python3`.
- C compiler (GCC/Clang) is available for C targets.
- WASM build tools are available for `wasi-web` target.
