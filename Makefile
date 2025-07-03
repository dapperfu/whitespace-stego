#
# Simplified Makefile for whitespace-stego project
#
# Core targets:
# - test: Run Python module tests
# - all: Build all binaries and place in bin/ folder
# - clean: Remove build artifacts
#
VENV?=.venv
BIN_DIR=bin
MAKEFILE_DIR:=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: help venv test all clean rust c go python-binary python-binary-docker install maturin-develop wasi wasi-web

# Default target
help:
	@echo "Available targets:"
	@echo "  help            - Show this help message"
	@echo "  venv            - Create Python virtual environment"
	@echo "  install         - Install Python package and dependencies"
	@echo "  test            - Run Python module tests"
	@echo "  all             - Build all binaries and place in bin/ folder"
	@echo "  rust            - Build Rust CLI binary"
	@echo "  c               - Build C CLI binary"
	@echo "  go              - Build Go CLI binary"
	@echo "  python-binary   - Build Python CLI binary (local)"
	@echo "  python-binary-docker - Build portable Python CLI binary (Docker)"
	@echo "  wasi            - Build WASM web interface"
	@echo "  wasi-web        - Build and serve WASM web interface"
	@echo "  clean           - Remove all build artifacts"

# Create Python virtual environment
venv:
	python3 -m venv ${VENV}

# Install Python package and dependencies
install: venv maturin-develop
	${VENV}/bin/pip install -e .
	${VENV}/bin/pip install -r requirements-dev.txt

# Install Rust extension in development mode
VENV_ABS:=$(abspath ${VENV})
maturin-develop: ${VENV}/bin/maturin
	PATH="${VENV_ABS}/bin:$$PATH" PYTHON_SYS_EXECUTABLE="${VENV_ABS}/bin/python3" cd whitespace-stego-python && ../${VENV}/bin/maturin develop

${VENV}/bin/maturin: venv
	${VENV}/bin/pip install maturin

# Run Python module tests
test: venv maturin-develop install
	@echo "Running Python module tests..."
	${VENV}/bin/pytest -v

# Build Rust CLI binary and Python extension
rust: venv
	@echo "Building Rust CLI binary and Python extension..."
	cargo build --release --manifest-path rust/Cargo.toml --target-dir rust/target
	cargo build --release --manifest-path whitespace-stego-python/Cargo.toml --target-dir whitespace-stego-python/target
	mkdir -p ${BIN_DIR}
	cp rust/target/release/whitespace-stego-rs ${BIN_DIR}/

# Build C CLI binary
c:
	@echo "Building C CLI binary..."
	cd c && make clean && make
	cd ..
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}c/bin/whitespace-stego-c ${BIN_DIR}/

# Build Go CLI binary
go:
	@echo "Building Go CLI binary..."
	cd go && make clean && make build
	cd ..
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}go/bin/whitespace-stego-go ${BIN_DIR}/

# Build Python CLI binary using PyInstaller (local build)
python-binary: venv install maturin-develop rust c
	@echo "Building Python CLI binary with PyInstaller..."
	${VENV}/bin/pip install pyinstaller
	${VENV}/bin/pyinstaller --clean ${MAKEFILE_DIR}/whitespace_stego.spec
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}dist/whitespace-stego-py ${BIN_DIR}/

# Build portable Python CLI binary using Docker
python-binary-docker:
	@echo "Building portable Python CLI binary using Docker..."
	docker build -t whitespace-stego-py-builder .
	mkdir -p dist ${BIN_DIR}
	docker run --rm --entrypoint cp -v "$(PWD)/dist:/out" whitespace-stego-py-builder /build/dist/whitespace-stego-py /out/
	cp ${MAKEFILE_DIR}dist/whitespace-stego-py ${BIN_DIR}/
	@echo "Testing the binary..."
	${BIN_DIR}/whitespace-stego-py --help

# Build all binaries and place in bin/ folder
all: rust c go python-binary-docker
	@echo "All binaries built and placed in ${BIN_DIR}/ folder:"
	@ls -la ${BIN_DIR}/

# Build WASM web interface
wasi:
	@echo "Building WASM web interface..."
	cd wasi && ./build.sh
	@echo "WASM build completed. Run 'make wasi-web' to serve it."

# Build and serve WASM web interface
wasi-web: wasi
	@echo "Starting web server on http://localhost:8000"
	@echo "Press Ctrl+C to stop the server"
	cd wasi/pkg && python3 -m http.server 8000

# Remove all build artifacts
clean:
	rm -rf ${VENV}
	rm -rf whitespace-stego-python/target
	rm -rf whitespace-stego-python/*.egg-info
	rm -rf whitespace-stego-python/dist
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build
	rm -f whitespace-stego-rs
	rm -f whitespace-stego-c
	rm -f whitespace-stego-go
	rm -f whitespace-stego-py
	rm -rf htmlcov
	rm -f coverage.xml
	rm -f .coverage*
	rm -f test_*_encoded.txt test_*_decoded.txt
	rm -f encoded*.txt
	rm -rf results
	rm -rf ${BIN_DIR}
	rm -rf wasi/pkg
	rm -rf wasi/target
	# Keep spec files for builds
	cargo clean 