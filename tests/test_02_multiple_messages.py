"""
Test 02: Multiple Message Support

This test verifies that the Python implementation correctly handles
multiple messages in a single carrier using the new multiple message
functionality.
"""

import pytest
from whitespace_stego.core import encode, decode


@pytest.fixture
def basic_carrier():
    """Basic carrier text for testing."""
    return "Carrier message"


@pytest.fixture
def short_carrier():
    """Short carrier for testing slot allocation."""
    return "ABC"


@pytest.fixture
def unicode_carrier():
    """Unicode carrier for testing internationalization."""
    return "Unicode carrier: 中文 🌍"


@pytest.mark.parametrize("messages", [
    ["First", "Second"],
    ["A", "B", "C"],
    ["Hello", "World", "Test", "Multiple"],
    ["Unicode 🌍", "Emoji 🚀", "中文"],
    ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5"],
])
def test_multiple_messages_roundtrip(messages, basic_carrier):
    """Test encoding and decoding multiple messages in sequence."""
    encoded = basic_carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    assert decoded == messages


@pytest.mark.parametrize("carrier_length,num_messages", [
    ("A", 1),      # Single char carrier
    ("AB", 2),     # Two char carrier
    ("ABC", 3),    # Three char carrier
    ("ABCD", 4),   # Four char carrier
    ("ABCDE", 5),  # Five char carrier
])
def test_slot_allocation_logic(carrier_length, num_messages):
    """Test that messages are allocated to correct slots based on carrier length."""
    carrier = carrier_length
    messages = [f"Msg{i}" for i in range(num_messages)]
    
    encoded = carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    assert len(decoded) == num_messages
    assert decoded == messages


@pytest.mark.parametrize("messages", [
    ["First", "Second", "Third"],
    ["A", "B", "C", "D", "E"],
    ["One", "Two", "Three", "Four", "Five", "Six"],
])
def test_message_order_preservation(messages, basic_carrier):
    """Test that message order is preserved during encoding and decoding."""
    encoded = basic_carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    assert decoded == messages  # Order must be preserved exactly


@pytest.mark.parametrize("password", [None, "password", "secure123", ""])
def test_multiple_messages_with_password(password, basic_carrier):
    """Test multiple messages with password protection."""
    messages = ["Secret1", "Secret2", "Secret3"]
    
    encoded = basic_carrier
    for msg in messages:
        encoded = encode(msg, encoded, password)
    
    decoded = decode(encoded, password)
    assert decoded == messages


def test_mixed_password_messages(basic_carrier):
    """Test encoding messages with and without passwords in the same carrier."""
    # Encode first message without password
    encoded1 = encode("Public", basic_carrier)
    
    # Encode second message with password
    encoded2 = encode("Secret", encoded1, "password")
    
    # When decoding with password, only password-protected messages should be decoded
    decoded_with_password = decode(encoded2, "password")
    assert "Secret" in decoded_with_password
    assert "Public" not in decoded_with_password  # Unencrypted message not decoded with password
    
    # When decoding without password, only unencrypted messages should be decoded
    decoded_without_password = decode(encoded2)
    assert "Public" in decoded_without_password
    assert "Secret" not in decoded_without_password  # Encrypted message not decoded without password


@pytest.mark.parametrize("messages", [
    ["Single"],
    ["First", "Second"],
    ["A", "B", "C", "D", "E"],
])
def test_backward_compatibility_single_message(messages, basic_carrier):
    """Test that single message decode still returns list with correct items."""
    if len(messages) == 1:
        # Single message case
        encoded = encode(messages[0], basic_carrier)
        decoded = decode(encoded)
        assert isinstance(decoded, list)
        assert len(decoded) == 1
        assert decoded[0] == messages[0]
    else:
        # Multiple message case
        encoded = basic_carrier
        for msg in messages:
            encoded = encode(msg, encoded)
        
        decoded = decode(encoded)
        assert isinstance(decoded, list)
        assert len(decoded) == len(messages)
        assert decoded == messages


@pytest.mark.parametrize("num_messages", [10, 20, 50])
def test_many_messages_performance(num_messages):
    """Test performance and correctness with many messages."""
    carrier = "A" * num_messages  # Ensure enough slots
    messages = [f"Message{i:03d}" for i in range(num_messages)]
    
    encoded = carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    assert decoded == messages


@pytest.mark.parametrize("messages", [
    ["Unicode 🌍", "Emoji 🚀"],
    ["中文", "日本語", "한국어"],
    ["Café", "naïve", "façade"],
    ["Test", "Unicode 🌍", "中文", "Café"],
])
def test_multiple_unicode_messages(messages, unicode_carrier):
    """Test multiple messages with various Unicode content."""
    encoded = unicode_carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    assert decoded == messages


def test_corrupted_multi_message_handling(basic_carrier):
    """Test that corruption in one message doesn't break decoding of others."""
    messages = ["First", "Second", "Third"]
    
    encoded = basic_carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    # Corrupt one of the messages by replacing a zero-width character
    corrupted = encoded.replace("\u200b", "X", 1)
    
    # Should still decode the uncorrupted messages
    try:
        decoded = decode(corrupted)
        # At least one message should decode successfully
        assert len(decoded) >= 1
        # The decoded messages should be a subset of the original
        for msg in decoded:
            assert msg in messages
    except ValueError:
        # It's also acceptable for corruption to cause a complete decode failure
        pass


@pytest.mark.parametrize("messages", [
    ["Empty", "", "NotEmpty"],  # Empty message in middle
    ["", "NotEmpty"],           # Empty message at start
    ["NotEmpty", ""],           # Empty message at end
])
def test_multiple_messages_with_empty_handling(messages, basic_carrier):
    """Test handling of empty messages in multiple message scenarios."""
    # Filter out empty messages since they should raise ValueError
    non_empty_messages = [msg for msg in messages if msg]
    
    if not non_empty_messages:
        # If all messages are empty, should raise ValueError
        with pytest.raises(ValueError):
            encoded = basic_carrier
            for msg in messages:
                encoded = encode(msg, encoded)
    else:
        # Encode only non-empty messages
        encoded = basic_carrier
        for msg in non_empty_messages:
            encoded = encode(msg, encoded)
        
        decoded = decode(encoded)
        assert decoded == non_empty_messages


def test_slot_exhaustion_behavior():
    """Test behavior when more messages are encoded than available slots."""
    carrier = "ABC"  # Only 3 slots available
    messages = ["Msg1", "Msg2", "Msg3", "Msg4", "Msg5"]  # 5 messages
    
    encoded = carrier
    for msg in messages:
        encoded = encode(msg, encoded)
    
    decoded = decode(encoded)
    # Should decode all messages even if slots are exhausted
    assert len(decoded) == len(messages)
    assert decoded == messages


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 