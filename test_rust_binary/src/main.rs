use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use whitespace_stego_core::{decode_binary, encode_binary};

fn main() {
    let message = "Hello, World";
    let data = BASE64.encode(message.as_bytes());
    println!("Base64 data: {}", data);

    let binary = encode_binary(&data.as_bytes());
    let first_50: String = binary.chars().take(50).collect();
    println!("Rust binary (first 50 chars): {:?}", first_50);

    // Test decode
    match decode_binary(&binary) {
        Ok(decoded) => {
            println!("Decoded bytes: {:?}", decoded);
            let decoded_str = String::from_utf8(decoded).unwrap();
            println!("Decoded string: {}", decoded_str);
        }
        Err(e) => println!("Decode error: {}", e),
    }
}
