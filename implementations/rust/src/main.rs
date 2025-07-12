use clap::{Arg, Command};
use env_logger;
use log::LevelFilter;
use std::error::Error;
use std::fs;
use whitespace_stego_core::{decode as core_decode, encode as core_encode};

fn main() -> Result<(), Box<dyn Error>> {
    env_logger::builder().filter_level(LevelFilter::Info).init();
    let matches = Command::new("whitespace-stego-rs")
        .version("1.0")
        .author("Your Name")
        .about("Whitespace steganography tool")
        .subcommand(
            Command::new("encode")
                .about("Encode a message into a carrier")
                .arg(
                    Arg::new("message")
                        .short('m')
                        .long("message")
                        .num_args(1)
                        .help("Message to encode"),
                )
                .arg(
                    Arg::new("message_file")
                        .long("mf")
                        .num_args(1)
                        .help("File containing the message to encode"),
                )
                .arg(
                    Arg::new("carrier")
                        .short('c')
                        .long("carrier")
                        .num_args(1)
                        .help("Carrier text"),
                )
                .arg(
                    Arg::new("carrier_file")
                        .long("cf")
                        .num_args(1)
                        .help("File containing the carrier text"),
                )
                .arg(
                    Arg::new("password")
                        .short('p')
                        .long("password")
                        .num_args(1)
                        .help("Password for encryption"),
                )
                .arg(
                    Arg::new("output")
                        .short('o')
                        .long("output")
                        .num_args(1)
                        .help("Output file (default: stdout)"),
                ),
        )
        .subcommand(
            Command::new("decode")
                .about("Decode a message from a carrier")
                .arg(
                    Arg::new("carrier")
                        .short('c')
                        .long("carrier")
                        .num_args(1)
                        .help("Carrier text"),
                )
                .arg(
                    Arg::new("carrier_file")
                        .long("cf")
                        .num_args(1)
                        .help("File containing the carrier text"),
                )
                .arg(
                    Arg::new("password")
                        .short('p')
                        .long("password")
                        .num_args(1)
                        .help("Password for decryption"),
                )
                .arg(
                    Arg::new("output")
                        .short('o')
                        .long("output")
                        .num_args(1)
                        .help("Output file (default: stdout)"),
                ),
        )
        .get_matches();

    match matches.subcommand() {
        Some(("encode", sub_m)) => {
            let message = if let Some(mf) = sub_m.get_one::<String>("message_file") {
                fs::read_to_string(mf)?
            } else if let Some(m) = sub_m.get_one::<String>("message") {
                m.to_string()
            } else {
                return Err("No message provided".into());
            };
            let carrier = if let Some(cf) = sub_m.get_one::<String>("carrier_file") {
                fs::read_to_string(cf)?
            } else if let Some(c) = sub_m.get_one::<String>("carrier") {
                c.to_string()
            } else {
                String::new()
            };
            let password = sub_m.get_one::<String>("password").map(|s| s.as_str());
            let output = sub_m.get_one::<String>("output").map(|s| s.as_str());
            let encoded = core_encode(&message, &carrier, password)
                .map_err(|e| format!("Encoding failed: {}", e))?;
            if let Some(out) = output {
                fs::write(out, &encoded)?;
            } else {
                println!("{}", encoded);
            }
        },
        Some(("decode", sub_m)) => {
            let carrier = if let Some(cf) = sub_m.get_one::<String>("carrier_file") {
                fs::read_to_string(cf)?
            } else if let Some(c) = sub_m.get_one::<String>("carrier") {
                c.to_string()
            } else {
                return Err("No carrier provided".into());
            };
            let password = sub_m.get_one::<String>("password").map(|s| s.as_str());
            let output = sub_m.get_one::<String>("output").map(|s| s.as_str());
            let decoded =
                core_decode(&carrier, password).map_err(|e| format!("Decoding failed: {}", e))?;
            if let Some(out) = output {
                fs::write(out, &decoded)?;
            } else {
                println!("{}", decoded);
            }
        },
        _ => {
            return Err("No subcommand provided. Use encode or decode.".into());
        },
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    // Test data for comprehensive permutation testing
    const MESSAGES: &[&str] = &[
        "Hello, World!",
        "Test message with emoji 😀",
        "Multilingual text: 你好, 世界!",
        "Special chars: !@#$%^&*()",
        "A", // Single character message
        "Very long message that contains many characters and should test the encoding and decoding capabilities thoroughly. It includes various types of content like numbers 123, symbols !@#, emojis 😀🎉, and unicode characters 你好世界.",
        "", // Empty message (should fail)
    ];

    const PASSWORDS: &[Option<&str>] = &[
        None,
        Some("simple_password"),
        Some("complex_password_123!@#"),
        Some(""), // Empty password
        Some("unicode_password_你好世界"),
        Some("emoji_password_😀🎉"),
        Some("very_long_password_that_should_be_hashed_properly_and_tested_for_edge_cases_in_the_encoding_process"),
    ];

    const CARRIERS: &[&str] = &[
        "", // Empty carrier
        "Simple carrier text",
        "Carrier with emoji 🎉",
        "Multilingual carrier: 你好世界",
        "A", // Single character carrier
        "Very long carrier text that will be used to test the embedding of encoded messages. It contains various characters and should be long enough to test different insertion points and edge cases in the encoding process.",
        "Carrier with special chars: !@#$%^&*()",
        "Carrier with unicode: 你好世界 😀🎉",
    ];

    #[test]
    fn test_encode_decode_roundtrip() {
        for &message in MESSAGES {
            for &password in PASSWORDS {
                for &carrier in CARRIERS {
                    let result = core_encode(message, carrier, password);
                    if message.is_empty() {
                        assert!(result.is_err(), "Empty message should return error");
                    } else {
                        let encoded = result.unwrap();
                        let decoded = core_decode(&encoded, password);
                        assert!(decoded.is_ok(), "Decoding should succeed");
                        assert_eq!(decoded.unwrap(), message);
                    }
                }
            }
        }
    }

    #[test]
    fn test_encode_decode_no_password() {
        let message = "Hello, World!";
        let carrier = "This is a test";
        let encoded = core_encode(message, carrier, None).unwrap();
        let decoded = core_decode(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_with_password() {
        let message = "Secret message";
        let carrier = "This is a test";
        let password = "test_password";
        let encoded = core_encode(message, carrier, Some(password)).unwrap();
        let decoded = core_decode(&encoded, Some(password)).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_empty_carrier() {
        for &message in MESSAGES {
            if message.is_empty() {
                continue; // Skip empty messages
            }
            let encoded = core_encode(message, "", None).unwrap();
            let decoded = core_decode(&encoded, None).unwrap();
            assert_eq!(decoded, message);
        }
    }

    #[test]
    fn test_encode_decode_single_char_carrier() {
        for &message in MESSAGES {
            if message.is_empty() {
                continue; // Skip empty messages
            }
            let encoded = core_encode(message, "A", None).unwrap();
            let decoded = core_decode(&encoded, None).unwrap();
            assert_eq!(decoded, message);
        }
    }

    #[test]
    fn test_decode_invalid_carrier() {
        let result = core_decode("Invalid carrier", None);
        assert!(result.is_err());
    }

    #[test]
    fn test_decode_wrong_password() {
        for &message in MESSAGES {
            if message.is_empty() {
                continue; // Skip empty messages
            }
            let password = "correct_password";
            let wrong_password = "wrong_password";
            let encoded = core_encode(message, "Test carrier", Some(password)).unwrap();
            let result = core_decode(&encoded, Some(wrong_password));
            assert!(result.is_err());
        }
    }

    #[test]
    fn test_unicode_edge_cases() {
        let unicode_messages = &[
            "Hello 你好世界",
            "Emoji test 😀🎉🌟",
            "Mixed content: Hello 你好 😀 World 世界",
            "Special unicode: 🚀🌍🎯💻🔐",
        ];

        let unicode_carriers = &[
            "Unicode carrier: 你好世界",
            "Carrier with emojis 🎉🌟",
            "Mixed carrier: Hello 你好 😀 World 世界",
        ];

        for &message in unicode_messages {
            for &carrier in unicode_carriers {
                for &password in PASSWORDS {
                    let result = core_encode(message, carrier, password);
                    assert!(result.is_ok(), "Unicode encoding should succeed");
                    let encoded = result.unwrap();
                    let decoded = core_decode(&encoded, password);
                    assert!(decoded.is_ok(), "Unicode decoding should succeed");
                    assert_eq!(decoded.unwrap(), message);
                }
            }
        }
    }

    #[test]
    fn test_password_variations() {
        let test_message = "Test message";
        let test_carrier = "Test carrier";

        for &password in PASSWORDS {
            let result = core_encode(test_message, test_carrier, password);
            assert!(result.is_ok(), "Encoding with password should succeed");
            let encoded = result.unwrap();
            let decoded = core_decode(&encoded, password);
            assert!(decoded.is_ok(), "Decoding with password should succeed");
            assert_eq!(decoded.unwrap(), test_message);
        }
    }

    #[test]
    fn test_empty_message_rejected() {
        for &carrier in CARRIERS {
            for &password in PASSWORDS {
                let result = core_encode("", carrier, password);
                assert!(result.is_err(), "Empty message should be rejected");
            }
        }
    }

    #[test]
    fn test_long_message_edge_cases() {
        let long_message = "This is a very long message that contains many characters and should test the encoding and decoding capabilities thoroughly. It includes various types of content like numbers 123, symbols !@#, emojis 😀🎉, and unicode characters 你好世界. This message is designed to be long enough to test edge cases in the binary encoding and decoding process.";
        
        for &carrier in CARRIERS {
            for &password in PASSWORDS {
                let result = core_encode(long_message, carrier, password);
                assert!(result.is_ok(), "Long message encoding should succeed");
                let encoded = result.unwrap();
                let decoded = core_decode(&encoded, password);
                assert!(decoded.is_ok(), "Long message decoding should succeed");
                assert_eq!(decoded.unwrap(), long_message);
            }
        }
    }

    #[test]
    fn test_special_character_edge_cases() {
        let special_messages = &[
            "Message with special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?",
            "Message with tabs\tand\nnewlines",
            "Message with null bytes: \x00\x01\x02",
            "Message with unicode control chars: \u{0000}\u{0001}\u{0002}",
        ];

        for &message in special_messages {
            for &carrier in CARRIERS {
                for &password in PASSWORDS {
                    let result = core_encode(message, carrier, password);
                    assert!(result.is_ok(), "Special character encoding should succeed");
                    let encoded = result.unwrap();
                    let decoded = core_decode(&encoded, password);
                    assert!(decoded.is_ok(), "Special character decoding should succeed");
                    assert_eq!(decoded.unwrap(), message);
                }
            }
        }
    }

    #[test]
    fn test_multiple_encodings_same_carrier() {
        let carrier = "This is a test carrier";
        let messages = &["First message", "Second message", "Third message"];
        
        let mut encoded_carrier = carrier.to_string();
        
        for &message in messages {
            let result = core_encode(message, &encoded_carrier, None);
            assert!(result.is_ok(), "Multiple encoding should succeed");
            encoded_carrier = result.unwrap();
        }
        
        // Decode all messages
        let decoded_messages = core_decode(&encoded_carrier, None);
        assert!(decoded_messages.is_ok());
        let decoded = decoded_messages.unwrap();
        
        // The decoded result should contain all messages (joined with newlines)
        for &message in messages {
            assert!(decoded.contains(message), "Decoded should contain: {}", message);
        }
    }

    #[test]
    fn test_error_conditions() {
        // Test decoding invalid carriers
        let invalid_carriers = &[
            "No markers here",
            "Only start marker \u{FEFF}",
            "Only end marker \u{200C}",
            "Wrong order \u{200C}end\u{FEFF}start",
            "Incomplete markers \u{FEFF}incomplete",
        ];

        for &carrier in invalid_carriers {
            let result = core_decode(carrier, None);
            assert!(result.is_err(), "Invalid carrier should fail: {}", carrier);
        }
    }
}
