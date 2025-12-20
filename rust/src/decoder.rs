//! Decoding functions for whitespace steganography.

use base64::{engine::general_purpose, Engine as _};

use crate::constants::{BIT_0, BIT_1, CONTROL_END, CONTROL_START};
use crate::errors::StegoError;

/// Decode a message from invisible Unicode characters.
///
/// # Arguments
///
/// * `encoded_text` - Text containing the encoded message with control markers.
///
/// # Returns
///
/// The decoded original message string.
///
/// # Errors
///
/// Returns various `StegoError` variants for different failure modes:
/// - `MissingMarker` if CONTROL_START or CONTROL_END markers are missing
/// - `InvalidPayload` if payload contains invalid characters
/// - `InvalidBase64` if Base64 decoding fails
/// - `InvalidUTF8` if UTF-8 decoding fails
/// - `Decoding` for other decoding errors
pub fn decode(encoded_text: &str) -> Result<String, StegoError> {
    // Find control markers
    let start_idx = encoded_text
        .find(CONTROL_START)
        .ok_or_else(|| StegoError::MissingMarker("CONTROL_START marker (U+2060) not found".to_string()))?;
    let end_idx = encoded_text
        .find(CONTROL_END)
        .ok_or_else(|| StegoError::MissingMarker("CONTROL_END marker (U+2063) not found".to_string()))?;

    // Extract payload (between markers, excluding markers)
    let payload_start = start_idx + CONTROL_START.len_utf8();
    let payload = &encoded_text[payload_start..end_idx];

    // Check if payload is empty
    if payload.is_empty() {
        // Empty payload means empty message
        return Ok(String::new());
    }

    // Convert invisible characters to binary bits
    let mut binary_bits = String::new();
    for char in payload.chars() {
        match char {
            c if c == BIT_0 => binary_bits.push('0'),
            c if c == BIT_1 => binary_bits.push('1'),
            _ => {
                return Err(StegoError::InvalidPayload(format!(
                    "Invalid character in payload: U+{:04X}. Only U+200B and U+200C are allowed.",
                    char as u32
                )))
            }
        }
    }

    // Check if payload is complete (divisible by 8)
    if binary_bits.len() % 8 != 0 {
        return Err(StegoError::Decoding(format!(
            "Incomplete payload: {} bits (must be divisible by 8)",
            binary_bits.len()
        )));
    }

    // Group bits into 8-bit bytes
    let mut bytes_list = Vec::new();
    for i in (0..binary_bits.len()).step_by(8) {
        let byte_bits = &binary_bits[i..i + 8];
        let byte_value = u8::from_str_radix(byte_bits, 2)
            .map_err(|e| StegoError::Decoding(format!("Invalid binary: {}", e)))?;
        bytes_list.push(byte_value);
    }

    // Convert bytes to Base64 string
    let base64_str = String::from_utf8(bytes_list.clone())
        .map_err(|e| StegoError::InvalidBase64(format!("Invalid Base64 data: {}", e)))?;

    // Decode Base64 to UTF-8 bytes
    let utf8_bytes = general_purpose::STANDARD
        .decode(&base64_str)
        .map_err(|e| StegoError::InvalidBase64(format!("Base64 decoding failed: {}", e)))?;

    // Decode UTF-8 bytes to original message
    let message = String::from_utf8(utf8_bytes)
        .map_err(|e| StegoError::InvalidUTF8(format!("UTF-8 decoding failed: {}", e)))?;

    Ok(message)
}

