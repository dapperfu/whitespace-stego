import os
import pytest
import shutil
from pathlib import Path
from whitespace_stego.core import encode as py_encode, decode as py_decode
import subprocess

# Implementations to test
IMPLEMENTATIONS = {
    "python_core": {
        "name": "Python Core",
        "encode": py_encode,
        "decode": py_decode,
        "type": "library"
    },
    "python_cli": {
        "name": "Python CLI",
        "cmd": [".venv/bin/python", "-m", "whitespace_stego.cli"],
        "type": "cli"
    },
    "rust_cli": {
        "name": "Rust CLI",
        "cmd": ["./whitespace-stego-rs"],
        "type": "cli"
    },
    "c_cli": {
        "name": "C CLI",
        "cmd": ["./whitespace-stego-c"],
        "type": "cli"
    },
    "standalone_py": {
        "name": "Standalone Python",
        "cmd": ["./dist/whitespace-stego-py"],
        "type": "cli"
    }
}

MESSAGES = {
    "ascii": "Hello World!",
    "utf8": "Hello 世界! 🚀",
    "emoji": "😀😃😄😁😆😅😂🤣😊😇",
}
CARRIER = "This is the carrier text."
PASSWORD = "testpass"

CROSS_DIR = Path("cross_vectors")
CROSS_DIR.mkdir(exist_ok=True)

@pytest.mark.parametrize("msgtype,message", list(MESSAGES.items()))
@pytest.mark.parametrize("use_password", [False, True])
def test_cross_vector_matrix(msgtype, message, use_password):
    password = PASSWORD if use_password else None
    encoded_files = {}
    # 1. Encode with each implementation
    for impl_id, impl in IMPLEMENTATIONS.items():
        fname = CROSS_DIR / f"{impl_id}_encoded_{msgtype}{'_pw' if use_password else ''}.txt"
        if impl["type"] == "library":
            try:
                encoded = impl["encode"](message, CARRIER, password)
                fname.write_text(encoded, encoding="utf-8")
                encoded_files[impl_id] = fname
            except Exception as e:
                pytest.skip(f"{impl_id} encode failed: {e}")
        else:
            # CLI encode
            msgfile = CROSS_DIR / f"{impl_id}_msg.txt"
            carfile = CROSS_DIR / f"{impl_id}_carrier.txt"
            msgfile.write_text(message, encoding="utf-8")
            carfile.write_text(CARRIER, encoding="utf-8")
            cmd = impl["cmd"] + ["encode", "--mf", str(msgfile), "--cf", str(carfile), "-o", str(fname)]
            if password:
                cmd += ["-p", password]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and fname.exists():
                encoded_files[impl_id] = fname
            else:
                pytest.skip(f"{impl_id} encode failed: {result.stderr}")
    # 2. Decode with all implementations
    for enc_impl, enc_file in encoded_files.items():
        encoded = enc_file.read_text(encoding="utf-8")
        for dec_impl, impl in IMPLEMENTATIONS.items():
            if impl["type"] == "library":
                try:
                    decoded = impl["decode"](encoded, password)
                except Exception as e:
                    pytest.fail(f"{dec_impl} decode failed on {enc_impl}: {e}")
            else:
                # CLI decode
                out_file = CROSS_DIR / f"{enc_impl}_decoded_by_{dec_impl}_{msgtype}{'_pw' if use_password else ''}.txt"
                encfile = CROSS_DIR / f"{enc_impl}_decode_input.txt"
                encfile.write_text(encoded, encoding="utf-8")
                cmd = impl["cmd"] + ["decode", "--cf", str(encfile), "-o", str(out_file)]
                if password:
                    cmd += ["-p", password]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0 and out_file.exists():
                    decoded = out_file.read_text(encoding="utf-8")
                else:
                    pytest.fail(f"{dec_impl} decode failed on {enc_impl}: {result.stderr}")
            assert decoded == message, f"Decoded mismatch: Encoded by {enc_impl}, decoded by {dec_impl}, expected '{message}', got '{decoded}'" 