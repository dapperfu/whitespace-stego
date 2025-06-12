import pytest
from whitespace_stego import crypto
import logging

logging.basicConfig(level=logging.DEBUG)

def test_derive_key_benchmark(benchmark):
    password = "benchmark_password"
    logging.debug(f"Running {__name__}.test_derive_key_benchmark")
    result = benchmark(crypto.derive_key, password)
    key, salt = result
    assert isinstance(key, bytes)
    assert isinstance(salt, bytes)

def test_encrypt_decrypt_benchmark(benchmark):
    message = "Benchmark secret message"
    password = "benchmark_password"
    logging.debug(f"Running {__name__}.test_encrypt_decrypt_benchmark")
    encrypted = benchmark(crypto.encrypt_message, message, password)
    decrypted = crypto.decrypt_message(encrypted, password)
    assert decrypted == message 