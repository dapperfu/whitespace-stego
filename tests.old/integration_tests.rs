use whitespace_stego_core::{encode, decode, extract_encoded, StegoError};

/// Integration tests that test the complete workflow and cross-module functionality
#[cfg(test)]
mod integration_tests {
    use super::*;

    #[test]
    fn test_complete_workflow_with_all_combinations() {
        // Test all combinations of message lengths, carrier lengths, and password presence
        let test_cases = vec![
            // (message, carrier, password, description)
            ("", "", None, "empty everything"),
            ("", "", Some(""), "empty message and carrier, empty password"),
            ("", "", Some("pass"), "empty message and carrier, with password"),
            ("", "Hello", None, "empty message, short carrier, no password"),
            ("", "Hello", Some(""), "empty message, short carrier, empty password"),
            ("", "Hello", Some("pass"), "empty message, short carrier, with password"),
            ("", "This is a very long carrier text for testing", None, "empty message, long carrier, no password"),
            ("", "This is a very long carrier text for testing", Some("pass"), "empty message, long carrier, with password"),
            
            ("Hi", "", None, "short message, empty carrier, no password"),
            ("Hi", "", Some(""), "short message, empty carrier, empty password"),
            ("Hi", "", Some("pass"), "short message, empty carrier, with password"),
            ("Hi", "A", None, "short message, single char carrier, no password"),
            ("Hi", "A", Some("pass"), "short message, single char carrier, with password"),
            ("Hi", "Hello World", None, "short message, short carrier, no password"),
            ("Hi", "Hello World", Some("pass"), "short message, short carrier, with password"),
            ("Hi", "This is a very long carrier text for testing", None, "short message, long carrier, no password"),
            ("Hi", "This is a very long carrier text for testing", Some("pass"), "short message, long carrier, with password"),
            
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "", None, "long message, empty carrier, no password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "", Some("pass"), "long message, empty carrier, with password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "A", None, "long message, single char carrier, no password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "A", Some("pass"), "long message, single char carrier, with password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "Hello World", None, "long message, short carrier, no password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "Hello World", Some("pass"), "long message, short carrier, with password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "This is a very long carrier text for testing", None, "long message, long carrier, no password"),
            ("This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly", "This is a very long carrier text for testing", Some("pass"), "long message, long carrier, with password"),
        ];

        for (message, carrier, password, description) in test_cases {
            // Test encode -> decode round trip
            let encoded = encode(message, carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, message, "Round trip failed for: {}", description);

            // Test extract_encoded functionality
            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}')); // START_MARKER
            assert!(extracted.contains('\u{200C}')); // END_MARKER
            
            if !carrier.is_empty() {
                assert_eq!(remaining, carrier, "Carrier extraction failed for: {}", description);
            } else {
                assert_eq!(remaining, "", "Empty carrier extraction failed for: {}", description);
            }
        }
    }

    #[test]
    fn test_unicode_integration() {
        let unicode_test_cases = vec![
            ("Hello 世界", "Carrier with 世界", None),
            ("Emoji test 😀🎉🚀", "Emoji carrier 🎉", Some("pass")),
            ("Mixed: Hello 世界 😀 123 !@#", "Mixed carrier: Hello 世界 😀", Some("")),
            ("Zero-width chars: \u{200B}\u{200C}\u{200D}\u{FEFF}", "Test carrier", Some("unicode_pass")),
            ("Surrogate pairs: \u{1F600}", "Carrier with \u{1F600}", None),
            ("Combining chars: e\u{0301}", "Carrier with combining chars", Some("combining_pass")),
        ];

        for (message, carrier, password) in unicode_test_cases {
            let encoded = encode(message, carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, message, "Unicode round trip failed for message: '{}'", message);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            assert_eq!(remaining, carrier);
        }
    }

    #[test]
    fn test_binary_data_integration() {
        let binary_test_cases = vec![
            ("\x00\x01\x02\x03", "Normal carrier", None),
            ("\xFF\xFE\xFD\xFC", "Carrier with high bytes", Some("binary_pass")),
            ("Mixed\x00\x01text", "Mixed binary and text", Some("")),
            ("Text with \x00 null \x01 bytes", "Carrier text", Some("null_bytes_pass")),
        ];

        for (message, carrier, password) in binary_test_cases {
            let encoded = encode(message, carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, message, "Binary round trip failed for message: '{:?}'", message);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            assert_eq!(remaining, carrier);
        }
    }

    #[test]
    fn test_password_variations_integration() {
        let password_variations = vec![
            None,
            Some(""),
            Some("a"),
            Some("ab"),
            Some("abc"),
            Some("password"),
            Some("very_long_password_that_exceeds_normal_length"),
            Some("!@#$%^&*()"),
            Some("password with spaces"),
            Some("password\nwith\nnewlines"),
            Some("password\twith\ttabs"),
            Some("你好世界"),
        ];

        let test_message = "Test message for password variations";
        let test_carrier = "Test carrier";

        for password in password_variations {
            let encoded = encode(test_message, test_carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, test_message, "Password variation failed for: {:?}", password);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            assert_eq!(remaining, test_carrier);
        }
    }

    #[test]
    fn test_error_handling_integration() {
        // Test various error conditions
        assert!(matches!(
            decode("plain text without markers", None),
            Err(StegoError::InvalidCarrier(_))
        ));

        assert!(matches!(
            decode("", None),
            Err(StegoError::InvalidCarrier(_))
        ));

        // Test with only start marker
        let partial_encoded = format!("{}some data", '\u{200B}');
        assert!(matches!(
            decode(&partial_encoded, None),
            Err(StegoError::InvalidCarrier(_))
        ));

        // Test with only end marker
        let partial_encoded = format!("some data{}", '\u{200C}');
        assert!(matches!(
            decode(&partial_encoded, None),
            Err(StegoError::InvalidCarrier(_))
        ));

        // Test wrong password for encrypted data
        let encoded = encode("secret message", "carrier", Some("correct_password")).unwrap();
        assert!(matches!(
            decode(&encoded, Some("wrong_password")),
            Err(StegoError::DecryptionFailed(_))
        ));

        // Test no password when encrypted
        assert!(matches!(
            decode(&encoded, None),
            Err(StegoError::DecryptionFailed(_))
        ));
    }

    #[test]
    fn test_stress_integration() {
        // Test with very long messages and carriers
        let very_long_message = "A".repeat(1000);
        let very_long_carrier = "B".repeat(1000);
        
        for password in [None, Some(""), Some("stress_test_password")] {
            let encoded = encode(&very_long_message, &very_long_carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, very_long_message);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            assert_eq!(remaining, very_long_carrier);
        }
    }

    #[test]
    fn test_special_characters_integration() {
        let special_test_cases = vec![
            ("Message with newlines\nand\ttabs", "Carrier with\nnewlines", None),
            ("Message with quotes: \"Hello\" and 'World'", "Carrier with \"quotes\"", Some("quote_pass")),
            ("Message with backslashes: \\n\\t\\r", "Carrier with \\backslashes", Some("")),
            ("Message with control chars: \x01\x02\x03", "Carrier with control \x04\x05", Some("control_pass")),
            ("Message with unicode: αβγδε", "Carrier with unicode: αβγδε", None),
            ("Message with combining chars: e\u{0301}", "Carrier with combining: e\u{0301}", Some("combining_pass")),
        ];

        for (message, carrier, password) in special_test_cases {
            let encoded = encode(message, carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, message, "Special characters round trip failed for message: '{:?}'", message);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            assert_eq!(remaining, carrier);
        }
    }

    #[test]
    fn test_edge_case_integration() {
        // Test edge cases that might cause issues
        let edge_cases = vec![
            // Single character carriers
            ("Test message", "A", None),
            ("Test message", "😀", Some("emoji_carrier")),
            ("Test message", "你", Some("unicode_carrier")),
            ("Test message", "1", None),
            ("Test message", "!", Some("symbol_carrier")),
            ("Test message", " ", Some("space_carrier")),
            
            // Messages with zero-width characters (should be preserved)
            ("Message with \u{200B}\u{200C}\u{200D}\u{FEFF}", "Normal carrier", None),
            
            // Very short messages
            ("", "A", None),
            ("", "A", Some("")),
            ("", "A", Some("pass")),
            
            // Messages that are exactly one character
            ("A", "", None),
            ("A", "", Some("pass")),
            ("😀", "Carrier", None),
            ("你", "Carrier", Some("pass")),
        ];

        for (message, carrier, password) in edge_cases {
            let encoded = encode(message, carrier, password).unwrap();
            let decoded = decode(&encoded, password).unwrap();
            assert_eq!(decoded, message, "Edge case failed for message: '{:?}', carrier: '{:?}', password: {:?}", message, carrier, password);

            let (extracted, remaining) = extract_encoded(&encoded).unwrap();
            assert!(extracted.contains('\u{200B}'));
            assert!(extracted.contains('\u{200C}'));
            
            if !carrier.is_empty() {
                assert_eq!(remaining, carrier);
            } else {
                assert_eq!(remaining, "");
            }
        }
    }
} 