#!/bin/bash
# Profile Python implementation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT/python"

echo "Profiling Python implementation..."

# Install if needed
pip install -e . > /dev/null 2>&1 || true

# Run with cProfile
python -m cProfile -o profile.stats -m whitespace_stego.cli encode "Test message for profiling" > /dev/null

echo "Profile data saved to python/profile.stats"
echo "View with: python -m pstats profile.stats"

