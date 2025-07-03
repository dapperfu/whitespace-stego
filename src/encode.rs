//!
//! Encoding utilities for whitespace steganography.
//!
//! Provides the `encode` function for embedding messages in carrier text, optionally encrypted.
//!
//! ## Examples
//! See the `encode` function for usage examples.

use pyo3::exceptions::PyValueError;

/// Converts StegoError to a Python error.
impl From<StegoError> for PyErr {
    fn from(err: StegoError) -> PyErr {
        PyValueError::new_err(err.0)
    }
}

/// Encodes a message into the given carrier string, optionally encrypting with a password.
///
/// # Errors
/// Returns a [`PyErr`] if encryption fails or the Fernet key is invalid.
///
/// # Examples
/// ```
/// let encoded = encode("secret", "cover text", Some("password"))?;
/// ```
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    let mut data = message.as_bytes().to_vec();
    if let Some(pwd) = password {
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
        let token = f.encrypt(message.as_bytes());
        data = token;
    }
    Ok(format!(
        "{carrier}{START_MARKER}{encoded}{END_MARKER}",
        carrier = carrier,
        START_MARKER = START_MARKER,
        encoded = URL_SAFE.encode(&data),
        END_MARKER = END_MARKER
    ))
}
