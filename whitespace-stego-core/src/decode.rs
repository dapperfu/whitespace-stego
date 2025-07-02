//! Decoding functionality for whitespace steganography.
//!
//! This module provides functions for decoding zero-width Unicode characters
//! back to binary data and extracting messages from carrier text.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};

use crate::constants::{START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT};
use crate::crypto::decrypt_data;
use crate::error::StegoError;

/// Convert a string of zero-width characters back to bytes
///
/// Each 8 zero-width characters are converted back to a single byte, where:
/// - `ZERO_BIT` represents a 0 bit
/// - `ONE_BIT` represents a 1 bit
///
/// # Arguments
/// * `encoded` - The string containing zero-width characters
///
/// # Returns
/// The decoded binary data
///
/// # Errors
/// Returns `StegoError::InvalidBinaryData` if the encoded data is malformed
pub fn decode_binary(encoded: &str) -> Result<Vec<u8>, StegoError> {
    let mut result = Vec::new();
    let mut current_byte = 0u8;
    let mut bit_count = 0;

    for c in encoded.chars() {
        if c == ONE_BIT || c == ZERO_BIT {
            current_byte = (current_byte << 1) | if c == ONE_BIT { 1 } else { 0 };
            bit_count += 1;

            if bit_count == 8 {
                result.push(current_byte);
                current_byte = 0;
                bit_count = 0;
            }
        }
    }

    // Check if we have incomplete bytes
    if bit_count > 0 {
        return Err(StegoError::invalid_binary_data(
            format!("Incomplete byte: {} bits remaining", bit_count)
        ));
    }

    Ok(result)
}

/// Decode a message from carrier text containing zero-width characters
///
/// This function:
/// 1. Finds the encoded message between start and end markers
/// 2. Converts zero-width characters back to binary data
/// 3. Optionally decrypts the data with a password
/// 4. Base64 decodes the data to get the original message
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
/// * `password` - Optional password for decryption
///
/// # Returns
/// The decoded message
///
/// # Errors
/// Returns `StegoError::InvalidCarrier` if no markers are found
/// Returns `StegoError::DecryptionFailed` if decryption fails
/// Returns `StegoError::InvalidBinaryData` if the encoded data is malformed
pub fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Find byte indices for START_MARKER and END_MARKER (match Python behavior)
    let start = carrier.find(START_MARKER)
        .ok_or_else(|| StegoError::invalid_carrier("No start marker found"))?;
    let end = carrier.find(END_MARKER)
        .ok_or_else(|| StegoError::invalid_carrier("No end marker found"))?;
    let encoded = &carrier[start + START_MARKER.len_utf8()..end];
    eprintln!("[DEBUG] Rust decode extracted encoded message: {:?}", encoded);
    eprintln!("[DEBUG] Rust decode extracted length: {}", encoded.chars().count());
    let codepoints: Vec<String> = encoded.chars().take(20).map(|c| format!("0x{:x}", c as u32)).collect();
    eprintln!("[DEBUG] Rust decode codepoints: {:?}", codepoints);
    let binary_string: String = encoded.chars().map(|c| if c == ONE_BIT { '1' } else { '0' }).collect();
    eprintln!("[DEBUG] Rust decode binary string: {}", &binary_string[..80.min(binary_string.len())]);
    let mut data = decode_binary(encoded)?;
    if let Some(pwd) = password {
        data = decrypt_data(&data, pwd)?;
    }
    let decoded = BASE64.decode(&data)?;
    String::from_utf8(decoded).map_err(Into::into)
}

/// Extract the encoded message and remaining carrier text
///
/// This function separates the encoded message from the carrier text,
/// returning both parts. This is useful for analyzing the structure
/// of encoded text or for partial processing.
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
///
/// # Returns
/// A tuple of (encoded_message, remaining_carrier)
///
/// # Errors
/// Returns `StegoError::InvalidCarrier` if no markers are found
pub fn extract_encoded(carrier: &str) -> Result<(String, String), StegoError> {
    let start = carrier.find(START_MARKER)
        .ok_or_else(|| StegoError::invalid_carrier("No start marker found"))?;
    let end = carrier[start + START_MARKER.len_utf8()..]
        .find(END_MARKER)
        .map(|e| start + START_MARKER.len_utf8() + e)
        .ok_or_else(|| StegoError::invalid_carrier("No end marker found after start marker"))?;
    if end <= start {
        return Err(StegoError::invalid_carrier("End marker before start marker"));
    }
    let encoded = &carrier[start..end + END_MARKER.len_utf8()];
    let remaining = format!(
        "{}{}",
        &carrier[..start],
        &carrier[end + END_MARKER.len_utf8()..]
    );
    Ok((encoded.to_string(), remaining))
}

/// Get the position of the encoded message in the carrier text
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
///
/// # Returns
/// A tuple of (start_position, end_position) in characters, or `None` if not found
pub fn get_encoded_message_position(carrier: &str) -> Option<(usize, usize)> {
    let start = carrier.find(START_MARKER)?;
    let end = carrier.find(END_MARKER)?;
    
    if end <= start {
        return None;
    }
    
    Some((start, end + END_MARKER.len_utf8()))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_decode_binary() {
        let data = b"test";
        let encoded = crate::encode::encode_binary(data);
        let decoded = decode_binary(&encoded).unwrap();
        assert_eq!(decoded, data);
    }

    #[test]
    fn test_decode_binary_incomplete() {
        // Create incomplete binary data (not multiple of 8)
        let incomplete = format!("{}{}{}", ZERO_BIT, ONE_BIT, ZERO_BIT);
        let result = decode_binary(&incomplete);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::InvalidBinaryData { .. }));
    }

    #[test]
    fn test_decode_binary_with_invalid_chars() {
        // Mix valid and invalid characters
        let mixed = format!("{}a{}b{}", ZERO_BIT, ONE_BIT, ZERO_BIT);
        let result = decode_binary(&mixed);
        // Should still work, ignoring invalid characters
        assert!(result.is_ok());
    }

    #[test]
    fn test_decode_roundtrip() {
        let message = "Hello, World!";
        let carrier = "This is carrier text";
        
        let encoded = crate::encode::encode(message, carrier, None).unwrap();
        let decoded = decode(&encoded, None).unwrap();
        
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_decode_with_password() {
        let message = "Secret message";
        let carrier = "Carrier text";
        let password = "mypassword";
        
        let encoded = crate::encode::encode(message, carrier, Some(password)).unwrap();
        let decoded = decode(&encoded, Some(password)).unwrap();
        
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_decode_wrong_password() {
        let message = "Secret message";
        let carrier = "Carrier text";
        let password = "correct_password";
        let wrong_password = "wrong_password";
        
        let encoded = crate::encode::encode(message, carrier, Some(password)).unwrap();
        let result = decode(&encoded, Some(wrong_password));
        
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
    }

    #[test]
    fn test_decode_no_markers() {
        let result = decode("plain text", None);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    }

    #[test]
    fn test_decode_only_start_marker() {
        let text = format!("text with start{}", START_MARKER);
        let result = decode(&text, None);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    }

    #[test]
    fn test_decode_only_end_marker() {
        let text = format!("text with end{}", END_MARKER);
        let result = decode(&text, None);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    }

    #[test]
    fn test_decode_markers_wrong_order() {
        let text = format!("text with{}data{}", END_MARKER, START_MARKER);
        let result = decode(&text, None);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    }

    #[test]
    fn test_extract_encoded() {
        let message = "Test message";
        let carrier = "This is carrier text";
        let encoded = crate::encode::encode(message, carrier, None).unwrap();
        
        let (extracted, remaining) = extract_encoded(&encoded).unwrap();
        
        assert!(extracted.contains(START_MARKER));
        assert!(extracted.contains(END_MARKER));
        assert_eq!(remaining, carrier);
    }

    #[test]
    fn test_extract_encoded_empty_carrier() {
        let message = "Test message";
        let encoded = crate::encode::encode(message, "", None).unwrap();
        
        let (extracted, remaining) = extract_encoded(&encoded).unwrap();
        
        assert!(extracted.contains(START_MARKER));
        assert!(extracted.contains(END_MARKER));
        assert_eq!(remaining, "");
    }

    #[test]
    fn test_get_encoded_message_position() {
        let message = "Test message";
        let carrier = "This is carrier text";
        let encoded = crate::encode::encode(message, carrier, None).unwrap();
        
        let position = get_encoded_message_position(&encoded);
        assert!(position.is_some());
        
        let (start, end) = position.unwrap();
        assert!(start < end);
        assert!(encoded[start..].starts_with(START_MARKER));
        assert!(encoded[..end].ends_with(END_MARKER));
    }

    #[test]
    fn test_get_encoded_message_position_not_found() {
        let position = get_encoded_message_position("plain text");
        assert!(position.is_none());
    }
} 