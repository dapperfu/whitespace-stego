"""Encoding functions for whitespace steganography."""

import base64
from typing import Optional

from whitespace_stego.errors import EncodingError

# Unicode control characters
CONTROL_START = "\u2060"  # U+2060 Word Joiner
CONTROL_END = "\u2063"  # U+2063 Invisible Separator
BIT_0 = "\u200B"  # U+200B Zero Width Space
BIT_1 = "\u200C"  # U+200C Zero Width Non-Joiner


def encode(message: str, carrier: Optional[str] = None) -> str:
    """Encode a message into invisible Unicode characters.

    Args:
        message: The message to encode. Can be any Unicode string.
        carrier: Optional carrier text to embed the encoded message in.
                 If provided, the encoded payload will be inserted after
                 the first character of the carrier text.

    Returns:
        A string containing the encoded message wrapped in control markers.
        If carrier is provided, returns carrier text with encoded message embedded.

    Raises:
        EncodingError: If encoding fails for any reason.
    """
    try:
        # Convert message to UTF-8 bytes
        utf8_bytes = message.encode("utf-8")

        # Encode to Base64
        base64_str = base64.b64encode(utf8_bytes).decode("ascii")

        # Convert Base64 string to binary representation
        binary_bits = ""
        for char in base64_str:
            # Convert each character to 8-bit binary (MSB to LSB)
            binary_bits += format(ord(char), "08b")

        # Map binary bits to invisible Unicode characters
        encoded_payload = ""
        for bit in binary_bits:
            if bit == "0":
                encoded_payload += BIT_0
            elif bit == "1":
                encoded_payload += BIT_1
            else:
                raise EncodingError(f"Invalid bit value: {bit}")

        # Wrap payload with control markers
        encoded_message = CONTROL_START + encoded_payload + CONTROL_END

        # If carrier text is provided, embed the encoded message
        if carrier is not None:
            # Check if carrier contains control characters
            if CONTROL_START in carrier or CONTROL_END in carrier:
                raise EncodingError(
                    "Carrier text contains control characters. "
                    "This may cause decoding issues."
                )
            if len(carrier) > 0:
                # Insert after first character
                return carrier[0] + encoded_message + carrier[1:]
            else:
                # Empty carrier, return just encoded message
                return encoded_message

        return encoded_message

    except Exception as e:
        if isinstance(e, EncodingError):
            raise
        raise EncodingError(f"Encoding failed: {str(e)}") from e

