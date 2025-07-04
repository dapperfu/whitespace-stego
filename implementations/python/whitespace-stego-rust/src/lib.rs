//!
//! Python bindings for whitespace steganography core library.
//!
//! This crate provides Python bindings for the whitespace_stego_core library,
//! allowing Python code to use the high-performance Rust implementation.
//!
//! ## Features
//! - Encode messages into carrier text
//! - Decode messages from carrier text
//! - Count embedded messages
//! - Debug logging capabilities
//!
//! ## Examples
//! ```python
//! import whitespace_stego_rust
//! encoded = whitespace_stego_rust.encode("secret", "cover text", None)
//! decoded = whitespace_stego_rust.decode(encoded, None)
//! ```
//!
//! ## License
//! SPDX-License-Identifier: MIT

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use whitespace_stego_core::decode::decode_debug_log_only;
use whitespace_stego_core::{count_messages, decode, decode_all, encode, StegoError};

/// A Python module implemented in Rust.
///
/// Provides Python bindings for whitespace steganography operations.
///
/// # Errors
/// Returns a [`PyErr`] if module creation fails.
#[pymodule]
fn whitespace_stego_rust(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_all_py, m)?)?;
    m.add_function(wrap_pyfunction!(count_messages_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_debug_log_only_py, m)?)?;
    Ok(())
}

/// Python binding for encoding messages.
///
/// # Arguments
/// * `message` - The message to encode
/// * `carrier` - The carrier text
/// * `password` - Optional password for encryption
///
/// # Returns
/// The encoded carrier text
///
/// # Errors
/// Returns a [`PyValueError`] if encoding fails.
///
/// # Examples
/// ```python
/// encoded = encode_py("secret", "cover text", None)
/// ```
#[pyfunction]
pub fn encode_py(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    encode(message, carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
}

/// Python binding for decoding messages.
///
/// # Arguments
/// * `carrier` - The carrier text containing encoded message
/// * `password` - Optional password for decryption
///
/// # Returns
/// The decoded message
///
/// # Errors
/// Returns a [`PyValueError`] if decoding fails.
///
/// # Examples
/// ```python
/// decoded = decode_py(encoded_carrier, None)
/// ```
#[pyfunction]
pub fn decode_py(carrier: &str, password: Option<&str>) -> PyResult<String> {
    decode(carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
}

/// Python binding for decoding all messages.
///
/// # Arguments
/// * `carrier` - The carrier text containing encoded messages
/// * `password` - Optional password for decryption
///
/// # Returns
/// A list of decoded messages
///
/// # Errors
/// Returns a [`PyValueError`] if decoding fails.
///
/// # Examples
/// ```python
/// messages = decode_all_py(encoded_carrier, None)
/// ```
#[pyfunction]
pub fn decode_all_py(carrier: &str, password: Option<&str>) -> PyResult<Vec<String>> {
    decode_all(carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
}

/// Python binding for counting embedded messages.
///
/// # Arguments
/// * `carrier` - The carrier text to analyze
///
/// # Returns
/// The number of embedded messages
///
/// # Examples
/// ```python
/// count = count_messages_py(carrier_text)
/// ```
#[pyfunction]
pub fn count_messages_py(carrier: &str) -> PyResult<usize> {
    Ok(count_messages(carrier))
}

/// Python binding for debug logging.
///
/// # Arguments
/// * `carrier` - The carrier text to log
///
/// # Returns
/// Always returns `Ok(())`
///
/// # Errors
/// Returns a [`PyValueError`] if logging fails.
///
/// # Examples
/// ```python
/// decode_debug_log_only_py("test input")
/// ```
#[pyfunction]
fn decode_debug_log_only_py(carrier: &str) -> PyResult<()> {
    decode_debug_log_only(carrier).map_err(|e| PyValueError::new_err(format!("{:?}", e)))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode_decode_py() {
        let message = "Hello, backend!";
        let carrier = "Carrier text";
        let encoded = encode_py(message, carrier, None).unwrap();
        let decoded = decode_py(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_decode_py_invalid() {
        let result = decode_py("not encoded", None);
        assert!(result.is_err());
    }

    #[test]
    fn test_multiple_messages() {
        let message1 = "First message";
        let message2 = "Second message";
        let carrier = "Carrier text";

        // Encode first message
        let encoded1 = encode_py(message1, carrier, None).unwrap();

        // Encode second message
        let encoded2 = encode_py(message2, &encoded1, None).unwrap();

        // Decode all messages
        let decoded_all = decode_all_py(&encoded2, None).unwrap();
        assert_eq!(decoded_all.len(), 2);
        assert_eq!(decoded_all[0], message1);
        assert_eq!(decoded_all[1], message2);

        // Decode as single string (should be joined with newlines)
        let decoded_single = decode_py(&encoded2, None).unwrap();
        assert_eq!(decoded_single, format!("{}\n{}", message1, message2));
    }
}
