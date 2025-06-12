"""Benchmark suite for whitespace-stego Python and Rust backends."""

import pytest
from faker import Faker
from whitespace_stego import encode as py_encode, decode as py_decode
from whitespace_stego.rust_bridge import (
    encode_message as rust_encode,
    decode_message as rust_decode,
    RUST_AVAILABLE
)

pytestmark = pytest.mark.skipif(not RUST_AVAILABLE, reason="Rust module not available")

@pytest.fixture
def large_text():
    fake = Faker()
    # Generate a very large body of text (e.g., 100,000 characters)
    return fake.text(max_nb_chars=100000)

@pytest.mark.benchmark(group="encode")
def test_benchmark_encode_python(benchmark, large_text):
    result = benchmark(py_encode, large_text, "A carrier message" * 1000)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="encode")
def test_benchmark_encode_rust(benchmark, large_text):
    carrier = "A" * 10000
    result = benchmark(lambda: rust_encode(large_text, carrier))

@pytest.mark.benchmark(group="decode")
def test_benchmark_decode_python(benchmark, large_text):
    encoded = py_encode(large_text, "A carrier message" * 1000)
    result = benchmark(py_decode, encoded)
    assert isinstance(result, tuple)
    assert large_text in result[0]

@pytest.mark.benchmark(group="decode")
def test_benchmark_decode_rust(benchmark, large_text):
    carrier = "A" * 10000
    encoded = rust_encode(large_text, carrier)
    result = benchmark(lambda: rust_decode(encoded))

@pytest.mark.benchmark(group="encode_unicode")
def test_benchmark_encode_unicode_python(benchmark, large_text):
    result = benchmark(py_encode, large_text, "A carrier message" * 1000)
    assert isinstance(result, str)

@pytest.mark.benchmark(group="encode_unicode")
def test_benchmark_encode_unicode_rust(benchmark, large_text):
    carrier = "A" * 10000
    result = benchmark(lambda: rust_encode(large_text, carrier))

@pytest.mark.benchmark(group="decode_unicode")
def test_benchmark_decode_unicode_python(benchmark, large_text):
    encoded = py_encode(large_text, "A carrier message" * 1000)
    result = benchmark(py_decode, encoded)
    assert isinstance(result, tuple)
    assert large_text in result[0]

@pytest.mark.benchmark(group="decode_unicode")
def test_benchmark_decode_unicode_rust(benchmark, large_text):
    carrier = "A" * 10000
    encoded = rust_encode(large_text, carrier)
    result = benchmark(lambda: rust_decode(encoded))
    assert isinstance(result, str)
    assert large_text == result 