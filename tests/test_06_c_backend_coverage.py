"""Tests for C backend coverage to achieve 100% coverage."""

import pytest
import ctypes
import ctypes.util
import os
import sys
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path

from whitespace_stego.c_backend import (
    encode, decode, is_available, count_messages, 
    c_backend_available, _lib, _load_library
)


class TestCBackendLibraryLoading:
    """Test C backend library loading scenarios."""
    
    def test_load_library_with_ctypes_util_find_library(self):
        """Test _load_library when ctypes.util.find_library finds the library."""
        with patch('pathlib.Path.exists', return_value=False):
            with patch('ctypes.util.find_library') as mock_find_library:
                with patch('ctypes.CDLL') as mock_cdll:
                    mock_find_library.return_value = "/path/to/libwhitespace_stego.so"
                    mock_cdll.return_value = MagicMock()
                    
                    # Test the find_library path (lines 52-58)
                    result = _load_library()
                    
                    mock_find_library.assert_called_with("libwhitespace_stego.so")
                    mock_cdll.assert_called_with("/path/to/libwhitespace_stego.so")
                    assert result == mock_cdll.return_value
    
    def test_load_library_oserror_handling(self):
        """Test _load_library OSError handling (lines 64-67)."""
        with patch('pathlib.Path.exists', return_value=False):
            with patch('ctypes.util.find_library', return_value=None):
                with pytest.raises(OSError, match="Could not find libwhitespace_stego.so"):
                    _load_library()


class TestCBackendAvailability:
    """Test C backend availability scenarios."""
    
    def test_c_backend_unavailable_encoding(self):
        """Test encode when C backend is unavailable."""
        with patch('whitespace_stego.c_backend.c_backend_available', False):
            with pytest.raises(RuntimeError, match="C backend not available"):
                encode("test message", "test carrier")
    
    def test_c_backend_unavailable_decoding(self):
        """Test decode when C backend is unavailable."""
        with patch('whitespace_stego.c_backend.c_backend_available', False):
            with pytest.raises(ValueError, match="C backend not available"):
                decode("test carrier")
    
    def test_c_backend_unavailable_count_messages(self):
        """Test count_messages when C backend is unavailable."""
        with patch('whitespace_stego.c_backend.c_backend_available', False):
            with pytest.raises(RuntimeError, match="C backend not available"):
                count_messages("test carrier")


class TestCBackendErrorHandling:
    """Test C backend error handling scenarios."""
    
    def test_encode_with_c_library_error(self):
        """Test encode when C library returns error (line 138)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock the encode function to return False (error)
                mock_lib.whitespace_stego_encode.return_value = False
                mock_lib.whitespace_stego_last_error.return_value = b"Test error message"
                
                with pytest.raises(RuntimeError, match="Encoding failed: Test error message"):
                    encode("test message", "test carrier")
    
    def test_encode_with_unknown_error(self):
        """Test encode when C library returns error but no error message (line 162)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock the encode function to return False (error)
                mock_lib.whitespace_stego_encode.return_value = False
                mock_lib.whitespace_stego_last_error.return_value = None
                
                with pytest.raises(RuntimeError, match="Encoding failed: Unknown encoding error"):
                    encode("test message", "test carrier")
    
    def test_decode_all_with_no_messages_and_password(self):
        """Test decode when decode_all succeeds but returns 0 messages with password (lines 223-225)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock decode_all to succeed but return 0 messages
                mock_lib.whitespace_stego_decode_all.return_value = True
                
                # Mock result_count to be 0
                result_count = ctypes.c_size_t(0)
                
                with patch('ctypes.byref', return_value=result_count):
                    with pytest.raises(ValueError, match="Invalid password or no valid messages found"):
                        decode("test carrier", "wrong_password")
    
    def test_decode_all_with_no_messages_and_no_password(self):
        """Test decode when decode_all succeeds but returns 0 messages without password (lines 234, 244-249)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock decode_all to succeed but return 0 messages
                mock_lib.whitespace_stego_decode_all.return_value = True
                mock_lib.whitespace_stego_last_error.return_value = b"Test error message"
                
                # Mock result_count to be 0
                result_count = ctypes.c_size_t(0)
                
                with patch('ctypes.byref', return_value=result_count):
                    with pytest.raises(ValueError, match="Invalid carrier text: Test error message"):
                        decode("test carrier")
    
    def test_decode_all_with_unknown_error_no_password(self):
        """Test decode when decode_all succeeds but returns 0 messages without password and no error message."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock decode_all to succeed but return 0 messages
                mock_lib.whitespace_stego_decode_all.return_value = True
                mock_lib.whitespace_stego_last_error.return_value = None
                
                # Mock result_count to be 0
                result_count = ctypes.c_size_t(0)
                
                with patch('ctypes.byref', return_value=result_count):
                    with pytest.raises(ValueError, match="Invalid carrier text: No valid messages found in carrier text"):
                        decode("test carrier")
    
    def test_decode_single_with_error(self):
        """Test decode when single decode fails (lines 266, 270-275)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock decode_all to fail
                mock_lib.whitespace_stego_decode_all.return_value = False
                # Mock single decode to fail
                mock_lib.whitespace_stego_decode.return_value = False
                mock_lib.whitespace_stego_last_error.return_value = b"Test decode error"
                
                with pytest.raises(ValueError, match="Invalid carrier text: Test decode error"):
                    decode("test carrier")
    
    def test_decode_single_with_unknown_error(self):
        """Test decode when single decode fails with no error message."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            with patch('whitespace_stego.c_backend._lib') as mock_lib:
                # Mock decode_all to fail
                mock_lib.whitespace_stego_decode_all.return_value = False
                # Mock single decode to fail
                mock_lib.whitespace_stego_decode.return_value = False
                mock_lib.whitespace_stego_last_error.return_value = None
                
                with pytest.raises(ValueError, match="Invalid carrier text: Unknown decoding error"):
                    decode("test carrier")


class TestCBackendCountMessages:
    """Test C backend count_messages function."""
    
    def test_count_messages_basic(self):
        """Test count_messages with basic input (lines 305-314)."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            # Test with no markers
            assert count_messages("no markers here") == 0
            
            # Test with one complete pair (using correct markers: START_MARKER = "\ufeff", END_MARKER = "\u200c")
            assert count_messages("text\ufeff\u200c") == 1
            
            # Test with multiple pairs
            assert count_messages("text\ufeff\u200c\ufeff\u200c") == 2
            
            # Test with mismatched markers (should return minimum)
            assert count_messages("text\ufeff\ufeff\u200c") == 1  # 2 start, 1 end
    
    def test_count_messages_with_unicode_content(self):
        """Test count_messages with Unicode content."""
        with patch('whitespace_stego.c_backend.c_backend_available', True):
            # Test with Unicode content and markers
            unicode_text = "Hello 世界! \ufeff\u200c"
            assert count_messages(unicode_text) == 1


class TestCBackendIntegration:
    """Test C backend integration scenarios."""
    
    def test_is_available_function(self):
        """Test the is_available function."""
        # This should return the actual availability status
        result = is_available()
        assert isinstance(result, bool)
    
    def test_encode_decode_roundtrip_with_password(self):
        """Test encode/decode roundtrip with password."""
        if not c_backend_available:
            pytest.skip("C backend not available")
        
        message = "Secret message"
        carrier = "Public carrier text"
        password = "test_password"
        
        # Encode
        encoded = encode(message, carrier, password)
        assert encoded != carrier
        assert message in encoded or len(encoded) > len(carrier)
        
        # Decode
        decoded = decode(encoded, password)
        assert decoded == message
    
    def test_encode_decode_roundtrip_without_password(self):
        """Test encode/decode roundtrip without password."""
        if not c_backend_available:
            pytest.skip("C backend not available")
        
        message = "Public message"
        carrier = "Public carrier text"
        
        # Encode
        encoded = encode(message, carrier)
        assert encoded != carrier
        assert message in encoded or len(encoded) > len(carrier)
        
        # Decode
        decoded = decode(encoded)
        assert decoded == message 