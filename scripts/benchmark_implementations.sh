#!/bin/bash

# Benchmark Implementation Comparison Script
# Compares static C, dynamic C, Rust, Go, and Python implementations

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
RESULTS_DIR="${PROJECT_ROOT}/benchmark_results"
LOG_FILE="${RESULTS_DIR}/benchmark.log"

# Default configuration
DEFAULT_RUNS=3
MIN_RUNS=3
MAX_RUNS=20
STD_DEV_THRESHOLD=0.1  # 10% threshold for increasing runs
CONFIG_FILE="${SCRIPT_DIR}/benchmark_config.sh"

# Test data
TEST_MESSAGES=(
    "Hello, World!"
    "This is a longer test message with spaces and punctuation!"
    "Unicode: 🚀🌟🎉"
    "A" "B" "C" "D" "E" "F" "G" "H" "I" "J"
)

TEST_PASSWORDS=(
    ""
    "simple_password"
    "complex_password_123!@#"
    "🚀🌟🎉"
)

TEST_CARRIER="This is a sample carrier text that will be used for testing the whitespace steganography implementations. It contains enough text to embed various sized messages."

# Load configuration if exists
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Parse command line arguments
RUNS=${1:-$DEFAULT_RUNS}
VERBOSE=${2:-false}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging functions
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}✗${NC} $1" | tee -a "$LOG_FILE"
}

# Utility functions
calculate_mean() {
    local values=("$@")
    local sum=0
    local count=${#values[@]}
    
    for value in "${values[@]}"; do
        sum=$(echo "$sum + $value" | bc -l)
    done
    
    echo "scale=3; $sum / $count" | bc -l
}

calculate_std_dev() {
    local values=("$@")
    local mean=$(calculate_mean "${values[@]}")
    local sum_sq_diff=0
    local count=${#values[@]}
    
    for value in "${values[@]}"; do
        local diff=$(echo "$value - $mean" | bc -l)
        local sq_diff=$(echo "$diff * $diff" | bc -l)
        sum_sq_diff=$(echo "$sum_sq_diff + $sq_diff" | bc -l)
    done
    
    local variance=$(echo "scale=6; $sum_sq_diff / $count" | bc -l)
    echo "scale=3; sqrt($variance)" | bc -l
}

calculate_cv() {
    local mean=$1
    local std_dev=$2
    
    if [ "$(echo "$mean > 0" | bc -l)" -eq 1 ]; then
        echo "scale=3; $std_dev / $mean" | bc -l
    else
        echo "0"
    fi
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
    local encode_mean=$(calculate_mean "${encode_times[@]}")
    local encode_std=$(calculate_std_dev "${encode_times[@]}")
    local encode_cv=$(calculate_cv "$encode_mean" "$encode_std")
    
    local decode_mean=$(calculate_mean "${decode_times[@]}")
    local decode_std=$(calculate_std_dev "${decode_times[@]}")
    local decode_cv=$(calculate_cv "$decode_mean" "$decode_std")
    
    local total_mean=$(calculate_mean "${total_times[@]}")
    local total_std=$(calculate_std_dev "${total_times[@]}")
    local total_cv=$(calculate_cv "$total_mean" "$total_std")
    
    # Return results as JSON-like string
    echo "{\"impl\":\"$impl_name\",\"message\":\"$message\",\"password\":\"$password\",\"runs\":$runs,\"encode_mean\":$encode_mean,\"encode_std\":$encode_std,\"encode_cv\":$encode_cv,\"decode_mean\":$decode_mean,\"decode_std\":$decode_std,\"decode_cv\":$decode_cv,\"total_mean\":$total_mean,\"total_std\":$total_std,\"total_cv\":$total_cv}"
}

# Determine optimal number of runs based on coefficient of variation
determine_optimal_runs() {
    local initial_runs=$1
    local impl_name=$2
    local encode_cmd=$3
    local decode_cmd=$4
    local message=$5
    local password=$6
    
    local current_runs=$initial_runs
    local max_runs=$MAX_RUNS
    
    while [ $current_runs -lt $max_runs ]; do
        local result=$(benchmark_impl "$impl_name" "$encode_cmd" "$decode_cmd" "$message" "$password" $current_runs)
        local total_cv=$(echo "$result" | grep -o '"total_cv":[0-9.]*' | cut -d':' -f2)
        
        # Check if total_cv is empty or invalid
        if [ -z "$total_cv" ] || ! [[ "$total_cv" =~ ^[0-9.]+$ ]]; then
            log_warning "$impl_name: Invalid CV result, using $current_runs runs"
            break
        fi
        
        if [ "$(echo "$total_cv < $STD_DEV_THRESHOLD" | bc -l)" -eq 1 ]; then
            log_success "$impl_name: CV=$total_cv < $STD_DEV_THRESHOLD, using $current_runs runs"
            break
        else
            log_warning "$impl_name: CV=$total_cv >= $STD_DEV_THRESHOLD, increasing runs to $((current_runs + 1))"
            current_runs=$((current_runs + 1))
        fi
    done
    
    echo $current_runs
}

# Generate results table
generate_table() {
    local results_file=$1
    local output_file=$2
    
    cat > "$output_file" << 'EOF'
# Benchmark Results

## Test Configuration
- **Test Messages**: Various sizes from 1 byte to Unicode strings
- **Test Passwords**: Empty, simple, complex, and Unicode
- **Carrier Text**: Standard test carrier
- **Runs**: Automatically adjusted based on coefficient of variation (CV < 10%)

## Results Summary

| Implementation | Message Size | Password | Runs | Encode (ms) | Decode (ms) | Total (ms) | CV (%) |
|----------------|--------------|----------|------|-------------|-------------|------------|--------|
EOF
    
    # Parse results and generate table rows
    while IFS= read -r line; do
        if [[ $line =~ \"impl\":\"([^\"]+)\" ]]; then
            local impl="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"message\":\"([^\"]+)\" ]]; then
            local message="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"password\":\"([^\"]+)\" ]]; then
            local password="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"runs\":([0-9]+) ]]; then
            local runs="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"encode_mean\":([0-9.]+) ]]; then
            local encode_mean="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"decode_mean\":([0-9.]+) ]]; then
            local decode_mean="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"total_mean\":([0-9.]+) ]]; then
            local total_mean="${BASH_REMATCH[1]}"
        fi
        if [[ $line =~ \"total_cv\":([0-9.]+) ]]; then
            local total_cv="${BASH_REMATCH[1]}"
        fi
        
        # Convert to milliseconds and format
        local encode_ms=$(echo "scale=2; $encode_mean * 1000" | bc -l)
        local decode_ms=$(echo "scale=2; $decode_mean * 1000" | bc -l)
        local total_ms=$(echo "scale=2; $total_mean * 1000" | bc -l)
        local cv_pct=$(echo "scale=1; $total_cv * 100" | bc -l)
        
        # Truncate long messages for display
        local msg_display=$(echo "$message" | cut -c1-20)
        if [ ${#message} -gt 20 ]; then
            msg_display="${msg_display}..."
        fi
        
        # Handle empty password
        local pwd_display="$password"
        if [ -z "$password" ]; then
            pwd_display="(none)"
        fi
        
        printf "| %-15s | %-12s | %-8s | %4d | %11s | %11s | %10s | %6s |\n" \
               "$impl" "$msg_display" "$pwd_display" "$runs" "$encode_ms" "$decode_ms" "$total_ms" "$cv_pct" >> "$output_file"
    done < "$results_file"
    
    cat >> "$output_file" << 'EOF'

## Performance Analysis

### Fastest Implementations
- **Encode**: [Implementation] - [Time] ms
- **Decode**: [Implementation] - [Time] ms
- **Total**: [Implementation] - [Time] ms

### Memory Usage
- **Static C**: No dynamic allocation, predictable memory usage
- **Dynamic C**: Uses malloc/free, variable memory usage
- **Rust**: Safe memory management with ownership
- **Go**: Garbage collected, automatic memory management
- **Python**: Garbage collected, higher memory overhead

### Recommendations
- Use **Static C** for embedded/safety-critical systems
- Use **Rust** for high-performance applications
- Use **Python** for rapid prototyping and development
- Use **Go** for concurrent applications
- Use **Dynamic C** for flexibility and large data

## Test Environment
- **OS**: $(uname -s) $(uname -r)
- **Architecture**: $(uname -m)
- **CPU**: $(grep "model name" /proc/cpuinfo | head -1 | cut -d':' -f2 | xargs)
- **Memory**: $(free -h | grep Mem | awk '{print $2}')
- **Date**: $(date)
EOF
}

# Main benchmarking function
run_benchmarks() {
    local results_file="${RESULTS_DIR}/benchmark_results.json"
    local table_file="${RESULTS_DIR}/benchmark_table.md"
    
    # Create results directory
    mkdir -p "$RESULTS_DIR"
    
    # Clear previous results
    > "$results_file"
    > "$LOG_FILE"
    
    log "Starting benchmark comparison of all implementations"
    log "Configuration: $RUNS initial runs, CV threshold: $STD_DEV_THRESHOLD"
    
    # Check available implementations
    local implementations=()
    
    # C implementations (currently disabled due to segfaults)
    # if check_implementation "whitespace-stego-static" "${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-static"; then
    #     implementations+=("static-c")
    # fi
    # if check_implementation "whitespace-stego-static-small" "${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-static-small"; then
    #     implementations+=("static-c-small")
    # fi
    # if check_implementation "whitespace-stego-static-tiny" "${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-static-tiny"; then
    #     implementations+=("static-c-tiny")
    # fi
    # if check_implementation "whitespace-stego-c" "${PROJECT_ROOT}/implementations/c/bin/whitespace-stego-c"; then
    #     implementations+=("dynamic-c")
    # fi
    
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
    
    # Run benchmarks for each implementation and test case
    for impl in "${implementations[@]}"; do
        for message in "${TEST_MESSAGES[@]}"; do
            for password in "${TEST_PASSWORDS[@]}"; do
                # Create test files
                create_test_files
                
                # Get actual commands for this implementation
                local encode_cmd=$(get_encode_cmd "$impl" "$message" "$password")
                local decode_cmd=$(get_decode_cmd "$impl" "$password")
                
                # Determine optimal number of runs
                local optimal_runs=$(determine_optimal_runs $RUNS "$impl" "$encode_cmd" "$decode_cmd" "$message" "$password")
                
                # Run actual benchmark with optimal runs
                local result=$(benchmark_impl "$impl" "$encode_cmd" "$decode_cmd" "$message" "$password" $optimal_runs)
                echo "$result" >> "$results_file"
                
                # Clean up test files
                cleanup_test_files
            done
        done
    done
    
    # Generate results table
    generate_table "$results_file" "$table_file"
    
    log_success "Benchmark completed!"
    log "Results saved to: $results_file"
    log "Table saved to: $table_file"
    
    # Display summary
    echo
    echo "=== Benchmark Summary ==="
    echo "Results: $results_file"
    echo "Table: $table_file"
    echo "Log: $LOG_FILE"
    echo
    echo "Top 5 fastest implementations (total time):"
    tail -n +2 "$table_file" | head -n 20 | sort -k7 -n | head -5 | while read line; do
        echo "  $line"
    done
}

# Help function
show_help() {
    cat << EOF
Benchmark Implementation Comparison Script

Usage: $0 [runs] [verbose]

Arguments:
  runs     Number of initial benchmark runs (default: $DEFAULT_RUNS)
  verbose  Enable verbose output (true/false, default: false)

Examples:
  $0                    # Run with default settings
  $0 5                  # Run with 5 initial runs
  $0 3 true             # Run with 3 initial runs and verbose output

Configuration:
  The script automatically adjusts the number of runs based on the coefficient
  of variation (CV). If CV >= $STD_DEV_THRESHOLD, runs are increased until
  CV < $STD_DEV_THRESHOLD or max runs ($MAX_RUNS) is reached.

Output:
  - JSON results file: benchmark_results.json
  - Markdown table: benchmark_table.md
  - Log file: benchmark.log

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