#!/bin/bash

# Comprehensive test script for standalone binaries
# This script runs both basic functionality tests and cross-round-trip compatibility tests

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
TEST_RESULTS_DIR="$PROJECT_ROOT/test_results"

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

# Function to run a test script and capture results
run_test_script() {
    local script_name=$1
    local script_path="$SCRIPT_DIR/$script_name"
    local description=$2
    
    print_status "INFO" "🚀 Running $description..."
    print_status "INFO" "📄 Script: $script_path"
    
    if [[ ! -f "$script_path" ]]; then
        print_status "ERROR" "Test script not found: $script_path"
        return 1
    fi
    
    if [[ ! -x "$script_path" ]]; then
        print_status "ERROR" "Test script not executable: $script_path"
        return 1
    fi
    
    # Change to project root directory
    cd "$PROJECT_ROOT"
    
    # Run the test script
    if "$script_path"; then
        print_status "SUCCESS" "$description completed successfully"
        return 0
    else
        print_status "ERROR" "$description failed"
        return 1
    fi
}

# Function to display test results
display_results() {
    print_status "INFO" "📊 Test Results Summary:"
    
    if [[ -f "$TEST_RESULTS_DIR/standalone_binary_tests.json" ]]; then
        print_status "INFO" "📋 Standalone Binary Tests:"
        cat "$TEST_RESULTS_DIR/standalone_binary_tests.json" | jq -r '. | "  Total: \(.total_tests), Passed: \(.passed_tests), Failed: \(.failed_tests), Success Rate: \(.success_rate)%"'
    fi
    
    if [[ -f "$TEST_RESULTS_DIR/cross_roundtrip_tests.json" ]]; then
        print_status "INFO" "📋 Cross-Round-Trip Tests:"
        cat "$TEST_RESULTS_DIR/cross_roundtrip_tests.json" | jq -r '. | "  Total: \(.total_tests), Passed: \(.passed_tests), Failed: \(.failed_tests), Success Rate: \(.success_rate)%"'
    fi
}

# Main function
main() {
    print_status "INFO" "🧪 Starting comprehensive standalone binary tests..."
    print_status "INFO" "📁 Project root: $PROJECT_ROOT"
    print_status "INFO" "📁 Script directory: $SCRIPT_DIR"
    
    # Create test results directory
    mkdir -p "$TEST_RESULTS_DIR"
    
    # Track overall results
    local overall_success=true
    
    echo
    
    # Run standalone binary tests
    if ! run_test_script "test_standalone_binaries.sh" "Standalone Binary Functionality Tests"; then
        overall_success=false
    fi
    
    echo
    
    # Run cross-round-trip tests
    if ! run_test_script "test_cross_roundtrip.sh" "Cross-Round-Trip Compatibility Tests"; then
        overall_success=false
    fi
    
    echo
    
    # Display results
    display_results
    
    echo
    
    # Final status
    if [[ "$overall_success" == "true" ]]; then
        print_status "SUCCESS" "🎉 All comprehensive tests passed!"
        exit 0
    else
        print_status "ERROR" "💥 Some tests failed!"
        exit 1
    fi
}

# Run main function
main "$@" 