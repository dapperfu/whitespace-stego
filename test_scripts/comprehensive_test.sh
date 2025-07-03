#!/bin/bash

# Comprehensive N-way comparison test for whitespace steganography implementations
# Tests: Python, Rust, C, Go implementations with various scenarios

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test directory
TEST_DIR="/tmp/whitespace_stego_test"
mkdir -p "$TEST_DIR"

echo -e "${BLUE}=== Whitespace Steganography N-Way Comparison Test ===${NC}"

# Function to run test and check result
run_test() {
    local test_name="$1"
    local command="$2"
    local expected_output="$3"
    
    echo -e "${YELLOW}Running: $test_name${NC}"
    echo "Command: $command"
    
    local output
    if output=$(eval "$command" 2>&1); then
        if [[ "$output" == *"$expected_output"* ]]; then
            echo -e "${GREEN}✓ PASS: $test_name${NC}"
            return 0
        else
            echo -e "${RED}✗ FAIL: $test_name (unexpected output)${NC}"
            echo "Expected: $expected_output"
            echo "Got: $output"
            return 1
        fi
    else
        echo -e "${RED}✗ FAIL: $test_name (command failed)${NC}"
        echo "Error: $output"
        return 1
    fi
}

# Function to create test files
create_test_files() {
    echo "Creating test files..."
    
    # Basic test files
    echo "Hello, World!" > "$TEST_DIR/message1.txt"
    echo "This is a secret message" > "$TEST_DIR/message2.txt"
    echo "Carrier text for testing" > "$TEST_DIR/carrier1.txt"
    echo "Another carrier text" > "$TEST_DIR/carrier2.txt"
    
    # Multiple messages
    echo "First message" > "$TEST_DIR/multi_msg1.txt"
    echo "Second message" > "$TEST_DIR/multi_msg2.txt"
    echo "Third message" > "$TEST_DIR/multi_msg3.txt"
    
    # Multi-recipient messages
    echo "Message for Alice" > "$TEST_DIR/alice_msg.txt"
    echo "Message for Bob" > "$TEST_DIR/bob_msg.txt"
    echo "Message for Charlie" > "$TEST_DIR/charlie_msg.txt"
    
    # Multi-recipient carrier
    echo "Multi-recipient carrier text" > "$TEST_DIR/multi_carrier.txt"
}

# Function to test single implementation encode/decode
test_implementation() {
    local impl="$1"
    local test_name="$2"
    local message_file="$3"
    local carrier_file="$4"
    local password="$5"
    local output_file="$6"
    
    echo -e "${BLUE}Testing $impl: $test_name${NC}"
    
    # Encode
    case $impl in
        "python")
            PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "rust")
            # Assuming Rust CLI is available
            cargo run --bin whitespace-stego-cli encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "c")
            # Assuming C binary is available
            ./bin/whitespace-stego-c encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "go")
            ./bin/whitespace-stego-go encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
    esac
    
    # Decode
    local decoded_output
    case $impl in
        "python")
            decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "rust")
            decoded_output=$(cargo run --bin whitespace-stego-cli decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "c")
            decoded_output=$(./bin/whitespace-stego-c decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "go")
            decoded_output=$(./bin/whitespace-stego-go decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
    esac
    
    # Check if decoded output matches original message
    local original_message
    original_message=$(cat "$message_file")
    
    if [[ "$decoded_output" == *"$original_message"* ]]; then
        echo -e "${GREEN}✓ $impl: $test_name PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ $impl: $test_name FAILED${NC}"
        echo "Expected: $original_message"
        echo "Got: $decoded_output"
        return 1
    fi
}

# Function to test cross-implementation compatibility
test_cross_compatibility() {
    local source_impl="$1"
    local target_impl="$2"
    local test_name="$3"
    local message_file="$4"
    local carrier_file="$5"
    local password="$6"
    local temp_file="$7"
    
    echo -e "${BLUE}Testing $source_impl -> $target_impl: $test_name${NC}"
    
    # Encode with source implementation
    case $source_impl in
        "python")
            PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
        "rust")
            cargo run --bin whitespace-stego-cli encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
        "c")
            ./bin/whitespace-stego-c encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
        "go")
            ./bin/whitespace-stego-go encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
    esac
    
    # Decode with target implementation
    local decoded_output
    case $target_impl in
        "python")
            decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "rust")
            decoded_output=$(cargo run --bin whitespace-stego-cli decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "c")
            decoded_output=$(./bin/whitespace-stego-c decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "go")
            decoded_output=$(./bin/whitespace-stego-go decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
    esac
    
    # Check if decoded output matches original message
    local original_message
    original_message=$(cat "$message_file")
    
    if [[ "$decoded_output" == *"$original_message"* ]]; then
        echo -e "${GREEN}✓ $source_impl -> $target_impl: $test_name PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ $source_impl -> $target_impl: $test_name FAILED${NC}"
        echo "Expected: $original_message"
        echo "Got: $decoded_output"
        return 1
    fi
}

# Function to test multiple messages in one carrier
test_multiple_messages() {
    echo -e "${BLUE}Testing multiple messages in one carrier${NC}"
    
    # Start with first message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/multi_msg1.txt" \
        --carrier-file "$TEST_DIR/multi_carrier.txt" \
        --output "$TEST_DIR/multi_encoded1.txt"
    
    # Add second message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/multi_msg2.txt" \
        --carrier-file "$TEST_DIR/multi_encoded1.txt" \
        --output "$TEST_DIR/multi_encoded2.txt"
    
    # Add third message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/multi_msg3.txt" \
        --carrier-file "$TEST_DIR/multi_encoded2.txt" \
        --output "$TEST_DIR/multi_encoded3.txt"
    
    # Decode all messages
    local decoded_output
    decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
        --carrier-file "$TEST_DIR/multi_encoded3.txt")
    
    # Check if all messages are present
    local msg1=$(cat "$TEST_DIR/multi_msg1.txt")
    local msg2=$(cat "$TEST_DIR/multi_msg2.txt")
    local msg3=$(cat "$TEST_DIR/multi_msg3.txt")
    
    if [[ "$decoded_output" == *"$msg1"* && "$decoded_output" == *"$msg2"* && "$decoded_output" == *"$msg3"* ]]; then
        echo -e "${GREEN}✓ Multiple messages test PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ Multiple messages test FAILED${NC}"
        echo "Decoded output: $decoded_output"
        return 1
    fi
}

# Function to test multiple password-protected messages for different recipients
test_multi_recipient() {
    echo -e "${BLUE}Testing multiple password-protected messages for different recipients${NC}"
    
    # Encode message for Alice
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/alice_msg.txt" \
        --carrier-file "$TEST_DIR/multi_carrier.txt" \
        --output "$TEST_DIR/alice_encoded.txt" \
        --password "alice_password"
    
    # Encode message for Bob in the same carrier
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/bob_msg.txt" \
        --carrier-file "$TEST_DIR/alice_encoded.txt" \
        --output "$TEST_DIR/both_encoded.txt" \
        --password "bob_password"
    
    # Encode message for Charlie in the same carrier
    PYTHONPATH=src:. python3 -m whitespace_stego.cli encode \
        --message-file "$TEST_DIR/charlie_msg.txt" \
        --carrier-file "$TEST_DIR/both_encoded.txt" \
        --output "$TEST_DIR/all_encoded.txt" \
        --password "charlie_password"
    
    # Test that each recipient can only decode their own message
    local alice_output
    alice_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "alice_password")
    
    local bob_output
    bob_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "bob_password")
    
    local charlie_output
    charlie_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "charlie_password")
    
    # Check results
    local alice_msg=$(cat "$TEST_DIR/alice_msg.txt")
    local bob_msg=$(cat "$TEST_DIR/bob_msg.txt")
    local charlie_msg=$(cat "$TEST_DIR/charlie_msg.txt")
    
    local success=true
    
    if [[ "$alice_output" == *"$alice_msg"* ]]; then
        echo -e "${GREEN}✓ Alice can decode her message${NC}"
    else
        echo -e "${RED}✗ Alice cannot decode her message${NC}"
        success=false
    fi
    
    if [[ "$bob_output" == *"$bob_msg"* ]]; then
        echo -e "${GREEN}✓ Bob can decode his message${NC}"
    else
        echo -e "${RED}✗ Bob cannot decode his message${NC}"
        success=false
    fi
    
    if [[ "$charlie_output" == *"$charlie_msg"* ]]; then
        echo -e "${GREEN}✓ Charlie can decode his message${NC}"
    else
        echo -e "${RED}✗ Charlie cannot decode his message${NC}"
        success=false
    fi
    
    # Test that wrong passwords don't work
    local wrong_output
    wrong_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "wrong_password" 2>&1 || true)
    
    if [[ "$wrong_output" == *"invalid password"* || "$wrong_output" == *"Invalid password"* ]]; then
        echo -e "${GREEN}✓ Wrong password correctly rejected${NC}"
    else
        echo -e "${RED}✗ Wrong password not properly rejected${NC}"
        success=false
    fi
    
    if $success; then
        echo -e "${GREEN}✓ Multi-recipient test PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ Multi-recipient test FAILED${NC}"
        return 1
    fi
}

# Main test execution
main() {
    echo "Setting up test environment..."
    create_test_files
    
    local total_tests=0
    local passed_tests=0
    
    echo -e "\n${BLUE}=== Basic Functionality Tests ===${NC}"
    
    # Test 1: Python ASCII message without password
    total_tests=$((total_tests + 1))
    if test_implementation "python" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test1_encoded.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 2: Python ASCII message with password
    total_tests=$((total_tests + 1))
    if test_implementation "python" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test2_encoded.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 3: Go ASCII message without password
    total_tests=$((total_tests + 1))
    if test_implementation "go" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test3_encoded.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 4: Go ASCII message with password
    total_tests=$((total_tests + 1))
    if test_implementation "go" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test4_encoded.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    echo -e "\n${BLUE}=== Cross-Implementation Tests ===${NC}"
    
    # Test 5: Python -> Go
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "go" "Python->Go ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross1.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 6: Go -> Python
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "python" "Go->Python ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross2.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 7: Python -> Go (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "go" "Python->Go password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross3.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 8: Go -> Python (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "python" "Go->Python password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross4.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 9: Python -> Rust
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "rust" "Python->Rust ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross5.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 10: Rust -> Python
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "python" "Rust->Python ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross6.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 11: Python -> Rust (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "rust" "Python->Rust password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross7.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 12: Rust -> Python (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "python" "Rust->Python password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross8.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 13: Go -> Rust
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "rust" "Go->Rust ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross9.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 14: Rust -> Go
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "go" "Rust->Go ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross10.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 15: Go -> Rust (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "rust" "Go->Rust password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross11.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 16: Rust -> Go (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "go" "Rust->Go password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross12.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 17: Python -> C
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "c" "Python->C ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross13.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 18: C -> Python
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "python" "C->Python ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross14.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 19: Python -> C (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "python" "c" "Python->C password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross15.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 20: C -> Python (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "python" "C->Python password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross16.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 21: Go -> C
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "c" "Go->C ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross17.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 22: C -> Go
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "go" "C->Go ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross18.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 23: Go -> C (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "go" "c" "Go->C password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross19.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 24: C -> Go (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "go" "C->Go password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross20.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 25: Rust -> C
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "c" "Rust->C ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross21.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 26: C -> Rust
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "rust" "C->Rust ASCII" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "" "$TEST_DIR/cross22.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 27: Rust -> C (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "rust" "c" "Rust->C password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "testpass123" "$TEST_DIR/cross23.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 28: C -> Rust (password)
    total_tests=$((total_tests + 1))
    if test_cross_compatibility "c" "rust" "C->Rust password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross24.txt"; then
        passed_tests=$((passed_tests + 1))
    fi
    
    echo -e "\n${BLUE}=== Advanced Feature Tests ===${NC}"
    
    # Test 29: Multiple messages in one carrier
    total_tests=$((total_tests + 1))
    if test_multiple_messages; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test 30: Multi-recipient password-protected messages
    total_tests=$((total_tests + 1))
    if test_multi_recipient; then
        passed_tests=$((passed_tests + 1))
    fi
    
    echo -e "\n${BLUE}=== Test Summary ===${NC}"
    echo "Total tests: $total_tests"
    echo "Passed: $passed_tests"
    echo "Failed: $((total_tests - passed_tests))"
    
    if [ $passed_tests -eq $total_tests ]; then
        echo -e "${GREEN}🎉 All tests PASSED!${NC}"
        exit 0
    else
        echo -e "${RED}❌ Some tests FAILED!${NC}"
        exit 1
    fi
}

# Run main function
main "$@" 