"""Core implementation of whitespace steganography.

This module provides the core functionality for encoding and decoding messages
using zero-width Unicode whitespace characters.
"""

import base64
import logging
from typing import Optional, Tuple, List, Union
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
from cryptography.hazmat.primitives import padding

from .logger import setup_logger

# Create logger instance
logger = setup_logger(__name__)

# Zero-width characters for encoding
ZERO_BIT = "\u200b"  # Zero-width space
ONE_BIT = "\u200d"   # Zero-width joiner
START_MARKER = "\ufeff"  # Zero-width no-break space
END_MARKER = "\u200c"    # Zero-width non-joiner


def _encode_binary(data: bytes) -> str:
    """Encode binary data into zero-width characters.

    Parameters
    ----------
    data : bytes
        The binary data to encode.

    Returns
    -------
    str
        The encoded binary data as zero-width characters.
    """
    binary = "".join(format(b, "08b") for b in data)
    return "".join(ONE_BIT if bit == "1" else ZERO_BIT for bit in binary)


def _decode_binary(encoded: str) -> bytes:
    """Decode zero-width characters back to binary data.

    Parameters
    ----------
    encoded : str
        The encoded binary data as zero-width characters.

    Returns
    -------
    bytes
        The decoded binary data.
    """
    # Filter out only the zero-width characters we care about
    filtered_encoded = ''.join(char for char in encoded if char in (ZERO_BIT, ONE_BIT))
    
    binary = "".join("1" if char == ONE_BIT else "0" for char in filtered_encoded)
    
    # Ensure the binary string length is a multiple of 8
    if len(binary) % 8 != 0:
        logger.warning(f"Binary string length {len(binary)} is not a multiple of 8, truncating")
        binary = binary[:-(len(binary) % 8)]
    
    if not binary:
        raise ValueError("No valid binary data found")
    
    return bytes(int(binary[i : i + 8], 2) for i in range(0, len(binary), 8))


def derive_key(password: str) -> bytes:
    """Derive a 32-byte key from password (same as C implementation).
    
    Parameters
    ----------
    password : str
        The password to derive the key from.
        
    Returns
    -------
    bytes
        A 32-byte key derived from the password.
    """
    # Convert password to UTF-8 bytes and hash to get consistent 32-byte key
    import hashlib
    password_bytes = password.encode('utf-8')
    key_hash = hashlib.sha256(password_bytes).digest()
    return key_hash


def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using AES-256-CBC with PKCS7 padding (same as C/Rust implementation).
    
    Parameters
    ----------
    data : bytes
        The data to encrypt.
    password : str
        The password to use for encryption.
        
    Returns
    -------
    bytes
        The encrypted data (IV + ciphertext).
    """
    key = derive_key(password)
    
    # Generate random IV
    iv = os.urandom(16)
    
    # Create cipher with PKCS7 padding (same as C/Rust)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # PKCS7 padder
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Encrypt with automatic PKCS7 padding
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return IV + ciphertext
    return iv + ciphertext


def decrypt_data(data: bytes, password: str) -> bytes:
    """Decrypt data using AES-256-CBC with PKCS7 padding (same as C/Rust implementation).
    
    Parameters
    ----------
    data : bytes
        The encrypted data (IV + ciphertext).
    password : str
        The password to use for decryption.
        
    Returns
    -------
    bytes
        The decrypted data.
    """
    if len(data) < 16:
        raise ValueError("Invalid encrypted data")
    
    key = derive_key(password)
    
    # Extract IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Create cipher with PKCS7 padding (same as C/Rust)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt with automatic PKCS7 padding removal
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # PKCS7 unpadder
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    return data


def _count_message_pairs(carrier: str) -> int:
    """Count the number of start/end marker pairs in the carrier text.
    
    Parameters
    ----------
    carrier : str
        The carrier text to analyze.
        
    Returns
    -------
    int
        The number of complete start/end marker pairs found.
    """
    start_count = carrier.count(START_MARKER)
    end_count = carrier.count(END_MARKER)
    return min(start_count, end_count)


def _find_next_slot(carrier: str) -> int:
    """Find the next available slot for encoding a message.
    
    The algorithm places messages in slots between characters of the original carrier string, skipping over already-encoded messages.
    - First message goes between characters 0 and 1
    - Second message goes between characters 1 and 2
    - And so on until the last character
    - Remaining messages go before the last visible character
    
    Parameters
    ----------
    carrier : str
        The carrier text to find a slot in.
        
    Returns
    -------
    int
        The position where the next message should be inserted.
    """
    # Remove all encoded messages to get the original carrier
    import re
    pattern = re.compile(f"{START_MARKER}.*?{END_MARKER}")
    cleaned_carrier = pattern.sub("", carrier)
    
    # Count how many messages are already encoded
    existing_messages = _count_message_pairs(carrier)
    logger.debug(f"Found {existing_messages} existing messages in carrier")
    
    # If no existing messages, place after first character
    if existing_messages == 0:
        position = 1 if len(cleaned_carrier) > 1 else 0
        logger.debug(f"No existing messages, placing at position {position}")
        return position
    
    # For subsequent messages, place in slots between characters
    # until we reach the last character, then place before the last character
    if existing_messages < len(cleaned_carrier) - 1:
        position = existing_messages + 1
        logger.debug(f"Placing message {existing_messages + 1} at position {position}")
        return position
    else:
        # Place before the last visible character
        position = len(cleaned_carrier) - 1
        logger.debug(f"Placing message {existing_messages + 1} before last character at position {position}")
        return position


def _insert_message_at_position(carrier: str, encoded_message: str, position: int) -> str:
    """Insert an encoded message at a specific position in the original carrier, skipping over already-encoded messages.
    
    Parameters
    ----------
    carrier : str
        The carrier text (may already contain encoded messages).
    encoded_message : str
        The encoded message to insert.
    position : int
        The position to insert the message at (in the original carrier, not counting encoded messages).
        
    Returns
    -------
    str
        The carrier text with the message inserted.
    """
    import re
    # Remove all encoded messages to get the original carrier
    pattern = re.compile(f"{START_MARKER}.*?{END_MARKER}")
    cleaned_carrier = pattern.sub("", carrier)
    
    # Insert the encoded message at the correct position in the cleaned carrier
    if position == 0:
        new_carrier = encoded_message + cleaned_carrier
    elif position >= len(cleaned_carrier):
        new_carrier = cleaned_carrier + encoded_message
    else:
        new_carrier = cleaned_carrier[:position] + encoded_message + cleaned_carrier[position:]
    
    # Now, re-insert all previously encoded messages at their original positions in the original carrier
    # We'll scan the original carrier and for each encoded message, insert it at the same index as before
    # (relative to the cleaned carrier)
    result = new_carrier
    matches = list(pattern.finditer(carrier))
    offset = 0
    for match in matches:
        # Find the position in the cleaned carrier where this encoded message was originally
        # This is the number of non-encoded characters before the match.start()
        pre = carrier[:match.start()]
        cleaned_pre = pattern.sub("", pre)
        insert_pos = len(cleaned_pre) + offset
        result = result[:insert_pos] + match.group(0) + result[insert_pos:]
        offset += len(match.group(0))
    return result


def encode(message: str, carrier: str = "", password: Optional[str] = None) -> str:
    """Encode a message into a carrier text using zero-width characters.

    Parameters
    ----------
    message : str
        The message to encode.
    carrier : str, optional
        The carrier text to embed the message in. If empty, returns just the encoded message.
    password : str, optional
        Optional password for encryption.

    Returns
    -------
    str
        The carrier text with the encoded message embedded.
    """
    # Check for empty message with humorous error
    if not message:
        raise ValueError("🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!")
    
    logger.debug("Encoding message: %s", message)
    logger.debug("Using carrier: %s", carrier)
    if password:
        logger.debug("Using password protection")

    # Base64 encode the message
    encoded = base64.b64encode(message.encode("utf-8"))

    # Add password encryption if provided
    if password:
        logger.debug("Using password protection")
        encoded = encrypt_data(encoded, password)

    # Convert to zero-width characters
    zero_width = _encode_binary(encoded)

    # Add markers
    encoded_message = START_MARKER + zero_width + END_MARKER

    # Return just the encoded message if no carrier
    if not carrier:
        logger.info("Message encoded successfully")
        return encoded_message

    # Find the next available slot for this message
    slot_position = _find_next_slot(carrier)
    
    # Insert the message at the appropriate position
    result = _insert_message_at_position(carrier, encoded_message, slot_position)

    logger.info("Message encoded successfully at position %d", slot_position)
    return result


class BadPasswordError(ValueError):
    """Raised when a password was only able to decode part of the secret message.
    
    This allows for multi-recipient scenarios where each recipient can decode
    their intended message while other messages remain encrypted.
    """
    pass


def decode(carrier: str, password: Optional[str] = None) -> Union[str, List[str]]:
    """Decode messages from carrier text containing zero-width characters.

    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded messages.
    password : str, optional
        Optional password for decryption.

    Returns
    -------
    Union[str, List[str]]
        A single decoded message as string, or a list of decoded messages if multiple.

    Raises
    ------
    ValueError
        If no valid message is found in the carrier text.
    BadPasswordError
        If the password was only able to decode part of the secret message.
        This allows for multi-recipient scenarios where each recipient can decode
        their intended message while other messages remain encrypted.
    """
    logger.debug("Decoding messages from text: %s", carrier)
    if password:
        logger.debug("Using password protection")

    messages = []
    decryption_failures = 0
    
    # Find all start and end markers
    start_positions = []
    end_positions = []
    
    pos = 0
    while True:
        start = carrier.find(START_MARKER, pos)
        if start == -1:
            break
        start_positions.append(start)
        pos = start + 1
    
    pos = 0
    while True:
        end = carrier.find(END_MARKER, pos)
        if end == -1:
            break
        end_positions.append(end)
        pos = end + 1
    
    logger.debug(f"Found {len(start_positions)} start markers and {len(end_positions)} end markers")
    
    # Match start and end markers to extract messages
    start_idx = 0
    end_idx = 0
    
    while start_idx < len(start_positions) and end_idx < len(end_positions):
        start_pos = start_positions[start_idx]
        end_pos = end_positions[end_idx]
        
        # Find the next valid pair (end after start)
        if end_pos <= start_pos:
            end_idx += 1
            continue
        
        # Extract the encoded message
        encoded = carrier[start_pos + len(START_MARKER) : end_pos]
        
        logger.debug(f"Processing message {len(messages) + 1}: start={start_pos}, end={end_pos}, length={len(encoded)}")
        
        try:
            # Convert zero-width characters back to binary
            data = _decode_binary(encoded)

            # Decrypt if password provided
            if password:
                try:
                    data = decrypt_data(data, password)
                except Exception as e:
                    logger.warning("Failed to decrypt message: %s", e)
                    decryption_failures += 1
                    # Skip this message and continue with the next one
                    start_idx += 1
                    end_idx += 1
                    continue

            # Base64 decode and convert to string
            decoded_message = base64.b64decode(data).decode("utf-8")
            messages.append(decoded_message)
            logger.debug("Successfully decoded message: %s", decoded_message)
            
        except Exception as e:
            logger.warning("Failed to decode message: %s", e)
            decryption_failures += 1
        
        # Move to next pair
        start_idx += 1
        end_idx += 1
    
    # If we have a password and some messages failed to decrypt, but we successfully decrypted at least one,
    # this is a partial decode scenario (multi-recipient)
    if password and decryption_failures > 0 and len(messages) > 0:
        logger.info("Partial decode: %d messages decrypted, %d failed", len(messages), decryption_failures)
        # Return only the successfully decrypted messages
        if len(messages) == 1:
            return messages[0]
        else:
            return messages
    
    # If we have a password and no messages were decrypted, raise BadPasswordError
    if password and len(messages) == 0:
        raise BadPasswordError("Password was only able to decode part of the secret message.")
    
    # If no messages found at all, raise ValueError
    if not messages:
        raise ValueError("No valid messages found in carrier text")
    
    logger.info("Successfully decoded %d messages", len(messages))
    
    # Return string for single message, list for multiple messages
    if len(messages) == 1:
        return messages[0]
    else:
        return messages


def extract_encoded(carrier: str) -> Tuple[str, str]:
    """Extract the encoded message and remaining carrier text.

    Parameters
    ----------
    carrier : str
        The carrier text containing the encoded message.

    Returns
    -------
    Tuple[str, str]
        A tuple containing (encoded_message, remaining_carrier)

    Raises
    ------
    ValueError
        If no valid message is found in the carrier text.
    """
    start = carrier.find(START_MARKER)
    end = carrier.find(END_MARKER)

    if start == -1 or end == -1:
        raise ValueError("No valid message found in carrier text")

    encoded = carrier[start : end + len(END_MARKER)]
    remaining = carrier[:start] + carrier[end + len(END_MARKER) :]

    return encoded, remaining


def has_encoded_message(text: str) -> bool:
    """Check if text contains an encoded message.

    This function checks if the text contains both the start and end markers
    that indicate the presence of an encoded message using zero-width characters.

    Parameters
    ----------
    text : str
        The text to check for encoded messages.

    Returns
    -------
    bool
        True if the text contains both start and end markers, False otherwise.
    """
    return START_MARKER in text and END_MARKER in text


def get_encoded_message_size(text: str) -> Optional[int]:
    """Get the size of an encoded message in bytes.

    This function extracts the encoded message and calculates its size in bytes.
    Note that this is the size of the encoded data, not the original message.

    Parameters
    ----------
    text : str
        The text containing the encoded message.

    Returns
    -------
    Optional[int]
        The size of the encoded message in bytes, or None if no message found.
    """
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    
    if start == -1 or end == -1 or end <= start:
        return None
    
    # Extract the encoded data between markers
    encoded = text[start + len(START_MARKER):end]
    
    # Count only the zero-width characters (ZERO_BIT and ONE_BIT)
    zero_width_count = sum(1 for char in encoded if char in (ZERO_BIT, ONE_BIT))
    
    # Each byte is encoded as 8 zero-width characters
    return zero_width_count // 8 if zero_width_count > 0 else None
