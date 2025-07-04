//! WASI-compatible whitespace steganography implementation.
//!
//! This module provides WASM bindings for the core whitespace steganography
//! functionality, compiled to WebAssembly for use in web browsers.

use wasm_bindgen::prelude::*;
use whitespace_stego_core::{
    count_messages, decode as core_decode, decode_all, encode as core_encode, extract_encoded,
    has_encoded_message, END_MARKER, ONE_BIT, START_MARKER, ZERO_BIT,
};

/// Encode a message into carrier text using zero-width characters
///
/// # Arguments
/// * `message` - The message to encode
/// * `carrier` - The carrier text to embed the message in
/// * `password` - Optional password for encryption
///
/// # Returns
/// * `Ok(String)` - The carrier text with the encoded message embedded
/// * `Err(JsValue)` - Error message if encoding fails
#[wasm_bindgen]
pub fn encode(message: &str, carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    core_encode(message, carrier, password_ref).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Decode a message from carrier text
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
/// * `password` - Optional password for decryption
///
/// # Returns
/// * `Ok(String)` - The decoded message
/// * `Err(JsValue)` - Error message if decoding fails
#[wasm_bindgen]
pub fn decode(carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    core_decode(carrier, password_ref).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Check if the given text contains encoded data
///
/// # Arguments
/// * `text` - The text to check
///
/// # Returns
/// * `bool` - True if encoded data is found, false otherwise
#[wasm_bindgen]
pub fn has_encoded_data(text: &str) -> bool {
    has_encoded_message(text)
}

/// Extract the original carrier text without the encoded message
///
/// # Arguments
/// * `text` - The text containing encoded data
///
/// # Returns
/// * `Ok(String)` - The original carrier text
/// * `Err(JsValue)` - Error message if extraction fails
#[wasm_bindgen]
pub fn extract_carrier(text: &str) -> Result<String, JsValue> {
    let (_, carrier) = extract_encoded(text).map_err(|e| JsValue::from_str(&e.to_string()))?;
    Ok(carrier)
}

/// Count the number of encoded messages in the text
///
/// # Arguments
/// * `text` - The text to analyze
///
/// # Returns
/// * `usize` - The number of encoded messages found
#[wasm_bindgen]
pub fn count_messages_in_text(text: &str) -> usize {
    count_messages(text)
}

/// Decode all messages from the text
///
/// # Arguments
/// * `text` - The text containing encoded messages
/// * `password` - Optional password for decryption
///
/// # Returns
/// * `Ok(Vec<String>)` - Vector of decoded messages
/// * `Err(JsValue)` - Error message if decoding fails
#[wasm_bindgen]
pub fn decode_all_messages(text: &str, password: Option<String>) -> Result<Vec<String>, JsValue> {
    let password_ref = password.as_deref();
    decode_all(text, password_ref).map_err(|e| JsValue::from_str(&e.to_string()))
}

/// Debug function to visualize zero-width characters in text
///
/// # Arguments
/// * `text` - The text to visualize
///
/// # Returns
/// * `String` - Text with zero-width characters replaced with visible markers
#[wasm_bindgen]
pub fn visualize_whitespace(text: &str) -> String {
    let mut out = String::new();
    for c in text.chars() {
        match c {
            START_MARKER => {
                out.push_str("[START]");
            },
            END_MARKER => {
                out.push_str("[END]");
            },
            ZERO_BIT => {
                out.push('0');
            },
            ONE_BIT => {
                out.push('1');
            },
            _ => {
                out.push(c);
            },
        }
    }
    out
}

/// Get information about the encoded message in the text
///
/// # Arguments
/// * `text` - The text to analyze
///
/// # Returns
/// * `JsValue` - Object containing message information
#[wasm_bindgen]
pub fn get_message_info(text: &str) -> JsValue {
    let info = js_sys::Object::new();

    // Check if there's encoded data
    let has_data = has_encoded_message(text);
    js_sys::Reflect::set(&info, &"hasEncodedData".into(), &has_data.into()).unwrap();

    if has_data {
        // Count messages
        let count = count_messages(text);
        js_sys::Reflect::set(&info, &"messageCount".into(), &count.into()).unwrap();

        // Try to extract carrier
        if let Ok((encoded, carrier)) = extract_encoded(text) {
            js_sys::Reflect::set(&info, &"carrierLength".into(), &carrier.len().into()).unwrap();
            js_sys::Reflect::set(&info, &"encodedLength".into(), &encoded.len().into()).unwrap();
        }
    }

    info.into()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode_decode_roundtrip() {
        let message = "Hello, World!";
        let carrier = "This is carrier text";
        let encoded = encode(message, carrier, None).unwrap();
        let decoded = decode(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_with_password() {
        let message = "Secret message";
        let carrier = "Carrier text";
        let password = "secret_password";
        let encoded = encode(message, carrier, Some(password.to_string())).unwrap();
        let decoded = decode(&encoded, Some(password.to_string())).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_has_encoded_data() {
        let message = "Test";
        let carrier = "Carrier";
        let encoded = encode(message, carrier, None).unwrap();
        assert!(has_encoded_data(&encoded));
        assert!(!has_encoded_data("Plain text"));
    }

    #[test]
    fn test_extract_carrier() {
        let message = "Hidden";
        let carrier = "Visible text";
        let encoded = encode(message, carrier, None).unwrap();
        let extracted = extract_carrier(&encoded).unwrap();
        assert_eq!(extracted, carrier);
    }

    #[test]
    fn test_count_messages() {
        let message = "Test message";
        let carrier = "Carrier";
        let encoded = encode(message, carrier, None).unwrap();
        assert_eq!(count_messages_in_text(&encoded), 1);
        assert_eq!(count_messages_in_text("No encoded data"), 0);
    }

    #[test]
    fn test_visualize_whitespace() {
        let message = "Test";
        let carrier = "A";
        let encoded = encode(message, carrier, None).unwrap();
        let visualized = visualize_whitespace(&encoded);
        assert!(visualized.contains("[START]"));
        assert!(visualized.contains("[END]"));
        assert!(visualized.contains("0") || visualized.contains("1"));
    }
}
