import subprocess
import tempfile
import os
import sys
import pytest

BINARIES = {
    'python-cli': os.path.abspath('.venv/bin/whitespace-stego'),
    'c': os.path.abspath('bin/whitespace-stego-c'),
    'go': os.path.abspath('bin/whitespace-stego-go'),
    'py': os.path.abspath('bin/whitespace-stego-py'),
    'rs': os.path.abspath('bin/whitespace-stego-rs'),
}

@pytest.mark.parametrize('encoder', list(BINARIES.keys()))
def test_cross_impl_roundtrip(encoder):
    message = "cross-impl test message"
    carrier = "This is the carrier text."
    
    # Prepare temp files
    with tempfile.TemporaryDirectory() as tmpdir:
        carrier_path = os.path.join(tmpdir, 'carrier.txt')
        encoded_path = os.path.join(tmpdir, 'encoded.txt')
        with open(carrier_path, 'w', encoding='utf-8') as f:
            f.write(carrier)
        
        # Encode with the selected encoder
        enc_bin = BINARIES[encoder]
        enc_cmd = [enc_bin, 'encode', '-m', message, '-c', carrier_path, '-o', encoded_path]
        subprocess.run(enc_cmd, check=True)
        
        # For each decoder (other than encoder), decode and check
        for decoder, dec_bin in BINARIES.items():
            if decoder == encoder:
                continue
            dec_cmd = [dec_bin, 'decode', '-c', encoded_path]
            result = subprocess.run(dec_cmd, check=True, capture_output=True, encoding='utf-8')
            decoded = result.stdout.strip()
            assert decoded == message, f"Decoded with {decoder} did not match: {decoded}" 