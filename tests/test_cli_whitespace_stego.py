import pytest
import subprocess
import tempfile
from pathlib import Path
from test_data import MESSAGES, CARRIERS, PASSWORDS

@pytest.mark.parametrize("backend", ["python", "rust"])
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_cli_roundtrip_whitespace_stego(backend, message, carrier, password):
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"
        dec_path = Path(tmpdir) / "decoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        if backend == "rust":
            encode_cmd = [
                "./whitespace-stego-rs", "encode",
                "--mf", str(msg_path),
                "--cf", str(car_path),
                "-o", str(enc_path)
            ]
            if password:
                encode_cmd += ["-p", password]
            subprocess.run(encode_cmd, check=True)

            decode_cmd = [
                "./whitespace-stego-rs", "decode",
                "--cf", str(enc_path),
                "-o", str(dec_path)
            ]
            if password:
                decode_cmd += ["-p", password]
            subprocess.run(decode_cmd, check=True)
        else:
            encode_cmd = [
                "python3", "-m", "whitespace_stego.cli", "encode",
                "--message-file", str(msg_path),
                "--carrier-file", str(car_path),
                "--output", str(enc_path)
            ]
            if password:
                encode_cmd += ["--password", password]
            subprocess.run(encode_cmd, check=True)

            decode_cmd = [
                "python3", "-m", "whitespace_stego.cli", "decode",
                "--carrier-file", str(enc_path),
                "--output", str(dec_path)
            ]
            if password:
                decode_cmd += ["--password", password]
            subprocess.run(decode_cmd, check=True)

        result = dec_path.read_text(encoding="utf-8")
        assert result == message
