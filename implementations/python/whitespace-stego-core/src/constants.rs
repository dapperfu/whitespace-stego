//! Unicode character constants for whitespace steganography.
//!
//! This module defines the zero-width Unicode characters used for encoding
//! binary data in text without visible changes.

/// Zero-width no-break space character used as start marker.
pub const START_MARKER: char = '\u{FEFF}';

/// Zero-width non-joiner character used as end marker.
pub const END_MARKER: char = '\u{200C}';

/// Zero-width space character used to represent zero bits.
pub const ZERO_BIT: char = '\u{200B}';

/// Zero-width joiner character used to represent one bits.
pub const ONE_BIT: char = '\u{200D}';

/// All zero-width characters used in encoding.
pub const ZERO_WIDTH_CHARS: [char; 4] = [START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT];

/// Check if a character is a zero-width character used in steganography.
///
/// # Arguments
/// * `c` - The character to check
///
/// # Returns
/// `true` if the character is a zero-width character used in steganography
///
/// # Examples
/// ```
/// use whitespace_stego_core::constants::is_zero_width_char;
/// assert!(is_zero_width_char('\u{FEFF}'));
/// assert!(!is_zero_width_char('a'));
/// ```
pub fn is_zero_width_char(c: char) -> bool {
    matches!(c, '\u{FEFF}' | '\u{200C}' | '\u{200B}' | '\u{200D}')
}

/// Check if a character is a data bit (ZERO_BIT or ONE_BIT).
///
/// # Arguments
/// * `c` - The character to check
///
/// # Returns
/// `true` if the character is a data bit
///
/// # Examples
/// ```
/// use whitespace_stego_core::constants::is_data_bit;
/// assert!(is_data_bit('\u{200B}'));
/// assert!(is_data_bit('\u{200D}'));
/// assert!(!is_data_bit('\u{FEFF}'));
/// ```
pub fn is_data_bit(c: char) -> bool {
    matches!(c, '\u{200B}' | '\u{200D}')
}

/// Check if a character is a marker (START_MARKER or END_MARKER).
///
/// # Arguments
/// * `c` - The character to check
///
/// # Returns
/// `true` if the character is a marker
///
/// # Examples
/// ```
/// use whitespace_stego_core::constants::is_marker;
/// assert!(is_marker('\u{FEFF}'));
/// assert!(is_marker('\u{200C}'));
/// assert!(!is_marker('\u{200B}'));
/// ```
pub fn is_marker(c: char) -> bool {
    matches!(c, '\u{FEFF}' | '\u{200C}')
}
