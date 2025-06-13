#!/bin/bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test directory
TEST_DIR="test_output"
mkdir -p "$TEST_DIR"

# Function to run a test and check its output
run_test() {
    local test_name="$1"
    local command="$2"
    local expected_output="$3"
    local actual_output

    echo "Running test: $test_name"
    actual_output=$(eval "$command")
    
    if [ "$actual_output" = "$expected_output" ]; then
        echo -e "${GREEN}✓ Test passed: $test_name${NC}"
    else
        echo -e "${RED}✗ Test failed: $test_name${NC}"
        echo "Expected: $expected_output"
        echo "Got: $actual_output"
        exit 1
    fi
}

# Function to test roundtrip encoding/decoding between implementations
test_roundtrip() {
    local test_name="$1"
    local message="$2"
    local password="$3"
    local carrier="$4"
    
    echo -e "\n${YELLOW}Running roundtrip test: $test_name${NC}"
    
    # Build command options
    local py_opts=""
    local go_opts=""
    if [ -n "$password" ]; then
        py_opts="$py_opts --password '$password'"
        go_opts="$go_opts -p '$password'"
    fi
    if [ -n "$carrier" ]; then
        py_opts="$py_opts --carrier '$carrier'"
        go_opts="$go_opts -c '$carrier'"
    fi

    # Test Python (pure) -> Go
    echo "Testing Python (pure) -> Go..."
    encoded=$(echo "$message" | python3 -m whitespace_stego.cli encode $py_opts --backend python)
    echo "Encoded output: [$encoded]"
    decoded=$(echo "$encoded" | ./bin/whitespace-stego-go decode $go_opts)
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ Python (pure) -> Go passed${NC}"
    else
        echo -e "${RED}✗ Python (pure) -> Go failed${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi

    # Test Python (rust) -> Go
    echo "Testing Python (rust) -> Go..."
    encoded=$(echo "$message" | python3 -m whitespace_stego.cli encode $py_opts --backend rust)
    decoded=$(echo "$encoded" | ./bin/whitespace-stego-go decode $go_opts)
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ Python (rust) -> Go passed${NC}"
    else
        echo -e "${RED}✗ Python (rust) -> Go failed${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi

    # Test Go -> Python (pure)
    echo "Testing Go -> Python (pure)..."
    encoded=$(echo "$message" | ./bin/whitespace-stego-go encode $go_opts)
    decoded=$(echo "$encoded" | python3 -m whitespace_stego.cli decode $py_opts --backend python)
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ Go -> Python (pure) passed${NC}"
    else
        echo -e "${RED}✗ Go -> Python (pure) failed${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi

    # Test Go -> Python (rust)
    echo "Testing Go -> Python (rust)..."
    encoded=$(echo "$message" | ./bin/whitespace-stego-go encode $go_opts)
    decoded=$(echo "$encoded" | python3 -m whitespace_stego.cli decode $py_opts --backend rust)
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ Go -> Python (rust) passed${NC}"
    else
        echo -e "${RED}✗ Go -> Python (rust) failed${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi

    echo -e "${GREEN}✓ All roundtrip tests passed for: $test_name${NC}"
}

# Build the Go CLI
echo "Building Go CLI..."
make go-cli

# Test basic encoding/decoding
test_roundtrip "Basic ASCII" "Hello, World!" "" ""
test_roundtrip "Unicode" "Hello, 世界!" "" ""
test_roundtrip "Empty message" "" "" ""

# Test with passwords
test_roundtrip "With password" "Secret message" "mypassword" ""
test_roundtrip "With password and Unicode" "Secret 世界" "mypassword" ""

# Test with carrier text
test_roundtrip "With carrier" "Secret message" "" "This is a carrier text"
test_roundtrip "With carrier and password" "Secret message" "mypassword" "This is a carrier text"

# Test with longer messages
test_roundtrip "Long message" "This is a longer message that tests the handling of multiple blocks and ensures proper encoding/decoding across implementations. It includes various characters and spaces to test edge cases." "" ""
test_roundtrip "Long message with password" "This is a longer message that tests the handling of multiple blocks and ensures proper encoding/decoding across implementations. It includes various characters and spaces to test edge cases." "mypassword" ""

# Clean up
rm -rf "$TEST_DIR"

echo -e "\n${GREEN}All bi-directional tests passed!${NC}" 