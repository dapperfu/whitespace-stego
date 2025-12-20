"""Decoding functions for whitespace steganography."""

import base64
from typing import Optional

from whitespace_stego.errors import (
    DecodingError,
    MissingMarkerError,
    InvalidPayloadError,
    InvalidBase64Error,
    InvalidUTF8Error,
)

# Unicode control characters
CONTROL_START = "\u2060"  # U+2060 Word Joiner
CONTROL_END = "\u2063"  # U+2063 Invisible Separator
BIT_0 = "\u200B"  # U+200B Zero Width Space
BIT_1 = "\u200C"  # U+200C Zero Width Non-Joiner


def decode(encoded_text: str, password: Optional[str] = None) -> str:
    """Decode a message from invisible Unicode characters.

    Args:
        encoded_text: Text containing the encoded message with control markers.
        password: Optional password for XOR decryption. If provided, the
                 message will be decrypted after Base64 decoding.

    Returns:
        The decoded original message string.

    Raises:
        MissingMarkerError: If CONTROL_START or CONTROL_END markers are missing.
        InvalidPayloadError: If payload contains invalid characters.
        InvalidBase64Error: If Base64 decoding fails.
        InvalidUTF8Error: If UTF-8 decoding fails.
        DecodingError: For other decoding errors.
    """
    try:
        # Find control markers
        start_idx = encoded_text.find(CONTROL_START)
        end_idx = encoded_text.find(CONTROL_END)

        # Check for missing markers
        if start_idx == -1:
            raise MissingMarkerError("CONTROL_START marker (U+2060) not found")
        if end_idx == -1:
            raise MissingMarkerError("CONTROL_END marker (U+2063) not found")

        # Extract payload (between markers, excluding markers)
        payload_start = start_idx + len(CONTROL_START)
        payload = encoded_text[payload_start:end_idx]

        # Check if payload is empty
        if len(payload) == 0:
            # Empty payload means empty message
            return ""

        # Convert invisible characters to binary bits
        binary_bits = ""
        for char in payload:
            if char == BIT_0:
                binary_bits += "0"
            elif char == BIT_1:
                binary_bits += "1"
            else:
                raise InvalidPayloadError(
                    f"Invalid character in payload: U+{ord(char):04X}. "
                    "Only U+200B and U+200C are allowed."
                )

        # Check if payload is complete (divisible by 8)
        if len(binary_bits) % 8 != 0:
            raise DecodingError(
                f"Incomplete payload: {len(binary_bits)} bits "
                "(must be divisible by 8)"
            )

        # Group bits into 8-bit bytes
        bytes_list = []
        for i in range(0, len(binary_bits), 8):
            byte_bits = binary_bits[i : i + 8]
            byte_value = int(byte_bits, 2)
            bytes_list.append(byte_value)

        # Convert bytes to Base64 string
        base64_bytes = bytes(bytes_list)
        try:
            base64_str = base64_bytes.decode("ascii")
        except UnicodeDecodeError as e:
            raise InvalidBase64Error(f"Invalid Base64 data: {str(e)}") from e

        # Decode Base64 to UTF-8 bytes
        try:
            utf8_bytes = base64.b64decode(base64_str)
        except Exception as e:
            raise InvalidBase64Error(f"Base64 decoding failed: {str(e)}") from e

        # Apply XOR decryption if password is provided
        if password is not None:
            password_bytes = password.encode("utf-8")
            if len(password_bytes) == 0:
                raise DecodingError("Password cannot be empty")
            # Derive key by repeating password bytes cyclically
            key = (password_bytes * ((len(utf8_bytes) // len(password_bytes)) + 1))[:len(utf8_bytes)]
            # XOR decrypt each byte
            utf8_bytes = bytes(a ^ b for a, b in zip(utf8_bytes, key))

        # Decode UTF-8 bytes to original message
        try:
            message = utf8_bytes.decode("utf-8")
        except UnicodeDecodeError as e:
            raise InvalidUTF8Error(f"UTF-8 decoding failed: {str(e)}") from e

        return message

    except DecodingError:
        raise
    except Exception as e:
        raise DecodingError(f"Decoding failed: {str(e)}") from e

