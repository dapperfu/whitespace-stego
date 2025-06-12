import pytest
from whitespace_stego import encode
import logging

logging.basicConfig(level=logging.DEBUG)

def test_encode_binary_benchmark(benchmark):
    binary = "01" * 10000
    logging.debug(f"Running {__name__}.test_encode_binary_benchmark")
    result = benchmark(encode.encode_binary, binary)
    assert isinstance(result, str)

def test_encode_message_benchmark(benchmark):
    message = "Benchmark message" * 1000
    logging.debug(f"Running {__name__}.test_encode_message_benchmark")
    result = benchmark(encode.encode_message, message)
    assert isinstance(result, str)

def test_encode_and_insert_benchmark(benchmark):
    message = "Benchmark message" * 1000
    carrier = "A" * 10000
    logging.debug(f"Running {__name__}.test_encode_and_insert_benchmark")
    result = benchmark(encode.encode_and_insert, message, carrier)
    assert isinstance(result, str) 