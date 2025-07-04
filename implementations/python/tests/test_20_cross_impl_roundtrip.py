import subprocess
import tempfile
import os
import pytest
from whitespace_stego.constants import START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT

# Define binaries and their supported backends
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
BINARIES = {
    'python-cli': {
        'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-py'),
        'backends': ['python', 'rust', 'c'],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
            [bin_path, '-b', backend] + ['encode', '-m', msg, '-c', carrier_path, '-o', output_path] if backend else
            [bin_path, 'encode', '-m', msg, '-c', carrier_path, '-o', output_path],
        'decode_cmd': lambda bin_path, carrier_path, output_path, backend=None:
            [bin_path, '-b', backend] + ['decode', '--carrier-file', carrier_path, '-o', output_path] if backend else
            [bin_path, 'decode', '--carrier-file', carrier_path, '-o', output_path]
    },
    'py': {
        'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-py'),
        'backends': ['python', 'rust', 'c'],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
            [bin_path, '-b', backend] + ['encode', '-m', msg, '-c', carrier_path, '-o', output_path] if backend else
            [bin_path, 'encode', '-m', msg, '-c', carrier_path, '-o', output_path],
        'decode_cmd': lambda bin_path, carrier_path, output_path, backend=None:
            [bin_path, '-b', backend] + ['decode', '--carrier-file', carrier_path, '-o', output_path] if backend else
            [bin_path, 'decode', '--carrier-file', carrier_path, '-o', output_path]
    },
    'c': {
        'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-c'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
            [bin_path, 'encode', '--message-file', msg, '--carrier-file', carrier_path, '--output', output_path],
        'decode_cmd': lambda bin_path, carrier_path, output_path, backend=None:
            [bin_path, 'decode', '--carrier-file', carrier_path, '--output', output_path]
    },
    'go': {
        'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-go'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
            [bin_path, 'encode', '-m', msg, '-cf', carrier_path, '-o', output_path],
        'decode_cmd': lambda bin_path, carrier_path, output_path, backend=None:
            [bin_path, 'decode', '-cf', carrier_path, '-o', output_path]
    },
    'rs': {
        'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-rs'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
            [bin_path, 'encode', '-m', msg, '--cf', carrier_path, '-o', output_path],
        'decode_cmd': lambda bin_path, carrier_path, output_path, backend=None:
            [bin_path, 'decode', '--cf', carrier_path, '-o', output_path]
    },
}

# Generate all combinations for testing
ALL_METHODS = []
for binary_name, binary_info in BINARIES.items():
    for backend in binary_info['backends']:
        ALL_METHODS.append((binary_name, backend))

@pytest.mark.parametrize('encoder_name,encoder_backend', ALL_METHODS)
def test_self_consistency_roundtrip(encoder_name, encoder_backend):
    """Test that each implementation can encode and decode its own messages correctly."""
    message = "self-consistency test message"
    carrier = "This is the carrier text."

    with tempfile.TemporaryDirectory() as tmpdir:
        carrier_path = os.path.join(tmpdir, 'carrier.txt')
        encoded_path = os.path.join(tmpdir, 'encoded.txt')
        decoded_path = os.path.join(tmpdir, 'decoded.txt')
        
        # Write carrier to file
        with open(carrier_path, 'w', encoding='utf-8') as f:
            f.write(carrier)

        # For C binary, we need to write message to a file
        if encoder_name == 'c':
            message_path = os.path.join(tmpdir, 'message.txt')
            with open(message_path, 'w', encoding='utf-8') as f:
                f.write(message)
            msg_arg = message_path
        else:
            msg_arg = message

        # Build encode command
        enc_bin = BINARIES[encoder_name]['path']
        enc_cmd = BINARIES[encoder_name]['encode_cmd'](enc_bin, msg_arg, carrier_path, encoded_path, encoder_backend)
        subprocess.run(enc_cmd, check=True)

        # Decode with the same implementation/backend
        dec_bin = BINARIES[encoder_name]['path']
        dec_cmd = BINARIES[encoder_name]['decode_cmd'](dec_bin, encoded_path, decoded_path, encoder_backend)
        subprocess.run(dec_cmd, check=True)
        
        # Read the decoded message
        with open(decoded_path, 'r', encoding='utf-8') as f:
            decoded_message = f.read().strip()
        
        assert message in decoded_message, f"Failed to decode with {encoder_name} (backend: {encoder_backend}). Expected '{message}', got '{decoded_message}'"

def test_encoding_compatibility():
    """Test if different implementations produce compatible encoded output."""
    message = "compatibility test message"
    carrier = "This is the carrier text."
    
    print(f"Testing with message: {repr(message)}")
    print(f"Testing with carrier: {repr(carrier)}")
    
    BINARIES = {
        'python-cli': {
            'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-py'),
            'backends': ['python', 'rust', 'c'],
            'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
                [bin_path, '-b', backend] + ['encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path] if backend else
                [bin_path, 'encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path],
        },
        'py': {
            'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-py'),
            'backends': ['python', 'rust', 'c'],
            'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
                [bin_path, '-b', backend] + ['encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path] if backend else
                [bin_path, 'encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path],
        },
        'c': {
            'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-c'),
            'backends': [None],
            'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
                [bin_path, 'encode', '--message-file', msg, '--carrier-file', carrier_path, '--output', output_path],
        },
        'go': {
            'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-go'),
            'backends': [None],
            'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
                [bin_path, 'encode', '-m', msg, '-cf', carrier_path, '-o', output_path],
        },
        'rs': {
            'path': os.path.join(PROJECT_ROOT, 'bin', 'whitespace-stego-rs'),
            'backends': [None],
            'encode_cmd': lambda bin_path, msg, carrier_path, output_path, backend=None: 
                [bin_path, 'encode', '-m', msg, '--cf', carrier_path, '-o', output_path],
        },
    }

    encoded_outputs = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        carrier_path = os.path.join(tmpdir, 'carrier.txt')
        with open(carrier_path, 'w', encoding='utf-8') as f:
            f.write(carrier)
        
        for binary_name, binary_info in BINARIES.items():
            for backend in binary_info['backends']:
                encoded_path = os.path.join(tmpdir, f'encoded_{binary_name}_{backend}.txt')
                # For C binary, we need to write message to a file
                if binary_name == 'c':
                    message_path = os.path.join(tmpdir, 'message.txt')
                    with open(message_path, 'w', encoding='utf-8') as f:
                        f.write(message)
                    msg_arg = message_path
                else:
                    msg_arg = message
                # Build encode command
                enc_bin = binary_info['path']
                enc_cmd = binary_info['encode_cmd'](enc_bin, msg_arg, carrier_path, encoded_path, backend)
                print(f"Running {binary_name} (backend={backend}) command: {enc_cmd}")
                subprocess.run(enc_cmd, check=True)
                with open(encoded_path, 'r', encoding='utf-8') as f:
                    encoded_outputs[f"{binary_name}-{backend}"] = f.read()
        # Compare all outputs
        outputs = list(encoded_outputs.items())
        first_name, first_output = outputs[0]
        all_match = True
        for name, output in outputs[1:]:
            if output != first_output:
                print(f"FAILURE: {name} produces different output than {first_name}")
                print(f"{first_name} output (first 50): {repr(first_output[:50])}")
                print(f"{name} output (first 50): {repr(output[:50])}")
                print(f"{first_name} hex: {first_output[:50].encode('utf-8').hex()}")
                print(f"{name} hex: {output[:50].encode('utf-8').hex()}")
                all_match = False
        if all_match:
            print("SUCCESS: All implementations produce identical encoded output")
        assert all_match, "Not all implementations produce identical encoded output" 
        assert all_match, "Not all implementations produce identical encoded output" 