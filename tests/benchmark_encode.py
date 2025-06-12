import pytest
from whitespace_stego import encode

def test_encode_binary_benchmark(benchmark):
    binary = "01" * 10000
    result = benchmark(encode.encode_binary, binary)
    assert isinstance(result, str)

def test_encode_message_benchmark(benchmark):
    message = "Benchmark message" * 1000
    result = benchmark(encode.encode_message, message)
    assert isinstance(result, str)

def test_encode_and_insert_benchmark(benchmark):
    message = "Benchmark message" * 1000
    carrier = "A" * 10000
    result = benchmark(encode.encode_and_insert, message, carrier)
    assert isinstance(result, str) 