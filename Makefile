.PHONY: help venv install test maturin-develop maturin-build cargo-build cargo-clean clean format rust
m
# Default target
help:
	@echo "Available targets:"
	@echo "  help            - Show this help message"
	@echo "  venv            - Create Python virtual environment"
	@echo "  install         - Install Python package and dependencies"
	@echo "  test            - Run tests using pytest"
	@echo "  maturin-develop - Install Rust extension in development mode"
	@echo "  maturin-build   - Build Python wheel from Rust extension"
	@echo "  cargo-build     - Build pure Rust CLI binary"
	@echo "  cargo-clean     - Clean Rust build artifacts"
	@echo "  clean           - Remove all build artifacts and virtual environment"
	@echo "  format          - Format code (Rust and Python)"
	@echo "  rust            - Build Rust CLI in release mode and copy to top-level directory"

# Create Python virtual environment
venv:
	python3 -m venv .venv

# Install Python package and dependencies
install: venv
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt

# Run tests
.venv/bin/pytest: install

test: .venv/bin/pytest
	.venv/bin/pytest --workers 8

# Install Rust extension in development mode
maturin-develop:
	maturin develop

# Build Python wheel from Rust extension
maturin-build:
	maturin build --release

# Build pure Rust CLI binary
cargo-build:
	cargo build --release

# Clean Rust build artifacts
cargo-clean:
	cargo clean

# Remove all build artifacts and virtual environment
clean:
	rm -rf .venv/
	rm -rf target/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -f whitespace-stego-rs
	cargo clean

# Format code (Rust and Python)
format: .venv/bin/ruff
	.venv/bin/ruff format .

# ... existing code ...
.venv/bin/ruff: venv
	.venv/bin/pip install ruff

# ... existing code ...

# Build Rust CLI in release mode and copy to top-level directory
rust:
	cargo build --release --manifest-path rust/Cargo.toml --target-dir rust/target
	cp rust/target/release/whitespace-stego-rs ./whitespace-stego-rs 