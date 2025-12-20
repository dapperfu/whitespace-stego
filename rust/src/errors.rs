//! Error types for whitespace steganography operations.

use std::fmt;

/// Error type for all steganography operations.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum StegoError {
    /// Encoding failed
    Encoding(String),
    /// Decoding failed
    Decoding(String),
    /// Invalid payload characters
    InvalidPayload(String),
    /// Missing control markers
    MissingMarker(String),
    /// Invalid Base64 data
    InvalidBase64(String),
    /// Invalid UTF-8 sequence
    InvalidUTF8(String),
}

impl fmt::Display for StegoError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            StegoError::Encoding(msg) => write!(f, "Encoding error: {}", msg),
            StegoError::Decoding(msg) => write!(f, "Decoding error: {}", msg),
            StegoError::InvalidPayload(msg) => write!(f, "Invalid payload: {}", msg),
            StegoError::MissingMarker(msg) => write!(f, "Missing marker: {}", msg),
            StegoError::InvalidBase64(msg) => write!(f, "Invalid Base64: {}", msg),
            StegoError::InvalidUTF8(msg) => write!(f, "Invalid UTF-8: {}", msg),
        }
    }
}

impl std::error::Error for StegoError {}

