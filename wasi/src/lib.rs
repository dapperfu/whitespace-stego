//! WASI-compatible whitespace steganography implementation.
//!
//! This module provides the core functionality for encoding and decoding messages
//! using zero-width Unicode whitespace characters, compiled to WebAssembly.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use thiserror::Error;
use wasm_bindgen::prelude::*;

/// Error type for steganography operations
#[derive(Error, Debug)]
pub enum StegoError {
    #[error("Invalid carrier text: {0}")]
    InvalidCarrier(String),
    #[error("Decryption failed: {0}")]
    DecryptionFailed(String),
    #[error("Encoding failed: {0}")]
    EncodingFailed(String),
}

/// Zero-width characters for encoding
pub const START_MARKER: char = '\u{200B}'; // Zero-width space
pub const END_MARKER: char = '\u{200C}'; // Zero-width non-joiner
pub const ZERO_BIT: char = '\u{200D}'; // Zero-width joiner
pub const ONE_BIT: char = '\u{FEFF}'; // Zero-width no-break space

/// Convert bytes to a string of zero-width characters
fn encode_binary(data: &[u8]) -> String {
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

/// Convert a string of zero-width characters back to bytes
fn decode_binary(encoded: &str) -> Vec<u8> {
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

    result
}

/// Encode a message into carrier text using zero-width characters
fn encode_internal(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Check if password is provided (not yet supported in WASM)
    if password.is_some() {
        return Err(StegoError::EncodingFailed("Password encryption is not yet supported in the WebAssembly version. Please use the Python, Rust, or C implementations for password protection.".to_string()));
    }

    // Base64 encode the message
    let encoded = BASE64.encode(message.as_bytes());
    let data = encoded.as_bytes().to_vec();

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

/// Decode a message from carrier text containing zero-width characters
fn decode_internal(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Check if password is provided (not yet supported in WASM)
    if password.is_some() {
        return Err(StegoError::DecryptionFailed("Password decryption is not yet supported in the WebAssembly version. Please use the Python, Rust, or C implementations for password protection.".to_string()));
    }

    // Find the encoded message between markers
    let start = carrier
        .find(START_MARKER)
        .ok_or_else(|| StegoError::InvalidCarrier("No start marker found".to_string()))?;
    let end = carrier
        .find(END_MARKER)
        .ok_or_else(|| StegoError::InvalidCarrier("No end marker found".to_string()))?;

    // Use char_indices to get char boundaries
    let start_char = carrier
        .char_indices()
        .find(|&(i, c)| i == start && c == START_MARKER)
        .map(|(i, _)| i)
        .unwrap();
    let end_char = carrier
        .char_indices()
        .find(|&(i, c)| i == end && c == END_MARKER)
        .map(|(i, _)| i)
        .unwrap();
    let encoded = carrier[start_char + START_MARKER.len_utf8()..end_char].to_string();
    let data = decode_binary(&encoded);

    // Base64 decode and convert to string
    let decoded = BASE64
        .decode(&data)
        .map_err(|e| StegoError::DecryptionFailed(e.to_string()))?;
    String::from_utf8(decoded).map_err(|e| StegoError::DecryptionFailed(e.to_string()))
}

/// WASI-compatible encode function
#[wasm_bindgen]
pub fn encode(message: &str, carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    encode_internal(message, carrier, password_ref)
        .map_err(|e| JsValue::from_str(&e.to_string()))
}

/// WASI-compatible decode function
#[wasm_bindgen]
pub fn decode(carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    decode_internal(carrier, password_ref)
        .map_err(|e| JsValue::from_str(&e.to_string()))
}

/// WASI-compatible function to check if text contains encoded data
#[wasm_bindgen]
pub fn has_encoded_data(text: &str) -> bool {
    text.contains(START_MARKER) && text.contains(END_MARKER)
}

/// WASI-compatible function to get the original carrier text (without encoded data)
#[wasm_bindgen]
pub fn extract_carrier(text: &str) -> Result<String, JsValue> {
    let start = text.find(START_MARKER);
    let end = text.find(END_MARKER);
    
    match (start, end) {
        (Some(start_idx), Some(end_idx)) => {
            if start_idx < end_idx {
                let start_char = text
                    .char_indices()
                    .find(|&(i, _)| i == start_idx)
                    .map(|(i, _)| i)
                    .unwrap_or(start_idx);
                let end_char = text
                    .char_indices()
                    .find(|&(i, _)| i == end_idx)
                    .map(|(i, _)| i)
                    .unwrap_or(end_idx);
                
                let result = format!(
                    "{}{}",
                    &text[..start_char],
                    &text[end_char + END_MARKER.len_utf8()..]
                );
                Ok(result)
            } else {
                Ok(text.to_string())
            }
        }
        _ => Ok(text.to_string())
    }
} 