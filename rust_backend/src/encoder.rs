use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{BINARY_TO_CHAR, START_MARKER, END_MARKER, is_valid_carrier};

/// Encode a binary string using zero-width characters.
///
/// # Arguments
///
/// * `binary_str` - A string of '0's and '1's to encode
///
/// # Returns
///
/// * `String` - The encoded string using zero-width characters
pub fn encode_binary(binary_str: &str) -> String {
    binary_str
        .chars()
        .map(|c| BINARY_TO_CHAR.get(&(c.to_digit(10).unwrap() as u8)).unwrap())
        .collect()
}

/// Encode a message into a steganographic payload.
///
/// # Arguments
///
/// * `message` - The message to encode
/// * `password` - Optional password for encryption before encoding
///
/// # Returns
///
/// * `String` - The encoded steganographic payload
pub fn encode_message(message: &str, password: Option<&str>) -> String {
    // First encrypt/encode the message
    let encrypted = if let Some(pwd) = password {
        // TODO: Implement encryption with password
        BASE64.encode(message.as_bytes())
    } else {
        BASE64.encode(message.as_bytes())
    };

    // Convert to binary
    let binary = encrypted
        .bytes()
        .map(|b| format!("{:08b}", b))
        .collect::<String>();

    // Encode binary using zero-width characters
    let encoded = encode_binary(&binary);

    // Wrap with control characters
    format!("{}{}{}", START_MARKER, encoded, END_MARKER)
}

/// Insert a steganographic payload into carrier text.
///
/// # Arguments
///
/// * `carrier` - The carrier text to insert the payload into
/// * `payload` - The encoded steganographic payload
/// * `position` - Position to insert the payload. If None, inserts at the end
///
/// # Returns
///
/// * `Result<String, String>` - The carrier text with the payload inserted, or an error message
pub fn insert_payload(carrier: &str, payload: &str, position: Option<usize>) -> Result<String, String> {
    if !is_valid_carrier(carrier) {
        return Err("Carrier text contains control characters".to_string());
    }

    let pos = position.unwrap_or_else(|| carrier.len());
    if pos > carrier.len() {
        return Err("Invalid insertion position".to_string());
    }

    let mut result = carrier.to_string();
    result.insert_str(pos, payload);
    Ok(result)
}

/// Encode a message and insert it into carrier text.
///
/// # Arguments
///
/// * `message` - The message to encode
/// * `carrier` - The carrier text to insert the encoded message into
/// * `password` - Optional password for encryption
/// * `position` - Position to insert the payload. If None, inserts at the end
///
/// # Returns
///
/// * `Result<String, String>` - The carrier text with the encoded message inserted, or an error message
pub fn encode_and_insert(
    message: &str,
    carrier: &str,
    password: Option<&str>,
    position: Option<usize>,
) -> Result<String, String> {
    let payload = encode_message(message, password);
    insert_payload(carrier, &payload, position)
} 