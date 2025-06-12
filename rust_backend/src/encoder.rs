use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{binary_to_char, START_MARKER, END_MARKER, is_valid_carrier, strip_zero_width_and_control};
use aes_gcm::{
    aead::{Aead, KeyInit},
    Aes256Gcm, Key, Nonce,
};
use pbkdf2::{
    password_hash::{
        PasswordHasher, SaltString,
    },
    Pbkdf2,
};
use rand::{Rng, rngs::OsRng};

const SALT_LENGTH: usize = 16;
const IV_LENGTH: usize = 12;
#[allow(dead_code)]
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
    let salt_str = SaltString::encode_b64(salt).unwrap();
    let password_hash = Pbkdf2.hash_password(
        password.as_bytes(),
        &salt_str,
    ).unwrap();

    password_hash.hash.unwrap().as_bytes().to_vec()
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
/// * `carrier` - The carrier text to hide the message in
/// * `password` - Optional password for encryption
///
/// # Returns
///
/// * `Result<String, String>` - The text with the hidden message, or an error message
pub fn encode_message(message: &str, carrier: &str, password: Option<&str>) -> Result<String, String> {
    // Encrypt/encode the message
    let bytes = if let Some(password) = password {
        // Generate a random salt and IV
        let mut salt = [0u8; SALT_LENGTH];
        let mut iv = [0u8; IV_LENGTH];
        OsRng.fill(&mut salt);
        OsRng.fill(&mut iv);

        // Derive key using the salt
        let key = derive_key(password, &salt);
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(&key));
        let nonce = Nonce::from_slice(&iv);

        // Encrypt the message
        let ciphertext = cipher.encrypt(nonce, message.as_bytes()).map_err(|e| e.to_string())?;

        // Combine salt, IV, and ciphertext
        let mut combined = Vec::new();
        combined.extend_from_slice(&salt);
        combined.extend_from_slice(&iv);
        combined.extend_from_slice(&ciphertext);
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

    // Insert the encoded message into the carrier text
    let result = format!("{}{}{}{}", carrier, START_MARKER, zero_width, END_MARKER);

    Ok(result)
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
    let payload = encode_message(message, carrier, password)?;
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