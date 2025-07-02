//! Core implementation of whitespace steganography.
//!
//! This library provides the core functionality for encoding and decoding messages
//! using zero-width Unicode whitespace characters. It supports optional encryption
//! using Fernet symmetric encryption, which is compatible with Python's
//! cryptography.fernet module.
//!
//! # Features
//!
//! - **Encoding**: Hide messages in carrier text using zero-width Unicode characters
//! - **Decoding**: Extract hidden messages from carrier text
//! - **Encryption**: Optional password-based encryption using Fernet
//! - **Analysis**: Utilities for detecting and analyzing encoded messages
//! - **Compatibility**: Compatible with Python implementations
//!
//! # Quick Start
//!
//! ```rust
//! use whitespace_stego_core::{encode, decode, StegoError};
//!
//! fn main() -> Result<(), StegoError> {
//!     // Encode a message
//!     let message = "Hello, World!";
//!     let carrier = "This is carrier text";
//!     let encoded = encode(message, carrier, None)?;
//!
//!     // Decode the message
//!     let decoded = decode(&encoded, None)?;
//!     assert_eq!(decoded, message);
//!
//!     // With encryption
//!     let password = "secret_password";
//!     let encoded = encode(message, carrier, Some(password))?;
//!     let decoded = decode(&encoded, Some(password))?;
//!     assert_eq!(decoded, message);
//!
//!     Ok(())
//! }
//! ```
//!
//! # Unicode Characters Used
//!
//! The library uses the following zero-width Unicode characters:
//!
//! - `\u{200B}` (Zero-width space) - Start marker
//! - `\u{200C}` (Zero-width non-joiner) - End marker
//! - `\u{200D}` (Zero-width joiner) - Represents 0 bits
//! - `\u{FEFF}` (Zero-width no-break space) - Represents 1 bits
//!
//! # Encoding Process
//!
//! 1. **Base64 Encoding**: The message is first base64 encoded
//! 2. **Optional Encryption**: If a password is provided, the data is encrypted using Fernet
//! 3. **Binary Conversion**: Each byte is converted to 8 zero-width characters
//! 4. **Embedding**: The encoded data is embedded in the carrier text after the first character
//!
//! # Security
//!
//! - Encryption uses Fernet (AES-128 in CBC mode with PKCS7 padding)
//! - Keys are derived from passwords using a deterministic method
//! - Compatible with Python's cryptography.fernet module
//! - No key derivation function is used (for compatibility)

pub mod constants;
pub mod crypto;
pub mod decode;
pub mod encode;
pub mod error;

// Re-export main types and functions
pub use constants::{END_MARKER, ONE_BIT, START_MARKER, ZERO_BIT};
pub use error::StegoError;

// Re-export main functions
pub use decode::{decode, decode_all, decode_binary, extract_encoded, get_encoded_message_position, count_messages};
pub use encode::{encode, encode_binary, get_encoded_message_size, has_encoded_message};

// Re-export crypto functions for advanced usage
pub use crypto::{decrypt_data, encrypt_data, is_encrypted};

// Test data for comprehensive permutation testing
const EMPTY_MESSAGE: &str = "";
const SHORT_MESSAGE: &str = "Hi";
const LONG_MESSAGE: &str = "This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly. It includes various types of content like numbers 123, symbols !@#, emojis 😀🎉, and unicode characters 你好世界. This message is designed to be long enough to test edge cases in the binary encoding and decoding process.";

const EMPTY_CARRIER: &str = "";
const SHORT_CARRIER: &str = "A";
const LONG_CARRIER: &str = "This is a very long carrier text that will be used to test the embedding of encoded messages. It contains various characters and should be long enough to test different insertion points and edge cases in the encoding process. The carrier text should remain unchanged after extraction of the encoded message.";

const EMPTY_PASSWORD: Option<&str> = Some("");
const SHORT_PASSWORD: Option<&str> = Some("pass");
const LONG_PASSWORD: Option<&str> = Some("this_is_a_very_long_password_for_testing");
const NO_PASSWORD: Option<&str> = None;

#[cfg(test)]
mod tests {
    use super::*;

    const MESSAGES: &[&str] = &[
        "Hello, World!",
        "Test message with emoji 😀",
        "Multilingual text: 你好, 世界!",
        "Special chars: !@#$%^&*()",
        "A", // Single character message
    ];

    const PASSWORDS: &[Option<&str>] = &[
        None,
        Some("simple_password"),
        Some("complex_password_123!@#"),
        Some(""), // Empty password
    ];

    const CARRIERS: &[&str] = &[
        "", // Empty carrier
        "Simple carrier text",
        "Carrier with emoji 🎉",
        "Multilingual carrier: 你好",
    ];

    #[test]
    fn test_encode_decode_roundtrip() {
        for &message in MESSAGES {
            for &password in PASSWORDS {
                for &carrier in CARRIERS {
                    let result = encode(message, carrier, password);
                    if message.is_empty() {
                        assert!(result.is_err(), "Empty message should return error");
                        assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
                    } else {
                        let encoded = result.unwrap();
                        let decoded = decode(&encoded, password);
                        if password.is_some() {
                            // If password was used for encoding, decoding without password should fail
                            assert!(decoded.is_ok(), "Decoding with password should succeed");
                            assert_eq!(decoded.unwrap(), message);
                        } else {
                            // If no password was used, decoding should succeed
                            assert!(decoded.is_ok(), "Decoding without password should succeed");
                            assert_eq!(decoded.unwrap(), message);
                        }
                    }
                }
            }
        }
    }

    #[test]
    fn test_empty_carrier() {
        for &message in MESSAGES {
            let result = encode(message, "", None);
            if message.is_empty() {
                assert!(result.is_err(), "Empty message should return error");
                assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
            } else {
                let encoded = result.unwrap();
            assert!(encoded.contains(START_MARKER));
            assert!(encoded.contains(END_MARKER));
            assert!(encoded.len() > message.len());
        }
        }
    }

    #[test]
    fn test_empty_message_rejected() {
        // Test that empty messages are properly rejected
        let result = encode("", "carrier", None);
        assert!(result.is_err());
        assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
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
                let result = encode(message, carrier, None);
                if message.is_empty() {
                    assert!(result.is_err(), "Empty message should return error");
                    assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
                } else {
                    let encoded = result.unwrap();
                let (extracted, remaining) = extract_encoded(&encoded).unwrap();
                assert!(extracted.contains(START_MARKER));
                assert!(extracted.contains(END_MARKER));
                if !carrier.is_empty() {
                    assert_eq!(remaining, carrier);
                    } else {
                        assert_eq!(remaining, "");
                    }
                }
            }
        }
    }

    #[test]
    fn test_password_mismatch() {
        for &message in MESSAGES {
            if message.is_empty() {
                continue;
            }
            let password = Some("test_password");
            let encoded = encode(message, "", password).unwrap();
            let result = decode(&encoded, Some("wrong_password"));
            assert!(result.is_err());
            assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
            
            // Test decoding without password when message is encrypted
            let result = decode(&encoded, None);
            assert!(result.is_err());
            assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
        }
    }

    #[test]
    fn test_encode_binary_and_decode_binary() {
        let data = b"test data";
        let encoded = encode_binary(data);
        let decoded = decode_binary(&encoded).unwrap();
        assert_eq!(decoded, data);
    }

    #[test]
    fn test_derive_key_length_and_consistency() {
        use crate::crypto::derive_key;
        let key1 = derive_key("short");
        let key2 = derive_key("this_is_a_very_long_password_that_should_be_hashed");
        assert_eq!(key1.len(), 32);
        assert_eq!(key2.len(), 32);
        
        // Test that same password produces same key
        let key3a = derive_key("test_password");
        let key3b = derive_key("test_password");
        assert_eq!(key3a, key3b);
        
        // Test that different passwords produce different keys
        let key4a = derive_key("password1");
        let key4b = derive_key("password2");
        assert_ne!(key4a, key4b);
    }

    #[test]
    fn test_encrypt_decrypt_data_roundtrip() {
        let data = b"super secret";
        let password = "password123";
        let encrypted = encrypt_data(data, password).unwrap();
        let decrypted = decrypt_data(&encrypted, password).unwrap();
        assert_eq!(decrypted, data);
    }

    #[test]
    fn test_decrypt_data_wrong_password() {
        let data = b"super secret";
        let password = "password123";
        let wrong_password = "wrongpass";
        let encrypted = encrypt_data(data, password).unwrap();
        let result = decrypt_data(&encrypted, wrong_password);
        assert!(result.is_err());
    }

    #[test]
    fn test_decode_binary_with_invalid_input() {
        // Not a valid zero-width sequence, should decode to empty
        let decoded = decode_binary("not zero width").unwrap();
        assert_eq!(decoded, Vec::<u8>::new());
    }

    #[test]
    fn test_has_encoded_message() {
        assert!(!has_encoded_message("plain text"));
        assert!(!has_encoded_message(&format!("text with start{}", START_MARKER)));
        assert!(!has_encoded_message(&format!("text with end{}", END_MARKER)));
        assert!(has_encoded_message(&format!("text with both{}data{}", START_MARKER, END_MARKER)));
    }

    #[test]
    fn test_get_encoded_message_size() {
        let message = "test";
        let carrier = "carrier";
        let encoded = encode(message, carrier, None).unwrap();
        
        let size = get_encoded_message_size(&encoded);
        assert!(size.is_some());
        assert!(size.unwrap() > 0);
    }

    #[test]
    fn test_get_encoded_message_position() {
        let message = "test";
        let carrier = "carrier";
        let encoded = encode(message, carrier, None).unwrap();
        
        let position = get_encoded_message_position(&encoded);
        assert!(position.is_some());
        
        let (start, end) = position.unwrap();
        assert!(start < end);
    }

    #[test]
    fn test_edge_case_combinations() {
        // Test edge cases: short message, empty carrier, empty password
        let encoded = encode(SHORT_MESSAGE, EMPTY_CARRIER, EMPTY_PASSWORD).unwrap();
        let decoded = decode(&encoded, EMPTY_PASSWORD);
        assert!(decoded.is_ok());
        assert_eq!(decoded.unwrap(), SHORT_MESSAGE);

        // Test short message with long carrier and password
        let encoded = encode(SHORT_MESSAGE, LONG_CARRIER, LONG_PASSWORD).unwrap();
        let decoded = decode(&encoded, LONG_PASSWORD);
        assert!(decoded.is_ok());
        assert_eq!(decoded.unwrap(), SHORT_MESSAGE);

        // Test long message with empty carrier and no password
        let encoded = encode(LONG_MESSAGE, EMPTY_CARRIER, NO_PASSWORD).unwrap();
        let decoded = decode(&encoded, NO_PASSWORD);
        assert!(decoded.is_ok());
        assert_eq!(decoded.unwrap(), LONG_MESSAGE);
    }

    #[test]
    fn test_single_character_carrier_edge_cases() {
        let single_char_carriers = ["A", "😀", "你", "1", "!", " "];
        
        for carrier in single_char_carriers {
            for &message in &[SHORT_MESSAGE, LONG_MESSAGE] {
                for &password in &[NO_PASSWORD, EMPTY_PASSWORD, SHORT_PASSWORD] {
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password);
                    assert!(decoded.is_ok(), 
                        "Failed for message: '{}', single char carrier: '{}', password: {:?}", 
                        message, carrier, password);
                    assert_eq!(decoded.unwrap(), message, 
                        "Failed for message: '{}', single char carrier: '{}', password: {:?}", 
                        message, carrier, password);
                }
            }
        }
    }

    #[test]
    fn test_unicode_edge_cases() {
        let unicode_messages = [
            "Hello 世界",
            "Emoji test 😀🎉🚀",
            "Mixed: Hello 世界 😀 123 !@#",
            "Zero-width chars: \u{200B}\u{200C}\u{200D}\u{FEFF}",
            "Surrogate pairs: \u{1F600}", // 😀
        ];

        let unicode_carriers = [
            "Carrier with 世界",
            "Emoji carrier 🎉",
            "Mixed carrier: Hello 世界 😀",
        ];

        for message in &unicode_messages {
            for carrier in &unicode_carriers {
                for &password in &[NO_PASSWORD, SHORT_PASSWORD] {
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password);
                    assert!(decoded.is_ok(), 
                        "Failed for unicode message: '{}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                    assert_eq!(decoded.unwrap(), *message, 
                        "Failed for unicode message: '{}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                }
            }
        }
    }

    #[test]
    fn test_binary_data_encoding() {
        // Test with binary-like data that might cause issues
        let binary_messages = [
            "\x00\x01\x02\x03", // Null bytes
            // High byte values skipped: not valid UTF-8
            "Mixed\x00\x01text", // Mixed text and binary
        ];

        for message in &binary_messages {
            for &carrier in &[EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER] {
                for &password in &[NO_PASSWORD, SHORT_PASSWORD] {
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password);
                    assert!(decoded.is_ok(), 
                        "Failed for binary message: '{:?}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                    assert_eq!(decoded.unwrap(), *message, 
                        "Failed for binary message: '{:?}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                }
            }
        }
    }

    #[test]
    fn test_password_variations() {
        let password_variations = [
            None,
            Some(""),
            Some("a"),
            Some("ab"),
            Some("abc"),
            Some("password"),
            Some("very_long_password_that_exceeds_normal_length"),
            Some("!@#$%^&*()"),
            Some("password with spaces"),
            Some("password\nwith\nnewlines"),
            Some("password\twith\ttabs"),
        ];

        let test_message = "Test message for password variations";
        let test_carrier = "Test carrier";

        for password in &password_variations {
            let encoded = encode(test_message, test_carrier, *password).unwrap();
            let decoded = decode(&encoded, *password);
            assert!(decoded.is_ok(), 
                "Failed for password: {:?}", password);
            assert_eq!(decoded.unwrap(), test_message, 
                "Failed for password: {:?}", password);
        }
    }

    #[test]
    fn test_error_conditions() {
        // Test decoding without markers
        assert!(matches!(
            decode("plain text without markers", None),
            Err(StegoError::InvalidCarrier { .. })
        ));
        assert!(matches!(
            decode("", None),
            Err(StegoError::InvalidCarrier { .. })
        ));

        // Test decoding with only start marker
        let partial_encoded = format!("{}some data", START_MARKER);
        assert!(matches!(
            decode(&partial_encoded, None),
            Err(StegoError::InvalidCarrier { .. })
        ));

        // Test decoding with only end marker
        let partial_encoded = format!("some data{}", END_MARKER);
        assert!(matches!(
            decode(&partial_encoded, None),
            Err(StegoError::InvalidCarrier { .. })
        ));

        // Test wrong password for encrypted data
        let encoded = encode("secret message", "carrier", Some("correct_password")).unwrap();
        assert!(matches!(
            decode(&encoded, Some("wrong_password")),
            Err(StegoError::DecryptionFailed { .. })
        ));
        assert!(matches!(
            decode(&encoded, None),
            Err(StegoError::DecryptionFailed { .. })
        )); // No password when encrypted
    }

    #[test]
    fn test_extract_encoded_comprehensive() {
        for &message in &[SHORT_MESSAGE, LONG_MESSAGE] {
            for &carrier in &[EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER] {
                for &password in &[NO_PASSWORD, SHORT_PASSWORD] {
                    let encoded = encode(message, carrier, password).unwrap();
                    let (extracted, remaining) = extract_encoded(&encoded).unwrap();
                    
                    // Verify extracted contains markers
                    assert!(extracted.contains(START_MARKER));
                    assert!(extracted.contains(END_MARKER));
                    
                    // Verify remaining matches original carrier
                    if !carrier.is_empty() {
                        assert_eq!(remaining, carrier, 
                            "Failed for message: '{}', carrier: '{}', password: {:?}", 
                            message, carrier, password);
                    } else {
                        assert_eq!(remaining, "");
                    }
                }
            }
        }
    }

    #[test]
    fn test_round_trip_with_special_characters() {
        let special_messages = [
            "Message with newlines\nand\ttabs",
            "Message with quotes: \"Hello\" and 'World'",
            "Message with backslashes: \\n\\t\\r",
            "Message with control chars: \x01\x02\x03",
            "Message with unicode: αβγδε",
            "Message with combining chars: e\u{0301}", // é
        ];

        for message in &special_messages {
            for &carrier in &[EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER] {
                for &password in &[NO_PASSWORD, SHORT_PASSWORD] {
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password);
                    assert!(decoded.is_ok(), 
                        "Failed for special message: '{:?}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                    assert_eq!(decoded.unwrap(), *message, 
                        "Failed for special message: '{:?}', carrier: '{}', password: {:?}", 
                        message, carrier, password);
                }
            }
        }
    }

    #[test]
    fn test_very_long_messages() {
        // Test with messages that are very long to test binary encoding limits
        let very_long_message = "A".repeat(1000);
        let very_long_carrier = "B".repeat(1000);
        
        for &password in &[NO_PASSWORD, SHORT_PASSWORD] {
            let encoded = encode(&very_long_message, &very_long_carrier, password).unwrap();
            let decoded = decode(&encoded, password);
            assert!(decoded.is_ok());
            assert_eq!(decoded.unwrap(), very_long_message);
        }
    }

    #[test]
    fn test_fernet_key_derivation_edge_cases() {
        // Test various password lengths and characters
        let test_passwords = [
            "",           // Empty
            "a",          // Single char
            "ab",         // Two chars
            "abc",        // Three chars
            &"a".repeat(31), // 31 chars (just under 32)
            &"a".repeat(32), // Exactly 32 chars
            &"a".repeat(33), // Over 32 chars
            "!@#$%^&*()", // Special chars
            "你好世界",     // Unicode
            "pass\nword", // With newlines
            "pass\tword", // With tabs
        ];

        for password in &test_passwords {
            use crate::crypto::derive_key;
            let key = derive_key(password);
            // All keys should be 32 bytes
            assert_eq!(key.len(), 32, "Key length wrong for password: '{:?}'", password);
            
            // Test that the key can be used for encryption/decryption
            let test_data = b"test data";
            let encrypted = encrypt_data(test_data, password).unwrap();
            let decrypted = decrypt_data(&encrypted, password).unwrap();
            assert_eq!(decrypted, test_data);
        }
    }
} 