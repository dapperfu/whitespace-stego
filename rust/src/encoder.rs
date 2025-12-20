//! Encoding functions for whitespace steganography.

use base64::{engine::general_purpose, Engine as _};

use crate::constants::{BIT_0, BIT_1, CONTROL_END, CONTROL_START};
use crate::errors::StegoError;

/// Encode a message into invisible Unicode characters.
///
/// # Arguments
///
/// * `message` - The message to encode. Can be any Unicode string.
/// * `carrier` - Optional carrier text to embed the encoded message in.
///               If provided, the encoded payload will be inserted after
///               the first character of the carrier text.
///
/// # Returns
///
/// A string containing the encoded message wrapped in control markers.
/// If carrier is provided, returns carrier text with encoded message embedded.
///
/// # Errors
///
/// Returns `StegoError::Encoding` if encoding fails for any reason.
pub fn encode(message: &str, carrier: Option<&str>) -> Result<String, StegoError> {
    // Convert message to UTF-8 bytes
    let utf8_bytes = message.as_bytes();

    // Encode to Base64
    let base64_str = general_purpose::STANDARD.encode(utf8_bytes);

    // Convert Base64 string to binary representation
    let mut binary_bits = String::new();
    for byte in base64_str.as_bytes() {
        // Convert each byte to 8-bit binary (MSB to LSB)
        binary_bits.push_str(&format!("{:08b}", byte));
    }

    // Map binary bits to invisible Unicode characters
    let mut encoded_payload = String::new();
    for bit in binary_bits.chars() {
        match bit {
            '0' => encoded_payload.push(BIT_0),
            '1' => encoded_payload.push(BIT_1),
            _ => {
                return Err(StegoError::Encoding(format!(
                    "Invalid bit value: {}",
                    bit
                )))
            }
        }
    }

    // Wrap payload with control markers
    let encoded_message = format!("{}{}{}", CONTROL_START, encoded_payload, CONTROL_END);

    // If carrier text is provided, embed the encoded message
    if let Some(carrier) = carrier {
        // Check if carrier contains control characters
        if carrier.contains(CONTROL_START) || carrier.contains(CONTROL_END) {
            return Err(StegoError::Encoding(
                "Carrier text contains control characters. This may cause decoding issues."
                    .to_string(),
            ));
        }
        if !carrier.is_empty() {
            // Insert after first character
            let mut result = String::new();
            result.push(carrier.chars().next().unwrap());
            result.push_str(&encoded_message);
            result.push_str(&carrier[1..]);
            return Ok(result);
        }
    }

    Ok(encoded_message)
}

