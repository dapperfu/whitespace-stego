//! Cryptographic operations for whitespace steganography.
//!
//! This module provides encryption and decryption functionality using AES-256-CBC,
//! which is compatible with the C and Python implementations.

use crate::error::StegoError;
use aes::Aes256;
use block_modes::block_padding::Pkcs7;
use block_modes::{BlockMode, Cbc};
use sha2::{Digest, Sha256};

type Aes256Cbc = Cbc<Aes256, Pkcs7>;

/// Derive a 32-byte key from password using SHA-256 (same as C/Python implementation).
///
/// This function creates a 32-byte key from a password by:
/// 1. Converting the password to UTF-8 bytes
/// 2. Computing SHA-256 hash of the password bytes
///
/// This is compatible with the C and Python implementations.
///
/// # Arguments
/// * `password` - The password to derive the key from
///
/// # Returns
/// A 32-byte key derived from the password
///
/// # Examples
/// ```
/// let key = derive_key("my_password");
/// assert_eq!(key.len(), 32);
/// ```
pub fn derive_key(password: &str) -> [u8; 32] {
    let mut hasher = Sha256::new();
    hasher.update(password.as_bytes());
    let result = hasher.finalize();
    result.into()
}

/// Encrypt data using AES-256-CBC (same as C/Python implementation).
///
/// # Arguments
/// * `data` - The data to encrypt
/// * `password` - The password to derive the encryption key from
///
/// # Returns
/// The encrypted data as bytes (IV + ciphertext)
///
/// # Errors
/// Returns `StegoError::EncodingFailed` if encryption fails
///
/// # Examples
/// ```
/// let encrypted = encrypt_data(b"secret", "password")?;
/// ```
pub fn encrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_key(password);

    // Generate random IV
    let mut iv = [0u8; 16];
    getrandom::getrandom(&mut iv).map_err(|e| StegoError::EncodingFailed {
        message: format!("Failed to generate IV: {}", e).into(),
    })?;

    // Create cipher
    let cipher = Aes256Cbc::new_from_slices(&key, &iv).map_err(|e| StegoError::EncodingFailed {
        message: format!("Failed to create cipher: {}", e).into(),
    })?;

    // Encrypt
    let ciphertext = cipher.encrypt_vec(data);

    // Return IV + ciphertext
    let mut result = Vec::with_capacity(16 + ciphertext.len());
    result.extend_from_slice(&iv);
    result.extend_from_slice(&ciphertext);

    Ok(result)
}

/// Decrypt data using AES-256-CBC (same as C/Python implementation).
///
/// # Arguments
/// * `data` - The encrypted data (IV + ciphertext)
/// * `password` - The password to derive the decryption key from
///
/// # Returns
/// The decrypted data as bytes
///
/// # Errors
/// Returns `StegoError::DecryptionFailed` if decryption fails
///
/// # Examples
/// ```
/// let decrypted = decrypt_data(&encrypted_data, "password")?;
/// ```
pub fn decrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    if data.len() < 16 {
        return Err(StegoError::DecryptionFailed {
            message: "Invalid encrypted data: too short".to_string(),
        });
    }

    let key = derive_key(password);

    // Extract IV and ciphertext
    let iv = &data[..16];
    let ciphertext = &data[16..];

    // Create cipher
    let cipher =
        Aes256Cbc::new_from_slices(&key, iv).map_err(|e| StegoError::DecryptionFailed {
            message: format!("Failed to create cipher: {}", e).into(),
        })?;

    // Decrypt
    cipher
        .decrypt_vec(ciphertext)
        .map_err(|e| StegoError::DecryptionFailed {
            message: format!("Decryption failed: {}", e).into(),
        })
}

/// Check if data appears to be encrypted (has minimum length for IV + ciphertext).
///
/// # Arguments
/// * `data` - The data to check
///
/// # Returns
/// `true` if the data appears to be encrypted
///
/// # Examples
/// ```
/// assert!(!is_encrypted(b"plain text"));
/// assert!(is_encrypted(&encrypted_data));
/// ```
pub fn is_encrypted(data: &[u8]) -> bool {
    if data.len() < 16 {
        return false; // Too short to be encrypted
    }

    // If data is >= 16 bytes, check if it looks like base64 (unencrypted) vs random bytes (encrypted)
    // Base64 data will have a high percentage of printable ASCII characters
    let printable_count = data.iter().filter(|&&b| b >= 32 && b <= 126).count();
    let printable_ratio = printable_count as f64 / data.len() as f64;

    // If more than 90% of bytes are printable ASCII, it's likely base64 (unencrypted)
    // If less than 90% are printable, it's likely encrypted random bytes
    printable_ratio < 0.9
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_derive_key() {
        // Test that keys are always 32 bytes
        let key1 = derive_key("short");
        assert_eq!(key1.len(), 32);

        let key2 = derive_key("this_is_a_very_long_password_that_should_be_hashed");
        assert_eq!(key2.len(), 32);

        let key3 = derive_key("");
        assert_eq!(key3.len(), 32);

        // Test that same password produces same key
        let key4a = derive_key("test_password");
        let key4b = derive_key("test_password");
        assert_eq!(key4a, key4b);

        // Test that different passwords produce different keys
        let key5a = derive_key("password1");
        let key5b = derive_key("password2");
        assert_ne!(key5a, key5b);
    }

    #[test]
    fn test_encrypt_decrypt_roundtrip() {
        let data = b"super secret message";
        let password = "test_password_123";

        let encrypted = encrypt_data(data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();

        assert_eq!(decrypted, data);
    }

    #[test]
    fn test_encrypt_decrypt_wrong_password() {
        let data = b"super secret message";
        let password = "correct_password";
        let wrong_password = "wrong_password";

        let encrypted = encrypt_data(data, password).unwrap();
        let result = decrypt_data(&encrypted, wrong_password);

        assert!(result.is_err());
        assert!(matches!(
            result.unwrap_err(),
            StegoError::DecryptionFailed { .. }
        ));
    }

    #[test]
    fn test_encrypt_decrypt_empty_data() {
        let data = b"";
        let password = "test_password";

        let encrypted = encrypt_data(data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();

        assert_eq!(decrypted, data);
    }

    #[test]
    fn test_encrypt_decrypt_unicode_data() {
        let data = "Hello, 世界! 🌍".as_bytes();
        let password = "unicode_password";

        let encrypted = encrypt_data(data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();

        assert_eq!(decrypted, data);
    }

    #[test]
    fn test_is_encrypted() {
        let plain_data = b"not encrypted";
        assert!(!is_encrypted(plain_data));

        let encrypted_data = encrypt_data(b"secret", "password").unwrap();
        assert!(is_encrypted(&encrypted_data));
    }

    #[test]
    fn test_derive_key_unicode() {
        // Test that Unicode passwords work correctly
        let key1 = derive_key("password");
        let key2 = derive_key("密码");
        let key3 = derive_key("パスワード");

        assert_eq!(key1.len(), 32);
        assert_eq!(key2.len(), 32);
        assert_eq!(key3.len(), 32);

        // Different Unicode passwords should produce different keys
        assert_ne!(key1, key2);
        assert_ne!(key2, key3);
    }
}
