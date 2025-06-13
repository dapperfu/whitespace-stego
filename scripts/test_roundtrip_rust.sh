#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Function to run a test case for a given backend
run_test_backend() {
    local backend="$1"
    local message="$2"
    local carrier="$3"
    local password="$4"
    local test_num="$5"

    echo "  Backend: $backend"
    # Encode the message
    encoded=$(python3 -c "
from whitespace_stego.encode import encode_and_insert
print(encode_and_insert('$message', '$carrier'${password:+, '$password'}, backend='$backend'))
")
    if [ $? -ne 0 ]; then
        echo -e "${RED}    Encoding failed${NC}"
        return 1
    fi
    echo "    Encoded: \`$encoded\`"
    # Decode the message
    decoded=$(python3 -c "
from whitespace_stego.decode import decode_and_remove
decoded, _ = decode_and_remove('$encoded'${password:+, '$password'}, backend='$backend')
print(decoded)
")
    if [ $? -ne 0 ]; then
        echo -e "${RED}    Decoding failed${NC}"
        return 1
    fi
    # Compare original and decoded messages
    if [ "$message" = "$decoded" ]; then
        echo -e "${GREEN}    Test passed: Message matches${NC}"
        return 0
    else
        echo -e "${RED}    Test failed: Message mismatch${NC}"
        echo "    Original: $message"
        echo "    Decoded:  $decoded"
        return 1
    fi
}

# Function to run a test case for both backends
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
    failed=0
    for backend in python rust; do
        if ! run_test_backend "$backend" "$message" "$carrier" "$password" "$test_num"; then
            failed=1
        fi
    done
    echo "============================"
    return $failed
}

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

# Main test loop
echo "Starting round-trip tests for Python and Rust backends..."
echo "============================"

failed_tests=0
for i in "${!TEST_MESSAGES[@]}"; do
    echo
    if ! run_test "${TEST_MESSAGES[$i]}" "${TEST_CARRIERS[$i]}" "${TEST_PASSWORDS[$i]}" $((i + 1)); then
        failed_tests=$((failed_tests + 1))
    fi
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