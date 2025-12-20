//! Whitespace steganography using invisible Unicode characters.
//!
//! This library provides encoding and decoding functions for hiding messages
//! in text using invisible Unicode control characters.

pub mod constants;
pub mod decoder;
pub mod encoder;
pub mod errors;

pub use decoder::decode;
pub use encoder::encode;
pub use errors::StegoError;

