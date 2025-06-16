
FROM python:3.11-slim

# Install build tools
RUN apt-get update && apt-get install -y build-essential python3-dev curl cargo git

# Install maturin
RUN pip install maturin

# Set up workdir
WORKDIR /app

# Copy project files
COPY . .

# Build and install module
RUN make maturin-develop

# Default command
CMD ["python3"]
