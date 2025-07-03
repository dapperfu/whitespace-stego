#!/bin/bash

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

# Function to print colored output
print_status() {
    local status=$1
    local message=$2
    case $status in
        "PASS")
            echo -e "${GREEN}✅ PASS:${NC} $message"
            ;;
        "FAIL")
            echo -e "${RED}❌ FAIL:${NC} $message"
            ;;
        "INFO")
            echo -e "${BLUE}ℹ️  INFO:${NC} $message"
            ;;
        "WARN")
            echo -e "${YELLOW}⚠️  WARN:${NC} $message"
            ;;
    esac
}

# Function to run a test and track results
run_test() {
    local test_name=$1
    local test_command=$2
    
    print_status "INFO" "Running $test_name..."
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    
    if eval "$test_command" > /dev/null 2>&1; then
        print_status "PASS" "$test_name"
        PASSED_TESTS=$((PASSED_TESTS + 1))
        return 0
    else
        print_status "FAIL" "$test_name"
        FAILED_TESTS=$((FAILED_TESTS + 1))
        return 1
    fi
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install dependencies
install_dependencies() {
    print_status "INFO" "Checking dependencies..."
    
    # Check for gcc
    if ! command_exists gcc; then
        print_status "FAIL" "gcc not found. Please install gcc."
        exit 1
    fi
    
    # Check for make
    if ! command_exists make; then
        print_status "FAIL" "make not found. Please install make."
        exit 1
    fi
    
    # Check for OpenSSL
    if ! pkg-config --exists openssl; then
        print_status "WARN" "OpenSSL development headers not found. Some tests may fail."
    fi
    
    # Check for coverage tools
    if ! command_exists gcov; then
        print_status "WARN" "gcov not found. Coverage reports will not be generated."
    fi
    
    if ! command_exists lcov; then
        print_status "WARN" "lcov not found. HTML coverage reports will not be generated."
    fi
    
    print_status "INFO" "Dependencies check completed."
}

# Function to build the project
build_project() {
    print_status "INFO" "Building project..."
    
    if make clean && make all; then
        print_status "PASS" "Project built successfully"
        return 0
    else
        print_status "FAIL" "Project build failed"
        return 1
    fi
}

# Function to run basic tests
run_basic_tests() {
    print_status "INFO" "Running basic shell tests..."
    
    if ./test/run_tests.sh > /dev/null 2>&1; then
        print_status "PASS" "Basic shell tests"
        return 0
    else
        print_status "FAIL" "Basic shell tests"
        return 1
    fi
}

# Function to run C implementation tests
run_c_tests() {
    print_status "INFO" "Running C implementation tests..."
    
    if make test-c > /dev/null 2>&1; then
        print_status "PASS" "C implementation tests"
        return 0
    else
        print_status "FAIL" "C implementation tests"
        return 1
    fi
}

# Function to run Unity framework tests
run_unity_tests() {
    print_status "INFO" "Running Unity framework tests..."
    
    # Install Unity if not present
    if [ ! -f "test/unity.h" ]; then
        print_status "INFO" "Installing Unity test framework..."
        make install-unity > /dev/null 2>&1
    fi
    
    if make test-unity > /dev/null 2>&1; then
        print_status "PASS" "Unity framework tests"
        return 0
    else
        print_status "FAIL" "Unity framework tests"
        return 1
    fi
}

# Function to run coverage tests
run_coverage_tests() {
    print_status "INFO" "Running coverage tests..."
    
    if make test-coverage > /dev/null 2>&1; then
        print_status "PASS" "Coverage tests"
        return 0
    else
        print_status "FAIL" "Coverage tests"
        return 1
    fi
}

# Function to generate coverage report
generate_coverage_report() {
    if command_exists gcov && command_exists lcov; then
        print_status "INFO" "Generating coverage report..."
        
        if make coverage-report > /dev/null 2>&1; then
            print_status "PASS" "Coverage report generated"
            print_status "INFO" "Coverage report available at: coverage/html/index.html"
            return 0
        else
            print_status "FAIL" "Coverage report generation failed"
            return 1
        fi
    else
        print_status "WARN" "Skipping coverage report (gcov or lcov not available)"
        return 0
    fi
}

# Function to run memory leak tests
run_memory_tests() {
    print_status "INFO" "Running memory leak tests..."
    
    if command_exists valgrind; then
        # Run a simple test with valgrind
        if valgrind --leak-check=full --error-exitcode=1 ./bin/test-c > /dev/null 2>&1; then
            print_status "PASS" "Memory leak tests"
            return 0
        else
            print_status "FAIL" "Memory leak tests"
            return 1
        fi
    else
        print_status "WARN" "Skipping memory tests (valgrind not available)"
        return 0
    fi
}

# Function to run performance tests
run_performance_tests() {
    print_status "INFO" "Running performance tests..."
    
    # Simple performance test
    local start_time=$(date +%s.%N)
    for i in {1..100}; do
        echo "test message $i" | ./bin/whitespace-stego-c -e "performance test" > /dev/null 2>&1
    done
    local end_time=$(date +%s.%N)
    
    local duration=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0")
    
    if (( $(echo "$duration < 10" | bc -l 2>/dev/null || echo "1") )); then
        print_status "PASS" "Performance tests (${duration}s for 100 operations)"
        return 0
    else
        print_status "FAIL" "Performance tests (${duration}s for 100 operations - too slow)"
        return 1
    fi
}

# Function to print summary
print_summary() {
    echo
    echo "=========================================="
    echo "           TEST SUMMARY"
    echo "=========================================="
    echo "Total tests: $TOTAL_TESTS"
    echo -e "Passed: ${GREEN}$PASSED_TESTS${NC}"
    echo -e "Failed: ${RED}$FAILED_TESTS${NC}"
    
    if [ $FAILED_TESTS -eq 0 ]; then
        echo -e "${GREEN}🎉 All tests passed!${NC}"
        return 0
    else
        echo -e "${RED}❌ Some tests failed!${NC}"
        return 1
    fi
}

# Main execution
main() {
    echo "=========================================="
    echo "    C Testing Suite for Whitespace Stego"
    echo "=========================================="
    echo
    
    # Install dependencies
    install_dependencies
    
    # Build project
    if ! build_project; then
        exit 1
    fi
    
    # Run all test suites
    run_test "Basic Shell Tests" "run_basic_tests"
    run_test "C Implementation Tests" "run_c_tests"
    run_test "Unity Framework Tests" "run_unity_tests"
    run_test "Coverage Tests" "run_coverage_tests"
    run_test "Memory Leak Tests" "run_memory_tests"
    run_test "Performance Tests" "run_performance_tests"
    
    # Generate coverage report
    run_test "Coverage Report Generation" "generate_coverage_report"
    
    # Print summary
    print_summary
    
    exit $?
}

# Run main function
main "$@" 