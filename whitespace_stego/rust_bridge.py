"""Python bridge to the Rust backend."""

from typing import Optional

try:
    from whitespace_stego_rs import encode_rs, decode_rs
except ImportError:
    raise ImportError(
        "Rust backend not found. Please install it with 'cd rust_py_backend && maturin develop'"
    )

def encode(message: str, carrier: str, password: Optional[str] = None) -> str:
    """Encode a message using the Rust backend.
    
    Args:
        message: The message to encode
        carrier: The carrier text to embed the message in
        password: Optional password for encryption
        
    Returns:
        The carrier text with the encoded message embedded
    """
    return encode_rs(message, carrier, password)

def decode(carrier: str, password: Optional[str] = None) -> str:
    """Decode a message using the Rust backend.
    
    Args:
        carrier: The carrier text containing the encoded message
        password: Optional password for decryption
        
    Returns:
        The decoded message
        
    Raises:
        ValueError: If no valid message is found in the carrier
    """
    return decode_rs(carrier, password) 