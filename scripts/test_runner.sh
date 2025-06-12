#!/bin/bash

# Test runner for all bash test scripts after building everything
set -e

# Build all implementations
make all-cli
make install

# Run all test*.sh scripts in the scripts directory
EXIT_CODE=0
for script in scripts/test*.sh; do
    echo "============================="
    echo "Running $script"
    echo "============================="
    bash "$script" || EXIT_CODE=$?
    echo
done

exit $EXIT_CODE 