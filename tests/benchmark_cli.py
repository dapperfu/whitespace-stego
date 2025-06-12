import pytest
from whitespace_stego import cli
import logging

logging.basicConfig(level=logging.DEBUG)

def test_main_encode_benchmark(benchmark, tmp_path):
    message_file = tmp_path / "message.txt"
    carrier_file = tmp_path / "carrier.txt"
    output_file = tmp_path / "output.txt"
    message = "Benchmark message" * 1000
    carrier = "A" * 10000
    message_file.write_text(message)
    carrier_file.write_text(carrier)
    args = [
        "encode",
        "-m", str(message_file),
        "-c", str(carrier_file),
        "-o", str(output_file)
    ]
    logging.debug(f"Running {__name__}.test_main_encode_benchmark")
    benchmark(lambda: cli.main(args))
    assert output_file.exists()

def test_main_decode_benchmark(benchmark, tmp_path):
    message = "Benchmark message" * 1000
    carrier = "A" * 10000
    from whitespace_stego.encode import encode_and_insert
    encoded = encode_and_insert(message, carrier)
    encoded_file = tmp_path / "encoded.txt"
    output_file = tmp_path / "decoded.txt"
    encoded_file.write_text(encoded)
    args = [
        "decode",
        "-c", str(encoded_file),
        "-o", str(output_file)
    ]
    logging.debug(f"Running {__name__}.test_main_decode_benchmark")
    benchmark(lambda: cli.main(args))
    assert output_file.exists() 