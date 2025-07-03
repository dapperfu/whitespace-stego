use pyo3::exceptions::PyValueError;

/// Converts StegoError to a Python error.
impl From<StegoError> for PyErr {
    fn from(err: StegoError) -> PyErr {
        PyValueError::new_err(err.0)
    }
}

//!
//! Decoding utilities for whitespace steganography.
//!
//! Provides the `decode` function for extracting messages from carrier text, optionally decrypting.
//!
//! ## Examples
//! See the `decode` function for usage examples.

/// Decodes a message from the given carrier string, optionally decrypting with a password.
///
/// # Errors
/// Returns a [`PyErr`] if decoding fails, the message is not found, or decryption fails.
///
/// # Examples
/// ```
/// let decoded = decode("carrier text with secret", Some("password"))?;
/// ```
pub fn decode(carrier: &str, password: Option<&str>) -> PyResult<String> {
    let start = carrier
        .find(START_MARKER)
        .ok_or_else(|| StegoError::from("No valid message found in carrier text".to_string()))
        .map_err(PyErr::from)?;
    let end = carrier
        .find(END_MARKER)
        .ok_or_else(|| StegoError::from("No valid message found in carrier text".to_string()))
        .map_err(PyErr::from)?;
    let data = &carrier[start + START_MARKER.len()..end];
    let bytes = zero_width_to_bytes(data).map_err(PyErr::from)?;
    let data = URL_SAFE
        .decode(&bytes)
        .map_err(|e| PyErr::from(StegoError::from(e.to_string())))?;
    let decoded = if let Some(pwd) = password {
        let key_bytes: Vec<u8> = pwd
            .as_bytes()
            .iter()
            .cloned()
            .chain(std::iter::repeat(0))
            .take(32)
            .collect();
        let key = URL_SAFE.encode(&key_bytes);
        let f = fernet::Fernet::new(&key)
            .ok_or_else(|| StegoError::from("Invalid Fernet key".to_string()))
            .map_err(PyErr::from)?;
        f.decrypt(&data)
            .map_err(|e| PyErr::from(StegoError::from(e.to_string())))?
    } else {
        data
    };
    Ok(String::from_utf8(decoded).map_err(|e| PyErr::from(StegoError::from(e.to_string())))?)
}
