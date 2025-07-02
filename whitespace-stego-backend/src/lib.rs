use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use whitespace_stego_core::{encode, decode, decode_all, count_messages, StegoError};

/// A Python module implemented in Rust.
#[pymodule]
fn whitespace_stego_backend(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_py, m)?)?;
    m.add_function(wrap_pyfunction!(decode_all_py, m)?)?;
    m.add_function(wrap_pyfunction!(count_messages_py, m)?)?;
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

#[pyfunction]
pub fn decode_all_py(carrier: &str, password: Option<&str>) -> PyResult<Vec<String>> {
    decode_all(carrier, password).map_err(|e| PyValueError::new_err(e.to_string()))
}

#[pyfunction]
pub fn count_messages_py(carrier: &str) -> PyResult<usize> {
    Ok(count_messages(carrier))
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