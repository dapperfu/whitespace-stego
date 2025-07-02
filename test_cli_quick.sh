#!/bin/bash

# Quick CLI Test - Verify basic functionality
# Tests a few key cases to ensure CLI tools work

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    local status=$1
    local message=$2
    case $status in
        "PASS")
            echo -e "${GREEN}✓ PASS${NC}: $message"
            ;;
        "FAIL")
            echo -e "${RED}✗ FAIL${NC}: $message"
            ;;
        "INFO")
            echo -e "${BLUE}ℹ INFO${NC}: $message"
            ;;
    esac
}

# Test data
TEST_MESSAGE="Hello, World! 🌍"
TEST_CARRIER="This is a test carrier text."
TEST_PASSWORD="test123"

# Create temporary files
TEMP_DIR=$(mktemp -d)
MESSAGE_FILE="$TEMP_DIR/message.txt"
CARRIER_FILE="$TEMP_DIR/carrier.txt"
ENCODED_FILE="$TEMP_DIR/encoded.txt"
DECODED_FILE="$TEMP_DIR/decoded.txt"

# Cleanup function
cleanup() {
    rm -rf "$TEMP_DIR"
}

trap cleanup EXIT

# Create test files
echo -n "$TEST_MESSAGE" > "$MESSAGE_FILE"
echo -n "$TEST_CARRIER" > "$CARRIER_FILE"

echo "=========================================="
echo "  Quick CLI Test"
echo "=========================================="
echo

# Test Python CLI
print_status "INFO" "Testing Python CLI..."
if python -m whitespace_stego.cli --backend python encode --message-file "$MESSAGE_FILE" --carrier-file "$CARRIER_FILE" --password "$TEST_PASSWORD" --output "$ENCODED_FILE"; then
    if python -m whitespace_stego.cli --backend python decode --carrier-file "$ENCODED_FILE" --password "$TEST_PASSWORD" --output "$DECODED_FILE"; then
        DECODED=$(cat "$DECODED_FILE")
        if [[ "$DECODED" == "$TEST_MESSAGE" ]]; then
            print_status "PASS" "Python CLI roundtrip successful"
        else
            print_status "FAIL" "Python CLI decode mismatch: expected '$TEST_MESSAGE', got '$DECODED'"
            exit 1
        fi
    else
        print_status "FAIL" "Python CLI decode failed"
        exit 1
    fi
else
    print_status "FAIL" "Python CLI encode failed"
    exit 1
fi

# Test Rust CLI
print_status "INFO" "Testing Rust CLI..."
if ./whitespace-stego-rs encode --mf "$MESSAGE_FILE" --cf "$CARRIER_FILE" --password "$TEST_PASSWORD" --output "$ENCODED_FILE"; then
    if ./whitespace-stego-rs decode --cf "$ENCODED_FILE" --password "$TEST_PASSWORD" --output "$DECODED_FILE"; then
        DECODED=$(cat "$DECODED_FILE")
        if [[ "$DECODED" == "$TEST_MESSAGE" ]]; then
            print_status "PASS" "Rust CLI roundtrip successful"
        else
            print_status "FAIL" "Rust CLI decode mismatch: expected '$TEST_MESSAGE', got '$DECODED'"
            exit 1
        fi
    else
        print_status "FAIL" "Rust CLI decode failed"
        exit 1
    fi
else
    print_status "FAIL" "Rust CLI encode failed"
    exit 1
fi

# Test C CLI
print_status "INFO" "Testing C CLI..."
if ./whitespace-stego-c encode --message-file "$MESSAGE_FILE" --carrier-file "$CARRIER_FILE" --password "$TEST_PASSWORD" --output "$ENCODED_FILE"; then
    if ./whitespace-stego-c decode --carrier-file "$ENCODED_FILE" --password "$TEST_PASSWORD" --output "$DECODED_FILE"; then
        DECODED=$(cat "$DECODED_FILE")
        if [[ "$DECODED" == "$TEST_MESSAGE" ]]; then
            print_status "PASS" "C CLI roundtrip successful"
        else
            print_status "FAIL" "C CLI decode mismatch: expected '$TEST_MESSAGE', got '$DECODED'"
            exit 1
        fi
    else
        print_status "FAIL" "C CLI decode failed"
        exit 1
    fi
else
    print_status "FAIL" "C CLI encode failed"
    exit 1
fi

echo
print_status "PASS" "All CLI tools working correctly! 🎉"
echo
print_status "INFO" "You can now run the comprehensive tests:"
echo "  ./test_cli_simple.sh     # Quick comprehensive test"
echo "  ./test_cli_comprehensive.sh  # Full permutation test" 