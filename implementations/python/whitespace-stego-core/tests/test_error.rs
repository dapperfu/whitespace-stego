use whitespace_stego_core::StegoError;
use std::error::Error;

#[cfg(test)]
mod tests {
    use super::*;
    // ... (copy all tests from src/error.rs #[cfg(test)] mod)
}

#[test]
fn test_error_display_implementations() {
    // Test EncodingFailed
    let encoding_error = StegoError::EncodingFailed {
        message: "Test encoding failed".to_string(),
    };
    let display = format!("{}", encoding_error);
    assert!(display.contains("Test encoding failed"));
    
    // Test DecryptionFailed
    let decryption_error = StegoError::DecryptionFailed {
        message: "Test decryption failed".to_string(),
    };
    let display = format!("{}", decryption_error);
    assert!(display.contains("Test decryption failed"));
    
    // Test InvalidCarrier
    let invalid_carrier_error = StegoError::InvalidCarrier {
        message: "Test invalid carrier".to_string(),
    };
    let display = format!("{}", invalid_carrier_error);
    assert!(display.contains("Test invalid carrier"));
    
    // Test Base64Error
    let base64_error = StegoError::Base64Error {
        message: "Test base64 error".to_string(),
    };
    let display = format!("{}", base64_error);
    assert!(display.contains("Test base64 error"));
    
    // Test Utf8Error
    let utf8_error = StegoError::Utf8Error {
        message: "Test utf8 error".to_string(),
    };
    let display = format!("{}", utf8_error);
    assert!(display.contains("Test utf8 error"));
    
    // Test InvalidKey
    let invalid_key_error = StegoError::InvalidKey {
        message: "Test invalid key".to_string(),
    };
    let display = format!("{}", invalid_key_error);
    assert!(display.contains("Test invalid key"));
    
    // Test NoMessageFound
    let no_message_error = StegoError::NoMessageFound;
    let display = format!("{}", no_message_error);
    assert!(display.contains("No encoded message found"));
    
    // Test InvalidBinaryData
    let invalid_binary_error = StegoError::InvalidBinaryData {
        message: "Test invalid binary data".to_string(),
    };
    let display = format!("{}", invalid_binary_error);
    assert!(display.contains("Test invalid binary data"));
}

#[test]
fn test_error_debug_implementations() {
    // Test Debug trait for all error variants
    let errors = vec![
        StegoError::EncodingFailed {
            message: "Debug test".to_string(),
        },
        StegoError::DecryptionFailed {
            message: "Debug test".to_string(),
        },
        StegoError::InvalidCarrier {
            message: "Debug test".to_string(),
        },
        StegoError::Base64Error {
            message: "Debug test".to_string(),
        },
        StegoError::Utf8Error {
            message: "Debug test".to_string(),
        },
        StegoError::InvalidKey {
            message: "Debug test".to_string(),
        },
        StegoError::NoMessageFound,
        StegoError::InvalidBinaryData {
            message: "Debug test".to_string(),
        },
    ];
    
    for error in errors {
        let debug = format!("{:?}", error);
        assert!(debug.contains("Debug test") || debug.contains("NoMessageFound"));
    }
}

#[test]
fn test_error_source_implementations() {
    // Test that all error variants implement Error trait correctly
    let errors = vec![
        StegoError::EncodingFailed {
            message: "Source test".to_string(),
        },
        StegoError::DecryptionFailed {
            message: "Source test".to_string(),
        },
        StegoError::InvalidCarrier {
            message: "Source test".to_string(),
        },
        StegoError::Base64Error {
            message: "Source test".to_string(),
        },
        StegoError::Utf8Error {
            message: "Source test".to_string(),
        },
        StegoError::InvalidKey {
            message: "Source test".to_string(),
        },
        StegoError::NoMessageFound,
        StegoError::InvalidBinaryData {
            message: "Source test".to_string(),
        },
    ];
    
    for error in errors {
        // Test that source() returns None (as expected for our error types)
        assert!(error.source().is_none());
        
        // Test that the error can be used as a trait object
        let error_ref: &dyn Error = &error;
        assert!(error_ref.source().is_none());
    }
}

#[test]
fn test_error_from_conversions() {
    // Test conversion from base64::DecodeError
    let base64_error = base64::DecodeError::InvalidLength;
    let stego_error: StegoError = base64_error.into();
    
    match stego_error {
        StegoError::Base64Error { message } => {
            assert!(!message.is_empty());
        }
        _ => panic!("Expected Base64Error"),
    }
}

#[test]
fn test_error_message_extraction() {
    // Test that we can extract messages from all error variants
    let test_message = "Test error message";
    
    let encoding_error = StegoError::EncodingFailed {
        message: test_message.to_string(),
    };
    let display = format!("{}", encoding_error);
    assert!(display.contains(test_message));
    
    let decryption_error = StegoError::DecryptionFailed {
        message: test_message.to_string(),
    };
    let display = format!("{}", decryption_error);
    assert!(display.contains(test_message));
    
    let invalid_carrier_error = StegoError::InvalidCarrier {
        message: test_message.to_string(),
    };
    let display = format!("{}", invalid_carrier_error);
    assert!(display.contains(test_message));
    
    let base64_error = StegoError::Base64Error {
        message: test_message.to_string(),
    };
    let display = format!("{}", base64_error);
    assert!(display.contains(test_message));
    
    let utf8_error = StegoError::Utf8Error {
        message: test_message.to_string(),
    };
    let display = format!("{}", utf8_error);
    assert!(display.contains(test_message));
    
    let invalid_key_error = StegoError::InvalidKey {
        message: test_message.to_string(),
    };
    let display = format!("{}", invalid_key_error);
    assert!(display.contains(test_message));
    
    let invalid_binary_error = StegoError::InvalidBinaryData {
        message: test_message.to_string(),
    };
    let display = format!("{}", invalid_binary_error);
    assert!(display.contains(test_message));
}

#[test]
fn test_error_with_empty_messages() {
    // Test error variants with empty messages
    let empty_message = "";
    
    let encoding_error = StegoError::EncodingFailed {
        message: empty_message.to_string(),
    };
    let display = format!("{}", encoding_error);
    assert!(!display.is_empty()); // Should still have some display text
    
    let decryption_error = StegoError::DecryptionFailed {
        message: empty_message.to_string(),
    };
    let display = format!("{}", decryption_error);
    assert!(!display.is_empty());
    
    let invalid_carrier_error = StegoError::InvalidCarrier {
        message: empty_message.to_string(),
    };
    let display = format!("{}", invalid_carrier_error);
    assert!(!display.is_empty());
    
    let base64_error = StegoError::Base64Error {
        message: empty_message.to_string(),
    };
    let display = format!("{}", base64_error);
    assert!(!display.is_empty());
    
    let utf8_error = StegoError::Utf8Error {
        message: empty_message.to_string(),
    };
    let display = format!("{}", utf8_error);
    assert!(!display.is_empty());
    
    let invalid_key_error = StegoError::InvalidKey {
        message: empty_message.to_string(),
    };
    let display = format!("{}", invalid_key_error);
    assert!(!display.is_empty());
    
    let invalid_binary_error = StegoError::InvalidBinaryData {
        message: empty_message.to_string(),
    };
    let display = format!("{}", invalid_binary_error);
    assert!(!display.is_empty());
}

#[test]
fn test_error_with_unicode_messages() {
    // Test error variants with Unicode messages
    let unicode_message = "你好世界 😀🎉🌟";
    
    let encoding_error = StegoError::EncodingFailed {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", encoding_error);
    assert!(display.contains(unicode_message));
    
    let decryption_error = StegoError::DecryptionFailed {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", decryption_error);
    assert!(display.contains(unicode_message));
    
    let invalid_carrier_error = StegoError::InvalidCarrier {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", invalid_carrier_error);
    assert!(display.contains(unicode_message));
    
    let base64_error = StegoError::Base64Error {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", base64_error);
    assert!(display.contains(unicode_message));
    
    let utf8_error = StegoError::Utf8Error {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", utf8_error);
    assert!(display.contains(unicode_message));
    
    let invalid_key_error = StegoError::InvalidKey {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", invalid_key_error);
    assert!(display.contains(unicode_message));
    
    let invalid_binary_error = StegoError::InvalidBinaryData {
        message: unicode_message.to_string(),
    };
    let display = format!("{}", invalid_binary_error);
    assert!(display.contains(unicode_message));
}

#[test]
fn test_error_creation_methods() {
    // Test the convenience methods for creating errors
    let encoding_error = StegoError::encoding_failed("Test encoding failed");
    assert!(matches!(encoding_error, StegoError::EncodingFailed { .. }));
    
    let decryption_error = StegoError::decryption_failed("Test decryption failed");
    assert!(matches!(decryption_error, StegoError::DecryptionFailed { .. }));
    
    let invalid_carrier_error = StegoError::invalid_carrier("Test invalid carrier");
    assert!(matches!(invalid_carrier_error, StegoError::InvalidCarrier { .. }));
    
    let base64_error = StegoError::base64_error("Test base64 error");
    assert!(matches!(base64_error, StegoError::Base64Error { .. }));
    
    let utf8_error = StegoError::utf8_error("Test utf8 error");
    assert!(matches!(utf8_error, StegoError::Utf8Error { .. }));
    
    let invalid_key_error = StegoError::invalid_key("Test invalid key");
    assert!(matches!(invalid_key_error, StegoError::InvalidKey { .. }));
    
    let invalid_binary_error = StegoError::invalid_binary_data("Test invalid binary data");
    assert!(matches!(invalid_binary_error, StegoError::InvalidBinaryData { .. }));
}
