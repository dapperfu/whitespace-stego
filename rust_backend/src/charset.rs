/// Unicode control characters for message framing
pub const START_MARKER: &str = "\u{2060}"; // Word Joiner
pub const END_MARKER: &str = "\u{2061}";   // Function Application

/// Binary encoding characters
pub const ZWSP: &str = "\u{200B}"; // Zero-Width Space (bit 0)
pub const ZWNJ: &str = "\u{200C}"; // Zero-Width Non-Joiner (bit 1)

/// Convert a binary value to a zero-width character.
pub fn binary_to_char(bit: u8) -> &'static str {
    match bit {
        0 => ZWSP,
        1 => ZWNJ,
        _ => panic!("Invalid bit: {}", bit),
    }
}

/// Convert a zero-width character to a binary value.
pub fn char_to_binary(c: char) -> Option<u8> {
    match c {
        '\u{200B}' => Some(0),
        '\u{200C}' => Some(1),
        _ => None,
    }
}

/// Check if the carrier text is valid for steganography.
///
/// A valid carrier text should not contain any of our control characters
/// to avoid conflicts with the steganographic encoding.
///
/// # Arguments
///
/// * `text` - The carrier text to validate
///
/// # Returns
///
/// * `bool` - True if the text is valid, False otherwise
pub fn is_valid_carrier(text: &str) -> bool {
    !text.contains(START_MARKER) && 
    !text.contains(END_MARKER) && 
    !text.contains(ZWSP) && 
    !text.contains(ZWNJ)
}

/// Get the start and end control characters.
///
/// # Returns
///
/// * `(&str, &str)` - A tuple containing (start_marker, end_marker)
pub fn get_control_chars() -> (&'static str, &'static str) {
    (START_MARKER, END_MARKER)
}

/// Get the binary encoding characters.
///
/// # Returns
///
/// * `(&str, &str)` - A tuple containing (zero_width_space, zero_width_non_joiner)
pub fn get_binary_chars() -> (&'static str, &'static str) {
    (ZWSP, ZWNJ)
} 