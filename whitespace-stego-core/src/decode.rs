//! Decoding functionality for whitespace steganography.
//!
//! This module provides functions for decoding zero-width Unicode characters
//! back to binary data and extracting messages from carrier text.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};

use crate::constants::{START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT};
use crate::crypto::decrypt_data;
use crate::error::StegoError;

/// Convert a string of zero-width characters back to bytes
///
/// Each 8 zero-width characters are converted back to a single byte, where:
/// - `ZERO_BIT` represents a 0 bit
/// - `ONE_BIT` represents a 1 bit
///
/// # Arguments
/// * `encoded` - The string containing zero-width characters
///
/// # Returns
/// The decoded binary data
///
/// # Errors
/// Returns `StegoError::InvalidBinaryData` if the encoded data is malformed
pub fn decode_binary(encoded: &str) -> Result<Vec<u8>, StegoError> {
    let mut result = Vec::new();
    let mut current_byte = 0u8;
    let mut bit_count = 0;

    for c in encoded.chars() {
        if c == ONE_BIT || c == ZERO_BIT {
            current_byte = (current_byte << 1) | if c == ONE_BIT { 1 } else { 0 };
            bit_count += 1;

            if bit_count == 8 {
                result.push(current_byte);
                current_byte = 0;
                bit_count = 0;
            }
        }
    }

    // Check if we have incomplete bytes
    if bit_count > 0 {
        return Err(StegoError::invalid_binary_data(
            format!("Incomplete byte: {} bits remaining", bit_count)
        ));
    }

    Ok(result)
}

/// Decode messages from carrier text containing zero-width characters
///
/// This function:
/// 1. Finds all encoded messages between start and end markers
/// 2. Converts zero-width characters back to binary data
/// 3. Optionally decrypts the data with a password
/// 4. Base64 decodes the data to get the original messages
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded messages
/// * `password` - Optional password for decryption
///
/// # Returns
/// A single decoded message as String, or a vector of decoded messages if multiple
///
/// # Errors
/// Returns `StegoError::InvalidCarrier` if no markers are found
/// Returns `StegoError::DecryptionFailed` if decryption fails
/// Returns `StegoError::InvalidBinaryData` if the encoded data is malformed
pub fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    let messages = decode_all(carrier, password)?;
    
    // Return string for single message, join with newlines for multiple messages
    if messages.len() == 1 {
        Ok(messages.into_iter().next().unwrap())
    } else {
        Ok(messages.join("\n"))
    }
}

/// Decode all messages from carrier text containing zero-width characters
///
/// This function:
/// 1. Finds all encoded messages between start and end markers
/// 2. Converts zero-width characters back to binary data
/// 3. Optionally decrypts the data with a password
/// 4. Base64 decodes the data to get the original messages
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded messages
/// * `password` - Optional password for decryption
///
/// # Returns
/// A vector of decoded messages
///
/// # Errors
/// Returns `StegoError::InvalidCarrier` if no markers are found
/// Returns `StegoError::DecryptionFailed` if decryption fails
/// Returns `StegoError::InvalidBinaryData` if the encoded data is malformed
pub fn decode_all(carrier: &str, password: Option<&str>) -> Result<Vec<String>, StegoError> {
    let mut messages = Vec::new();
    
    // Find all start and end markers
    let mut start_positions = Vec::new();
    let mut end_positions = Vec::new();
    
    // Use char_indices to handle UTF-8 boundaries correctly
    for (char_pos, _) in carrier.char_indices() {
        if carrier[char_pos..].starts_with(START_MARKER) {
            start_positions.push(char_pos);
        }
        if carrier[char_pos..].starts_with(END_MARKER) {
            end_positions.push(char_pos);
        }
    }
    
    // Match start and end markers to extract messages
    let mut start_idx = 0;
    let mut end_idx = 0;
    
    while start_idx < start_positions.len() && end_idx < end_positions.len() {
        let start_pos = start_positions[start_idx];
        let end_pos = end_positions[end_idx];
        
        // Find the next valid pair (end after start)
        if end_pos <= start_pos {
            end_idx += 1;
            continue;
        }
        
        // Extract the encoded message
        let encoded = &carrier[start_pos + START_MARKER.len_utf8()..end_pos];
        
        // Convert zero-width characters back to binary
        let mut data = decode_binary(encoded)?;
        
        // Decrypt if password provided
        if let Some(pwd) = password {
            match decrypt_data(&data, pwd) {
                Ok(decrypted) => data = decrypted,
                Err(_) => {
                    // Raise error if decryption fails (matches Python BadPasswordError behavior)
                    return Err(StegoError::decryption_failed("Password was only able to decode part of the secret message"));
                }
            }
        }
        
        // Base64 decode and convert to string
        match BASE64.decode(&data) {
            Ok(decoded) => {
                match String::from_utf8(decoded) {
                    Ok(message) => messages.push(message),
                    Err(_) => {
                        // Skip this message if UTF-8 conversion fails
                        start_idx += 1;
                        end_idx += 1;
                        continue;
                    }
                }
            }
            Err(_) => {
                // Skip this message if base64 decode fails
                start_idx += 1;
                end_idx += 1;
                continue;
            }
        }
        
        // Move to next pair
        start_idx += 1;
        end_idx += 1;
    }
    
    if messages.is_empty() {
        return Err(StegoError::invalid_carrier("No valid messages found in carrier text"));
    }
    
    Ok(messages)
}

/// Extract the encoded message and remaining carrier text
///
/// This function separates the encoded message from the carrier text,
/// returning both parts. This is useful for analyzing the structure
/// of encoded text or for partial processing.
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
///
/// # Returns
/// A tuple of (encoded_message, remaining_carrier)
///
/// # Errors
/// Returns `StegoError::InvalidCarrier` if no markers are found
pub fn extract_encoded(carrier: &str) -> Result<(String, String), StegoError> {
    let start = carrier.find(START_MARKER)
        .ok_or_else(|| StegoError::invalid_carrier("No start marker found"))?;
    let end = carrier[start + START_MARKER.len_utf8()..]
        .find(END_MARKER)
        .map(|e| start + START_MARKER.len_utf8() + e)
        .ok_or_else(|| StegoError::invalid_carrier("No end marker found after start marker"))?;
    if end <= start {
        return Err(StegoError::invalid_carrier("End marker before start marker"));
    }
    let encoded = &carrier[start..end + END_MARKER.len_utf8()];
    let remaining = format!(
        "{}{}",
        &carrier[..start],
        &carrier[end + END_MARKER.len_utf8()..]
    );
    Ok((encoded.to_string(), remaining))
}

/// Get the position of the encoded message in the carrier text
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
///
/// # Returns
/// A tuple of (start_position, end_position) in characters, or `None` if not found
pub fn get_encoded_message_position(carrier: &str) -> Option<(usize, usize)> {
    let start = carrier.find(START_MARKER)?;
    let end = carrier.find(END_MARKER)?;
    
    if end <= start {
        return None;
    }
    
    Some((start, end + END_MARKER.len_utf8()))
} 