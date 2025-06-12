"""Character set definitions and utilities for whitespace steganography.

This module defines the Unicode characters used for zero-width steganography
and provides utility functions for character mapping and validation.
"""

from typing import Dict, Tuple, Final

# Unicode control characters for message framing
START_MARKER: Final[str] = "\u2060"  # Word Joiner
END_MARKER: Final[str] = "\u2061"    # Function Application

# Binary encoding characters
ZWSP: Final[str] = "\u200B"  # Zero-Width Space (bit 0)
ZWNJ: Final[str] = "\u200C"  # Zero-Width Non-Joiner (bit 1)

# Mapping between binary values and zero-width characters
BINARY_TO_CHAR: Final[Dict[int, str]] = {
    0: ZWSP,
    1: ZWNJ
}

# Reverse mapping for decoding
CHAR_TO_BINARY: Final[Dict[str, int]] = {
    ZWSP: 0,
    ZWNJ: 1
}

def is_valid_carrier(text: str) -> bool:
    """Check if the carrier text is valid for steganography.
    
    Parameters
    ----------
    text : str
        The carrier text to validate.
        
    Returns
    -------
    bool
        True if the text is valid, False otherwise.
        
    Notes
    -----
    A valid carrier text should not contain any of our control characters
    to avoid conflicts with the steganographic encoding.
    """
    return not any(char in text for char in (START_MARKER, END_MARKER, ZWSP, ZWNJ))

def get_control_chars() -> Tuple[str, str]:
    """Get the start and end control characters.
    
    Returns
    -------
    Tuple[str, str]
        A tuple containing (start_marker, end_marker)
    """
    return START_MARKER, END_MARKER

def get_binary_chars() -> Tuple[str, str]:
    """Get the binary encoding characters.
    
    Returns
    -------
    Tuple[str, str]
        A tuple containing (zero_width_space, zero_width_non_joiner)
    """
    return ZWSP, ZWNJ

def strip_zero_width_and_control(text: str) -> str:
    """Remove all zero-width and control characters used for steganography from the text.
    
    Parameters
    ----------
    text : str
        The text to clean.
    
    Returns
    -------
    str
        The cleaned text with all stego control and zero-width characters removed.
    """
    for char in (START_MARKER, END_MARKER, ZWSP, ZWNJ):
        text = text.replace(char, "")
    return text 