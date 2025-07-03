"""Comprehensive tests for the whitespace steganography encode functionality."""

import pytest
from unittest.mock import patch, MagicMock
from whitespace_stego.core import encode_message
from whitespace_stego.constants import START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT, ZWSP, ZWJ, ZWNJ, ZWNBSP


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
        """Test that encode_message correctly uses the python backend."""
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "encoded_text"
                result = encode_message(sample_message, sample_carrier)
                assert result == "encoded_text"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)

    def test_encode_message_default_backend(self, sample_message, sample_carrier, click_context):
        """Test that encode_message defaults to python backend when no backend is specified."""
        click_context.obj = {}  # No backend specified
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "default_encoded"
                result = encode_message(sample_message, sample_carrier)
                assert result == "default_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)

    def test_encode_message_with_password(self, sample_message, sample_carrier, sample_password, click_context):
        """Test that encode_message correctly passes password to the backend."""
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "password_encoded"
                result = encode_message(sample_message, sample_carrier, sample_password)
                assert result == "password_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, sample_password)

    def test_encode_message_unknown_backend(self, sample_message, sample_carrier, click_context):
        """Test that encode_message raises ValueError for unknown backends."""
        click_context.obj["backend"] = "unknown_backend"
        with patch('click.get_current_context', return_value=click_context):
            with pytest.raises(ValueError, match="Unknown backend: unknown_backend"):
                encode_message(sample_message, sample_carrier)

    def test_encode_message_no_click_context(self, sample_message, sample_carrier):
        """Test that encode_message works when no click context is available."""
        with patch('click.get_current_context', side_effect=RuntimeError("No context")):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "no_context_encoded"
                result = encode_message(sample_message, sample_carrier)
                assert result == "no_context_encoded"
                mock_core_encode.assert_called_once_with(sample_message, sample_carrier, None)

    def test_encode_message_empty_carrier(self, sample_message, click_context):
        """Test that encode_message works with empty carrier text."""
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "empty_carrier_encoded"
                result = encode_message(sample_message, "")
                assert result == "empty_carrier_encoded"
                mock_core_encode.assert_called_once_with(sample_message, "", None)

    def test_encode_message_empty_message(self, sample_carrier, click_context):
        """Test that encode_message works with empty message."""
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "empty_message_encoded"
                result = encode_message("", sample_carrier)
                assert result == "empty_message_encoded"
                mock_core_encode.assert_called_once_with("", sample_carrier, None)

    def test_encode_message_unicode_content(self, click_context):
        """Test that encode_message works with Unicode content."""
        click_context.obj["backend"] = "python"
        unicode_message = "Hello 世界! 🌍"
        unicode_carrier = "Carrier with émojis 🚀"
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
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
        """Test that _encode_python correctly calls core_encode with the right parameters."""
        with patch('whitespace_stego.core._encode_python_impl') as mock_core_encode:
            mock_core_encode.return_value = expected_result
            from whitespace_stego.core import _encode_python
            result = _encode_python(message, carrier, password)
            assert result == expected_result
            mock_core_encode.assert_called_once_with(message, carrier, password)

    def test_encode_python_return_type(self):
        """Test that _encode_python returns the correct type (string)."""
        with patch('whitespace_stego.core._encode_python_impl') as mock_core_encode:
            mock_core_encode.return_value = "encoded_string"
            from whitespace_stego.core import _encode_python
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
        (START_MARKER, "\ufeff"),
        (END_MARKER, "\u200c"),
    ])
    def test_constant_values(self, constant, expected_value):
        """Test that all constants have the correct Unicode values."""
        assert constant == expected_value

    def test_marker_combinations(self):
        """Test that marker combinations work correctly."""
        assert START_MARKER == ZWNBSP
        assert END_MARKER == ZWNJ

    def test_bit_encoding_constants(self):
        """Test that bit encoding constants are correctly defined."""
        assert ZERO_BIT == ZWSP
        assert ONE_BIT == ZWJ


class TestErrorHandling:
    """Test error handling scenarios."""

    def test_encode_message_core_encode_error(self, sample_message, sample_carrier, click_context):
        """Test that encode_message handles core_encode errors gracefully."""
        click_context.obj["backend"] = "python"
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.side_effect = ValueError("Encoding failed")
                with pytest.raises(ValueError, match="Encoding failed"):
                    encode_message(sample_message, sample_carrier)


class TestIntegration:
    """Integration tests for the encode functionality."""

    def test_encode_message_full_workflow(self, click_context):
        """Test a complete encode workflow."""
        click_context.obj["backend"] = "python"
        message = "Hello, World!"
        carrier = "This is a test carrier."
        
        with patch('whitespace_stego.core._encode_python') as mock_core_encode:
            mock_core_encode.return_value = "encoded_carrier"
            result = encode_message(message, carrier)
            assert result == "encoded_carrier"
            mock_core_encode.assert_called_once_with(message, carrier, None)

    def test_encode_message_multiple_encodings(self, click_context):
        """Test multiple consecutive encodings."""
        click_context.obj["backend"] = "python"
        messages = ["First", "Second", "Third"]
        carrier = "Initial carrier"
        
        with patch('whitespace_stego.core._encode_python') as mock_core_encode:
            mock_core_encode.return_value = "encoded_carrier"
            
            current_carrier = carrier
            for message in messages:
                current_carrier = encode_message(message, current_carrier)
                assert current_carrier == "encoded_carrier"
            
            # Should be called once for each message
            assert mock_core_encode.call_count == len(messages)

    def test_encode_message_with_password_workflow(self, click_context):
        """Test a complete encode workflow with password protection."""
        click_context.obj["backend"] = "python"
        message = "Secret message"
        carrier = "Public carrier"
        password = "secret123"
        
        with patch('whitespace_stego.core._encode_python') as mock_core_encode:
            mock_core_encode.return_value = "encrypted_carrier"
            result = encode_message(message, carrier, password)
            assert result == "encrypted_carrier"
            mock_core_encode.assert_called_once_with(message, carrier, password)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_encode_message_very_long_message(self, sample_carrier, click_context):
        """Test encoding with a very long message."""
        click_context.obj["backend"] = "python"
        long_message = "A" * 10000  # 10KB message
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "long_encoded"
                result = encode_message(long_message, sample_carrier)
                assert result == "long_encoded"
                mock_core_encode.assert_called_once_with(long_message, sample_carrier, None)

    def test_encode_message_very_long_carrier(self, sample_message, click_context):
        """Test encoding with a very long carrier text."""
        click_context.obj["backend"] = "python"
        long_carrier = "B" * 10000  # 10KB carrier
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "long_carrier_encoded"
                result = encode_message(sample_message, long_carrier)
                assert result == "long_carrier_encoded"
                mock_core_encode.assert_called_once_with(sample_message, long_carrier, None)

    def test_encode_message_special_characters(self, click_context):
        """Test encoding with special characters and control codes."""
        click_context.obj["backend"] = "python"
        special_message = "\x00\x01\x02\n\r\t\x7f\xff"
        special_carrier = "Carrier with \x00\x01\x02\n\r\t"
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "special_encoded"
                result = encode_message(special_message, special_carrier)
                assert result == "special_encoded"
                mock_core_encode.assert_called_once_with(special_message, special_carrier, None)

    def test_encode_message_binary_data(self, click_context):
        """Test encoding with binary-like data."""
        click_context.obj["backend"] = "python"
        binary_message = bytes(range(256)).decode('latin1')  # All byte values
        binary_carrier = "Carrier with binary: " + bytes(range(32)).decode('latin1')
        
        with patch('click.get_current_context', return_value=click_context):
            with patch('whitespace_stego.core._encode_python') as mock_core_encode:
                mock_core_encode.return_value = "binary_encoded"
                result = encode_message(binary_message, binary_carrier)
                assert result == "binary_encoded"
                mock_core_encode.assert_called_once_with(binary_message, binary_carrier, None)
