#!/usr/bin/env python3
"""Investigate C backend multi-recipient behavior."""

import whitespace_stego
import sys

def test_c_backend_multi_recipient():
    """Test C backend multi-recipient behavior step by step."""
    
    if not whitespace_stego.c_available():
        print("C backend not available")
        return
    
    print("Testing C backend multi-recipient behavior...")
    
    # Test data
    carrier = "C"
    m1, m2, m3 = "msg1", "msg2", "msg3"
    p1, p2, p3 = "pw1", "pw2", "pw3"
    
    print(f"Original carrier: '{carrier}'")
    print(f"Messages: {m1}, {m2}, {m3}")
    print(f"Passwords: {p1}, {p2}, {p3}")
    
    try:
        # Step 1: Encode first message
        print("\n1. Encoding first message...")
        c1 = whitespace_stego.c_encode(m1, carrier, p1)
        print(f"   Result: '{c1}'")
        print(f"   Length: {len(c1)}")
        print(f"   Contains markers: START={c1.count('\\ufeff')}, END={c1.count('\\u200c')}")
        
        # Step 2: Encode second message
        print("\n2. Encoding second message...")
        c2 = whitespace_stego.c_encode(m2, c1, p2)
        print(f"   Result: '{c2}'")
        print(f"   Length: {len(c2)}")
        print(f"   Contains markers: START={c2.count('\\ufeff')}, END={c2.count('\\u200c')}")
        
        # Step 3: Encode third message
        print("\n3. Encoding third message...")
        c3 = whitespace_stego.c_encode(m3, c2, p3)
        print(f"   Result: '{c3}'")
        print(f"   Length: {len(c3)}")
        print(f"   Contains markers: START={c3.count('\\ufeff')}, END={c3.count('\\u200c')}")
        
        # Step 4: Try to decode with each password
        print("\n4. Testing decode with each password...")
        
        print(f"\n   Decoding with {p1}...")
        try:
            result1 = whitespace_stego.c_decode(c3, p1)
            print(f"   Success: '{result1}'")
        except Exception as e:
            print(f"   Failed: {e}")
        
        print(f"\n   Decoding with {p2}...")
        try:
            result2 = whitespace_stego.c_decode(c3, p2)
            print(f"   Success: '{result2}'")
        except Exception as e:
            print(f"   Failed: {e}")
        
        print(f"\n   Decoding with {p3}...")
        try:
            result3 = whitespace_stego.c_decode(c3, p3)
            print(f"   Success: '{result3}'")
        except Exception as e:
            print(f"   Failed: {e}")
        
        # Step 5: Try decode_all
        print(f"\n5. Testing decode_all with {p1}...")
        try:
            # We need to access the C library directly for decode_all
            import ctypes
            from whitespace_stego.c_backend import _lib
            
            carrier_bytes = c3.encode('utf-8')
            password_bytes = p1.encode('utf-8')
            
            results_ptr = ctypes.POINTER(ctypes.c_char_p)()
            result_count = ctypes.c_size_t()
            
            success = _lib.whitespace_stego_decode_all(
                carrier_bytes,
                len(carrier_bytes),
                password_bytes,
                ctypes.byref(results_ptr),
                ctypes.byref(result_count)
            )
            
            print(f"   decode_all success: {success}")
            print(f"   result_count: {result_count.value}")
            
            if success and result_count.value > 0:
                messages = []
                for i in range(result_count.value):
                    msg_ptr = results_ptr[i]
                    if msg_ptr:
                        messages.append(msg_ptr.decode('utf-8'))
                print(f"   Messages: {messages}")
                
                # Free memory
                _lib.whitespace_stego_free_all(results_ptr, result_count.value)
            
        except Exception as e:
            print(f"   decode_all failed: {e}")
        
        # Step 6: Compare with Python backend
        print(f"\n6. Comparing with Python backend...")
        try:
            py_c1 = whitespace_stego.py_encode(m1, carrier, p1)
            py_c2 = whitespace_stego.py_encode(m2, py_c1, p2)
            py_c3 = whitespace_stego.py_encode(m3, py_c2, p3)
            
            py_result1 = whitespace_stego.py_decode(py_c3, p1)
            print(f"   Python with {p1}: '{py_result1}'")
            
            py_result2 = whitespace_stego.py_decode(py_c3, p2)
            print(f"   Python with {p2}: '{py_result2}'")
            
            py_result3 = whitespace_stego.py_decode(py_c3, p3)
            print(f"   Python with {p3}: '{py_result3}'")
            
        except Exception as e:
            print(f"   Python comparison failed: {e}")
        
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_c_backend_multi_recipient() 