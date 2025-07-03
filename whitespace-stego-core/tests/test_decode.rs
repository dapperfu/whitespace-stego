use whitespace_stego_core::*;
use whitespace_stego_core::decode::*;
use whitespace_stego_core::StegoError;
use whitespace_stego_core::constants::*;

#[cfg(test)]
mod tests {
    use super::*;
    // ... (copy all tests from src/decode.rs #[cfg(test)] mod)
}

#[test]
fn test_decode_binary_edge_cases() {
    // Test empty input
    let empty_input = "";
    let result = decode_binary(empty_input);
    assert!(result.is_ok());
    assert_eq!(result.unwrap(), b"");
    
    // Test input with only zero bits
    let zero_bits = ZERO_BIT.to_string().repeat(8);
    let result = decode_binary(&zero_bits);
    assert!(result.is_ok());
    assert_eq!(result.unwrap(), b"\x00");
    
    // Test input with only one bits
    let one_bits = ONE_BIT.to_string().repeat(8);
    let result = decode_binary(&one_bits);
    assert!(result.is_ok());
    assert_eq!(result.unwrap(), b"\xFF");
    
    // Test input with mixed bits
    let mixed_bits = format!("{}{}", ZERO_BIT.to_string().repeat(4), ONE_BIT.to_string().repeat(4));
    let result = decode_binary(&mixed_bits);
    assert!(result.is_ok());
    assert_eq!(result.unwrap(), b"\x0F");
    
    // Test input with invalid length (not multiple of 8)
    let invalid_length = ZERO_BIT.to_string().repeat(7);
    let result = decode_binary(&invalid_length);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidBinaryData { .. }));
    
    // Test input with invalid characters
    let invalid_chars = "Hello, World!";
    let result = decode_binary(invalid_chars);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidBinaryData { .. }));
}

#[test]
fn test_decode_binary_large_data() {
    // Test with large encoded data
    let large_encoded = ZERO_BIT.to_string().repeat(8000); // 1000 bytes
    let result = decode_binary(&large_encoded);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded.len(), 1000);
    assert!(decoded.iter().all(|&b| b == 0));
    
    // Test with alternating pattern
    let alternating = (ZERO_BIT.to_string() + &ONE_BIT.to_string()).repeat(4000); // 1000 bytes
    let result = decode_binary(&alternating);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded.len(), 1000);
    assert_eq!(decoded[0], 0x0F);
}

#[test]
fn test_decode_binary_unicode_handling() {
    // Test that decode_binary handles Unicode characters correctly
    let unicode_encoded = format!("{}{}", ZERO_BIT.to_string().repeat(4), ONE_BIT.to_string().repeat(4));
    let result = decode_binary(&unicode_encoded);
    assert!(result.is_ok());
    assert_eq!(result.unwrap(), b"\x0F");
}

#[test]
fn test_extract_encoded_edge_cases() {
    // Test text without encoded message
    let result = extract_encoded("Hello, World!");
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test empty text
    let result = extract_encoded("");
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with only start marker
    let result = extract_encoded(&format!("Hello{}World", START_MARKER));
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with only end marker
    let result = extract_encoded(&format!("Hello{}World", END_MARKER));
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with markers in wrong order
    let result = extract_encoded(&format!("Hello{}World{}", END_MARKER, START_MARKER));
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
}

#[test]
fn test_extract_encoded_with_multiple_messages() {
    // Test extraction with multiple encoded messages
    let encoded1 = format!("{}{}{}", START_MARKER, "message1", END_MARKER);
    let encoded2 = format!("{}{}{}", START_MARKER, "message2", END_MARKER);
    let carrier = format!("Hello{}World{}Test", encoded1, encoded2);
    
    let result = extract_encoded(&carrier);
    assert!(result.is_ok());
    let (extracted, remaining) = result.unwrap();
    
    // Should extract the first message
    assert!(extracted.contains(&encoded1));
    assert!(!extracted.contains(&encoded2));
    
    // Remaining should contain the second message
    assert!(remaining.contains(&encoded2));
}

#[test]
fn test_get_encoded_message_position_edge_cases() {
    // Test text without encoded message
    assert!(get_encoded_message_position("Hello, World!").is_none());
    
    // Test empty text
    assert!(get_encoded_message_position("").is_none());
    
    // Test text with only start marker
    assert!(get_encoded_message_position(&format!("Hello{}World", START_MARKER)).is_none());
    
    // Test text with only end marker
    assert!(get_encoded_message_position(&format!("Hello{}World", END_MARKER)).is_none());
    
    // Test text with markers in wrong order
    assert!(get_encoded_message_position(&format!("Hello{}World{}", END_MARKER, START_MARKER)).is_none());
}

#[test]
fn test_get_encoded_message_position_with_multiple_messages() {
    // Test with multiple encoded messages
    let encoded1 = format!("{}{}{}", START_MARKER, "message1", END_MARKER);
    let encoded2 = format!("{}{}{}", START_MARKER, "message2", END_MARKER);
    let carrier = format!("Hello{}World{}Test", encoded1, encoded2);
    
    let position = get_encoded_message_position(&carrier);
    assert!(position.is_some());
    let (start, end) = position.unwrap();
    
    // Should return position of first message
    assert!(start < end);
    assert!(start < carrier.len());
    assert!(end <= carrier.len());
}

#[test]
fn test_decode_edge_cases() {
    // Test empty text
    let result = decode("", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text without encoded message
    let result = decode("Hello, World!", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with only start marker
    let result = decode(&format!("Hello{}World", START_MARKER), None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with only end marker
    let result = decode(&format!("Hello{}World", END_MARKER), None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with markers in wrong order
    let result = decode(&format!("Hello{}World{}", END_MARKER, START_MARKER), None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
}

#[test]
fn test_decode_with_corrupted_data() {
    // Test with corrupted encoded data
    let encoded = format!("{}{}{}", START_MARKER, "corrupted", END_MARKER);
    let result = decode(&encoded, None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidBinaryData { .. }));
    
    // Test with invalid base64
    let invalid_base64 = format!("{}{}{}", START_MARKER, "!@#$%^&*()", END_MARKER);
    let result = decode(&invalid_base64, None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::Base64Error { .. }));
}

#[test]
fn test_decode_with_wrong_password() {
    // Test encrypted message with wrong password
    let message = "secret message";
    let password = "correct_password";
    let wrong_password = "wrong_password";
    
    let encoded = whitespace_stego_core::encode(message, "carrier", Some(password)).unwrap();
    let result = decode(&encoded, Some(wrong_password));
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::DecryptionFailed { .. }));
}

#[test]
fn test_decode_all_edge_cases() {
    // Test empty text
    let result = decode_all("", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text without encoded messages
    let result = decode_all("Hello, World!", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::InvalidCarrier { .. }));
    
    // Test text with single encoded message
    let encoded = whitespace_stego_core::encode("message", "carrier", None).unwrap();
    let result = decode_all(&encoded, None);
    assert!(result.is_ok());
    let messages = result.unwrap();
    assert_eq!(messages.len(), 1);
    assert_eq!(messages[0], "message");
}

#[test]
fn test_decode_all_with_multiple_messages() {
    // Test with multiple encoded messages
    let carrier = "Hello, World!";
    let encoded1 = whitespace_stego_core::encode("message1", &carrier, None).unwrap();
    let encoded2 = whitespace_stego_core::encode("message2", &encoded1, None).unwrap();
    
    let result = decode_all(&encoded2, None);
    assert!(result.is_ok());
    let messages = result.unwrap();
    assert_eq!(messages.len(), 2);
    assert_eq!(messages[0], "message1");
    assert_eq!(messages[1], "message2");
}

#[test]
fn test_count_messages_edge_cases() {
    // Test empty text
    assert_eq!(count_messages(""), 0);
    
    // Test text without encoded messages
    assert_eq!(count_messages("Hello, World!"), 0);
    
    // Test text with only start marker
    assert_eq!(count_messages(&format!("Hello{}World", START_MARKER)), 0);
    
    // Test text with only end marker
    assert_eq!(count_messages(&format!("Hello{}World", END_MARKER)), 0);
    
    // Test text with markers in wrong order
    assert_eq!(count_messages(&format!("Hello{}World{}", END_MARKER, START_MARKER)), 0);
}

#[test]
fn test_count_messages_with_multiple_messages() {
    // Test with single encoded message
    let encoded = format!("{}{}{}", START_MARKER, "message", END_MARKER);
    assert_eq!(count_messages(&encoded), 1);
    
    // Test with multiple encoded messages
    let encoded1 = format!("{}{}{}", START_MARKER, "message1", END_MARKER);
    let encoded2 = format!("{}{}{}", START_MARKER, "message2", END_MARKER);
    let carrier = format!("Hello{}World{}Test", encoded1, encoded2);
    assert_eq!(count_messages(&carrier), 2);
}

#[test]
fn test_decode_with_unicode() {
    // Test with Unicode message
    let unicode_message = "Hello, 世界! 🌍";
    let encoded = whitespace_stego_core::encode(unicode_message, "carrier", None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, unicode_message);
    
    // Test with Unicode carrier
    let unicode_carrier = "你好，世界！";
    let encoded = whitespace_stego_core::encode("message", unicode_carrier, None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, "message");
}

#[test]
fn test_decode_with_special_characters() {
    // Test with special characters in message
    let special_message = "!@#$%^&*()_+-=[]{}|;':\",./<>?";
    let encoded = whitespace_stego_core::encode(special_message, "carrier", None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, special_message);
    
    // Test with special characters in carrier
    let special_carrier = "!@#$%^&*()_+-=[]{}|;':\",./<>?";
    let encoded = whitespace_stego_core::encode("message", special_carrier, None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, "message");
}

#[test]
fn test_decode_with_very_long_message() {
    // Test with very long message
    let long_message = "A".repeat(10000);
    let encoded = whitespace_stego_core::encode(&long_message, "carrier", None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, long_message);
}

#[test]
fn test_decode_with_very_long_carrier() {
    // Test with very long carrier
    let long_carrier = "A".repeat(10000);
    let encoded = whitespace_stego_core::encode("message", &long_carrier, None).unwrap();
    let result = decode(&encoded, None);
    assert!(result.is_ok());
    let decoded = result.unwrap();
    assert_eq!(decoded, "message");
}
