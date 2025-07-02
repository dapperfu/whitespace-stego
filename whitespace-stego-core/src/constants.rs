//! Unicode character constants for whitespace steganography.
//!
//! This module defines the zero-width Unicode characters used for encoding
//! binary data in text without visible changes.

/// Zero-width no-break space character used as start marker
pub const START_MARKER: &str = "\u{FEFF}";

/// Zero-width non-joiner character used as end marker
pub const END_MARKER: &str = "\u{200C}";

/// Zero-width space character used to represent zero bits
pub const ZERO_BIT: &str = "\u{200B}";

/// Zero-width joiner character used to represent one bits
pub const ONE_BIT: &str = "\u{200D}";

/// All zero-width characters used in encoding
pub const ZERO_WIDTH_CHARS: [&str; 4] = [START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT];

/// Check if a character is a zero-width character used in steganography
pub fn is_zero_width_char(c: char) -> bool {
    matches!(c, '\u{FEFF}' | '\u{200C}' | '\u{200B}' | '\u{200D}')
}

/// Check if a character is a data bit (ZERO_BIT or ONE_BIT)
pub fn is_data_bit(c: char) -> bool {
    matches!(c, '\u{200B}' | '\u{200D}')
}

/// Check if a character is a marker (START_MARKER or END_MARKER)
pub fn is_marker(c: char) -> bool {
    matches!(c, '\u{FEFF}' | '\u{200C}')
} 