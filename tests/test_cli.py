import subprocess
import pytest
import os
import hashlib

MESSAGES = ["hello", "😀 test", "秘密", "🏳️‍🌈🌍🐍🧪📦"]
CARRIERS = ["", "abc", "XYZ"]
PASSWORDS = ["", "hunter2", "pässwörd"]
BINARIES = {
    "c": "./whitespace-stego-c",
    "rust": "rust/whitespace_stego_rs/target/release/whitespace-stego-rs",
}

def hash_output(data):
    return hashlib.sha256(data.encode()).hexdigest()

@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
@pytest.mark.parametrize("lang", list(BINARIES.keys()))
def test_crosslang_password_roundtrip(tmp_path, message, carrier, password, lang):
    binary = BINARIES[lang]
    args = [binary, "encode", "-m", message, "-c", carrier]
    if password:
        args += ["-p", password]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert result.returncode == 0, f"Encoding failed: {result.stderr}"
    encoded = result.stdout.strip()
    assert encoded != ""

    decode_args = [binary, "decode", "-m", encoded]
    if password:
        decode_args += ["-p", password]
    decoded_result = subprocess.run(decode_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert decoded_result.returncode == 0, f"Decoding failed: {decoded_result.stderr}"
    decoded = decoded_result.stdout.strip()
    assert decoded == message

    # Regression snapshot check
    snapshot_path = tmp_path / ("snapshot_" + lang + ".sha256")
    snapshot_hash = hash_output(encoded)
    if not snapshot_path.exists():
        snapshot_path.write_text(snapshot_hash)
    else:
        stored = snapshot_path.read_text()
        assert snapshot_hash == stored, f"Output mismatch for {lang}: {snapshot_hash} != {stored}"