use whitespace_stego_core::crypto::*;
use whitespace_stego_core::error::StegoError;

#[cfg(test)]
mod tests {
    use super::*;
    // ... (copy all tests from src/crypto.rs #[cfg(test)] mod)
}

#[test]
fn test_derive_key_edge_cases() {
    // Test empty password
    let key = derive_key("");
    assert_eq!(key.len(), 32);
    
    // Test very long password
    let long_password = "a".repeat(1000);
    let key = derive_key(&long_password);
    assert_eq!(key.len(), 32);
    
    // Test password with special characters
    let special_password = "!@#$%^&*()_+-=[]{}|;':\",./<>?";
    let key = derive_key(special_password);
    assert_eq!(key.len(), 32);
    
    // Test password with null bytes
    let null_password = "test\0password";
    let key = derive_key(null_password);
    assert_eq!(key.len(), 32);
}

#[test]
fn test_encrypt_decrypt_edge_cases() {
    // Test empty data
    let empty_data = b"";
    let password = "test_password";
    
    let encrypted = encrypt_data(empty_data, password).unwrap();
    assert!(!encrypted.is_empty());
    
    let decrypted = decrypt_data(&encrypted, password).unwrap();
    assert_eq!(decrypted, empty_data);
    
    // Test very large data
    let large_data = vec![0u8; 10000];
    let encrypted = encrypt_data(&large_data, password).unwrap();
    let decrypted = decrypt_data(&encrypted, password).unwrap();
    assert_eq!(decrypted, large_data);
    
    // Test data with null bytes
    let null_data = b"test\0data\0with\0nulls";
    let encrypted = encrypt_data(null_data, password).unwrap();
    let decrypted = decrypt_data(&encrypted, password).unwrap();
    assert_eq!(decrypted, null_data);
}

#[test]
fn test_encrypt_decrypt_unicode_passwords() {
    let test_data = b"Hello, World!";
    
    // Test various Unicode passwords
    let unicode_passwords = [
        "你好世界",
        "😀🎉🌟",
        "Café",
        "résumé",
        "naïve",
        "façade",
        "garçon",
        "über",
        "naïve",
        "café",
    ];
    
    for password in &unicode_passwords {
        let encrypted = encrypt_data(test_data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();
        assert_eq!(decrypted, test_data);
        
        // Test wrong password
        let wrong_password = format!("{}_wrong", password);
        let result = decrypt_data(&encrypted, &wrong_password);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
    }
}

#[test]
fn test_encrypt_decrypt_binary_data() {
    let password = "test_password";
    
    // Test various binary data patterns
    let test_cases = [
        vec![0u8; 100],           // All zeros
        vec![255u8; 100],         // All ones
        (0..100).collect(),       // Sequential bytes
        vec![0xAA; 100],          // Alternating pattern
        vec![0x55; 100],          // Alternating pattern
    ];
    
    for data in &test_cases {
        let encrypted = encrypt_data(data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();
        assert_eq!(decrypted, *data);
    }
}

#[test]
fn test_is_encrypted_edge_cases() {
    // Test empty data
    assert!(!is_encrypted(b""));
    
    // Test data too short to be encrypted
    assert!(!is_encrypted(b"short"));
    
    // Test data that looks like Fernet but isn't
    let fake_fernet = b"gAAAAABfake_base64_data_that_is_not_fernet";
    assert!(!is_encrypted(fake_fernet));
    
    // Test with actual encrypted data
    let password = "test_password";
    let data = b"Hello, World!";
    let encrypted = encrypt_data(data, password).unwrap();
    assert!(is_encrypted(&encrypted));
}

#[test]
fn test_encrypt_decrypt_roundtrip_consistency() {
    let password = "test_password";
    let data = b"Hello, World!";
    
    // Encrypt the same data multiple times
    let encrypted1 = encrypt_data(data, password).unwrap();
    let encrypted2 = encrypt_data(data, password).unwrap();
    
    // Each encryption should produce different output (due to salt)
    assert_ne!(encrypted1, encrypted2);
    
    // But both should decrypt to the same data
    let decrypted1 = decrypt_data(&encrypted1, password).unwrap();
    let decrypted2 = decrypt_data(&encrypted2, password).unwrap();
    assert_eq!(decrypted1, data);
    assert_eq!(decrypted2, data);
}

#[test]
fn test_encrypt_decrypt_with_different_key_lengths() {
    let test_data = b"Test data";
    
    // Test passwords of different lengths
    let passwords = [
        "",                    // Empty
        "a",                   // Single character
        "ab",                  // Two characters
        "abc",                 // Three characters
        "abcd",                // Four characters
        "password",            // Normal length
        "very_long_password_for_testing_purposes", // Long password
    ];
    
    for password in &passwords {
        let encrypted = encrypt_data(test_data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();
        assert_eq!(decrypted, test_data);
    }
}

#[test]
fn test_encrypt_decrypt_corrupted_data() {
    let password = "test_password";
    let data = b"Hello, World!";
    let encrypted = encrypt_data(data, password).unwrap();
    
    // Test with corrupted encrypted data
    let mut corrupted = encrypted.clone();
    if corrupted.len() > 10 {
        corrupted[10] = corrupted[10].wrapping_add(1);
    }
    
    let result = decrypt_data(&corrupted, password);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
}

#[test]
fn test_derive_key_consistency() {
    let password = "test_password";
    
    // Derive the same key multiple times
    let key1 = derive_key(password);
    let key2 = derive_key(password);
    let key3 = derive_key(password);
    
    // All derivations should produce the same key
    assert_eq!(key1, key2);
    assert_eq!(key2, key3);
    assert_eq!(key1, key3);
}

#[test]
fn test_encrypt_decrypt_with_whitespace_in_password() {
    let test_data = b"Hello, World!";
    let passwords_with_whitespace = [
        " password",   // Leading space
        "password ",   // Trailing space
        " pass word ", // Spaces in middle
        "\tpassword",  // Tab character
        "pass\nword",  // Newline character
        "pass\r\nword", // CRLF
    ];
    
    for password in &passwords_with_whitespace {
        let encrypted = encrypt_data(test_data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();
        assert_eq!(decrypted, test_data);
    }
}
