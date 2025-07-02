# Makefile Specification for Whitespace Steganography Project

## Overview

This Makefile manages the development environment and build process for both the Python and Rust components of the project. It handles virtual environments, installation, testing, and Rust compilation, ensuring consistent development workflows across all implementations.

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
- Command: `cargo build --release`

---

### `cargo-clean`
- Cleans up Rust build artifacts.
- Command: `cargo clean`

---

### `clean`
- Removes:
  - `.venv/`
  - `target/`
  - `build/`
  - `dist/`
  - `*.egg-info/` directories

---

## Assumptions

- `maturin` and `cargo` are installed and available in the system's PATH.
- `requirements-dev.txt` includes all necessary test dependencies.
- Python 3 is available as `python3`.
