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

# Function to clean up existing files
cleanup() {
    rm -f "$MESSAGE_FILE" "$CARRIER_FILE" "$ENCODED_FILE" "$DECODED_FILE"
}

# Function to create message and carrier files
create_files() {
    echo "$MESSAGE" > "$MESSAGE_FILE"
    echo "$CARRIER" > "$CARRIER_FILE"
    echo "Created message file: $MESSAGE_FILE"
    echo "Created carrier file: $CARRIER_FILE"
}

# Function to encode a message into a carrier
encode_message() {
    local message_file="$1"
    local carrier_file="$2"
    local output_file="$3"
    echo "Encoding message from $message_file into carrier $carrier_file and output to $output_file..."
    venv/bin/whitespace-stego encode -m "$message_file" -c "$carrier_file" -o "$output_file"
    if [ ! -f "$output_file" ]; then
        echo "Error: Encoded file was not created."
        exit 1
    fi
    echo "Encoded file created: $output_file"
}

# Function to decode a message from an encoded file
decode_message() {
    local input_file="$1"
    local output_file="$2"
    echo "Decoding message from $input_file and output to $output_file..."
    venv/bin/whitespace-stego decode -i "$input_file" -o "$output_file"
    if [ ! -f "$output_file" ]; then
        echo "Error: Decoded file was not created."
        exit 1
    fi
    echo "Decoded file created: $output_file"
}

# Function to verify the decoded message matches the original
verify_message() {
    local original_message="$1"
    local decoded_file="$2"
    local decoded_message=$(cat "$decoded_file")
    if [ "$decoded_message" = "$original_message" ]; then
        echo "Test passed: Decoded message matches the original message."
    else
        echo "Test failed: Decoded message does not match the original message."
        echo "Original message: $original_message"
        echo "Decoded message: $decoded_message"
        exit 1
    fi
}

# Main script execution
cleanup
create_files

# Test 1: Encode message from file into carrier file and output to file
encode_message "$MESSAGE_FILE" "$CARRIER_FILE" "$ENCODED_FILE"

# Test 2: Decode message from encoded file and output to file
decode_message "$ENCODED_FILE" "$DECODED_FILE"
verify_message "$MESSAGE" "$DECODED_FILE"

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