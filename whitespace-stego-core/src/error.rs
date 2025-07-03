//! Error types for whitespace steganography operations.
//!
//! This module defines the error types used throughout the steganography
//! library, providing detailed error information for debugging and user feedback.

use thiserror::Error;

/// Error type for steganography operations
#[derive(Error, Debug, Clone, PartialEq)]
pub enum StegoError {
    /// Invalid carrier text (no markers found, malformed data, etc.)
    #[error("Invalid carrier text: {message}")]
    InvalidCarrier { message: String },

    /// Decryption failed (wrong password, corrupted data, etc.)
    #[error("Decryption failed: {message}")]
    DecryptionFailed { message: String },

    /// Encoding failed (invalid input, encryption error, etc.)
    #[error("Encoding failed: {message}")]
    EncodingFailed { message: String },

    /// Base64 encoding/decoding error
    #[error("Base64 error: {message}")]
    Base64Error { message: String },

    /// UTF-8 encoding/decoding error
    #[error("UTF-8 error: {message}")]
    Utf8Error { message: String },

    /// Invalid key for encryption/decryption
    #[error("Invalid key: {message}")]
    InvalidKey { message: String },

    /// No encoded message found in carrier text
    #[error("No encoded message found in carrier text")]
    NoMessageFound,

    /// Invalid binary data (wrong length, malformed bits, etc.)
    #[error("Invalid binary data: {message}")]
    InvalidBinaryData { message: String },
}

impl StegoError {
    /// Create an invalid carrier error
    pub fn invalid_carrier(message: impl Into<String>) -> Self {
        Self::InvalidCarrier {
            message: message.into(),
        }
    }

    /// Create a decryption failed error
    pub fn decryption_failed(message: impl Into<String>) -> Self {
        Self::DecryptionFailed {
            message: message.into(),
        }
    }

    /// Create an encoding failed error
    pub fn encoding_failed(message: impl Into<String>) -> Self {
        Self::EncodingFailed {
            message: message.into(),
        }
    }

    /// Create a base64 error
    pub fn base64_error(message: impl Into<String>) -> Self {
        Self::Base64Error {
            message: message.into(),
        }
    }

    /// Create a UTF-8 error
    pub fn utf8_error(message: impl Into<String>) -> Self {
        Self::Utf8Error {
            message: message.into(),
        }
    }

    /// Create an invalid key error
    pub fn invalid_key(message: impl Into<String>) -> Self {
        Self::InvalidKey {
            message: message.into(),
        }
    }

    /// Create an invalid binary data error
    pub fn invalid_binary_data(message: impl Into<String>) -> Self {
        Self::InvalidBinaryData {
            message: message.into(),
        }
    }
}

impl From<std::string::FromUtf8Error> for StegoError {
    fn from(err: std::string::FromUtf8Error) -> Self {
        Self::utf8_error(err.to_string())
    }
}

impl From<std::str::Utf8Error> for StegoError {
    fn from(err: std::str::Utf8Error) -> Self {
        Self::utf8_error(err.to_string())
    }
}

impl From<base64::DecodeError> for StegoError {
    fn from(err: base64::DecodeError) -> Self {
        Self::base64_error(err.to_string())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_error_creation() {
        let carrier_error = StegoError::invalid_carrier("No markers found");
        assert!(matches!(carrier_error, StegoError::InvalidCarrier { .. }));

        let decrypt_error = StegoError::decryption_failed("Wrong password");
        assert!(matches!(decrypt_error, StegoError::DecryptionFailed { .. }));

        let encode_error = StegoError::encoding_failed("Invalid input");
        assert!(matches!(encode_error, StegoError::EncodingFailed { .. }));
    }

    #[test]
    fn test_error_display() {
        let error = StegoError::invalid_carrier("Test message");
        let display = format!("{}", error);
        assert!(display.contains("Invalid carrier text"));
        assert!(display.contains("Test message"));
    }

    #[test]
    fn test_error_from_conversions() {
        // Test UTF-8 error conversion
        let utf8_bytes = vec![0xFF, 0xFE]; // Invalid UTF-8
        let utf8_error = String::from_utf8(utf8_bytes).unwrap_err();
        let stego_error: StegoError = utf8_error.into();
        assert!(matches!(stego_error, StegoError::Utf8Error { .. }));

        // Test base64 error conversion
        use base64::Engine;
        let base64_error = base64::engine::general_purpose::STANDARD
            .decode("invalid base64!")
            .unwrap_err();
        let stego_error: StegoError = base64_error.into();
        assert!(matches!(stego_error, StegoError::Base64Error { .. }));
    }
}
