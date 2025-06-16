"""Pytest configuration and fixtures."""

import logging
import pytest
from whitespace_stego.logger import setup_logger

@pytest.fixture(scope="session")
def debug_logger():
    """Create a debug logger for tests."""
    return setup_logger("test", logging.DEBUG)

@pytest.fixture(autouse=True)
def setup_test_logging(debug_logger):
    """Set up logging for each test."""
    yield
    # Clean up logging after each test
    for handler in debug_logger.handlers[:]:
        debug_logger.removeHandler(handler) 