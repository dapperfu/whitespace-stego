# Unified Makefile for whitespace-stego project

BINDIR = bin

.PHONY: all build-all build-cli-all test-all clean-all verify-all verify-python verify-rust verify-rust-wasm verify-c verify-go verify-cpp verify-asm benchmark-all help publish-docs

help:
	@echo "whitespace-stego Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  build-all          - Build all language implementations"
	@echo "  build-cli-all      - Build all CLI binaries to bin/ directory"
	@echo "  test-all           - Run all tests"
	@echo "  clean-all           - Clean all build artifacts"
	@echo "  verify-all          - Verify all implementations build"
	@echo "  verify-python       - Verify Python builds and imports"
	@echo "  verify-rust         - Verify Rust builds and tests"
	@echo "  verify-rust-wasm    - Verify Rust-WASM builds"
	@echo "  verify-c            - Verify C builds"
	@echo "  verify-go           - Verify Go builds"
	@echo "  verify-cpp          - Verify C++ builds"
	@echo "  verify-asm          - Verify Assembly builds"
	@echo "  benchmark-all       - Run all benchmarks"
	@echo "  serve               - Build WASM and serve web demo on http://localhost:8000"
	@echo "  publish-docs        - Build WASM and publish to docs/ for GitHub Pages"

all: build-all

build-all: build-python build-rust build-c build-go build-cpp build-asm

build-cli-all: | $(BINDIR)
	@echo "Building all CLI binaries..."
	@$(MAKE) build-cli-python
	@$(MAKE) build-cli-rust
	@$(MAKE) build-cli-c
	@$(MAKE) build-cli-go
	@$(MAKE) build-cli-cpp
	@echo "All CLI binaries built in $(BINDIR)/"

$(BINDIR):
	mkdir -p $(BINDIR)

build-python:
	@echo "Building Python..."
	cd python && pip install -e . > /dev/null 2>&1 || true

build-cli-python: | $(BINDIR)
	@echo "Building Python CLI binary..."
	@if command -v python3 > /dev/null; then \
		cd python && $(MAKE) cli || \
		(python3 -m pip install --user --quiet pyinstaller 2>/dev/null || \
		 python3 -m pip install --break-system-packages --quiet pyinstaller 2>/dev/null || true) && \
		if python3 -m PyInstaller --version > /dev/null 2>&1; then \
			python3 -m PyInstaller --onefile --name whitespace-stego-python \
				--hidden-import whitespace_stego \
				--hidden-import whitespace_stego.encoder \
				--hidden-import whitespace_stego.decoder \
				--hidden-import whitespace_stego.errors \
				--clean \
				cli.py && \
			cp dist/whitespace-stego-python ../$(BINDIR)/whitespace-stego-python && \
			chmod +x ../$(BINDIR)/whitespace-stego-python; \
		else \
			echo "PyInstaller not available, skipping Python CLI binary build"; \
		fi; \
	else \
		echo "python3 not found, skipping Python CLI build"; \
	fi

build-rust:
	@echo "Building Rust..."
	@if command -v cargo > /dev/null; then \
		cd rust && cargo build --release; \
	else \
		echo "cargo not found, skipping Rust build"; \
	fi

build-cli-rust: | $(BINDIR)
	@echo "Building Rust CLI..."
	@if command -v cargo > /dev/null; then \
		cd rust && cargo build --release --bin whitespace-stego-rust && \
		cp target/release/whitespace-stego-rust ../$(BINDIR)/whitespace-stego-rust; \
	else \
		echo "cargo not found, skipping Rust CLI build"; \
	fi

build-rust-wasm:
	@echo "Building Rust-WASM..."
	@WASM_PACK=$$(command -v wasm-pack 2>/dev/null || \
		([ -f ~/.cargo/bin/wasm-pack ] && echo ~/.cargo/bin/wasm-pack) || \
		([ -f $$HOME/.cargo/bin/wasm-pack ] && echo $$HOME/.cargo/bin/wasm-pack) || \
		echo ""); \
	if [ -z "$$WASM_PACK" ]; then \
		echo "Error: wasm-pack not found!"; \
		echo ""; \
		echo "Install wasm-pack with:"; \
		echo "  curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh"; \
		echo ""; \
		echo "Or using cargo:"; \
		echo "  cargo install wasm-pack"; \
		echo ""; \
		echo "Note: After installation, ensure ~/.cargo/bin is in your PATH"; \
		exit 1; \
	fi
	@WASM_PACK=$$(command -v wasm-pack 2>/dev/null || \
		([ -f ~/.cargo/bin/wasm-pack ] && echo ~/.cargo/bin/wasm-pack) || \
		([ -f $$HOME/.cargo/bin/wasm-pack ] && echo $$HOME/.cargo/bin/wasm-pack)); \
	cd rust-wasm && "$$WASM_PACK" build --target web --out-dir pkg

serve: build-rust-wasm
	@if [ ! -d "rust-wasm/pkg" ] || [ ! -f "rust-wasm/pkg/whitespace_stego_wasm.js" ]; then \
		echo "Error: WASM module not built!"; \
		echo "Run 'make build-rust-wasm' first."; \
		exit 1; \
	fi
	@echo "Starting web server for WASM demo..."
	@echo ""
	@echo "🌐 Open http://localhost:8000 in your browser"
	@echo "Press Ctrl+C to stop the server"
	@echo ""
	@cd rust-wasm && \
	if command -v python3 > /dev/null; then \
		python3 -m http.server 8000; \
	elif command -v python > /dev/null; then \
		python -m SimpleHTTPServer 8000; \
	else \
		echo "Error: No web server found. Install Python or use:"; \
		echo "  cd rust-wasm && python3 -m http.server 8000"; \
		exit 1; \
	fi

publish-docs: build-rust-wasm
	@echo "Publishing WASM demo to docs/ for GitHub Pages..."
	@if [ ! -d "rust-wasm/pkg" ] || [ ! -f "rust-wasm/pkg/whitespace_stego_wasm.js" ]; then \
		echo "Error: WASM module not built!"; \
		echo "Run 'make build-rust-wasm' first."; \
		exit 1; \
	fi
	@mkdir -p docs
	@cp rust-wasm/index.html docs/
	@cp -r rust-wasm/pkg docs/
	@touch docs/.nojekyll
	@echo "✓ Published to docs/"
	@echo ""
	@echo "To enable GitHub Pages:"
	@echo "  1. Go to repository Settings > Pages"
	@echo "  2. Select 'Deploy from a branch'"
	@echo "  3. Choose 'main' (or your default branch) and '/docs' folder"
	@echo "  4. Your site will be available at: https://<username>.github.io/<repo>/"

build-c:
	@echo "Building C..."
	@if command -v gcc > /dev/null || command -v clang > /dev/null; then \
		cd c && make all; \
	else \
		echo "C compiler not found, skipping C build"; \
	fi

build-cli-c: | $(BINDIR)
	@echo "Building C CLI..."
	@if command -v gcc > /dev/null || command -v clang > /dev/null; then \
		cd c && make cli; \
	else \
		echo "C compiler not found, skipping C CLI build"; \
	fi

build-go:
	@echo "Building Go..."
	@if command -v go > /dev/null; then \
		cd go && go build ./...; \
	else \
		echo "go not found, skipping Go build"; \
	fi

build-cli-go: | $(BINDIR)
	@echo "Building Go CLI..."
	@if command -v go > /dev/null; then \
		cd go && $(MAKE) cli || (command -v go > /dev/null && go build -o ../$(BINDIR)/whitespace-stego-go ./cmd/cli); \
	else \
		echo "go not found, skipping Go CLI build"; \
	fi

build-cpp:
	@echo "Building C++..."
	@if command -v cmake > /dev/null; then \
		cd cpp && mkdir -p build && cd build && \
		cmake .. && cmake --build .; \
	else \
		echo "cmake not found, skipping C++ build"; \
	fi

build-cli-cpp: | $(BINDIR)
	@echo "Building C++ CLI..."
	@if command -v cmake > /dev/null; then \
		cd cpp && mkdir -p build && cd build && \
		cmake .. && cmake --build . --target whitespace-stego-cli && \
		cp whitespace-stego-cli ../../$(BINDIR)/whitespace-stego-cpp; \
	else \
		echo "cmake not found, skipping C++ CLI build"; \
	fi

build-asm:
	@echo "Building Assembly..."
	@if command -v nasm > /dev/null; then \
		cd asm && make all; \
	else \
		echo "nasm not found, skipping Assembly build"; \
	fi

test-all:
	@echo "Running all tests..."
	@./tests/test_runner.sh

clean-all: clean-python clean-rust clean-c clean-go clean-cpp clean-asm clean-bin

clean-python:
	@cd python && rm -rf build dist *.egg-info __pycache__ .pytest_cache *.spec
	@rm -f $(BINDIR)/whitespace-stego-python

clean-rust:
	@cd rust && cargo clean 2>/dev/null || true
	@cd rust-wasm && cargo clean 2>/dev/null || true

clean-c:
	@cd c && make clean 2>/dev/null || true

clean-go:
	@cd go && go clean ./... 2>/dev/null || true

clean-cpp:
	@cd cpp && rm -rf build 2>/dev/null || true

clean-asm:
	@cd asm && make clean 2>/dev/null || true

clean-bin:
	@rm -rf $(BINDIR)

verify-all: verify-python verify-rust verify-rust-wasm verify-c verify-go verify-cpp verify-asm
	@echo ""
	@echo "✓ All build verifications passed!"

verify-python:
	@echo "Verifying Python build..."
	@cd python && pip install -e . > /dev/null 2>&1 && \
		python -c "import whitespace_stego; print('✓ Python import successful')" || \
		(echo "✗ Python build verification failed" && exit 1)

verify-rust:
	@echo "Verifying Rust build..."
	@if command -v cargo > /dev/null; then \
		cd rust && cargo build --release > /dev/null 2>&1 && \
		cargo test --lib > /dev/null 2>&1 && \
		echo "✓ Rust build and tests passed"; \
	else \
		echo "⚠ cargo not found, skipping Rust verification"; \
	fi

verify-rust-wasm:
	@echo "Verifying Rust-WASM build..."
	@if command -v wasm-pack > /dev/null && command -v cargo > /dev/null; then \
		cd rust-wasm && \
		(cargo build --target wasm32-unknown-unknown --release > /dev/null 2>&1 && \
		 cargo build --target wasm32-wasi --release > /dev/null 2>&1 && \
		 echo "✓ Rust-WASM builds passed") || \
		(echo "✗ Rust-WASM build verification failed" && exit 1); \
	else \
		echo "⚠ wasm-pack or cargo not found, skipping WASM verification"; \
	fi

verify-c:
	@echo "Verifying C build..."
	@if command -v gcc > /dev/null || command -v clang > /dev/null; then \
		cd c && make all > /dev/null 2>&1 && \
		[ -f lib/libwhitespace_stego.a ] && \
		echo "✓ C build passed"; \
	else \
		echo "⚠ C compiler not found, skipping C verification"; \
	fi

verify-go:
	@echo "Verifying Go build..."
	@if command -v go > /dev/null; then \
		cd go && go build ./... > /dev/null 2>&1 && \
		go test ./... > /dev/null 2>&1 && \
		echo "✓ Go build and tests passed"; \
	else \
		echo "⚠ go not found, skipping Go verification"; \
	fi

verify-cpp:
	@echo "Verifying C++ build..."
	@if command -v cmake > /dev/null; then \
		cd cpp && mkdir -p build && cd build && \
		cmake .. > /dev/null 2>&1 && \
		cmake --build . > /dev/null 2>&1 && \
		echo "✓ C++ build passed"; \
	else \
		echo "⚠ cmake not found, skipping C++ verification"; \
	fi

verify-asm:
	@echo "Verifying Assembly build..."
	@if command -v nasm > /dev/null; then \
		cd asm && make all > /dev/null 2>&1 && \
		[ -f libwhitespace_stego_asm.a ] && \
		echo "✓ Assembly build passed"; \
	else \
		echo "⚠ nasm not found, skipping Assembly verification"; \
	fi

benchmark-all:
	@echo "Running benchmarks..."
	@if [ -f benchmarks/benchmark.py ]; then \
		python3 benchmarks/benchmark.py; \
	else \
		echo "Benchmark script not found"; \
	fi

