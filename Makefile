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
MAKEFILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY: all c clean coverage coverage-xml cov-c cov-go cov-python go help install maturin-develop rust test venv wasi wasi-web

# Default target
help:
	@echo "Available targets:"
	@echo "  all             - Build all binaries and place in bin/ folder"
	@echo "  c               - Build C CLI binary"
	@echo "  clean           - Remove all build artifacts"
	@echo "  coverage        - Run coverage tests for all languages"
	@echo "  coverage-xml    - Generate consolidated Cobertura XML reports"
	@echo "  cov-c           - Run C tests with coverage"
	@echo "  cov-go          - Run Go tests with coverage"
	@echo "  cov-python      - Run Python tests with coverage"
	@echo "  cov-rust        - Run Rust tests with coverage"
	@echo "  go              - Build Go CLI binary"
	@echo "  help            - Show this help message"
	@echo "  install         - Install Python package and dependencies"
	@echo "  maturin-develop - Install Rust extension in development mode"

	@echo "  rust            - Build Rust CLI binary"
	@echo "  test            - Run Python module tests"
	@echo "  venv            - Create Python virtual environment"
	@echo "  wasi            - Build WASM web interface"
	@echo "  wasi-web        - Build and serve WASM web interface"

# Build all binaries and place in bin/ folder
all: rust c go python-binary-docker
	@echo "All binaries built and placed in ${BIN_DIR}/ folder:"
	@ls -la ${BIN_DIR}/

# Build C CLI binary
c:
	@echo "Building C CLI binary..."
	cd implementations/c && make clean && make
	cd ../..
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}/implementations/c/bin/whitespace-stego-c ${BIN_DIR}/

# Remove all build artifacts
clean:
	rm -rf ${VENV}
	rm -rf implementations/python/whitespace-stego-python/target
	rm -rf implementations/python/whitespace-stego-python/*.egg-info
	rm -rf implementations/python/whitespace-stego-python/dist
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
	rm -rf implementations/go/coverage.out implementations/go/coverage.html implementations/go/coverage.txt
	rm -rf implementations/c/coverage
	rm -rf implementations/rust/target/coverage
	rm -rf coverage-reports
	# Keep spec files for builds
	cargo clean

# Run coverage for all languages
coverage: cov-go cov-rust cov-c cov-python
	@echo "🎉 All coverage reports generated!"
	@echo "📊 Reports available:"
	@echo "  Go: implementations/go/coverage.html"
	@echo "  Rust: implementations/rust/coverage/tarpaulin-report.html"
	@echo "  C: implementations/c/coverage/html/index.html"
	@echo "  Python: htmlcov/index.html"

# Generate consolidated Cobertura XML coverage report
coverage-xml: coverage
	@echo "📊 Generating consolidated Cobertura XML coverage report..."
	@mkdir -p coverage-reports
	# Python already generates coverage.xml
	@cp coverage.xml coverage-reports/python-coverage.xml
	# Convert Go coverage to Cobertura XML
	@if command -v gocover-cobertura >/dev/null 2>&1; then \
		gocover-cobertura < implementations/go/coverage.out > coverage-reports/go-coverage.xml; \
	else \
		echo "gocover-cobertura not available, skipping Go XML conversion"; \
	fi
	# Rust already generates XML
	@cp implementations/rust/coverage/tarpaulin.xml coverage-reports/rust-coverage.xml
	# C coverage to XML
	@cd implementations/c && gcovr --xml --output=../../coverage-reports/c-coverage.xml
	@echo "📊 Consolidated coverage reports in coverage-reports/"
	@echo "  Python: coverage-reports/python-coverage.xml"
	@echo "  Go: coverage-reports/go-coverage.xml"
	@echo "  Rust: coverage-reports/rust-coverage.xml"
	@echo "  C: coverage-reports/c-coverage.xml"

# Coverage targets
cov-c:
	@echo "🧪 Running C tests with coverage..."
	cd implementations/c && make install-unity
	cd implementations/c && make clean
	cd implementations/c && make test-coverage
	cd implementations/c && make coverage-report
	@echo "📊 C coverage report generated: implementations/c/coverage/html/index.html"

cov-go:
	@echo "🧪 Running Go tests with coverage..."
	cd implementations/go && go test -coverprofile=coverage.out -covermode=atomic ./src/stego
	cd implementations/go && go tool cover -func=coverage.out > coverage.txt
	cd implementations/go && go tool cover -html=coverage.out -o coverage.html
	@echo "📊 Go coverage report generated: implementations/go/coverage.html"
	@echo "📋 Go coverage summary: implementations/go/coverage.txt"

cov-python: all
	@echo "🧪 Running Python tests with coverage..."
	cd implementations/python && ${VENV}/bin/pytest --cov=whitespace_stego --cov=whitespace_stego_rust --cov-report=html:../htmlcov --cov-report=term-missing --cov-report=xml:../coverage.xml
	@echo "📊 Python coverage report generated: htmlcov/index.html"

cov-rust:
	@echo "🧪 Running Rust tests with coverage..."
	cd implementations/rust && cargo tarpaulin --out Html --output-dir coverage
	cd implementations/rust && cargo tarpaulin --out Xml --output-dir coverage
	@echo "📊 Rust coverage report generated: implementations/rust/coverage/tarpaulin-report.html"

# Build Go CLI binary
go:
	@echo "Building Go CLI binary..."
	cd implementations/go && make clean && make build
	cd ../..
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}/implementations/go/bin/whitespace-stego-go ${BIN_DIR}/

# Install Python package and dependencies
install: venv maturin-develop
	${VENV}/bin/pip install -e implementations/python/
	${VENV}/bin/pip install -r requirements-dev.txt

# Install Rust extension in development mode
VENV_ABS:=$(abspath ${VENV})
maturin-develop: ${VENV}/bin/maturin
	PATH="${VENV_ABS}/bin:$$PATH" PYTHON_SYS_EXECUTABLE="${VENV_ABS}/bin/python3" cd implementations/python/whitespace-stego-python && ../../${VENV}/bin/maturin develop

${VENV}/bin/maturin: venv
	${VENV}/bin/pip install maturin

# Build Python CLI binary using PyInstaller (local build)
python-binary: venv install maturin-develop rust c
	@echo "Building Python CLI binary with PyInstaller..."
	${VENV}/bin/pip install pyinstaller
	${VENV}/bin/pyinstaller --clean ${MAKEFILE_DIR}/../whitespace_stego.spec
	mkdir -p ${BIN_DIR}
	cp ${MAKEFILE_DIR}/dist/whitespace-stego-py ${BIN_DIR}/

# Build portable Python CLI binary using Docker
python-binary-docker:
	@echo "Building portable Python CLI binary using Docker..."
	docker build -t whitespace-stego-py-builder .
	mkdir -p dist ${BIN_DIR}
	docker run --rm --entrypoint cp -v "$(PWD)/dist:/out" whitespace-stego-py-builder /build/dist/whitespace-stego-py /out/
	cp ${MAKEFILE_DIR}/dist/whitespace-stego-py ${BIN_DIR}/
	@echo "Testing the binary..."
	${BIN_DIR}/whitespace-stego-py --help

# Build Rust CLI binary and Python extension
rust: venv
	@echo "Building Rust CLI binary and Python extension..."
	cargo build --release --manifest-path implementations/rust/Cargo.toml --target-dir implementations/rust/target
	cargo build --release --manifest-path implementations/python/whitespace-stego-python/Cargo.toml --target-dir implementations/python/whitespace-stego-python/target
	mkdir -p ${BIN_DIR}
	cp implementations/rust/target/release/whitespace-stego-rs ${BIN_DIR}/

# Run Python module tests
test: venv maturin-develop install all
	@echo "Running Python module tests..."
	cd implementations/python && ${VENV}/bin/pytest -v

# Create Python virtual environment
venv:
	python3 -m venv ${VENV}

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