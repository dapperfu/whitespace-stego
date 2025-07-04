#!/bin/bash

# Test script for standalone binaries
# This script tests that all standalone binaries are available and functional

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
mkdir -p "$TEST_RESULTS_DIR"

# Test results tracking
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

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

# Function to run a command and capture results
run_command() {
    local binary_path=$1
    shift
    local args=("$@")
    
    if timeout 30s "$binary_path" "${args[@]}" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function to test a single binary
test_binary() {
    local binary_name=$1
    local binary_path="$BIN_DIR/$binary_name"
    local description=$2
    local help_cmd=$3
    local encode_cmd=$4
    local decode_cmd=$5
    
    print_status "INFO" "Testing $binary_name ($description)"
    
    # Check if binary exists
    if [[ ! -f "$binary_path" ]]; then
        print_status "ERROR" "$binary_name not found: $binary_path"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Check if binary is executable
    if [[ ! -x "$binary_path" ]]; then
        print_status "ERROR" "$binary_name not executable: $binary_path"
        ((FAILED_TESTS++))
        return 1
    fi
    
    # Test help command
    ((TOTAL_TESTS++))
    if run_command "$binary_path" $help_cmd; then
        print_status "SUCCESS" "  Help command works"
        ((PASSED_TESTS++))
    else
        print_status "ERROR" "  Help command failed"
        ((FAILED_TESTS++))
    fi
    
    # Test encode help
    ((TOTAL_TESTS++))
    if run_command "$binary_path" $encode_cmd; then
        print_status "SUCCESS" "  Encode help works"
        ((PASSED_TESTS++))
    else
        print_status "ERROR" "  Encode help failed"
        ((FAILED_TESTS++))
    fi
    
    # Test decode help
    ((TOTAL_TESTS++))
    if run_command "$binary_path" $decode_cmd; then
        print_status "SUCCESS" "  Decode help works"
        ((PASSED_TESTS++))
    else
        print_status "ERROR" "  Decode help failed"
        ((FAILED_TESTS++))
    fi
}

# Main test function
main() {
    print_status "INFO" "🚀 Starting standalone binary tests..."
    print_status "INFO" "📁 Binary directory: $(realpath "$BIN_DIR")"
    
    if [[ ! -d "$BIN_DIR" ]]; then
        print_status "ERROR" "Binary directory not found: $BIN_DIR"
        exit 1
    fi
    
    # List available binaries
    print_status "INFO" "📦 Found $(ls "$BIN_DIR" | wc -l) files in bin directory:"
    for binary in "$BIN_DIR"/*; do
        if [[ -f "$binary" ]]; then
            print_status "INFO" "  - $(basename "$binary")"
        fi
    done
    
    echo
    
    # Test each binary
    test_binary "whitespace-stego-py" "Python standalone CLI (PyInstaller)" "--help" "encode" "--help" "decode" "--help"
    test_binary "whitespace-stego-rs" "Rust standalone CLI" "--help" "encode" "--help" "decode" "--help"
    test_binary "whitespace-stego-c" "C standalone CLI" "--help" "encode" "--help" "decode" "--help"
    test_binary "whitespace-stego-go" "Go standalone CLI" "help" "encode" "--help" "decode" "--help"
    
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
    cat > "$TEST_RESULTS_DIR/standalone_binary_tests.json" << EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "total_tests": $TOTAL_TESTS,
  "passed_tests": $PASSED_TESTS,
  "failed_tests": $FAILED_TESTS,
  "success_rate": ${success_rate:-0}
}
EOF
    
    print_status "INFO" "💾 Results saved to: $TEST_RESULTS_DIR/standalone_binary_tests.json"
    
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