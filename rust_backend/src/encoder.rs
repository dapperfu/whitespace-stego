use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{binary_to_char, START_MARKER, END_MARKER, is_valid_carrier, strip_zero_width_and_control};
use aes_gcm::{
    aead::{Aead, KeyInit, AeadInPlace},
    Aes256Gcm, Key, Nonce,
};
use pbkdf2::Pbkdf2;
use pbkdf2::password_hash::{PasswordHasher, SaltString};
use rand::{Rng, rngs::OsRng, distributions::Alphanumeric};
use std::io::{self, Write};
use hex;
use hmac::Hmac;
use sha2::Sha256;

const SALT_LENGTH: usize = 16;
const IV_LENGTH: usize = 12;
#[allow(dead_code)]
const TAG_LENGTH: usize = 16;
#[allow(dead_code)]
const KEY_LENGTH: usize = 32; // 256 bits
#[allow(dead_code)]
const ITERATIONS: u32 = 100_000;

/// Generate a random salt string of a given length using only [A-Za-z0-9./].
///
/// # Arguments
///
/// * `len` - The length of the salt string to generate
///
/// # Returns
///
/// * `String` - The generated salt string
fn generate_phc_salt(len: usize) -> String {
    const PHC_CHARS: &[u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789./";
    let mut rng = OsRng;
    (0..len)
        .map(|_| {
            let idx = rng.gen_range(0..PHC_CHARS.len());
            PHC_CHARS[idx] as char
        })
        .collect()
}

/// Generate a random salt as PHC bytes.
///
/// # Arguments
///
/// * `len` - The length of the salt bytes to generate
///
/// # Returns
///
/// * `Vec<u8>` - The generated salt bytes
fn generate_phc_salt_bytes(len: usize) -> Vec<u8> {
    let mut salt = [0u8; 16];
    OsRng.fill(&mut salt);
    salt.to_vec()
}

/// Derive an encryption key from a password using PBKDF2.
///
/// # Arguments
///
/// * `password` - The password to derive the key from
/// * `salt` - Salt for key derivation
///
/// # Returns
///
/// * `Vec<u8>` - The derived key
fn derive_key(password: &str, salt: &[u8]) -> Vec<u8> {
    let mut key = vec![0u8; KEY_LENGTH];
    pbkdf2::pbkdf2::<Hmac<Sha256>>(
        password.as_bytes(),
        salt,
        ITERATIONS,
        &mut key,
    ).unwrap();
    key
}

/// Encode a binary string into zero-width characters.
///
/// # Arguments
///
/// * `binary` - The binary string to encode
///
/// # Returns
///
/// * `Result<String, String>` - The encoded string using zero-width characters, or an error message
pub fn encode_binary(binary: &str) -> Result<String, String> {
    let mut encoded = String::new();
    for c in binary.chars() {
        let bit = c.to_digit(2).ok_or_else(|| format!("Invalid binary char: {}", c))? as u8;
        encoded.push_str(binary_to_char(bit));
    }
    Ok(encoded)
}

/// Encode a message into text.
///
/// # Arguments
///
/// * `message` - The message to encode
/// * `password` - Optional password for encryption
///
/// # Returns
///
/// * `Result<String, String>` - The text with the hidden message, or an error message
pub fn encode_message(message: &str, password: Option<&str>) -> Result<String, String> {
    let bytes = if let Some(password) = password {
        // Generate a random salt as PHC bytes
        let salt = generate_phc_salt_bytes(SALT_LENGTH);
        // Generate a random IV
        let mut iv = [0u8; IV_LENGTH];
        OsRng.fill(&mut iv);
        // Derive key using the salt
        let key = derive_key(password, &salt);
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(&key));
        let nonce = Nonce::from_slice(&iv);
        // Encrypt the message
        let mut buffer = message.as_bytes().to_vec();
        let tag = cipher.encrypt_in_place_detached(nonce, b"", &mut buffer).map_err(|e| e.to_string())?;
        // Combine salt + iv + tag + ciphertext
        let mut combined = Vec::new();
        combined.extend_from_slice(&salt);
        combined.extend_from_slice(&iv);
        combined.extend_from_slice(&tag);
        combined.extend_from_slice(&buffer);
        combined
    } else {
        message.as_bytes().to_vec()
    };
    // Base64 encode the bytes
    let encoded = BASE64.encode(&bytes);
    // Convert to binary
    let binary = encoded.as_bytes().iter()
        .map(|&b| format!("{:08b}", b))
        .collect::<String>();
    // Encode binary into zero-width characters
    let zero_width = encode_binary(&binary)?;
    // Just return the payload with markers
    Ok(format!("{}{}{}", START_MARKER, zero_width, END_MARKER))
}

/// Insert a steganographic payload into carrier text.
///
/// # Arguments
///
/// * `carrier` - The carrier text to insert the payload into
/// * `payload` - The encoded steganographic payload
/// * `position` - Position to insert the payload. If None, inserts at the end
///
/// # Returns
///
/// * `Result<String, String>` - The carrier text with the payload inserted, or an error message
pub fn insert_payload(carrier: &str, payload: &str, position: Option<usize>) -> Result<String, String> {
    if !is_valid_carrier(carrier) {
        return Err("Carrier text contains control characters".to_string());
    }

    let pos = position.unwrap_or(carrier.len());
    if pos > carrier.len() {
        return Err("Position is beyond carrier text length".to_string());
    }

    let mut result = carrier[..pos].to_string();
    result.push_str(payload);
    result.push_str(&carrier[pos..]);
    Ok(result)
}

/// Encode a message and insert it into carrier text.
///
/// # Arguments
///
/// * `message` - The message to encode
/// * `carrier` - The carrier text to insert the encoded message into
/// * `password` - Optional password for encryption
/// * `position` - Position to insert the payload. If None, inserts at the end
///
/// # Returns
///
/// * `Result<String, String>` - The carrier text with the encoded message inserted, or an error message
pub fn encode_and_insert(
    message: &str,
    carrier: &str,
    password: Option<&str>,
    position: Option<usize>,
) -> Result<String, String> {
    let payload = encode_message(message, password)?;
    insert_payload(carrier, &payload, position)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_carrier_integrity() {
        let carrier = "Secret Secret";
        let message = "Hello World";
        let result = encode_and_insert(message, carrier, None, None).unwrap();
        let carrier_after = strip_zero_width_and_control(&result);
        assert_eq!(carrier_after, carrier);
    }
} 