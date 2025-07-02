"""Comprehensive tests for the whitespace steganography encode module."""

import pytest
from unittest.mock import patch, MagicMock
from whitespace_stego.encode import (
    encode_message,
    _encode_python,
    ZWSP,
    ZWJ,
    ZWNJ,
    ZWNBSP,
    START_MARKER,
    END_MARKER,
    ZERO_BIT,
    ONE_BIT,
)


@pytest.fixture
def sample_message():
    """Sample message for testing."""
    return "Hello, World!"


@pytest.fixture
def sample_carrier():
    """Sample carrier text for testing."""
    return "This is a test carrier text."


@pytest.fixture
def sample_password():
    """Sample password for testing."""
    return "secret123"


@pytest.fixture
def click_context():
    """Mock click context for testing."""
    ctx = MagicMock()
    ctx.obj = {"backend": "python"}
    return ctx


class TestEncodeMessage:
    """Test the encode_message function."""

    def test_encode_message_python_backend(self, sample_message, sample_carrier, click_context):
        """
        Test that encode_message correctly uses the python backend.
        """
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "encoded_text"
                result = encode_message(sample_message, sample_carrier)
                assert result == "encoded_text"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)



    def test_encode_message_default_backend(self, sample_message, sample_carrier, click_context):
        """
        Test that encode_message defaults to python backend when no backend is specified.
        """
        click_context.obj = {}  # No backend specified
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "default_encoded"
                result = encode_message(sample_message, sample_carrier)
                assert result == "default_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)

    def test_encode_message_with_password(self, sample_message, sample_carrier, sample_password, click_context):
        """
        Test that encode_message correctly passes password to the backend.
        """
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "password_encoded"
                result = encode_message(sample_message, sample_carrier, sample_password)
                assert result == "password_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, sample_password)

    def test_encode_message_unknown_backend(self, sample_message, sample_carrier, click_context):
        """
        Test that encode_message raises ValueError for unknown backends.
        """
        click_context.obj["backend"] = "unknown_backend"
        with patch('click.get_current_context', return_value=click_context):
            with pytest.raises(ValueError, match="Unknown backend: unknown_backend"):
                encode_message(sample_message, sample_carrier)

    def test_encode_message_no_click_context(self, sample_message, sample_carrier):
        """
        Test that encode_message works when no click context is available.
        """
        with patch('click.get_current_context', side_effect=RuntimeError("No context")):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "no_context_encoded"
                result = encode_message(sample_message, sample_carrier)
                assert result == "no_context_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)

    def test_encode_message_empty_carrier(self, sample_message, click_context):
        """
        Test that encode_message works with empty carrier text.
        """
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "empty_carrier_encoded"
                result = encode_message(sample_message, "")
                assert result == "empty_carrier_encoded"
                mock_core_encode.assert_called_once_with(sample_message, "", None)

    def test_encode_message_empty_message(self, sample_carrier, click_context):
        """
        Test that encode_message works with empty message.
        """
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "empty_message_encoded"
                result = encode_message("", sample_carrier)
                assert result == "empty_message_encoded"
                mock_core_encode.assert_called_once_with("", sample_carrier, None)

    def test_encode_message_unicode_content(self, click_context):
        """
        Test that encode_message works with Unicode content.
        """
        click_context.obj["backend"] = "python"
        unicode_message = "Hello 世界! 🌍"
        unicode_carrier = "Carrier with émojis 🚀"
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "unicode_encoded"
                result = encode_message(unicode_message, unicode_carrier)
                assert result == "unicode_encoded"
                mock_core_encode.assert_called_once_with(unicode_message, unicode_carrier, None)


class TestEncodePython:
    """Test the _encode_python function."""

    @pytest.mark.parametrize("message,carrier,password,expected_result", [
        ("test", "carrier", None, "encoded_no_password"),
        ("test", "carrier", "password", "encoded_with_password"),
        ("test", "carrier", "", "encoded_empty_password"),
        ("", "carrier", None, "encoded_empty_message"),
        ("test", "", None, "encoded_empty_carrier"),
    ])
    def test_encode_python_calls_core_encode(self, message, carrier, password, expected_result):
        """
        Test that _encode_python correctly calls core_encode with the right parameters.
        
        Args:
            message: The message to encode
            carrier: The carrier text
            password: The password to use for encryption
            expected_result: The expected result from core_encode
        """
        with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
            mock_core_encode.return_value = expected_result
            result = _encode_python(message, carrier, password)
            assert result == expected_result
            mock_core_encode.assert_called_once_with(message, carrier, password)

    def test_encode_python_return_type(self):
        """
        Test that _encode_python returns the correct type (string).
        """
        with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
            mock_core_encode.return_value = "encoded_string"
            result = _encode_python("test", "carrier")
            assert isinstance(result, str)
            assert result == "encoded_string"


class TestConstants:
    """Test that all constants are correctly defined."""

    @pytest.mark.parametrize("constant,expected_value", [
        (ZWSP, "\u200b"),
        (ZWJ, "\u200d"),
        (ZWNJ, "\u200c"),
        (ZWNBSP, "\ufeff"),
        (ZERO_BIT, "\u200b"),
        (ONE_BIT, "\u200d"),
        (START_MARKER, "\u200b\u200d"),
        (END_MARKER, "\u200c\ufeff"),
    ])
    def test_constant_values(self, constant, expected_value):
        """
        Test that all constants have the correct Unicode values.
        
        Args:
            constant: The constant to test
            expected_value: The expected Unicode value
        """
        assert constant == expected_value

    def test_marker_combinations(self):
        """
        Test that START_MARKER and END_MARKER are correctly composed from individual constants.
        """
        assert START_MARKER == ZWSP + ZWJ
        assert END_MARKER == ZWNJ + ZWNBSP

    def test_bit_encoding_constants(self):
        """
        Test that ZERO_BIT and ONE_BIT are correctly defined.
        """
        assert ZERO_BIT == ZWSP
        assert ONE_BIT == ZWJ


class TestErrorHandling:
    """Test error handling scenarios."""



    def test_encode_message_core_encode_error(self, sample_message, sample_carrier, click_context):
        """
        Test that encode_message propagates errors from core_encode.
        """
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.side_effect = ValueError("Invalid input")
                with pytest.raises(ValueError, match="Invalid input"):
                    encode_message(sample_message, sample_carrier)




class TestIntegration:
    """Integration tests for the encode module."""

    def test_encode_message_full_workflow(self, click_context):
        """
        Test the complete workflow of encode_message with real core_encode.
        
        Args:
            click_context: Mock click context fixture
        """
        click_context.obj["backend"] = "python"
        
        # This test uses the real core_encode to ensure integration works
        from whitespace_stego.core import encode
        
        original_message = "Test message"
        carrier = "Hello World"
        
        with patch('click.get_current_context', return_value=click_context):
            result = encode_message(original_message, carrier)
            # Verify that the result contains the start marker
            assert START_MARKER in result
            # Verify that the result is longer than the original carrier (due to encoding)
            assert len(result) > len(carrier)

    def test_encode_message_multiple_encodings(self, click_context):
        """
        Test multiple encodings on the same carrier text.
        
        Args:
            click_context: Mock click context fixture
        """
        click_context.obj["backend"] = "python"
        
        from whitespace_stego.core import encode
        
        messages = ["First", "Second"]
        carrier = "Hello World"
        
        with patch('click.get_current_context', return_value=click_context):
            encoded = carrier
            for msg in messages:
                encoded = encode_message(msg, encoded)
            
            # Verify that the final result contains markers (may be more than expected due to encoding)
            assert START_MARKER in encoded
            # Verify that the result is longer than the original carrier
            assert len(encoded) > len(carrier)

    def test_encode_message_with_password_workflow(self, click_context):
        """
        Test the complete workflow with password encryption.
        
        Args:
            click_context: Mock click context fixture
        """
        click_context.obj["backend"] = "python"
        
        from whitespace_stego.core import encode
        
        original_message = "Secret message"
        carrier = "Public text"
        password = "mypassword"
        
        with patch('click.get_current_context', return_value=click_context):
            result = encode_message(original_message, carrier, password)
            # Verify that the result contains the start marker
            assert START_MARKER in result
            # Verify that the result is longer than the original carrier
            assert len(result) > len(carrier)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_encode_message_very_long_message(self, sample_carrier, click_context):
        """
        Test encoding with a very long message.
        """
        click_context.obj["backend"] = "python"
        long_message = "A" * 1000  # 1000 character message
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "long_message_encoded"
                result = encode_message(long_message, sample_carrier)
                assert result == "long_message_encoded"
                mock_core_encode.assert_called_once_with(long_message, sample_carrier, None)

    def test_encode_message_very_long_carrier(self, sample_message, click_context):
        """
        Test encoding with a very long carrier text.
        """
        click_context.obj["backend"] = "python"
        long_carrier = "B" * 1000  # 1000 character carrier
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "long_carrier_encoded"
                result = encode_message(sample_message, long_carrier)
                assert result == "long_carrier_encoded"
                mock_core_encode.assert_called_once_with(sample_message, long_carrier, None)

    def test_encode_message_special_characters(self, click_context):
        """
        Test encoding with special characters in message and carrier.
        """
        click_context.obj["backend"] = "python"
        special_message = "Message with \n\t\r special chars: !@#$%^&*()"
        special_carrier = "Carrier with \n\t\r special chars: !@#$%^&*()"
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "special_chars_encoded"
                result = encode_message(special_message, special_carrier)
                assert result == "special_chars_encoded"
                mock_core_encode.assert_called_once_with(special_message, special_carrier, None)

    def test_encode_message_binary_data(self, click_context):
        """
        Test encoding with binary-like data (base64 encoded).
        """
        click_context.obj["backend"] = "python"
        import base64
        binary_data = base64.b64encode(b"binary data").decode('ascii')
        carrier = "Text carrier"
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.encode.core_encode') as mock_core_encode:
                mock_core_encode.return_value = "binary_data_encoded"
                result = encode_message(binary_data, carrier)
                assert result == "binary_data_encoded"
                mock_core_encode.assert_called_once_with(binary_data, carrier, None)


if __name__ == "__main__":
    """Run the tests directly when executed as a script."""
    import sys
    import pytest
    
    # Add the project root to the path
    sys.path.insert(0, '.')
    
    # Run the tests
    exit_code = pytest.main([
        __file__,
        "-v",
        "--tb=short",
        "--no-header",
        "--no-summary"
    ])
    
    sys.exit(exit_code) 