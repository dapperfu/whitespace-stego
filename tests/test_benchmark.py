"""Benchmark suite for whitespace-stego Python and Rust backends."""

import pytest
from whitespace_stego import encode as py_encode, decode as py_decode
from whitespace_stego.rust_bridge import (
    encode_message as rust_encode,
    decode_message as rust_decode,
    RUST_AVAILABLE
)

pytestmark = pytest.mark.skipif(not RUST_AVAILABLE, reason="Rust module not available")

@pytest.mark.benchmark(group="encode")
def test_benchmark_encode_python(benchmark):
    message = "Hello, World! " * 1000
    result = benchmark(py_encode, message, "A carrier message" * 1000)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="encode")
def test_benchmark_encode_rust(benchmark):
    message = "Hello, World! " * 1000
    result = benchmark(rust_encode, message)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="decode")
def test_benchmark_decode_python(benchmark):
    message = "Hello, World! " * 1000
    encoded = py_encode(message, "A carrier message" * 1000)
    result = benchmark(py_decode, encoded)
    assert isinstance(result, tuple)
    assert message in result[0]

@pytest.mark.benchmark(group="decode")
def test_benchmark_decode_rust(benchmark):
    message = "Hello, World! " * 1000
    encoded = rust_encode(message)
    result = benchmark(rust_decode, encoded)
    assert isinstance(result, str)
    assert message == result

@pytest.mark.benchmark(group="encode_unicode")
def test_benchmark_encode_unicode_python(benchmark):
    message = "Hello, 世界! 👋 " * 1000
    result = benchmark(py_encode, message, "A carrier message" * 1000)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="encode_unicode")
def test_benchmark_encode_unicode_rust(benchmark):
    message = "Hello, 世界! 👋 " * 1000
    result = benchmark(rust_encode, message)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="decode_unicode")
def test_benchmark_decode_unicode_python(benchmark):
    message = "Hello, 世界! 👋 " * 1000
    encoded = py_encode(message, "A carrier message" * 1000)
    result = benchmark(py_decode, encoded)
    assert isinstance(result, tuple)
    assert message in result[0]

@pytest.mark.benchmark(group="decode_unicode")
def test_benchmark_decode_unicode_rust(benchmark):
    message = "Hello, 世界! 👋 " * 1000
    encoded = rust_encode(message)
    result = benchmark(rust_decode, encoded)
    assert isinstance(result, str)
    assert message == result 