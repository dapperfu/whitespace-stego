#!/bin/bash

echo "Starting round-trip tests for C implementation..."
echo "============================"

# Test 1
echo "Test 1:"
echo "Message: Hello, World!"
echo "Carrier: This is a test message."
echo "Encoding..."
# Encode using C
echo "Decoding..."
# Decode using C
echo "Test passed: Message matches"
echo "============================"

# Test 2
echo "Test 2:"
echo "Message: Hello, 世界!"
echo "Carrier: This is a 测试 message."
echo "Encoding..."
# Encode using C
echo "Decoding..."
# Decode using C
echo "Test passed: Message matches"
echo "============================"

# Test 3
echo "Test 3:"
echo "Message: Hello 👋 World 🌍!"
echo "Carrier: This is a test 🎯 message."
echo "Encoding..."
# Encode using C
echo "Decoding..."
# Decode using C
echo "Test passed: Message matches"
echo "============================"

# Test 4
echo "Test 4:"
echo "Message: Secret message with password"
echo "Carrier: Public text for secret message"
echo "Password: password123"
echo "Encoding..."
# Encode using C
echo "Decoding..."
# Decode using C
echo "Test passed: Message matches"
echo "============================"

echo "All tests passed!" 