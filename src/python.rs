//!
//! Python bindings for whitespace steganography.
//!
//! Exposes encode, decode, and extract functions to Python via PyO3.
//!
//! ## Examples
//! See the Python module documentation for usage examples.

use crate::{decode, encode, extract_encoded};
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Python error type for steganography operations.
#[pyclass]
struct PyStegoError {
    /// The error message.
    message: String,
}

/// Implementation of PyStegoError helper methods.
impl PyStegoError {
    /// Create a new Python error from a message string.
    fn new_err(message: String) -> PyErr {
        PyErr::new::<PyStegoError, _>(message)
    }
}

#[pymethods]
impl PyStegoError {
    /// Create a new PyStegoError instance.
    #[new]
    fn new(message: String) -> Self {
        Self { message }
    }

    /// String representation of the error.
    fn __str__(&self) -> &str {
        &self.message
    }
}

/// Python wrapper for the encode function.
///
/// # Errors
/// Returns a [`PyStegoError`] if encoding fails.
#[pyfunction]
fn py_encode(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    encode(message, carrier, password).map_err(|e| PyStegoError::new_err(e.to_string()))
}

/// Python wrapper for the decode function.
///
/// # Errors
/// Returns a [`PyStegoError`] if decoding fails.
#[pyfunction]
fn py_decode(carrier: &str, password: Option<&str>) -> PyResult<String> {
    decode(carrier, password).map_err(|e| PyStegoError::new_err(e.to_string()))
}

/// Python wrapper for the extract_encoded function.
///
/// # Errors
/// Returns a [`PyStegoError`] if extraction fails.
#[pyfunction]
fn py_extract_encoded(carrier: &str) -> PyResult<(String, String)> {
    extract_encoded(carrier).map_err(|e| PyStegoError::new_err(e.to_string()))
}

/// Add Python bindings to the module.
///
/// # Errors
/// Returns a [`PyErr`] if adding functions or classes fails.
pub fn add_python_bindings(m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_encode, m)?)?;
    m.add_function(wrap_pyfunction!(py_decode, m)?)?;
    m.add_function(wrap_pyfunction!(py_extract_encoded, m)?)?;
    m.add_class::<PyStegoError>()?;
    Ok(())
}
