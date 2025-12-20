#!/bin/bash
# Periodic build verification script
# Tests that all implementations build successfully

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Running build verification for all implementations..."
echo ""

cd "$PROJECT_ROOT"

# Run unified Makefile verification
make verify-all

echo ""
echo "✓ All build verifications completed successfully!"

