#!/bin/bash

# Test script for Go implementation
set -e

BIN="../bin/whitespace-stego-go"
TEST_DIR="$(dirname "$0")"

echo "Running Go implementation tests..."

# Check if binary exists
if [ ! -f "$BIN" ]; then
    echo "Error: Binary not found at $BIN"
    echo "Please run 'make build' first"
    exit 1
fi

# Test 1: Basic encode/decode without password
echo "Test 1: Basic encode/decode without password"
MESSAGE="Hello, World!"
CARRIER="This is a test message."

ENCODED=$($BIN encode -m "$MESSAGE" -c "$CARRIER")
DECODED=$($BIN decode -c "$ENCODED")

if [ "$DECODED" = "$MESSAGE" ]; then
    echo "✓ Basic encode/decode test passed"
else
    echo "✗ Basic encode/decode test failed"
    echo "Expected: $MESSAGE"
    echo "Got: $DECODED"
    exit 1
fi

# Test 2: Encode/decode with password
echo "Test 2: Encode/decode with password"
PASSWORD="secret123"

ENCODED_PW=$($BIN encode -m "$MESSAGE" -c "$CARRIER" -p "$PASSWORD")
DECODED_PW=$($BIN decode -c "$ENCODED_PW" -p "$PASSWORD")

if [ "$DECODED_PW" = "$MESSAGE" ]; then
    echo "✓ Password-protected encode/decode test passed"
else
    echo "✗ Password-protected encode/decode test failed"
    echo "Expected: $MESSAGE"
    echo "Got: $DECODED_PW"
    exit 1
fi

# Test 3: Empty carrier
echo "Test 3: Empty carrier"
ENCODED_EMPTY=$($BIN encode -m "$MESSAGE" -c "")
DECODED_EMPTY=$($BIN decode -c "$ENCODED_EMPTY")

if [ "$DECODED_EMPTY" = "$MESSAGE" ]; then
    echo "✓ Empty carrier test passed"
else
    echo "✗ Empty carrier test failed"
    echo "Expected: $MESSAGE"
    echo "Got: $DECODED_EMPTY"
    exit 1
fi

# Test 4: Unicode/emoji support
echo "Test 4: Unicode/emoji support"
UNICODE_MSG="Hello 世界! 😀"
ENCODED_UNICODE=$($BIN encode -m "$UNICODE_MSG" -c "$CARRIER")
DECODED_UNICODE=$($BIN decode -c "$ENCODED_UNICODE")

if [ "$DECODED_UNICODE" = "$UNICODE_MSG" ]; then
    echo "✓ Unicode/emoji test passed"
else
    echo "✗ Unicode/emoji test failed"
    echo "Expected: $UNICODE_MSG"
    echo "Got: $DECODED_UNICODE"
    exit 1
fi

# Test 5: File I/O
echo "Test 5: File I/O"
echo "$MESSAGE" > "$TEST_DIR/test_message.txt"
echo "$CARRIER" > "$TEST_DIR/test_carrier.txt"

ENCODED_FILE=$($BIN encode -mf "$TEST_DIR/test_message.txt" -cf "$TEST_DIR/test_carrier.txt")
echo "$ENCODED_FILE" > "$TEST_DIR/test_encoded.txt"
DECODED_FILE=$($BIN decode -cf "$TEST_DIR/test_encoded.txt")

if [ "$DECODED_FILE" = "$MESSAGE" ]; then
    echo "✓ File I/O test passed"
else
    echo "✗ File I/O test failed"
    echo "Expected: $MESSAGE"
    echo "Got: $DECODED_FILE"
    exit 1
fi

# Cleanup test files
rm -f "$TEST_DIR/test_message.txt" "$TEST_DIR/test_carrier.txt" "$TEST_DIR/test_encoded.txt"

echo "All tests passed!" 