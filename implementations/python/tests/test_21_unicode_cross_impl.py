import subprocess
import tempfile
import os
import pytest
from whitespace_stego.constants import START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT

BINARIES = {
    'python-cli': {
        'path': os.path.abspath('.venv/bin/whitespace-stego'),
        'backends': ['python', 'rust', 'c'],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, password, backend=None: 
            [bin_path, '-b', backend] + ['encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path, '-p', password] if backend else
            [bin_path, 'encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path, '-p', password],
        'decode_cmd': lambda bin_path, carrier_path, output_path, password, backend=None:
            [bin_path, '-b', backend] + ['decode', '--carrier-file', carrier_path, '-o', output_path, '-p', password] if backend else
            [bin_path, 'decode', '--carrier-file', carrier_path, '-o', output_path, '-p', password]
    },
    'py': {
        'path': os.path.abspath('bin/whitespace-stego-py'),
        'backends': ['python', 'rust', 'c'],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, password, backend=None: 
            [bin_path, '-b', backend] + ['encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path, '-p', password] if backend else
            [bin_path, 'encode', '-m', msg, '--carrier-file', carrier_path, '-o', output_path, '-p', password],
        'decode_cmd': lambda bin_path, carrier_path, output_path, password, backend=None:
            [bin_path, '-b', backend] + ['decode', '--carrier-file', carrier_path, '-o', output_path, '-p', password] if backend else
            [bin_path, 'decode', '--carrier-file', carrier_path, '-o', output_path, '-p', password]
    },
    'c': {
        'path': os.path.abspath('bin/whitespace-stego-c'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, password, backend=None: 
            [bin_path, 'encode', '--message-file', msg, '--carrier-file', carrier_path, '--output', output_path, '--password', password],
        'decode_cmd': lambda bin_path, carrier_path, output_path, password, backend=None:
            [bin_path, 'decode', '--carrier-file', carrier_path, '--output', output_path, '--password', password]
    },
    'go': {
        'path': os.path.abspath('bin/whitespace-stego-go'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, password, backend=None: 
            [bin_path, 'encode', '-m', msg, '-cf', carrier_path, '-o', output_path, '-p', password],
        'decode_cmd': lambda bin_path, carrier_path, output_path, password, backend=None:
            [bin_path, 'decode', '-cf', carrier_path, '-o', output_path, '-p', password]
    },
    'rs': {
        'path': os.path.abspath('bin/whitespace-stego-rs'),
        'backends': [None],
        'encode_cmd': lambda bin_path, msg, carrier_path, output_path, password, backend=None: 
            [bin_path, 'encode', '-m', msg, '--cf', carrier_path, '-o', output_path, '-p', password],
        'decode_cmd': lambda bin_path, carrier_path, output_path, password, backend=None:
            [bin_path, 'decode', '--cf', carrier_path, '-o', output_path, '-p', password]
    },
}

UNICODE_TESTS = [
    {
        'carrier': 'Hello 🌍 Привет мир こんにちは世界',
        'message': 'Secret 😎 сообщение テスト',
        'password': '🔑парольPa$$w0rd🌈',
    },
    {
        'carrier': '🚀✨🐍 Python is fun 漢字',
        'message': 'Emoji test: 😁😂🥰🤔',
        'password': '密码🔒',
    },
    {
        'carrier': 'Plain ASCII',
        'message': 'Unicode: üöäß 漢字',
        'password': 'simple',
    },
    {
        'carrier': 'Emojis everywhere 😁😂🥰🤔',
        'message': 'Carrier: こんにちは世界',
        'password': '🔑',
    },
]

# Generate all encode/decode methods
ALL_METHODS = []
for binary_name, binary_info in BINARIES.items():
    for backend in binary_info['backends']:
        ALL_METHODS.append((binary_name, backend))

@pytest.mark.parametrize('test_case', UNICODE_TESTS)
def test_unicode_cross_impl(test_case):
    """
    For each test case, encode with each implementation, then decode with all others.
    All should be able to decode each other's encoded message.
    """
    carrier = test_case['carrier']
    message = test_case['message']
    password = test_case['password']

    with tempfile.TemporaryDirectory() as tmpdir:
        carrier_path = os.path.join(tmpdir, 'carrier.txt')
        with open(carrier_path, 'w', encoding='utf-8') as f:
            f.write(carrier)
        # For C binary, message must be a file
        message_path = os.path.join(tmpdir, 'message.txt')
        with open(message_path, 'w', encoding='utf-8') as f:
            f.write(message)
        # Encode with each implementation
        encoded_files = {}
        for encoder_name, encoder_backend in ALL_METHODS:
            encoded_path = os.path.join(tmpdir, f'encoded_{encoder_name}_{encoder_backend}.txt')
            enc_bin = BINARIES[encoder_name]['path']
            if encoder_name == 'c':
                msg_arg = message_path
            else:
                msg_arg = message
            enc_cmd = BINARIES[encoder_name]['encode_cmd'](enc_bin, msg_arg, carrier_path, encoded_path, password, encoder_backend)
            print(f"Encoding with {encoder_name} (backend={encoder_backend}): {enc_cmd}")
            subprocess.run(enc_cmd, check=True)
            encoded_files[(encoder_name, encoder_backend)] = encoded_path
        # Now decode each encoded file with all implementations
        for (encoder_name, encoder_backend), encoded_path in encoded_files.items():
            for decoder_name, decoder_backend in ALL_METHODS:
                dec_bin = BINARIES[decoder_name]['path']
                decoded_path = os.path.join(tmpdir, f'decoded_{encoder_name}_{encoder_backend}_by_{decoder_name}_{decoder_backend}.txt')
                dec_cmd = BINARIES[decoder_name]['decode_cmd'](dec_bin, encoded_path, decoded_path, password, decoder_backend)
                print(f"Decoding {encoder_name} (backend={encoder_backend}) with {decoder_name} (backend={decoder_backend}): {dec_cmd}")
                subprocess.run(dec_cmd, check=True)
                with open(decoded_path, 'r', encoding='utf-8') as f:
                    decoded_message = f.read().strip()
                assert message == decoded_message, (
                    f"Decoded message mismatch\n"
                    f"Encoded by: {encoder_name} (backend={encoder_backend})\n"
                    f"Decoded by: {decoder_name} (backend={decoder_backend})\n"
                    f"Expected: {repr(message)}\n"
                    f"Got: {repr(decoded_message)}\n"
                ) 