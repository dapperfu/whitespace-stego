#!/bin/bash

# Whitespace Steganography - Bash 101 Demo Script
# Demonstrates encoding and decoding using each implementation

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test files
TEST_MESSAGE="Hello, World! This is a secret message from bash demo."
TEST_CARRIER="This is a carrier text that will contain the hidden message. It can be any text that looks normal."
TEST_PASSWORD="demo_password_123"

# Create test files
echo "$TEST_MESSAGE" > test_message.txt
echo "$TEST_CARRIER" > test_carrier.txt

echo -e "${BLUE}=== Whitespace Steganography Bash 101 Demo ===${NC}"
echo -e "${YELLOW}Test message:${NC} $TEST_MESSAGE"
echo -e "${YELLOW}Test carrier:${NC} $TEST_CARRIER"
echo -e "${YELLOW}Test password:${NC} $TEST_PASSWORD"
echo

# Function to test an implementation
test_implementation() {
    local name="$1"
    local encode_cmd="$2"
    local decode_cmd="$3"
    
    echo -e "${BLUE}--- Testing $name Implementation ---${NC}"
    
    # Clean up previous test files
    rm -f ${name}_encoded.txt ${name}_decoded.txt
    
    # Encode
    echo -e "${YELLOW}Encoding...${NC}"
    if eval "$encode_cmd"; then
        echo -e "${GREEN}✓ Encoding successful${NC}"
    else
        echo -e "${RED}✗ Encoding failed${NC}"
        return 1
    fi
    
    # Decode
    echo -e "${YELLOW}Decoding...${NC}"
    if eval "$decode_cmd"; then
        echo -e "${GREEN}✓ Decoding successful${NC}"
    else
        echo -e "${RED}✗ Decoding failed${NC}"
        return 1
    fi
    
    # Verify result
    if [ -f "${name}_decoded.txt" ]; then
        local decoded_content=$(cat "${name}_decoded.txt")
        if [ "$decoded_content" = "$TEST_MESSAGE" ]; then
            echo -e "${GREEN}✓ Roundtrip successful - message matches!${NC}"
        else
            echo -e "${RED}✗ Roundtrip failed - message mismatch${NC}"
            echo "Expected: $TEST_MESSAGE"
            echo "Got: $decoded_content"
        fi
    else
        echo -e "${RED}✗ No decoded file found${NC}"
    fi
    
    echo
}

# Check if implementations are built/available
check_implementation() {
    local name="$1"
    local binary="$2"
    
    if [ -f "$binary" ] || command -v "$binary" >/dev/null 2>&1; then
        echo -e "${GREEN}✓ $name available${NC}"
        return 0
    else
        echo -e "${RED}✗ $name not available${NC}"
        return 1
    fi
}

echo -e "${BLUE}=== Checking Available Implementations ===${NC}"

# Check C implementation
if check_implementation "C" "implementations/c/bin/whitespace-stego"; then
    C_AVAILABLE=true
else
    C_AVAILABLE=false
fi

# Check C++ implementation
if check_implementation "C++" "implementations/cpp/bin/whitespace-stego-cpp"; then
    CPP_AVAILABLE=true
else
    CPP_AVAILABLE=false
fi

# Check Python implementation
if command -v python3 >/dev/null 2>&1 && [ -d "implementations/python" ]; then
    echo -e "${GREEN}✓ Python available${NC}"
    PYTHON_AVAILABLE=true
else
    echo -e "${RED}✗ Python not available${NC}"
    PYTHON_AVAILABLE=false
fi

# Check Go implementation
if check_implementation "Go" "implementations/go/bin/whitespace-stego-go"; then
    GO_AVAILABLE=true
else
    GO_AVAILABLE=false
fi

# Check Rust implementation
if check_implementation "Rust" "implementations/rust/target/release/whitespace-stego-rs"; then
    RUST_AVAILABLE=true
else
    RUST_AVAILABLE=false
fi

echo

# Test implementations if available
if [ "$C_AVAILABLE" = true ]; then
    test_implementation "C" \
        "implementations/c/bin/whitespace-stego encode -mf test_message.txt -cf test_carrier.txt -o C_encoded.txt -p $TEST_PASSWORD" \
        "implementations/c/bin/whitespace-stego decode -cf C_encoded.txt -o C_decoded.txt -p $TEST_PASSWORD"
fi

if [ "$CPP_AVAILABLE" = true ]; then
    test_implementation "C++" \
        "implementations/cpp/bin/whitespace-stego-cpp encode -mf test_message.txt -cf test_carrier.txt -o CPP_encoded.txt -p $TEST_PASSWORD" \
        "implementations/cpp/bin/whitespace-stego-cpp decode -cf CPP_encoded.txt -o CPP_decoded.txt -p $TEST_PASSWORD"
fi

if [ "$PYTHON_AVAILABLE" = true ]; then
    test_implementation "Python" \
        "cd implementations/python && python3 -m whitespace_stego.cli encode -mf ../../test_message.txt -cf ../../test_carrier.txt -o ../../PYTHON_encoded.txt -p $TEST_PASSWORD" \
        "cd implementations/python && python3 -m whitespace_stego.cli decode -cf ../../PYTHON_encoded.txt -o ../../PYTHON_decoded.txt -p $TEST_PASSWORD"
fi

if [ "$GO_AVAILABLE" = true ]; then
    test_implementation "Go" \
        "implementations/go/bin/whitespace-stego-go encode -mf test_message.txt -cf test_carrier.txt -o GO_encoded.txt -p $TEST_PASSWORD" \
        "implementations/go/bin/whitespace-stego-go decode -cf GO_encoded.txt -o GO_decoded.txt -p $TEST_PASSWORD"
fi

if [ "$RUST_AVAILABLE" = true ]; then
    test_implementation "Rust" \
        "implementations/rust/target/release/whitespace-stego-rs encode -m \"$TEST_MESSAGE\" -cf test_carrier.txt -o RUST_encoded.txt -p $TEST_PASSWORD" \
        "implementations/rust/target/release/whitespace-stego-rs decode -cf RUST_encoded.txt -o RUST_decoded.txt -p $TEST_PASSWORD"
fi

echo -e "${BLUE}=== Demo Complete ===${NC}"
echo -e "${YELLOW}Test files created:${NC}"
ls -la test_*.txt *_encoded.txt *_decoded.txt 2>/dev/null || echo "No test files found"

echo -e "${YELLOW}To clean up test files, run:${NC}"
echo "rm -f test_*.txt *_encoded.txt *_decoded.txt" 