#!/bin/bash

# Exit on any error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Test messages
TEST_MESSAGES=(
    "Hello World"
    "Special chars: !@#$%^&*()"
    "Unicode: 你好世界"
    "Emoji: 🌍🌎🌏"
    "Multiline
message
with
newlines"
)

# Test carriers
TEST_CARRIERS=(
    "Simple carrier"
    "Carrier with spaces"
    "Carrier with special chars: !@#$%^&*()"
    "Unicode carrier: 你好世界"
    "Multiline carrier
with
newlines"
)

# Create temporary directory for test files
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "🔍 Testing round-trip compatibility between Python and Rust implementations..."

# Function to run a test case
run_test() {
    local msg="$1"
    local carrier="$2"
    local test_name="$3"
    local password="$4"
    
    echo -e "\n📝 Test: $test_name"
    echo "Message: $msg"
    echo "Carrier: $carrier"
    if [ ! -z "$password" ]; then
        echo "Password: $password"
    fi
    
    # Write message and carrier to temporary files
    echo "$msg" > "$TEMP_DIR/message.txt"
    echo "$carrier" > "$TEMP_DIR/carrier.txt"
    
    # Python encode -> Rust decode
    echo "Testing Python encode -> Rust decode..."
    python3 -m whitespace_stego.cli encode -m "$TEMP_DIR/message.txt" -c "$TEMP_DIR/carrier.txt" -o "$TEMP_DIR/py_encoded.txt" ${password:+-p "$password"}
    ./target/release/whitespace_stego_rs decode -i "$TEMP_DIR/py_encoded.txt" ${password:+-p "$password"} > "$TEMP_DIR/rust_decoded.txt"
    
    if [ "$(cat "$TEMP_DIR/rust_decoded.txt")" = "$msg" ]; then
        echo -e "${GREEN}✓ Python encode -> Rust decode: PASS${NC}"
    else
        echo -e "${RED}✗ Python encode -> Rust decode: FAIL${NC}"
        echo "Expected: $msg"
        echo "Got: $(cat "$TEMP_DIR/rust_decoded.txt")"
        exit 1
    fi
    
    # Rust encode -> Python decode
    echo "Testing Rust encode -> Python decode..."
    ./target/release/whitespace_stego_rs encode -m "$msg" -c "$carrier" -o "$TEMP_DIR/rust_encoded.txt" ${password:+-p "$password"}
    python3 -m whitespace_stego.cli decode -i "$TEMP_DIR/rust_encoded.txt" ${password:+-p "$password"} > "$TEMP_DIR/py_decoded.txt"
    
    if [ "$(cat "$TEMP_DIR/py_decoded.txt")" = "$msg" ]; then
        echo -e "${GREEN}✓ Rust encode -> Python decode: PASS${NC}"
    else
        echo -e "${RED}✗ Rust encode -> Python decode: FAIL${NC}"
        echo "Expected: $msg"
        echo "Got: $(cat "$TEMP_DIR/py_decoded.txt")"
        exit 1
    fi
}

# Run tests without password
for msg in "${TEST_MESSAGES[@]}"; do
    for carrier in "${TEST_CARRIERS[@]}"; do
        run_test "$msg" "$carrier" "Basic test"
    done
done

# Run tests with password
PASSWORD="test_password123"
for msg in "${TEST_MESSAGES[@]}"; do
    for carrier in "${TEST_CARRIERS[@]}"; do
        run_test "$msg" "$carrier" "Password-protected test" "$PASSWORD"
    done
done

# Test with empty carrier
for msg in "${TEST_MESSAGES[@]}"; do
    run_test "$msg" "" "Empty carrier test"
    run_test "$msg" "" "Empty carrier with password" "$PASSWORD"
done

echo -e "\n${GREEN}✅ All tests passed!${NC}" 