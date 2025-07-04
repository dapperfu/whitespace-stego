"""Logger configuration for the whitespace_stego package."""

import logging
import sys
from typing import Optional


def setup_logger(name: str, level=logging.INFO, verbose=False):
    """
    Set up a logger with the given name and level.

    Parameters
    ----------
    name : str
        Logger name.
    level : int, optional
        Logging level (default: logging.INFO).
    verbose : bool, optional
        If True, use verbose format (default: False).

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s' if verbose else '%(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
