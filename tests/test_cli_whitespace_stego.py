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
    """Test same-backend roundtrips for Python CLI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"
        dec_path = Path(tmpdir) / "decoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        encode_cmd = [
            ".venv/bin/python",
            "-m",
            "whitespace_stego.cli",
            "--backend",
            backend,
            "encode",
            "--message-file",
            str(msg_path),
            "--carrier-file",
            str(car_path),
            "--output",
            str(enc_path),
        ]
        if password:
            encode_cmd += ["--password", password]
        subprocess.run(encode_cmd, check=True)

        decode_cmd = [
            ".venv/bin/python",
            "-m",
            "whitespace_stego.cli",
            "--backend",
            backend,
            "decode",
            "--carrier-file",
            str(enc_path),
            "--output",
            str(dec_path),
        ]
        if password:
            decode_cmd += ["--password", password]
        subprocess.run(decode_cmd, check=True)

        result = dec_path.read_text(encoding="utf-8")
        assert result == message


@pytest.mark.parametrize("encode_backend", ["python", "rust"])
@pytest.mark.parametrize("decode_backend", ["python", "rust"])
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize(
    "password", [None]
)  # Only test without passwords for cross-backend compatibility
def test_cli_cross_backend_roundtrip(
    encode_backend, decode_backend, message, carrier, password
):
    """Test cross-backend roundtrips for Python CLI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"
        dec_path = Path(tmpdir) / "decoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # Encode with first backend
        encode_cmd = [
            ".venv/bin/python",
            "-m",
            "whitespace_stego.cli",
            "--backend",
            encode_backend,
            "encode",
            "--message-file",
            str(msg_path),
            "--carrier-file",
            str(car_path),
            "--output",
            str(enc_path),
        ]
        if password:
            encode_cmd += ["--password", password]
        subprocess.run(encode_cmd, check=True)

        # Decode with second backend
        decode_cmd = [
            ".venv/bin/python",
            "-m",
            "whitespace_stego.cli",
            "--backend",
            decode_backend,
            "decode",
            "--carrier-file",
            str(enc_path),
            "--output",
            str(dec_path),
        ]
        if password:
            decode_cmd += ["--password", password]
        subprocess.run(decode_cmd, check=True)

        result = dec_path.read_text(encoding="utf-8")
        assert result == message


@pytest.mark.parametrize("encode_tool", ["python", "rust-cli"])
@pytest.mark.parametrize("decode_tool", ["python", "rust-cli"])
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize(
    "password", [None]
)  # Only test without passwords for cross-tool compatibility
def test_cli_cross_tool_roundtrip(encode_tool, decode_tool, message, carrier, password):
    """Test cross-tool roundtrips between Python CLI and Rust CLI."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"
        dec_path = Path(tmpdir) / "decoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # Encode with first tool
        if encode_tool == "python":
            encode_cmd = [
                ".venv/bin/python",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "rust",  # Use rust backend for Python CLI
                "encode",
                "--message-file",
                str(msg_path),
                "--carrier-file",
                str(car_path),
                "--output",
                str(enc_path),
            ]
            if password:
                encode_cmd += ["--password", password]
        else:  # rust-cli
            encode_cmd = [
                "./whitespace-stego-rs",
                "encode",
                "--mf",
                str(msg_path),
                "--cf",
                str(car_path),
                "-o",
                str(enc_path),
            ]
            if password:
                encode_cmd += ["-p", password]

        subprocess.run(encode_cmd, check=True)

        # Decode with second tool
        if decode_tool == "python":
            decode_cmd = [
                ".venv/bin/python",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "rust",  # Use rust backend for Python CLI
                "decode",
                "--carrier-file",
                str(enc_path),
                "--output",
                str(dec_path),
            ]
            if password:
                decode_cmd += ["--password", password]
        else:  # rust-cli
            decode_cmd = [
                "./whitespace-stego-rs",
                "decode",
                "--cf",
                str(enc_path),
                "-o",
                str(dec_path),
            ]
            if password:
                decode_cmd += ["-p", password]

        subprocess.run(decode_cmd, check=True)

        result = dec_path.read_text(encoding="utf-8")
        assert result == message
