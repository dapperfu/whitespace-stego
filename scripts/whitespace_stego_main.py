#!/usr/bin/env python3
"""Main entry point for whitespace steganography CLI."""

import sys
import os

# Add the implementations/python directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementations', 'python'))

from whitespace_stego.cli import main

if __name__ == "__main__":
    main() 