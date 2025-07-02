"""
Test 00: Parametrized Core (Python), Rust PyO3 Backend, and C Backend

This test suite runs all encode/decode tests against the Python, Rust, and C backends.
"""

import pytest
import sys
from typing import List, Optional

# Import Python backend
import whitespace_stego.core as pycore

# Import Rust backend
try:
    import whitespace_stego_rust as rustcore
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False
    rustcore = None

# Try to import C backend
try:
    import whitespace_stego.c_backend as ccore
    C_AVAILABLE = ccore.is_available()
except ImportError:
    C_AVAILABLE = False
    ccore = None

# Build backends list
BACKENDS = [
    ("python", pycore.encode, pycore.decode),
]

if RUST_AVAILABLE:
    BACKENDS.append(("rust", rustcore.encode, rustcore.decode))

if C_AVAILABLE:
    BACKENDS.append(("c", ccore.encode, ccore.decode))

@pytest.mark.parametrize("backend_name,encode_func,decode_func", BACKENDS)
@pytest.mark.parametrize("message,carrier,password", [
    ("Hello, World!", None, None),
    ("Hello, World!", "", None),
    ("Secret message", "This is some carrier text", None),
    ("Top secret", None, "mypassword123"),
    ("Very secret message", "Public carrier text", "securepass"),
    ("Hello 世界! 🌍", None, None),
    ("Test", "Carrier with 中文 and emoji 🚀", None),
    ("A" * 100, None, None),
    ("!@#$%^&*()_+-=[]{}|;':\",./<>?", None, None),
    ("Line 1\nLine 2\nLine 3", None, None),
    ("Tab\tseparated\tvalues", None, None),
    ("Single char", None, None),
    ("Message", "", "password"),
    ("Message", None, ""),
])
def test_encode_decode_roundtrip(backend_name, encode_func, decode_func, message, carrier, password):
    carrier_param = carrier if carrier is not None else ""
    password_param = password if password is not None else ""
    if message:
        encoded = encode_func(message, carrier_param, password_param)
        decoded = decode_func(encoded, password_param)
        assert decoded == message
    else:
        with pytest.raises(Exception):
            encode_func(message, carrier_param, password_param)


@pytest.mark.parametrize("backend_name,encode_func,decode_func", BACKENDS)
@pytest.mark.parametrize("test_input,expected_error", [
    ("", Exception),
    (("Secret", "correct", "wrong"), Exception),
    ("This text has no markers", Exception),
    (f"This text has \ufeff but no end marker", Exception),
    (f"This text has \u200c but no start marker", Exception),
])
def test_error_conditions(backend_name, encode_func, decode_func, test_input, expected_error):
    if isinstance(test_input, tuple):
        message, correct_password, wrong_password = test_input
        encoded = encode_func(message, "", correct_password)
        with pytest.raises(ValueError):
            decode_func(encoded, wrong_password)
    else:
        if test_input == "":
            with pytest.raises(Exception):
                encode_func(test_input, "", "")
        else:
            with pytest.raises(ValueError):
                decode_func(test_input, "")


@pytest.mark.parametrize("backend", ["python", "rust", "c"])
def test_multi_recipient_cross_backend(backend):
    """Test multi-recipient behavior works consistently across all backends."""
    if backend == "python":
        encode, decode = pycore.encode, pycore.decode
    elif backend == "rust":
        if not RUST_AVAILABLE:
            pytest.skip("Rust backend not available")
        encode, decode = rustcore.encode, rustcore.decode
    elif backend == "c":
        if not C_AVAILABLE:
            pytest.skip("C backend not available")
        encode, decode = ccore.encode, ccore.decode
    
    # Test multi-recipient scenario
    carrier = "C"
    m1, m2, m3 = "msg1", "msg2", "msg3"
    p1, p2, p3 = "pw1", "pw2", "pw3"
    
    # Encode three messages with three different passwords
    c1 = encode(m1, carrier, p1)
    c2 = encode(m2, c1, p2)
    c3 = encode(m3, c2, p3)
    
    # Each password should decrypt only its own message
    assert decode(c3, password=p1) == m1
    assert decode(c3, password=p2) == m2
    assert decode(c3, password=p3) == m3
    
    # Wrong password behavior varies by backend
    if backend == "python":
        # Python backend raises ValueError for wrong passwords
        with pytest.raises(ValueError):  # BadPasswordError inherits from ValueError
            decode(c3, password="wrong")
    elif backend == "c":
        # C backend raises ValueError for wrong passwords (consistent with Python)
        with pytest.raises(ValueError):
            decode(c3, password="wrong")
    elif backend == "rust":
        # Rust backend raises ValueError for wrong passwords (consistent with Python)
        with pytest.raises(ValueError):
            decode(c3, password="wrong")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 