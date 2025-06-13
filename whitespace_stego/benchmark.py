"""Benchmark utilities for whitespace-stego.

This module provides functions for benchmarking encryption and compression operations.
"""

import time
import os
from typing import Dict, Union
from . import crypto, encode, decode

def benchmark_encryption(file_path: str) -> Dict[str, Union[float, int]]:
    """Benchmark encryption and decryption operations on a file.
    
    Parameters
    ----------
    file_path : str
        Path to the file to benchmark.
        
    Returns
    -------
    Dict[str, Union[float, int]]
        Dictionary containing benchmark results:
        - encryption_time: Time taken to encrypt (seconds)
        - decryption_time: Time taken to decrypt (seconds)
        - compression_ratio: Ratio of original size to encrypted size
        - message_size: Size of original message in bytes
        - stego_size: Size of encrypted message in bytes
    """
    # Read the file
    with open(file_path, 'rb') as f:
        message = f.read().decode()
    
    # Get original size
    message_size = len(message.encode())
    
    # Benchmark encryption
    start_time = time.time()
    encrypted = crypto.encrypt_message(message, "benchmark_password")
    encryption_time = time.time() - start_time
    
    # Get encrypted size
    stego_size = len(encrypted.encode())
    
    # Benchmark decryption
    start_time = time.time()
    decrypted = crypto.decrypt_message(encrypted, "benchmark_password")
    decryption_time = time.time() - start_time
    
    # Calculate compression ratio
    compression_ratio = message_size / stego_size if stego_size > 0 else 0
    
    return {
        'encryption_time': encryption_time,
        'decryption_time': decryption_time,
        'compression_ratio': compression_ratio,
        'message_size': message_size,
        'stego_size': stego_size
    }

def benchmark_compression(file_path: str) -> Dict[str, Union[float, int]]:
    """Benchmark compression operations on a file.
    
    Parameters
    ----------
    file_path : str
        Path to the file to benchmark.
        
    Returns
    -------
    Dict[str, Union[float, int]]
        Dictionary containing benchmark results:
        - original_size: Size of original file in bytes
        - compressed_size: Size of compressed file in bytes
        - compression_ratio: Ratio of original size to compressed size
        - compression_time: Time taken to compress (seconds)
    """
    # Read the file
    with open(file_path, 'rb') as f:
        message = f.read().decode()
    
    # Get original size
    original_size = len(message.encode())
    
    # Benchmark compression (using encode as a simple compression)
    start_time = time.time()
    encoded = encode.encode_message(message)
    compression_time = time.time() - start_time
    
    # Get compressed size
    compressed_size = len(encoded.encode())
    
    # Calculate compression ratio
    compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
    
    return {
        'original_size': original_size,
        'compressed_size': compressed_size,
        'compression_ratio': compression_ratio,
        'compression_time': compression_time
    } 