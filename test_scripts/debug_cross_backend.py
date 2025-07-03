import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../whitespace-stego-rust/whitespace_stego_rust')))
from whitespace_stego.core import encode as py_encode, _decode_binary, START_MARKER, END_MARKER
import whitespace_stego_rust
import base64

print('Available in whitespace_stego_rust:', dir(whitespace_stego_rust))

msg = 'Test message for encoding identity validation'
carrier = 'This is the carrier text for testing.'
pw = 'test_password_123'

# Test Python encoding
print("=== Python Encoding ===")
enc_py = py_encode(msg, carrier, pw)
print('Python encoded length:', len(enc_py))

# Extract the zero-width payload
start_idx = enc_py.find(START_MARKER)
end_idx = enc_py.find(END_MARKER)
if start_idx != -1 and end_idx != -1:
    zero_width_payload = enc_py[start_idx + len(START_MARKER):end_idx]
    print(f'Zero-width payload length: {len(zero_width_payload)}')
    
    # Decode zero-width to bytes
    payload_bytes = _decode_binary(zero_width_payload)
    print(f'Payload bytes length: {len(payload_bytes)}')
    
    # This should be base64-encoded encrypted data
    try:
        base64_str = payload_bytes.decode('utf-8')
        print(f'Base64 string (first 100 chars): {base64_str[:100]}')
        
        # Decode base64 to get encrypted bytes
        encrypted_bytes = base64.b64decode(base64_str)
        print(f'Encrypted bytes length: {len(encrypted_bytes)}')
        
        # Try to decrypt with Python
        from whitespace_stego.core import decrypt_data
        try:
            decrypted_py = decrypt_data(encrypted_bytes, pw)
            print(f'Python decrypted: {decrypted_py.decode("utf-8")}')
        except Exception as e:
            print(f'Python decryption failed: {e}')
            
    except Exception as e:
        print(f'Base64 decode failed: {e}')

# Test Rust encoding
print("\n=== Rust Encoding ===")
try:
    enc_rust = whitespace_stego_rust.encode_py(msg, carrier, pw)
    print('Rust encoded length:', len(enc_rust))
    
    # Extract the zero-width payload from Rust output
    start_idx = enc_rust.find(START_MARKER)
    end_idx = enc_rust.find(END_MARKER)
    if start_idx != -1 and end_idx != -1:
        zero_width_payload_rust = enc_rust[start_idx + len(START_MARKER):end_idx]
        print(f'Rust zero-width payload length: {len(zero_width_payload_rust)}')
        
        # Decode zero-width to bytes
        payload_bytes_rust = _decode_binary(zero_width_payload_rust)
        print(f'Rust payload bytes length: {len(payload_bytes_rust)}')
        
        # This should be base64-encoded encrypted data
        try:
            base64_str_rust = payload_bytes_rust.decode('utf-8')
            print(f'Rust base64 string (first 100 chars): {base64_str_rust[:100]}')
            
            # Decode base64 to get encrypted bytes
            encrypted_bytes_rust = base64.b64decode(base64_str_rust)
            print(f'Rust encrypted bytes length: {len(encrypted_bytes_rust)}')
            
        except Exception as e:
            print(f'Rust base64 decode failed: {e}')
    
    # Test if Rust can decode its own output
    try:
        dec_rust_own = whitespace_stego_rust.decode_py(enc_rust, pw)
        print(f'Rust can decode its own output: {dec_rust_own}')
    except Exception as e:
        print(f'Rust cannot decode its own output: {e}')
        
except Exception as e:
    print(f'Rust encoding failed: {e}')

# Test cross-decoding
print("\n=== Cross-Decoding Tests ===")
try:
    dec_rust = whitespace_stego_rust.decode_py(enc_py, pw)
    print('Rust backend decoded Python output:', dec_rust)
except Exception as e:
    print('Rust backend failed to decode Python output:', e) 