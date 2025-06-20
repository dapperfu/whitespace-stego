VENV?=.venv
.PHONY: help venv install test coverage maturin-develop maturin-build cargo-build cargo-clean clean format rust wasi-web test-wasm test-wasm-only test-all docker-build docker-build-python docker-build-rust docker-build-c docker-compose-up docker-compose-down docker-compose-dev docker-compose-jupyter docker-compose-test docker-compose-production docker-clean docker-push docker-pull docker-run-python docker-run-rust docker-run-c docker-run-jupyter docker-run-test docker-logs docker-shell docker-stop-all
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
	@echo "  wasi-web        - Build WASI web app and serve it at http://localhost:8000"
	@echo ""
	@echo "Docker targets:"
	@echo "  docker-build           - Build all Docker images"
	@echo "  docker-build-python    - Build Python implementation Docker image"
	@echo "  docker-build-rust      - Build Rust implementation Docker image"
	@echo "  docker-build-c         - Build C implementation Docker image"
	@echo "  docker-compose-up      - Start all Docker services"
	@echo "  docker-compose-down    - Stop all Docker services"
	@echo "  docker-compose-dev     - Start development environment"
	@echo "  docker-compose-jupyter - Start Jupyter notebook environment"
	@echo "  docker-compose-test    - Start testing environment"
	@echo "  docker-compose-production - Start production environment"
	@echo "  docker-run-python      - Run Python implementation container"
	@echo "  docker-run-rust        - Run Rust implementation container"
	@echo "  docker-run-c           - Run C implementation container"
	@echo "  docker-run-jupyter     - Run Jupyter notebook container"
	@echo "  docker-run-test        - Run test container"
	@echo "  docker-shell           - Start shell in development container"
	@echo "  docker-logs            - Show logs from all containers"
	@echo "  docker-stop-all        - Stop all running containers"
	@echo "  docker-clean           - Remove all Docker containers and images"
	@echo "  docker-push            - Push Docker images to registry"
	@echo "  docker-pull            - Pull Docker images from registry"

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
	rm -rf htmlcov
	rm -f coverage.xml
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

# Docker targets

# Build all Docker images
docker-build: docker-build-base docker-build-python docker-build-rust docker-build-c
	@echo "All Docker images built successfully"

# Build base Docker image
docker-build-base:
	@echo "Building base Docker image..."
	docker build -f Dockerfile.base -t whitespace-stego:base .

# Build Python implementation Docker image
docker-build-python:
	@echo "Building Python Docker image..."
	docker build -f Dockerfile.python -t whitespace-stego:python .

# Build Rust implementation Docker image
docker-build-rust:
	@echo "Building Rust Docker image..."
	docker build -f Dockerfile.rust -t whitespace-stego:rust .

# Build C implementation Docker image
docker-build-c:
	@echo "Building C Docker image..."
	docker build -f Dockerfile.c -t whitespace-stego:c .

# Build main multi-stage Docker image
docker-build-main:
	docker build -f Dockerfile -t whitespace-stego:latest .

# Start all Docker services
docker-compose-up:
	docker-compose up -d

# Stop all Docker services
docker-compose-down:
	docker-compose down

# Start development environment
docker-compose-dev:
	docker-compose --profile development up -d dev

# Start Jupyter notebook environment
docker-compose-jupyter:
	docker-compose --profile jupyter up -d jupyter

# Start testing environment
docker-compose-test:
	docker-compose --profile testing up -d test

# Start production environment
docker-compose-production:
	docker-compose --profile production up -d production

# Start individual implementation services
docker-compose-python:
	docker-compose --profile individual up -d python-cli

docker-compose-rust:
	docker-compose --profile individual up -d rust-cli

docker-compose-c:
	docker-compose --profile individual up -d c-cli

# Run Python implementation container
docker-run-python:
	docker run --rm -it -v $(PWD)/data:/app/data whitespace-stego:python

# Run Rust implementation container
docker-run-rust:
	docker run --rm -it -v $(PWD)/data:/app/data whitespace-stego:rust

# Run C implementation container
docker-run-c:
	docker run --rm -it -v $(PWD)/data:/app/data whitespace-stego:c

# Run Jupyter notebook container
docker-run-jupyter:
	docker run --rm -it -p 8888:8888 -v $(PWD):/workspace whitespace-stego:latest jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

# Run test container
docker-run-test:
	docker run --rm -it -v $(PWD):/workspace whitespace-stego:latest make test

# Start shell in development container
docker-shell:
	docker run --rm -it -v $(PWD):/workspace -p 8888:8888 whitespace-stego:latest /bin/bash

# Show logs from all containers
docker-logs:
	docker-compose logs -f

# Stop all running containers
docker-stop-all:
	docker stop $$(docker ps -q) 2>/dev/null || true

# Remove all Docker containers and images
docker-clean:
	docker-compose down -v --remove-orphans
	docker system prune -f
	docker image prune -f

# Push Docker images to registry (requires registry configuration)
docker-push:
	docker push whitespace-stego:python
	docker push whitespace-stego:rust
	docker push whitespace-stego:c
	docker push whitespace-stego:latest

# Pull Docker images from registry (requires registry configuration)
docker-pull:
	docker pull whitespace-stego:python
	docker pull whitespace-stego:rust
	docker pull whitespace-stego:c
	docker pull whitespace-stego:latest

# ... existing code ... 