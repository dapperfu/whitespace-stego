#!/usr/bin/env python3
"""
Comprehensive round-trip compatibility test between all implementations:
- C++ implementation
- Python implementation (core, Rust backend, C backend)
- C implementation
- Go implementation
"""

import subprocess
import sys
import os
import tempfile
import json
from typing import List, Dict, Tuple, Optional

# Add Python implementation to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'implementations', 'python'))

def run_command(cmd: List[str], input_data: Optional[str] = None) -> Tuple[int, str, str]:
    """Run a command and return (return_code, stdout, stderr)"""
    try:
        result = subprocess.run(
            cmd,
            input=input_data.encode() if input_data else None,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except Exception as e:
        return -1, "", str(e)

def create_temp_file(content: str, suffix: str = ".txt") -> str:
    """Create a temporary file with content and return the path"""
    fd, path = tempfile.mkstemp(suffix=suffix)
    with os.fdopen(fd, 'w') as f:
        f.write(content)
    return path

def cleanup_temp_file(path: str):
    """Clean up a temporary file"""
    try:
        os.unlink(path)
    except:
        pass

def test_cpp_encode_decode(message: str, carrier: str, password: str = "") -> Dict:
    """Test C++ implementation encode/decode round-trip"""
    print(f"  Testing C++ implementation...")
    
    # Create temporary files
    carrier_file = create_temp_file(carrier)
    output_file = create_temp_file("")
    decoded_file = create_temp_file("")
    
    try:
        # Encode with C++
        encode_cmd = [
            "./implementations/cpp/bin/whitespace-stego-cpp",
            "encode",
            "-m", message,
            "-cf", carrier_file,
            "-o", output_file
        ]
        if password:
            encode_cmd.extend(["-p", password])
        
        ret_code, stdout, stderr = run_command(encode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Encode failed: {stderr}"}
        
        # Read encoded output
        with open(output_file, 'r') as f:
            encoded = f.read()
        
        # Decode with C++
        decode_cmd = [
            "./implementations/cpp/bin/whitespace-stego-cpp",
            "decode",
            "-cf", output_file,
            "-o", decoded_file
        ]
        if password:
            decode_cmd.extend(["-p", password])
        
        ret_code, stdout, stderr = run_command(decode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Decode failed: {stderr}"}
        
        # Read decoded output
        with open(decoded_file, 'r') as f:
            decoded = f.read().strip()
        
        success = decoded == message
        return {
            "success": success,
            "encoded": encoded,
            "decoded": decoded,
            "expected": message
        }
        
    finally:
        cleanup_temp_file(carrier_file)
        cleanup_temp_file(output_file)
        cleanup_temp_file(decoded_file)

def test_c_encode_decode(message: str, carrier: str, password: str = "") -> Dict:
    """Test C implementation encode/decode round-trip"""
    print(f"  Testing C implementation...")
    
    # Create temporary files
    message_file = create_temp_file(message)
    carrier_file = create_temp_file(carrier)
    output_file = create_temp_file("")
    decoded_file = create_temp_file("")
    
    try:
        # Encode with C
        encode_cmd = [
            "./implementations/c/bin/whitespace-stego-c",
            "encode",
            "--message-file", message_file,
            "--carrier-file", carrier_file,
            "--output", output_file
        ]
        if password:
            encode_cmd.extend(["--password", password])
        
        ret_code, stdout, stderr = run_command(encode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Encode failed: {stderr}"}
        
        # Read encoded output
        with open(output_file, 'r') as f:
            encoded = f.read()
        
        # Decode with C
        decode_cmd = [
            "./implementations/c/bin/whitespace-stego-c",
            "decode",
            "--carrier-file", output_file,
            "--output", decoded_file
        ]
        if password:
            decode_cmd.extend(["--password", password])
        
        ret_code, stdout, stderr = run_command(decode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Decode failed: {stderr}"}
        
        # Read decoded output
        with open(decoded_file, 'r') as f:
            decoded = f.read().strip()
        
        success = decoded == message
        return {
            "success": success,
            "encoded": encoded,
            "decoded": decoded,
            "expected": message
        }
        
    finally:
        cleanup_temp_file(message_file)
        cleanup_temp_file(carrier_file)
        cleanup_temp_file(output_file)
        cleanup_temp_file(decoded_file)

def test_go_encode_decode(message: str, carrier: str, password: str = "") -> Dict:
    """Test Go implementation encode/decode round-trip"""
    print(f"  Testing Go implementation...")
    
    # Create temporary files
    carrier_file = create_temp_file(carrier)
    output_file = create_temp_file("")
    decoded_file = create_temp_file("")
    
    try:
        # Encode with Go
        encode_cmd = [
            "./implementations/go/bin/whitespace-stego-go",
            "encode",
            "-message", message,
            "-carrier-file", carrier_file,
            "-output", output_file
        ]
        if password:
            encode_cmd.extend(["-password", password])
        
        ret_code, stdout, stderr = run_command(encode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Encode failed: {stderr}"}
        
        # Read encoded output
        with open(output_file, 'r') as f:
            encoded = f.read()
        
        # Decode with Go
        decode_cmd = [
            "./implementations/go/bin/whitespace-stego-go",
            "decode",
            "-carrier-file", output_file,
            "-output", decoded_file
        ]
        if password:
            decode_cmd.extend(["-password", password])
        
        ret_code, stdout, stderr = run_command(decode_cmd)
        if ret_code != 0:
            return {"success": False, "error": f"Decode failed: {stderr}"}
        
        # Read decoded output
        with open(decoded_file, 'r') as f:
            decoded = f.read().strip()
        
        success = decoded == message
        return {
            "success": success,
            "encoded": encoded,
            "decoded": decoded,
            "expected": message
        }
        
    finally:
        cleanup_temp_file(carrier_file)
        cleanup_temp_file(output_file)
        cleanup_temp_file(decoded_file)

def test_python_encode_decode(message: str, carrier: str, password: str = "", backend: str = "core") -> Dict:
    """Test Python implementation encode/decode round-trip"""
    print(f"  Testing Python implementation ({backend} backend)...")
    
    # Create Python test script
    test_script = f"""
import sys
sys.path.insert(0, 'implementations/python')

try:
    import whitespace_stego
    
    # Test encoding
    if '{backend}' == 'rust' and whitespace_stego.rust_available:
        encoded = whitespace_stego.rust_encode('{message}', '{carrier}', '{password}')
    elif '{backend}' == 'c' and whitespace_stego.c_available:
        encoded = whitespace_stego.c_encode('{message}', '{carrier}', '{password}')
    else:
        encoded = whitespace_stego.encode('{message}', '{carrier}', '{password}')
    
    # Test decoding
    if '{backend}' == 'rust' and whitespace_stego.rust_available:
        decoded = whitespace_stego.rust_decode(encoded, '{password}')
    elif '{backend}' == 'c' and whitespace_stego.c_available:
        decoded = whitespace_stego.c_decode(encoded, '{password}')
    else:
        decoded = whitespace_stego.decode(encoded, '{password}')
    
    print(f"ENCODED:{{encoded}}")
    print(f"DECODED:{{decoded}}")
    print(f"SUCCESS:{{decoded == '{message}'}}")
    
except Exception as e:
    print(f"ERROR:{{str(e)}}")
    sys.exit(1)
"""
    
    ret_code, stdout, stderr = run_command(["python3", "-c", test_script])
    if ret_code != 0:
        return {"success": False, "error": f"Python test failed: {stderr}"}
    
    # Parse output
    lines = stdout.strip().split('\n')
    encoded = None
    decoded = None
    success = False
    
    for line in lines:
        if line.startswith("ENCODED:"):
            encoded = line[8:]
        elif line.startswith("DECODED:"):
            decoded = line[8:]
        elif line.startswith("SUCCESS:"):
            success = line[8:].lower() == "true"
    
    if encoded is None or decoded is None:
        return {"success": False, "error": "Could not parse Python output"}
    
    return {
        "success": success,
        "encoded": encoded,
        "decoded": decoded,
        "expected": message
    }

def test_cross_implementation_compatibility():
    """Test cross-implementation compatibility"""
    print("Testing cross-implementation compatibility...")
    
    test_cases = [
        {
            "name": "Simple ASCII",
            "message": "Hello, World!",
            "carrier": "This is a test carrier text.",
            "password": ""
        },
        {
            "name": "Unicode characters",
            "message": "Hello 世界! 🌍",
            "carrier": "This is a test carrier with unicode: 测试",
            "password": ""
        },
        {
            "name": "With password",
            "message": "Secret message",
            "carrier": "Public carrier text",
            "password": "mypassword123"
        },
        {
            "name": "Long message",
            "message": "A" * 100,
            "carrier": "B" * 50,
            "password": ""
        }
    ]
    
    implementations = [
        ("cpp", test_cpp_encode_decode),
        ("c", test_c_encode_decode),
        ("go", test_go_encode_decode),
        ("python_core", lambda m, c, p: test_python_encode_decode(m, c, p, "core")),
        ("python_rust", lambda m, c, p: test_python_encode_decode(m, c, p, "rust")),
        ("python_c", lambda m, c, p: test_python_encode_decode(m, c, p, "c"))
    ]
    
    results = {}
    
    for test_case in test_cases:
        print(f"\n=== Test Case: {test_case['name']} ===")
        results[test_case['name']] = {}
        
        for impl_name, test_func in implementations:
            print(f"Testing {impl_name}...")
            try:
                result = test_func(
                    test_case['message'],
                    test_case['carrier'],
                    test_case['password']
                )
                results[test_case['name']][impl_name] = result
                
                if result['success']:
                    print(f"  ✓ {impl_name}: PASS")
                else:
                    print(f"  ✗ {impl_name}: FAIL - {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"  ✗ {impl_name}: ERROR - {str(e)}")
                results[test_case['name']][impl_name] = {
                    "success": False,
                    "error": str(e)
                }
    
    return results

def test_cross_decode():
    """Test decoding with different implementations"""
    print("\n=== Testing Cross-Decode Compatibility ===")
    
    # Use a simple test case
    message = "Cross-decode test"
    carrier = "Carrier text"
    password = "testpass"
    
    # Encode with each implementation
    encoders = [
        ("cpp", lambda: test_cpp_encode_decode(message, carrier, password)),
        ("c", lambda: test_c_encode_decode(message, carrier, password)),
        ("go", lambda: test_go_encode_decode(message, carrier, password)),
        ("python_core", lambda: test_python_encode_decode(message, carrier, password, "core")),
        ("python_rust", lambda: test_python_encode_decode(message, carrier, password, "rust")),
        ("python_c", lambda: test_python_encode_decode(message, carrier, password, "c"))
    ]
    
    encoded_results = {}
    
    # Get encoded data from each implementation
    for encoder_name, encoder_func in encoders:
        print(f"Encoding with {encoder_name}...")
        result = encoder_func()
        if result['success']:
            encoded_results[encoder_name] = result['encoded']
            print(f"  ✓ {encoder_name} encoded successfully")
        else:
            print(f"  ✗ {encoder_name} failed to encode: {result.get('error', 'Unknown error')}")
    
    # Test decoding with each implementation
    decoders = [
        ("cpp", lambda encoded: test_cpp_encode_decode("dummy", encoded, password)),
        ("c", lambda encoded: test_c_encode_decode("dummy", encoded, password)),
        ("go", lambda encoded: test_go_encode_decode("dummy", encoded, password)),
        ("python_core", lambda encoded: test_python_encode_decode("dummy", encoded, password, "core")),
        ("python_rust", lambda encoded: test_python_encode_decode("dummy", encoded, password, "rust")),
        ("python_c", lambda encoded: test_python_encode_decode("dummy", encoded, password, "c"))
    ]
    
    cross_decode_results = {}
    
    for encoder_name, encoded_data in encoded_results.items():
        print(f"\nTesting decoding of {encoder_name} output...")
        cross_decode_results[encoder_name] = {}
        
        for decoder_name, decoder_func in decoders:
            print(f"  Decoding with {decoder_name}...")
            try:
                result = decoder_func(encoded_data)
                cross_decode_results[encoder_name][decoder_name] = result
                
                if result['success'] and result['decoded'] == message:
                    print(f"    ✓ {decoder_name}: PASS")
                else:
                    print(f"    ✗ {decoder_name}: FAIL - got '{result.get('decoded', 'None')}', expected '{message}'")
                    
            except Exception as e:
                print(f"    ✗ {decoder_name}: ERROR - {str(e)}")
                cross_decode_results[encoder_name][decoder_name] = {
                    "success": False,
                    "error": str(e)
                }
    
    return cross_decode_results

def main():
    """Main test function"""
    print("=== Whitespace Steganography Cross-Implementation Compatibility Test ===")
    
    # Test individual implementation round-trips
    round_trip_results = test_cross_implementation_compatibility()
    
    # Test cross-decode compatibility
    cross_decode_results = test_cross_decode()
    
    # Generate summary report
    print("\n" + "="*80)
    print("SUMMARY REPORT")
    print("="*80)
    
    # Round-trip summary
    print("\nROUND-TRIP COMPATIBILITY:")
    for test_name, impl_results in round_trip_results.items():
        print(f"\n{test_name}:")
        for impl_name, result in impl_results.items():
            status = "PASS" if result.get('success', False) else "FAIL"
            print(f"  {impl_name}: {status}")
    
    # Cross-decode summary
    print("\nCROSS-DECODE COMPATIBILITY:")
    for encoder_name, decoder_results in cross_decode_results.items():
        print(f"\n{encoder_name} encoded data:")
        for decoder_name, result in decoder_results.items():
            status = "PASS" if result.get('success', False) else "FAIL"
            print(f"  {decoder_name}: {status}")
    
    # Save detailed results
    with open("roundtrip_test_results_fixed.json", "w") as f:
        json.dump({
            "round_trip": round_trip_results,
            "cross_decode": cross_decode_results
        }, f, indent=2)
    
    print(f"\nDetailed results saved to: roundtrip_test_results_fixed.json")

if __name__ == "__main__":
    main() 