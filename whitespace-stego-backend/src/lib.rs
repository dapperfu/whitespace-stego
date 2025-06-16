use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use whitespace_stego_core::{encode, decode, StegoError};

/// A Python module implemented in Rust.
#[pymodule]
fn whitespace_stego_backend(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_py, m)?)?;
    Ok(())
}

#[pyfunction]
pub fn encode_py(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    encode(message, carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
}

#[pyfunction]
pub fn decode_py(carrier: &str, password: Option<&str>) -> PyResult<String> {
    decode(carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
} 