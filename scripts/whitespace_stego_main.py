#!/usr/bin/env python3
"""
Standalone entry point for whitespace-stego CLI.
This script is used by PyInstaller to create a standalone binary.
"""

import sys

# Explicitly import all backends to ensure PyInstaller includes them
try:
    import whitespace_stego_rust
except ImportError:
    pass  # Rust backend not available

try:
    import whitespace_stego.c_backend
except ImportError:
    pass  # C backend not available

from whitespace_stego.cli import main

if __name__ == "__main__":
    main() 