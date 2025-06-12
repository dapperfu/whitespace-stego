#!/bin/bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
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

# Function to test roundtrip encoding/decoding
test_roundtrip() {
    local test_name="$1"
    local message="$2"
    local password="$3"
    local carrier="$4"
    
    echo "Running roundtrip test: $test_name"
    
    # Build the encode command
    local encode_cmd="./bin/whitespace-stego-go encode"
    if [ -n "$password" ]; then
        encode_cmd="$encode_cmd -p '$password'"
    fi
    if [ -n "$carrier" ]; then
        encode_cmd="$encode_cmd -c '$carrier'"
    fi
    
    # Encode the message
    local encoded
    encoded=$(echo "$message" | eval "$encode_cmd")
    
    # Build the decode command
    local decode_cmd="./bin/whitespace-stego-go decode"
    if [ -n "$password" ]; then
        decode_cmd="$decode_cmd -p '$password'"
    fi
    
    # Decode the message
    local decoded
    decoded=$(echo "$encoded" | eval "$decode_cmd")
    
    # Check if the decoded message matches the original
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ Roundtrip test passed: $test_name${NC}"
    else
        echo -e "${RED}✗ Roundtrip test failed: $test_name${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi
}

# Function to test file operations
test_file_operations() {
    local test_name="$1"
    local message="$2"
    local password="$3"
    
    echo "Running file operation test: $test_name"
    
    # Write message to input file
    echo "$message" > "$TEST_DIR/input.txt"
    
    # Build the encode command
    local encode_cmd="./bin/whitespace-stego-go encode -i '$TEST_DIR/input.txt' -o '$TEST_DIR/encoded.txt'"
    if [ -n "$password" ]; then
        encode_cmd="$encode_cmd -p '$password'"
    fi
    
    # Encode the message
    eval "$encode_cmd"
    
    # Build the decode command
    local decode_cmd="./bin/whitespace-stego-go decode -i '$TEST_DIR/encoded.txt' -o '$TEST_DIR/decoded.txt'"
    if [ -n "$password" ]; then
        decode_cmd="$decode_cmd -p '$password'"
    fi
    
    # Decode the message
    eval "$decode_cmd"
    
    # Check if the decoded message matches the original
    local decoded
    decoded=$(cat "$TEST_DIR/decoded.txt")
    
    if [ "$decoded" = "$message" ]; then
        echo -e "${GREEN}✓ File operation test passed: $test_name${NC}"
    else
        echo -e "${RED}✗ File operation test failed: $test_name${NC}"
        echo "Original: $message"
        echo "Decoded: $decoded"
        exit 1
    fi
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

# Test file operations
test_file_operations "File operations - ASCII" "Hello, World!" ""
test_file_operations "File operations - Unicode" "Hello, 世界!" ""
test_file_operations "File operations - With password" "Secret message" "mypassword"

# Test command-line arguments
run_test "Command-line argument encoding" "./bin/whitespace-stego-go encode 'Hello, World!'" "$(echo 'Hello, World!' | ./bin/whitespace-stego-go encode)"
run_test "Command-line argument with password" "./bin/whitespace-stego-go encode -p 'mypassword' 'Secret message'" "$(echo 'Secret message' | ./bin/whitespace-stego-go encode -p 'mypassword')"

# Test wrong password
echo "Testing wrong password..."
encoded=$(echo "Secret message" | ./bin/whitespace-stego-go encode -p "correct123")
if echo "$encoded" | ./bin/whitespace-stego-go decode -p "wrong123" 2>/dev/null; then
    echo -e "${RED}✗ Wrong password test failed: Decoding should fail with wrong password${NC}"
    exit 1
else
    echo -e "${GREEN}✓ Wrong password test passed${NC}"
fi

# Clean up
rm -rf "$TEST_DIR"

echo -e "\n${GREEN}All tests passed!${NC}" 