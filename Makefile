VENV?=.venv
.PHONY: help venv install test coverage maturin-develop maturin-build cargo-build cargo-clean clean format rust c wasi-web test-wasm test-wasm-only test-all git-clean
# Default target
help:
	@echo "Available targets:"
	@echo "  help            - Show this help message"
	@echo "  venv            - Create Python virtual environment"
	@echo "  install         - Install Python package and dependencies"
	@echo "  test            - Run tests using pytest"
	@echo "  test-wasm       - Run WASM website Selenium tests"
	@echo "  test-wasm-only  - Run only WASM website Selenium tests"
	@echo "  test-all        - Run all tests (including WASM website tests)"
	@echo "  coverage        - Run tests with coverage reporting"
	@echo "  maturin-develop - Install Rust extension in development mode"
	@echo "  maturin-build   - Build Python wheel from Rust extension"
	@echo "  cargo-build     - Build pure Rust CLI binary"
	@echo "  cargo-clean     - Clean Rust build artifacts"
	@echo "  clean           - Remove all build artifacts and virtual environment"
	@echo "  format          - Format code (Rust and Python)"
	@echo "  rust            - Build Rust CLI in release mode and copy to top-level directory"
	@echo "  c               - Build C CLI in release mode and copy to top-level directory"
	@echo "  wasi-web        - Build WASI web app and serve it at http://localhost:8000"
	@echo "  git-clean       - Clean all untracked files and directories (use with caution)"

# Build pure Rust CLI binary
cargo-build:
	cargo build --release

# Clean Rust build artifacts
cargo-clean:
	cargo clean

# Remove all build artifacts and virtual environment
clean:
	rm -rf ${VENV}
	rm -rf whitespace-stego-backend/target
	rm -rf whitespace-stego-backend/*.egg-info
	rm -rf whitespace-stego-backend/dist
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build
	rm -f whitespace-stego-rs
	rm -f whitespace-stego-c
	rm -rf htmlcov
	rm -f coverage.xml
	rm -f .coverage*
	rm -f test_*_encoded.txt test_*_decoded.txt
	rm -f encoded*.txt
	cargo clean

# Run tests with coverage reporting
coverage: venv maturin-develop rust
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pytest --cov=whitespace_stego --cov=whitespace_stego_backend --cov-report=term-missing --cov-report=html --cov-report=xml

# Format code (Rust and Python)
format: .venv/bin/ruff
	.venv/bin/ruff format .

# Install Python package and dependencies
install: venv
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt

# Install Rust extension in development mode
VENV_ABS:=$(abspath ${VENV})

maturin-develop: ${VENV}/bin/maturin
	PATH="${VENV_ABS}/bin:$$PATH" PYTHON_SYS_EXECUTABLE="${VENV_ABS}/bin/python3" cd whitespace-stego-backend && ../${VENV}/bin/maturin develop

# Build Python wheel from Rust extension
maturin-build: ${VENV}/bin/maturin
	PATH="${VENV_ABS}/bin:$$PATH" PYTHON_SYS_EXECUTABLE="${VENV_ABS}/bin/python3" cd whitespace-stego-backend && ../${VENV}/bin/maturin build --release

# Build Rust CLI in release mode and copy to top-level directory
rust:
	cargo build --release --manifest-path rust/Cargo.toml --target-dir rust/target
	cp rust/target/release/whitespace-stego-rs ./whitespace-stego-rs

# Build C CLI in release mode and copy to top-level directory
c:
	cd c && make clean && make
	cp c/bin/whitespace-stego-c ./whitespace-stego-c 

# Run standard tests (excluding WASM website tests)
test: venv maturin-develop rust
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt
	.venv/bin/pytest -k "not test_wasm_website"

# Run WASM website Selenium tests
test-wasm: venv wasi-web
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt
	@echo "Starting WASM web server in background..."
	@cd wasi/pkg && python3 -m http.server 8000 > /dev/null 2>&1 & echo $$! > /tmp/wasm_server.pid
	@sleep 3
	@echo "Running WASM website Selenium tests..."
	@PYTHONPATH=. .venv/bin/pytest tests/test_wasm_website.py -v --disable-warnings
	@echo "Stopping WASM web server..."
	@kill $$(cat /tmp/wasm_server.pid) 2>/dev/null || true
	@rm -f /tmp/wasm_server.pid

# Run only WASM website Selenium tests (assumes server is already running)
test-wasm-only: venv
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements-dev.txt
	@echo "Running WASM website Selenium tests..."
	@PYTHONPATH=. .venv/bin/pytest tests/test_wasm_website.py -v --disable-warnings

# Run all tests (including WASM website tests)
test-all: test test-wasm

# Create Python virtual environment
venv:
	python3 -m venv ${VENV}

.venv/bin/ruff: venv
	.venv/bin/pip install ruff

.venv/bin/maturin: venv
	.venv/bin/pip install maturin

# Build WASI web app and serve it with Python
wasi-web:
	cd wasi && ./build.sh
	cd wasi/pkg && python3 -m http.server 8000

# Clean all untracked files and directories (use with caution)
git-clean:
	@echo "Cleaning all untracked files and directories..."
	@echo "This will remove:"
	@echo "  - All .coverage.* files"
	@echo "  - All untracked files and directories"
	@echo "  - All ignored files"
	@echo "Are you sure? [y/N]"
	@read -p "" confirm && [ "$$confirm" = "y" ] || exit 1
	git clean -xfd 