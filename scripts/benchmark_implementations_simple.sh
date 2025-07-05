#!/bin/bash

# Simple Benchmark Implementation Comparison Script
# Compares Rust, Go, and Python implementations

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
RESULTS_DIR="${PROJECT_ROOT}/benchmark_results"
LOG_FILE="${RESULTS_DIR}/benchmark_simple.log"

# Default configuration
DEFAULT_RUNS=3
RUNS=${1:-$DEFAULT_RUNS}
VERBOSE=${2:-false}

# Test data
TEST_MESSAGES=(
    "Hello, World!"
    "This is a longer test message with spaces and punctuation!"
    "Unicode: 🚀🌟🎉"
    "A" "B" "C"
)

TEST_PASSWORDS=(
    ""
    "simple_password"
    "complex_password_123!@#"
)

TEST_CARRIER="This is a sample carrier text that will be used for testing the whitespace steganography implementations. It contains enough text to embed various sized messages."

# Test files
TEST_CARRIER_FILE="${PROJECT_ROOT}/test_carrier.txt"
TEST_ENCODED_FILE="${PROJECT_ROOT}/test_encoded.txt"
TEST_DECODED_FILE="${PROJECT_ROOT}/test_decoded.txt"

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

# Create test files
create_test_files() {
    echo "$TEST_CARRIER" > "$TEST_CARRIER_FILE"
}

# Clean up test files
cleanup_test_files() {
    rm -f "$TEST_CARRIER_FILE" "$TEST_ENCODED_FILE" "$TEST_DECODED_FILE"
}

# Check if implementation is available
check_implementation() {
    local impl=$1
    local path=$2
    
    if [ -f "$path" ] && [ -x "$path" ]; then
        return 0
    else
        return 1
    fi
}

# Benchmark a single implementation
benchmark_impl() {
    local impl_name=$1
    local encode_cmd=$2
    local decode_cmd=$3
    local message=$4
    local password=$5
    local runs=$6
    
    local encode_times=()
    local decode_times=()
    local total_times=()
    
    log "Benchmarking $impl_name with message: '$message'"
    
    for ((i=1; i<=runs; i++)); do
        # Encode benchmark
        local encode_start=$(date +%s.%N)
        if ! eval "$encode_cmd" > /dev/null 2>&1; then
            log_error "$impl_name: Encode command failed on run $i"
            return 1
        fi
        local encode_end=$(date +%s.%N)
        local encode_time=$(echo "$encode_end - $encode_start" | bc -l)
        encode_times+=("$encode_time")
        
        # Decode benchmark
        local decode_start=$(date +%s.%N)
        if ! eval "$decode_cmd" > /dev/null 2>&1; then
            log_error "$impl_name: Decode command failed on run $i"
            return 1
        fi
        local decode_end=$(date +%s.%N)
        local decode_time=$(echo "$decode_end - $decode_start" | bc -l)
        decode_times+=("$decode_time")
        
        # Total time
        local total_time=$(echo "$encode_time + $decode_time" | bc -l)
        total_times+=("$total_time")
        
        if [ "$VERBOSE" = "true" ]; then
            echo "  Run $i: encode=${encode_time}s, decode=${decode_time}s, total=${total_time}s"
        fi
    done
    
    # Calculate statistics
    local encode_sum=0
    local decode_sum=0
    local total_sum=0
    
    for time in "${encode_times[@]}"; do
        encode_sum=$(echo "$encode_sum + $time" | bc -l)
    done
    
    for time in "${decode_times[@]}"; do
        decode_sum=$(echo "$decode_sum + $time" | bc -l)
    done
    
    for time in "${total_times[@]}"; do
        total_sum=$(echo "$total_sum + $time" | bc -l)
    done
    
    local encode_mean=$(echo "scale=6; $encode_sum / $runs" | bc -l)
    local decode_mean=$(echo "scale=6; $decode_sum / $runs" | bc -l)
    local total_mean=$(echo "scale=6; $total_sum / $runs" | bc -l)
    
    # Convert to milliseconds
    local encode_ms=$(echo "scale=2; $encode_mean * 1000" | bc -l)
    local decode_ms=$(echo "scale=2; $decode_mean * 1000" | bc -l)
    local total_ms=$(echo "scale=2; $total_mean * 1000" | bc -l)
    
    # Print results
    printf "%-15s | %-12s | %-8s | %4d | %11s | %11s | %10s\n" \
           "$impl_name" "$(echo "$message" | cut -c1-12)" "$(echo "$password" | cut -c1-8)" "$runs" "$encode_ms" "$decode_ms" "$total_ms"
}

# Get encode command for implementation
get_encode_cmd() {
    local impl=$1
    local message=$2
    local password=$3
    
    case $impl in
        rust)
            echo "${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs encode -m '$message' --cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'}"
            ;;
        go)
            echo "${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go encode -m '$message' -cf '$TEST_CARRIER_FILE' -o '$TEST_ENCODED_FILE' ${password:+-p '$password'}"
            ;;
        python-pure)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '${PROJECT_ROOT}/test_carrier.txt' -o '${PROJECT_ROOT}/test_encoded.txt' ${password:+-p '$password'}"
            ;;
        python-rust)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '${PROJECT_ROOT}/test_carrier.txt' -o '${PROJECT_ROOT}/test_encoded.txt' ${password:+-p '$password'}"
            ;;
        python-c)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" encode -m '$message' -cf '${PROJECT_ROOT}/test_carrier.txt' -o '${PROJECT_ROOT}/test_encoded.txt' ${password:+-p '$password'}"
            ;;
        *)
            echo "echo 'Unknown implementation: $impl'"
            ;;
    esac
}

# Get decode command for implementation
get_decode_cmd() {
    local impl=$1
    local password=$2
    
    case $impl in
        rust)
            echo "${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs decode --cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'}"
            ;;
        go)
            echo "${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go decode -cf '$TEST_ENCODED_FILE' -o '$TEST_DECODED_FILE' ${password:+-p '$password'}"
            ;;
        python-pure)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '${PROJECT_ROOT}/test_encoded.txt' -o '${PROJECT_ROOT}/test_decoded.txt' ${password:+-p '$password'}"
            ;;
        python-rust)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '${PROJECT_ROOT}/test_encoded.txt' -o '${PROJECT_ROOT}/test_decoded.txt' ${password:+-p '$password'}"
            ;;
        python-c)
            echo "cd ${PROJECT_ROOT}/implementations/python && python3 -c \"from whitespace_stego.cli import main; main()\" decode -cf '${PROJECT_ROOT}/test_encoded.txt' -o '${PROJECT_ROOT}/test_decoded.txt' ${password:+-p '$password'}"
            ;;
        *)
            echo "echo 'Unknown implementation: $impl'"
            ;;
    esac
}

# Main benchmarking function
run_benchmarks() {
    # Create results directory
    mkdir -p "$RESULTS_DIR"
    
    # Clear previous log
    > "$LOG_FILE"
    
    log "Starting simple benchmark comparison"
    log "Configuration: $RUNS runs"
    
    # Check available implementations
    local implementations=()
    
    # Rust implementation
    if check_implementation "whitespace-stego-rs" "${PROJECT_ROOT}/implementations/rust/target/release/whitespace-stego-rs"; then
        implementations+=("rust")
    fi
    
    # Go implementation
    if check_implementation "whitespace-stego-go" "${PROJECT_ROOT}/implementations/go/bin/whitespace-stego-go"; then
        implementations+=("go")
    fi
    
    # Python implementations
    if command -v python3 >/dev/null 2>&1; then
        implementations+=("python-pure")
        implementations+=("python-rust")
        implementations+=("python-c")
    fi
    
    log "Found implementations: ${implementations[*]}"
    
    # Create test files
    create_test_files
    
    # Print header
    echo
    echo "Benchmark Results"
    echo "================="
    echo
    printf "%-15s | %-12s | %-8s | %4s | %11s | %11s | %10s\n" \
           "Implementation" "Message" "Password" "Runs" "Encode (ms)" "Decode (ms)" "Total (ms)"
    echo "----------------|-------------|----------|------|-------------|-------------|------------"
    
    # Run benchmarks for each implementation and test case
    for impl in "${implementations[@]}"; do
        for message in "${TEST_MESSAGES[@]}"; do
            for password in "${TEST_PASSWORDS[@]}"; do
                # Get commands for this implementation
                local encode_cmd=$(get_encode_cmd "$impl" "$message" "$password")
                local decode_cmd=$(get_decode_cmd "$impl" "$password")
                
                # Run benchmark
                if benchmark_impl "$impl" "$encode_cmd" "$decode_cmd" "$message" "$password" $RUNS; then
                    log_success "$impl: Completed benchmark for '$message'"
                else
                    log_error "$impl: Failed benchmark for '$message'"
                fi
            done
        done
    done
    
    # Clean up test files
    cleanup_test_files
    
    log_success "Benchmark completed!"
    log "Log saved to: $LOG_FILE"
    
    echo
    echo "Benchmark completed successfully!"
    echo "Log file: $LOG_FILE"
}

# Help function
show_help() {
    cat << EOF
Simple Benchmark Implementation Comparison Script

Usage: $0 [runs] [verbose]

Arguments:
  runs     Number of benchmark runs (default: $DEFAULT_RUNS)
  verbose  Enable verbose output (true/false, default: false)

Examples:
  $0                    # Run with default settings
  $0 5                  # Run with 5 runs
  $0 3 true             # Run with 3 runs and verbose output

Output:
  - Console table with results
  - Log file: benchmark_simple.log

EOF
}

# Main execution
main() {
    case "${1:-}" in
        -h|--help)
            show_help
            exit 0
            ;;
    esac
    
    # Check dependencies
    if ! command -v bc >/dev/null 2>&1; then
        log_error "bc command not found. Please install bc package."
        exit 1
    fi
    
    if ! command -v date >/dev/null 2>&1; then
        log_error "date command not found."
        exit 1
    fi
    
    # Run benchmarks
    run_benchmarks
}

# Run main function
main "$@" 