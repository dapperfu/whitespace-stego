use std::collections::HashMap;
use lazy_static::lazy_static;

/// Unicode control characters for message framing
pub const START_MARKER: &str = "\u{2060}"; // Word Joiner
pub const END_MARKER: &str = "\u{2061}";   // Function Application

/// Binary encoding characters
pub const ZWSP: &str = "\u{200B}"; // Zero-Width Space (bit 0)
pub const ZWNJ: &str = "\u{200C}"; // Zero-Width Non-Joiner (bit 1)

lazy_static! {
    /// Mapping between binary values and zero-width characters
    pub static ref BINARY_TO_CHAR: HashMap<u8, &'static str> = {
        let mut m = HashMap::new();
        m.insert(0, ZWSP);
        m.insert(1, ZWNJ);
        m
    };

    /// Reverse mapping for decoding
    pub static ref CHAR_TO_BINARY: HashMap<&'static str, u8> = {
        let mut m = HashMap::new();
        m.insert(ZWSP, 0);
        m.insert(ZWNJ, 1);
        m
    };
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