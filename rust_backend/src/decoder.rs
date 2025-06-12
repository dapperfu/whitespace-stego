use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{char_to_binary, START_MARKER, END_MARKER};
use aes_gcm::{
    aead::{Aead, KeyInit},
    Aes256Gcm, Key, Nonce,
};
use pbkdf2::{
    password_hash::{
        PasswordHash, PasswordVerifier, SaltString,
    },
    Pbkdf2,
};

const SALT_LENGTH: usize = 16;
const KEY_LENGTH: usize = 32; // 256 bits
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
    let salt_str = SaltString::encode_b64(salt).unwrap();
    let password_hash = Pbkdf2.hash_password_customized(
        password.as_bytes(),
        None,
        None,
        pbkdf2::Params {
            rounds: ITERATIONS,
            output_length: KEY_LENGTH,
        },
        &salt_str,
    ).unwrap();

    password_hash.hash.unwrap().as_bytes().to_vec()
}

/// Extract the steganographic payload from text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden payload
///
/// # Returns
///
/// * `Result<(String, usize, usize), String>` - A tuple containing (payload, start_pos, end_pos), or an error message
pub fn extract_payload(text: &str) -> Result<(String, usize, usize), String> {
    let start_pos = text.find(START_MARKER).ok_or("No start marker found in text")?;
    let end_pos = text[start_pos..]
        .find(END_MARKER)
        .ok_or("No end marker found in text")? + start_pos;

    let payload = text[start_pos + START_MARKER.len()..end_pos].to_string();
    Ok((payload, start_pos, end_pos + END_MARKER.len()))
}

/// Decode zero-width characters back to binary string.
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
        binary.push_str(&char_to_binary(c)?);
    }
    Ok(binary)
}

/// Convert a binary string to bytes.
pub fn binary_to_bytes(binary: &str) -> Result<Vec<u8>, String> {
    if binary.len() % 8 != 0 {
        return Err("Binary string length must be a multiple of 8".to_string());
    }
    let bytes: Vec<u8> = binary
        .as_bytes()
        .chunks(8)
        .map(|chunk| {
            let byte_str = std::str::from_utf8(chunk).unwrap();
            u8::from_str_radix(byte_str, 2).unwrap()
        })
        .collect();
    Ok(bytes)
}

/// Convert a binary string to the original message string via base64 decode.
///
/// # Arguments
///
/// * `binary` - A string of '0's and '1's representing base64 characters
///
/// # Returns
///
/// * `Result<String, String>` - The decoded base64 string, or an error message
pub fn binary_to_base64(binary: &str) -> Result<String, String> {
    let bytes = binary_to_bytes(binary)?;
    let base64_decoded = BASE64.decode(&bytes).map_err(|e| format!("Base64 decode error: {}", e))?;
    String::from_utf8(base64_decoded).map_err(|e| format!("UTF-8 decode error: {}", e))
}

/// Decode a hidden message from text.
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
    // Extract the encoded part between markers
    let start = text.find(START_MARKER).ok_or("Start marker not found")?;
    let end = text.find(END_MARKER).ok_or("End marker not found")?;
    let encoded = &text[start + START_MARKER.len()..end];

    // Decode zero-width characters to binary
    let binary = decode_binary(encoded)?;

    // Convert binary to bytes
    let mut bytes = Vec::new();
    for chunk in binary.as_bytes().chunks(8) {
        let byte = u8::from_str_radix(std::str::from_utf8(chunk).unwrap(), 2).unwrap();
        bytes.push(byte);
    }

    // Decrypt/decode the message
    let message = if let Some(password) = password {
        // Decode the base64 message
        let encrypted_data = BASE64.decode(&bytes).map_err(|e| e.to_string())?;

        // Extract salt, iv, and ciphertext
        let salt = &encrypted_data[..SALT_LENGTH];
        let iv = &encrypted_data[SALT_LENGTH..SALT_LENGTH + 12];
        let ciphertext = &encrypted_data[SALT_LENGTH + 12..];

        // Derive key using the stored salt
        let key = derive_key(password, salt);
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(&key));
        let nonce = Nonce::from_slice(iv);

        // Decrypt the message
        let plaintext = cipher.decrypt(nonce, ciphertext).map_err(|e| e.to_string())?;
        String::from_utf8(plaintext).map_err(|e| e.to_string())?
    } else {
        String::from_utf8(BASE64.decode(&bytes).map_err(|e| e.to_string())?)
            .map_err(|e| e.to_string())?
    };

    Ok(message)
}

/// Decode a hidden message and remove it from the carrier text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
/// * `password` - Optional password for decryption
///
/// # Returns
///
/// * `Result<(String, String), String>` - A tuple containing (decoded message, carrier text), or an error message
pub fn decode_and_remove(text: &str, password: Option<&str>) -> Result<(String, String), String> {
    let message = decode_message(text, password)?;

    // Remove the encoded part
    let start = text.find(START_MARKER).unwrap();
    let end = text.find(END_MARKER).unwrap() + END_MARKER.len();
    let carrier = text[..start].to_string() + &text[end..];

    Ok((message, carrier))
} 