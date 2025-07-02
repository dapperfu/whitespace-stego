#!/usr/bin/env python3
"""Debug test for message insertion."""

import logging
from whitespace_stego.core import encode, decode, _count_message_pairs, _find_next_slot

# Set up debug logging
logging.basicConfig(level=logging.DEBUG)

def debug_test():
    """Debug the message insertion process."""
    carrier = "Carrier message"
    message1 = "Hello World"
    message2 = "Top Secret"
    
    print(f"Original carrier: '{carrier}'")
    print(f"Length: {len(carrier)}")
    
    # Encode first message
    encoded1 = encode(message1, carrier)
    print(f"\nAfter encoding message 1:")
    print(f"Length: {len(encoded1)}")
    print(f"Message pairs: {_count_message_pairs(encoded1)}")
    
    # Check what slot would be used for second message
    next_slot = _find_next_slot(encoded1)
    print(f"Next slot position: {next_slot}")
    
    # Encode second message
    encoded2 = encode(message2, encoded1)
    print(f"\nAfter encoding message 2:")
    print(f"Length: {len(encoded2)}")
    print(f"Message pairs: {_count_message_pairs(encoded2)}")
    
    # Try to decode
    try:
        decoded = decode(encoded2)
        print(f"Decoded messages: {decoded}")
        print(f"Number of messages: {len(decoded)}")
    except Exception as e:
        print(f"Decode error: {e}")

if __name__ == "__main__":
    debug_test() 