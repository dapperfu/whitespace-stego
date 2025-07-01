//! Cryptographic operations for whitespace steganography.
//!
//! This module provides encryption and decryption functionality using the
//! Fernet symmetric encryption scheme, which is compatible with Python's
//! cryptography.fernet module.

use base64::{engine::general_purpose::URL_SAFE_NO_PAD, Engine};
use fernet::Fernet;

use crate::error::StegoError;

/// Derive a Fernet key from a password
///
/// This function creates a Fernet key from a password by:
/// 1. Converting the password to UTF-8 bytes
/// 2. Padding or truncating to exactly 32 bytes
/// 3. Base64 URL-safe encoding without padding
///
/// This is compatible with Python's implementation:
/// `base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])`
pub fn derive_fernet_key(password: &str) -> String {
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

/// Encrypt data using Fernet
///
/// # Arguments
/// * `data` - The data to encrypt
/// * `password` - The password to derive the encryption key from
///
/// # Returns
/// The encrypted data as bytes
///
/// # Errors
/// Returns `StegoError::InvalidKey` if the derived key is invalid
/// Returns `StegoError::EncodingFailed` if encryption fails
pub fn encrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    let fernet = Fernet::new(&key)
        .ok_or_else(|| StegoError::invalid_key("Invalid Fernet key derived from password"))?;
    
    Ok(fernet.encrypt(data).as_bytes().to_vec())
}

/// Decrypt data using Fernet
///
/// # Arguments
/// * `data` - The encrypted data
/// * `password` - The password to derive the decryption key from
///
/// # Returns
/// The decrypted data as bytes
///
/// # Errors
/// Returns `StegoError::InvalidKey` if the derived key is invalid
/// Returns `StegoError::DecryptionFailed` if decryption fails
pub fn decrypt_data(data: &[u8], password: &str) -> Result<Vec<u8>, StegoError> {
    let key = derive_fernet_key(password);
    let fernet = Fernet::new(&key)
        .ok_or_else(|| StegoError::invalid_key("Invalid Fernet key derived from password"))?;
    
    let data_str = std::str::from_utf8(data)
        .map_err(|e| StegoError::utf8_error(format!("Invalid UTF-8 in encrypted data: {}", e)))?;
    
    fernet.decrypt(data_str)
        .map_err(|e| StegoError::decryption_failed(format!("Decryption failed: {}", e)))
}

/// Check if data appears to be encrypted (starts with Fernet header)
///
/// # Arguments
/// * `data` - The data to check
///
/// # Returns
/// `true` if the data appears to be Fernet encrypted
pub fn is_encrypted(data: &[u8]) -> bool {
    // Fernet tokens start with a specific header
    data.len() > 0 && data[0] == b'g' // Fernet tokens start with 'g' in base64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_derive_fernet_key() {
        // Test short password
        let key1 = derive_fernet_key("short");
        assert_eq!(key1.len(), 43); // 32 bytes base64-url encoded, no padding
        
        // Test long password
        let key2 = derive_fernet_key("this_is_a_very_long_password_that_should_be_truncated");
        assert_eq!(key2.len(), 43);
        
        // Test empty password
        let key3 = derive_fernet_key("");
        assert_eq!(key3.len(), 43);
        
        // Test exact 32-byte password
        let key4 = derive_fernet_key("12345678901234567890123456789012");
        assert_eq!(key4.len(), 43);
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
        assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
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
    fn test_derive_fernet_key_padding() {
        // Test that short passwords are padded with spaces
        let key_short = derive_fernet_key("short");
        let key_long = derive_fernet_key("short                "); // 20 spaces
        assert_eq!(key_short, key_long);
    }
} 