#!/bin/bash
# Basic usage examples for whitespace-stego CLI

echo "=== Whitespace Steganography CLI - Basic Usage Examples ==="
echo

# Example 1: Basic encode/decode
echo "1. Basic encode/decode:"
echo "Message: 'Hello, World!'"
echo "Carrier: 'This is a test message.'"
echo

# Encode
echo "Encoding..."
echo "Hello, World!" > message.txt
echo "This is a test message." > carrier.txt
whitespace-stego encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt

# Decode
echo "Decoding..."
whitespace-stego decode --carrier-file encoded.txt --output decoded.txt

echo "Original message:"
cat message.txt
echo
echo "Decoded message:"
cat decoded.txt
echo

# Example 2: With password
echo "2. Encode/decode with password:"
echo "Message: 'Secret message'"
echo "Password: 'mypassword'"
echo

# Encode with password
echo "Encoding with password..."
echo "Secret message" > secret_message.txt
whitespace-stego encode --message-file secret_message.txt --carrier-file carrier.txt --password mypassword --output secret_encoded.txt

# Decode with password
echo "Decoding with password..."
whitespace-stego decode --carrier-file secret_encoded.txt --password mypassword --output secret_decoded.txt

echo "Original secret message:"
cat secret_message.txt
echo
echo "Decoded secret message:"
cat secret_decoded.txt
echo

# Example 3: Interactive mode
echo "3. Interactive mode:"
echo "You can also use interactive mode:"
echo "whitespace-stego encode --interactive"
echo "whitespace-stego decode --interactive"
echo

# Example 4: Analyze text
echo "4. Analyze text for encoded messages:"
echo "Analyzing encoded text..."
whitespace-stego analyze --file encoded.txt
echo

# Example 5: Extract encoded message
echo "5. Extract encoded message and remaining carrier:"
echo "Extracting..."
whitespace-stego extract --carrier-file encoded.txt --output-dir extracted
echo "Files created in 'extracted' directory:"
ls -la extracted/
echo

# Cleanup
echo "Cleaning up..."
rm -f message.txt carrier.txt encoded.txt decoded.txt
rm -f secret_message.txt secret_encoded.txt secret_decoded.txt
rm -rf extracted

echo "=== Examples completed ===" 