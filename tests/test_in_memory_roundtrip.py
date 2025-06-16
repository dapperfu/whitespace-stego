import pytest
from test_data import MESSAGES, CARRIERS, PASSWORDS
from whitespace_stego.core import encode as encode_python, decode as decode_python
from whitespace_stego_backend.whitespace_stego_backend import encode as encode_rust, decode as decode_rust


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_roundtrip_python_to_rust(message: str, carrier: str, password: str | None) -> None:
    """Test roundtrip encoding with Python and decoding with Rust.
    
    Parameters
    ----------
    message : str
        The message to encode/decode
    carrier : str
        The carrier text to use
    password : str | None
        Optional password for encryption
    """
    encoded = encode_python(message, carrier, password)
    decoded = decode_rust(encoded, password)
    assert decoded == message


@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("carrier", CARRIERS)
@pytest.mark.parametrize("password", PASSWORDS)
def test_roundtrip_rust_to_python(message: str, carrier: str, password: str | None) -> None:
    """Test roundtrip encoding with Rust and decoding with Python.
    
    Parameters
    ----------
    message : str
        The message to encode/decode
    carrier : str
        The carrier text to use
    password : str | None
        Optional password for encryption
    """
    encoded = encode_rust(message, carrier, password)
    decoded = decode_python(encoded, password)
    assert decoded == message
