use aes_gcm::{
    aead::{Aead, KeyInit},
    Aes256Gcm, Key, Nonce,
};
use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use pbkdf2::{
    password_hash::{PasswordHash, PasswordHasher, PasswordVerifier, SaltString},
    Pbkdf2,
};
use pyo3::prelude::*;
use sha2::Sha256;
use thiserror::Error;

const ZERO_WIDTH_SPACE: char = '\u{200B}';
const ZERO_WIDTH_NON_JOINER: char = '\u{200C}';
const WORD_JOINER: char = '\u{2060}';
const FUNCTION_APPLICATION: char = '\u{2061}';

#[derive(Error, Debug)]
pub enum StegoError {
    #[error("Encryption error: {0}")]
    Encryption(String),
    #[error("Decryption error: {0}")]
    Decryption(String),
    #[error("Invalid carrier: {0}")]
    InvalidCarrier(String),
}

impl From<aes_gcm::Error> for StegoError {
    fn from(err: aes_gcm::Error) -> Self {
        StegoError::Encryption(err.to_string())
    }
}

fn derive_key(password: &str) -> Result<Key<Aes256Gcm>, StegoError> {
    let salt = SaltString::generate(&mut rand::thread_rng());
    let hash = Pbkdf2::hash_password(password.as_bytes(), &salt)
        .map_err(|e| StegoError::Encryption(e.to_string()))?;
    let key_bytes = hash.hash.unwrap().as_bytes();
    Key::<Aes256Gcm>::from_slice(key_bytes)
        .try_clone()
        .map_err(|e| StegoError::Encryption(e.to_string()))
}

fn encrypt_message(message: &str, password: Option<&str>) -> Result<String, StegoError> {
    if let Some(pwd) = password {
        let key = derive_key(pwd)?;
        let cipher = Aes256Gcm::new(&key);
        let nonce = Nonce::from_slice(b"whitespace_stego_nonce");
        let ciphertext = cipher
            .encrypt(nonce, message.as_bytes())
            .map_err(|e| StegoError::Encryption(e.to_string()))?;
        Ok(BASE64.encode(ciphertext))
    } else {
        Ok(BASE64.encode(message.as_bytes()))
    }
}

fn decrypt_message(encrypted: &str, password: Option<&str>) -> Result<String, StegoError> {
    if let Some(pwd) = password {
        let key = derive_key(pwd)?;
        let cipher = Aes256Gcm::new(&key);
        let nonce = Nonce::from_slice(b"whitespace_stego_nonce");
        let ciphertext = BASE64
            .decode(encrypted)
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        let plaintext = cipher
            .decrypt(nonce, ciphertext.as_slice())
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        String::from_utf8(plaintext).map_err(|e| StegoError::Decryption(e.to_string()))
    } else {
        let decoded = BASE64
            .decode(encrypted)
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        String::from_utf8(decoded).map_err(|e| StegoError::Decryption(e.to_string()))
    }
}

fn binary_to_zero_width(binary: &str) -> String {
    binary
        .chars()
        .map(|c| match c {
            '0' => ZERO_WIDTH_SPACE,
            '1' => ZERO_WIDTH_NON_JOINER,
            _ => c,
        })
        .collect()
}

fn zero_width_to_binary(zero_width: &str) -> String {
    zero_width
        .chars()
        .map(|c| match c {
            c if c == ZERO_WIDTH_SPACE => '0',
            c if c == ZERO_WIDTH_NON_JOINER => '1',
            _ => c,
        })
        .collect()
}

#[pyfunction]
fn encode_rs(message: &str, carrier: &str, password: Option<&str>) -> PyResult<String> {
    let encrypted = encrypt_message(message, password)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;
    
    let binary: String = encrypted
        .bytes()
        .map(|b| format!("{:08b}", b))
        .collect();
    
    let zero_width = binary_to_zero_width(&binary);
    let framed = format!("{}{}{}", WORD_JOINER, zero_width, FUNCTION_APPLICATION);
    
    if carrier.is_empty() {
        Ok(framed)
    } else {
        Ok(format!("{}{}{}", &carrier[0..1], framed, &carrier[1..]))
    }
}

#[pyfunction]
fn decode_rs(carrier: &str, password: Option<&str>) -> PyResult<String> {
    let start = carrier
        .find(WORD_JOINER)
        .ok_or_else(|| PyErr::new::<pyo3::exceptions::PyValueError, _>("No start delimiter found"))?;
    let end = carrier
        .find(FUNCTION_APPLICATION)
        .ok_or_else(|| PyErr::new::<pyo3::exceptions::PyValueError, _>("No end delimiter found"))?;
    
    if start >= end {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Invalid message format",
        ));
    }
    
    let zero_width = &carrier[start + 1..end];
    let binary = zero_width_to_binary(zero_width);
    
    let mut encrypted = String::new();
    for chunk in binary.as_bytes().chunks(8) {
        let byte = u8::from_str_radix(&String::from_utf8_lossy(chunk), 2)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;
        encrypted.push(byte as char);
    }
    
    decrypt_message(&encrypted, password)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))
}

#[pymodule]
fn whitespace_stego_rs(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_rs, m)?)?;
    m.add_function(wrap_pyfunction!(decode_rs, m)?)?;
    Ok(())
} 