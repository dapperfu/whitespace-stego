#!/bin/bash
# Profile Rust implementation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT/rust"

echo "Profiling Rust implementation..."

# Build with debug symbols
cargo build --release

# Profile with perf (if available)
if command -v perf > /dev/null; then
    echo "Running perf profile..."
    perf record -g -- ./target/release/examples/cli encode "Test message for profiling" > /dev/null
    perf report
else
    echo "perf not available, skipping profiling"
fi

