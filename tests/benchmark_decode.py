import pytest
from whitespace_stego import encode, decode
import logging

logging.basicConfig(level=logging.DEBUG)

def test_decode_message_benchmark(benchmark):
    message = "Benchmark message" * 1000
    encoded = encode.encode_message(message)
    logging.debug(f"Running {__name__}.test_decode_message_benchmark")
    result = benchmark(decode.decode_message, encoded)
    assert result == message

def test_decode_and_remove_benchmark(benchmark):
    message = "Benchmark message" * 1000
    carrier = "A" * 10000
    encoded = encode.encode_and_insert(message, carrier)
    logging.debug(f"Running {__name__}.test_decode_and_remove_benchmark")
    result = benchmark(decode.decode_and_remove, encoded)
    assert result[0] == message 