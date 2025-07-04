#!/bin/bash

# Buffer Size Configuration Script
# Automatically detects the maximum working buffer size and generates headers

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/build"
CONFIG_DIR="${SCRIPT_DIR}/config"
INCLUDE_DIR="${SCRIPT_DIR}/include"

# Create directories
mkdir -p "${BUILD_DIR}" "${CONFIG_DIR}"

echo "=== Buffer Size Configuration ==="
echo "Detecting maximum working buffer size..."

# Test sizes to try (in bytes)
TEST_SIZES=(
    1024        # 1 KiB
    4096        # 4 KiB
    16384       # 16 KiB
    65536       # 64 KiB
    131072      # 128 KiB
    262144      # 256 KiB
    524288      # 512 KiB
    1048576     # 1 MiB
    2097152     # 2 MiB
    4194304     # 4 MiB
    8388608     # 8 MiB
    16777216    # 16 MiB
    33554432    # 32 MiB
    67108864    # 64 MiB
    134217728   # 128 MiB
    268435456   # 256 MiB
    536870912   # 512 MiB
    1073741824  # 1 GiB
    2147483648  # 2 GiB
    3221225472  # 3 GiB
    3758096384  # 3.5 GiB
    4026531840  # 3.75 GiB
    4194304000  # 3.9 GiB
    4294967295  # 4 GiB - 1 (max)
)

# Create test program
cat > "${BUILD_DIR}/test_buffer_size.c" << 'EOF'
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Buffer size to test (will be replaced by script)
#define TEST_BUFFER_SIZE BUFFER_SIZE_PLACEHOLDER

// Static buffer structure
typedef struct {
    char carrier[TEST_BUFFER_SIZE];
    char message[TEST_BUFFER_SIZE];
    char encoded[TEST_BUFFER_SIZE];
    char decoded[TEST_BUFFER_SIZE];
    char temp[TEST_BUFFER_SIZE];
    char base64[TEST_BUFFER_SIZE];
    unsigned char crypto_temp[TEST_BUFFER_SIZE];
    size_t buffer_size;
} test_buffers_t;

// Global buffer
static test_buffers_t global_buffers;

// Simple test functions
int test_init(void) {
    memset(&global_buffers, 0, sizeof(global_buffers));
    global_buffers.buffer_size = TEST_BUFFER_SIZE;
    return 1;
}

int test_encode(const char* message) {
    if (!message) return 0;
    
    // Simple test: just copy message to encoded
    strncpy(global_buffers.encoded, message, TEST_BUFFER_SIZE - 1);
    global_buffers.encoded[TEST_BUFFER_SIZE - 1] = '\0';
    return 1;
}

int test_decode(void) {
    // Simple test: just copy encoded to decoded
    strncpy(global_buffers.decoded, global_buffers.encoded, TEST_BUFFER_SIZE - 1);
    global_buffers.decoded[TEST_BUFFER_SIZE - 1] = '\0';
    return 1;
}

int main() {
    const char* test_message = "Test message";
    
    if (!test_init()) {
        return 1;
    }
    
    if (!test_encode(test_message)) {
        return 1;
    }
    
    if (!test_decode()) {
        return 1;
    }
    
    if (strcmp(global_buffers.decoded, test_message) != 0) {
        return 1;
    }
    
    return 0;
}
EOF

# Find maximum working buffer size
MAX_WORKING_SIZE=0

for size in "${TEST_SIZES[@]}"; do
    echo -n "Testing ${size} bytes ("
    if [ $size -ge 1073741824 ]; then
        echo -n "$(($size / 1073741824)) GiB)... "
    elif [ $size -ge 1048576 ]; then
        echo -n "$(($size / 1048576)) MiB)... "
    elif [ $size -ge 1024 ]; then
        echo -n "$(($size / 1024)) KiB)... "
    else
        echo -n "${size} bytes)... "
    fi
    
    # Create test file with current size
    sed "s/BUFFER_SIZE_PLACEHOLDER/${size}/g" "${BUILD_DIR}/test_buffer_size.c" > "${BUILD_DIR}/test_current.c"
    
    # Try to compile and run
    if gcc -o "${BUILD_DIR}/test_current" "${BUILD_DIR}/test_current.c" 2>/dev/null; then
        if "${BUILD_DIR}/test_current" 2>/dev/null; then
            echo "PASSED"
            MAX_WORKING_SIZE=$size
        else
            echo "FAILED (runtime)"
            break
        fi
    else
        echo "FAILED (compile)"
        break
    fi
done

echo
echo "=== Results ==="
if [ $MAX_WORKING_SIZE -gt 0 ]; then
    echo "✓ Maximum working buffer size: ${MAX_WORKING_SIZE} bytes"
    
    if [ $MAX_WORKING_SIZE -ge 1073741824 ]; then
        echo "✓ This is $(($MAX_WORKING_SIZE / 1073741824)) GiB"
    elif [ $MAX_WORKING_SIZE -ge 1048576 ]; then
        echo "✓ This is $(($MAX_WORKING_SIZE / 1048576)) MiB"
    elif [ $MAX_WORKING_SIZE -ge 1024 ]; then
        echo "✓ This is $(($MAX_WORKING_SIZE / 1024)) KiB"
    fi
    
    # Calculate recommended sizes
    TINY_SIZE=$((4 * 1024))           # 4 KiB
    SMALL_SIZE=$((1024 * 1024))       # 1 MiB
    STANDARD_SIZE=$((16 * 1024 * 1024))  # 16 MiB
    LARGE_SIZE=$MAX_WORKING_SIZE
    
    # Adjust if maximum is smaller than standard sizes
    if [ $LARGE_SIZE -lt $STANDARD_SIZE ]; then
        STANDARD_SIZE=$LARGE_SIZE
    fi
    if [ $LARGE_SIZE -lt $SMALL_SIZE ]; then
        SMALL_SIZE=$LARGE_SIZE
    fi
    if [ $LARGE_SIZE -lt $TINY_SIZE ]; then
        TINY_SIZE=$LARGE_SIZE
    fi
    
    echo
    echo "=== Recommended Buffer Sizes ==="
    echo "Tiny:     ${TINY_SIZE} bytes ($(($TINY_SIZE / 1024)) KiB)"
    echo "Small:    ${SMALL_SIZE} bytes ($(($SMALL_SIZE / 1024)) KiB)"
    echo "Standard: ${STANDARD_SIZE} bytes ($(($STANDARD_SIZE / 1024)) KiB)"
    echo "Large:    ${LARGE_SIZE} bytes ($(($LARGE_SIZE / 1024)) KiB)"
    
    # Generate configuration header
    cat > "${CONFIG_DIR}/buffer_sizes.h" << EOF
/*
 * Auto-generated buffer size configuration
 * Generated by configure_buffer_sizes.sh
 */

#ifndef BUFFER_SIZES_H
#define BUFFER_SIZES_H

// Maximum detected working buffer size
#define MAX_DETECTED_BUFFER_SIZE ${MAX_WORKING_SIZE}

// Recommended buffer sizes
#define TINY_BUFFER_SIZE ${TINY_SIZE}
#define SMALL_BUFFER_SIZE ${SMALL_SIZE}
#define STANDARD_BUFFER_SIZE ${STANDARD_SIZE}
#define LARGE_BUFFER_SIZE ${LARGE_SIZE}

// Buffer size validation
#define IS_VALID_BUFFER_SIZE(size) ((size) <= MAX_DETECTED_BUFFER_SIZE)

#endif // BUFFER_SIZES_H
EOF

    # Generate CMake configuration
    cat > "${CONFIG_DIR}/buffer_sizes.cmake" << EOF
# Auto-generated buffer size configuration for CMake
# Generated by configure_buffer_sizes.sh

set(MAX_DETECTED_BUFFER_SIZE ${MAX_WORKING_SIZE})
set(TINY_BUFFER_SIZE ${TINY_SIZE})
set(SMALL_BUFFER_SIZE ${SMALL_SIZE})
set(STANDARD_BUFFER_SIZE ${STANDARD_SIZE})
set(LARGE_BUFFER_SIZE ${LARGE_SIZE})

message(STATUS "Buffer sizes configured:")
message(STATUS "  Tiny:     ${TINY_SIZE} bytes ($(($TINY_SIZE / 1024)) KiB)")
message(STATUS "  Small:    ${SMALL_SIZE} bytes ($(($SMALL_SIZE / 1024)) KiB)")
message(STATUS "  Standard: ${STANDARD_SIZE} bytes ($(($STANDARD_SIZE / 1024)) KiB)")
message(STATUS "  Large:    ${LARGE_SIZE} bytes ($(($LARGE_SIZE / 1024)) KiB)")
message(STATUS "  Maximum:  ${MAX_WORKING_SIZE} bytes")
EOF

    echo
    echo "✓ Configuration files generated:"
    echo "  - ${CONFIG_DIR}/buffer_sizes.h"
    echo "  - ${CONFIG_DIR}/buffer_sizes.cmake"
    
else
    echo "✗ No working buffer sizes found"
    exit 1
fi

# Cleanup
rm -f "${BUILD_DIR}/test_buffer_size.c" "${BUILD_DIR}/test_current.c" "${BUILD_DIR}/test_current"

echo
echo "Configuration complete!" 