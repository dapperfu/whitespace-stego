# Docker Guide

This guide covers Docker usage for the whitespace steganography toolkit, including building portable binaries and development environments.

## Overview

Docker is used in this project for:
- **Portable Binary Creation**: Building standalone executables that work across Linux distributions
- **Development Environment**: Consistent build environment for contributors
- **Testing**: Isolated testing environments
- **Deployment**: Containerized applications

## Dockerfile Architecture

### Main Dockerfile

The main `Dockerfile` creates a portable Python binary with Rust backend:

```dockerfile
# Use Python 3.10 slim for portability
FROM python:3.10-slim

# Install build dependencies for Python, Rust, and maturin
RUN apt-get update && \
    apt-get install -y build-essential python3-dev git curl && \
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
RUN cd whitespace-stego-backend && /opt/venv/bin/maturin develop --release

# Install your Python package and dependencies in the venv
RUN /opt/venv/bin/pip install .

# Build the binary with PyInstaller entry point using venv's python
RUN /opt/venv/bin/pyinstaller --onefile --name whitespace-stego-py whitespace_stego_main.py
```

### Key Features

1. **Multi-stage Build**: Optimized for binary creation
2. **Virtual Environment**: Isolated Python environment
3. **Rust Integration**: Builds Rust backend for performance
4. **PyInstaller**: Creates standalone executable
5. **Portability**: Works on most Linux distributions

## Build Process

### Building Portable Binary

```bash
# Build the Docker image and extract binary
make python-binary-docker
```

This command:
1. Builds the Docker image with all dependencies
2. Compiles the Rust backend using maturin
3. Installs the Python package
4. Creates a portable binary using PyInstaller
5. Extracts the binary to `dist/whitespace-stego-py`

### Manual Docker Build

```bash
# Build the image
docker build -t whitespace-stego-py-builder .

# Extract the binary
mkdir -p dist
docker run --rm -v "$(PWD)/dist:/out" whitespace-stego-py-builder /bin/cp /build/dist/whitespace-stego-py /out/
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
# Build and test the binary
make python-binary-docker

# Use the binary
./dist/whitespace-stego-py --help
./dist/whitespace-stego-py encode --message "Secret" --carrier "Hello World"
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
docker run --rm whitespace-stego-dev make test

# Run specific test suite
docker run --rm whitespace-stego-dev pytest tests/test_core.py
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
    command: /bin/cp /build/dist/whitespace-stego-py /out/
    
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
COPY --from=builder /build/dist/whitespace-stego-py /usr/local/bin/
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
docker build --no-cache -t whitespace-stego-py-builder .
```

#### Permission Issues
```bash
# Fix file permissions
sudo chown -R $USER:$USER dist/

# Use proper volume mounting
docker run --rm -v "$(PWD)/dist:/out:rw" whitespace-stego-py-builder /bin/cp /build/dist/whitespace-stego-py /out/
```

#### Memory Issues
```bash
# Increase Docker memory limit
docker run --memory=4g whitespace-stego-py-builder

# Use swap if needed
docker run --memory=2g --memory-swap=4g whitespace-stego-py-builder
```

### Debugging

#### Interactive Debugging
```bash
# Run container with debug tools
docker run -it --rm whitespace-stego-py-builder /bin/bash

# Install debug tools
apt-get update && apt-get install -y vim htop strace
```

#### Log Analysis
```bash
# View build logs
docker logs $(docker ps -q --filter ancestor=whitespace-stego-py-builder)

# Check image layers
docker history whitespace-stego-py-builder
```

## Best Practices

### Security
1. **Use specific base images**: Avoid `latest` tags
2. **Run as non-root**: Create dedicated user
3. **Minimize attack surface**: Remove unnecessary packages
4. **Scan for vulnerabilities**: Use `docker scan`

### Performance
1. **Optimize layer caching**: Order Dockerfile instructions carefully
2. **Use multi-stage builds**: Separate build and runtime
3. **Minimize image size**: Remove build dependencies
4. **Use .dockerignore**: Exclude unnecessary files

### Maintainability
1. **Document Dockerfile**: Add comments explaining steps
2. **Version dependencies**: Pin specific versions
3. **Use build args**: Make builds configurable
4. **Test containers**: Include container tests

## Advanced Usage

### Custom Build Scripts

Create `scripts/docker-build.sh`:
```bash
#!/bin/bash
set -e

# Build with custom options
docker build \
  --build-arg PYTHON_VERSION=3.11 \
  --build-arg RUST_VERSION=1.70.0 \
  --target runtime \
  -t whitespace-stego:latest .

# Run security scan
docker scan whitespace-stego:latest

# Test binary
docker run --rm whitespace-stego:latest whitespace-stego-py --help
```

### CI/CD Integration

```yaml
# GitHub Actions example
- name: Build Docker image
  run: |
    docker build -t whitespace-stego-py-builder .
    docker run --rm -v "$(PWD)/dist:/out" whitespace-stego-py-builder /bin/cp /build/dist/whitespace-stego-py /out/
    
- name: Test binary
  run: |
    chmod +x dist/whitespace-stego-py
    ./dist/whitespace-stego-py --help
```

### Distribution

```bash
# Create distribution package
tar -czf whitespace-stego-py-linux-x86_64.tar.gz dist/whitespace-stego-py

# Upload to releases
gh release upload v1.0.0 whitespace-stego-py-linux-x86_64.tar.gz
```

## Related Documentation

- [Installation Guide](INSTALLATION.md) - General installation instructions
- [Architecture](ARCHITECTURE.md) - System architecture overview
- [Testing Guide](TESTING.md) - Testing strategies and procedures
- [Contributing Guide](CONTRIBUTING.md) - Development guidelines 