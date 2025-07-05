#!/bin/bash

# Simple Benchmark Script for Whitespace Steganography Implementations
# Tests all available implementations with basic timing

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
RESULTS_DIR="${PROJECT_ROOT}/benchmark_results"
LOG_FILE="${RESULTS_DIR}/benchmark.log"

# Test data
TEST_MESSAGE="Hello, World! This is a test message for benchmarking."
TEST_PASSWORD="test_password_123"
TEST_CARRIER="This is a sample carrier text that will be used for testing the whitespace steganography implementations. It contains enough text to embed various sized messages."

# Test files
CARRIER_FILE="${PROJECT_ROOT}/test_carrier.txt"
MESSAGE_FILE="${PROJECT_ROOT}/test_message.txt"
ENCODED_FILE="${PROJECT_ROOT}/test_encoded.txt"
DECODED_FILE="${PROJECT_ROOT}/test_decoded.txt"

# Implementation binaries
declare -A BINARIES=(
    ["c-static"]="${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-static"
    ["c-dynamic"]="${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-c"
    ["cpp"]="${PROJECT_ROOT}/implementations/cpp/bin/whitespace-stego-cpp"
    ["go"]="${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go"
    ["rust"]="${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs"
    ["python"]="python3 -m whitespace_stego.cli"
)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}✗${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1" | tee -a "$LOG_FILE"
}

# Create test files
create_test_files() {
    echo "$TEST_CARRIER" > "$CARRIER_FILE"
    echo "$TEST_MESSAGE" > "$MESSAGE_FILE"
    log "Created test carrier file: $CARRIER_FILE"
    log "Created test message file: $MESSAGE_FILE"
}

# Clean up test files
cleanup_test_files() {
    rm -f "$CARRIER_FILE" "$MESSAGE_FILE" "$ENCODED_FILE" "$DECODED_FILE"
    log "Cleaned up test files"
}

# Check if binary exists and is executable
check_binary() {
    local name=$1
    local path=$2
    
    # Special handling for Python
    if [ "$name" = "python" ]; then
        if cd "${PROJECT_ROOT}/implementations/python" && python3 -c "import whitespace_stego.cli" >/dev/null 2>&1; then
            return 0
        else
            return 1
        fi
    fi
    
    if [ -f "$path" ] && [ -x "$path" ]; then
        return 0
    elif command -v "$path" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Time a command and return the result
time_command() {
    local cmd="$1"
    local start_time=$(date +%s.%N)
    
    if eval "$cmd" >/dev/null 2>&1; then
        local end_time=$(date +%s.%N)
        local duration=$(echo "$end_time - $start_time" | bc -l)
        echo "$duration"
    else
        echo "ERROR"
    fi
}

# Test a single implementation
test_implementation() {
    local name=$1
    local binary=$2
    
    log "Testing implementation: $name"
    
    # Check if binary exists
    if ! check_binary "$name" "$binary"; then
        log_warning "$name: Binary not found or not executable"
        return 1
    fi
    
    # Test encode
    local encode_cmd=""
    case $name in
        c-static)
            encode_cmd="$binary encode -m '$TEST_MESSAGE' -cf '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        c-dynamic)
            encode_cmd="$binary encode -m '$MESSAGE_FILE' -c '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        cpp)
            encode_cmd="$binary encode -m '$TEST_MESSAGE' -cf '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        rust)
            encode_cmd="$binary encode -m '$TEST_MESSAGE' --cf '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        go)
            encode_cmd="$binary encode -m '$TEST_MESSAGE' -cf '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        python)
            encode_cmd="cd ${PROJECT_ROOT}/implementations/python && $binary encode -m '$TEST_MESSAGE' -cf '$CARRIER_FILE' -o '$ENCODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        *)
            log_error "$name: Unknown implementation"
            return 1
            ;;
    esac
    
    local encode_time=$(time_command "$encode_cmd")
    if [ "$encode_time" = "ERROR" ]; then
        log_error "$name: Encode failed"
        return 1
    fi
    
    # Test decode
    local decode_cmd=""
    case $name in
        c-static)
            decode_cmd="$binary decode -cf '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        c-dynamic)
            decode_cmd="$binary decode -c '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        cpp)
            decode_cmd="$binary decode -cf '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        rust)
            decode_cmd="$binary decode --cf '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        go)
            decode_cmd="$binary decode -cf '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
        python)
            decode_cmd="cd ${PROJECT_ROOT}/implementations/python && $binary decode -cf '$ENCODED_FILE' -o '$DECODED_FILE' -p '$TEST_PASSWORD'"
            ;;
    esac
    
    local decode_time=$(time_command "$decode_cmd")
    if [ "$decode_time" = "ERROR" ]; then
        log_error "$name: Decode failed"
        return 1
    fi
    
    # Check if decode was successful
    if [ -f "$DECODED_FILE" ]; then
        local decoded_content=$(cat "$DECODED_FILE")
        if [ "$decoded_content" = "$TEST_MESSAGE" ]; then
            log_success "$name: Round-trip successful"
        else
            log_error "$name: Round-trip failed - message mismatch"
            return 1
        fi
    else
        log_error "$name: Decode failed - no output file"
        return 1
    fi
    
    # Calculate total time and convert to milliseconds
    local total_time=$(echo "$encode_time + $decode_time" | bc -l)
    local total_ms=$(echo "scale=2; $total_time * 1000" | bc -l)
    local encode_ms=$(echo "scale=2; $encode_time * 1000" | bc -l)
    local decode_ms=$(echo "scale=2; $decode_time * 1000" | bc -l)
    
    # Print results
    printf "%-12s | %8s | %8s | %8s\n" "$name" "$encode_ms" "$decode_ms" "$total_ms"
    
    return 0
}

# Main function
main() {
    # Create results directory
    mkdir -p "$RESULTS_DIR"
    
    # Clear previous log
    > "$LOG_FILE"
    
    log "Starting benchmark of whitespace steganography implementations"
    log "Test message: '$TEST_MESSAGE'"
    log "Test password: '$TEST_PASSWORD'"
    
    # Create test files
    create_test_files
    
    # Print header
    echo
    echo "Benchmark Results"
    echo "================="
    echo
    printf "%-12s | %8s | %8s | %8s\n" "Implementation" "Encode" "Decode" "Total"
    printf "%-12s | %8s | %8s | %8s\n" "------------" "------" "------" "-----"
    
    # Test each implementation
    local successful_tests=0
    local total_tests=0
    
    for name in "${!BINARIES[@]}"; do
        total_tests=$((total_tests + 1))
        if test_implementation "$name" "${BINARIES[$name]}"; then
            successful_tests=$((successful_tests + 1))
        fi
    done
    
    # Clean up test files
    cleanup_test_files
    
    # Print summary
    echo
    echo "Summary"
    echo "======="
    echo "Successful tests: $successful_tests/$total_tests"
    echo "Results saved to: $LOG_FILE"
    
    if [ $successful_tests -eq $total_tests ]; then
        log_success "All implementations passed!"
        exit 0
    else
        log_error "Some implementations failed"
        exit 1
    fi
}

# Run main function
main "$@" 