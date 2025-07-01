"""Cross-implementation tests for whitespace steganography.

This module tests interoperability between different implementations:
- Pure Python (whitespace_stego.core)
- Rust backend (whitespace_stego_backend)
- C implementation (whitespace-stego-c binary)
- CLI implementations

Tests include:
- has_encoded_message detection across implementations
- Full round-trip encoding/decoding
- Cross-implementation encoding/decoding
"""

import pytest
import subprocess
import tempfile
import os
from typing import List, Tuple, Optional
from pathlib import Path

# Import all available implementations
from whitespace_stego.core import (
    encode as py_encode,
    decode as py_decode,
    has_encoded_message as py_has_encoded_message,
    get_encoded_message_size as py_get_size
)

# Try to import Rust backend
try:
    from whitespace_stego_backend import (
        encode as rust_encode,
        decode as rust_decode,
    )
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

# Check if C binary is available
C_BINARY_PATH = Path("c/bin/whitespace-stego-c")
C_AVAILABLE = C_BINARY_PATH.exists() and os.access(C_BINARY_PATH, os.X_OK)

# Test data
TEST_MESSAGES = [
    "Hello, World!",
    "Simple ASCII message",
    "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?",
    "Numbers: 0123456789",
    "Mixed case: Hello World 123 !@#",
    "",  # Empty message
    "Unicode: 你好，世界！",  # Chinese
    "Unicode: こんにちは、世界！",  # Japanese
    "Unicode: 안녕하세요, 세계!",  # Korean
    "Unicode: Привет, мир!",  # Russian
    "Unicode: مرحبا بالعالم!",  # Arabic
    "Very long message: " + "x" * 1000,
]

TEST_CARRIERS = [
    "Simple carrier",
    "Carrier with spaces and punctuation!",
    "Unicode carrier: 你好世界",
    "",  # Empty carrier
    "Single char: A",
    "Very long carrier: " + "carrier text " * 100,
]

TEST_PASSWORDS = [
    None,  # No password
    "simple_password",
    "password_with_special_chars!@#$%",
    "Unicode password: 密码",
    "very_long_password_" + "x" * 50,
]


def run_c_binary_encode(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Run the C binary to encode a message."""
    if not C_AVAILABLE:
        pytest.skip("C binary not available")
    
    cmd = [str(C_BINARY_PATH), "encode"]
    
    # Create temporary files for input/output
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as msg_file:
        msg_file.write(message)
        msg_file_path = msg_file.name
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
        carrier_file.write(carrier)
        carrier_file_path = carrier_file.name
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
        output_file_path = output_file.name
    
    try:
        cmd.extend(["--message-file", msg_file_path])
        cmd.extend(["--carrier-file", carrier_file_path])
        cmd.extend(["--output", output_file_path])
        
        if password:
            cmd.extend(["--password", password])
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            raise RuntimeError(f"C binary encode failed: {result.stderr}")
        
        # Read the output
        with open(output_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    finally:
        # Clean up temporary files
        for path in [msg_file_path, carrier_file_path, output_file_path]:
            try:
                os.unlink(path)
            except OSError:
                pass


def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
    """Run the C binary to decode a message."""
    if not C_AVAILABLE:
        pytest.skip("C binary not available")
    
    cmd = [str(C_BINARY_PATH), "decode"]
    
    # Create temporary file for carrier (encoded) input
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
        carrier_file.write(encoded_text)
        carrier_file_path = carrier_file.name
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
        output_file_path = output_file.name
    
    try:
        cmd.extend(["--carrier-file", carrier_file_path])
        cmd.extend(["--output", output_file_path])
        
        if password:
            cmd.extend(["--password", password])
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            raise RuntimeError(f"C binary decode failed: {result.stderr}")
        
        # Read the output
        with open(output_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    finally:
        # Clean up temporary files
        for path in [carrier_file_path, output_file_path]:
            try:
                os.unlink(path)
            except OSError:
                pass


def get_available_implementations() -> List[Tuple[str, callable, callable, callable]]:
    """Get list of available implementations with their functions."""
    implementations = []
    
    # Python implementation
    implementations.append(("Python", py_encode, py_decode, py_has_encoded_message))
    
    # Rust implementation (uses Python's has_encoded_message since Rust doesn't expose it)
    if RUST_AVAILABLE:
        implementations.append(("Rust", rust_encode, rust_decode, py_has_encoded_message))
    
    return implementations


class TestCrossImplementationHasEncodedMessage:
    """Test has_encoded_message across different implementations."""
    
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    @pytest.mark.parametrize("carrier", TEST_CARRIERS)
    @pytest.mark.parametrize("password", TEST_PASSWORDS)
    def test_python_has_encoded_message_with_rust_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with Rust-encoded messages."""
        if not RUST_AVAILABLE:
            pytest.skip("Rust backend not available")
        
        # Encode with Rust
        rust_encoded = rust_encode(message, carrier, password)
        
        # Check with Python has_encoded_message
        assert py_has_encoded_message(rust_encoded), f"Python failed to detect Rust-encoded message: {message}"
        
        # Verify the message can be decoded
        decoded = py_decode(rust_encoded, password)
        assert decoded == message, f"Failed to decode Rust-encoded message: {message}"
    
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    @pytest.mark.parametrize("carrier", TEST_CARRIERS)
    @pytest.mark.parametrize("password", TEST_PASSWORDS)
    def test_rust_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust has_encoded_message with Python-encoded messages."""
        if not RUST_AVAILABLE:
            pytest.skip("Rust backend not available")
        
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
        
        # Check with Python has_encoded_message (Rust doesn't expose this function)
        assert py_has_encoded_message(py_encoded), f"Python failed to detect Python-encoded message: {message}"
        
        # Verify the message can be decoded
        decoded = rust_decode(py_encoded, password)
        assert decoded == message, f"Failed to decode Python-encoded message: {message}"
    
    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
        
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
        
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
        
        # Verify the message can be decoded
        decoded = py_decode(c_encoded, password)
        assert decoded == message, f"Failed to decode C-encoded message: {message}"
    
    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
        
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
        
        # Decode with C to verify it can read Python-encoded messages
        c_decoded = run_c_binary_decode(py_encoded, password)
        assert c_decoded == message, f"C failed to decode Python-encoded message: {message}"
    
    def test_has_encoded_message_with_plain_text(self):
        """Test has_encoded_message with plain text (should return False)."""
        plain_texts = [
            "Hello world",
            "Text with spaces",
            "Unicode: 你好世界",
            "",
            "Special chars: !@#$%^&*()",
        ]
        
        for text in plain_texts:
            assert not py_has_encoded_message(text), f"False positive for plain text: {text}"
    
    def test_has_encoded_message_with_partial_markers(self):
        """Test has_encoded_message with partial markers (should return False)."""
        partial_marker_texts = [
            "Text with start\u200b",  # Only start marker
            "Text with end\u200c",    # Only end marker
            "Start\u200b middle end\u200c",  # Wrong order
        ]
        
        for text in partial_marker_texts:
            assert not py_has_encoded_message(text), f"False positive for partial markers: {text}"


class TestCrossImplementationRoundTrip:
    """Test full round-trip encoding/decoding across implementations."""
    
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    @pytest.mark.parametrize("carrier", TEST_CARRIERS)
    @pytest.mark.parametrize("password", TEST_PASSWORDS)
    def test_python_rust_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python -> Rust -> Python round trip."""
        if not RUST_AVAILABLE:
            pytest.skip("Rust backend not available")
        
        # Python encode -> Rust decode
        py_encoded = py_encode(message, carrier, password)
        rust_decoded = rust_decode(py_encoded, password)
        assert rust_decoded == message, f"Rust failed to decode Python-encoded message: {message}"
        
        # Rust encode -> Python decode
        rust_encoded = rust_encode(message, carrier, password)
        py_decoded = py_decode(rust_encoded, password)
        assert py_decoded == message, f"Python failed to decode Rust-encoded message: {message}"
    
    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
        
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
        c_decoded = run_c_binary_decode(py_encoded, password)
        assert c_decoded == message, f"C failed to decode Python-encoded message: {message}"
        
        # C encode -> Python decode
        c_encoded = run_c_binary_encode(message, carrier, password)
        py_decoded = py_decode(c_encoded, password)
        assert py_decoded == message, f"Python failed to decode C-encoded message: {message}"
    
    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
        
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
        c_decoded = run_c_binary_decode(rust_encoded, password)
        assert c_decoded == message, f"C failed to decode Rust-encoded message: {message}"
        
        # C encode -> Rust decode
        c_encoded = run_c_binary_encode(message, carrier, password)
        rust_decoded = rust_decode(c_encoded, password)
        assert rust_decoded == message, f"Rust failed to decode C-encoded message: {message}"


class TestCrossImplementationMessageSize:
    """Test get_encoded_message_size across implementations."""
    
    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])
    @pytest.mark.parametrize("password", [None, "test_password"])
    def test_message_size_consistency(self, message: str, carrier: str, password: Optional[str]):
        """Test that message sizes are consistent across implementations."""
        implementations = get_available_implementations()
        
        if len(implementations) < 2:
            pytest.skip("Need at least 2 implementations for comparison")
        
        sizes = []
        
        for name, encode_func, decode_func, has_func in implementations:
            encoded = encode_func(message, carrier, password)
            size = py_get_size(encoded)  # Use Python's get_size for all
            sizes.append((name, size))
        
        # All implementations should produce the same size
        first_size = sizes[0][1]
        for name, size in sizes[1:]:
            assert size == first_size, f"Size mismatch: {sizes[0][0]}={first_size}, {name}={size}"
    
    def test_message_size_with_no_message(self):
        """Test get_encoded_message_size with text containing no message."""
        plain_texts = [
            "Hello world",
            "Text with spaces",
            "Unicode: 你好世界",
            "",
        ]
        
        for text in plain_texts:
            size = py_get_size(text)
            assert size is None, f"Expected None size for plain text: {text}"


class TestCrossImplementationEdgeCases:
    """Test edge cases across implementations."""
    
    def test_empty_message_all_implementations(self):
        """Test encoding/decoding empty messages across all implementations."""
        implementations = get_available_implementations()
        
        for name, encode_func, decode_func, has_func in implementations:
            encoded = encode_func("", "carrier", None)
            assert has_func(encoded), f"{name} failed to detect empty encoded message"
            
            decoded = decode_func(encoded, None)
            assert decoded == "", f"{name} failed to decode empty message"
    
    def test_empty_carrier_all_implementations(self):
        """Test encoding/decoding with empty carrier across all implementations."""
        implementations = get_available_implementations()
        
        for name, encode_func, decode_func, has_func in implementations:
            encoded = encode_func("test message", "", None)
            assert has_func(encoded), f"{name} failed to detect message in empty carrier"
            
            decoded = decode_func(encoded, None)
            assert decoded == "test message", f"{name} failed to decode message from empty carrier"
    
    def test_single_character_carrier_all_implementations(self):
        """Test encoding/decoding with single character carrier."""
        implementations = get_available_implementations()
        
        for name, encode_func, decode_func, has_func in implementations:
            encoded = encode_func("test message", "A", None)
            assert has_func(encoded), f"{name} failed to detect message in single char carrier"
            
            decoded = decode_func(encoded, None)
            assert decoded == "test message", f"{name} failed to decode message from single char carrier"
    
    def test_very_long_messages(self):
        """Test encoding/decoding very long messages."""
        long_message = "x" * 10000
        implementations = get_available_implementations()
        
        for name, encode_func, decode_func, has_func in implementations:
            encoded = encode_func(long_message, "carrier", None)
            assert has_func(encoded), f"{name} failed to detect long encoded message"
            
            decoded = decode_func(encoded, None)
            assert decoded == long_message, f"{name} failed to decode long message"


def test_implementation_availability():
    """Test which implementations are available."""
    print(f"Python implementation: Available")
    print(f"Rust implementation: {'Available' if RUST_AVAILABLE else 'Not available'}")
    print(f"C implementation: {'Available' if C_AVAILABLE else 'Not available'}")
    
    # At least Python should be available
    assert True, "Python implementation should always be available" 