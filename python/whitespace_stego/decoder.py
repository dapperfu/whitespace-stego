import base64

CONTROL_START = '⁠'
CONTROL_END = '⁣'
BIT_0 = '​'
BIT_1 = '‌'

def decode_message(encoded: str) -> str:
    try:
        start = encoded.index(CONTROL_START) + 1
        end = encoded.index(CONTROL_END)
        payload = encoded[start:end]
        bits = ''.join('0' if c == BIT_0 else '1' for c in payload)
        chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        return base64.b64decode(''.join(chars)).decode()
    except Exception as e:
        raise ValueError("Invalid encoded message.") from e
