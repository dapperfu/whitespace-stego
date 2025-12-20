#!/bin/bash
# Test runner script for all language implementations

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Running whitespace-stego tests..."
echo ""

# Python tests
if [ -d "$PROJECT_ROOT/python" ]; then
    echo "Testing Python implementation..."
    cd "$PROJECT_ROOT/python"
    if [ -f "setup.py" ]; then
        pip install -e . > /dev/null 2>&1 || true
    fi
    if python -m pytest --version > /dev/null 2>&1; then
        python -m pytest tests/ -v || echo "Python tests failed"
    else
        echo "  pytest not available, skipping Python tests"
    fi
    echo ""
fi

# Rust tests
if [ -d "$PROJECT_ROOT/rust" ] && command -v cargo > /dev/null; then
    echo "Testing Rust implementation..."
    cd "$PROJECT_ROOT/rust"
    cargo test --lib --test integration_test || echo "Rust tests failed"
    echo ""
fi

# Go tests
if [ -d "$PROJECT_ROOT/go" ] && command -v go > /dev/null; then
    echo "Testing Go implementation..."
    cd "$PROJECT_ROOT/go"
    go test ./... || echo "Go tests failed"
    echo ""
fi

# C tests
if [ -d "$PROJECT_ROOT/c" ] && command -v make > /dev/null; then
    echo "Testing C implementation..."
    cd "$PROJECT_ROOT/c"
    make test || echo "C tests failed"
    echo ""
fi

# C++ tests
if [ -d "$PROJECT_ROOT/cpp" ] && command -v cmake > /dev/null; then
    echo "Testing C++ implementation..."
    cd "$PROJECT_ROOT/cpp"
    mkdir -p build
    cd build
    cmake .. && cmake --build . && ctest || echo "C++ tests failed"
    echo ""
fi

# Cross-language tests
if [ -f "$SCRIPT_DIR/cross_lang_test.py" ]; then
    echo "Running cross-language compatibility tests..."
    cd "$PROJECT_ROOT"
    python3 "$SCRIPT_DIR/cross_lang_test.py" || echo "Cross-language tests failed"
    echo ""
fi

echo "All tests completed!"

