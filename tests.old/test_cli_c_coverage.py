"""Tests for C CLI functionality and cross-implementation roundtrips."""

import pytest
import subprocess
import tempfile
from pathlib import Path
from test_data import MESSAGES, CARRIERS, PASSWORDS


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_c_cli_roundtrip(message, carrier, password):
    """Test C CLI self roundtrip (encode with C CLI, decode with C CLI)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"
        dec_path = Path(tmpdir) / "decoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # Encode with C CLI
        encode_cmd = [
            "./whitespace-stego-c",
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

        # Capture output to see what's happening
        result = subprocess.run(encode_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Encode command failed: {encode_cmd}")
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
            print(f"returncode: {result.returncode}")
            result.check_returncode()  # This will raise the exception with the captured output

        # Decode with C CLI
        decode_cmd = [
            "./whitespace-stego-c",
            "decode",
            "--carrier-file",
            str(enc_path),
            "--output",
            str(dec_path),
        ]
        if password:
            decode_cmd += ["--password", password]

        result = subprocess.run(decode_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Decode command failed: {decode_cmd}")
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
            print(f"returncode: {result.returncode}")
            result.check_returncode()  # This will raise the exception with the captured output

        result = dec_path.read_text(encoding="utf-8")
        assert result == message


@pytest.mark.parametrize("encode_tool", ["python", "rust-cli", "c-cli"])
@pytest.mark.parametrize("decode_tool", ["python", "rust-cli", "c-cli"])
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize(
    "password", [None]
)  # Only test without passwords for cross-tool compatibility
def test_cross_tool_roundtrip_with_c(
    encode_tool, decode_tool, message, carrier, password
):
    """Test cross-tool roundtrips including C CLI with Python and Rust CLIs."""
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
        elif encode_tool == "rust-cli":
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
        else:  # c-cli
            encode_cmd = [
                "./whitespace-stego-c",
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
        elif decode_tool == "rust-cli":
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
        else:  # c-cli
            decode_cmd = [
                "./whitespace-stego-c",
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


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_c_cli_verbose_output(message, carrier, password):
    """Test C CLI verbose flag output."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # Test verbose output during encoding
        encode_cmd = [
            "./whitespace-stego-c",
            "--verbose",
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

        result = subprocess.run(encode_cmd, capture_output=True, text=True, check=True)

        # Check for debug output in stderr
        assert "DEBUG:" in result.stderr
        assert "Encoding message from file:" in result.stderr
        assert "Using password:" in result.stderr


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_c_cli_error_handling(message, carrier, password):
    """Test C CLI error handling for missing files and invalid arguments."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path = Path(tmpdir) / "encoded.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # Test missing message file
        encode_cmd = [
            "./whitespace-stego-c",
            "encode",
            "--message-file",
            "nonexistent.txt",
            "--carrier-file",
            str(car_path),
            "--output",
            str(enc_path),
        ]
        if password:
            encode_cmd += ["--password", password]

        result = subprocess.run(encode_cmd, capture_output=True, text=True)
        assert result.returncode != 0
        assert "Error opening file" in result.stderr

        # Test missing carrier file
        encode_cmd = [
            "./whitespace-stego-c",
            "encode",
            "--message-file",
            str(msg_path),
            "--carrier-file",
            "nonexistent.txt",
            "--output",
            str(enc_path),
        ]
        if password:
            encode_cmd += ["--password", password]

        result = subprocess.run(encode_cmd, capture_output=True, text=True)
        assert result.returncode != 0
        assert "Error opening file" in result.stderr

        # Test invalid command
        result = subprocess.run(
            ["./whitespace-stego-c", "invalid"], capture_output=True, text=True
        )
        assert result.returncode != 0
        assert "Unknown command" in result.stderr


def test_c_cli_help_output():
    """Test C CLI help output consistency."""
    # Test main help
    result = subprocess.run(
        ["./whitespace-stego-c", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Usage:" in result.stdout
    assert "encode" in result.stdout
    assert "decode" in result.stdout
    assert "help" in result.stdout

    # Test encode help
    result = subprocess.run(
        ["./whitespace-stego-c", "help", "encode"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Usage:" in result.stdout
    assert "--message-file" in result.stdout
    assert "--carrier-file" in result.stdout
    assert "--output" in result.stdout
    assert "--password" in result.stdout

    # Test decode help
    result = subprocess.run(
        ["./whitespace-stego-c", "help", "decode"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Usage:" in result.stdout
    assert "--carrier-file" in result.stdout
    assert "--output" in result.stdout
    assert "--password" in result.stdout


@pytest.mark.parametrize("message", MESSAGES[:2])  # Test with first 2 messages
@pytest.mark.parametrize("carrier", CARRIERS[:2])  # Test with first 2 carriers
def test_c_cli_output_consistency(message, carrier):
    """Test that C CLI produces consistent output across multiple runs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        msg_path = Path(tmpdir) / "msg.txt"
        car_path = Path(tmpdir) / "carrier.txt"
        enc_path1 = Path(tmpdir) / "encoded1.txt"
        enc_path2 = Path(tmpdir) / "encoded2.txt"

        msg_path.write_text(message, encoding="utf-8")
        car_path.write_text(carrier, encoding="utf-8")

        # First encoding
        encode_cmd1 = [
            "./whitespace-stego-c",
            "encode",
            "--message-file",
            str(msg_path),
            "--carrier-file",
            str(car_path),
            "--output",
            str(enc_path1),
        ]
        subprocess.run(encode_cmd1, check=True)

        # Second encoding
        encode_cmd2 = [
            "./whitespace-stego-c",
            "encode",
            "--message-file",
            str(msg_path),
            "--carrier-file",
            str(car_path),
            "--output",
            str(enc_path2),
        ]
        subprocess.run(encode_cmd2, check=True)

        # Both outputs should be identical
        output1 = enc_path1.read_text(encoding="utf-8")
        output2 = enc_path2.read_text(encoding="utf-8")
        assert output1 == output2
