"""Benchmark suite for whitespace-stego Python and Rust backends."""

import pytest
from faker import Faker
from whitespace_stego import encode as py_encode, decode as py_decode
from whitespace_stego.rust_bridge import (
    encode_message as rust_encode,
    decode_message as rust_decode,
    RUST_AVAILABLE
)
import tempfile
import os

pytestmark = pytest.mark.skipif(not RUST_AVAILABLE, reason="Rust module not available")

@pytest.fixture
def large_text():
    fake = Faker()
    # Generate a very large body of text (e.g., 100,000 characters)
    return fake.text(max_nb_chars=100000)

@pytest.fixture
def benchmark_encryption():
    """Fixture to provide encryption benchmark data."""
    fake = Faker()
    message = fake.text(max_nb_chars=1000)
    carrier = "A" * 10000
    return message, carrier

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
    assert isinstance(result, str)
    assert large_text in result

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
    assert isinstance(result, str)
    assert large_text in result

@pytest.mark.benchmark(group="decode_unicode")
def test_benchmark_decode_unicode_rust(benchmark, large_text):
    carrier = "A" * 10000
    encoded = rust_encode(large_text, carrier)
    result = benchmark(lambda: rust_decode(encoded))
    assert isinstance(result, str)
    assert large_text == result

@pytest.mark.benchmark(group="encryption")
def test_benchmark_encryption():
    """Test benchmark encryption functionality."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
        temp_file.write(b"Test message")
        temp_file_path = temp_file.name

    try:
        # Run benchmark
        result = benchmark.benchmark_encryption(temp_file_path)
        
        # Verify result structure
        assert isinstance(result, dict)
        assert 'encryption_time' in result
        assert 'decryption_time' in result
        assert 'compression_ratio' in result
        assert 'message_size' in result
        assert 'stego_size' in result
        
        # Verify value types
        assert isinstance(result['encryption_time'], float)
        assert isinstance(result['decryption_time'], float)
        assert isinstance(result['compression_ratio'], float)
        assert isinstance(result['message_size'], int)
        assert isinstance(result['stego_size'], int)
        
        # Verify value ranges
        assert result['encryption_time'] >= 0
        assert result['decryption_time'] >= 0
        assert result['compression_ratio'] > 0
        assert result['message_size'] > 0
        assert result['stego_size'] > 0
        
    finally:
        # Clean up
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

def test_benchmark_compression():
    """Test benchmark compression functionality."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
        temp_file.write(b"Test message" * 1000)  # Create a larger file for better compression test
        temp_file_path = temp_file.name

    try:
        # Run benchmark
        result = benchmark.benchmark_compression(temp_file_path)
        
        # Verify result structure
        assert isinstance(result, dict)
        assert 'original_size' in result
        assert 'compressed_size' in result
        assert 'compression_ratio' in result
        assert 'compression_time' in result
        
        # Verify value types
        assert isinstance(result['original_size'], int)
        assert isinstance(result['compressed_size'], int)
        assert isinstance(result['compression_ratio'], float)
        assert isinstance(result['compression_time'], float)
        
        # Verify value ranges
        assert result['original_size'] > 0
        assert result['compressed_size'] > 0
        assert result['compression_ratio'] > 0
        assert result['compression_time'] >= 0
        
    finally:
        # Clean up
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path) 