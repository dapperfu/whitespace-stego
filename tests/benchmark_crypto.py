import pytest
from whitespace_stego import crypto

def test_derive_key_benchmark(benchmark):
    password = "benchmark_password"
    result = benchmark(crypto.derive_key, password)
    key, salt = result
    assert isinstance(key, bytes)
    assert isinstance(salt, bytes)

def test_encrypt_decrypt_benchmark(benchmark):
    message = "Benchmark secret message"
    password = "benchmark_password"
    encrypted = benchmark(crypto.encrypt_message, message, password)
    decrypted = crypto.decrypt_message(encrypted, password)
    assert decrypted == message 