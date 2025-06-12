import pytest
from whitespace_stego.common import charset

def test_is_valid_carrier_benchmark(benchmark):
    carrier = "A" * 10000
    result = benchmark(charset.is_valid_carrier, carrier)
    assert result is True

def test_get_control_chars_benchmark(benchmark):
    start, end = benchmark(lambda: charset.get_control_chars())
    assert isinstance(start, str) and isinstance(end, str)

def test_get_binary_chars_benchmark(benchmark):
    zwsp, zwnj = benchmark(lambda: charset.get_binary_chars())
    assert isinstance(zwsp, str) and isinstance(zwnj, str) 