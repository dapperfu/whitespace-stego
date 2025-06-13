"""Tests for cross-implementation compatibility."""

import pytest

from whitespace_stego.core import decode as py_decode, encode as py_encode
from whitespace_stego.rust_bridge import decode as rs_decode, encode as rs_encode

def test_python_to_rust() -> None:
    """Test Python encoding -> Rust decoding."""
    message = "Secret message"
    carrier = "Public text"
    password = "mysecretpassword"
    
    # Python encode
    encoded = py_encode(message, carrier, password)
    
    # Rust decode
    decoded = rs_decode(encoded, password)
    assert decoded == message

def test_rust_to_python() -> None:
    """Test Rust encoding -> Python decoding."""
    message = "Secret message"
    carrier = "Public text"
    password = "mysecretpassword"
    
    # Rust encode
    encoded = rs_encode(message, carrier, password)
    
    # Python decode
    decoded = py_decode(encoded, password)
    assert decoded == message

def test_python_to_rust_no_password() -> None:
    """Test Python encoding -> Rust decoding without password."""
    message = "Secret message"
    carrier = "Public text"
    
    # Python encode
    encoded = py_encode(message, carrier)
    
    # Rust decode
    decoded = rs_decode(encoded)
    assert decoded == message

def test_rust_to_python_no_password() -> None:
    """Test Rust encoding -> Python decoding without password."""
    message = "Secret message"
    carrier = "Public text"
    
    # Rust encode
    encoded = rs_encode(message, carrier)
    
    # Python decode
    decoded = py_decode(encoded)
    assert decoded == message

def test_python_to_rust_unicode() -> None:
    """Test Python encoding -> Rust decoding with Unicode."""
    message = "Unicode: 你好世界 🌍"
    carrier = "English text"
    password = "mysecretpassword"
    
    # Python encode
    encoded = py_encode(message, carrier, password)
    
    # Rust decode
    decoded = rs_decode(encoded, password)
    assert decoded == message

def test_rust_to_python_unicode() -> None:
    """Test Rust encoding -> Python decoding with Unicode."""
    message = "Unicode: 你好世界 🌍"
    carrier = "English text"
    password = "mysecretpassword"
    
    # Rust encode
    encoded = rs_encode(message, carrier, password)
    
    # Python decode
    decoded = py_decode(encoded, password)
    assert decoded == message 