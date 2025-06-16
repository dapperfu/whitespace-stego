"""Logger configuration for the whitespace_stego package."""

import logging
import sys
from typing import Optional

def setup_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """Set up a logger with the given name and level.
    
    Parameters
    ----------
    name : str
        The name of the logger.
    level : Optional[int]
        The logging level. If None, uses INFO.
        
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
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
    
    return logger 