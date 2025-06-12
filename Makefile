.PHONY: install test lint format clean md-report-gfm test-all rust-cli c-cli all-cli clean-rust clean-c clean-cli go-cli test-go-cli test-go-cli-integration

install:
	pip install -e .[dev]

test:
	.venv/bin/pytest tests/ --cov=python --cov-report=term-missing

lint:
	mypy python/ tests/
	flake8 python/ tests/
	isort --check-only python/ tests/

format:
	black python/ tests/
	isort python/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

md-report-gfm:
	venv/bin/pytest --md-report --md-report-flavor gfm tests/ > report.md

test-all: test
	cd rust_backend && cargo test
	./test_roundtrip.sh
	# Add any other bash test scripts here

whitespace_stego_rs: rust_backend/Cargo.toml $(shell find rust_backend/src -type f)
	$(MAKE) -C rust_backend build-release
	cp rust_backend/target/release/whitespace_stego_rs ./whitespace_stego_rs

rust-cli: whitespace_stego_rs

whitespace_stego_c: c_backend/Makefile $(shell find c_backend/src -type f)
	$(MAKE) -C c_backend
	cp c_backend/bin/whitespace_stego_c ./whitespace_stego_c

c-cli: whitespace_stego_c

all-cli: rust-cli c-cli

clean-rust:
	$(MAKE) -C rust_backend clean

clean-c:
	$(MAKE) -C c_backend clean

clean-cli: clean-rust clean-c

go-cli:
	cd go_cli && go build -o ../bin/whitespace-stego-go

test-go-cli:
	cd go_cli && go test ./...

test-go-cli-integration:
	./scripts/test_go.sh 