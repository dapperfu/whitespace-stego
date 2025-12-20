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
    # Create/use virtual environment per cursor rules: venv_$(basename $(pwd))
    VENV_NAME="venv_whitespace-stego"
    VENV_PATH="$PROJECT_ROOT/$VENV_NAME"
    PYTHON_CMD=$(command -v python3 || command -v python)
    
    # Create venv if it doesn't exist
    if [ ! -d "$VENV_PATH" ]; then
        echo "  Creating virtual environment: $VENV_NAME"
        if ! $PYTHON_CMD -m venv "$VENV_PATH" 2>/dev/null; then
            echo "  Failed to create virtual environment, skipping Python tests"
            echo ""
        fi
    fi
    
    # Use venv python and pip if venv exists
    if [ -d "$VENV_PATH" ]; then
        VENV_PYTHON="$VENV_PATH/bin/python"
        VENV_PIP="$VENV_PATH/bin/pip"
        VENV_PYTEST="$VENV_PATH/bin/pytest"
        
        # Install package and dev dependencies in venv
        cd "$PROJECT_ROOT/python"
        if [ -f "pyproject.toml" ]; then
            $VENV_PIP install -e ".[dev]" > /dev/null 2>&1 || true
        elif [ -f "setup.py" ]; then
            $VENV_PIP install -e ".[dev]" > /dev/null 2>&1 || true
        fi
        
        # Ensure docs directory exists for HTML output
        mkdir -p "$PROJECT_ROOT/docs"
        
        # Run pytest from venv (configuration in pyproject.toml will handle HTML output)
        if [ -f "$VENV_PYTEST" ]; then
            $VENV_PYTEST tests/ -v || echo "Python tests failed"
        else
            echo "  pytest not found in virtual environment, skipping Python tests"
        fi
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

