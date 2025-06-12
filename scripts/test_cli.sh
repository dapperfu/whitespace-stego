#!/bin/bash

# test_cli.sh
# This script tests the command line functionality of whitespace-stego.
# It encodes a message into a carrier file and then decodes it, verifying that the decoded message matches the original.

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

# Encode the message into the carrier
echo "Encoding message into carrier..."
venv/bin/whitespace-stego encode -m "$MESSAGE_FILE" -c "$CARRIER_FILE" -o "$ENCODED_FILE"

if [ ! -f "$ENCODED_FILE" ]; then
    echo "Error: Encoded file was not created."
    exit 1
fi
echo "Encoded file created: $ENCODED_FILE"

# Decode the message from the encoded file
echo "Decoding message from encoded file..."
venv/bin/whitespace-stego decode -i "$ENCODED_FILE" -o "$DECODED_FILE"

if [ ! -f "$DECODED_FILE" ]; then
    echo "Error: Decoded file was not created."
    exit 1
fi
echo "Decoded file created: $DECODED_FILE"

# Verify the decoded message matches the original
DECODED_MESSAGE=$(cat "$DECODED_FILE")
if [ "$DECODED_MESSAGE" = "$MESSAGE" ]; then
    echo "Test passed: Decoded message matches the original message."
else
    echo "Test failed: Decoded message does not match the original message."
    echo "Original message: $MESSAGE"
    echo "Decoded message: $DECODED_MESSAGE"
    exit 1
fi

echo "CLI test completed successfully." 