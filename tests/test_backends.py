"""Parameterized tests for both Python and Rust backends."""

import pytest
from typing import Callable, Optional, Tuple

from whitespace_stego.core import decode as py_decode, encode as py_encode
from whitespace_stego.rust_bridge import decode as rs_decode, encode as rs_encode

# Unicode characters used for encoding
WORD_JOINER = "\u2060"
FUNCTION_APPLICATION = "\u2061"

# Define backend types
Backend = Tuple[Callable[[str, str, Optional[str]], str], Callable[[str, Optional[str]], str]]

# Test cases
TEST_CASES = [
    # (message, carrier, password)
    ("Hello, World!", "Public text", None),
    ("Secret message", "Normal text", "password123"),
    ("Special chars: !@#$%^&*()", "Carrier text", "special@pass"),
    ("Unicode: 你好世界 🌍", "English text", "unicode_pass"),
    ("", "Empty message", None),
    ("Long message " * 100, "Long carrier " * 10, "long_pass"),
]

@pytest.fixture(params=["python", "rust"])
def backend(request: pytest.FixtureRequest) -> Backend:
    """Fixture that provides encode/decode functions for the requested backend.
    
    Args:
        request: The pytest request object
        
    Returns:
        A tuple of (encode_fn, decode_fn) for the requested backend
        
    Raises:
        ImportError: If the Rust backend is requested but not available
    """
    if request.param == "python":
        return (py_encode, py_decode)
    elif request.param == "rust":
        try:
            return (rs_encode, rs_decode)
        except ImportError as e:
            pytest.skip(f"Rust backend not available: {e}")
    else:
        raise ValueError(f"Unknown backend: {request.param}")

@pytest.fixture(params=TEST_CASES)
def test_case(request: pytest.FixtureRequest) -> Tuple[str, str, Optional[str]]:
    """Fixture that provides test cases.
    
    Args:
        request: The pytest request object
        
    Returns:
        A tuple of (message, carrier, password)
    """
    return request.param

def test_encode_decode_roundtrip(backend: Backend, test_case: Tuple[str, str, Optional[str]]) -> None:
    """Test that encoding and decoding with the same backend works.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
        test_case: Tuple of (message, carrier, password)
    """
    message, carrier, password = test_case
    encode_fn, decode_fn = backend
    encoded = encode_fn(message, carrier, password)
    decoded = decode_fn(encoded, password)
    assert decoded == message

def test_encode_decode_cross_backend(
    backend: Backend,
    test_case: Tuple[str, str, Optional[str]]
) -> None:
    """Test that encoding with one backend and decoding with another works.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
        test_case: Tuple of (message, carrier, password)
    """
    message, carrier, password = test_case
    encode_fn, _ = backend
    other_encode_fn, other_decode_fn = (py_encode, py_decode) if encode_fn == rs_encode else (rs_encode, rs_decode)
    
    # Skip if Rust backend is not available
    if encode_fn == rs_encode:
        try:
            rs_encode("test", "test", None)
        except ImportError:
            pytest.skip("Rust backend not available")
    
    encoded = encode_fn(message, carrier, password)
    decoded = other_decode_fn(encoded, password)
    assert decoded == message

def test_invalid_carrier(backend: Backend) -> None:
    """Test that invalid carriers raise appropriate errors.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
    """
    _, decode_fn = backend
    with pytest.raises(ValueError, match="No valid message found"):
        decode_fn("Invalid carrier text", None)

def test_password_mismatch(backend: Backend) -> None:
    """Test that using wrong password raises appropriate errors.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
    """
    encode_fn, decode_fn = backend
    message = "Secret message"
    carrier = "Public text"
    password = "correct_password"
    wrong_password = "wrong_password"
    
    encoded = encode_fn(message, carrier, password)
    with pytest.raises(ValueError):
        decode_fn(encoded, wrong_password)

def test_empty_carrier(backend: Backend) -> None:
    """Test encoding/decoding with empty carrier.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
    """
    encode_fn, decode_fn = backend
    message = "Test message"
    carrier = ""
    password = "test_password"
    
    encoded = encode_fn(message, carrier, password)
    decoded = decode_fn(encoded, password)
    assert decoded == message
    assert encoded.startswith(WORD_JOINER) and encoded.endswith(FUNCTION_APPLICATION)

def test_single_char_carrier(backend: Backend) -> None:
    """Test encoding/decoding with single character carrier.
    
    Args:
        backend: Tuple of (encode_fn, decode_fn)
    """
    encode_fn, decode_fn = backend
    message = "Test message"
    carrier = "A"
    password = "test_password"
    
    encoded = encode_fn(message, carrier, password)
    decoded = decode_fn(encoded, password)
    assert decoded == message
    assert encoded.startswith("A" + WORD_JOINER) and encoded.endswith(FUNCTION_APPLICATION) 