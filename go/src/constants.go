package main

// Zero-width Unicode characters (match Python/Rust/C implementations)
const (
	START_MARKER  = "\uFEFF" // Zero-width no-break space (U+FEFF)
	END_MARKER    = "\u200C" // Zero-width non-joiner (U+200C)
	ZERO_BIT      = "\u200B" // Zero-width space (U+200B)
	ONE_BIT       = "\u200D" // Zero-width joiner (U+200D)
	BITS_PER_CHAR = 8
)
