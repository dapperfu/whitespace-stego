"""
Test 41: Protocol and Constants

This test suite checks protocol invariants, marker uniqueness, bit encoding, and cross-language constant agreement.
"""

import pytest
from whitespace_stego.constants import ZWSP, ZWJ, ZWNJ, ZWNBSP, ZERO_BIT, ONE_BIT, START_MARKER, END_MARKER, BITS_PER_CHAR

class TestProtocolConstants:
    def test_marker_uniqueness(self):
        markers = {ZWSP, ZWJ, ZWNJ, ZWNBSP}
        assert len(markers) == 4
        assert len({ZERO_BIT, ONE_BIT, START_MARKER, END_MARKER}) == 4
    def test_bit_encoding(self):
        assert ZERO_BIT != ONE_BIT
        assert START_MARKER != END_MARKER
        assert isinstance(ZERO_BIT, str)
        assert isinstance(ONE_BIT, str)
    def test_bits_per_char(self):
        assert BITS_PER_CHAR == 8
    def test_cross_language_constants(self):
        # These values must match C/Rust/Go implementations
        assert ZWSP == "\u200b"
        assert ZWJ == "\u200d"
        assert ZWNJ == "\u200c"
        assert ZWNBSP == "\ufeff"
        assert ZERO_BIT == ZWSP
        assert ONE_BIT == ZWJ
        assert START_MARKER == ZWNBSP
        assert END_MARKER == ZWNJ 