# Docker Guide

This guide covers Docker usage for the whitespace steganography toolkit, including building portable binaries and development environments for all supported backends.

## Overview

Docker is used in this project for:
- **Portable Binary Creation**: Building standalone executables for Python, Rust, C, and Go
- **Development Environment**: Consistent build environment for contributors
- **Testing**: Isolated testing environments for all implementations
- **Deployment**: Containerized applications and web UI

## Dockerfile Architecture

### Main Dockerfile

The main `Dockerfile` creates a portable Python binary with Rust backend, and can be adapted for other backends:

```dockerfile
# Use Python 3.10 slim for portability
FROM python:3.10-slim

# Install build dependencies for Python, Rust, Go, and maturin
RUN apt-get update && \
    apt-get install -y build-essential python3-dev git curl golang-go && \
    rm -rf /var/lib/apt/lists/*

# Install Rust using rustup (for up-to-date cargo)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"

# Install maturin and pyinstaller in the venv
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install maturin pyinstaller

WORKDIR /build
COPY . /build

# Build and install the Rust backend in the venv
RUN cd whitespace-stego-rust && /opt/venv/bin/maturin develop --release

# Install your Python package and dependencies in the venv
RUN /opt/venv/bin/pip install .

# Build the binary with PyInstaller entry point using venv's python
RUN /opt/venv/bin/pyinstaller --onefile --name whitespace-stego-py whitespace_stego_main.py

# Build Go binary
RUN cd go/src && go build -o /build/bin/whitespace-stego-go main.go

# Build Rust CLI binary
RUN cd whitespace-stego-cli && cargo build --release && cp target/release/whitespace-stego /build/bin/whitespace-stego-rs

# Build C binary
RUN cd c && make && cp bin/whitespace-stego-c /build/bin/whitespace-stego-c
```

### Key Features

1. **Multi-language Build**: Python, Rust, C, and Go binaries
2. **Virtual Environment**: Isolated Python environment
3. **Rust Integration**: Builds Rust backend and CLI
4. **Go Integration**: Builds Go CLI
5. **C Integration**: Builds C CLI
6. **PyInstaller**: Creates standalone Python executable
7. **Portability**: Works on most Linux distributions

## Build Process

### Building All Binaries

```bash
# Build the Docker image and extract all binaries
make all-binaries-docker
```

This command:
1. Builds the Docker image with all dependencies
2. Compiles the Rust backend and CLI using maturin and cargo
3. Compiles the Go CLI
4. Compiles the C CLI
5. Installs the Python package
6. Creates a portable Python binary using PyInstaller
7. Extracts all binaries to `bin/` or `dist/`

### Manual Docker Build

```bash
# Build the image
docker build -t whitespace-stego-builder .

# Extract the binaries
mkdir -p dist
for bin in whitespace-stego-py whitespace-stego-go whitespace-stego-rs whitespace-stego-c; do
  docker run --rm -v "$(PWD)/dist:/out" whitespace-stego-builder /bin/cp /build/bin/$bin /out/
done
```

### Build Options

#### Custom Python Version
```dockerfile
# Use different Python version
FROM python:3.11-slim
```

#### Custom Rust Toolchain
```dockerfile
# Use specific Rust version
RUN rustup install 1.70.0
RUN rustup default 1.70.0
```

#### Optimized Build
```dockerfile
# Enable optimizations
ENV RUSTFLAGS="-C target-cpu=native"
ENV CARGO_PROFILE_RELEASE_OPT_LEVEL=3
```

## Usage Examples

### Basic Usage

```bash
# Build and test all binaries
make all-binaries-docker

# Use the binaries
./dist/whitespace-stego-py --help
./dist/whitespace-stego-go --help
./dist/whitespace-stego-rs --help
./dist/whitespace-stego-c --help
```

### Development Environment

```bash
# Build development image
docker build -t whitespace-stego-dev .

# Run interactive shell
docker run -it --rm whitespace-stego-dev /bin/bash

# Mount source code for development
docker run -it --rm -v "$(PWD):/workspace" whitespace-stego-dev /bin/bash
```

### Testing in Container

```bash
# Run tests in container
docker run --rm whitespace-stego-dev make test-all

# Run specific test suite
docker run --rm whitespace-stego-dev pytest tests/test_core.py
```

### WebAssembly UI

```bash
# Build WASM package (from host or in container)
make wasi-web

# Serve the web UI
cd wasi/pkg && python3 -m http.server 8000
# Or in Docker:
docker run -p 8000:8000 whitespace-stego-dev bash -c 'cd wasi/pkg && python3 -m http.server 8000'
```

## Docker Compose

For more complex setups, create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  builder:
    build: .
    volumes:
      - ./dist:/out
    command: /bin/cp /build/bin/whitespace-stego-py /out/
      # Repeat for other binaries as needed
  tester:
    build: .
    volumes:
      - ./tests:/tests
    command: pytest /tests
  web:
    build: .
    ports:
      - "8000:8000"
    command: cd wasi/pkg && python3 -m http.server 8000
```

## Optimization

### Image Size Optimization

```dockerfile
# Multi-stage build for smaller image
FROM python:3.10-slim as builder
# ... build steps ...

FROM python:3.10-slim as runtime
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /build/bin/whitespace-stego-py /usr/local/bin/
COPY --from=builder /build/bin/whitespace-stego-go /usr/local/bin/
COPY --from=builder /build/bin/whitespace-stego-rs /usr/local/bin/
COPY --from=builder /build/bin/whitespace-stego-c /usr/local/bin/
```

### Build Speed Optimization

```dockerfile
# Use build cache effectively
COPY requirements*.txt ./
RUN pip install -r requirements.txt

COPY . .
```

### Security Hardening

```dockerfile
# Run as non-root user
RUN useradd -m -s /bin/bash app
USER app
WORKDIR /home/app

# Remove unnecessary packages
RUN apt-get purge -y build-essential && \
    apt-get autoremove -y
```

## Troubleshooting

### Common Issues

#### Build Failures
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t whitespace-stego-builder .
```

#### Permission Issues
```bash
# Fix file permissions
sudo chown -R $USER:$USER dist/

# Use proper volume mounting
docker run --rm -v "$(PWD)/dist:/out:rw" whitespace-stego-builder /bin/cp /build/bin/whitespace-stego-py /out/
```

#### Memory Issues
```bash
# Increase Docker memory limit
docker run --memory=4g whitespace-stego-builder

# Use swap if needed
docker run --memory=2g --memory-swap=4g whitespace-stego-builder
```

### Debugging

#### Interactive Debugging
```bash
# Run container with debug tools
docker run -it --rm whitespace-stego-builder /bin/bash

# Install debug tools as needed
```

## Multi-Platform Support

- **Linux**: Fully supported (x86_64, ARM64)
- **macOS**: Use Docker for Mac for builds
- **Windows**: Use WSL2 or Docker Desktop
- **WebAssembly**: Build and serve WASM UI in container

## Best Practices

- Use Docker for reproducible builds and tests
- Extract all binaries for cross-platform deployment
- Use multi-stage builds for smaller images
- Mount source code for rapid development
- Use Docker Compose for complex workflows

## Author

This Docker setup was implemented by Claude Sonnet 4 (claude-3-5-sonnet-20241022) via Cursor IDE (cursor.sh) with AI assistance. 