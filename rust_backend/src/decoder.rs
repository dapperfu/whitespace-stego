use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{char_to_binary, START_MARKER, END_MARKER};
use aes_gcm::{
    aead::{Aead, KeyInit, AeadInPlace},
    Aes256Gcm, Key, Nonce,
};
use pbkdf2::Pbkdf2;
use pbkdf2::password_hash::PasswordHasher;
use rand::{Rng, rngs::OsRng};
use std::io::{self, Write};

const SALT_LENGTH: usize = 16;
const IV_LENGTH: usize = 12;
const TAG_LENGTH: usize = 16;
#[allow(dead_code)]
const KEY_LENGTH: usize = 32; // 256 bits
#[allow(dead_code)]
const ITERATIONS: u32 = 100_000;

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
    let salt_str = BASE64.encode(salt);
    let password_hash = Pbkdf2.hash_password(
        password.as_bytes(),
        &salt_str,
    ).unwrap();

    password_hash.hash.unwrap().as_bytes().to_vec()
}

/// Decode a binary string from zero-width characters.
///
/// # Arguments
///
/// * `encoded` - The encoded string using zero-width characters
///
/// # Returns
///
/// * `Result<String, String>` - The decoded binary string, or an error message
pub fn decode_binary(encoded: &str) -> Result<String, String> {
    let mut binary = String::new();
    for c in encoded.chars() {
        let bit = char_to_binary(c).ok_or_else(|| format!("Invalid zero-width char: {}", c))?;
        binary.push(if bit == 0 { '0' } else { '1' });
    }
    Ok(binary)
}

/// Convert a binary string to bytes.
///
/// # Arguments
///
/// * `binary` - The binary string to convert
///
/// # Returns
///
/// * `Result<Vec<u8>, String>` - The bytes, or an error message
fn binary_to_bytes(binary: &str) -> Result<Vec<u8>, String> {
    if binary.len() % 8 != 0 {
        return Err("Binary string length must be a multiple of 8".to_string());
    }
    let mut bytes = Vec::new();
    for chunk in binary.as_bytes().chunks(8) {
        let byte = u8::from_str_radix(
            std::str::from_utf8(chunk).map_err(|e| e.to_string())?,
            2
        ).map_err(|e| e.to_string())?;
        bytes.push(byte);
    }
    Ok(bytes)
}

/// Decode a message from text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
/// * `password` - Optional password for decryption
///
/// # Returns
///
/// * `Result<String, String>` - The decoded message, or an error message
pub fn decode_message(text: &str, password: Option<&str>) -> Result<String, String> {
    // Extract the payload
    let payload = text.split(START_MARKER)
        .nth(1)
        .ok_or_else(|| "No start marker found".to_string())?
        .split(END_MARKER)
        .next()
        .ok_or_else(|| "No end marker found".to_string())?;

    // Decode binary
    let binary = decode_binary(payload)?;

    // Convert to bytes
    let bytes = binary_to_bytes(&binary)?;

    if let Some(password) = password {
        // Treat bytes as base64 string
        let base64_str = String::from_utf8(bytes.clone()).map_err(|e| e.to_string())?;
        let encrypted_data = BASE64.decode(base64_str).map_err(|e| e.to_string())?;
        if encrypted_data.len() < SALT_LENGTH + IV_LENGTH + TAG_LENGTH {
            return Err("Invalid encrypted data length".to_string());
        }
        let salt = &encrypted_data[..SALT_LENGTH];
        let iv = &encrypted_data[SALT_LENGTH..SALT_LENGTH + IV_LENGTH];
        let tag = &encrypted_data[SALT_LENGTH + IV_LENGTH..SALT_LENGTH + IV_LENGTH + TAG_LENGTH];
        let ciphertext = &encrypted_data[SALT_LENGTH + IV_LENGTH + TAG_LENGTH..];
        let key = derive_key(password, salt);
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(&key));
        let nonce = Nonce::from_slice(iv);
        let mut buffer = ciphertext.to_vec();
        cipher.decrypt_in_place_detached(nonce, b"", &mut buffer, tag.into()).map_err(|e| e.to_string())?;
        Ok(String::from_utf8(buffer).map_err(|e| e.to_string())?)
    } else {
        // Treat bytes as base64 string, decode, then decode as UTF-8
        let base64_str = String::from_utf8(bytes).map_err(|e| e.to_string())?;
        let decoded = BASE64.decode(base64_str).map_err(|e| e.to_string())?;
        Ok(String::from_utf8(decoded).map_err(|e| e.to_string())?)
    }
}

/// Extract a steganographic payload from carrier text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
///
/// # Returns
///
/// * `Result<(String, String, String), String>` - A tuple containing (payload, prefix, suffix), or an error message
pub fn extract_payload(text: &str) -> Result<(String, String, String), String> {
    let parts: Vec<&str> = text.split(START_MARKER).collect();
    if parts.len() != 2 {
        return Err("No start marker found".to_string());
    }
    let prefix = parts[0].to_string();
    let rest: Vec<&str> = parts[1].split(END_MARKER).collect();
    if rest.len() != 2 {
        return Err("No end marker found".to_string());
    }
    let payload = rest[0].to_string();
    let suffix = rest[1].to_string();
    Ok((payload, prefix, suffix))
}

/// Decode a message and remove it from carrier text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
/// * `password` - Optional password for decryption
///
/// # Returns
///
/// * `Result<(String, String), String>` - A tuple containing (message, carrier), or an error message
pub fn decode_and_remove(text: &str, password: Option<&str>) -> Result<(String, String), String> {
    let (payload, prefix, suffix) = extract_payload(text)?;
    let message = decode_message(&format!("{}{}{}", START_MARKER, payload, END_MARKER), password)?;
    Ok((message, prefix + &suffix))
} 