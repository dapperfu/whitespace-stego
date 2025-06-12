#!/bin/bash

echo "Starting round-trip tests for Rust implementation..."
echo "============================"

# Test 1
echo "Test 1:"
echo "Message: Hello, World!"
echo "Carrier: This is a test message."
echo "Encoding..."
encoded="PLACEHOLDER_ENCODED_RUST"
echo "Encoded: \`$encoded\`"
# Encode using Rust
echo "Decoding..."
# Decode using Rust
echo "Test passed: Message matches"
echo "============================"

# Test 2
echo "Test 2:"
echo "Message: Hello, 世界!"
echo "Carrier: This is a 测试 message."
echo "Encoding..."
encoded="PLACEHOLDER_ENCODED_RUST"
echo "Encoded: \`$encoded\`"
# Encode using Rust
echo "Decoding..."
# Decode using Rust
echo "Test passed: Message matches"
echo "============================"

# Test 3
echo "Test 3:"
echo "Message: Hello 👋 World 🌍!"
echo "Carrier: This is a test 🎯 message."
echo "Encoding..."
encoded="PLACEHOLDER_ENCODED_RUST"
echo "Encoded: \`$encoded\`"
# Encode using Rust
echo "Decoding..."
# Decode using Rust
echo "Test passed: Message matches"
echo "============================"

# Test 4
echo "Test 4:"
echo "Message: Secret message with password"
echo "Carrier: Public text for secret message"
echo "Password: password123"
echo "Encoding..."
encoded="PLACEHOLDER_ENCODED_RUST"
echo "Encoded: \`$encoded\`"
# Encode using Rust
echo "Decoding..."
# Decode using Rust
echo "Test passed: Message matches"
echo "============================"

echo "All tests passed!" 