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
MAKEFILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))/

.PHONY: help venv test all clean rust c go python-binary python-binary-docker install maturin-develop wasi wasi-web cov-go cov-rust cov-c cov-python coverage coverage-xml

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
	@echo "  cov-go          - Run Go tests with coverage"
	@echo "  cov-rust        - Run Rust tests with coverage"
	@echo "  cov-c           - Run C tests with coverage"
	@echo "  cov-python      - Run Python tests with coverage"
	@echo "  coverage        - Run coverage tests for all languages"
	@echo "  coverage-xml    - Generate consolidated Cobertura XML reports"
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
	rm -rf go/coverage.out go/coverage.html go/coverage.txt
	rm -rf c/coverage
	rm -rf rust/target/coverage
	rm -rf coverage-reports
	# Keep spec files for builds
	cargo clean

# Coverage targets
cov-go:
	@echo "🧪 Running Go tests with coverage..."
	cd go && go test -coverprofile=coverage.out -covermode=atomic ./src/stego
	cd go && go tool cover -func=coverage.out > coverage.txt
	cd go && go tool cover -html=coverage.out -o coverage.html
	@echo "📊 Go coverage report generated: go/coverage.html"
	@echo "📋 Go coverage summary: go/coverage.txt"

cov-rust:
	@echo "🧪 Running Rust tests with coverage..."
	cd rust && cargo tarpaulin --out Html --output-dir coverage
	cd rust && cargo tarpaulin --out Xml --output-dir coverage
	@echo "📊 Rust coverage report generated: rust/coverage/tarpaulin-report.html"

cov-c:
	@echo "🧪 Running C tests with coverage..."
	cd c && make install-unity
	cd c && make clean
	cd c && make test-coverage
	cd c && make coverage-report
	@echo "📊 C coverage report generated: c/coverage/html/index.html"

cov-python:
	@echo "🧪 Running Python tests with coverage..."
	${VENV}/bin/pytest --cov=whitespace_stego --cov=whitespace_stego_rust --cov-report=html:htmlcov --cov-report=term-missing --cov-report=xml:coverage.xml
	@echo "📊 Python coverage report generated: htmlcov/index.html"

# Run coverage for all languages
coverage: cov-go cov-rust cov-c cov-python
	@echo "🎉 All coverage reports generated!"
	@echo "📊 Reports available:"
	@echo "  Go: go/coverage.html"
	@echo "  Rust: rust/coverage/tarpaulin-report.html"
	@echo "  C: c/coverage/html/index.html"
	@echo "  Python: htmlcov/index.html"

# Generate consolidated Cobertura XML coverage report
coverage-xml: coverage
	@echo "📊 Generating consolidated Cobertura XML coverage report..."
	@mkdir -p coverage-reports
	# Python already generates coverage.xml
	@cp coverage.xml coverage-reports/python-coverage.xml
	# Convert Go coverage to Cobertura XML
	@if command -v gocover-cobertura >/dev/null 2>&1; then \
		gocover-cobertura < go/coverage.out > coverage-reports/go-coverage.xml; \
	else \
		echo "gocover-cobertura not available, skipping Go XML conversion"; \
	fi
	# Rust already generates XML
	@cp rust/coverage/tarpaulin.xml coverage-reports/rust-coverage.xml
	# C coverage to XML
	@cd c && gcovr --xml --output=../coverage-reports/c-coverage.xml
	@echo "📊 Consolidated coverage reports in coverage-reports/"
	@echo "  Python: coverage-reports/python-coverage.xml"
	@echo "  Go: coverage-reports/go-coverage.xml"
	@echo "  Rust: coverage-reports/rust-coverage.xml"
	@echo "  C: coverage-reports/c-coverage.xml" 