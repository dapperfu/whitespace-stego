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
    let mut decryption_failures = 0;
    
    // Find all start and end markers using byte positions (safe for UTF-8)
    let mut start_positions = Vec::new();
    let mut end_positions = Vec::new();
    
    // Find all start markers
    let mut pos = 0;
    while pos < carrier.len() {
        if let Some(start_pos) = carrier[pos..].find(START_MARKER) {
            start_positions.push(pos + start_pos);
            pos = pos + start_pos + START_MARKER.len_utf8();
        } else {
            break;
        }
    }
    
    // Find all end markers
    pos = 0;
    while pos < carrier.len() {
        if let Some(end_pos) = carrier[pos..].find(END_MARKER) {
            end_positions.push(pos + end_pos);
            pos = pos + end_pos + END_MARKER.len_utf8();
        } else {
            break;
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
        
        // Extract the encoded message using byte positions (safe for UTF-8)
        let encoded = &carrier[start_pos + START_MARKER.len_utf8()..end_pos];
        
        // Convert zero-width characters back to binary
        let mut data = match decode_binary(encoded) {
            Ok(d) => d,
            Err(_) => {
                // Skip this message if binary decode fails
                decryption_failures += 1;
                start_idx += 1;
                end_idx += 1;
                continue;
            }
        };
        
        // Decrypt if password provided
        if let Some(pwd) = password {
            match decrypt_data(&data, pwd) {
                Ok(decrypted) => data = decrypted,
                Err(_) => {
                    // Skip this message if decryption fails (multi-recipient behavior)
                    decryption_failures += 1;
                    start_idx += 1;
                    end_idx += 1;
                    continue;
                }
            }
        } else if crate::crypto::is_encrypted(&data) {
            // If data is encrypted but no password is provided, skip this message
            decryption_failures += 1;
            start_idx += 1;
            end_idx += 1;
            continue;
        }
        
        // Base64 decode and convert to string
        match BASE64.decode(&data) {
            Ok(decoded) => {
                match String::from_utf8(decoded) {
                    Ok(message) => messages.push(message),
                    Err(_) => {
                        // Skip this message if UTF-8 conversion fails
                        decryption_failures += 1;
                        start_idx += 1;
                        end_idx += 1;
                        continue;
                    }
                }
            }
            Err(_) => {
                // Skip this message if base64 decode fails
                decryption_failures += 1;
                start_idx += 1;
                end_idx += 1;
                continue;
            }
        }
        
        // Move to next pair
        start_idx += 1;
        end_idx += 1;
    }
    
    // If we have a password and some messages failed to decrypt, but we successfully decrypted at least one,
    // this is a partial decode scenario (multi-recipient)
    if password.is_some() && decryption_failures > 0 && !messages.is_empty() {
        // Return only the successfully decrypted messages
        return Ok(messages);
    }
    
    // If we have a password and no messages were decrypted, return decryption error
    if password.is_some() && messages.is_empty() {
        return Err(StegoError::decryption_failed("Password was only able to decode part of the secret message"));
    }
    
    // If no messages found at all, return invalid carrier error
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
    
    // All positions are byte positions from find(), so slicing is safe
    let encoded = &carrier[start..end + END_MARKER.len_utf8()];
    let mut remaining = format!(
        "{}{}",
        &carrier[..start],
        &carrier[end + END_MARKER.len_utf8()..]
    );
    // If the remaining carrier starts with a START_MARKER, remove it
    // This handles the case where the original carrier started with a START_MARKER
    if remaining.starts_with(START_MARKER) {
        remaining = remaining[START_MARKER.len_utf8()..].to_string();
    }
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
    
    Some((start, end))
}

/// Count the number of messages embedded in the carrier text
///
/// This function counts the number of complete start/end marker pairs,
/// which represents the number of messages that have been embedded.
///
/// # Arguments
/// * `carrier` - The carrier text to analyze
///
/// # Returns
/// The number of messages embedded in the carrier text
pub fn count_messages(carrier: &str) -> usize {
    let start_count = carrier.matches(START_MARKER).count();
    let end_count = carrier.matches(END_MARKER).count();
    start_count.min(end_count)
} 