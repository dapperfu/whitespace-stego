use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod charset;
pub mod encoder;
pub mod decoder;

use encoder::{encode_binary, encode_message, insert_payload, encode_and_insert};
use decoder::{decode_binary, decode_message, decode_and_remove};

// Re-export the main functions for the CLI
pub use encoder::encode_and_insert as encode;
pub use decoder::decode_and_remove as decode;

/// Encode a binary string using zero-width characters.
#[pyfunction]
fn encode_binary_rs(binary_str: &str) -> PyResult<String> {
    Ok(encode_binary(binary_str))
}

/// Encode a message into a steganographic payload.
#[pyfunction]
fn encode_message_rs(message: &str, password: Option<&str>) -> PyResult<String> {
    Ok(encode_message(message, password))
}

/// Insert a steganographic payload into carrier text.
#[pyfunction]
fn insert_payload_rs(carrier: &str, payload: &str, position: Option<usize>) -> PyResult<String> {
    insert_payload(carrier, payload, position).map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e))
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
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e))
}

/// Decode zero-width characters back to binary string.
#[pyfunction]
fn decode_binary_rs(encoded: &str) -> PyResult<String> {
    decode_binary(encoded).map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e))
}

/// Decode a hidden message from text.
#[pyfunction]
fn decode_message_rs(text: &str, password: Option<&str>) -> PyResult<String> {
    decode_message(text, password).map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e))
}

/// Decode a hidden message and remove it from the carrier text.
#[pyfunction]
fn decode_and_remove_rs(text: &str, password: Option<&str>) -> PyResult<(String, String)> {
    decode_and_remove(text, password).map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e))
}

/// A Python module implemented in Rust.
#[pymodule]
fn whitespace_stego_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_binary_rs, m)?)?;
    m.add_function(wrap_pyfunction!(encode_message_rs, m)?)?;
    m.add_function(wrap_pyfunction!(insert_payload_rs, m)?)?;
    m.add_function(wrap_pyfunction!(encode_and_insert_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_binary_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_message_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_and_remove_rs, m)?)?;
    Ok(())
} 