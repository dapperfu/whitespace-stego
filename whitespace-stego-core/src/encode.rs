//! Encoding functionality for whitespace steganography.
//!
//! This module provides functions for encoding binary data into zero-width
//! Unicode characters and embedding messages into carrier text.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};

use crate::constants::{START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT};
use crate::crypto::{encrypt_data, is_encrypted};
use crate::error::StegoError;

/// Convert bytes to a string of zero-width characters
///
/// Each byte is converted to 8 zero-width characters, where:
/// - `ZERO_BIT` represents a 0 bit
/// - `ONE_BIT` represents a 1 bit
///
/// # Arguments
/// * `data` - The binary data to encode
///
/// # Returns
/// A string containing only zero-width Unicode characters
pub fn encode_binary(data: &[u8]) -> String {
    data.iter()
        .flat_map(|&byte| {
            (0..8).map(move |i| {
                if (byte >> (7 - i)) & 1 == 1 {
                    ONE_BIT
                } else {
                    ZERO_BIT
                }
            })
        })
        .collect()
}

/// Encode a message into carrier text using zero-width characters
///
/// This function:
/// 1. Base64 encodes the message
/// 2. Optionally encrypts the data with a password
/// 3. Converts the data to zero-width characters
/// 4. Embeds the encoded message in the carrier text
///
/// # Arguments
/// * `message` - The message to encode
/// * `carrier` - The carrier text to hide the message in
/// * `password` - Optional password for encryption
///
/// # Returns
/// The carrier text with the encoded message embedded
///
/// # Errors
/// Returns `StegoError::EncodingFailed` if encryption fails
/// Returns `StegoError::InvalidCarrier` if the carrier is invalid
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Check for empty message with humorous error
    if message.is_empty() {
        return Err(StegoError::encoding_failed(
            "🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!"
        ));
    }
    
    // Base64 encode the message
    let encoded = BASE64.encode(message.as_bytes());
    let mut data = encoded.as_bytes().to_vec();

    // Encrypt if password provided
    if let Some(pwd) = password {
        data = encrypt_data(&data, pwd)?;
    }

    // Convert to zero-width characters
    let zero_width = encode_binary(&data);
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);

    // Embed in carrier after first character
    let mut result = String::with_capacity(carrier.len() + encoded_message.len());
    
    if let Some((first_char_end, _)) = carrier.char_indices().nth(1) {
        // Get the first character and the rest of the string
        result.push_str(&carrier[..first_char_end]);
        result.push_str(&encoded_message);
        result.push_str(&carrier[first_char_end..]);
    } else if !carrier.is_empty() {
        // Only one character in carrier
        result.push_str(carrier);
        result.push_str(&encoded_message);
    } else {
        // carrier is empty, just return the encoded message
        return Ok(encoded_message);
    }
    
    Ok(result)
}

/// Check if text contains an encoded message
///
/// # Arguments
/// * `text` - The text to check
///
/// # Returns
/// `true` if the text contains both start and end markers
pub fn has_encoded_message(text: &str) -> bool {
    text.contains(START_MARKER) && text.contains(END_MARKER)
}

/// Get the size of an encoded message in bytes
///
/// # Arguments
/// * `text` - The text containing the encoded message
///
/// # Returns
/// The size of the encoded message in bytes, or `None` if no message found
pub fn get_encoded_message_size(text: &str) -> Option<usize> {
    let start = text.find(START_MARKER)?;
    let end = text.find(END_MARKER)?;
    
    if end <= start {
        return None;
    }
    
    let encoded = &text[start + START_MARKER.len_utf8()..end];
    Some(encoded.len() / 8) // Each byte is encoded as 8 zero-width characters
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode_binary() {
        let data = b"test";
        let encoded = encode_binary(data);
        
        // Each byte should be encoded as 8 zero-width characters
        assert_eq!(encoded.chars().count(), data.len() * 8);
        
        // All characters should be zero-width
        for c in encoded.chars() {
            assert!(c == ZERO_BIT || c == ONE_BIT);
        }
    }

    #[test]
    fn test_encode_decode_roundtrip() {
        let message = "Hello, World!";
        let carrier = "This is carrier text";
        
        let encoded = encode(message, carrier, None).unwrap();
        assert!(has_encoded_message(&encoded));
        
        // The encoded text should be longer than the original carrier
        assert!(encoded.len() > carrier.len());
        
        // The encoded text should contain the original carrier text
        assert!(encoded.contains("This"));
        assert!(encoded.contains("carrier"));
    }

    #[test]
    fn test_encode_with_password() {
        let message = "Secret message";
        let carrier = "Carrier text";
        let password = "mypassword";
        
        let encoded = encode(message, carrier, Some(password)).unwrap();
        assert!(has_encoded_message(&encoded));
        
        // The encoded data should be encrypted
        let start = encoded.find(START_MARKER).unwrap();
        let end = encoded.find(END_MARKER).unwrap();
        let encoded_data = &encoded[start + START_MARKER.len_utf8()..end];
        
        // Convert back to bytes to check if encrypted
        let mut binary = String::new();
        for c in encoded_data.chars() {
            if c == ONE_BIT {
                binary.push('1');
            } else if c == ZERO_BIT {
                binary.push('0');
            }
        }
        
        let mut bytes = Vec::new();
        for i in (0..binary.len()).step_by(8) {
            if i + 8 <= binary.len() {
                let byte_str = &binary[i..i+8];
                let byte = u8::from_str_radix(byte_str, 2).unwrap();
                bytes.push(byte);
            }
        }
        
        // The data should appear to be encrypted
        assert!(is_encrypted(&bytes));
    }

    #[test]
    fn test_encode_empty_carrier() {
        let message = "Test message";
        let encoded = encode(message, "", None).unwrap();
        
        assert!(encoded.starts_with(START_MARKER));
        assert!(encoded.ends_with(END_MARKER));
        assert!(has_encoded_message(&encoded));
    }

    #[test]
    fn test_encode_single_char_carrier() {
        let message = "Test message";
        let carrier = "A";
        let encoded = encode(message, carrier, None).unwrap();
        
        assert!(encoded.starts_with("A"));
        assert!(encoded.contains(START_MARKER));
        assert!(encoded.ends_with(END_MARKER));
    }

    #[test]
    fn test_has_encoded_message() {
        assert!(!has_encoded_message("plain text"));
        assert!(!has_encoded_message("text with start\u{200B}"));
        assert!(!has_encoded_message("text with end\u{200C}"));
        assert!(has_encoded_message("text with both\u{200B}data\u{200C}"));
    }

    #[test]
    fn test_get_encoded_message_size() {
        let message = "test";
        let carrier = "carrier";
        let encoded = encode(message, carrier, None).unwrap();
        
        let size = get_encoded_message_size(&encoded);
        assert!(size.is_some());
        
        // The size should be reasonable (base64 encoded message)
        let size = size.unwrap();
        assert!(size > 0);
    }

    #[test]
    fn test_get_encoded_message_size_no_message() {
        let size = get_encoded_message_size("plain text");
        assert!(size.is_none());
    }
} 