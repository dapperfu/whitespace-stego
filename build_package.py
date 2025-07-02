#!/usr/bin/env python3
"""
Build script for whitespace-stego package.

This script ensures that the C shared library is built before creating the Python package.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {cmd}")
        print(f"   Error: {e.stderr}")
        return False

def check_c_library():
    """Check if the C shared library exists."""
    lib_path = Path("c/lib/libwhitespace_stego.so")
    return lib_path.exists()

def build_c_library():
    """Build the C shared library."""
    if not run_command("cd c && make shared", "Building C shared library"):
        return False
    
    if not check_c_library():
        print("❌ C shared library was not created")
        return False
    
    print("✅ C shared library built successfully")
    return True

def build_rust_backend():
    """Build the Rust backend."""
    if not run_command("cd whitespace-stego-backend && maturin build --release", "Building Rust backend"):
        return False
    
    # Check if the Rust extension was built
    rust_ext_path = Path("whitespace-stego-backend/whitespace_stego_backend/whitespace_stego_backend.cpython-*-linux-gnu.so")
    if not list(rust_ext_path.parent.glob("*.so")):
        print("❌ Rust backend was not created")
        return False
    
    print("✅ Rust backend built successfully")
    return True

def build_python_package():
    """Build the Python package."""
    if not run_command("python -m build", "Building Python package"):
        return False
    
    print("✅ Python package built successfully")
    return True

def main():
    """Main build process."""
    print("🚀 Starting whitespace-stego package build...")
    print()
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Build C library if needed
    if not check_c_library():
        print("📦 C shared library not found, building...")
        if not build_c_library():
            print("❌ Failed to build C library")
            sys.exit(1)
    else:
        print("✅ C shared library already exists")
    
    # Build Rust backend if needed
    rust_ext_path = Path("whitespace-stego-backend/whitespace_stego_backend/whitespace_stego_backend.cpython-*-linux-gnu.so")
    if not list(rust_ext_path.parent.glob("*.so")):
        print("📦 Rust backend not found, building...")
        if not build_rust_backend():
            print("❌ Failed to build Rust backend")
            sys.exit(1)
    else:
        print("✅ Rust backend already exists")
    
    # Build Python package
    if not build_python_package():
        print("❌ Failed to build Python package")
        sys.exit(1)
    
    print()
    print("🎉 Package build completed successfully!")
    print("📦 Package files are in the dist/ directory")
    print()
    print("To install the package:")
    print("  pip install dist/whitespace_stego-*.whl")
    print()
    print("To upload to PyPI:")
    print("  python -m twine upload dist/*")

if __name__ == "__main__":
    main() 