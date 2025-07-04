# Binaries

This directory contains compiled binaries for all implementations.

## Contents

After running `make all`, this directory will contain:

- **whitespace-stego-rs** - Rust CLI binary
- **whitespace-stego-go** - Go CLI binary  
- **whitespace-stego-c** - C CLI binary

## Usage

```bash
# Encode with Rust
./bin/whitespace-stego-rs encode -m "secret" --cf input.txt -o output.txt

# Encode with Go
./bin/whitespace-stego-go encode -m "secret" -cf input.txt -o output.txt

# Encode with C
./bin/whitespace-stego-c encode --message-file message.txt --carrier-file input.txt --output output.txt
```

## Building

Binaries are automatically built when you run:

```bash
make all    # Build all binaries
make rust   # Build Rust binary only
make go     # Build Go binary only
make c      # Build C binary only
```

## Notes

- Binaries are created by the top-level Makefile
- Each binary is self-contained and doesn't require additional dependencies
- All binaries support the same core functionality but with language-specific CLI syntax 