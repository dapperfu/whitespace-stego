"""
Test 00: Parametrized Core (Python), Rust PyO3 Backend, and C Backend

This test suite runs all encode/decode tests against the Python, Rust, and C backends.
"""

import pytest
import importlib

# Import Python backend
import whitespace_stego.core as pycore

# Try to import Rust backend
try:
    import whitespace_stego_backend as rustcore
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False
    rustcore = None

# Try to import C backend
try:
    from whitespace_stego.c_backend import encode as c_encode, decode as c_decode, is_available as c_is_available
    C_AVAILABLE = c_is_available()
except ImportError:
    C_AVAILABLE = False
    c_encode = c_decode = None

# Build backends list
BACKENDS = [
    ("python", pycore.encode, pycore.decode),
]

if RUST_AVAILABLE:
    BACKENDS.append(("rust", rustcore.encode, rustcore.decode))

if C_AVAILABLE:
    BACKENDS.append(("c", c_encode, c_decode))

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
        with pytest.raises(expected_error):
            decode_func(encoded, wrong_password)
    else:
        if test_input == "":
            with pytest.raises(expected_error):
                encode_func(test_input, "", "")
        else:
            with pytest.raises(expected_error):
                decode_func(test_input, "")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 