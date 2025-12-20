#!/bin/bash
# Profile C implementation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT/c"

echo "Profiling C implementation..."

# Build with profiling flags
make clean
make CFLAGS="-Wall -Wextra -std=c11 -O2 -pg" all

# Run with gprof
./tests/test_main
gprof ./tests/test_main gmon.out > profile.txt

echo "Profile data saved to c/profile.txt"

