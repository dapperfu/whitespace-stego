use whitespace_stego_core::constants::*;

#[cfg(test)]
mod tests {
    use super::*;
    // ... (copy all tests from src/constants.rs #[cfg(test)] mod)
}

#[test]
fn test_is_zero_width_char() {
    // Test all zero-width characters
    assert!(is_zero_width_char(START_MARKER));
    assert!(is_zero_width_char(END_MARKER));
    assert!(is_zero_width_char(ZERO_BIT));
    assert!(is_zero_width_char(ONE_BIT));
    
    // Test non-zero-width characters
    assert!(!is_zero_width_char('a'));
    assert!(!is_zero_width_char(' '));
    assert!(!is_zero_width_char('\n'));
    assert!(!is_zero_width_char('😀'));
    assert!(!is_zero_width_char('漢'));
}

#[test]
fn test_is_data_bit() {
    // Test data bit characters
    assert!(is_data_bit(ZERO_BIT));
    assert!(is_data_bit(ONE_BIT));
    
    // Test non-data bit characters
    assert!(!is_data_bit(START_MARKER));
    assert!(!is_data_bit(END_MARKER));
    assert!(!is_data_bit('a'));
    assert!(!is_data_bit(' '));
}

#[test]
fn test_is_marker() {
    // Test marker characters
    assert!(is_marker(START_MARKER));
    assert!(is_marker(END_MARKER));
    
    // Test non-marker characters
    assert!(!is_marker(ZERO_BIT));
    assert!(!is_marker(ONE_BIT));
    assert!(!is_marker('a'));
    assert!(!is_marker(' '));
}

#[test]
fn test_zero_width_chars_array() {
    // Test that the array contains all expected characters
    assert_eq!(ZERO_WIDTH_CHARS.len(), 4);
    assert!(ZERO_WIDTH_CHARS.contains(&START_MARKER));
    assert!(ZERO_WIDTH_CHARS.contains(&END_MARKER));
    assert!(ZERO_WIDTH_CHARS.contains(&ZERO_BIT));
    assert!(ZERO_WIDTH_CHARS.contains(&ONE_BIT));
}

#[test]
fn test_unicode_code_points() {
    // Test that the constants have the correct Unicode code points
    assert_eq!(START_MARKER as u32, 0xFEFF);
    assert_eq!(END_MARKER as u32, 0x200C);
    assert_eq!(ZERO_BIT as u32, 0x200B);
    assert_eq!(ONE_BIT as u32, 0x200D);
}
