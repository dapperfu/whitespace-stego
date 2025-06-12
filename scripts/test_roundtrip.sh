#!/bin/bash

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

    # Encode the message
    echo "Encoding..."
    encoded=$(python3 -c "
from whitespace_stego import encode
print(encode('$message', '$carrier'${password:+, '$password'}))
")

    if [ $? -ne 0 ]; then
        echo -e "${RED}Encoding failed${NC}"
        return 1
    fi

    echo "Encoded: \`$encoded\`"

    # Decode the message
    echo "Decoding..."
    decoded=$(python3 -c "
from whitespace_stego import decode
decoded, _ = decode('$encoded'${password:+, '$password'})
print(decoded)
")

    if [ $? -ne 0 ]; then
        echo -e "${RED}Decoding failed${NC}"
        return 1
    fi

    # Compare original and decoded messages
    if [ "$message" = "$decoded" ]; then
        echo -e "${GREEN}Test passed: Message matches${NC}"
        return 0
    else
        echo -e "${RED}Test failed: Message mismatch${NC}"
        echo "Original: $message"
        echo "Decoded:  $decoded"
        return 1
    fi
}

# Main test loop
echo "Starting round-trip tests..."
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