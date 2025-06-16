import pytest
from test_data import MESSAGES, CARRIERS, PASSWORDS

# Dummy function stubs (replace with actual encoder/decoder functions)
def encode_python(message, carrier, password=None):
    return f"<encoded:{message}:{carrier}:{password}>"

def decode_python(encoded, password=None):
    # Extract message from encoded string
    parts = encoded.split(":")
    if len(parts) >= 2:
        return parts[1]
    return None

def encode_rust(message, carrier, password=None):
    return f"<rust_encoded:{message}:{carrier}:{password}>"

def decode_rust(encoded, password=None):
    # Extract message from encoded string
    parts = encoded.split(":")
    if len(parts) >= 2:
        return parts[1]
    return None

@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_roundtrip_python_to_rust(message, carrier, password):
    encoded = encode_python(message, carrier, password)
    decoded = decode_rust(encoded, password)
    assert decoded == message

@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_roundtrip_rust_to_python(message, carrier, password):
    encoded = encode_rust(message, carrier, password)
    decoded = decode_python(encoded, password)
    assert decoded == message
