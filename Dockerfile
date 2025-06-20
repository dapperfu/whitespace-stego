# Multi-stage Dockerfile for Whitespace Steganography Development Environment
# This provides a complete environment with Python, Rust, and C implementations

# Base stage with common dependencies
FROM ubuntu:22.04 AS base

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV RUST_BACKTRACE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    curl \
    git \
    make \
    gcc \
    g++ \
    cmake \
    pkg-config \
    libssl-dev \
    jupyter \
    jupyter-notebook \
    patchelf \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Create workspace directory
WORKDIR /workspace

# Development stage with all tools
FROM base AS development

# Install Python development dependencies
COPY requirements-dev.txt pyproject.toml README.md ./
RUN pip3 install --no-cache-dir -r requirements-dev.txt
RUN pip3 install --no-cache-dir -e .

# Install Rust dependencies and build
COPY Cargo.toml Cargo.lock ./
COPY rust/ ./rust/
COPY src/ ./src/
RUN cargo build --release --manifest-path rust/Cargo.toml --target-dir rust/target
RUN cp rust/target/release/whitespace-stego-rs ./whitespace-stego-rs

# Build C implementation
COPY c/ ./c/
RUN cd c && make clean && make

# Install Rust backend for Python
COPY whitespace-stego-core/ ./whitespace-stego-core/
COPY whitespace-stego-backend/ ./whitespace-stego-backend/
RUN cd whitespace-stego-backend && maturin build --release
RUN pip3 install --no-cache-dir whitespace-stego-backend/target/wheels/*.whl

# Copy notebooks and documentation
COPY *.ipynb ./

# Create convenience scripts
RUN echo '#!/bin/bash\n\
echo "=== Whitespace Steganography Development Environment ==="\n\
echo "Available implementations:"\n\
echo "  Python CLI: python3 -m whitespace_stego.cli --help"\n\
echo "  Rust CLI: ./whitespace-stego-rs --help"\n\
echo "  C CLI: ./c/bin/whitespace-stego --help"\n\
echo ""\n\
echo "Jupyter notebooks available:"\n\
ls -la *.ipynb\n\
echo ""\n\
echo "Run tests: make test"\n\
echo "Start Jupyter: jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"\n\
' > /usr/local/bin/whitespace-stego-help && chmod +x /usr/local/bin/whitespace-stego-help

# Expose Jupyter port
EXPOSE 8888

# Default command
CMD ["/bin/bash"]

# Production stage with minimal runtime
FROM base AS production

# Copy only the built binaries and runtime dependencies
COPY --from=development /workspace/whitespace-stego-rs /usr/local/bin/
COPY --from=development /workspace/c/bin/whitespace-stego /usr/local/bin/
COPY --from=development /workspace/whitespace-stego-backend/target/wheels/ /tmp/wheels/

# Install Python package from wheel
RUN pip3 install --no-cache-dir /tmp/wheels/*.whl

# Create a simple user
RUN useradd -m -s /bin/bash stego
USER stego
WORKDIR /home/stego

# Test stage for CI/CD
FROM development AS test

# Copy test files
COPY tests/ ./tests/
COPY test_*.py ./
COPY pytest.ini ./

# Install test dependencies
RUN pip3 install pytest pytest-cov pytest-html pytest-xdist

# Run tests
CMD ["make", "test"]

# Jupyter stage for interactive development
FROM development AS jupyter

# Install additional Jupyter dependencies
RUN pip3 install --no-cache-dir \
    ipywidgets \
    matplotlib \
    pandas \
    numpy

# Copy notebooks
COPY *.ipynb ./

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"] 