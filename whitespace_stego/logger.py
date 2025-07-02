"""Logger configuration for the whitespace_stego package."""

import logging
import sys
from typing import Optional


def setup_logger(
    name: str, level: Optional[int] = None, verbose: bool = False
) -> logging.Logger:
    """Set up a logger with the given name and level.

    Parameters
    ----------
    name : str
        The name of the logger.
    level : Optional[int]
        The logging level. If None, uses INFO.
    verbose : bool
        If True, output debug messages to stderr. If False, output to stdout.

    Returns
    -------
    logging.Logger
        The configured logger instance.
    """
    logger = logging.getLogger(name)

    if level is None:
        level = logging.INFO

    logger.setLevel(level)

    # Create console handler if none exists
    if not logger.handlers:
        # Always use stderr for all log output to avoid interfering with Click's stdout
        # Click handles user-facing output through click.echo() and click.secho()
        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(level)

        # Create formatter
        if verbose:
            # Debug format for verbose mode
            formatter = logging.Formatter("DEBUG: %(message)s")
        else:
            # Normal format for non-verbose mode
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

    return logger
