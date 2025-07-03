//! Encoding functionality for whitespace steganography.
//!
//! This module provides functions for encoding binary data into zero-width
//! Unicode characters and embedding messages into carrier text.

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use regex::Regex;

use crate::constants::{END_MARKER, ONE_BIT, START_MARKER, ZERO_BIT};
use crate::crypto::{encrypt_data, is_encrypted};
use crate::error::StegoError;

/// Convert bytes to a string of zero-width characters
///
/// Each byte is converted to 8 zero-width characters, where:
/// - `ZERO_BIT` represents a 0 bit
/// - `ONE_BIT` represents a 1 bit
///
/// # Arguments
/// * `data` - The binary data to encode
///
/// # Returns
/// A string containing only zero-width Unicode characters
pub fn encode_binary(data: &[u8]) -> String {
    data.iter()
        .flat_map(|&byte| {
            (0..8).map(move |i| {
                if (byte >> (7 - i)) & 1 == 1 {
                    ONE_BIT
                } else {
                    ZERO_BIT
                }
            })
        })
        .collect()
}

/// Count the number of start/end marker pairs in the carrier text
///
/// # Arguments
/// * `carrier` - The carrier text to analyze
///
/// # Returns
/// The number of complete start/end marker pairs found
fn count_message_pairs(carrier: &str) -> usize {
    let start_count = carrier.matches(START_MARKER).count();
    let end_count = carrier.matches(END_MARKER).count();
    start_count.min(end_count)
}

/// Find the next available slot for encoding a message
///
/// The algorithm places messages in slots between characters of the original carrier string,
/// skipping over already-encoded messages.
/// - First message goes between characters 0 and 1
/// - Second message goes between characters 1 and 2
/// - And so on until the last character
/// - Remaining messages go before the last visible character
///
/// # Arguments
/// * `carrier` - The carrier text to find a slot in
///
/// # Returns
/// The position where the next message should be inserted
fn find_next_slot(carrier: &str) -> usize {
    // Remove all encoded messages to get the original carrier
    let start_escaped = regex::escape(&START_MARKER.to_string());
    let end_escaped = regex::escape(&END_MARKER.to_string());
    let pattern = Regex::new(&format!("{}.*?{}", start_escaped, end_escaped)).unwrap();
    let cleaned_carrier = pattern.replace_all(carrier, "").to_string();

    // Count how many messages are already encoded
    let existing_messages = count_message_pairs(carrier);

    // If no existing messages, place after first character
    if existing_messages == 0 {
        return if cleaned_carrier.chars().count() > 1 {
            1
        } else {
            0
        };
    }

    // For subsequent messages, place in slots between characters
    // until we reach the last character, then place before the last character
    let char_count = cleaned_carrier.chars().count();
    if existing_messages < char_count - 1 {
        existing_messages + 1
    } else {
        // Place before the last visible character
        char_count - 1
    }
}

/// Insert an encoded message at a specific position in the original carrier, skipping over already-encoded messages
///
/// # Arguments
/// * `carrier` - The carrier text (may already contain encoded messages)
/// * `encoded_message` - The encoded message to insert
/// * `position` - The position to insert the message at (in the original carrier, not counting encoded messages)
///
/// # Returns
/// The carrier text with the message inserted
fn insert_message_at_position(carrier: &str, encoded_message: &str, position: usize) -> String {
    // Remove all encoded messages to get the original carrier
    let start_escaped = regex::escape(&START_MARKER.to_string());
    let end_escaped = regex::escape(&END_MARKER.to_string());
    let pattern = Regex::new(&format!("{}.*?{}", start_escaped, end_escaped)).unwrap();
    let cleaned_carrier = pattern.replace_all(carrier, "").to_string();

    // Insert the encoded message at the correct position in the cleaned carrier
    let mut new_carrier = String::new();
    if position == 0 {
        new_carrier = encoded_message.to_string() + &cleaned_carrier;
    } else if position >= cleaned_carrier.chars().count() {
        new_carrier = cleaned_carrier + encoded_message;
    } else {
        // Convert to char indices for proper insertion
        let chars: Vec<char> = cleaned_carrier.chars().collect();
        let mut result = String::new();
        for (i, &ch) in chars.iter().enumerate() {
            if i == position {
                result.push_str(encoded_message);
            }
            result.push(ch);
        }
        new_carrier = result;
    }

    // Now, re-insert all previously encoded messages at their original positions
    let mut result = new_carrier;
    let matches: Vec<_> = pattern.find_iter(carrier).collect();
    let mut offset = 0;

    for mat in matches {
        // Find the position in the cleaned carrier where this encoded message was originally
        let pre = &carrier[..mat.start()];
        let cleaned_pre = pattern.replace_all(pre, "").to_string();
        let insert_pos = cleaned_pre.chars().count() + offset;

        // Insert at the correct character position
        let chars: Vec<char> = result.chars().collect();
        let mut new_result = String::new();
        for (i, &ch) in chars.iter().enumerate() {
            if i == insert_pos {
                new_result.push_str(mat.as_str());
            }
            new_result.push(ch);
        }
        if insert_pos >= chars.len() {
            new_result.push_str(mat.as_str());
        }
        result = new_result;
        offset += mat.as_str().chars().count();
    }

    result
}

/// Encode a message into carrier text using zero-width characters
///
/// This function:
/// 1. Base64 encodes the message
/// 2. Optionally encrypts the data with a password
/// 3. Converts the data to zero-width characters
/// 4. Embeds the encoded message in the carrier text at the next available slot
///
/// # Arguments
/// * `message` - The message to encode
/// * `carrier` - The carrier text to hide the message in
/// * `password` - Optional password for encryption
///
/// # Returns
/// The carrier text with the encoded message embedded
///
/// # Errors
/// Returns `StegoError::EncodingFailed` if encryption fails
/// Returns `StegoError::InvalidCarrier` if the carrier is invalid
pub fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    // Check for empty message with humorous error
    if message.is_empty() {
        return Err(StegoError::encoding_failed(
            "🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!"
        ));
    }

    // Encrypt if password provided, then base64 encode
    let data = if let Some(pwd) = password {
        // Encrypt the original message first
        let encrypted = encrypt_data(message.as_bytes(), pwd)?;
        // Base64 encode the encrypted data to convert random bytes to safe ASCII
        BASE64.encode(&encrypted).into_bytes()
    } else {
        // For non-password messages, base64 encode the original message
        BASE64.encode(message.as_bytes()).into_bytes()
    };

    // Convert to zero-width characters
    let zero_width = encode_binary(&data);
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);

    // Return just the encoded message if no carrier
    if carrier.is_empty() {
        return Ok(encoded_message);
    }

    // Find the next available slot for this message
    let slot_position = find_next_slot(carrier);

    // Insert the message at the appropriate position
    let result = insert_message_at_position(carrier, &encoded_message, slot_position);

    Ok(result)
}

/// Check if text contains an encoded message
///
/// # Arguments
/// * `text` - The text to check
///
/// # Returns
/// `true` if the text contains both start and end markers
pub fn has_encoded_message(text: &str) -> bool {
    text.contains(START_MARKER) && text.contains(END_MARKER)
}

/// Get the size of an encoded message in bytes
///
/// # Arguments
/// * `text` - The text containing the encoded message
///
/// # Returns
/// The size of the encoded message in bytes, or `None` if no message found
pub fn get_encoded_message_size(text: &str) -> Option<usize> {
    let start = text.find(START_MARKER)?;
    let end = text.find(END_MARKER)?;

    if end <= start {
        return None;
    }

    // Use char_indices to find the correct UTF-8 boundaries
    let mut start_char_pos = 0;
    let mut end_char_pos = 0;
    let mut found_start = false;
    let mut found_end = false;

    for (char_pos, (byte_pos, ch)) in text.char_indices().enumerate() {
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
        return None;
    }

    // Extract the encoded part using char positions
    let encoded: String = text
        .chars()
        .skip(start_char_pos + 1)
        .take(end_char_pos - start_char_pos - 1)
        .collect();
    Some(encoded.len() / 8) // Each byte is encoded as 8 zero-width characters
}
