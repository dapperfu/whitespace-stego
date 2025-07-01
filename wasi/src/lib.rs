//! WASI-compatible whitespace steganography implementation.
//!
//! This module provides the core functionality for encoding and decoding messages
//! using zero-width Unicode whitespace characters, compiled to WebAssembly.

use aes::Aes128;
use base64::{engine::general_purpose::{STANDARD as BASE64, URL_SAFE_NO_PAD}, Engine};
use hmac::{Hmac, Mac};
use sha2::Sha256;
use thiserror::Error;
use wasm_bindgen::prelude::*;
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;

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

/// Derive a Fernet key from a password
///
/// This function creates a Fernet key from a password by:
/// 1. Converting the password to UTF-8 bytes
/// 2. Padding or truncating to exactly 32 bytes
/// 3. Base64 URL-safe encoding without padding
///
/// This is compatible with Python's implementation:
/// `base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])`
fn derive_fernet_key(password: &str) -> String {
    let mut key_bytes = [0u8; 32];
    let pw_bytes = password.as_bytes();
    
    // Copy password bytes, truncating if longer than 32 bytes
    for (i, &b) in pw_bytes.iter().enumerate().take(32) {
        key_bytes[i] = b;
    }
    
    // If password is shorter than 32 bytes, pad with spaces (like Python's ljust)
    if pw_bytes.len() < 32 {
        for i in pw_bytes.len()..32 {
            key_bytes[i] = b' ';
        }
    }
    
    URL_SAFE_NO_PAD.encode(&key_bytes)
}

/// Fernet-compatible encryption using AES-128-CBC + PKCS7
fn fernet_encrypt(data: &[u8], key: &str) -> Result<Vec<u8>, StegoError> {
    // Decode the base64 key
    let key_bytes = URL_SAFE_NO_PAD.decode(key)
        .map_err(|e| StegoError::EncodingFailed(format!("Invalid key: {}", e)))?;
    if key_bytes.len() != 32 {
        return Err(StegoError::EncodingFailed("Invalid key length".to_string()));
    }
    // Split key into encryption and signing keys
    let encryption_key = &key_bytes[..16];
    let signing_key = &key_bytes[16..];
    // Generate random IV
    let mut iv = [0u8; 16];
    getrandom::getrandom(&mut iv)
        .map_err(|e| StegoError::EncodingFailed(format!("Failed to generate IV: {}", e)))?;
    // Encrypt the data using AES-128-CBC + PKCS7
    let cipher = Cbc::<Aes128, Pkcs7>::new_from_slices(encryption_key, &iv)
        .map_err(|e| StegoError::EncodingFailed(format!("Failed to create cipher: {}", e)))?;
    let encrypted = cipher.encrypt_vec(data);
    // Create timestamp (current time in seconds since epoch)
    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs() as u64;
    // Fernet token: version (1 byte, always 0x80), timestamp (8 bytes, big-endian), IV (16 bytes), ciphertext, HMAC (32 bytes)
    let mut token = Vec::new();
    token.push(0x80); // Fernet version
    token.extend_from_slice(&timestamp.to_be_bytes());
    token.extend_from_slice(&iv);
    token.extend_from_slice(&encrypted);
    // Calculate HMAC-SHA256
    let mut mac = Hmac::<Sha256>::new_from_slice(signing_key)
        .map_err(|e| StegoError::EncodingFailed(format!("Failed to create HMAC: {}", e)))?;
    mac.update(&token);
    let signature = mac.finalize().into_bytes();
    token.extend_from_slice(&signature);
    // Base64 encode the entire token
    Ok(BASE64.encode(&token).as_bytes().to_vec())
}

/// Fernet-compatible decryption using AES-128-CBC + PKCS7
fn fernet_decrypt(data: &[u8], key: &str) -> Result<Vec<u8>, StegoError> {
    // Decode the base64 key
    let key_bytes = URL_SAFE_NO_PAD.decode(key)
        .map_err(|e| StegoError::DecryptionFailed(format!("Invalid key: {}", e)))?;
    if key_bytes.len() != 32 {
        return Err(StegoError::DecryptionFailed("Invalid key length".to_string()));
    }
    // Split key into encryption and signing keys
    let encryption_key = &key_bytes[..16];
    let signing_key = &key_bytes[16..];
    // Decode the token
    let token_str = std::str::from_utf8(data)
        .map_err(|e| StegoError::DecryptionFailed(format!("Invalid UTF-8 in token: {}", e)))?;
    let token = BASE64.decode(token_str)
        .map_err(|e| StegoError::DecryptionFailed(format!("Invalid base64 token: {}", e)))?;
    if token.len() < 57 { // 1+8+16+32 = 57 minimum
        return Err(StegoError::DecryptionFailed("Token too short".to_string()));
    }
    // Extract components
    let version = token[0];
    if version != 0x80 {
        return Err(StegoError::DecryptionFailed("Invalid Fernet version byte".to_string()));
    }
    let _timestamp = u64::from_be_bytes(token[1..9].try_into().unwrap());
    let iv = &token[9..25];
    let sig_start = token.len() - 32;
    let ciphertext = &token[25..sig_start];
    let signature = &token[sig_start..];
    // Verify HMAC
    let mut mac = Hmac::<Sha256>::new_from_slice(signing_key)
        .map_err(|e| StegoError::DecryptionFailed(format!("Failed to create HMAC: {}", e)))?;
    mac.update(&token[..sig_start]);
    let expected_signature = mac.finalize().into_bytes();
    if signature != expected_signature.as_slice() {
        return Err(StegoError::DecryptionFailed("Invalid signature".to_string()));
    }
    // Decrypt the data using AES-128-CBC + PKCS7
    let cipher = Cbc::<Aes128, Pkcs7>::new_from_slices(encryption_key, iv)
        .map_err(|e| StegoError::DecryptionFailed(format!("Failed to create cipher: {}", e)))?;
    let decrypted = cipher.decrypt_vec(ciphertext)
        .map_err(|e| StegoError::DecryptionFailed(format!("Decryption failed: {}", e)))?;
    Ok(decrypted)
}

/// Encrypt data using Fernet
fn encrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    fernet_encrypt(data, &key)
}

/// Decrypt data using Fernet
fn decrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    fernet_decrypt(data, &key)
}

/// Check if data appears to be encrypted (Fernet encrypted data)
fn is_encrypted(data: &[u8]) -> bool {
    // Fernet tokens start with 'g' in base64
    data.len() > 0 && data[0] == b'g'
}

/// Encode a message into carrier text using zero-width characters
fn encode_internal(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    let data = if let Some(pwd) = password {
        // Encrypt the message if password is provided
        let message_bytes = message.as_bytes();
        let encrypted = encrypt_data(message_bytes, pwd)?;
        encrypted
    } else {
        // Base64 encode the message if no password
        let encoded = BASE64.encode(message.as_bytes());
        encoded.as_bytes().to_vec()
    };

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

    // Decrypt or decode based on whether data appears encrypted
    let message_bytes = if is_encrypted(&data) {
        // Data is encrypted, decrypt it
        if let Some(pwd) = password {
            decrypt_data(&data, pwd)?
        } else {
            return Err(StegoError::DecryptionFailed("Encrypted data found but no password provided".to_string()));
        }
    } else {
        // Data is base64 encoded, decode it
        BASE64
            .decode(&data)
            .map_err(|e| StegoError::DecryptionFailed(e.to_string()))?
    };

    String::from_utf8(message_bytes).map_err(|e| StegoError::DecryptionFailed(e.to_string()))
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

/// WASI-compatible function to get debug information for encoding
#[wasm_bindgen]
pub fn debug_encode(message: &str, carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    
    let (data, encoding_type, aes_key) = if let Some(pwd) = password_ref {
        // Encrypt the message if password is provided
        let message_bytes = message.as_bytes();
        let encrypted = encrypt_data(message_bytes, pwd)
            .map_err(|e| JsValue::from_str(&format!("Encryption failed: {}", e)))?;
        let key = derive_fernet_key(pwd);
        (encrypted, "Fernet Encrypted", Some(key))
    } else {
        // Base64 encode the message if no password
        let encoded = BASE64.encode(message.as_bytes());
        let data = encoded.as_bytes().to_vec();
        (data, "Base64 Encoded", None)
    };

    // Convert to zero-width characters
    let zero_width = encode_binary(&data);
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);

    // Create debug information
    let debug_info = format!(
        "=== ENCODE DEBUG INFO ===\n\
        Original Message: {}\n\
        Message Length: {} characters\n\
        Message Bytes: {:?}\n\
        Encoding Type: {}\n\
        {}: {}\n\
        Binary Representation:\n{}\n\
        Zero-width Characters: {}\n\
        Zero-width Length: {} characters\n\
        Start Marker: {} (U+200B)\n\
        End Marker: {} (U+200C)\n\
        Zero Bit: {} (U+200D)\n\
        One Bit: {} (U+FEFF)\n\
        Full Encoded Message: {}\n\
        Carrier Text: {}\n\
        Carrier Length: {} characters\n\
        Final Result Length: {} characters",
        message,
        message.len(),
        message.as_bytes(),
        encoding_type,
        if aes_key.is_some() { "Fernet Key" } else { "Base64 Encoded" },
        aes_key.unwrap_or_else(|| BASE64.encode(message.as_bytes())),
        data.iter()
            .map(|&byte| format!("{:08b}", byte))
            .collect::<Vec<_>>()
            .join(" "),
        zero_width,
        zero_width.len(),
        START_MARKER,
        END_MARKER,
        ZERO_BIT,
        ONE_BIT,
        encoded_message,
        carrier,
        carrier.len(),
        carrier.len() + encoded_message.len()
    );

    Ok(debug_info)
}

/// WASI-compatible function to get debug information for decoding
#[wasm_bindgen]
pub fn debug_decode(carrier: &str, password: Option<String>) -> Result<String, JsValue> {
    let password_ref = password.as_deref();
    
    // Find the encoded message between markers
    let start = carrier.find(START_MARKER);
    let end = carrier.find(END_MARKER);
    
    if start.is_none() || end.is_none() {
        return Err(JsValue::from_str("No encoded data found in carrier text"));
    }

    let start_idx = start.unwrap();
    let end_idx = end.unwrap();

    // Use char_indices to get char boundaries
    let start_char = carrier
        .char_indices()
        .find(|&(i, c)| i == start_idx && c == START_MARKER)
        .map(|(i, _)| i)
        .unwrap();
    let end_char = carrier
        .char_indices()
        .find(|&(i, c)| i == end_idx && c == END_MARKER)
        .map(|(i, _)| i)
        .unwrap();
    
    let encoded = carrier[start_char + START_MARKER.len_utf8()..end_char].to_string();
    let data = decode_binary(&encoded);

    // Decrypt or decode based on whether data appears encrypted
    let (message_bytes, decoding_type, aes_key) = if is_encrypted(&data) {
        // Data is encrypted, decrypt it
        if let Some(pwd) = password_ref {
            let decrypted = decrypt_data(&data, pwd)
                .map_err(|e| JsValue::from_str(&format!("Decryption failed: {}", e)))?;
            let key = derive_fernet_key(pwd);
            (decrypted, "Fernet Decrypted", Some(key))
        } else {
            return Err(JsValue::from_str("Encrypted data found but no password provided"));
        }
    } else {
        // Data is base64 encoded, decode it
        let decoded = BASE64
            .decode(&data)
            .map_err(|e| JsValue::from_str(&format!("Base64 decode error: {}", e)))?;
        (decoded, "Base64 Decoded", None)
    };

    let message = String::from_utf8(message_bytes)
        .map_err(|e| JsValue::from_str(&format!("UTF-8 decode error: {}", e)))?;

    // Create debug information
    let debug_info = format!(
        "=== DECODE DEBUG INFO ===\n\
        Carrier Text: {}\n\
        Carrier Length: {} characters\n\
        Start Marker Position: {}\n\
        End Marker Position: {}\n\
        Encoded Zero-width String: {}\n\
        Encoded Length: {} characters\n\
        Decoded Binary Data: {:?}\n\
        Binary Representation:\n{}\n\
        Decoding Type: {}\n\
        {}: {}\n\
        Final Message: {}\n\
        Message Length: {} characters\n\
        Original Carrier (without encoded data): {}\n\
        Original Carrier Length: {} characters",
        carrier,
        carrier.len(),
        start_idx,
        end_idx,
        encoded,
        encoded.len(),
        data,
        data.iter()
            .map(|&byte| format!("{:08b}", byte))
            .collect::<Vec<_>>()
            .join(" "),
        decoding_type,
        if aes_key.is_some() { "Fernet Key" } else { "Base64 Decoded" },
        aes_key.unwrap_or_else(|| String::from_utf8_lossy(&data).to_string()),
        message,
        message.len(),
        extract_carrier(carrier).unwrap_or_else(|_| "Error extracting carrier".to_string()),
        extract_carrier(carrier).unwrap_or_else(|_| "Error".to_string()).len()
    );

    Ok(debug_info)
}

/// WASI-compatible function to visualize whitespace characters
#[wasm_bindgen]
pub fn visualize_whitespace(text: &str) -> String {
    let mut result = String::new();
    result.push_str("=== WHITESPACE VISUALIZATION ===\n");
    result.push_str("Text: ");
    
    for (_i, c) in text.char_indices() {
        match c {
            START_MARKER => result.push_str("[START]"),
            END_MARKER => result.push_str("[END]"),
            ZERO_BIT => result.push_str("[0]"),
            ONE_BIT => result.push_str("[1]"),
            ' ' => result.push_str("[SPACE]"),
            '\t' => result.push_str("[TAB]"),
            '\n' => result.push_str("[NEWLINE]"),
            '\r' => result.push_str("[CR]"),
            _ => result.push(c),
        }
    }
    
    result.push_str("\n\nCharacter Analysis:\n");
    for (i, c) in text.char_indices() {
        result.push_str(&format!("Position {}: '{}' (U+{:04X})\n", i, c, c as u32));
    }
    
    result
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