#!/bin/bash
# CI/CD build script
# Runs build, test, and verification for CI environments

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

echo "=== CI Build Process ==="
echo ""

echo "Step 1: Building all implementations..."
make build-all

echo ""
echo "Step 2: Verifying all builds..."
make verify-all

echo ""
echo "Step 3: Running tests..."
make test-all

echo ""
echo "✓ CI build completed successfully!"

