#!/usr/bin/env python3
"""Focused test for C backend multi-recipient behavior."""

import whitespace_stego

def test_c_multi_recipient():
    """Test C backend multi-recipient behavior with detailed debugging."""
    
    if not whitespace_stego.c_available():
        print("C backend not available")
        return
    
    print("Testing C backend multi-recipient behavior...")
    
    # Simple test case
    carrier = "C"
    m1, m2 = "msg1", "msg2"
    p1, p2 = "pw1", "pw2"
    
    print(f"Original carrier: '{carrier}'")
    print(f"Messages: {m1}, {m2}")
    print(f"Passwords: {p1}, {p2}")
    
    try:
        # Step 1: Encode first message
        print("\n1. Encoding first message...")
        c1 = whitespace_stego.c_encode(m1, carrier, p1)
        print(f"   Result length: {len(c1)}")
        print(f"   START_MARKER count: {c1.count('\\ufeff')}")
        print(f"   END_MARKER count: {c1.count('\\u200c')}")
        print(f"   First 20 chars: {repr(c1[:20])}")
        
        # Step 2: Encode second message
        print("\n2. Encoding second message...")
        c2 = whitespace_stego.c_encode(m2, c1, p2)
        print(f"   Result length: {len(c2)}")
        print(f"   START_MARKER count: {c2.count('\\ufeff')}")
        print(f"   END_MARKER count: {c2.count('\\u200c')}")
        print(f"   First 20 chars: {repr(c2[:20])}")
        
        # Step 3: Try to decode with each password
        print("\n3. Testing decode with each password...")
        
        print(f"\n   Decoding with {p1}...")
        try:
            result1 = whitespace_stego.c_decode(c2, p1)
            print(f"   Success: '{result1}'")
        except Exception as e:
            print(f"   Failed: {e}")
        
        print(f"\n   Decoding with {p2}...")
        try:
            result2 = whitespace_stego.c_decode(c2, p2)
            print(f"   Success: '{result2}'")
        except Exception as e:
            print(f"   Failed: {e}")
        
        # Step 4: Compare with Python backend
        print(f"\n4. Comparing with Python backend...")
        try:
            py_c1 = whitespace_stego.py_encode(m1, carrier, p1)
            py_c2 = whitespace_stego.py_encode(m2, py_c1, p2)
            
            print(f"   Python c2 length: {len(py_c2)}")
            print(f"   Python START_MARKER count: {py_c2.count('\\ufeff')}")
            print(f"   Python END_MARKER count: {py_c2.count('\\u200c')}")
            
            py_result1 = whitespace_stego.py_decode(py_c2, p1)
            print(f"   Python with {p1}: '{py_result1}'")
            
            py_result2 = whitespace_stego.py_decode(py_c2, p2)
            print(f"   Python with {p2}: '{py_result2}'")
            
        except Exception as e:
            print(f"   Python comparison failed: {e}")
        
        # Step 5: Test single message decode
        print(f"\n5. Testing single message decode...")
        try:
            single_result = whitespace_stego.c_decode(c1, p1)
            print(f"   Single message decode: '{single_result}'")
        except Exception as e:
            print(f"   Single message decode failed: {e}")
        
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_c_multi_recipient() 