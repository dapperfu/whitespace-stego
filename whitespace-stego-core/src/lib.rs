//! Core whitespace steganography logic for Rust and FFI consumers.

use base64::Engine;
use fernet::{DecryptionError, Fernet};

const START_MARKER: &str = "\u{200b}";  // Zero-width space
const END_MARKER: &str = "\u{200c}";    // Zero-width non-joiner
const ZERO_BIT: &str = "\u{200d}";      // Zero-width joiner
const ONE_BIT: &str = "\u{feff}";       // Zero-width no-break space

/// Errors for steganography operations.
#[derive(Debug)]
pub enum StegoError {
    InvalidKey,
    DecryptionError(DecryptionError),
    NoMessageFound,
    Utf8Error,
    Base64Error,
}

impl std::fmt::Display for StegoError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            StegoError::InvalidKey => write!(f, "Invalid key"),
            StegoError::DecryptionError(e) => write!(f, "Decryption error: {}", e),
            StegoError::NoMessageFound => write!(f, "No valid message found in carrier text"),
            StegoError::Utf8Error => write!(f, "Invalid UTF-8 in message"),
            StegoError::Base64Error => write!(f, "Base64 decode error"),
        }
    }
}

impl std::error::Error for StegoError {}

/// Convert bytes to a string of zero-width characters.
fn encode_binary(data: &[u8]) -> String {
    let mut result = String::new();
    for &byte in data {
        for i in 0..8 {
            let bit = (byte >> (7 - i)) & 1;
            if bit == 1 {
                result.push_str(ONE_BIT);
            } else {
                result.push_str(ZERO_BIT);
            }
        }
    }
    result
}

/// Convert a string of zero-width characters back to bytes.
fn decode_binary(encoded: &str) -> Result<Vec<u8>, StegoError> {
    let mut binary = String::new();
    for ch in encoded.chars() {
        if ch.to_string() == ONE_BIT {
            binary.push('1');
        } else if ch.to_string() == ZERO_BIT {
            binary.push('0');
        }
    }
    
    if binary.len() % 8 != 0 {
        return Err(StegoError::Base64Error);
    }
    
    let mut result = Vec::new();
    for i in (0..binary.len()).step_by(8) {
        let byte_str = &binary[i..i+8];
        let byte = u8::from_str_radix(byte_str, 2)
            .map_err(|_| StegoError::Base64Error)?;
        result.push(byte);
    }
    Ok(result)
}

/// Encode a message into a carrier string, optionally encrypting with a password.
///
/// # Arguments
/// * `message` - The message to encode.
/// * `carrier` - The carrier text to hide the message in.
/// * `password` - Optional password for encryption.
///
/// # Returns
/// Encoded carrier string with the message hidden.
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Base64 encode the message
    let encoded = base64::engine::general_purpose::STANDARD.encode(message.as_bytes());
    
    // Add password encryption if provided
    let final_data = if let Some(pwd) = password {
        let mut key_bytes = pwd.as_bytes().to_vec();
        key_bytes.resize(32, 0); // Pad to 32 bytes
        let key = base64::engine::general_purpose::URL_SAFE.encode(&key_bytes);
        let fernet = Fernet::new(&key).ok_or(StegoError::InvalidKey)?;
        fernet.encrypt(encoded.as_bytes()).into_bytes()
    } else {
        encoded.into_bytes()
    };
    
    // Convert to zero-width characters
    let zero_width = encode_binary(&final_data);
    
    // Add markers
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);
    
    // Return just the encoded message if no carrier
    if carrier.is_empty() {
        return Ok(encoded_message);
    }
    
    // Embed in carrier after first Unicode character
    let chars: Vec<char> = carrier.chars().collect();
    if chars.len() > 1 {
        let mut result = String::new();
        result.push(chars[0]);
        result.push_str(&encoded_message);
        result.extend(chars[1..].iter());
        Ok(result)
    } else {
        Ok(format!("{}{}", carrier, encoded_message))
    }
}

/// Decode a message from a carrier string, optionally decrypting with a password.
///
/// # Arguments
/// * `carrier` - The carrier text containing the hidden message.
/// * `password` - Optional password for decryption.
///
/// # Returns
/// The decoded message as a string.
pub fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Find the encoded message between markers
    let start = carrier.find(START_MARKER).ok_or(StegoError::NoMessageFound)?;
    let end = carrier.find(END_MARKER).ok_or(StegoError::NoMessageFound)?;
    
    // Extract the encoded message
    let encoded = &carrier[start + START_MARKER.len()..end];
    
    // Convert from zero-width characters to bytes
    let data = decode_binary(encoded)?;
    
    // Decrypt if password provided
    let decoded_data = if let Some(pwd) = password {
        let mut key_bytes = pwd.as_bytes().to_vec();
        key_bytes.resize(32, 0); // Pad to 32 bytes
        let key = base64::engine::general_purpose::URL_SAFE.encode(&key_bytes);
        let fernet = Fernet::new(&key).ok_or(StegoError::InvalidKey)?;
        fernet.decrypt(&String::from_utf8(data).map_err(|_| StegoError::Utf8Error)?)
            .map_err(StegoError::DecryptionError)?
    } else {
        data
    };
    
    // Base64 decode and convert to string
    let result = base64::engine::general_purpose::STANDARD.decode(&decoded_data)
        .map_err(|_| StegoError::Base64Error)?;
    String::from_utf8(result).map_err(|_| StegoError::Utf8Error)
} 