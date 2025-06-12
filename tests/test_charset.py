"""Tests for the charset module.

This module contains tests for character set definitions and utilities.
"""

import pytest
from whitespace_stego.common.charset import (
    START_MARKER,
    END_MARKER,
    ZWSP,
    ZWNJ,
    is_valid_carrier,
    get_control_chars,
    get_binary_chars
)

def test_is_valid_carrier() -> None:
    """Test carrier text validation."""
    # Valid carrier text
    assert is_valid_carrier("Hello, world!")
    assert is_valid_carrier("こんにちは")
    assert is_valid_carrier("👋🌍")
    
    # Invalid carrier text (contains control characters)
    assert not is_valid_carrier(f"Hello{START_MARKER}world")
    assert not is_valid_carrier(f"Hello{END_MARKER}world")
    assert not is_valid_carrier(f"Hello{ZWSP}world")
    assert not is_valid_carrier(f"Hello{ZWNJ}world")
    
    # Invalid carrier text (contains multiple control characters)
    assert not is_valid_carrier(f"Hello{START_MARKER}world{END_MARKER}!")
    assert not is_valid_carrier(f"Hello{ZWSP}world{ZWNJ}!")

def test_get_control_chars() -> None:
    """Test getting control characters."""
    start, end = get_control_chars()
    assert start == START_MARKER
    assert end == END_MARKER

def test_get_binary_chars() -> None:
    """Test getting binary encoding characters."""
    zwsp, zwnj = get_binary_chars()
    assert zwsp == ZWSP
    assert zwnj == ZWNJ 