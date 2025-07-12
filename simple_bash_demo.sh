#!/bin/bash

# Simple Bash 101 Demo for Whitespace Steganography
# Uses files to avoid stdout issues

echo "=== Whitespace Steganography - Simple Bash Demo ==="

# Create test files
echo "Hello, World! This is a secret message." > message.txt
echo "This is a carrier text that will contain the hidden message." > carrier.txt
PASSWORD="demo123"

echo "Test message: $(cat message.txt)"
echo "Test carrier: $(cat carrier.txt)"
echo "Test password: $PASSWORD"
echo

# Function to test an implementation
test_impl() {
    local name="$1"
    local encode_cmd="$2"
    local decode_cmd="$3"
    
    echo "--- Testing $name ---"
    
    # Encode
    echo "Encoding..."
    if eval "$encode_cmd"; then
        echo "✓ Encode successful"
    else
        echo "✗ Encode failed"
        return 1
    fi
    
    # Decode
    echo "Decoding..."
    if eval "$decode_cmd"; then
        echo "✓ Decode successful"
    else
        echo "✗ Decode failed"
        return 1
    fi
    
    # Check result
    if [ -f "${name}_decoded.txt" ]; then
        local result=$(cat "${name}_decoded.txt")
        local expected=$(cat message.txt)
        if [ "$result" = "$expected" ]; then
            echo "✓ Roundtrip successful!"
        else
            echo "✗ Roundtrip failed"
            echo "Expected: $expected"
            echo "Got: $result"
        fi
    fi
    echo
}

# Test C implementation (if available)
if [ -f "implementations/c/bin/whitespace-stego-c" ]; then
    test_impl "C" \
        "implementations/c/bin/whitespace-stego-c encode -mf message.txt -cf carrier.txt -o C_encoded.txt -p $PASSWORD" \
        "implementations/c/bin/whitespace-stego-c decode -cf C_encoded.txt -o C_decoded.txt -p $PASSWORD"
fi

# Test C++ implementation (if available)
if [ -f "implementations/cpp/bin/whitespace-stego-cpp" ]; then
    test_impl "CPP" \
        "implementations/cpp/bin/whitespace-stego-cpp encode -mf message.txt -cf carrier.txt -o CPP_encoded.txt -p $PASSWORD" \
        "implementations/cpp/bin/whitespace-stego-cpp decode -cf CPP_encoded.txt -o CPP_decoded.txt -p $PASSWORD"
fi

# Test Python implementation (if available)
if command -v python3 >/dev/null 2>&1 && [ -d "implementations/python" ]; then
    test_impl "PYTHON" \
        "PYTHONPATH=implementations/python python3 -m whitespace_stego.cli encode -mf message.txt -cf carrier.txt -o PYTHON_encoded.txt -p $PASSWORD" \
        "PYTHONPATH=implementations/python python3 -m whitespace_stego.cli decode -cf PYTHON_encoded.txt -o PYTHON_decoded.txt -p $PASSWORD"
fi

# Test Go implementation (if available)
if [ -f "implementations/go/bin/whitespace-stego-go" ]; then
    test_impl "GO" \
        "implementations/go/bin/whitespace-stego-go encode -mf message.txt -cf carrier.txt -o GO_encoded.txt -p $PASSWORD" \
        "implementations/go/bin/whitespace-stego-go decode -cf GO_encoded.txt -o GO_decoded.txt -p $PASSWORD"
fi

# Test Rust implementation (if available)
if [ -f "implementations/rust/target/release/whitespace-stego-rs" ]; then
    test_impl "RUST" \
        "implementations/rust/target/release/whitespace-stego-rs encode -m \"$(cat message.txt)\" --cf carrier.txt -o RUST_encoded.txt -p $PASSWORD" \
        "implementations/rust/target/release/whitespace-stego-rs decode --cf RUST_encoded.txt -o RUST_decoded.txt -p $PASSWORD"
fi

echo "=== Demo Complete ==="
echo "Files created:"
ls -la message.txt carrier.txt *_encoded.txt *_decoded.txt 2>/dev/null || echo "No files found"

echo
echo "To clean up: rm -f message.txt carrier.txt *_encoded.txt *_decoded.txt" 