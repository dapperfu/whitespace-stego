import pytest
from whitespace_stego.common import charset
import logging

logging.basicConfig(level=logging.DEBUG)

def test_is_valid_carrier_benchmark(benchmark):
    carrier = "A" * 10000
    logging.debug(f"Running {__name__}.test_is_valid_carrier_benchmark")
    result = benchmark(charset.is_valid_carrier, carrier)
    assert result is True

def test_get_control_chars_benchmark(benchmark):
    start, end = benchmark(lambda: charset.get_control_chars())
    logging.debug(f"Running {__name__}.test_get_control_chars_benchmark")
    assert isinstance(start, str) and isinstance(end, str)

def test_get_binary_chars_benchmark(benchmark):
    zwsp, zwnj = benchmark(lambda: charset.get_binary_chars())
    logging.debug(f"Running {__name__}.test_get_binary_chars_benchmark")
    assert isinstance(zwsp, str) and isinstance(zwnj, str) 