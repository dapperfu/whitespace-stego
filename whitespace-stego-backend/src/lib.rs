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
} 