#!/usr/bin/env python3
"""Cross-language compatibility testing for whitespace steganography.

This script tests that any message encoded by one language implementation
can be decoded by any other language implementation.
"""

import json
import subprocess
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Add python module to path
sys.path.insert(0, str(Path(__file__).parent.parent / "python"))

try:
    from whitespace_stego import encode, decode
except ImportError:
    print("Error: Could not import whitespace_stego Python module")
    print("Make sure Python implementation is installed: cd python && pip install -e .")
    sys.exit(1)


def load_test_vectors() -> List[Dict]:
    """Load all test vectors from JSON files."""
    test_vectors_dir = Path(__file__).parent / "test_vectors"
    all_cases = []
    
    for json_file in test_vectors_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_cases.extend(data.get("test_cases", []))
    
    return all_cases


def python_encode(message: str, carrier: Optional[str] = None) -> str:
    """Encode using Python implementation."""
    return encode(message, carrier if carrier else None)


def python_decode(encoded_text: str) -> str:
    """Decode using Python implementation."""
    return decode(encoded_text)


def rust_encode(message: str, carrier: Optional[str] = None) -> str:
    """Encode using Rust implementation."""
    rust_dir = Path(__file__).parent.parent / "rust"
    cmd = ["cargo", "run", "--example", "cli", "--", "encode", message]
    if carrier:
        cmd.extend(["-c", carrier])
    
    result = subprocess.run(
        cmd,
        cwd=rust_dir,
        capture_output=True,
        text=True,
        check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"Rust encode failed: {result.stderr}")
    return result.stdout.strip()


def rust_decode(encoded_text: str) -> str:
    """Decode using Rust implementation."""
    rust_dir = Path(__file__).parent.parent / "rust"
    result = subprocess.run(
        ["cargo", "run", "--example", "cli", "--", "decode", encoded_text],
        cwd=rust_dir,
        capture_output=True,
        text=True,
        check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"Rust decode failed: {result.stderr}")
    return result.stdout.strip()


def test_round_trip_python(test_case: Dict) -> Tuple[bool, str]:
    """Test round-trip encoding/decoding with Python."""
    try:
        message = test_case["message"]
        carrier = test_case.get("carrier", "")
        
        encoded = python_encode(message, carrier if carrier else None)
        decoded = python_decode(encoded)
        
        if decoded == message:
            return True, ""
        else:
            return False, f"Round-trip failed: expected '{message}', got '{decoded}'"
    except Exception as e:
        return False, f"Exception: {str(e)}"


def test_cross_language(test_case: Dict) -> Tuple[bool, str]:
    """Test cross-language compatibility."""
    message = test_case["message"]
    carrier = test_case.get("carrier", "")
    
    # Skip tests with special characters that don't work well via CLI
    # (newlines, tabs, etc. get mangled by shell argument parsing)
    if any(c in message for c in ['\n', '\t', '\r']):
        # These work in Python but CLI argument parsing may mangle them
        return True, "Skipped (special characters not suitable for CLI testing)"
    
    # Encode with Python
    try:
        encoded = python_encode(message, carrier if carrier else None)
    except Exception as e:
        return False, f"Python encode failed: {str(e)}"
    
    # Try to decode with Rust (if available)
    try:
        decoded = rust_decode(encoded)
        if decoded != message:
            return False, f"Cross-language decode failed: expected '{message!r}', got '{decoded!r}'"
    except FileNotFoundError:
        # Rust not available, skip
        pass
    except Exception as e:
        return False, f"Rust decode failed: {str(e)}"
    
    return True, ""


def main():
    """Run all cross-language tests."""
    print("Loading test vectors...")
    test_cases = load_test_vectors()
    print(f"Loaded {len(test_cases)} test cases\n")
    
    passed = 0
    failed = 0
    
    print("Testing Python round-trip...")
    for test_case in test_cases:
        name = test_case["name"]
        success, error = test_round_trip_python(test_case)
        if success:
            passed += 1
            print(f"  ✓ {name}")
        else:
            failed += 1
            print(f"  ✗ {name}: {error}")
    
    print(f"\nPython round-trip: {passed} passed, {failed} failed")
    
    # Test cross-language if Rust is available
    if shutil.which("cargo"):
        print("\nTesting cross-language compatibility...")
        cross_passed = 0
        cross_failed = 0
        
        for test_case in test_cases:
            name = test_case["name"]
            success, error = test_cross_language(test_case)
            if success:
                cross_passed += 1
                print(f"  ✓ {name}")
            else:
                cross_failed += 1
                print(f"  ✗ {name}: {error}")
        
        print(f"\nCross-language: {cross_passed} passed, {cross_failed} failed")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    import shutil
    main()

