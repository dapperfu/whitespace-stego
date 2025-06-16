//! Core implementation of whitespace steganography.
//!
//! This module provides the core functionality for encoding and decoding messages
//! using zero-width Unicode whitespace characters.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use thiserror::Error;
use fernet::{Fernet, DecryptionError};

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
pub const END_MARKER: char = '\u{200C}';   // Zero-width non-joiner
pub const ZERO_BIT: char = '\u{200D}';     // Zero-width joiner
pub const ONE_BIT: char = '\u{FEFF}';      // Zero-width no-break space

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

/// Encrypt data using Fernet (compatible with Python cryptography.fernet)
fn encrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    let fernet = Fernet::new(&key).ok_or_else(|| StegoError::EncodingFailed("Invalid Fernet key".to_string()))?;
    Ok(fernet.encrypt(data).as_bytes().to_vec())
}

/// Decrypt data using Fernet (compatible with Python cryptography.fernet)
fn decrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    let fernet = Fernet::new(&key).ok_or_else(|| StegoError::DecryptionFailed("Invalid Fernet key".to_string()))?;
    let data_str = std::str::from_utf8(data).map_err(|e| StegoError::DecryptionFailed(e.to_string()))?;
    fernet.decrypt(data_str).map_err(|e| StegoError::DecryptionFailed(e.to_string()))
}

/// Derive a Fernet key from a password (base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32]))
fn derive_fernet_key(password: &str) -> String {
    use base64::{engine::general_purpose::URL_SAFE_NO_PAD, Engine as _};
    let mut key_bytes = [0u8; 32];
    let pw_bytes = password.as_bytes();
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

/// Encode a message into carrier text using zero-width characters
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
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

/// Decode a message from carrier text containing zero-width characters
pub fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Find the encoded message between markers
    let start = carrier.find(START_MARKER).ok_or_else(|| {
        StegoError::InvalidCarrier("No start marker found".to_string())
    })?;
    let end = carrier.find(END_MARKER).ok_or_else(|| {
        StegoError::InvalidCarrier("No end marker found".to_string())
    })?;

    // Use char_indices to get char boundaries
    let start_char = carrier.char_indices().find(|&(i, c)| i == start && c == START_MARKER).map(|(i, _)| i).unwrap();
    let end_char = carrier.char_indices().find(|&(i, c)| i == end && c == END_MARKER).map(|(i, _)| i).unwrap();
    let encoded = carrier[start_char + START_MARKER.len_utf8()..end_char].to_string();
    let mut data = decode_binary(&encoded);

    // Decrypt if password provided
    if let Some(pwd) = password {
        data = decrypt_data(&data, pwd)?;
    }

    // Base64 decode and convert to string
    let decoded = BASE64.decode(&data)
        .map_err(|e| StegoError::DecryptionFailed(e.to_string()))?;
    String::from_utf8(decoded)
        .map_err(|e| StegoError::DecryptionFailed(e.to_string()))
}

/// Extract the encoded message and remaining carrier text
pub fn extract_encoded(carrier: &str) -> Result<(String, String), StegoError> {
    let start = carrier.find(START_MARKER).ok_or_else(|| {
        StegoError::InvalidCarrier("No start marker found".to_string())
    })?;
    let end = carrier.find(END_MARKER).ok_or_else(|| {
        StegoError::InvalidCarrier("No end marker found".to_string())
    })?;
    let start_char = carrier.char_indices().find(|&(i, c)| i == start && c == START_MARKER).map(|(i, _)| i).unwrap();
    let end_char = carrier.char_indices().find(|&(i, c)| i == end && c == END_MARKER).map(|(i, _)| i).unwrap();
    let encoded = carrier[start_char..=end_char + END_MARKER.len_utf8() - 1].to_string();
    let remaining = format!("{}{}", &carrier[..start_char], &carrier[end_char + END_MARKER.len_utf8()..]);
    Ok((encoded, remaining))
}

#[cfg(test)]
mod tests {
    use super::*;

    const MESSAGES: &[&str] = &[
        "Hello, World!",
        "Test message with emoji 😀",
        "Multilingual text: 你好, 世界!",
        "Special chars: !@#$%^&*()",
        "",  // Empty message
    ];

    const PASSWORDS: &[Option<&str>] = &[
        None,
        Some("simple_password"),
        Some("complex_password_123!@#"),
        Some(""),  // Empty password
    ];

    const CARRIERS: &[&str] = &[
        "",  // Empty carrier
        "Simple carrier text",
        "Carrier with emoji 🎉",
        "Multilingual carrier: 你好",
    ];

    #[test]
    fn test_encode_decode() {
        for &message in MESSAGES {
            for &password in PASSWORDS {
                for &carrier in CARRIERS {
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password).unwrap();
                    assert_eq!(decoded, message);
                }
            }
        }
    }

    #[test]
    fn test_empty_carrier() {
        for &message in MESSAGES {
            let encoded = encode(message, "", None).unwrap();
            assert!(encoded.contains(START_MARKER));
            assert!(encoded.contains(END_MARKER));
            assert!(encoded.len() > message.len());
        }
    }

    #[test]
    fn test_invalid_decode() {
        for &carrier in CARRIERS {
            assert!(decode(carrier, None).is_err());
        }
    }

    #[test]
    fn test_extract_encoded() {
        for &message in MESSAGES {
            for &carrier in CARRIERS {
                let encoded = encode(message, carrier, None).unwrap();
                let (extracted, remaining) = extract_encoded(&encoded).unwrap();
                assert!(extracted.contains(START_MARKER));
                assert!(extracted.contains(END_MARKER));
                if !carrier.is_empty() {
                    assert_eq!(remaining, &carrier[1..]);
                }
            }
        }
    }

    #[test]
    fn test_password_mismatch() {
        for &message in MESSAGES {
            let password = Some("test_password");
            let encoded = encode(message, "", password).unwrap();
            assert!(decode(&encoded, Some("wrong_password")).is_err());
        }
    }
} 