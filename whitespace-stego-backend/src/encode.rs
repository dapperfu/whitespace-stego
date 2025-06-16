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

fn encode_binary(data: &[u8]) -> String {
    let binary: String = data
        .iter()
        .map(|byte| format!("{:08b}", byte))
        .collect::<Vec<String>>()
        .join("");
    
    binary
        .chars()
        .map(|bit| if bit == '1' { ONE_BIT } else { ZERO_BIT })
        .collect()
}

#[pyfunction]
pub fn encode(message: &str, carrier: Option<&str>, password: Option<&str>) -> PyResult<String> {
    // Base64 encode the message
    let encoded = base64::engine::general_purpose::STANDARD.encode(message.as_bytes());

    // Add password encryption if provided
    let encoded = if let Some(pwd) = password {
        let key = URL_SAFE.encode(pwd.as_bytes().iter().chain(std::iter::repeat(&0)).take(32));
        let f = fernet::Fernet::new(&key).map_err(|e| StegoError::from(e.to_string()))?;
        f.encrypt(&encoded).map_err(|e| StegoError::from(e.to_string()))?
    } else {
        encoded.into_bytes()
    };

    // Convert to zero-width characters
    let zero_width = encode_binary(&encoded);

    // Add markers
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);

    // Return just the encoded message if no carrier
    if carrier.is_none() {
        return Ok(encoded_message);
    }

    // Embed in carrier after first Unicode character
    let carrier = carrier.unwrap();
    let chars: Vec<char> = carrier.chars().collect();
    if chars.len() > 1 {
        Ok(format!("{}{}{}", chars[0], encoded_message, chars[1..].iter().collect::<String>()))
    } else {
        Ok(format!("{}{}", carrier, encoded_message))
    }
} 