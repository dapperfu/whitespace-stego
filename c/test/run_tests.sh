#!/bin/bash

BIN="bin/whitespace-stego"

# Test cases
test_encode_decode() {
    local message="Hello, World!"
    local carrier="This is a test message."
    local password="test123"

    # Test encoding
    local encoded=$(echo "$carrier" | $BIN -e "$message" -p "$password")
    if [ $? -ne 0 ]; then
        echo "Error: Encoding failed"
        return 1
    fi

    # Test decoding
    local decoded=$(echo "$encoded" | $BIN -d -p "$password")
    if [ $? -ne 0 ]; then
        echo "Error: Decoding failed"
        return 1
    fi

    if [ "$decoded" != "$message" ]; then
        echo "Error: Decoded message doesn't match original"
        echo "Expected: $message"
        echo "Got: $decoded"
        return 1
    fi

    echo "Test passed: encode/decode with password"
    return 0
}

test_encode_decode_no_password() {
    local message="Hello, World!"
    local carrier="This is a test message."

    # Test encoding
    local encoded=$(echo "$carrier" | $BIN -e "$message")
    if [ $? -ne 0 ]; then
        echo "Error: Encoding failed"
        return 1
    fi

    # Test decoding
    local decoded=$(echo "$encoded" | $BIN -d)
    if [ $? -ne 0 ]; then
        echo "Error: Decoding failed"
        return 1
    fi

    if [ "$decoded" != "$message" ]; then
        echo "Error: Decoded message doesn't match original"
        echo "Expected: $message"
        echo "Got: $decoded"
        return 1
    fi

    echo "Test passed: encode/decode without password"
    return 0
}

test_invalid_password() {
    local message="Hello, World!"
    local carrier="This is a test message."
    local password="test123"
    local wrong_password="wrong123"

    # Test encoding
    local encoded=$(echo "$carrier" | $BIN -e "$message" -p "$password")
    if [ $? -ne 0 ]; then
        echo "Error: Encoding failed"
        return 1
    fi

    # Test decoding with wrong password
    local output
    output=$(echo "$encoded" | $BIN -d -p "$wrong_password" 2>&1)
    if [ $? -eq 0 ]; then
        echo "Error: Decoding succeeded with wrong password"
        return 1
    fi
    if [[ "$output" != *"wrong password"* && "$output" != *"Decryption failed"* ]]; then
        echo "Error: Wrong password error not reported"
        echo "Output: $output"
        return 1
    fi

    echo "Test passed: invalid password detection"
    return 0
}

test_insufficient_space() {
    local message="This is a very long message that should not fit in the carrier text."
    local carrier="A"

    # Test encoding
    local encoded=$(echo "$carrier" | $BIN -e "$message" 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo "Error: Encoding succeeded with insufficient space"
        return 1
    fi

    echo "Test passed: insufficient space detection"
    return 0
}

test_unicode() {
    local message="Hello, 世界!"
    local carrier="This is a test message."
    local password="test123"

    # Test encoding
    local encoded=$(echo "$carrier" | $BIN -e "$message" -p "$password")
    if [ $? -ne 0 ]; then
        echo "Error: Encoding failed with Unicode"
        return 1
    fi

    # Test decoding
    local decoded=$(echo "$encoded" | $BIN -d -p "$password")
    if [ $? -ne 0 ]; then
        echo "Error: Decoding failed with Unicode"
        return 1
    fi

    if [ "$decoded" != "$message" ]; then
        echo "Error: Decoded Unicode message doesn't match original"
        echo "Expected: $message"
        echo "Got: $decoded"
        return 1
    fi

    echo "Test passed: Unicode support"
    return 0
}

# Run all tests
echo "Running tests..."

test_encode_decode
test_encode_decode_no_password
test_invalid_password
test_insufficient_space
test_unicode

echo "All tests completed" 