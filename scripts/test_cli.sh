#!/bin/bash

# test_cli.sh
# This script tests the command line functionality of whitespace-stego.
# It demonstrates both file input and plain text input, and outputs to stdout.

set -e

# Configuration
MESSAGE="Hello, this is a test message for whitespace-stego CLI."
CARRIER="This is a carrier text. It will be used to hide the message."
MESSAGE_FILE="message.txt"
CARRIER_FILE="carrier.txt"
ENCODED_FILE="encoded.txt"
DECODED_FILE="decoded.txt"

# Clean up any existing files
rm -f "$MESSAGE_FILE" "$CARRIER_FILE" "$ENCODED_FILE" "$DECODED_FILE"

# Create message and carrier files
echo "$MESSAGE" > "$MESSAGE_FILE"
echo "$CARRIER" > "$CARRIER_FILE"

echo "Created message file: $MESSAGE_FILE"
echo "Created carrier file: $CARRIER_FILE"

# Test 1: Encode message from file into carrier file and output to file
echo "Test 1: Encoding message from file into carrier file and output to file..."
venv/bin/whitespace-stego encode -m "$MESSAGE_FILE" -c "$CARRIER_FILE" -o "$ENCODED_FILE"

if [ ! -f "$ENCODED_FILE" ]; then
    echo "Error: Encoded file was not created."
    exit 1
fi
echo "Encoded file created: $ENCODED_FILE"

# Test 2: Decode message from encoded file and output to file
echo "Test 2: Decoding message from encoded file and output to file..."
venv/bin/whitespace-stego decode -i "$ENCODED_FILE" -o "$DECODED_FILE"

if [ ! -f "$DECODED_FILE" ]; then
    echo "Error: Decoded file was not created."
    exit 1
fi
echo "Decoded file created: $DECODED_FILE"

# Verify the decoded message matches the original
DECODED_MESSAGE=$(cat "$DECODED_FILE")
if [ "$DECODED_MESSAGE" = "$MESSAGE" ]; then
    echo "Test 2 passed: Decoded message matches the original message."
else
    echo "Test 2 failed: Decoded message does not match the original message."
    echo "Original message: $MESSAGE"
    echo "Decoded message: $DECODED_MESSAGE"
    exit 1
fi

# Test 3: Encode message from file into plain text carrier and output to stdout
echo "Test 3: Encoding message from file into plain text carrier and output to stdout..."
ENCODED_STDOUT=$(venv/bin/whitespace-stego encode -m "$MESSAGE_FILE" -c "Plain text carrier" -o -)
if [ -z "$ENCODED_STDOUT" ]; then
    echo "Error: No output to stdout."
    exit 1
fi
echo "Encoded output to stdout: $ENCODED_STDOUT"

# Test 4: Decode message from stdin (using the output from Test 3)
echo "Test 4: Decoding message from stdin..."
DECODED_STDOUT=$(echo "$ENCODED_STDOUT" | venv/bin/whitespace-stego decode -i - -o -)
if [ -z "$DECODED_STDOUT" ]; then
    echo "Error: No output to stdout."
    exit 1
fi
echo "Decoded output to stdout: $DECODED_STDOUT"

# Verify the decoded message matches the original
if [ "$DECODED_STDOUT" = "$MESSAGE" ]; then
    echo "Test 4 passed: Decoded message matches the original message."
else
    echo "Test 4 failed: Decoded message does not match the original message."
    echo "Original message: $MESSAGE"
    echo "Decoded message: $DECODED_STDOUT"
    exit 1
fi

echo "CLI test completed successfully." 