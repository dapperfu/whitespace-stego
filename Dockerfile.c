# Use the base image
FROM whitespace-stego:base as base

# Create a C build stage
FROM base AS c-build

WORKDIR /workspace

# Copy C files and build the binary
COPY c/ ./c/
RUN cd c && make

# Create a final, smaller image
FROM base AS final

WORKDIR /app

# Copy the built binary from the build stage
COPY --from=c-build /workspace/c/bin/whitespace-stego /usr/local/bin/

CMD ["whitespace-stego", "--help"] 