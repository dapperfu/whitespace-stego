import pytest
from whitespace_stego import encode, decode  # Assuming encode/decode functions are in whitespace_stego module

@pytest.mark.parametrize("message,password,carrier", [
    # ASCII tests
    ("hello", "secret", ""),              # password with empty carrier
    ("hello", "", ""),                    # empty password
    ("hello", None, ""),                  # None password
    ("hello", "secret", "A"),             # one-character carrier
    ("hello", "", "A"),                   # empty password, one-char carrier
    ("hello", None, "A"),                 # None password, one-char carrier
    ("hello", "secret", "AB"),            # two-char carrier
    ("hello", "", "AB"),                  # empty password, two-char carrier
    ("hello", None, "AB"),                # None password, two-char carrier
    ("hello", "secret", "The quick brown fox jumps"), # long carrier
    ("hello", "", "The quick brown fox jumps"),
    ("hello", None, "The quick brown fox jumps"),

    # Unicode and emoji tests
    ("こんにちは", "秘密", "🌸"),                # Japanese with emoji carrier
    ("👋🌍", "", "Hello World"),             # emoji message with ASCII carrier
    ("💡⚡🚀", None, "Start here:"),         # emoji message with sentence carrier
])
def test_stego_encode_decode(message, password, carrier):
    encoded = encode(message, password=password, carrier=carrier)
    decoded = decode(encoded, password=password)
    assert decoded == message
