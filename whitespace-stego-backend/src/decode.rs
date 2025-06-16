use base64::{engine::general_purpose::URL_SAFE, Engine};
use pyo3::prelude::*;
use std::error::Error;
use std::fmt;

const START_MARKER: &str = "\u{200b}";  // Zero-width space
const END_MARKER: &str = "\u{200c}";    // Zero-width non-joiner
const ZERO_BIT: &str = "\u{200d}";      // Zero-width joiner
const ONE_BIT: &str = "\u{feff}";       // Zero-width no-break space

#[derive(Debug)]
pub struct StegoError {
    message: String,
}

impl Error for StegoError {}

impl fmt::Display for StegoError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.message)
    }
}

impl From<String> for StegoError {
    fn from(message: String) -> Self {
        StegoError { message }
    }
}

impl From<&str> for StegoError {
    fn from(message: &str) -> Self {
        StegoError {
            message: message.to_string(),
        }
    }
}

fn decode_binary(encoded: &str) -> Vec<u8> {
    let binary: String = encoded
        .chars()
        .map(|c| if c == ONE_BIT.chars().next().unwrap() { '1' } else { '0' })
        .collect();

    binary
        .as_bytes()
        .chunks(8)
        .map(|chunk| {
            let byte_str = std::str::from_utf8(chunk).unwrap();
            u8::from_str_radix(byte_str, 2).unwrap()
        })
        .collect()
}

#[pyfunction]
pub fn decode(carrier: &str, password: Option<&str>) -> PyResult<String> {
    // Find the encoded message between markers
    let start = carrier.find(START_MARKER).ok_or_else(|| StegoError::from("No valid message found in carrier text"))?;
    let end = carrier.find(END_MARKER).ok_or_else(|| StegoError::from("No valid message found in carrier text"))?;

    // Extract the encoded message
    let encoded = &carrier[start + START_MARKER.len()..end];

    // Convert from zero-width characters to bytes
    let data = decode_binary(encoded);

    // Decrypt if password provided
    let data = if let Some(pwd) = password {
        let key = URL_SAFE.encode(pwd.as_bytes().iter().chain(std::iter::repeat(&0)).take(32));
        let f = fernet::Fernet::new(&key).map_err(|e| StegoError::from(e.to_string()))?;
        f.decrypt(&data).map_err(|e| StegoError::from(e.to_string()))?
    } else {
        data
    };

    // Base64 decode and convert to string
    let decoded = base64::engine::general_purpose::STANDARD
        .decode(data)
        .map_err(|e| StegoError::from(e.to_string()))?;
    
    String::from_utf8(decoded).map_err(|e| StegoError::from(e.to_string()))
} 