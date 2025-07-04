"""
Test 40: Fuzz and Property-Based Testing

This test suite uses hypothesis to fuzz and property-test encode/decode for all edge cases.
"""

import pytest
from hypothesis import given, strategies as st
from whitespace_stego.core import encode, decode, BadPasswordError

@given(
    message=st.text(min_size=1, max_size=100),
    carrier=st.text(max_size=100),
    password=st.one_of(st.none(), st.text(max_size=20))
)
def test_encode_decode_property(message, carrier, password):
    encoded = encode(message, carrier, password)
    decoded = decode(encoded, password)
    if isinstance(decoded, list):
        assert message in decoded
    else:
        assert decoded == message

@given(
    carrier=st.text(max_size=100),
    password=st.one_of(st.none(), st.text(max_size=20))
)
def test_decode_random_noise_fails(carrier, password):
    # Random carrier with no valid message should fail
    with pytest.raises(Exception):
        decode(carrier, password) 