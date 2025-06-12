#!/bin/bash

# test_matrix.sh
# This script tests the full backend matrix for whitespace-stego.
# It loops over all encode backends (python, rust, c) and all decode backends,
# runs encode, then decode, then compares outputs.
# It fails if any decoded output does not match the original message.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Test cases
declare -a TEST_MESSAGES=(
    "Hello, World!"
    "Hello, 世界!"
    "Hello 👋 World 🌍!"
    "Secret message with password"
)

declare -a TEST_CARRIERS=(
    "This is a test message."
    "This is a 测试 message."
    "This is a test 🎯 message."
    "Public text for secret message"
)

declare -a TEST_PASSWORDS=(
    ""
    ""
    ""
    "password123"
)

# Encode backends
declare -a ENCODE_BACKENDS=(
    "venv/bin/whitespace-stego --backend python"
    "venv/bin/whitespace-stego --backend rust"
    "./whitespace_stego_rs"
    "./whitespace_stego_c"
)

# Decode backends
declare -a DECODE_BACKENDS=(
    "venv/bin/whitespace-stego --backend python"
    "venv/bin/whitespace-stego --backend rust"
    "./whitespace_stego_rs"
    "./whitespace_stego_c"
)

# Function to run a test case
run_test() {
    local message="$1"
    local carrier="$2"
    local password="$3"
    local test_num="$4"

    echo "Test $test_num:"
    echo "Message: $message"
    echo "Carrier: $carrier"
    if [ -n "$password" ]; then
        echo "Password: $password"
    fi

    for encode_backend in "${ENCODE_BACKENDS[@]}"; do
        echo "Encoding with $encode_backend..."
        encoded=$($encode_backend encode -m "$message" -c "$carrier" ${password:+-p "$password"})
        if [ $? -ne 0 ]; then
            echo -e "${RED}Encoding failed with $encode_backend${NC}"
            return 1
        fi
        echo "Encoded: \`$encoded\`"

        for decode_backend in "${DECODE_BACKENDS[@]}"; do
            echo "Decoding with $decode_backend..."
            decoded=$($decode_backend decode -i "$encoded" ${password:+-p "$password"})
            if [ $? -ne 0 ]; then
                echo -e "${RED}Decoding failed with $decode_backend${NC}"
                return 1
            fi

            # Compare original and decoded messages
            if [ "$message" = "$decoded" ]; then
                echo -e "${GREEN}Test passed: Message matches${NC}"
            else
                echo -e "${RED}Test failed: Message mismatch${NC}"
                echo "Original: $message"
                echo "Decoded:  $decoded"
                return 1
            fi
        done
    done
}

# Main test loop
echo "Starting backend matrix tests..."
echo "============================"

failed_tests=0
for i in "${!TEST_MESSAGES[@]}"; do
    echo
    if ! run_test "${TEST_MESSAGES[$i]}" "${TEST_CARRIERS[$i]}" "${TEST_PASSWORDS[$i]}" $((i + 1)); then
        failed_tests=$((failed_tests + 1))
    fi
    echo "============================"
done

# Print summary
echo
if [ $failed_tests -eq 0 ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}$failed_tests test(s) failed${NC}"
    exit 1
fi 