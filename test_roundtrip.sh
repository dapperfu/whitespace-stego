#!/bin/bash

# Test message and carrier text
MESSAGE="Hello, this is a secret message!"
CARRIER="This is some innocent looking text that will carry our secret message."
PASSWORD="test_password123"

# Create temporary files
TEMP_DIR=$(mktemp -d)
PYTHON_ENCODED="$TEMP_DIR/python_encoded.txt"
RUST_ENCODED="$TEMP_DIR/rust_encoded.txt"
PYTHON_DECODED="$TEMP_DIR/python_decoded.txt"
RUST_DECODED="$TEMP_DIR/rust_decoded.txt"

# Function to clean up temporary files
cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

echo "Testing round-trip encoding/decoding between Python and Rust implementations..."
echo "Message: $MESSAGE"
echo "Carrier: $CARRIER"
echo "Password: $PASSWORD"
echo

# Test 1: Python encode -> Python decode
echo "Test 1: Python encode -> Python decode"
python3 -c "
from whitespace_stego import encode, decode
encoded = encode('$MESSAGE', '$CARRIER', '$PASSWORD')
with open('$PYTHON_ENCODED', 'w') as f:
    f.write(encoded)
decoded, _ = decode(encoded, '$PASSWORD')
with open('$PYTHON_DECODED', 'w') as f:
    f.write(decoded)
"
if [ $? -eq 0 ]; then
    echo "✓ Python encode -> Python decode successful"
    echo "Decoded message: $(cat $PYTHON_DECODED)"
else
    echo "✗ Python encode -> Python decode failed"
    exit 1
fi
echo

# Test 2: Python encode -> Rust decode
echo "Test 2: Python encode -> Rust decode"
python3 -c "
from whitespace_stego import encode
encoded = encode('$MESSAGE', '$CARRIER', '$PASSWORD')
with open('$PYTHON_ENCODED', 'w') as f:
    f.write(encoded)
"
if [ $? -eq 0 ]; then
    cargo run -- decode -i "$PYTHON_ENCODED" -p "$PASSWORD" > "$RUST_DECODED"
    if [ $? -eq 0 ]; then
        echo "✓ Python encode -> Rust decode successful"
        echo "Decoded message: $(cat $RUST_DECODED)"
    else
        echo "✗ Python encode -> Rust decode failed"
        exit 1
    fi
else
    echo "✗ Python encode failed"
    exit 1
fi
echo

# Test 3: Rust encode -> Python decode
echo "Test 3: Rust encode -> Python decode"
cargo run -- encode -m "$MESSAGE" -c "$CARRIER" -p "$PASSWORD" -o "$RUST_ENCODED"
if [ $? -eq 0 ]; then
    python3 -c "
from whitespace_stego import decode
with open('$RUST_ENCODED', 'r') as f:
    encoded = f.read()
decoded, _ = decode(encoded, '$PASSWORD')
with open('$PYTHON_DECODED', 'w') as f:
    f.write(decoded)
"
    if [ $? -eq 0 ]; then
        echo "✓ Rust encode -> Python decode successful"
        echo "Decoded message: $(cat $PYTHON_DECODED)"
    else
        echo "✗ Rust encode -> Python decode failed"
        exit 1
    fi
else
    echo "✗ Rust encode failed"
    exit 1
fi
echo

# Test 4: Rust encode -> Rust decode
echo "Test 4: Rust encode -> Rust decode"
cargo run -- encode -m "$MESSAGE" -c "$CARRIER" -p "$PASSWORD" -o "$RUST_ENCODED"
if [ $? -eq 0 ]; then
    cargo run -- decode -i "$RUST_ENCODED" -p "$PASSWORD" > "$RUST_DECODED"
    if [ $? -eq 0 ]; then
        echo "✓ Rust encode -> Rust decode successful"
        echo "Decoded message: $(cat $RUST_DECODED)"
    else
        echo "✗ Rust encode -> Rust decode failed"
        exit 1
    fi
else
    echo "✗ Rust encode failed"
    exit 1
fi
echo

# Verify all decoded messages match the original
echo "Verifying all decoded messages match the original..."
DECODED_MESSAGES=("$(cat $PYTHON_DECODED)" "$(cat $RUST_DECODED)")
for msg in "${DECODED_MESSAGES[@]}"; do
    if [ "$msg" != "$MESSAGE" ]; then
        echo "✗ Decoded message mismatch:"
        echo "Expected: $MESSAGE"
        echo "Got: $msg"
        exit 1
    fi
done
echo "✓ All decoded messages match the original"
echo

echo "All tests passed successfully!" 