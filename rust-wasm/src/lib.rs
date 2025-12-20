//! WASM bindings for whitespace steganography.

use wasm_bindgen::prelude::*;
use whitespace_stego::{decode, encode};

/// Encode a message into invisible Unicode characters.
///
/// # Arguments
///
/// * `message` - The message to encode
/// * `carrier` - Optional carrier text (null/undefined for no carrier)
///
/// # Returns
///
/// Encoded string with invisible Unicode characters
///
/// # Errors
///
/// Throws a JavaScript error if encoding fails
#[wasm_bindgen]
pub fn encode_message(message: &str, carrier: Option<String>) -> Result<String, JsValue> {
    encode(message, carrier.as_deref()).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Decode a message from invisible Unicode characters.
///
/// # Arguments
///
/// * `encoded_text` - Text containing the encoded message
///
/// # Returns
///
/// Decoded original message
///
/// # Errors
///
/// Throws a JavaScript error if decoding fails
#[wasm_bindgen]
pub fn decode_message(encoded_text: &str) -> Result<String, JsValue> {
    decode(encoded_text).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Check if a string contains encoded data.
///
/// # Arguments
///
/// * `text` - Text to check
///
/// # Returns
///
/// True if the text contains encoded data markers
#[wasm_bindgen]
pub fn has_encoded_data(text: &str) -> bool {
    text.contains('\u{2060}') && text.contains('\u{2063}')
}

