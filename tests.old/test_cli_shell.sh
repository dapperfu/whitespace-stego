#!/bin/bash

# Comprehensive CLI test script for whitespace steganography
# Tests all functionality including mutually exclusive options, stdout output, and error handling

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Function to print test results
print_result() {
    local test_name="$1"
    local exit_code="$2"
    local expected_exit="$3"
    
    if [ "$exit_code" -eq "$expected_exit" ]; then
        echo -e "${GREEN}✅ PASS${NC}: $test_name"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ FAIL${NC}: $test_name (expected exit $expected_exit, got $exit_code)"
        ((TESTS_FAILED++))
    fi
}

# Function to create test files
setup_test_files() {
    echo "Setting up test files..."
    
    # Create test message file
    echo "Test message content" > test_message.txt
    
    # Create test carrier file
    echo "This is a test carrier text." > test_carrier.txt
    
    # Create Unicode test files
    echo "Hello 世界 🌍" > unicode_message.txt
    echo "Unicode carrier: café naïve" > unicode_carrier.txt
    
    echo "Test files created."
}

# Function to cleanup test files
cleanup_test_files() {
    echo "Cleaning up test files..."
    rm -f test_*.txt unicode_*.txt encoded_*.txt decoded_*.txt
    echo "Cleanup complete."
}

# Function to run a test
run_test() {
    local test_name="$1"
    local command="$2"
    local expected_exit="$3"
    
    echo -e "${BLUE}Running:${NC} $test_name"
    echo "Command: $command"
    
    # Run the command and capture exit code
    eval "$command"
    exit_code=$?
    
    print_result "$test_name" "$exit_code" "$expected_exit"
    echo ""
}

# Main test execution
main() {
    echo -e "${YELLOW}=== Whitespace Steganography CLI Comprehensive Tests ===${NC}"
    echo ""
    
    # Setup
    setup_test_files
    
    echo -e "${YELLOW}=== Help and Documentation Tests ===${NC}"
    
    # Test 1: Main CLI help
    run_test "Main CLI help" "python3 -m whitespace_stego.cli --help" 0
    
    # Test 2: Encode help
    run_test "Encode command help" "python3 -m whitespace_stego.cli encode --help" 0
    
    # Test 3: Decode help
    run_test "Decode command help" "python3 -m whitespace_stego.cli decode --help" 0
    
    echo -e "${YELLOW}=== Backend Validation Tests ===${NC}"
    
    # Test 4: Invalid backend
    run_test "Invalid backend validation" "python3 -m whitespace_stego.cli --backend invalid encode --help" 2
    
    # Test 5: Valid backends
    run_test "Python backend validation" "python3 -m whitespace_stego.cli --backend python encode --help" 0
    
    run_test "Rust backend validation" "python3 -m whitespace_stego.cli --backend rust encode --help" 0
    
    echo -e "${YELLOW}=== Mutually Exclusive Option Tests ===${NC}"
    
    # Test 6: Mutually exclusive message options
    run_test "Mutually exclusive message options" "python3 -m whitespace_stego.cli encode --message test --message-file test_message.txt --carrier carrier --output test.out" 2
    
    # Test 7: Mutually exclusive carrier options (encode)
    run_test "Mutually exclusive carrier options (encode)" "python3 -m whitespace_stego.cli encode --message test --carrier carrier --carrier-file test_carrier.txt --output test.out" 2
    
    # Test 8: Mutually exclusive carrier options (decode)
    run_test "Mutually exclusive carrier options (decode)" "python3 -m whitespace_stego.cli decode --carrier carrier --carrier-file test_carrier.txt --output test.out" 2
    
    echo -e "${YELLOW}=== Missing Required Option Tests ===${NC}"
    
    # Test 9: Missing message option
    run_test "Missing message option" "python3 -m whitespace_stego.cli encode --carrier carrier --output test.out" 1
    
    # Test 10: Missing carrier option (encode)
    run_test "Missing carrier option (encode)" "python3 -m whitespace_stego.cli encode --message test --output test.out" 1
    
    # Test 11: Missing carrier option (decode)
    run_test "Missing carrier option (decode)" "python3 -m whitespace_stego.cli decode --output test.out" 1
    
    echo -e "${YELLOW}=== Encode Command Tests ===${NC}"
    
    # Test 12: Encode with message and carrier from command line, output to stdout
    run_test "Encode message+carrier to stdout" "python3 -m whitespace_stego.cli encode --message 'Hello World' --carrier 'This is a test carrier.'" 0
    
    # Test 13: Encode with message from command line, carrier from file, output to stdout
    run_test "Encode message+carrier_file to stdout" "python3 -m whitespace_stego.cli encode --message 'Secret message' --carrier-file test_carrier.txt" 0
    
    # Test 14: Encode with message from file, carrier from command line, output to stdout
    run_test "Encode message_file+carrier to stdout" "python3 -m whitespace_stego.cli encode --message-file test_message.txt --carrier 'Another carrier text.'" 0
    
    # Test 15: Encode with both from files, output to stdout
    run_test "Encode message_file+carrier_file to stdout" "python3 -m whitespace_stego.cli encode --message-file test_message.txt --carrier-file test_carrier.txt" 0
    
    # Test 16: Encode with explicit stdout output (-)
    run_test "Encode with explicit stdout (-)" "python3 -m whitespace_stego.cli encode --message 'Test with dash' --carrier 'Carrier with dash' --output -" 0
    
    # Test 17: Encode with file output
    run_test "Encode with file output" "python3 -m whitespace_stego.cli encode --message 'File output test' --carrier 'Carrier for file' --output encoded_file.txt" 0
    
    echo -e "${YELLOW}=== Decode Command Tests ===${NC}"
    
    # Test 18: Decode from file, output to stdout
    run_test "Decode from file to stdout" "python3 -m whitespace_stego.cli decode --carrier-file encoded_file.txt" 0
    
    # Test 19: Decode with explicit stdout output (-)
    run_test "Decode with explicit stdout (-)" "python3 -m whitespace_stego.cli decode --carrier-file encoded_file.txt --output -" 0
    
    # Test 20: Decode with file output
    run_test "Decode with file output" "python3 -m whitespace_stego.cli decode --carrier-file encoded_file.txt --output decoded_file.txt" 0
    
    # Test 21: Verify decoded content
    if [ -f "decoded_file.txt" ] && grep -q "File output test" "decoded_file.txt"; then
        echo -e "${GREEN}✅ PASS${NC}: Verify decoded content"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ FAIL${NC}: Verify decoded content"
        ((TESTS_FAILED++))
    fi
    echo ""
    
    echo -e "${YELLOW}=== Password Protection Tests ===${NC}"
    
    # Test 22: Encode with password protection
    run_test "Encode with password" "python3 -m whitespace_stego.cli encode --message 'Secret with password' --carrier 'Protected carrier' --password 'mypassword' --output encoded_pwd.txt" 0
    
    # Test 23: Decode with correct password
    run_test "Decode with correct password" "python3 -m whitespace_stego.cli decode --carrier-file encoded_pwd.txt --password 'mypassword'" 0
    
    # Test 24: Decode with wrong password
    run_test "Decode with wrong password" "python3 -m whitespace_stego.cli decode --carrier-file encoded_pwd.txt --password 'wrongpassword'" 1
    
    echo -e "${YELLOW}=== Unicode Support Tests ===${NC}"
    
    # Test 25: Encode Unicode content
    run_test "Encode Unicode content" "python3 -m whitespace_stego.cli encode --message 'Hello 世界 🌍' --carrier 'Unicode carrier: café naïve' --output encoded_unicode.txt" 0
    
    # Test 26: Decode Unicode content
    run_test "Decode Unicode content" "python3 -m whitespace_stego.cli decode --carrier-file encoded_unicode.txt" 0
    
    echo -e "${YELLOW}=== Advanced Feature Tests ===${NC}"
    
    # Test 27: Verbose mode
    run_test "Verbose mode" "python3 -m whitespace_stego.cli --verbose encode --message 'Verbose test' --carrier 'Verbose carrier' --output -" 0
    
    # Test 28: Rust backend error (when not installed)
    run_test "Rust backend error handling" "python3 -m whitespace_stego.cli --backend rust encode --message 'test' --carrier 'carrier'" 1
    
    echo -e "${YELLOW}=== Pipeline Simulation Tests ===${NC}"
    
    # Test 29: Roundtrip pipeline simulation
    echo "Testing roundtrip pipeline simulation..."
    encoded_output=$(python3 -m whitespace_stego.cli encode --message 'Pipeline test message' --carrier 'Pipeline carrier text' 2>/dev/null | tail -n 1)
    echo "$encoded_output" > temp_encoded.txt
    
    run_test "Pipeline roundtrip decode" "python3 -m whitespace_stego.cli decode --carrier-file temp_encoded.txt" 0
    
    echo -e "${YELLOW}=== Short Options Tests ===${NC}"
    
    # Test 30: All short options
    run_test "All short options" "python3 -m whitespace_stego.cli -b python encode -m 'Short options test' -c 'Short carrier text' -o -" 0
    
    echo -e "${YELLOW}=== Long Options Tests ===${NC}"
    
    # Test 31: All long options
    run_test "All long options" "python3 -m whitespace_stego.cli --backend python encode --message 'Long options test' --carrier 'Long carrier text' --output -" 0
    
    echo -e "${YELLOW}=== Test Summary ===${NC}"
    echo "Tests passed: $TESTS_PASSED"
    echo "Tests failed: $TESTS_FAILED"
    echo "Total tests: $((TESTS_PASSED + TESTS_FAILED))"
    
    if [ $TESTS_FAILED -eq 0 ]; then
        echo -e "${GREEN}🎉 All tests passed!${NC}"
        exit_code=0
    else
        echo -e "${RED}❌ Some tests failed!${NC}"
        exit_code=1
    fi
    
    # Cleanup
    cleanup_test_files
    
    exit $exit_code
}

# Run main function
main "$@" 