#!/bin/bash

# Comprehensive N-way comparison test for whitespace steganography implementations
# Tests: Python (all backends), Rust, C, Go, Pure Python CLI, Compiled Binary

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Test directory
TEST_DIR="/tmp/whitespace_stego_test"
mkdir -p "$TEST_DIR"

echo -e "${BLUE}=== Whitespace Steganography Comprehensive N-Way Comparison Test ===${NC}"
echo -e "${CYAN}Testing all implementations and backends:${NC}"
echo -e "  • Python CLI with Python backend"
echo -e "  • Python CLI with Rust backend" 
echo -e "  • Python CLI with C backend"
echo -e "  • Rust CLI binary"
echo -e "  • C binary"
echo -e "  • Go binary"
echo -e "  • Pure Python CLI"
echo -e "  • Compiled PyInstaller binary (all backends)"

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
    local backend="$2"
    local test_name="$3"
    local message_file="$4"
    local carrier_file="$5"
    local password="$6"
    local output_file="$7"
    
    echo -e "${BLUE}Testing $impl${backend:+ with $backend backend}: $test_name${NC}"
    
    # Encode
    case $impl in
        "python")
            PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "$backend" encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "rust")
            ./bin/whitespace-stego-rs encode \
                --mf "$message_file" \
                --cf "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "c")
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
        "pure-python")
            .venv/bin/whitespace-stego --backend "$backend" encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$output_file" \
                ${password:+--password "$password"}
            ;;
        "compiled")
            ./bin/whitespace-stego-py --backend "$backend" encode \
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
            decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "$backend" decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "rust")
            decoded_output=$(./bin/whitespace-stego-rs decode \
                --cf "$output_file" \
                ${password:+--password "$password"})
            ;;
        "c")
            # C binary requires output file, so we use a temp file
            local temp_decode_file="$TEST_DIR/temp_decode_$$.txt"
            ./bin/whitespace-stego-c decode \
                --carrier-file "$output_file" \
                --output "$temp_decode_file" \
                ${password:+--password "$password"}
            decoded_output=$(cat "$temp_decode_file")
            rm -f "$temp_decode_file"
            ;;
        "go")
            decoded_output=$(./bin/whitespace-stego-go decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "pure-python")
            decoded_output=$(.venv/bin/whitespace-stego --backend "$backend" decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
        "compiled")
            decoded_output=$(./bin/whitespace-stego-py --backend "$backend" decode \
                --carrier-file "$output_file" \
                ${password:+--password "$password"})
            ;;
    esac
    
    # Check if decoded output matches original message
    local original_message
    original_message=$(cat "$message_file")
    
    if [[ "$decoded_output" == *"$original_message"* ]]; then
        echo -e "${GREEN}✓ $impl${backend:+ with $backend backend}: $test_name PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ $impl${backend:+ with $backend backend}: $test_name FAILED${NC}"
        echo "Expected: $original_message"
        echo "Got: $decoded_output"
        return 1
    fi
}

# Function to test cross-implementation compatibility
test_cross_compatibility() {
    local source_impl="$1"
    local source_backend="$2"
    local target_impl="$3"
    local target_backend="$4"
    local test_name="$5"
    local message_file="$6"
    local carrier_file="$7"
    local password="$8"
    local temp_file="$9"
    
    echo -e "${BLUE}Testing $source_impl${source_backend:+ with $source_backend backend} -> $target_impl${target_backend:+ with $target_backend backend}: $test_name${NC}"
    
    # Encode with source implementation
    case $source_impl in
        "python")
            PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "$source_backend" encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
        "rust")
            ./bin/whitespace-stego-rs encode \
                --mf "$message_file" \
                --cf "$carrier_file" \
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
        "pure-python")
            .venv/bin/whitespace-stego --backend "$source_backend" encode \
                --message-file "$message_file" \
                --carrier-file "$carrier_file" \
                --output "$temp_file" \
                ${password:+--password "$password"}
            ;;
        "compiled")
            ./bin/whitespace-stego-py --backend "$source_backend" encode \
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
            decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "$target_backend" decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "rust")
            decoded_output=$(./bin/whitespace-stego-rs decode \
                --cf "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "c")
            # C binary requires output file, so we use a temp file
            local temp_decode_file="$TEST_DIR/temp_decode_$$.txt"
            ./bin/whitespace-stego-c decode \
                --carrier-file "$temp_file" \
                --output "$temp_decode_file" \
                ${password:+--password "$password"}
            decoded_output=$(cat "$temp_decode_file")
            rm -f "$temp_decode_file"
            ;;
        "go")
            decoded_output=$(./bin/whitespace-stego-go decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "pure-python")
            decoded_output=$(.venv/bin/whitespace-stego --backend "$target_backend" decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
        "compiled")
            decoded_output=$(./bin/whitespace-stego-py --backend "$target_backend" decode \
                --carrier-file "$temp_file" \
                ${password:+--password "$password"})
            ;;
    esac
    
    # Check if decoded output matches original message
    local original_message
    original_message=$(cat "$message_file")
    
    if [[ "$decoded_output" == *"$original_message"* ]]; then
        echo -e "${GREEN}✓ $source_impl${source_backend:+ with $source_backend backend} -> $target_impl${target_backend:+ with $target_backend backend}: $test_name PASSED${NC}"
        return 0
    else
        echo -e "${RED}✗ $source_impl${source_backend:+ with $source_backend backend} -> $target_impl${target_backend:+ with $target_backend backend}: $test_name FAILED${NC}"
        echo "Expected: $original_message"
        echo "Got: $decoded_output"
        return 1
    fi
}

# Function to test multiple messages in one carrier
test_multiple_messages() {
    echo -e "${BLUE}Testing multiple messages in one carrier${NC}"
    
    # Start with first message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/multi_msg1.txt" \
        --carrier-file "$TEST_DIR/multi_carrier.txt" \
        --output "$TEST_DIR/multi_encoded1.txt"
    
    # Add second message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/multi_msg2.txt" \
        --carrier-file "$TEST_DIR/multi_encoded1.txt" \
        --output "$TEST_DIR/multi_encoded2.txt"
    
    # Add third message
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/multi_msg3.txt" \
        --carrier-file "$TEST_DIR/multi_encoded2.txt" \
        --output "$TEST_DIR/multi_encoded3.txt"
    
    # Decode all messages
    local decoded_output
    decoded_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" decode \
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
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/alice_msg.txt" \
        --carrier-file "$TEST_DIR/multi_carrier.txt" \
        --output "$TEST_DIR/alice_encoded.txt" \
        --password "alice_password"
    
    # Encode message for Bob in the same carrier
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/bob_msg.txt" \
        --carrier-file "$TEST_DIR/alice_encoded.txt" \
        --output "$TEST_DIR/both_encoded.txt" \
        --password "bob_password"
    
    # Encode message for Charlie in the same carrier
    PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" encode \
        --message-file "$TEST_DIR/charlie_msg.txt" \
        --carrier-file "$TEST_DIR/both_encoded.txt" \
        --output "$TEST_DIR/all_encoded.txt" \
        --password "charlie_password"
    
    # Test that each recipient can only decode their own message
    local alice_output
    alice_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "alice_password")
    
    local bob_output
    bob_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" decode \
        --carrier-file "$TEST_DIR/all_encoded.txt" \
        --password "bob_password")
    
    local charlie_output
    charlie_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" decode \
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
    wrong_output=$(PYTHONPATH=src:. python3 -m whitespace_stego.cli --backend "python" decode \
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
    
    # Test Python CLI with all backends
    for backend in "python" "rust" "c"; do
        # Test 1-3: Python ASCII message without password (all backends)
        total_tests=$((total_tests + 1))
        if test_implementation "python" "$backend" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test1_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
        
        # Test 4-6: Python ASCII message with password (all backends)
        total_tests=$((total_tests + 1))
        if test_implementation "python" "$backend" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test2_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
    done
    
    # Test 7-9: Rust, C, Go implementations
    for impl in "rust" "c" "go"; do
        total_tests=$((total_tests + 1))
        if test_implementation "$impl" "" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test3_${impl}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
        
        total_tests=$((total_tests + 1))
        if test_implementation "$impl" "" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test4_${impl}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
    done
    
    # Test 10-15: Pure Python CLI with all backends
    for backend in "python" "rust" "c"; do
        total_tests=$((total_tests + 1))
        if test_implementation "pure-python" "$backend" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test5_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
        
        total_tests=$((total_tests + 1))
        if test_implementation "pure-python" "$backend" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test6_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
    done
    
    # Test 16-21: Compiled binary with all backends
    for backend in "python" "rust" "c"; do
        total_tests=$((total_tests + 1))
        if test_implementation "compiled" "$backend" "ASCII no password" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/test7_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
        
        total_tests=$((total_tests + 1))
        if test_implementation "compiled" "$backend" "ASCII with password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/test8_${backend}_encoded.txt"; then
            passed_tests=$((passed_tests + 1))
        fi
    done
    
    echo -e "\n${BLUE}=== Cross-Implementation Tests ===${NC}"
    
    # Test Python backends cross-compatibility
    for source_backend in "python" "rust" "c"; do
        for target_backend in "python" "rust" "c"; do
            if [[ "$source_backend" != "$target_backend" ]]; then
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "python" "$source_backend" "python" "$target_backend" "Python ${source_backend}->${target_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_python_${source_backend}_${target_backend}.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
                
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "python" "$source_backend" "python" "$target_backend" "Python ${source_backend}->${target_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_python_${source_backend}_${target_backend}_pw.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
            fi
        done
    done
    
    # Test Pure Python CLI cross-compatibility
    for source_backend in "python" "rust" "c"; do
        for target_backend in "python" "rust" "c"; do
            if [[ "$source_backend" != "$target_backend" ]]; then
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "pure-python" "$source_backend" "pure-python" "$target_backend" "Pure Python ${source_backend}->${target_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_pure_${source_backend}_${target_backend}.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
                
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "pure-python" "$source_backend" "pure-python" "$target_backend" "Pure Python ${source_backend}->${target_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_pure_${source_backend}_${target_backend}_pw.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
            fi
        done
    done
    
    # Test Compiled binary cross-compatibility
    for source_backend in "python" "rust" "c"; do
        for target_backend in "python" "rust" "c"; do
            if [[ "$source_backend" != "$target_backend" ]]; then
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "compiled" "$source_backend" "compiled" "$target_backend" "Compiled ${source_backend}->${target_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_compiled_${source_backend}_${target_backend}.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
                
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "compiled" "$source_backend" "compiled" "$target_backend" "Compiled ${source_backend}->${target_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_compiled_${source_backend}_${target_backend}_pw.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
            fi
        done
    done
    
    # Test cross-implementation compatibility (Python backends <-> Native binaries)
    for python_backend in "python" "rust" "c"; do
        for native_impl in "rust" "c" "go"; do
            # Python -> Native
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "python" "$python_backend" "$native_impl" "" "Python ${python_backend}->${native_impl} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_python_${python_backend}_${native_impl}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "python" "$python_backend" "$native_impl" "" "Python ${python_backend}->${native_impl} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_python_${python_backend}_${native_impl}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            # Native -> Python
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "python" "$python_backend" "${native_impl}->Python ${python_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_${native_impl}_python_${python_backend}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "python" "$python_backend" "${native_impl}->Python ${python_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_${native_impl}_python_${python_backend}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
        done
    done
    
    # Test Pure Python CLI <-> Native binaries
    for python_backend in "python" "rust" "c"; do
        for native_impl in "rust" "c" "go"; do
            # Pure Python -> Native
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "pure-python" "$python_backend" "$native_impl" "" "Pure Python ${python_backend}->${native_impl} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_pure_${python_backend}_${native_impl}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "pure-python" "$python_backend" "$native_impl" "" "Pure Python ${python_backend}->${native_impl} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_pure_${python_backend}_${native_impl}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            # Native -> Pure Python
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "pure-python" "$python_backend" "${native_impl}->Pure Python ${python_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_${native_impl}_pure_${python_backend}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "pure-python" "$python_backend" "${native_impl}->Pure Python ${python_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_${native_impl}_pure_${python_backend}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
        done
    done
    
    # Test Compiled binary <-> Native binaries
    for compiled_backend in "python" "rust" "c"; do
        for native_impl in "rust" "c" "go"; do
            # Compiled -> Native
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "compiled" "$compiled_backend" "$native_impl" "" "Compiled ${compiled_backend}->${native_impl} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_compiled_${compiled_backend}_${native_impl}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "compiled" "$compiled_backend" "$native_impl" "" "Compiled ${compiled_backend}->${native_impl} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_compiled_${compiled_backend}_${native_impl}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            # Native -> Compiled
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "compiled" "$compiled_backend" "${native_impl}->Compiled ${compiled_backend} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_${native_impl}_compiled_${compiled_backend}.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
            
            total_tests=$((total_tests + 1))
            if test_cross_compatibility "$native_impl" "" "compiled" "$compiled_backend" "${native_impl}->Compiled ${compiled_backend} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_${native_impl}_compiled_${compiled_backend}_pw.txt"; then
                passed_tests=$((passed_tests + 1))
            fi
        done
    done
    
    # Test Native binary cross-compatibility
    for source_impl in "rust" "c" "go"; do
        for target_impl in "rust" "c" "go"; do
            if [[ "$source_impl" != "$target_impl" ]]; then
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "$source_impl" "" "$target_impl" "" "${source_impl}->${target_impl} ASCII" "$TEST_DIR/message1.txt" "$TEST_DIR/carrier1.txt" "" "$TEST_DIR/cross_${source_impl}_${target_impl}.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
                
                total_tests=$((total_tests + 1))
                if test_cross_compatibility "$source_impl" "" "$target_impl" "" "${source_impl}->${target_impl} password" "$TEST_DIR/message2.txt" "$TEST_DIR/carrier2.txt" "testpass123" "$TEST_DIR/cross_${source_impl}_${target_impl}_pw.txt"; then
                    passed_tests=$((passed_tests + 1))
                fi
            fi
        done
    done
    
    echo -e "\n${BLUE}=== Advanced Feature Tests ===${NC}"
    
    # Test multiple messages in one carrier
    total_tests=$((total_tests + 1))
    if test_multiple_messages; then
        passed_tests=$((passed_tests + 1))
    fi
    
    # Test multi-recipient password-protected messages
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