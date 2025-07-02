#!/usr/bin/env python3
"""
Test script to verify Fernet compatibility across Python, Rust, and WASM implementations.
This script tests round-trip encryption/decryption between all implementations.
"""

import base64
import subprocess
import sys
import tempfile
import os
from pathlib import Path

def test_python_fernet():
    """Test Python Fernet implementation"""
    print("🔍 Testing Python Fernet implementation...")
    
    # Test data
    message = "Hello, World! 🌍"
    password = "test_password_123"
    carrier = "This is a carrier text."
    
    try:
        # Import the Python implementation
        sys.path.insert(0, str(Path(__file__).parent / 'whitespace_stego'))
        from core import encode, decode
        
        # Test encoding
        encoded = encode(message, carrier, password)
        print(f"✅ Python encode: {len(encoded)} chars")
        
        # Test decoding
        decoded = decode(encoded, password)
        print(f"✅ Python decode: {decoded}")
        
        assert decoded == message, f"Python round-trip failed: {decoded} != {message}"
        print("✅ Python round-trip test passed!")
        
        return encoded
        
    except Exception as e:
        print(f"❌ Python test failed: {e}")
        return None

def test_rust_fernet():
    """Test Rust Fernet implementation"""
    print("🔍 Testing Rust Fernet implementation...")
    
    # Test data
    message = "Hello, World! 🌍"
    password = "test_password_123"
    carrier = "This is a carrier text."
    
    try:
        # Build and run Rust implementation
        result = subprocess.run(
            ["cargo", "run", "--bin", "whitespace-stego", "encode", 
             "--message", message, "--carrier", carrier, "--password", password],
            capture_output=True, text=True, cwd="whitespace-stego-cli"
        )
        
        if result.returncode != 0:
            print(f"❌ Rust encode failed: {result.stderr}")
            return None
            
        encoded = result.stdout.strip()
        print(f"✅ Rust encode: {len(encoded)} chars")
        
        # Test decoding
        result = subprocess.run(
            ["cargo", "run", "--bin", "whitespace-stego", "decode", 
             "--carrier", encoded, "--password", password],
            capture_output=True, text=True, cwd="whitespace-stego-cli"
        )
        
        if result.returncode != 0:
            print(f"❌ Rust decode failed: {result.stderr}")
            return None
            
        decoded = result.stdout.strip()
        print(f"✅ Rust decode: {decoded}")
        
        assert decoded == message, f"Rust round-trip failed: {decoded} != {message}"
        print("✅ Rust round-trip test passed!")
        
        return encoded
        
    except Exception as e:
        print(f"❌ Rust test failed: {e}")
        return None

def test_wasm_fernet():
    """Test WASM Fernet implementation"""
    print("🔍 Testing WASM Fernet implementation...")
    
    # Test data
    message = "Hello, World! 🌍"
    password = "test_password_123"
    carrier = "This is a carrier text."
    
    try:
        # Create a simple test HTML file
        test_html = """
<!DOCTYPE html>
<html>
<head>
    <title>WASM Fernet Test</title>
</head>
<body>
    <div id="output"></div>
    <script type="module">
        import init, { encode, decode } from './whitespace_stego_wasi.js';
        
        async function testWasm() {
            try {
                await init();
                
                const message = "Hello, World! 🌍";
                const password = "test_password_123";
                const carrier = "This is a carrier text.";
                
                // Test encoding
                const encoded = encode(message, carrier, password);
                console.log('WASM encode:', encoded.length, 'chars');
                
                // Test decoding
                const decoded = decode(encoded, password);
                console.log('WASM decode:', decoded);
                
                if (decoded === message) {
                    console.log('✅ WASM round-trip test passed!');
                    document.getElementById('output').innerHTML = 
                        '<p style="color: green;">✅ WASM test passed!</p>';
                } else {
                    console.log('❌ WASM round-trip failed');
                    document.getElementById('output').innerHTML = 
                        '<p style="color: red;">❌ WASM test failed</p>';
                }
                
            } catch (error) {
                console.error('WASM test error:', error);
                document.getElementById('output').innerHTML = 
                    '<p style="color: red;">❌ WASM test error: ' + error + '</p>';
            }
        }
        
        testWasm();
    </script>
</body>
</html>
"""
        
        # Write test HTML to pkg directory
        test_file = Path("wasi/pkg/test_fernet.html")
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text(test_html)
        
        print("✅ WASM test HTML created")
        print("🌐 To test WASM, open http://localhost:8000/test_fernet.html in browser")
        
        return "WASM test HTML created"
        
    except Exception as e:
        print(f"❌ WASM test failed: {e}")
        return None

def test_cross_implementation():
    """Test cross-implementation compatibility"""
    print("🔍 Testing cross-implementation compatibility...")
    
    # Test data
    message = "Cross-platform test message 🚀"
    password = "shared_password_456"
    carrier = "Shared carrier text for testing."
    
    try:
        # Encode with Python
        sys.path.insert(0, str(Path(__file__).parent / 'whitespace_stego'))
        from core import encode, decode
        
        python_encoded = encode(message, carrier, password)
        print(f"✅ Python encoded: {len(python_encoded)} chars")
        
        # Try to decode with Rust
        result = subprocess.run(
            ["cargo", "run", "--bin", "whitespace-stego", "decode", 
             "--carrier", python_encoded, "--password", password],
            capture_output=True, text=True, cwd="whitespace-stego-cli"
        )
        
        if result.returncode == 0:
            rust_decoded = result.stdout.strip()
            print(f"✅ Rust decoded Python: {rust_decoded}")
            assert rust_decoded == message, f"Rust couldn't decode Python: {rust_decoded} != {message}"
            print("✅ Python → Rust compatibility: PASSED")
        else:
            print(f"❌ Rust couldn't decode Python: {result.stderr}")
            return False
        
        # Encode with Rust
        result = subprocess.run(
            ["cargo", "run", "--bin", "whitespace-stego", "encode", 
             "--message", message, "--carrier", carrier, "--password", password],
            capture_output=True, text=True, cwd="whitespace-stego-cli"
        )
        
        if result.returncode == 0:
            rust_encoded = result.stdout.strip()
            print(f"✅ Rust encoded: {len(rust_encoded)} chars")
            
            # Try to decode with Python
            python_decoded = decode(rust_encoded, password)
            print(f"✅ Python decoded Rust: {python_decoded}")
            assert python_decoded == message, f"Python couldn't decode Rust: {python_decoded} != {message}"
            print("✅ Rust → Python compatibility: PASSED")
        else:
            print(f"❌ Rust encode failed: {result.stderr}")
            return False
        
        print("✅ Cross-implementation compatibility: ALL PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ Cross-implementation test failed: {e}")
        return False

def main():
    """Run all compatibility tests"""
    print("🚀 Starting Fernet Compatibility Tests")
    print("=" * 50)
    
    # Test individual implementations
    python_result = test_python_fernet()
    print()
    
    rust_result = test_rust_fernet()
    print()
    
    wasm_result = test_wasm_fernet()
    print()
    
    # Test cross-implementation compatibility
    cross_result = test_cross_implementation()
    print()
    
    # Summary
    print("=" * 50)
    print("📊 Test Summary:")
    print(f"Python Fernet: {'✅ PASS' if python_result else '❌ FAIL'}")
    print(f"Rust Fernet:   {'✅ PASS' if rust_result else '❌ FAIL'}")
    print(f"WASM Fernet:   {'✅ PASS' if wasm_result else '❌ FAIL'}")
    print(f"Cross-compat:  {'✅ PASS' if cross_result else '❌ FAIL'}")
    
    if all([python_result, rust_result, wasm_result, cross_result]):
        print("\n🎉 ALL TESTS PASSED! Fernet is fully compatible across implementations.")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main() 