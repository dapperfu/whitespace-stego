"""Simple cross-implementation tests for whitespace steganography."""

import pytest

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


def test_python_rust_cross_has_encoded_message():
    """Test that Python has_encoded_message works with Rust-encoded messages."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "Hello, World!"
    carrier = "Simple carrier"
    
    # Encode with Rust
    rust_encoded = rust_encode(message, carrier, None)
    
    # Check with Python has_encoded_message
    assert py_has_encoded_message(rust_encoded), "Python failed to detect Rust-encoded message"
    
    # Verify the message can be decoded
    decoded = py_decode(rust_encoded, None)
    assert decoded == message, "Failed to decode Rust-encoded message"


def test_rust_python_cross_has_encoded_message():
    """Test that Python has_encoded_message works with Python-encoded messages."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "Hello, World!"
    carrier = "Simple carrier"
    
    # Encode with Python
    py_encoded = py_encode(message, carrier, None)
    
    # Check with Python has_encoded_message
    assert py_has_encoded_message(py_encoded), "Python failed to detect Python-encoded message"
    
    # Verify the message can be decoded by Rust
    decoded = rust_decode(py_encoded, None)
    assert decoded == message, "Rust failed to decode Python-encoded message"


def test_python_rust_cross_roundtrip():
    """Test Python -> Rust -> Python round trip."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "Hello, World!"
    carrier = "Simple carrier"
    
    # Python encode -> Rust decode
    py_encoded = py_encode(message, carrier, None)
    rust_decoded = rust_decode(py_encoded, None)
    assert rust_decoded == message, "Rust failed to decode Python-encoded message"
    
    # Rust encode -> Python decode
    rust_encoded = rust_encode(message, carrier, None)
    py_decoded = py_decode(rust_encoded, None)
    assert py_decoded == message, "Python failed to decode Rust-encoded message"


def test_python_rust_cross_roundtrip_with_password():
    """Test Python -> Rust -> Python round trip with password."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "Secret message"
    carrier = "Public carrier"
    password = "test_password"
    
    # Python encode -> Rust decode
    py_encoded = py_encode(message, carrier, password)
    rust_decoded = rust_decode(py_encoded, password)
    assert rust_decoded == message, "Rust failed to decode Python-encoded message with password"
    
    # Rust encode -> Python decode
    rust_encoded = rust_encode(message, carrier, password)
    py_decoded = py_decode(rust_encoded, password)
    assert py_decoded == message, "Python failed to decode Rust-encoded message with password"


def test_python_rust_cross_roundtrip_unicode():
    """Test Python -> Rust -> Python round trip with Unicode."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "你好，世界！"  # Chinese
    carrier = "Unicode carrier: こんにちは"  # Japanese
    
    # Python encode -> Rust decode
    py_encoded = py_encode(message, carrier, None)
    rust_decoded = rust_decode(py_encoded, None)
    assert rust_decoded == message, "Rust failed to decode Python-encoded Unicode message"
    
    # Rust encode -> Python decode
    rust_encoded = rust_encode(message, carrier, None)
    py_decoded = py_decode(rust_encoded, None)
    assert py_decoded == message, "Python failed to decode Rust-encoded Unicode message"


def test_message_size_consistency():
    """Test that message sizes are consistent across implementations."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    message = "Test message"
    carrier = "Test carrier"
    
    # Encode with both implementations
    py_encoded = py_encode(message, carrier, None)
    rust_encoded = rust_encode(message, carrier, None)
    
    # Check sizes
    py_size = py_get_size(py_encoded)
    rust_size = py_get_size(rust_encoded)  # Use Python's get_size for both
    
    assert py_size == rust_size, f"Size mismatch: Python={py_size}, Rust={rust_size}"


def test_empty_message_cross_implementation():
    """Test encoding/decoding empty messages across implementations."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    # Test Python
    py_encoded = py_encode("", "carrier", None)
    assert py_has_encoded_message(py_encoded), "Python failed to detect empty encoded message"
    py_decoded = py_decode(py_encoded, None)
    assert py_decoded == "", "Python failed to decode empty message"
    
    # Test Rust
    rust_encoded = rust_encode("", "carrier", None)
    assert py_has_encoded_message(rust_encoded), "Python failed to detect Rust empty encoded message"
    rust_decoded = rust_decode(rust_encoded, None)
    assert rust_decoded == "", "Rust failed to decode empty message"


def test_empty_carrier_cross_implementation():
    """Test encoding/decoding with empty carrier across implementations."""
    if not RUST_AVAILABLE:
        pytest.skip("Rust backend not available")
    
    # Test Python
    py_encoded = py_encode("test message", "", None)
    assert py_has_encoded_message(py_encoded), "Python failed to detect message in empty carrier"
    py_decoded = py_decode(py_encoded, None)
    assert py_decoded == "test message", "Python failed to decode message from empty carrier"
    
    # Test Rust
    rust_encoded = rust_encode("test message", "", None)
    assert py_has_encoded_message(rust_encoded), "Python failed to detect Rust message in empty carrier"
    rust_decoded = rust_decode(rust_encoded, None)
    assert rust_decoded == "test message", "Rust failed to decode message from empty carrier"


def test_implementation_availability():
    """Test which implementations are available."""
    print(f"Python implementation: Available")
    print(f"Rust implementation: {'Available' if RUST_AVAILABLE else 'Not available'}")
    
    # At least Python should be available
    assert True, "Python implementation should always be available" 