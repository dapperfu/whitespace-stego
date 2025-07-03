//! Decoding functionality for whitespace steganography.
//!
//! This module provides functions for decoding zero-width Unicode characters
//! back to binary data and extracting messages from carrier text.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use std::fs::OpenOptions;
use std::io::Write;

use crate::constants::{END_MARKER, ONE_BIT, START_MARKER, ZERO_BIT};
use crate::crypto::decrypt_data;
use crate::error::StegoError;

fn debug_log(msg: &str) {
    if let Ok(mut file) = OpenOptions::new()
        .create(true)
        .append(true)
        .open("/tmp/rust_decode_debug.txt")
    {
        let _ = writeln!(file, "{}", msg);
    }
}

/// Convert a string of zero-width characters back to bytes.
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
///
/// # Examples
/// ```
/// let decoded = decode_binary("\u200D\u200D\u200D\u200D\u200D\u200D\u200D\u200D")?;
/// ```
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
        return Err(StegoError::invalid_binary_data(format!(
            "Incomplete byte: {} bits remaining",
            bit_count
        )));
    }

    Ok(result)
}

/// Decode messages from carrier text containing zero-width characters.
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
///
/// # Examples
/// ```
/// let decoded = decode("carrier\u200Bhidden\u200C", None)?;
/// ```
pub fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    let messages = decode_all(carrier, password)?;

    // Return string for single message, join with newlines for multiple messages
    if messages.len() == 1 {
        Ok(messages.into_iter().next().unwrap())
    } else {
        Ok(messages.join("\n"))
    }
}

/// Decode all messages from carrier text containing zero-width characters.
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
///
/// # Examples
/// ```
/// let messages = decode_all("carrier\u200Bhidden1\u200C\u200Bhidden2\u200C", None)?;
/// ```
pub fn decode_all(carrier: &str, password: Option<&str>) -> Result<Vec<String>, StegoError> {
    debug_log("[DEBUG] decode_all: function entered");
    debug_log(&format!("[DEBUG] decode_all input carrier: {:?}", carrier));
    let mut messages = Vec::new();
    let mut decryption_failures = 0;
    let chars: Vec<char> = carrier.chars().collect();
    let carrier_len = chars.len();
    let start_marker_len = 1; // START_MARKER is a char, so length is 1
    let end_marker_len = 1; // END_MARKER is a char, so length is 1
    debug_log(&format!(
        "[DEBUG] carrier_len: {} start_marker_len: {} end_marker_len: {}",
        carrier_len, start_marker_len, end_marker_len
    ));
    let mut i = 0;
    while i + start_marker_len <= carrier_len {
        debug_log(&format!("[DEBUG] marker search loop: i = {}", i));
        // Find start marker
        if chars[i] == START_MARKER {
            debug_log(&format!("[DEBUG] Found start marker at char {}", i));
            // Find end marker after start
            let mut j = i + start_marker_len;
            while j + end_marker_len <= carrier_len {
                debug_log(&format!("[DEBUG] end marker search: j = {}", j));
                if chars[j] == END_MARKER {
                    debug_log(&format!("[DEBUG] Found end marker at char {}", j));
                    // About to slice chars for encoded message
                    debug_log(&format!(
                        "[DEBUG] About to slice chars[{}..{}] (len={})",
                        i + start_marker_len,
                        j,
                        chars.len()
                    ));
                    let encoded: String = chars[i + start_marker_len..j].iter().collect();
                    debug_log(&format!("[DEBUG] Extracted encoded message: {:?}", encoded));
                    // Convert zero-width characters back to binary
                    let data = match decode_binary(&encoded) {
                        Ok(d) => d,
                        Err(_) => {
                            decryption_failures += 1;
                            i = j + end_marker_len;
                            break;
                        },
                    };
                    // Decrypt if password provided
                    if let Some(pwd) = password {
                        // Base64 decode the data to get encrypted bytes
                        match BASE64.decode(&data) {
                            Ok(encrypted) => {
                                // Decrypt the encrypted bytes
                                match decrypt_data(&encrypted, pwd) {
                                    Ok(decrypted) => {
                                        // The decrypted data is the original message
                                        match String::from_utf8(decrypted) {
                                            Ok(message) => messages.push(message),
                                            Err(_) => {
                                                // Map UTF-8 error to decryption failed
                                                decryption_failures += 1;
                                                i = j + end_marker_len;
                                                break;
                                            },
                                        }
                                    },
                                    Err(_) => {
                                        // Map decryption error to decryption failed
                                        decryption_failures += 1;
                                        i = j + end_marker_len;
                                        break;
                                    },
                                }
                            },
                            Err(_) => {
                                // Map base64 decode error to decryption failed
                                decryption_failures += 1;
                                i = j + end_marker_len;
                                break;
                            },
                        }
                    } else {
                        // For non-password messages, base64 decode the data directly
                        match BASE64.decode(&data) {
                            Ok(decoded) => {
                                match String::from_utf8(decoded) {
                                    Ok(message) => messages.push(message),
                                    Err(_) => {
                                        // Map UTF-8 error to decryption failed
                                        decryption_failures += 1;
                                        i = j + end_marker_len;
                                        break;
                                    },
                                }
                            },
                            Err(_) => {
                                // Map base64 decode error to decryption failed
                                decryption_failures += 1;
                                i = j + end_marker_len;
                                break;
                            },
                        }
                    }
                    // Move i past this message
                    i = j + end_marker_len;
                    break;
                }
                j += 1;
            }
            // If no end marker found, break
            if j + end_marker_len > carrier_len {
                debug_log("[DEBUG] No end marker found after start marker");
                break;
            }
        } else {
            i += 1;
        }
    }
    debug_log("[DEBUG] marker search loop finished");
    if password.is_some() && decryption_failures > 0 && !messages.is_empty() {
        debug_log("[DEBUG] returning partial messages due to decryption failures");
        return Ok(messages);
    }
    if decryption_failures > 0 && messages.is_empty() {
        debug_log("[DEBUG] raising error for decryption failure");
        return Err(StegoError::decryption_failed(
            "Decryption failed or no valid messages found in carrier text",
        ));
    }
    if password.is_some() && messages.is_empty() {
        debug_log("[DEBUG] raising error for wrong password");
        return Err(StegoError::decryption_failed(
            "Invalid password or no valid messages found in carrier text",
        ));
    }
    if messages.is_empty() {
        debug_log("[DEBUG] returning error: no valid messages found");
        return Err(StegoError::invalid_carrier(
            "No valid messages found in carrier text",
        ));
    }
    debug_log("[DEBUG] returning decoded messages");
    Ok(messages)
}

/// Extract the encoded message and remaining carrier text.
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
///
/// # Examples
/// ```
/// let (encoded, remaining) = extract_encoded("text\u200Bhidden\u200Cmore")?;
/// ```
pub fn extract_encoded(carrier: &str) -> Result<(String, String), StegoError> {
    let start = carrier
        .find(START_MARKER)
        .ok_or_else(|| StegoError::invalid_carrier("No start marker found"))?;
    let end = carrier[start..]
        .find(END_MARKER)
        .map(|e| start + e)
        .ok_or_else(|| StegoError::invalid_carrier("No end marker found after start marker"))?;

    if end <= start {
        return Err(StegoError::invalid_carrier(
            "End marker before start marker",
        ));
    }

    // Use char_indices to find the correct UTF-8 boundaries
    let mut start_char_pos = 0;
    let mut end_char_pos = 0;
    let mut found_start = false;
    let mut found_end = false;

    for (char_pos, (byte_pos, ch)) in carrier.char_indices().enumerate() {
        if byte_pos == start && !found_start {
            start_char_pos = char_pos;
            found_start = true;
        }
        if byte_pos == end && !found_end {
            end_char_pos = char_pos;
            found_end = true;
            break;
        }
    }

    if !found_start || !found_end {
        return Err(StegoError::invalid_carrier("Invalid marker positions"));
    }

    // Extract the encoded part using char positions
    let encoded: String = carrier
        .chars()
        .skip(start_char_pos)
        .take(end_char_pos - start_char_pos + 1)
        .collect();

    // Extract remaining parts
    let before: String = carrier.chars().take(start_char_pos).collect();
    let after: String = carrier.chars().skip(end_char_pos + 1).collect();
    let mut remaining = before + &after;

    // If the remaining carrier starts with a START_MARKER, remove it
    // This handles the case where the original carrier started with a START_MARKER
    if remaining.starts_with(START_MARKER) {
        remaining = remaining.chars().skip(1).collect();
    }

    Ok((encoded, remaining))
}

/// Get the position of the encoded message in the carrier text.
///
/// # Arguments
/// * `carrier` - The carrier text containing the encoded message
///
/// # Returns
/// A tuple of (start_position, end_position) in characters, or `None` if not found
///
/// # Examples
/// ```
/// let pos = get_encoded_message_position("text\u200Bhidden\u200Cmore");
/// ```
pub fn get_encoded_message_position(carrier: &str) -> Option<(usize, usize)> {
    let start = carrier.find(START_MARKER)?;
    let end = carrier.find(END_MARKER)?;

    if end <= start {
        return None;
    }

    Some((start, end))
}

/// Count the number of messages embedded in the carrier text.
///
/// This function counts the number of complete start/end marker pairs,
/// which represents the number of messages that have been embedded.
///
/// # Arguments
/// * `carrier` - The carrier text to analyze
///
/// # Returns
/// The number of messages embedded in the carrier text
///
/// # Examples
/// ```
/// let count = count_messages("text\u200Bhidden1\u200C\u200Bhidden2\u200C");
/// assert_eq!(count, 2);
/// ```
pub fn count_messages(carrier: &str) -> usize {
    let start_count = carrier.matches(START_MARKER).count();
    let end_count = carrier.matches(END_MARKER).count();
    start_count.min(end_count)
}

/// Debug function that only logs the input carrier text.
///
/// This function is used for debugging purposes to log carrier text
/// without performing any decoding operations.
///
/// # Arguments
/// * `carrier` - The carrier text to log
///
/// # Returns
/// Always returns `Ok(())`
///
/// # Examples
/// ```
/// let _ = decode_debug_log_only("test input");
/// ```
#[allow(dead_code)]
pub fn decode_debug_log_only(carrier: &str) -> Result<(), StegoError> {
    debug_log("[DEBUG] decode_debug_log_only: function entered");
    debug_log(&format!("[DEBUG] input carrier: {:?}", carrier));
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_decode_debug_log_only_creates_log() {
        let _ = std::fs::remove_file("/tmp/rust_decode_debug.txt");
        let result = decode_debug_log_only("test input \u{feff} marker");
        assert!(result.is_ok());
        let contents =
            std::fs::read_to_string("/tmp/rust_decode_debug.txt").expect("log file should exist");
        assert!(contents.contains("function entered"));
        assert!(contents.contains("test input"));
    }
}
