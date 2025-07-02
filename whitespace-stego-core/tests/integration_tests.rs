//! Integration tests for whitespace steganography core library.
//!
//! These tests verify the complete functionality of the library,
//! including edge cases and error conditions.

use whitespace_stego_core::*;

#[test]
fn test_basic_encode_decode() {
    let message = "Hello, World!";
    let carrier = "This is a test carrier text.";
    
    let encoded = encode(message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
    assert!(has_encoded_message(&encoded));
}

#[test]
fn test_encode_decode_with_password() {
    let message = "Secret message";
    let carrier = "Public carrier text";
    let password = "my_secret_password";
    
    let encoded = encode(message, carrier, Some(password)).unwrap();
    let decoded = decode(&encoded, Some(password)).unwrap();
    
    assert_eq!(decoded, message);
    assert!(has_encoded_message(&encoded));
}

#[test]
fn test_encode_decode_wrong_password() {
    let message = "Secret message";
    let carrier = "Public carrier text";
    let password = "correct_password";
    let wrong_password = "wrong_password";
    
    let encoded = encode(message, carrier, Some(password)).unwrap();
    let result = decode(&encoded, Some(wrong_password));
    
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
}

#[test]
fn test_empty_message() {
    let message = "";
    let carrier = "Carrier text";
    
    let result = encode(message, carrier, None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
}

#[test]
fn test_empty_carrier() {
    let message = "Test message";
    let carrier = "";
    
    let encoded = encode(message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
    assert!(encoded.starts_with(START_MARKER));
    assert!(encoded.ends_with(END_MARKER));
}

#[test]
fn test_unicode_message() {
    let message = "Hello, 世界! 🌍";
    let carrier = "English carrier text";
    
    let encoded = encode(message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
}

#[test]
fn test_unicode_carrier() {
    let message = "English message";
    let carrier = "你好，世界！";
    
    let encoded = encode(message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
}

#[test]
fn test_special_characters() {
    let message = "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?";
    let carrier = "Normal carrier text";
    
    let encoded = encode(message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
}

#[test]
fn test_large_message() {
    let message = "A".repeat(1000);
    let carrier = "Short carrier";
    
    let encoded = encode(&message, carrier, None).unwrap();
    let decoded = decode(&encoded, None).unwrap();
    
    assert_eq!(decoded, message);
}

#[test]
fn test_multiple_encodings() {
    let message1 = "First message";
    let message2 = "Second message";
    let carrier = "Carrier text";
    
    let encoded1 = encode(message1, carrier, None).unwrap();
    let encoded2 = encode(message2, carrier, None).unwrap();
    
    let decoded1 = decode(&encoded1, None).unwrap();
    let decoded2 = decode(&encoded2, None).unwrap();
    
    assert_eq!(decoded1, message1);
    assert_eq!(decoded2, message2);
    assert_ne!(encoded1, encoded2);
}

#[test]
fn test_extract_encoded() {
    let message = "Hidden message";
    let carrier = "Visible carrier text";
    
    let encoded = encode(message, carrier, None).unwrap();
    let (extracted, remaining) = extract_encoded(&encoded).unwrap();
    
    assert!(extracted.contains(START_MARKER));
    assert!(extracted.contains(END_MARKER));
    assert_eq!(remaining, carrier);
}

#[test]
fn test_get_encoded_message_position() {
    let message = "Test message";
    let carrier = "Carrier text";
    
    let encoded = encode(message, carrier, None).unwrap();
    let position = get_encoded_message_position(&encoded);
    
    assert!(position.is_some());
    let (start, end) = position.unwrap();
    assert!(start < end);
    assert!(encoded[start..].starts_with(START_MARKER));
    assert!(encoded[..end].ends_with(END_MARKER));
}

#[test]
fn test_get_encoded_message_size() {
    let message = "Test message";
    let carrier = "Carrier text";
    
    let encoded = encode(message, carrier, None).unwrap();
    let size = get_encoded_message_size(&encoded);
    
    assert!(size.is_some());
    assert!(size.unwrap() > 0);
}

#[test]
fn test_decode_plain_text() {
    let result = decode("Plain text without markers", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
}

#[test]
fn test_decode_malformed_markers() {
    let text = format!("Text with{}but no end", START_MARKER);
    let result = decode(&text, None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
}

#[test]
fn test_decode_markers_wrong_order() {
    let text = format!("Text with{}data{}", END_MARKER, START_MARKER);
    let result = decode(&text, None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
}

#[test]
fn test_has_encoded_message() {
    assert!(!has_encoded_message("Plain text"));
    assert!(!has_encoded_message(&format!("Text with start{}", START_MARKER)));
    assert!(!has_encoded_message(&format!("Text with end{}", END_MARKER)));
    assert!(has_encoded_message(&format!("Text with{}data{}", START_MARKER, END_MARKER)));
}

#[test]
fn test_encryption_compatibility() {
    // Test that our encryption is compatible with the original implementation
    let message = "Test message";
    let password = "test_password";
    
    let encoded = encode(message, "", Some(password)).unwrap();
    let decoded = decode(&encoded, Some(password)).unwrap();
    
    assert_eq!(decoded, message);
}

#[test]
fn test_binary_encoding_roundtrip() {
    let data = b"Binary data with \x00\x01\x02\x03 bytes";
    let encoded = encode_binary(data);
    let decoded = decode_binary(&encoded).unwrap();
    
    assert_eq!(decoded, data);
}

#[test]
fn test_crypto_functions() {
    let data = b"Secret data";
    let password = "password123";
    
    let encrypted = encrypt_data(data, password).unwrap();
    let decrypted = decrypt_data(&encrypted, password).unwrap();
    
    assert_eq!(decrypted, data);
    assert!(is_encrypted(&encrypted));
} 