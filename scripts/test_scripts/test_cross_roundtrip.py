#!/usr/bin/env python3
"""
Cross-round-trip compatibility test script.

This script tests that messages encoded by one binary can be decoded by another binary.
"""

import os
import subprocess
import sys
import json
import tempfile
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Test configuration
BIN_DIR = Path("bin")
TEST_RESULTS_DIR = Path("test_results")
TEST_RESULTS_DIR.mkdir(exist_ok=True)

# Test messages and carriers
TEST_CASES = [
    {
        "name": "simple_ascii",
        "message": "Hello, World!",
        "carrier": "This is a simple test message.",
        "password": None
    },
    {
        "name": "unicode_emoji",
        "message": "Hello 🌍 World! 你好世界!",
        "carrier": "This is a test with emojis 🚀 and unicode 测试.",
        "password": None
    },
    {
        "name": "password_protected",
        "message": "Secret message with password protection",
        "carrier": "This carrier text contains a hidden secret.",
        "password": "mysecretpassword123"
    },
    {
        "name": "empty_carrier",
        "message": "Message in empty carrier",
        "carrier": "",
        "password": None
    },
    {
        "name": "long_message",
        "message": "This is a longer message that tests the ability to handle larger amounts of data. It contains multiple sentences and should be properly encoded and decoded across all implementations.",
        "carrier": "A longer carrier text that provides more space for embedding messages. This helps test the robustness of the steganography implementation.",
        "password": None
    }
]

# Binary configurations
BINARY_CONFIGS = {
    "whitespace-stego-py": {
        "encode_cmd": lambda msg, carrier, pwd: [
            "encode", 
            "-m", msg, 
            "-c", carrier,
            *(["-p", pwd] if pwd else [])
        ],
        "decode_cmd": lambda carrier, pwd: [
            "decode", 
            "-c", carrier,
            *(["-p", pwd] if pwd else [])
        ],
        "description": "Python standalone CLI"
    },
    "whitespace-stego-rs": {
        "encode_cmd": lambda msg, carrier, pwd: [
            "encode", 
            "-m", msg, 
            "-c", carrier,
            *(["-p", pwd] if pwd else [])
        ],
        "decode_cmd": lambda carrier, pwd: [
            "decode", 
            "-c", carrier,
            *(["-p", pwd] if pwd else [])
        ],
        "description": "Rust standalone CLI"
    },
    "whitespace-stego-c": {
        "encode_cmd": lambda msg, carrier, pwd: [
            "encode", 
            "--message", msg, 
            "--carrier", carrier,
            *(["--password", pwd] if pwd else [])
        ],
        "decode_cmd": lambda carrier, pwd: [
            "decode", 
            "--carrier", carrier,
            *(["--password", pwd] if pwd else [])
        ],
        "description": "C standalone CLI"
    },
    "whitespace-stego-go": {
        "encode_cmd": lambda msg, carrier, pwd: [
            "encode", 
            "-m", msg, 
            "-cf", "carrier.txt",
            *(["-p", pwd] if pwd else [])
        ],
        "decode_cmd": lambda carrier, pwd: [
            "decode", 
            "-cf", "carrier.txt",
            *(["-p", pwd] if pwd else [])
        ],
        "description": "Go standalone CLI"
    }
}

def run_command(binary_path: Path, args: List[str], input_text: str = None, timeout: int = 30) -> Dict:
    """Run a command and return results."""
    try:
        if input_text:
            result = subprocess.run(
                [str(binary_path)] + args,
                input=input_text,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=Path.cwd()
            )
        else:
            result = subprocess.run(
                [str(binary_path)] + args,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=Path.cwd()
            )
        
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Command timed out after {timeout} seconds",
            "returncode": -1
        }
    except FileNotFoundError:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Binary not found: {binary_path}",
            "returncode": -1
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Error running command: {e}",
            "returncode": -1
        }

def encode_message(binary_name: str, binary_path: Path, message: str, carrier: str, password: Optional[str]) -> Dict:
    """Encode a message using a specific binary."""
    config = BINARY_CONFIGS[binary_name]
    args = config["encode_cmd"](message, carrier, password)
    
    # Handle Go binary which needs carrier file
    if binary_name == "whitespace-stego-go":
        with open("carrier.txt", "w", encoding="utf-8") as f:
            f.write(carrier)
    
    result = run_command(binary_path, args)
    
    # Clean up carrier file for Go
    if binary_name == "whitespace-stego-go" and Path("carrier.txt").exists():
        Path("carrier.txt").unlink()
    
    return result

def decode_message(binary_name: str, binary_path: Path, encoded_carrier: str, password: Optional[str]) -> Dict:
    """Decode a message using a specific binary."""
    config = BINARY_CONFIGS[binary_name]
    args = config["decode_cmd"](encoded_carrier, password)
    
    # Handle Go binary which needs carrier file
    if binary_name == "whitespace-stego-go":
        with open("carrier.txt", "w", encoding="utf-8") as f:
            f.write(encoded_carrier)
    
    result = run_command(binary_path, args)
    
    # Clean up carrier file for Go
    if binary_name == "whitespace-stego-go" and Path("carrier.txt").exists():
        Path("carrier.txt").unlink()
    
    return result

def test_cross_roundtrip(encode_binary: str, decode_binary: str, test_case: Dict) -> Dict:
    """Test cross-round-trip between two binaries."""
    encode_path = BIN_DIR / encode_binary
    decode_path = BIN_DIR / decode_binary
    
    if not encode_path.exists() or not decode_path.exists():
        return {
            "success": False,
            "error": f"Binary not found: {encode_binary} or {decode_binary}",
            "encode_result": None,
            "decode_result": None,
            "roundtrip_success": False
        }
    
    print(f"  🔄 {encode_binary} → {decode_binary}")
    
    # Encode
    encode_result = encode_message(
        encode_binary, 
        encode_path, 
        test_case["message"], 
        test_case["carrier"], 
        test_case["password"]
    )
    
    if not encode_result["success"]:
        return {
            "success": False,
            "error": f"Encode failed: {encode_result['stderr']}",
            "encode_result": encode_result,
            "decode_result": None,
            "roundtrip_success": False
        }
    
    # Decode
    decode_result = decode_message(
        decode_binary, 
        decode_path, 
        encode_result["stdout"], 
        test_case["password"]
    )
    
    if not decode_result["success"]:
        return {
            "success": False,
            "error": f"Decode failed: {decode_result['stderr']}",
            "encode_result": encode_result,
            "decode_result": decode_result,
            "roundtrip_success": False
        }
    
    # Check if decoded message matches original
    decoded_message = decode_result["stdout"]
    original_message = test_case["message"]
    
    roundtrip_success = decoded_message == original_message
    
    if roundtrip_success:
        print(f"    ✅ Roundtrip successful")
    else:
        print(f"    ❌ Roundtrip failed: expected '{original_message}', got '{decoded_message}'")
    
    return {
        "success": True,
        "error": None,
        "encode_result": encode_result,
        "decode_result": decode_result,
        "roundtrip_success": roundtrip_success,
        "original_message": original_message,
        "decoded_message": decoded_message
    }

def main():
    """Main test function."""
    print("🔄 Starting cross-round-trip compatibility tests...")
    print(f"📁 Binary directory: {BIN_DIR.absolute()}")
    
    if not BIN_DIR.exists():
        print(f"❌ Binary directory not found: {BIN_DIR}")
        sys.exit(1)
    
    # Get available binaries
    available_binaries = []
    for binary_name in BINARY_CONFIGS.keys():
        binary_path = BIN_DIR / binary_name
        if binary_path.exists() and os.access(binary_path, os.X_OK):
            available_binaries.append(binary_name)
    
    print(f"📦 Available binaries: {available_binaries}")
    
    if len(available_binaries) < 2:
        print("❌ Need at least 2 binaries for cross-round-trip testing")
        sys.exit(1)
    
    # Run tests
    all_results = {}
    total_tests = 0
    passed_tests = 0
    
    for test_case in TEST_CASES:
        print(f"\n🧪 Testing: {test_case['name']}")
        print(f"  Message: {repr(test_case['message'])}")
        print(f"  Carrier: {repr(test_case['carrier'])}")
        if test_case['password']:
            print(f"  Password: {test_case['password']}")
        
        test_results = {}
        
        # Test all combinations of encode/decode
        for encode_binary in available_binaries:
            for decode_binary in available_binaries:
                test_key = f"{encode_binary}→{decode_binary}"
                result = test_cross_roundtrip(encode_binary, decode_binary, test_case)
                test_results[test_key] = result
                
                total_tests += 1
                if result["success"] and result["roundtrip_success"]:
                    passed_tests += 1
        
        all_results[test_case["name"]] = test_results
    
    # Summary
    print(f"\n📊 Cross-Roundtrip Test Summary:")
    print(f"  Test cases: {len(TEST_CASES)}")
    print(f"  Available binaries: {len(available_binaries)}")
    print(f"  Total roundtrip tests: {total_tests}")
    print(f"  Passed roundtrip tests: {passed_tests}")
    print(f"  Success rate: {passed_tests/total_tests*100:.1f}%" if total_tests > 0 else "N/A")
    
    # Detailed results by test case
    for test_case_name, results in all_results.items():
        passed = sum(1 for r in results.values() if r["success"] and r["roundtrip_success"])
        total = len(results)
        print(f"  {test_case_name}: {passed}/{total} passed ({passed/total*100:.1f}%)")
    
    # Save results
    results_file = TEST_RESULTS_DIR / "cross_roundtrip_tests.json"
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"💾 Results saved to: {results_file}")
    
    # Exit with error if any critical tests failed
    if passed_tests < total_tests:
        print("❌ Some cross-round-trip tests failed!")
        sys.exit(1)
    else:
        print("✅ All cross-round-trip tests passed!")

if __name__ == "__main__":
    main() 