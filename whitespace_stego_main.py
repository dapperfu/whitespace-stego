#!/usr/bin/env python3
"""
Standalone entry point for whitespace-stego CLI.
This script is used by PyInstaller to create a standalone binary.
"""

import sys
from whitespace_stego.cli import main

if __name__ == "__main__":
    main() 