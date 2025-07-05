#!/bin/bash

# Benchmark Configuration
# Defines encode/decode commands for each implementation

# Test files
TEST_CARRIER_FILE="${PROJECT_ROOT}/test_carrier.txt"
TEST_MESSAGE_FILE="${PROJECT_ROOT}/test_message.txt"
TEST_ENCODED_FILE="${PROJECT_ROOT}/test_encoded.txt"
TEST_DECODED_FILE="${PROJECT_ROOT}/test_decoded.txt"

# Create test files
create_test_files() {
    echo "$TEST_CARRIER" > "$TEST_CARRIER_FILE"
    echo "$TEST_MESSAGE" > "$TEST_MESSAGE_FILE"
}

# Clean up test files
cleanup_test_files() {
    rm -f "$TEST_CARRIER_FILE" "$TEST_MESSAGE_FILE" "$TEST_ENCODED_FILE" "$TEST_DECODED_FILE"
}

# C Implementation Commands (currently disabled due to segfaults)
get_c_encode_cmd() {
    local impl=$1
    local message=$2
    local password=$3
    
    # C implementations are currently segfaulting, so return a dummy command
    echo "echo 'C implementation $impl not available (segfault)'"
}

get_c_decode_cmd() {
    local impl=$1
    local password=$2
    
    # C implementations are currently segfaulting, so return a dummy command
    echo "echo 'C implementation $impl not available (segfault)'"
}

# Rust Implementation Commands
get_rust_encode_cmd() {
    local message=$1
    local password=$2
    
    echo "${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs encode -m '$message' --cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'}"
}

get_rust_decode_cmd() {
    local password=$1
    
    echo "${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs decode --cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'}"
}

# Go Implementation Commands
get_go_encode_cmd() {
    local message=$1
    local password=$2
    
    echo "${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go encode -m '$message' -cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'}"
}

get_go_decode_cmd() {
    local password=$1
    
    echo "${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go decode -cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'}"
}

# Python Implementation Commands
get_python_encode_cmd() {
    local backend=$1
    local message=$2
    local password=$3
    
    case $backend in
        "python-pure")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'} -b python"
            ;;
        "python-rust")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'} -b rust"
            ;;
        "python-c")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'} -b c"
            ;;
        *)
            echo "echo 'Unknown Python backend: $backend'"
            ;;
    esac
}

get_python_decode_cmd() {
    local backend=$1
    local password=$2
    
    case $backend in
        "python-pure")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'} -b python"
            ;;
        "python-rust")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'} -b rust"
            ;;
        "python-c")
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'} -b c"
            ;;
        *)
            echo "echo 'Unknown Python backend: $backend'"
            ;;
    esac
}

# Get encode command for any implementation
get_encode_cmd() {
    local impl=$1
    local message=$2
    local password=$3
    
    case $impl in
        static-c|static-c-small|static-c-tiny|dynamic-c)
            get_c_encode_cmd "$impl" "$message" "$password"
            ;;
        rust)
            get_rust_encode_cmd "$message" "$password"
            ;;
        go)
            get_go_encode_cmd "$message" "$password"
            ;;
        python-pure|python-rust|python-c)
            get_python_encode_cmd "$impl" "$message" "$password"
            ;;
        *)
            echo "echo 'Unknown implementation: $impl'"
            ;;
    esac
}

# Get decode command for any implementation
get_decode_cmd() {
    local impl=$1
    local password=$2
    
    case $impl in
        static-c|static-c-small|static-c-tiny|dynamic-c)
            get_c_decode_cmd "$impl" "$password"
            ;;
        rust)
            get_rust_decode_cmd "$password"
            ;;
        go)
            get_go_decode_cmd "$password"
            ;;
        python-pure|python-rust|python-c)
            get_python_decode_cmd "$impl" "$password"
            ;;
        *)
            echo "echo 'Unknown implementation: $impl'"
            ;;
    esac
} 