use base64::{Engine as _, engine::general_purpose::STANDARD as BASE64};
use crate::charset::{char_to_binary, START_MARKER, END_MARKER};

/// Extract the steganographic payload from text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden payload
///
/// # Returns
///
/// * `Result<(String, usize, usize), String>` - A tuple containing (payload, start_pos, end_pos), or an error message
pub fn extract_payload(text: &str) -> Result<(String, usize, usize), String> {
    let start_pos = text.find(START_MARKER).ok_or("No start marker found in text")?;
    let end_pos = text[start_pos..]
        .find(END_MARKER)
        .ok_or("No end marker found in text")? + start_pos;

    let payload = text[start_pos + START_MARKER.len()..end_pos].to_string();
    Ok((payload, start_pos, end_pos + END_MARKER.len()))
}

/// Decode zero-width characters back to binary string.
///
/// # Arguments
///
/// * `encoded` - The encoded string using zero-width characters
///
/// # Returns
///
/// * `Result<String, String>` - The decoded binary string, or an error message
pub fn decode_binary(encoded: &str) -> Result<String, String> {
    let mut binary = String::new();
    for c in encoded.chars() {
        let bit = char_to_binary(c)
            .ok_or_else(|| format!("Invalid character in encoded string: {}", c))?;
        binary.push_str(&bit.to_string());
    }
    Ok(binary)
}

/// Convert a binary string to bytes.
pub fn binary_to_bytes(binary: &str) -> Result<Vec<u8>, String> {
    if binary.len() % 8 != 0 {
        return Err("Binary string length must be a multiple of 8".to_string());
    }
    let bytes: Vec<u8> = binary
        .as_bytes()
        .chunks(8)
        .map(|chunk| {
            let byte_str = std::str::from_utf8(chunk).unwrap();
            u8::from_str_radix(byte_str, 2).unwrap()
        })
        .collect();
    Ok(bytes)
}

/// Convert a binary string to the original message string via base64 decode.
///
/// # Arguments
///
/// * `binary` - A string of '0's and '1's representing base64 characters
///
/// # Returns
///
/// * `Result<String, String>` - The decoded base64 string, or an error message
pub fn binary_to_base64(binary: &str) -> Result<String, String> {
    let bytes = binary_to_bytes(binary)?;
    let base64_decoded = BASE64.decode(&bytes).map_err(|e| format!("Base64 decode error: {}", e))?;
    String::from_utf8(base64_decoded).map_err(|e| format!("UTF-8 decode error: {}", e))
}

/// Decode a hidden message from text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
/// * `password` - Optional password for decryption
///
/// # Returns
///
/// * `Result<String, String>` - The decoded message, or an error message
pub fn decode_message(text: &str, password: Option<&str>) -> Result<String, String> {
    // Extract the payload
    let (payload, _, _) = extract_payload(text)?;

    // Decode binary
    let binary = decode_binary(&payload)?;

    // Convert to base64 (actually, to the original message)
    if let Some(_pwd) = password {
        // TODO: Implement decryption with password
        binary_to_base64(&binary)
    } else {
        binary_to_base64(&binary)
    }
}

/// Decode a hidden message and remove it from the carrier text.
///
/// # Arguments
///
/// * `text` - The text containing the hidden message
/// * `password` - Optional password for decryption
///
/// # Returns
///
/// * `Result<(String, String), String>` - A tuple containing (decoded_message, carrier_text), or an error message
pub fn decode_and_remove(text: &str, password: Option<&str>) -> Result<(String, String), String> {
    // Extract payload and positions
    let (_, start_pos, end_pos) = extract_payload(text)?;

    // Decode the message
    let message = decode_message(text, password)?;

    // Remove the payload from the text
    let carrier = format!("{}{}", &text[..start_pos], &text[end_pos..]);

    Ok((message, carrier))
} 