#!/usr/bin/env python3
"""Test script for multiple message encoding/decoding functionality."""

from whitespace_stego.core import encode, decode

def test_multiple_messages():
    """Test encoding and decoding multiple messages."""
    print("Testing multiple message functionality...")
    
    # Test case 1: Two messages in a carrier
    carrier = "Carrier message"
    message1 = "Hello World"
    message2 = "Top Secret"
    
    print(f"\nOriginal carrier: '{carrier}'")
    print(f"Message 1: '{message1}'")
    print(f"Message 2: '{message2}'")
    
    # Encode first message
    encoded1 = encode(message1, carrier)
    print(f"\nAfter encoding message 1: '{encoded1}'")
    
    # Encode second message into the same carrier
    encoded2 = encode(message2, encoded1)
    print(f"After encoding message 2: '{encoded2}'")
    
    # Decode all messages
    decoded_messages = decode(encoded2)
    print(f"\nDecoded messages: {decoded_messages}")
    
    # Verify results
    assert len(decoded_messages) == 2, f"Expected 2 messages, got {len(decoded_messages)}"
    assert decoded_messages[0] == message1, f"First message mismatch: expected '{message1}', got '{decoded_messages[0]}'"
    assert decoded_messages[1] == message2, f"Second message mismatch: expected '{message2}', got '{decoded_messages[1]}'"
    
    print("✅ Test passed: Multiple messages work correctly!")
    
    # Test case 2: Single message (backward compatibility)
    print(f"\nTesting backward compatibility with single message...")
    single_encoded = encode("Single message", carrier)
    single_decoded = decode(single_encoded)
    
    print(f"Single decoded: {single_decoded}")
    assert len(single_decoded) == 1, f"Expected 1 message, got {len(single_decoded)}"
    assert single_decoded[0] == "Single message", f"Message mismatch: expected 'Single message', got '{single_decoded[0]}'"
    
    print("✅ Test passed: Single message backward compatibility works!")
    
    # Test case 3: Three messages
    print(f"\nTesting three messages...")
    message3 = "Third message"
    encoded3 = encode(message3, encoded2)
    decoded3 = decode(encoded3)
    
    print(f"Three decoded messages: {decoded3}")
    assert len(decoded3) == 3, f"Expected 3 messages, got {len(decoded3)}"
    assert decoded3[0] == message1, f"First message mismatch"
    assert decoded3[1] == message2, f"Second message mismatch"
    assert decoded3[2] == message3, f"Third message mismatch"
    
    print("✅ Test passed: Three messages work correctly!")
    
    print(f"\n🎉 All tests passed! Multiple message functionality is working correctly.")

if __name__ == "__main__":
    test_multiple_messages() 