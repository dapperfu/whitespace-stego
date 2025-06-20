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

#[cfg(test)]
mod tests {
    use super::*;

    // Test data for different character types
    const ASCII_MESSAGES: &[&str] = &[
        "Hello, World!",
        "This is a simple ASCII message",
        "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?",
        "Numbers: 0123456789",
        "Mixed case: Hello World 123 !@#",
        "", // Empty message
    ];

    const UNICODE_MESSAGES: &[&str] = &[
        "你好，世界！", // Chinese
        "こんにちは、世界！", // Japanese
        "안녕하세요, 세계!", // Korean
        "Привет, мир!", // Russian
        "مرحبا بالعالم!", // Arabic
        "नमस्ते दुनिया!", // Hindi
        "สวัสดีชาวโลก!", // Thai
        "Γεια σου κόσμε!", // Greek
        "Hola mundo!", // Spanish with accent
        "Café résumé naïve", // French with accents
        "München Zürich", // German with umlauts
        "ÆØÅ æøå", // Nordic characters
        "Café résumé naïve Münchën Zürich ÆØÅ æøå", // Mixed international
    ];

    const EMOJI_MESSAGES: &[&str] = &[
        "Hello 🌍!",
        "Test message with emoji 😀",
        "Multiple emojis: 🚀🎉🎊🎈🎁",
        "Animals: 🐶🐱🐭🐹🐰🦊🐻🐼",
        "Food: 🍕🍔🍟🌭🍿🧂🥨🥖",
        "Nature: 🌸🌺🌻🌼🌷🌹🌱🌲",
        "Weather: ☀️🌤️⛅🌥️☁️🌦️🌧️⛈️",
        "Activities: ⚽🏀🏈⚾🎾🏐🏉🎱",
        "Mixed: Hello 你好 🌍! Test 测试 🎉",
        "Complex: 🚀🎉🎊🎈🎁🐶🐱🐭🐹🐰🦊🐻🐼🍕🍔🍟🌭🍿🧂🥨🥖🌸🌺🌻🌼🌷🌹🌱🌲☀️🌤️⛅🌥️☁️🌦️🌧️⛈️⚽🏀🏈⚾🎾🏐🏉🎱",
    ];

    const ASCII_CARRIERS: &[&str] = &[
        "Simple carrier text",
        "This is a normal paragraph that could contain any text.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "The quick brown fox jumps over the lazy dog.",
        "A simple sentence.",
        "", // Empty carrier
    ];

    const UNICODE_CARRIERS: &[&str] = &[
        "你好世界", // Chinese
        "こんにちは世界", // Japanese
        "안녕하세요세계", // Korean
        "Привет мир", // Russian
        "مرحبا بالعالم", // Arabic
        "नमस्ते दुनिया", // Hindi
        "สวัสดีชาวโลก", // Thai
        "Γεια σου κόσμε", // Greek
        "Hola mundo", // Spanish
        "Bonjour le monde", // French
        "Hallo Welt", // German
        "Hej världen", // Swedish
        "Mixed international text: 你好 こんにちは 안녕하세요 Привет مرحبا नमस्ते สวัสดี Γεια Hola Bonjour Hallo Hej",
    ];

    const EMOJI_CARRIERS: &[&str] = &[
        "Hello 🌍!",
        "Carrier with emoji 🎉",
        "Multiple emojis: 🚀🎉🎊🎈🎁",
        "Animals: 🐶🐱🐭🐹🐰🦊🐻🐼",
        "Food: 🍕🍔🍟🌭🍿🧂🥨🥖",
        "Nature: 🌸🌺🌻🌼🌷🌹🌱🌲",
        "Weather: ☀️🌤️⛅🌥️☁️🌦️🌧️⛈️",
        "Activities: ⚽🏀🏈⚾🎾🏐🏉🎱",
        "Mixed: Hello 你好 🌍! Test 测试 🎉",
        "Complex: 🚀🎉🎊🎈🎁🐶🐱🐭🐹🐰🦊🐻🐼🍕🍔🍟🌭🍿🧂🥨🥖🌸🌺🌻🌼🌷🌹🌱🌲☀️🌤️⛅🌥️☁️🌦️🌧️⛈️⚽🏀🏈⚾🎾🏐🏉🎱",
    ];

    #[test]
    fn test_ascii_roundtrip() {
        for &message in ASCII_MESSAGES {
            for &carrier in ASCII_CARRIERS {
                let encoded = encode_internal(message, carrier, None).unwrap();
                let decoded = decode_internal(&encoded, None).unwrap();
                assert_eq!(decoded, message, "ASCII roundtrip failed for message: '{}', carrier: '{}'", message, carrier);
            }
        }
    }

    #[test]
    fn test_unicode_roundtrip() {
        for &message in UNICODE_MESSAGES {
            for &carrier in UNICODE_CARRIERS {
                let encoded = encode_internal(message, carrier, None).unwrap();
                let decoded = decode_internal(&encoded, None).unwrap();
                assert_eq!(decoded, message, "Unicode roundtrip failed for message: '{}', carrier: '{}'", message, carrier);
            }
        }
    }

    #[test]
    fn test_emoji_roundtrip() {
        for &message in EMOJI_MESSAGES {
            for &carrier in EMOJI_CARRIERS {
                let encoded = encode_internal(message, carrier, None).unwrap();
                let decoded = decode_internal(&encoded, None).unwrap();
                assert_eq!(decoded, message, "Emoji roundtrip failed for message: '{}', carrier: '{}'", message, carrier);
            }
        }
    }

    #[test]
    fn test_mixed_character_roundtrip() {
        let mixed_messages = [
            "Hello 你好 🌍!",
            "Test 测试 🎉 message",
            "ASCII + Unicode + Emoji: Hello 你好 🌍!",
            "Complex: 🚀🎉🎊🎈🎁 你好 こんにちは 안녕하세요 Привет مرحبا नमस्ते สวัสดี Γεια Hola Bonjour Hallo Hej",
        ];

        let mixed_carriers = [
            "Simple ASCII carrier",
            "Unicode carrier: 你好世界",
            "Emoji carrier: 🌍🎉",
            "Mixed carrier: Hello 你好 🌍! Test 测试 🎉",
        ];

        for &message in &mixed_messages {
            for &carrier in &mixed_carriers {
                let encoded = encode_internal(message, carrier, None).unwrap();
                let decoded = decode_internal(&encoded, None).unwrap();
                assert_eq!(decoded, message, "Mixed character roundtrip failed for message: '{}', carrier: '{}'", message, carrier);
            }
        }
    }

    #[test]
    fn test_edge_cases() {
        // Empty message and carrier
        let encoded = encode_internal("", "", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, "");

        // Empty message, non-empty carrier
        let encoded = encode_internal("", "Hello", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, "");

        // Non-empty message, empty carrier
        let encoded = encode_internal("Hello", "", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, "Hello");

        // Single character carrier
        let encoded = encode_internal("Test", "A", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, "Test");

        // Very long message
        let long_message = "A".repeat(1000);
        let encoded = encode_internal(&long_message, "Carrier", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, long_message);

        // Very long carrier
        let long_carrier = "Carrier".repeat(100);
        let encoded = encode_internal("Test", &long_carrier, None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, "Test");
    }

    #[test]
    fn test_has_encoded_data() {
        // Test with encoded data
        let encoded = encode_internal("Test", "Hello", None).unwrap();
        assert!(has_encoded_data(&encoded));

        // Test without encoded data
        assert!(!has_encoded_data("Hello, World!"));
        assert!(!has_encoded_data(""));
        assert!(!has_encoded_data("Hello 你好 🌍!"));
    }

    #[test]
    fn test_extract_carrier() {
        let original_carrier = "Hello, World!";
        let encoded = encode_internal("Test", original_carrier, None).unwrap();
        let extracted = extract_carrier(&encoded).unwrap();
        assert_eq!(extracted, original_carrier);

        // Test with Unicode carrier
        let unicode_carrier = "你好世界";
        let encoded = encode_internal("Test", unicode_carrier, None).unwrap();
        let extracted = extract_carrier(&encoded).unwrap();
        assert_eq!(extracted, unicode_carrier);

        // Test with emoji carrier
        let emoji_carrier = "Hello 🌍!";
        let encoded = encode_internal("Test", emoji_carrier, None).unwrap();
        let extracted = extract_carrier(&encoded).unwrap();
        assert_eq!(extracted, emoji_carrier);
    }

    #[test]
    fn test_password_not_supported() {
        // Test that password encryption is not supported
        let result = encode_internal("Test", "Hello", Some("password"));
        assert!(result.is_err());
        assert!(result.unwrap_err().to_string().contains("not yet supported"));

        // Test that password decryption is not supported
        let encoded = encode_internal("Test", "Hello", None).unwrap();
        let result = decode_internal(&encoded, Some("password"));
        assert!(result.is_err());
        assert!(result.unwrap_err().to_string().contains("not yet supported"));
    }

    #[test]
    fn test_invalid_decode() {
        // Test decoding text without encoded data
        let result = decode_internal("Hello, World!", None);
        assert!(result.is_err());
        assert!(result.unwrap_err().to_string().contains("No start marker found"));

        // Test decoding empty string
        let result = decode_internal("", None);
        assert!(result.is_err());
        assert!(result.unwrap_err().to_string().contains("No start marker found"));
    }

    #[test]
    fn test_binary_data_roundtrip() {
        // Test with binary-like data (Base64 encoded)
        let binary_message = "SGVsbG8gV29ybGQh"; // "Hello World!" in Base64
        let encoded = encode_internal(binary_message, "Carrier", None).unwrap();
        let decoded = decode_internal(&encoded, None).unwrap();
        assert_eq!(decoded, binary_message);
    }

    #[test]
    fn test_special_unicode_characters() {
        let special_messages = [
            "Zero-width characters: \u{200B}\u{200C}\u{200D}\u{FEFF}",
            "Combining characters: e\u{0301} (é)",
            "Surrogate pairs: \u{1F600}", // 😀
            "Variation selectors: \u{FE0F}",
            "Right-to-left: \u{202E}Hello\u{202C}",
            "Bidirectional: \u{202A}Hello\u{202C}",
        ];

        let special_carriers = [
            "Normal carrier",
            "Carrier with special chars: \u{200B}\u{200C}",
            "Mixed: Hello \u{1F600} 你好",
        ];

        for &message in &special_messages {
            for &carrier in &special_carriers {
                let encoded = encode_internal(message, carrier, None).unwrap();
                let decoded = decode_internal(&encoded, None).unwrap();
                assert_eq!(decoded, message, "Special Unicode roundtrip failed for message: '{}', carrier: '{}'", message, carrier);
            }
        }
    }
} 