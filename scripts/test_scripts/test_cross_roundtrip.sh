#!/bin/bash

# Cross-round-trip compatibility test script
# This script tests that binaries can encode/decode each other's output

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
BIN_DIR="bin"
TEST_RESULTS_DIR="test_results"
TEMP_DIR="test_temp"
mkdir -p "$TEST_RESULTS_DIR" "$TEMP_DIR"

# Test results tracking
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Test messages
TEST_MESSAGES=(
    "Hello, World!"
    "Secret message with emojis 🕵️‍♂️🔐"
    "Unicode: 你好世界 🌍"
    "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?"
    "Long message: $(printf 'A%.0s' {1..100})"
)

# Function to print colored output
print_status() {
    local status=$1
    local message=$2
    case $status in
        "INFO")
            echo -e "${BLUE}ℹ️  $message${NC}"
            ;;
        "SUCCESS")
            echo -e "${GREEN}✅ $message${NC}"
            ;;
        "WARNING")
            echo -e "${YELLOW}⚠️  $message${NC}"
            ;;
        "ERROR")
            echo -e "${RED}❌ $message${NC}"
            ;;
    esac
}

# Function to run encode command
encode_message() {
    local binary_path=$1
    local message=$2
    local carrier=$3
    local password=${4:-}
    local output_file=$5
    
    local cmd_args=()
    
    case $(basename "$binary_path") in
        "whitespace-stego-py")
            cmd_args=("encode" "-m" "$message" "-c" "$carrier")
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            cmd_args+=("-o" "$output_file")
            ;;
        "whitespace-stego-rs")
            cmd_args=("encode" "-m" "$message" "-c" "$carrier")
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            cmd_args+=("-o" "$output_file")
            ;;
        "whitespace-stego-c")
            # C binary expects files
            echo "$message" > "$TEMP_DIR/message.txt"
            echo "$carrier" > "$TEMP_DIR/carrier.txt"
            cmd_args=("encode" "--message-file" "$TEMP_DIR/message.txt" "--carrier-file" "$TEMP_DIR/carrier.txt" "--output" "$output_file")
            if [[ -n "$password" ]]; then
                cmd_args+=("--password" "$password")
            fi
            ;;
        "whitespace-stego-go")
            cmd_args=("encode" "-m" "$message" "-cf" "$TEMP_DIR/carrier.txt" "-o" "$output_file")
            echo "$carrier" > "$TEMP_DIR/carrier.txt"
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            ;;
        *)
            print_status "ERROR" "Unknown binary: $(basename "$binary_path")"
            return 1
            ;;
    esac
    
    if timeout 30s "$binary_path" "${cmd_args[@]}" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function to run decode command
decode_message() {
    local binary_path=$1
    local encoded_file=$2
    local password=${3:-}
    local output_file=$4
    
    local cmd_args=()
    
    case $(basename "$binary_path") in
        "whitespace-stego-py")
            cmd_args=("decode" "--carrier-file" "$encoded_file" "-o" "$output_file")
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            ;;
        "whitespace-stego-rs")
            cmd_args=("decode" "--cf" "$encoded_file" "-o" "$output_file")
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            ;;
        "whitespace-stego-c")
            cmd_args=("decode" "--carrier-file" "$encoded_file" "--output" "$output_file")
            if [[ -n "$password" ]]; then
                cmd_args+=("--password" "$password")
            fi
            ;;
        "whitespace-stego-go")
            cmd_args=("decode" "-cf" "$encoded_file" "-o" "$output_file")
            if [[ -n "$password" ]]; then
                cmd_args+=("-p" "$password")
            fi
            ;;
        *)
            print_status "ERROR" "Unknown binary: $(basename "$binary_path")"
            return 1
            ;;
    esac
    
    if timeout 30s "$binary_path" "${cmd_args[@]}" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function to test cross-round-trip between two binaries
test_cross_roundtrip() {
    local encoder=$1
    local decoder=$2
    local message=$3
    local carrier="This is innocent carrier text."
    local password="test_password_123"
    
    local test_name="$(basename "$encoder") -> $(basename "$decoder")"
    local encoded_file="$TEMP_DIR/encoded_${RANDOM}.txt"
    local decoded_file="$TEMP_DIR/decoded_${RANDOM}.txt"
    
    print_status "INFO" "Testing: $test_name"
    print_status "INFO" "  Message: ${message:0:50}$([[ ${#message} -gt 50 ]] && echo "...")"
    
    ((TOTAL_TESTS++))
    
    # Encode with first binary
    if ! encode_message "$encoder" "$message" "$carrier" "$password" "$encoded_file"; then
        print_status "ERROR" "  Encode failed with $(basename "$encoder")"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Decode with second binary
    if ! decode_message "$decoder" "$encoded_file" "$password" "$decoded_file"; then
        print_status "ERROR" "  Decode failed with $(basename "$decoder")"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Compare decoded message with original
    if [[ -f "$decoded_file" ]] && [[ "$(cat "$decoded_file")" == "$message" ]]; then
        print_status "SUCCESS" "  Cross-round-trip successful"
        ((PASSED_TESTS++))
    else
        print_status "ERROR" "  Decoded message doesn't match original"
        print_status "ERROR" "    Expected: $message"
        print_status "ERROR" "    Got: $(cat "$decoded_file" 2>/dev/null || echo '<no output>')"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Cleanup
    rm -f "$encoded_file" "$decoded_file"
}

# Function to test self-round-trip for a single binary
test_self_roundtrip() {
    local binary=$1
    local message=$2
    local carrier="This is innocent carrier text."
    local password="test_password_123"
    
    local test_name="$(basename "$binary") self-round-trip"
    local encoded_file="$TEMP_DIR/encoded_${RANDOM}.txt"
    local decoded_file="$TEMP_DIR/decoded_${RANDOM}.txt"
    
    print_status "INFO" "Testing: $test_name"
    print_status "INFO" "  Message: ${message:0:50}$([[ ${#message} -gt 50 ]] && echo "...")"
    
    ((TOTAL_TESTS++))
    
    # Encode
    if ! encode_message "$binary" "$message" "$carrier" "$password" "$encoded_file"; then
        print_status "ERROR" "  Encode failed"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Decode
    if ! decode_message "$binary" "$encoded_file" "$password" "$decoded_file"; then
        print_status "ERROR" "  Decode failed"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Compare
    if [[ -f "$decoded_file" ]] && [[ "$(cat "$decoded_file")" == "$message" ]]; then
        print_status "SUCCESS" "  Self-round-trip successful"
        ((PASSED_TESTS++))
    else
        print_status "ERROR" "  Decoded message doesn't match original"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Cleanup
    rm -f "$encoded_file" "$decoded_file"
}

# Main test function
main() {
    print_status "INFO" "🔄 Starting cross-round-trip compatibility tests..."
    print_status "INFO" "📁 Binary directory: $(realpath "$BIN_DIR")"
    
    if [[ ! -d "$BIN_DIR" ]]; then
        print_status "ERROR" "Binary directory not found: $BIN_DIR"
        exit 1
    fi
    
    # Get available binaries
    local binaries=()
    for binary in "$BIN_DIR"/whitespace-stego-*; do
        if [[ -f "$binary" ]] && [[ -x "$binary" ]]; then
            binaries+=("$binary")
        fi
    done
    
    if [[ ${#binaries[@]} -eq 0 ]]; then
        print_status "ERROR" "No executable binaries found in $BIN_DIR"
        exit 1
    fi
    
    print_status "INFO" "📦 Found ${#binaries[@]} binaries:"
    for binary in "${binaries[@]}"; do
        print_status "INFO" "  - $(basename "$binary")"
    done
    
    echo
    
    # Test self-round-trips first
    print_status "INFO" "🧪 Testing self-round-trips..."
    for binary in "${binaries[@]}"; do
        for message in "${TEST_MESSAGES[@]}"; do
            test_self_roundtrip "$binary" "$message"
        done
    done
    
    echo
    
    # Test cross-round-trips
    print_status "INFO" "🔄 Testing cross-round-trips..."
    for i in "${!binaries[@]}"; do
        for j in "${!binaries[@]}"; do
            if [[ $i -ne $j ]]; then
                for message in "${TEST_MESSAGES[@]}"; do
                    test_cross_roundtrip "${binaries[$i]}" "${binaries[$j]}" "$message"
                done
            fi
        done
    done
    
    echo
    print_status "INFO" "📊 Test Summary:"
    print_status "INFO" "  Total tests: $TOTAL_TESTS"
    print_status "INFO" "  Passed tests: $PASSED_TESTS"
    print_status "INFO" "  Failed tests: $FAILED_TESTS"
    
    if [[ $TOTAL_TESTS -gt 0 ]]; then
        local success_rate=$(echo "scale=1; $PASSED_TESTS * 100 / $TOTAL_TESTS" | bc -l)
        print_status "INFO" "  Success rate: ${success_rate}%"
    fi
    
    # Save results
    cat > "$TEST_RESULTS_DIR/cross_roundtrip_tests.json" << EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "total_tests": $TOTAL_TESTS,
  "passed_tests": $PASSED_TESTS,
  "failed_tests": $FAILED_TESTS,
  "success_rate": ${success_rate:-0},
  "binaries_tested": ${#binaries[@]}
}
EOF
    
    print_status "INFO" "💾 Results saved to: $TEST_RESULTS_DIR/cross_roundtrip_tests.json"
    
    # Cleanup
    rm -rf "$TEMP_DIR"
    
    # Exit with error if any tests failed
    if [[ $FAILED_TESTS -gt 0 ]]; then
        print_status "ERROR" "Some tests failed!"
        exit 1
    else
        print_status "SUCCESS" "All tests passed!"
    fi
}

# Run main function
main "$@" 