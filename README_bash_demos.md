# Bash 101 Demo Scripts

This directory contains simple bash scripts that demonstrate encoding and decoding using each implementation of the whitespace steganography project.

## Scripts

### `simple_bash_demo.sh`
A simple bash script that demonstrates encoding and decoding using each available implementation. Uses file-based I/O to avoid stdout issues.

**Features:**
- Tests all available implementations (C, C++, Python, Go, Rust)
- Uses files for input/output to avoid bash stdout issues
- Verifies roundtrip functionality (encode → decode → verify)
- Color-coded output for easy reading
- Automatic cleanup instructions

**Usage:**
```bash
./simple_bash_demo.sh
```

### `bash_101_demo.sh`
A more comprehensive bash script with additional features like:
- Detailed status checking for each implementation
- Better error handling
- More verbose output
- Implementation availability detection

**Usage:**
```bash
./bash_101_demo.sh
```

## How It Works

Both scripts follow the same basic pattern:

1. **Create test files**: Generate a message and carrier text
2. **Test each implementation**: For each available implementation:
   - Encode the message into the carrier
   - Decode the message from the encoded carrier
   - Verify the decoded message matches the original
3. **Report results**: Show success/failure for each implementation

## File Structure

The scripts create the following files:
- `message.txt` - The secret message to encode
- `carrier.txt` - The carrier text to hide the message in
- `*_encoded.txt` - Encoded output from each implementation
- `*_decoded.txt` - Decoded output from each implementation

## Implementation Commands

Each implementation is tested with these equivalent commands:

### C Implementation
```bash
implementations/c/bin/whitespace-stego-c encode -mf message.txt -cf carrier.txt -o C_encoded.txt -p password
implementations/c/bin/whitespace-stego-c decode -cf C_encoded.txt -o C_decoded.txt -p password
```

### C++ Implementation
```bash
implementations/cpp/bin/whitespace-stego-cpp encode -mf message.txt -cf carrier.txt -o CPP_encoded.txt -p password
implementations/cpp/bin/whitespace-stego-cpp decode -cf CPP_encoded.txt -o CPP_decoded.txt -p password
```

### Python Implementation
```bash
PYTHONPATH=implementations/python python3 -m whitespace_stego.cli encode -mf message.txt -cf carrier.txt -o PYTHON_encoded.txt -p password
PYTHONPATH=implementations/python python3 -m whitespace_stego.cli decode -cf PYTHON_encoded.txt -o PYTHON_decoded.txt -p password
```

### Go Implementation
```bash
implementations/go/bin/whitespace-stego-go encode -mf message.txt -cf carrier.txt -o GO_encoded.txt -p password
implementations/go/bin/whitespace-stego-go decode -cf GO_encoded.txt -o GO_decoded.txt -p password
```

### Rust Implementation
```bash
implementations/rust/target/release/whitespace-stego-rs encode -m "message" --cf carrier.txt -o RUST_encoded.txt -p password
implementations/rust/target/release/whitespace-stego-rs decode --cf RUST_encoded.txt -o RUST_decoded.txt -p password
```

## Requirements

- Bash shell
- Built implementations (C, C++, Python, Go, Rust binaries)
- Python 3 (for Python implementation)

## Cleanup

To clean up all test files:
```bash
rm -f message.txt carrier.txt *_encoded.txt *_decoded.txt
```

## Notes

- The scripts use file-based I/O to avoid issues with bash stdout handling
- Each implementation is tested independently
- The scripts check for implementation availability before testing
- All implementations should produce compatible results (same encoding/decoding)
- The test message and carrier are simple ASCII text for compatibility 