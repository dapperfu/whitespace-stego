# Docker Support for Whitespace Steganography

This project provides comprehensive Docker support for all three implementations (Python, Rust, and C) with individual containers for each implementation. This makes the project highly repeatable and accessible across different environments.

## Quick Start

### Prerequisites

- Docker installed on your system
- Docker Compose (usually included with Docker Desktop)

### Individual Implementation Containers

Each implementation has its own dedicated container:

#### Python Implementation

```bash
# Build and run Python container
docker build -f Dockerfile.python -t whitespace-stego-python .
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-python

# Or use Docker Compose
docker-compose -f docker-compose.individual.yml --profile python up python-stego
```

#### Rust Implementation

```bash
# Build and run Rust container
docker build -f Dockerfile.rust -t whitespace-stego-rust .
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-rust

# Or use Docker Compose
docker-compose -f docker-compose.individual.yml --profile rust up rust-stego
```

#### C Implementation

```bash
# Build and run C container
docker build -f Dockerfile.c -t whitespace-stego-c .
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-c

# Or use Docker Compose
docker-compose -f docker-compose.individual.yml --profile c up c-stego
```

## Docker Compose Profiles

The `docker-compose.individual.yml` file provides different profiles for different use cases:

### Available Profiles

- `python` - Python implementation only
- `rust` - Rust implementation only  
- `c` - C implementation only
- `all` - All three implementations
- `jupyter` - Jupyter notebook environment
- `test` - Testing environment
- `compatibility` - Cross-implementation compatibility tests

### Usage Examples

```bash
# Run all implementations
docker-compose -f docker-compose.individual.yml --profile all up

# Run Jupyter notebook environment
docker-compose -f docker-compose.individual.yml --profile jupyter up

# Run tests
docker-compose -f docker-compose.individual.yml --profile test up

# Run compatibility tests
docker-compose -f docker-compose.individual.yml --profile compatibility up
```

## Interactive Usage

### Jupyter Notebooks

Start the Jupyter environment:

```bash
docker-compose -f docker-compose.individual.yml --profile jupyter up
```

Then open your browser to `http://localhost:8888` to access the notebooks.

### Interactive Shell

Get an interactive shell in any container:

```bash
# Python container
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-python /bin/bash

# Rust container
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-rust /bin/bash

# C container
docker run -it --rm -v $(pwd)/data:/app/data whitespace-stego-c /bin/bash
```

## Data Persistence

All containers mount a `./data` directory to `/app/data` inside the container. This allows you to:

- Share files between your host and the containers
- Persist encoded/decoded files
- Work with the same data across different implementations

```bash
# Create data directory
mkdir -p data

# Your files will be available in the container at /app/data
```

## Example Workflows

### 1. Cross-Implementation Testing

```bash
# Create test files
echo "Secret message" > data/message.txt
echo "Hello world" > data/carrier.txt

# Encode with Python
docker run --rm -v $(pwd)/data:/app/data whitespace-stego-python \
  python -m whitespace_stego.cli encode \
  --message-file /app/data/message.txt \
  --carrier-file /app/data/carrier.txt \
  --output /app/data/encoded_python.txt

# Decode with Rust
docker run --rm -v $(pwd)/data:/app/data whitespace-stego-rust \
  whitespace-stego-rs decode \
  --cf /app/data/encoded_python.txt \
  -o /app/data/decoded_rust.txt

# Decode with C
docker run --rm -v $(pwd)/data:/app/data whitespace-stego-c \
  whitespace-stego decode \
  --carrier-file /app/data/encoded_python.txt \
  --output /app/data/decoded_c.txt
```

### 2. Batch Processing

```bash
# Process multiple files with different implementations
for file in data/messages/*.txt; do
  docker run --rm -v $(pwd)/data:/app/data whitespace-stego-python \
    python -m whitespace_stego.cli encode \
    --message-file "/app/data/messages/$(basename $file)" \
    --carrier-file /app/data/carrier.txt \
    --output "/app/data/encoded/$(basename $file .txt)_encoded.txt"
done
```

### 3. Performance Comparison

```bash
# Compare encoding performance across implementations
time docker run --rm -v $(pwd)/data:/app/data whitespace-stego-python \
  python -m whitespace_stego.cli encode \
  --message-file /app/data/large_message.txt \
  --carrier-file /app/data/large_carrier.txt \
  --output /app/data/encoded_python.txt

time docker run --rm -v $(pwd)/data:/app/data whitespace-stego-rust \
  whitespace-stego-rs encode \
  --mf /app/data/large_message.txt \
  --cf /app/data/large_carrier.txt \
  -o /app/data/encoded_rust.txt

time docker run --rm -v $(pwd)/data:/app/data whitespace-stego-c \
  whitespace-stego encode \
  --message-file /app/data/large_message.txt \
  --carrier-file /app/data/large_carrier.txt \
  --output /app/data/encoded_c.txt
```

## Development Workflow

### Building for Development

```bash
# Build with development dependencies
docker build -f Dockerfile.python -t whitespace-stego-python:dev \
  --build-arg BUILD_ENV=development .

# Run with source code mounted for development
docker run -it --rm \
  -v $(pwd):/app \
  -v $(pwd)/data:/app/data \
  whitespace-stego-python:dev /bin/bash
```

### Testing

```bash
# Run all tests
docker-compose -f docker-compose.individual.yml --profile test up

# Run specific test suite
docker run --rm -v $(pwd):/app whitespace-stego-python pytest tests/

# Run compatibility tests
docker-compose -f docker-compose.individual.yml --profile compatibility up
```

## Container Details

### Python Container (`Dockerfile.python`)

- **Base Image**: `python:3.11-slim`
- **Features**:
  - Python CLI with all backends (Python, Rust, C)
  - Jupyter notebook support
  - Full test suite
  - Development tools
- **Ports**: 8888 (Jupyter)
- **Volume**: `/app/data` for file persistence

### Rust Container (`Dockerfile.rust`)

- **Base Image**: `rust:1.75-slim`
- **Features**:
  - Pure Rust CLI implementation
  - Optimized release build
  - Minimal runtime dependencies
- **Volume**: `/app/data` for file persistence

### C Container (`Dockerfile.c`)

- **Base Image**: `gcc:12-slim`
- **Features**:
  - C CLI implementation
  - Compiled binary
  - Minimal runtime dependencies
- **Volume**: `/app/data` for file persistence

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure the `data` directory has proper permissions
   ```bash
   mkdir -p data && chmod 755 data
   ```

2. **Port Already in Use**: Change the Jupyter port
   ```bash
   docker run -p 8889:8888 whitespace-stego-python
   ```

3. **Build Failures**: Clean Docker cache
   ```bash
   docker system prune -a
   ```

4. **Volume Mount Issues**: Use absolute paths
   ```bash
   docker run -v $(pwd)/data:/app/data whitespace-stego-python
   ```

### Debugging

```bash
# Check container logs
docker logs <container_name>

# Inspect container filesystem
docker exec -it <container_name> /bin/bash

# Check container resources
docker stats <container_name>
```

## Performance Considerations

- **Image Size**: Rust and C containers are smaller than Python
- **Build Time**: C container builds fastest, Python slowest
- **Runtime Performance**: Rust typically fastest, Python most flexible
- **Memory Usage**: C container uses least memory

## Security Notes

- Containers run as root by default (consider using non-root users for production)
- Source code is included in containers for development
- Use `.dockerignore` to exclude sensitive files
- Consider using multi-stage builds for production images

## Production Deployment

For production use, consider:

1. **Multi-stage builds** to reduce image size
2. **Non-root users** for security
3. **Health checks** for container monitoring
4. **Resource limits** for stability
5. **Secrets management** for passwords and keys

Example production Dockerfile:

```dockerfile
FROM python:3.11-slim AS production

# Create non-root user
RUN useradd -m -s /bin/bash stego

# Install only runtime dependencies
COPY --from=builder /app/dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl

USER stego
WORKDIR /home/stego

CMD ["python", "-m", "whitespace_stego.cli", "--help"]
``` 