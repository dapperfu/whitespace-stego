use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::exceptions::PyValueError;
use std::str::FromStr;

mod charset;
pub mod encoder;
pub mod decoder;

use encoder::{encode_binary, encode_message as rust_encode_message, insert_payload, encode_and_insert};
use decoder::{decode_binary, decode_message as rust_decode_message, decode_and_remove};

// Re-export the main functions for the CLI
pub use encoder::encode_and_insert as encode;
pub use decoder::decode_and_remove as decode;

/// Encode a binary string using zero-width characters.
#[pyfunction]
fn encode_binary_rs(binary_str: &str) -> PyResult<String> {
    encode_binary(binary_str).map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// Encode a message into a steganographic payload.
#[pyfunction]
fn encode_message_rs(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    encode_and_insert(message, carrier, password, None)
        .map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// Insert a steganographic payload into carrier text.
#[pyfunction]
fn insert_payload_rs(carrier: &str, payload: &str, position: Option<usize>) -> PyResult<String> {
    insert_payload(carrier, payload, position).map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// Encode a message and insert it into carrier text.
#[pyfunction]
fn encode_and_insert_rs(
    message: &str,
    carrier: &str,
    password: Option<&str>,
    position: Option<usize>,
) -> PyResult<String> {
    encode_and_insert(message, carrier, password, position)
        .map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// Decode zero-width characters back to binary string.
#[pyfunction]
fn decode_binary_rs(encoded: &str) -> PyResult<String> {
    decode_binary(encoded).map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// Encode a message into a carrier text using zero-width Unicode characters.
///
/// Args:
///     message (str): The message to encode.
///     carrier (str): The carrier text to encode the message into.
///     password (str, optional): Password for encryption. Defaults to None.
///
/// Returns:
///     str: The encoded carrier text.
///
/// Raises:
///     ValueError: If encoding fails.
#[pyfunction]
fn encode_message(
    message: &str,
    carrier: &str,
    password: Option<&str>,
) -> PyResult<String> {
    let result = encode_and_insert(message, carrier, password, None)
        .map_err(|e| PyValueError::new_err(e.to_string()))?;

    Ok(result)
}

/// Decode a message from encoded text.
///
/// Args:
///     encoded_text (str): The encoded text to decode.
///     password (str, optional): Password for decryption. Defaults to None.
///
/// Returns:
///     str: The decoded message.
///
/// Raises:
///     ValueError: If decoding fails.
#[pyfunction]
fn decode_message(
    encoded_text: &str,
    password: Option<&str>,
) -> PyResult<String> {
    let result = rust_decode_message(encoded_text, password)
        .map_err(|e| PyValueError::new_err(e.to_string()))?;

    Ok(result)
}

/// Decode a hidden message and remove it from the carrier text.
#[pyfunction]
fn decode_and_remove_rs(text: &str, password: Option<&str>) -> PyResult<(String, String)> {
    decode_and_remove(text, password).map_err(PyErr::new::<pyo3::exceptions::PyValueError, _>)
}

/// A Python module implemented in Rust.
#[pymodule]
fn whitespace_stego_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_binary_rs, m)?)?;
    m.add_function(wrap_pyfunction!(encode_message_rs, m)?)?;
    m.add_function(wrap_pyfunction!(insert_payload_rs, m)?)?;
    m.add_function(wrap_pyfunction!(encode_and_insert_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_binary_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_message, m)?)?;
    m.add_function(wrap_pyfunction!(decode_and_remove_rs, m)?)?;
    Ok(())
} 