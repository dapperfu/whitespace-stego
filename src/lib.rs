//! Core implementation of whitespace steganography.
//!
//! This module provides the core functionality for encoding and decoding messages
//! using zero-width Unicode whitespace characters.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use crypto::buffer::{BufferResult, ReadBuffer, WriteBuffer};
use crypto::symmetriccipher::{Decryptor, Encryptor};
use crypto::aes::cbc_encryptor;
use crypto::aes::cbc_decryptor;
use crypto::blockmodes::PkcsPadding;
use crypto::aes::KeySize::KeySize256;
use thiserror::Error;

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

/// Encrypt data using AES-256-CBC
fn encrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_key(password);
    let iv = [0u8; 16]; // In production, use a proper IV

    let mut encryptor = cbc_encryptor(
        KeySize256,
        &key,
        &iv,
        PkcsPadding,
    );

    let mut buffer = [0; 4096];
    let mut read_buffer = crypto::buffer::RefReadBuffer::new(data);
    let mut write_buffer = crypto::buffer::RefWriteBuffer::new(&mut buffer);
    let mut result = Vec::new();

    loop {
        let result = encryptor.encrypt(&mut read_buffer, &mut write_buffer, true)
            .map_err(|e| StegoError::EncryptionFailed(e.to_string()))?;

        result.extend_from_slice(write_buffer.take_read_buffer().take_remaining());

        match result {
            BufferResult::BufferUnderflow => break,
            BufferResult::BufferOverflow => {}
        }
    }

    Ok(result)
}

/// Decrypt data using AES-256-CBC
fn decrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_key(password);
    let iv = [0u8; 16]; // In production, use a proper IV

    let mut decryptor = cbc_decryptor(
        KeySize256,
        &key,
        &iv,
        PkcsPadding,
    );

    let mut buffer = [0; 4096];
    let mut read_buffer = crypto::buffer::RefReadBuffer::new(data);
    let mut write_buffer = crypto::buffer::RefWriteBuffer::new(&mut buffer);
    let mut result = Vec::new();

    loop {
        let result = decryptor.decrypt(&mut read_buffer, &mut write_buffer, true)
            .map_err(|e| StegoError::DecryptionFailed(e.to_string()))?;

        result.extend_from_slice(write_buffer.take_read_buffer().take_remaining());

        match result {
            BufferResult::BufferUnderflow => break,
            BufferResult::BufferOverflow => {}
        }
    }

    Ok(result)
}

/// Derive a 32-byte key from a password
fn derive_key(password: &str) -> [u8; 32] {
    let mut key = [0u8; 32];
    let password_bytes = password.as_bytes();
    
    for (i, &byte) in password_bytes.iter().cycle().take(32).enumerate() {
        key[i] = byte;
    }
    
    key
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

    // Return just the encoded message if no carrier
    if carrier.is_empty() {
        return Ok(encoded_message);
    }

    // Embed in carrier after first character
    let mut result = String::with_capacity(carrier.len() + encoded_message.len());
    result.push(carrier.chars().next().unwrap());
    result.push_str(&encoded_message);
    result.push_str(&carrier[1..]);

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

    // Extract the encoded message
    let encoded = &carrier[start + 1..end];
    let mut data = decode_binary(encoded);

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

    let encoded = carrier[start..=end].to_string();
    let remaining = format!("{}{}", &carrier[..start], &carrier[end + 1..]);

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