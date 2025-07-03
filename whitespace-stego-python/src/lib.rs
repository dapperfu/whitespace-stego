//! Python bindings for whitespace steganography (stub)
//!
//! This is a stub for the Python module. Full implementation coming soon.

use pyo3::exceptions::PyException;
use pyo3::prelude::*;
use whitespace_stego_core::{decode, encode, extract_encoded, has_encoded_message, StegoError};

/// Python exception for whitespace steganography errors
#[pyclass(extends=PyException)]
struct StegoPyError;

/// Convert StegoError to PyErr
fn stego_error_to_pyerr(err: StegoError) -> PyErr {
    PyException::new_err(err.to_string())
}

/// Encode a message into carrier text using zero-width Unicode characters.
///
/// Args:
///     message (str): The message to encode.
///     carrier (str): The carrier text to hide the message in.
///     password (str, optional): Password for encryption.
///
/// Returns:
///     str: The carrier text with the encoded message embedded.
///
/// Raises:
///     StegoPyError: If encoding fails.
#[pyfunction]
#[pyo3(text_signature = "(message, carrier, password=None)")]
fn encode_py(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    encode(message, carrier, password).map_err(stego_error_to_pyerr)
}

/// Decode a message from carrier text containing zero-width Unicode characters.
///
/// Args:
///     carrier (str): The carrier text containing the encoded message.
///     password (str, optional): Password for decryption.
///
/// Returns:
///     str: The decoded message.
///
/// Raises:
///     StegoPyError: If decoding fails.
#[pyfunction]
#[pyo3(text_signature = "(carrier, password=None)")]
fn decode_py(carrier: &str, password: Option<&str>) -> PyResult<String> {
    decode(carrier, password).map_err(stego_error_to_pyerr)
}

/// Extract the encoded message and remaining carrier text.
///
/// Args:
///     carrier (str): The carrier text containing the encoded message.
///
/// Returns:
///     Tuple[str, str]: (encoded_message, remaining_carrier)
///
/// Raises:
///     StegoPyError: If extraction fails.
#[pyfunction]
#[pyo3(text_signature = "(carrier)")]
fn extract_encoded_py(carrier: &str) -> PyResult<(String, String)> {
    extract_encoded(carrier).map_err(stego_error_to_pyerr)
}

/// Check if text contains an encoded message.
///
/// Args:
///     text (str): The text to check.
///
/// Returns:
///     bool: True if the text contains an encoded message, False otherwise.
#[pyfunction]
#[pyo3(text_signature = "(text)")]
fn has_encoded_message_py(text: &str) -> bool {
    has_encoded_message(text)
}

/// Python module definition
#[pymodule]
fn whitespace_stego_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_py, m)?)?;
    m.add_function(wrap_pyfunction!(extract_encoded_py, m)?)?;
    m.add_function(wrap_pyfunction!(has_encoded_message_py, m)?)?;
    m.add("StegoPyError", _py.get_type::<PyException>())?;
    Ok(())
}
