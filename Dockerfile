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
    RUN cd whitespace-stego-python && /opt/venv/bin/maturin develop --release

# Install your Python package and dependencies in the venv
RUN /opt/venv/bin/pip install .

# Debug: List contents to verify files are copied
RUN ls -la /build/ && echo "=== Checking for spec file ===" && ls -la /build/whitespace_stego.spec || echo "Spec file not found!"

# Build the binary with PyInstaller using the spec file
RUN /opt/venv/bin/pyinstaller whitespace_stego.spec

# The resulting binary will be in /build/dist/whitespace-stego-py 