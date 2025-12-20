use whitespace_stego::{decode, encode, StegoError};

#[test]
fn test_encode_empty_message() {
    let result = encode("", None).unwrap();
    assert!(result.contains('\u{2060}')); // CONTROL_START
    assert!(result.contains('\u{2063}')); // CONTROL_END
}

#[test]
fn test_encode_simple_message() {
    let message = "Hello, World!";
    let result = encode(message, None).unwrap();
    assert!(!result.is_empty());
}

#[test]
fn test_round_trip() {
    let message = "Hello, World!";
    let encoded = encode(message, None).unwrap();
    let decoded = decode(&encoded).unwrap();
    assert_eq!(decoded, message);
}

#[test]
fn test_round_trip_unicode() {
    let message = "Hello 🌍 你好";
    let encoded = encode(message, None).unwrap();
    let decoded = decode(&encoded).unwrap();
    assert_eq!(decoded, message);
}

#[test]
fn test_encode_with_carrier() {
    let message = "Secret";
    let carrier = Some("This is normal text.");
    let result = encode(message, carrier).unwrap();
    assert!(result.contains("T")); // First char of carrier
}

#[test]
fn test_decode_missing_marker() {
    let result = decode("Some text\u{2063}");
    assert!(matches!(result, Err(StegoError::MissingMarker(_))));
}

