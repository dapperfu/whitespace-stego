# Makefile for whitespace-stego-rust

.PHONY: all clean build test install uninstall help dev debug release coverage coverage-html coverage-xml lint fmt clippy bench check check-all doc doc-open

# Binary name
BINARY_NAME = whitespace-stego-rs
BINARY_PATH = target/release/$(BINARY_NAME)

# Cargo profiles
CARGO_PROFILE_DEV = --profile dev
CARGO_PROFILE_RELEASE = --profile release
CARGO_PROFILE_BENCH = --profile bench

# Rust version
RUST_VERSION = 1.70

# Default target
all: build

help:
	@echo "Whitespace Steganography - Rust Implementation"
	@echo "============================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all             - Build the binary (default)"
	@echo "  help            - Show this help message"
	@echo "  build           - Build the binary"
	@echo "  dev             - Build with development profile"
	@echo "  debug           - Build with debug profile"
	@echo "  release         - Build optimized release version"
	@echo "  install         - Install to /usr/local/bin"
	@echo "  uninstall       - Remove from /usr/local/bin"
	@echo "  test            - Run tests"
	@echo "  test-verbose    - Run tests with verbose output"
	@echo "  test-all        - Run all tests including integration"
	@echo "  coverage        - Run tests with coverage"
	@echo "  coverage-html   - Generate HTML coverage report"
	@echo "  coverage-xml    - Generate XML coverage report"
	@echo "  lint            - Run clippy linter"
	@echo "  fmt             - Format code"
	@echo "  clippy          - Run clippy with all checks"
	@echo "  bench           - Run benchmarks"
	@echo "  check           - Check code without building"
	@echo "  check-all       - Run all checks (fmt, clippy, test)"
	@echo "  doc             - Generate documentation"
	@echo "  doc-open        - Generate and open documentation"
	@echo "  clean           - Clean build artifacts"
	@echo "  distclean       - Clean all artifacts and dependencies"

build: $(BINARY_PATH)

$(BINARY_PATH): Cargo.toml src/*.rs
	@echo "Building $(BINARY_NAME)..."
	cargo build --release

dev: Cargo.toml src/*.rs
	@echo "Building $(BINARY_NAME) with development profile..."
	cargo build $(CARGO_PROFILE_DEV)

debug: Cargo.toml src/*.rs
	@echo "Building $(BINARY_NAME) with debug profile..."
	cargo build

release: Cargo.toml src/*.rs
	@echo "Building $(BINARY_NAME) with release profile..."
	cargo build --release

install: build
	@echo "Installing $(BINARY_NAME)..."
	@sudo cp $(BINARY_PATH) /usr/local/bin/$(BINARY_NAME)
	@sudo chmod +x /usr/local/bin/$(BINARY_NAME)
	@echo "Installation complete!"

uninstall:
	@echo "Uninstalling $(BINARY_NAME)..."
	@sudo rm -f /usr/local/bin/$(BINARY_NAME)
	@echo "Uninstallation complete!"

test:
	@echo "Running tests..."
	cargo test

test-verbose:
	@echo "Running tests with verbose output..."
	cargo test --verbose

test-all:
	@echo "Running all tests including integration..."
	cargo test --all-features
	cargo test --tests
	cargo test --lib
	cargo test --bins

coverage:
	@echo "Running tests with coverage..."
	@if command -v cargo-tarpaulin >/dev/null 2>&1; then \
		cargo tarpaulin --out Html --output-dir coverage; \
		cargo tarpaulin --out Xml --output-dir coverage; \
	else \
		echo "cargo-tarpaulin not available, install with: cargo install cargo-tarpaulin"; \
		echo "Falling back to basic coverage..."; \
		cargo test --coverage; \
	fi

coverage-html: coverage
	@echo "HTML coverage report generated in coverage/tarpaulin-report.html"

coverage-xml: coverage
	@echo "XML coverage report generated in coverage/tarpaulin.xml"

lint:
	@echo "Running clippy linter..."
	cargo clippy

fmt:
	@echo "Formatting code..."
	cargo fmt

clippy:
	@echo "Running clippy with all checks..."
	cargo clippy -- -D warnings

bench:
	@echo "Running benchmarks..."
	cargo bench

check:
	@echo "Checking code without building..."
	cargo check

check-all: fmt clippy test
	@echo "All checks completed!"

doc:
	@echo "Generating documentation..."
	cargo doc --no-deps

doc-open:
	@echo "Generating and opening documentation..."
	cargo doc --no-deps --open

clean:
	@echo "Cleaning..."
	cargo clean

distclean: clean
	@echo "Cleaning all artifacts and dependencies..."
	@rm -rf coverage/
	@rm -rf target/

# Development targets
dev-run: dev
	@echo "Running in development mode..."
	@./target/debug/$(BINARY_NAME) --help

# Show version
version:
	@echo "Rust version: $(shell rustc --version)"
	@echo "Cargo version: $(shell cargo --version)"
	@echo "Binary version: $(shell ./$(BINARY_PATH) --version 2>/dev/null || echo 'Not built')"

# Check Rust version
check-rust:
	@echo "Checking Rust version..."
	@rustc --version | grep -q "rustc $(RUST_VERSION)" || \
		(echo "Warning: Expected Rust $(RUST_VERSION), found $$(rustc --version)"; exit 1)
	@echo "Rust version check passed: $$(rustc --version)"

# Update dependencies
update:
	@echo "Updating dependencies..."
	cargo update

# Audit dependencies
audit:
	@echo "Auditing dependencies..."
	cargo audit

# Build for multiple targets
build-linux: 
	@echo "Building for Linux..."
	cargo build --release --target x86_64-unknown-linux-gnu

build-macos:
	@echo "Building for macOS..."
	cargo build --release --target x86_64-apple-darwin

build-windows:
	@echo "Building for Windows..."
	cargo build --release --target x86_64-pc-windows-gnu

# Cross-compilation targets
cross-linux:
	@echo "Cross-compiling for Linux..."
	cross build --release --target x86_64-unknown-linux-gnu

cross-macos:
	@echo "Cross-compiling for macOS..."
	cross build --release --target x86_64-apple-darwin

cross-windows:
	@echo "Cross-compiling for Windows..."
	cross build --release --target x86_64-pc-windows-gnu 