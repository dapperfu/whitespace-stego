# C Implementation Dockerfile
FROM gcc:latest

# Set environment variables
ENV CC=gcc
ENV CXX=g++

# Install system dependencies
RUN apt-get update && apt-get install -y \
    make \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy C source code
COPY c/ ./c/

# Build C implementation
RUN cd c && make clean && make

# Copy binary to system path
RUN cp c/bin/whitespace-stego /usr/local/bin/

# Copy source code for reference
COPY c/ ./c/

# Create data directory
RUN mkdir -p /app/data

# Create convenience script
RUN echo '#!/bin/bash\n\
echo "=== C Whitespace Steganography ==="\n\
echo "Available commands:"\n\
echo "  CLI: whitespace-stego --help"\n\
echo "  Encode: whitespace-stego help encode"\n\
echo "  Decode: whitespace-stego help decode"\n\
echo ""\n\
echo "Examples:"\n\
echo "  whitespace-stego encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt"\n\
echo "  whitespace-stego decode --carrier-file encoded.txt --output decoded.txt"\n\
echo "  whitespace-stego --verbose encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt"\n\
' > /usr/local/bin/c-stego-help && chmod +x /usr/local/bin/c-stego-help

# Default command
CMD ["c-stego-help"] 