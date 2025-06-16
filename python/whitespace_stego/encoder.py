import base64

CONTROL_START = '⁠'
CONTROL_END = '⁣'
BIT_0 = '​'
BIT_1 = '‌'

def encode_message(message: str) -> str:
    b64 = base64.b64encode(message.encode()).decode()
    bits = ''.join(f"{:08b}".format(ord(c)) for c in b64)
    encoded = ''.join(BIT_0 if b == '0' else BIT_1 for b in bits)
    return f"{CONTROL_START}{encoded}{CONTROL_END}"

def embed_message(carrier: str, message: str) -> str:
    if not carrier:
        return encode_message(message)
    return carrier[0] + encode_message(message) + carrier[1:]
