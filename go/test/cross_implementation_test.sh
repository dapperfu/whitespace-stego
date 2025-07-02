#!/bin/bash

# Cross-implementation compatibility test for Go whitespace steganography
set -e

echo "Running cross-implementation compatibility tests..."

# Test data
MESSAGE="Hello, World! 🌍"
CARRIER="This is a test message."
PASSWORD="secret123"

# Create test files
echo "$MESSAGE" > test_message.txt
echo "$CARRIER" > test_carrier.txt
echo "$PASSWORD" > test_password.txt

# Test 1: Go encode -> Python decode
echo "Test 1: Go encode -> Python decode"
GO_ENCODED=$(../bin/whitespace-stego-go encode -m "$MESSAGE" -c "$CARRIER")
PYTHON_DECODED=$(python3 -c "
import sys
sys.path.append('../../whitespace_stego')
from whitespace_stego.core import decode
print(decode('$GO_ENCODED'))
")

if [ "$PYTHON_DECODED" = "$MESSAGE" ]; then
    echo "✓ Go -> Python compatibility passed"
else
    echo "✗ Go -> Python compatibility failed"
    echo "Expected: $MESSAGE"
    echo "Got: $PYTHON_DECODED"
    exit 1
fi

# Test 2: Python encode -> Go decode
echo "Test 2: Python encode -> Go decode"
PYTHON_ENCODED=$(python3 -c "
import sys
sys.path.append('../../whitespace_stego')
from whitespace_stego.core import encode
print(encode('$MESSAGE', '$CARRIER'))
")
GO_DECODED=$(../bin/whitespace-stego-go decode -c "$PYTHON_ENCODED")

if [ "$GO_DECODED" = "$MESSAGE" ]; then
    echo "✓ Python -> Go compatibility passed"
else
    echo "✗ Python -> Go compatibility failed"
    echo "Expected: $MESSAGE"
    echo "Got: $GO_DECODED"
    exit 1
fi

# Test 3: Go encode -> Rust decode (if available)
if [ -f "../../whitespace-stego-rs" ]; then
    echo "Test 3: Go encode -> Rust decode"
    echo "$GO_ENCODED" > test_go_encoded.txt
    RUST_DECODED=$(../../whitespace-stego-rs -d -c "$(cat test_go_encoded.txt)")
    
    if [ "$RUST_DECODED" = "$MESSAGE" ]; then
        echo "✓ Go -> Rust compatibility passed"
    else
        echo "✗ Go -> Rust compatibility failed"
        echo "Expected: $MESSAGE"
        echo "Got: $RUST_DECODED"
        exit 1
    fi
else
    echo "⚠ Rust binary not found, skipping Rust compatibility test"
fi

# Test 4: Rust encode -> Go decode (if available)
if [ -f "../../whitespace-stego-rs" ]; then
    echo "Test 4: Rust encode -> Go decode"
    RUST_ENCODED=$(../../whitespace-stego-rs -e -m "$MESSAGE" -c "$CARRIER")
    echo "$RUST_ENCODED" > test_rust_encoded.txt
    GO_DECODED_RUST=$(../bin/whitespace-stego-go decode -cf test_rust_encoded.txt)
    
    if [ "$GO_DECODED_RUST" = "$MESSAGE" ]; then
        echo "✓ Rust -> Go compatibility passed"
    else
        echo "✗ Rust -> Go compatibility failed"
        echo "Expected: $MESSAGE"
        echo "Got: $GO_DECODED_RUST"
        exit 1
    fi
fi

# Test 5: Go encode -> C decode (if available)
if [ -f "../../whitespace-stego-c" ]; then
    echo "Test 5: Go encode -> C decode"
    echo "$GO_ENCODED" > test_go_encoded.txt
    C_DECODED=$(../../whitespace-stego-c decode -cf test_go_encoded.txt)
    
    if [ "$C_DECODED" = "$MESSAGE" ]; then
        echo "✓ Go -> C compatibility passed"
    else
        echo "✗ Go -> C compatibility failed"
        echo "Expected: $MESSAGE"
        echo "Got: $C_DECODED"
        exit 1
    fi
else
    echo "⚠ C binary not found, skipping C compatibility test"
fi

# Test 6: C encode -> Go decode (if available)
if [ -f "../../whitespace-stego-c" ]; then
    echo "Test 6: C encode -> Go decode"
    echo "$MESSAGE" > test_message.txt
    echo "$CARRIER" > test_carrier.txt
    C_ENCODED=$(../../whitespace-stego-c encode -mf test_message.txt -cf test_carrier.txt)
    echo "$C_ENCODED" > test_c_encoded.txt
    GO_DECODED_C=$(../bin/whitespace-stego-go decode -cf test_c_encoded.txt)
    
    if [ "$GO_DECODED_C" = "$MESSAGE" ]; then
        echo "✓ C -> Go compatibility passed"
    else
        echo "✗ C -> Go compatibility failed"
        echo "Expected: $MESSAGE"
        echo "Got: $GO_DECODED_C"
        exit 1
    fi
fi

# Test 7: Password-protected cross-compatibility
echo "Test 7: Password-protected cross-compatibility"
GO_ENCODED_PW=$(../bin/whitespace-stego-go encode -m "$MESSAGE" -c "$CARRIER" -p "$PASSWORD")
PYTHON_DECODED_PW=$(python3 -c "
import sys
sys.path.append('../../whitespace_stego')
from whitespace_stego.core import decode
print(decode('$GO_ENCODED_PW', '$PASSWORD'))
")

if [ "$PYTHON_DECODED_PW" = "$MESSAGE" ]; then
    echo "✓ Password-protected Go -> Python compatibility passed"
else
    echo "✗ Password-protected Go -> Python compatibility failed"
    echo "Expected: $MESSAGE"
    echo "Got: $PYTHON_DECODED_PW"
    exit 1
fi

# Test 8: Multiple messages
echo "Test 8: Multiple messages cross-compatibility"
MESSAGE1="First secret message"
MESSAGE2="Second secret message"
MESSAGE3="Third secret message"

# Encode multiple messages with Go
GO_MULTI=$(../bin/whitespace-stego-go encode -m "$MESSAGE1" -c "$CARRIER")
GO_MULTI=$(../bin/whitespace-stego-go encode -m "$MESSAGE2" -c "$GO_MULTI")
GO_MULTI=$(../bin/whitespace-stego-go encode -m "$MESSAGE3" -c "$GO_MULTI")

# Decode with Python
PYTHON_MULTI=$(python3 -c "
import sys
sys.path.append('../../whitespace_stego')
from whitespace_stego.core import decode
messages = decode('$GO_MULTI')
for msg in messages:
    print(msg)
")

# Check if all messages are present
if echo "$PYTHON_MULTI" | grep -q "$MESSAGE1" && \
   echo "$PYTHON_MULTI" | grep -q "$MESSAGE2" && \
   echo "$PYTHON_MULTI" | grep -q "$MESSAGE3"; then
    echo "✓ Multiple messages cross-compatibility passed"
else
    echo "✗ Multiple messages cross-compatibility failed"
    echo "Expected: $MESSAGE1, $MESSAGE2, $MESSAGE3"
    echo "Got: $PYTHON_MULTI"
    exit 1
fi

# Cleanup
rm -f test_message.txt test_carrier.txt test_password.txt test_go_encoded.txt test_c_encoded.txt test_rust_encoded.txt

echo "All cross-implementation compatibility tests passed!" 