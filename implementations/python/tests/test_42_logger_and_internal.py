"""
Test 42: Logger and Internal Helpers

This test suite covers logger setup and all private/internal helpers in core.py.
"""

import pytest
from whitespace_stego.logger import setup_logger
from whitespace_stego import core

class TestLogger:
    def test_logger_basic(self):
        logger = setup_logger("test_logger")
        assert logger.name == "test_logger"
        logger2 = setup_logger("test_logger", verbose=True)
        assert logger2.name == "test_logger"

class TestInternalHelpers:
    def test_encode_decode_binary(self):
        data = b"abc"
        zw = core._encode_binary(data)
        out = core._decode_binary(zw)
        assert out == data
    def test_count_message_pairs(self):
        carrier = "A" + core.START_MARKER + core._encode_binary(b"x") + core.END_MARKER + "B"
        assert core._count_message_pairs(carrier) == 1
    def test_find_next_slot(self):
        carrier = "ABCD"
        slot = core._find_next_slot(carrier)
        assert isinstance(slot, int)
    def test_insert_message_at_position(self):
        carrier = "ABCD"
        emsg = core.START_MARKER + core._encode_binary(b"x") + core.END_MARKER
        inserted = core._insert_message_at_position(carrier, emsg, 2)
        assert emsg in inserted 