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
pub use decode::{decode, decode_binary, extract_encoded, get_encoded_message_position};
pub use encode::{encode, encode_binary, get_encoded_message_size, has_encoded_message};

// Re-export crypto functions for advanced usage
pub use crypto::{decrypt_data, encrypt_data, is_encrypted};

#[cfg(test)]
mod tests {
    use super::*;

    const MESSAGES: &[&str] = &[
        "Hello, World!",
        "Test message with emoji 😀",
        "Multilingual text: 你好, 世界!",
        "Special chars: !@#$%^&*()",
        "", // Empty message
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
                    let encoded = encode(message, carrier, password).unwrap();
                    let decoded = decode(&encoded, password).unwrap();
                    assert_eq!(decoded, message);
                }
            }
        }
    }

    #[test]
    fn test_empty_carrier() {
        for &message in MESSAGES {
            let encoded = encode(message, "", None).unwrap();
            assert!(encoded.contains(START_MARKER));
            assert!(encoded.contains(END_MARKER));
            assert!(encoded.len() > message.len());
        }
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
                let encoded = encode(message, carrier, None).unwrap();
                let (extracted, remaining) = extract_encoded(&encoded).unwrap();
                assert!(extracted.contains(START_MARKER));
                assert!(extracted.contains(END_MARKER));
                if !carrier.is_empty() {
                    assert_eq!(remaining, carrier);
                }
            }
        }
    }

    #[test]
    fn test_password_mismatch() {
        for &message in MESSAGES {
            let password = Some("test_password");
            let encoded = encode(message, "", password).unwrap();
            assert!(decode(&encoded, Some("wrong_password")).is_err());
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
    fn test_derive_fernet_key_length_and_padding() {
        let key1 = derive_fernet_key("short");
        let key2 = derive_fernet_key("this_is_a_very_long_password_that_should_be_truncated");
        assert_eq!(key1.len(), key2.len());
        assert_eq!(key1.len(), 43); // 32 bytes base64-url encoded, no padding
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
}

#[cfg(test)]
mod proptests {
    use super::*;
    use proptest::prelude::*;

    proptest! {
        #[test]
        fn prop_encode_decode_roundtrip(message in ".{0,100}", carrier in ".{0,100}") {
            let encoded = encode(&message, &carrier, None).unwrap();
            let decoded = decode(&encoded, None).unwrap();
            prop_assert_eq!(decoded, message);
        }

        #[test]
        fn prop_encode_decode_with_password(message in ".{0,100}", carrier in ".{0,100}", password in ".{0,32}") {
            let encoded = encode(&message, &carrier, Some(&password)).unwrap();
            let decoded = decode(&encoded, Some(&password)).unwrap();
            prop_assert_eq!(decoded, message);
        }

        #[test]
        fn prop_extract_encoded(message in ".{0,100}", carrier in ".{0,100}") {
            let encoded = encode(&message, &carrier, None).unwrap();
            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            prop_assert!(extracted.contains(START_MARKER));
            prop_assert!(extracted.contains(END_MARKER));
            if !carrier.is_empty() {
                prop_assert_eq!(remaining, carrier);
            }
        }
    }
} 