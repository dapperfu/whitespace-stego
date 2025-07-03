use whitespace_stego_core::*;
use whitespace_stego_core::encode::*;
use whitespace_stego_core::StegoError;
use whitespace_stego_core::constants::*;

#[cfg(test)]
mod tests {
    use super::*;
    // ... (copy all tests from src/encode.rs #[cfg(test)] mod)
}

#[test]
fn test_encode_binary_edge_cases() {
    // Test empty data
    let empty_data = b"";
    let result = encode_binary(empty_data);
    assert_eq!(result, "");
    
    // Test single byte
    let single_byte = b"A";
    let result = encode_binary(single_byte);
    assert_eq!(result.len(), 8); // 1 byte = 8 zero-width characters
    
    // Test data with all zeros
    let all_zeros = vec![0u8; 10];
    let result = encode_binary(&all_zeros);
    assert_eq!(result.len(), 80); // 10 bytes = 80 zero-width characters
    assert!(result.chars().all(|c| c == ZERO_BIT));
    
    // Test data with all ones
    let all_ones = vec![255u8; 10];
    let result = encode_binary(&all_ones);
    assert_eq!(result.len(), 80);
    assert!(result.chars().all(|c| c == ONE_BIT));
    
    // Test mixed data
    let mixed_data = vec![0xAA, 0x55, 0xFF, 0x00];
    let result = encode_binary(&mixed_data);
    assert_eq!(result.len(), 32); // 4 bytes = 32 zero-width characters
}

#[test]
fn test_encode_binary_large_data() {
    // Test with large data to ensure performance
    let large_data = vec![0x42u8; 1000];
    let result = encode_binary(&large_data);
    assert_eq!(result.len(), 8000); // 1000 bytes = 8000 zero-width characters
    
    // Verify the pattern
    let expected = ZERO_BIT.to_string().repeat(4) + &ONE_BIT.to_string().repeat(4);
    let expected = expected.repeat(1000);
    assert_eq!(result, expected);
}

#[test]
fn test_encode_binary_unicode_bytes() {
    // Test with bytes that represent Unicode characters
    let unicode_bytes = "Hello, 世界! 🌍".as_bytes();
    let result = encode_binary(unicode_bytes);
    assert_eq!(result.len(), unicode_bytes.len() * 8);
    
    // Verify that the result contains only zero-width characters
    assert!(result.chars().all(|c| c == ZERO_BIT || c == ONE_BIT));
}

#[test]
fn test_has_encoded_message() {
    // Test empty carrier
    assert!(!has_encoded_message(""));
    
    // Test carrier with no encoded messages
    assert!(!has_encoded_message("Hello, World!"));
    
    // Test carrier with one encoded message
    let carrier_with_one = format!("Hello{}World{}", START_MARKER, END_MARKER);
    assert!(has_encoded_message(&carrier_with_one));
    
    // Test carrier with multiple encoded messages
    let carrier_with_multiple = format!(
        "Hello{}World{}Test{}Message{}",
        START_MARKER, END_MARKER, START_MARKER, END_MARKER
    );
    assert!(has_encoded_message(&carrier_with_multiple));
    
    // Test carrier with incomplete markers
    let carrier_incomplete = format!("Hello{}World", START_MARKER);
    assert!(!has_encoded_message(&carrier_incomplete));
}



#[test]
fn test_encode_edge_cases() {
    // Test empty message (should return error)
    let result = encode("", "carrier", None);
    assert!(result.is_err());
    assert!(matches!(result.unwrap_err(), StegoError::EncodingFailed { .. }));
    
    // Test empty carrier
    let result = encode("message", "", None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    assert!(encoded.starts_with(START_MARKER));
    assert!(encoded.ends_with(END_MARKER));
    
    // Test with password
    let result = encode("message", "carrier", Some("password"));
    assert!(result.is_ok());
    let encoded = result.unwrap();
    assert!(encoded.contains(START_MARKER));
    assert!(encoded.contains(END_MARKER));
}

#[test]
fn test_encode_with_unicode() {
    // Test with Unicode message
    let unicode_message = "Hello, 世界! 🌍";
    let result = encode(unicode_message, "carrier", None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    // Decode to verify
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, unicode_message);
    
    // Test with Unicode carrier
    let unicode_carrier = "你好，世界！";
    let result = encode("message", unicode_carrier, None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, "message");
}

#[test]
fn test_encode_multiple_messages() {
    let carrier = "Hello, World!";
    
    // Encode first message
    let encoded1 = encode("message1", &carrier, None).unwrap();
    
    // Encode second message
    let encoded2 = encode("message2", &encoded1, None).unwrap();
    
    // Verify both messages can be decoded
    let decoded1 = whitespace_stego_core::decode(&encoded2, None).unwrap();
    assert_eq!(decoded1, "message1");
    
    // Decode all messages
    let all_decoded = whitespace_stego_core::decode_all(&encoded2, None).unwrap();
    assert_eq!(all_decoded.len(), 2);
    assert_eq!(all_decoded[0], "message1");
    assert_eq!(all_decoded[1], "message2");
}



#[test]
fn test_get_encoded_message_size() {
    // Test text without encoded message
    assert!(get_encoded_message_size("Hello, World!").is_none());
    
    // Test text with incomplete markers
    assert!(get_encoded_message_size(&format!("Hello{}World", START_MARKER)).is_none());
    
    // Test text with markers in wrong order
    assert!(get_encoded_message_size(&format!("Hello{}World{}", END_MARKER, START_MARKER)).is_none());
    
    // Test text with valid encoded message
    let encoded = format!("Hello{}World{}", START_MARKER, END_MARKER);
    let size = get_encoded_message_size(&encoded);
    assert_eq!(size, Some(0)); // Empty message = 0 bytes
    
    // Test with actual encoded data
    let message = "test";
    let encoded = encode(message, "carrier", None).unwrap();
    let size = get_encoded_message_size(&encoded);
    assert!(size.is_some());
    assert!(size.unwrap() > 0);
}

#[test]
fn test_encode_with_special_characters() {
    // Test with special characters in message
    let special_message = "!@#$%^&*()_+-=[]{}|;':\",./<>?";
    let result = encode(special_message, "carrier", None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, special_message);
    
    // Test with special characters in carrier
    let special_carrier = "!@#$%^&*()_+-=[]{}|;':\",./<>?";
    let result = encode("message", special_carrier, None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, "message");
}

#[test]
fn test_encode_with_very_long_message() {
    // Test with very long message
    let long_message = "A".repeat(10000);
    let result = encode(&long_message, "carrier", None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, long_message);
}

#[test]
fn test_encode_with_very_long_carrier() {
    // Test with very long carrier
    let long_carrier = "A".repeat(10000);
    let result = encode("message", &long_carrier, None);
    assert!(result.is_ok());
    let encoded = result.unwrap();
    
    let decoded = whitespace_stego_core::decode(&encoded, None).unwrap();
    assert_eq!(decoded, "message");
}
