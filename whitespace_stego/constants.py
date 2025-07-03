"""
whitespace_stego.constants
-------------------------
Canonical protocol constants for whitespace steganography.
All modules should import from here.
"""

# Zero-width Unicode characters
ZWSP = "\u200b"   # Zero-width space (U+200B)
ZWJ = "\u200d"    # Zero-width joiner (U+200D)
ZWNJ = "\u200c"   # Zero-width non-joiner (U+200C)
ZWNBSP = "\ufeff" # Zero-width no-break space (U+FEFF)

# Protocol markers (single codepoints, canonical - matches C/Rust/Go implementations)
ZERO_BIT = ZWSP
ONE_BIT = ZWJ
START_MARKER = ZWNBSP  # Single character, not combination
END_MARKER = ZWNJ      # Single character, not combination

BITS_PER_CHAR = 8 