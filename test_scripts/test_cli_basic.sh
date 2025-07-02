#!/bin/bash

# Basic CLI Test Suite
# Tests same-implementation roundtrips for all CLI tools

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Basic test cases
TEST_CASES=(
    # Format: "message|carrier|password|description"
    "Hello|Hello World|password|Basic ASCII"
    "Hello, World!|Test carrier|secret123|ASCII with punctuation"
    "Привет мир|Привет мир|password|Cyrillic"
    "你好世界|你好世界|password|Chinese"
    "こんにちは世界|こんにちは世界|password|Japanese"
    "Hello 🌍 World|Hello 🌍 World|password|ASCII with emoji"
    "🚀 Rocket|🚀 Rocket|password|Emoji heavy"
    "Test with 🎉🎊🎈|Test with 🎉🎊🎈|password|Mixed emoji"
    "Unicode: αβγδε|Unicode: αβγδε|password|Greek"
    "Special: !@#$%^&*()|Special: !@#$%^&*()|password|Special chars"
    "Multi\nline\ntext|Multi\nline\ncarrier|password|Newlines"
    "Hello|Hello World||No password"
)

# CLI implementations
CLI_IMPLS=("python" "rust" "c")

# Function to print colored output
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
        "WARN")
            echo -e "${YELLOW}⚠ WARN${NC}: $message"
            ;;
    esac
}

# Function to create temporary file with content
create_temp_file() {
    local content="$1"
    local prefix="$2"
    local temp_file=$(mktemp "${prefix}.XXXXXX")
    echo -n "$content" > "$temp_file"
    echo "$temp_file"
}

# Function to cleanup temporary files
cleanup_temp_files() {
    local files=("$@")
    for file in "${files[@]}"; do
        if [[ -f "$file" ]]; then
            rm -f "$file"
        fi
    done
}

# Function to run CLI encode command
run_cli_encode() {
    local impl=$1
    local message_file=$2
    local carrier_file=$3
    local password=$4
    local output_file=$5
    
    case $impl in
        "python")
            local cmd="python -m whitespace_stego.cli --backend python encode"
            if [[ -n "$message_file" ]]; then
                cmd="$cmd --message-file $message_file"
            fi
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --carrier-file $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
        "rust")
            local cmd="./whitespace-stego-rs encode"
            if [[ -n "$message_file" ]]; then
                cmd="$cmd --mf $message_file"
            fi
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --cf $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
        "c")
            local cmd="./whitespace-stego-c encode"
            if [[ -n "$message_file" ]]; then
                cmd="$cmd --message-file $message_file"
            fi
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --carrier-file $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
    esac
    
    eval "$cmd" 2>/dev/null
    return $?
}

# Function to run CLI decode command
run_cli_decode() {
    local impl=$1
    local carrier_file=$2
    local password=$3
    local output_file=$4
    
    case $impl in
        "python")
            local cmd="python -m whitespace_stego.cli --backend python decode"
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --carrier-file $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
        "rust")
            local cmd="./whitespace-stego-rs decode"
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --cf $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
        "c")
            local cmd="./whitespace-stego-c decode"
            if [[ -n "$carrier_file" ]]; then
                cmd="$cmd --carrier-file $carrier_file"
            fi
            if [[ -n "$password" ]]; then
                cmd="$cmd --password '$password'"
            fi
            cmd="$cmd --output $output_file"
            ;;
    esac
    
    eval "$cmd" 2>/dev/null
    return $?
}

# Function to test single roundtrip
test_roundtrip() {
    local encode_impl=$1
    local decode_impl=$2
    local message=$3
    local carrier=$4
    local password=$5
    local description=$6
    
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    local test_name="Encode($encode_impl) → Decode($decode_impl): $description"
    
    # Create temporary files
    local message_file=""
    local carrier_file=""
    local encoded_file=""
    local decoded_file=""
    
    if [[ -n "$message" ]]; then
        message_file=$(create_temp_file "$message" "msg")
    fi
    if [[ -n "$carrier" ]]; then
        carrier_file=$(create_temp_file "$carrier" "carrier")
    fi
    
    encoded_file=$(mktemp "encoded.XXXXXX")
    decoded_file=$(mktemp "decoded.XXXXXX")
    
    # Encode
    if ! run_cli_encode "$encode_impl" "$message_file" "$carrier_file" "$password" "$encoded_file"; then
        print_status "FAIL" "$test_name - Encode failed"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        cleanup_temp_files "$message_file" "$carrier_file" "$encoded_file" "$decoded_file"
        return 1
    fi
    
    # Decode
    if ! run_cli_decode "$decode_impl" "$encoded_file" "$password" "$decoded_file"; then
        print_status "FAIL" "$test_name - Decode failed"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        cleanup_temp_files "$message_file" "$carrier_file" "$encoded_file" "$decoded_file"
        return 1
    fi
    
    # Compare results
    local decoded_content=$(cat "$decoded_file")
    if [[ "$decoded_content" == "$message" ]]; then
        print_status "PASS" "$test_name"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        print_status "FAIL" "$test_name - Mismatch: expected '$message', got '$decoded_content'"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
    
    cleanup_temp_files "$message_file" "$carrier_file" "$encoded_file" "$decoded_file"
}

# Function to test same-implementation roundtrips
test_same_implementation() {
    local impl=$1
    
    print_status "INFO" "Testing same-implementation roundtrips: $impl"
    
    for test_case in "${TEST_CASES[@]}"; do
        IFS='|' read -r message carrier password description <<< "$test_case"
        test_roundtrip "$impl" "$impl" "$message" "$carrier" "$password" "$description"
    done
}

# Function to test error conditions
test_error_conditions() {
    print_status "INFO" "Testing error conditions"
    
    # Test empty message (should fail)
    for impl in "${CLI_IMPLS[@]}"; do
        TOTAL_TESTS=$((TOTAL_TESTS + 1))
        local message_file=$(create_temp_file "" "empty_msg")
        local carrier_file=$(create_temp_file "test carrier" "test_carrier")
        local output_file=$(mktemp "error_test.XXXXXX")
        
        if run_cli_encode "$impl" "$message_file" "$carrier_file" "" "$output_file"; then
            print_status "FAIL" "Empty message should fail for $impl"
            FAILED_TESTS=$((FAILED_TESTS + 1))
        else
            print_status "PASS" "Empty message correctly rejected by $impl"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        fi
        
        cleanup_temp_files "$message_file" "$carrier_file" "$output_file"
    done
}

# Function to test wrong password
test_wrong_password() {
    print_status "INFO" "Testing wrong password scenarios"
    
    local test_message="Secret message"
    local test_carrier="Test carrier"
    local correct_password="correct123"
    local wrong_password="wrong456"
    
    for impl in "${CLI_IMPLS[@]}"; do
        TOTAL_TESTS=$((TOTAL_TESTS + 1))
        
        local message_file=$(create_temp_file "$test_message" "msg")
        local carrier_file=$(create_temp_file "$test_carrier" "carrier")
        local encoded_file=$(mktemp "encoded.XXXXXX")
        local decoded_file=$(mktemp "decoded.XXXXXX")
        
        # Encode with correct password
        if ! run_cli_encode "$impl" "$message_file" "$carrier_file" "$correct_password" "$encoded_file"; then
            print_status "FAIL" "Failed to encode with correct password for $impl"
            FAILED_TESTS=$((FAILED_TESTS + 1))
            cleanup_temp_files "$message_file" "$carrier_file" "$encoded_file" "$decoded_file"
            continue
        fi
        
        # Try to decode with wrong password
        if run_cli_decode "$impl" "$encoded_file" "$wrong_password" "$decoded_file"; then
            local decoded_content=$(cat "$decoded_file")
            if [[ "$decoded_content" == "$test_message" ]]; then
                print_status "FAIL" "Wrong password should fail for $impl"
                FAILED_TESTS=$((FAILED_TESTS + 1))
            else
                print_status "PASS" "Wrong password correctly rejected by $impl"
                PASSED_TESTS=$((PASSED_TESTS + 1))
            fi
        else
            print_status "PASS" "Wrong password correctly rejected by $impl"
            PASSED_TESTS=$((PASSED_TESTS + 1))
        fi
        
        cleanup_temp_files "$message_file" "$carrier_file" "$encoded_file" "$decoded_file"
    done
}

# Function to print test summary
print_summary() {
    echo
    echo "=========================================="
    echo "           TEST SUMMARY"
    echo "=========================================="
    echo "Total tests: $TOTAL_TESTS"
    echo -e "Passed: ${GREEN}$PASSED_TESTS${NC}"
    echo -e "Failed: ${RED}$FAILED_TESTS${NC}"
    
    if [[ $FAILED_TESTS -eq 0 ]]; then
        echo -e "${GREEN}All tests passed! 🎉${NC}"
        exit 0
    else
        echo -e "${RED}Some tests failed! ❌${NC}"
        exit 1
    fi
}

# Main test execution
main() {
    echo "=========================================="
    echo "  Basic CLI Test Suite"
    echo "=========================================="
    echo
    
    # Check if CLI tools exist
    if [[ ! -f "./whitespace-stego-rs" ]]; then
        print_status "FAIL" "Rust CLI not found: ./whitespace-stego-rs"
        exit 1
    fi
    
    if [[ ! -f "./whitespace-stego-c" ]]; then
        print_status "FAIL" "C CLI not found: ./whitespace-stego-c"
        exit 1
    fi
    
    if ! command -v python &> /dev/null; then
        print_status "FAIL" "Python not found"
        exit 1
    fi
    
    print_status "INFO" "All CLI tools found, starting tests..."
    echo
    
    # Test same-implementation roundtrips
    for impl in "${CLI_IMPLS[@]}"; do
        test_same_implementation "$impl"
        echo
    done
    
    # Test error conditions
    test_error_conditions
    echo
    
    # Test wrong password scenarios
    test_wrong_password
    echo
    
    # Print summary
    print_summary
}

# Run main function
main "$@" 