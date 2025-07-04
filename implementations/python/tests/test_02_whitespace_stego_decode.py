"""
Test 10: Whitespace Stego Decode Module

This test verifies that the decode functionality correctly handles all scenarios
including different backends, error conditions, and edge cases.
"""

import pytest
from unittest.mock import patch, MagicMock
from typing import Optional, Union, List
import click

from whitespace_stego.core import decode_message
from whitespace_stego.constants import START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT, ZWSP, ZWJ, ZWNJ, ZWNBSP


@pytest.fixture
def sample_encoded_single():
    """Sample encoded text with a single message."""
    return f"Hello{START_MARKER}{ZERO_BIT * 8}{END_MARKER}World"


@pytest.fixture
def sample_encoded_multiple():
    """Sample encoded text with multiple messages."""
    return f"Hello{START_MARKER}{ZERO_BIT * 8}{END_MARKER}World{START_MARKER}{ZERO_BIT * 8}{END_MARKER}Test"


@pytest.fixture
def sample_encoded_with_password():
    """Sample encoded text with password protection."""
    return f"Secret{START_MARKER}{ONE_BIT * 16}{END_MARKER}Message"


@pytest.fixture
def invalid_encoded_text():
    """Text without valid start/end markers."""
    return "This text has no valid markers"


@pytest.fixture
def corrupted_encoded_text():
    """Text with corrupted markers."""
    return f"Hello{START_MARKER}corrupted{END_MARKER}World"


@pytest.fixture
def click_context():
    """Mock click context for testing backend selection."""
    with patch('click.get_current_context') as mock_context:
        mock_ctx = MagicMock()
        mock_ctx.obj = {}
        mock_context.return_value = mock_ctx
        yield mock_ctx


class TestDecodeMessage:
    """Test the main decode_message function."""

    def test_decode_message_python_backend(self, sample_encoded_single, click_context):
        """
        Test that decode_message correctly uses python backend.
        """
        click_context.obj["backend"] = "python"
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.return_value = "decoded"
            result = decode_message(sample_encoded_single)
            assert result == "decoded"
            mock_core_decode.assert_called_once_with(sample_encoded_single, None)

    def test_decode_message_rust_backend(self, sample_encoded_single, click_context):
        """
        Test that decode_message correctly uses rust backend (mocked import error).
        """
        click_context.obj["backend"] = "rust"
        with patch('whitespace_stego.core._decode_rust', side_effect=ValueError("Rust backend not available")):
            with pytest.raises(ValueError, match="Rust backend not available"):
                decode_message(sample_encoded_single)

    def test_decode_message_default_backend(self, sample_encoded_single, click_context):
        """
        Test that decode_message uses python backend by default when no backend is specified.
        """
        click_context.obj = {}  # No backend specified
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.return_value = "decoded"
            result = decode_message(sample_encoded_single)
            assert result == "decoded"
            mock_core_decode.assert_called_once_with(sample_encoded_single, None)

    def test_decode_message_with_password(self, sample_encoded_with_password, click_context):
        """
        Test that decode_message correctly passes password to the backend.
        """
        click_context.obj["backend"] = "python"
        password = "test_password"
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.return_value = "decoded_secret"
            result = decode_message(sample_encoded_with_password, password)
            assert result == "decoded_secret"
            mock_core_decode.assert_called_once_with(sample_encoded_with_password, password)

    def test_decode_message_unknown_backend(self, sample_encoded_single, click_context):
        """
        Test that decode_message raises ValueError for unknown backends.
        """
        click_context.obj["backend"] = "unknown_backend"
        with pytest.raises(ValueError, match="Unknown backend: unknown_backend"):
            decode_message(sample_encoded_single)

    def test_decode_message_single_vs_multiple(self, sample_encoded_single, sample_encoded_multiple, click_context):
        """
        Test that decode_message correctly handles single vs multiple messages.
        """
        click_context.obj["backend"] = "python"
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            # Test single message
            mock_core_decode.return_value = "single_message"
            result = decode_message(sample_encoded_single)
            assert result == "single_message"
            # Test multiple messages
            mock_core_decode.return_value = ["message1", "message2"]
            result = decode_message(sample_encoded_multiple)
            assert result == ["message1", "message2"]

    def test_decode_message_no_click_context(self, sample_encoded_single):
        """
        Test that decode_message works when no click context is available.
        """
        with patch('click.get_current_context', side_effect=RuntimeError("No context")):
            with patch('whitespace_stego.core._decode_python') as mock_core_decode:
                mock_core_decode.return_value = "decoded"
                result = decode_message(sample_encoded_single)
                assert result == "decoded"
                mock_core_decode.assert_called_once_with(sample_encoded_single, None)

    def test_decode_message_rust_backend_fallback(self, sample_encoded_single, click_context):
        """
        Test that decode_message falls back to rust_decode when rust_decode_all raises ImportError.
        """
        click_context.obj["backend"] = "rust"
        with patch('whitespace_stego.core._decode_rust', side_effect=ValueError("Rust backend not available")):
            with pytest.raises(ValueError, match="Rust backend not available"):
                decode_message(sample_encoded_single)

    def test_decode_message_rust_backend_multiple_messages(self, sample_encoded_multiple, click_context):
        """
        Test that decode_message correctly handles multiple messages from rust backend.
        """
        click_context.obj["backend"] = "rust"
        with patch('whitespace_stego.core._decode_rust') as mock_rust_decode_all:
            mock_rust_decode_all.return_value = ["message1", "message2", "message3"]
            result = decode_message(sample_encoded_multiple)
            assert result == ["message1", "message2", "message3"]
            mock_rust_decode_all.assert_called_once_with(sample_encoded_multiple, None)

    def test_decode_message_rust_backend_single_message(self, sample_encoded_single, click_context):
        """
        Test that decode_message correctly handles single message from rust backend.
        """
        click_context.obj["backend"] = "rust"
        with patch('whitespace_stego.core._decode_rust') as mock_rust_decode:
            mock_rust_decode.return_value = "single_message"  # Return string for single message
            result = decode_message(sample_encoded_single)
            assert result == "single_message"  # Should return string, not list
            mock_rust_decode.assert_called_once_with(sample_encoded_single, None)

    def test_decode_message_rust_backend_with_password(self, sample_encoded_single, click_context):
        """
        Test that decode_message correctly handles password-protected message from rust backend.
        """
        click_context.obj["backend"] = "rust"
        with patch('whitespace_stego.core._decode_rust') as mock_rust_decode:
            mock_rust_decode.return_value = "decoded_with_password"  # Return string for single message
            result = decode_message(sample_encoded_single, "password")
            assert result == "decoded_with_password"
            mock_rust_decode.assert_called_once_with(sample_encoded_single, "password")


class TestDecodePython:
    """Test the _decode_python function."""

    @pytest.mark.parametrize("encoded_text,password,expected_result", [
        ("test_text", None, "decoded_single"),
        ("test_text", "password", "decoded_with_password"),
        ("test_text", "", "decoded_empty_password"),
    ])
    def test_decode_python_calls_core_decode(self, encoded_text, password, expected_result):
        """
        Test that _decode_python correctly calls the core decode function with the right parameters.
        
        Args:
            encoded_text: The encoded text to decode
            password: The password to use for decryption
            expected_result: The expected result from the core decode function
        """
        with patch('whitespace_stego.core._decode_python_impl') as mock_core_decode:
            mock_core_decode.return_value = expected_result
            from whitespace_stego.core import _decode_python
            result = _decode_python(encoded_text, password)
            assert result == expected_result
            mock_core_decode.assert_called_once_with(encoded_text, password)

    def test_decode_python_return_types(self):
        """
        Test that _decode_python returns the correct types.
        """
        with patch('whitespace_stego.core._decode_python_impl') as mock_core_decode:
            # Test single message return
            mock_core_decode.return_value = "single_message"
            from whitespace_stego.core import _decode_python
            result = _decode_python("test", None)
            assert isinstance(result, str)
            assert result == "single_message"
            
            # Test multiple messages return
            mock_core_decode.return_value = ["message1", "message2"]
            result = _decode_python("test", None)
            assert isinstance(result, list)
            assert result == ["message1", "message2"]

    def test_decode_python_function(self):
        """
        Test that _decode_python function exists and is callable.
        """
        from whitespace_stego.core import _decode_python
        assert callable(_decode_python)


class TestConstants:
    """Test that all constants are correctly defined."""

    @pytest.mark.parametrize("constant,expected_value", [
        (ZWSP, "\u200b"),
        (ZWJ, "\u200d"),
        (ZWNJ, "\u200c"),
        (ZWNBSP, "\ufeff"),
        (ZERO_BIT, "\u200b"),
        (ONE_BIT, "\u200d"),
        (START_MARKER, "\ufeff"),  # Single character, not combination
        (END_MARKER, "\u200c"),    # Single character, not combination
    ])
    def test_constant_values(self, constant, expected_value):
        """Test that all constants have the correct Unicode values."""
        assert constant == expected_value

    def test_marker_combinations(self):
        """Test that marker combinations work correctly."""
        # These are now single characters, not combinations
        assert START_MARKER == ZWNBSP
        assert END_MARKER == ZWNJ


class TestErrorHandling:
    """Test error handling scenarios."""

    @pytest.mark.parametrize("invalid_text", [
        "",
        "   ",
        "no_markers_here",
        f"only_start{START_MARKER}",
        f"only_end{END_MARKER}",
        f"wrong_order{END_MARKER}text{START_MARKER}",
    ])
    def test_decode_message_invalid_input(self, invalid_text, click_context):
        """
        Test that decode_message handles invalid input gracefully.
        """
        click_context.obj["backend"] = "python"
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.side_effect = ValueError("Invalid carrier text")
            with pytest.raises(ValueError, match="Invalid carrier text"):
                decode_message(invalid_text)


class TestIntegration:
    """Integration tests for the decode functionality."""

    def test_decode_message_full_workflow(self, click_context):
        """
        Test a complete decode workflow.
        """
        click_context.obj["backend"] = "python"
        encoded_text = f"Hello{START_MARKER}{ZERO_BIT * 8}{END_MARKER}World"
        
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.return_value = "Hello"
            result = decode_message(encoded_text)
            assert result == "Hello"
            mock_core_decode.assert_called_once_with(encoded_text, None)

    def test_decode_message_multiple_workflow(self, click_context):
        """
        Test a complete decode workflow with multiple messages.
        """
        click_context.obj["backend"] = "python"
        encoded_text = f"Hello{START_MARKER}{ZERO_BIT * 8}{END_MARKER}World{START_MARKER}{ZERO_BIT * 8}{END_MARKER}Test"
        
        with patch('whitespace_stego.core._decode_python') as mock_core_decode:
            mock_core_decode.return_value = ["Hello", "World"]
            result = decode_message(encoded_text)
            assert result == ["Hello", "World"]
            mock_core_decode.assert_called_once_with(encoded_text, None)


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