use clap::{App, Arg};
use std::error::Error;
use log::{debug, error, info, LevelFilter};
use env_logger::Builder;
use base64;
use fernet::{Fernet, DecryptionError};
use sha2::{Sha256, Digest};

const START_MARKER: &str = "\u{200b}"; // Zero-width space
const END_MARKER: &str = "\u{200c}"; // Zero-width non-joiner
const ZERO_BIT: &str = "\u{200d}"; // Zero-width joiner
const ONE_BIT: &str = "\u{feff}"; // Zero-width no-break space

fn encode_binary(data: &[u8]) -> String {
    let binary: String = data.iter()
        .map(|byte| format!("{:08b}", byte))
        .collect();
    binary.chars()
        .map(|bit| if bit == '1' { ONE_BIT } else { ZERO_BIT })
        .collect()
}

fn decode_binary(encoded: &str) -> Vec<u8> {
    let binary: String = encoded.chars()
        .map(|char| if char == ONE_BIT.chars().next().unwrap() { '1' } else { '0' })
        .collect();
    (0..binary.len() / 8)
        .map(|i| u8::from_str_radix(&binary[i * 8..(i + 1) * 8], 2).unwrap())
        .collect()
}

fn derive_fernet_key(password: &str) -> String {
    let mut key_bytes = password.as_bytes().to_vec();
    key_bytes.resize(32, 0);
    base64::encode_config(&key_bytes, base64::STANDARD_NO_PAD)
}

fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, Box<dyn Error>> {
    info!("Encoding message: {}", message);
    info!("Using carrier: {}", carrier);
    if let Some(pwd) = password {
        info!("Using password: {}", pwd);
    }

    // Base64 encode the message
    let mut encoded = base64::encode(message.as_bytes()).into_bytes();

    // Fernet encrypt if password is provided
    if let Some(pwd) = password {
        let key = derive_fernet_key(pwd);
        let fernet = Fernet::new(&key).ok_or("Invalid Fernet key")?;
        let encrypted = fernet.encrypt(&encoded);
        encoded = encrypted.into_bytes();
    }

    let zero_width = encode_binary(&encoded);
    let encoded_message = format!("{}{}{}", START_MARKER, zero_width, END_MARKER);

    if carrier.is_empty() {
        return Ok(encoded_message);
    }

    let chars: Vec<char> = carrier.chars().collect();
    if chars.len() > 1 {
        let mut result = String::new();
        result.push(chars[0]);
        result.push_str(&encoded_message);
        for c in &chars[1..] {
            result.push(*c);
        }
        Ok(result)
    } else {
        Ok(format!("{}{}", carrier, encoded_message))
    }
}

fn decode(carrier: &str, password: Option<&str>) -> Result<String, Box<dyn Error>> {
    info!("Decoding carrier: {}", carrier);
    if let Some(pwd) = password {
        info!("Using password: {}", pwd);
    }

    let start = carrier.find(START_MARKER).ok_or("No valid message found in carrier text")?;
    let end = carrier.find(END_MARKER).ok_or("No valid message found in carrier text")?;
    let start_idx = carrier.char_indices().nth(start).map(|(i, _)| i).unwrap_or(0) + START_MARKER.len();
    let end_idx = carrier.char_indices().nth(end).map(|(i, _)| i).unwrap_or(carrier.len());
    let encoded = &carrier[start_idx..end_idx];

    let data = decode_binary(encoded);
    let mut decoded = data;

    // Fernet decrypt if password is provided
    if let Some(pwd) = password {
        let key = derive_fernet_key(pwd);
        let fernet = Fernet::new(&key).ok_or("Invalid Fernet key")?;
        let encrypted_str = std::str::from_utf8(&decoded)?;
        decoded = fernet.decrypt(encrypted_str).map_err(|e| format!("Fernet decryption failed: {:?}", e))?;
    }

    let result = String::from_utf8(base64::decode(&decoded)?)?;
    info!("Decoded message: {}", result);
    Ok(result)
}

fn main() -> Result<(), Box<dyn Error>> {
    let matches = App::new("whitespace-stego")
        .version("1.0")
        .author("Your Name")
        .about("Whitespace steganography tool")
        .arg(
            Arg::with_name("verbose")
                .short("v")
                .long("verbose")
                .help("Enable verbose output")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("encode")
                .short("e")
                .long("encode")
                .help("Encode mode")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("decode")
                .short("d")
                .long("decode")
                .help("Decode mode")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("message")
                .short("m")
                .long("message")
                .help("Message to encode")
                .takes_value(true),
        )
        .arg(
            Arg::with_name("carrier")
                .short("c")
                .long("carrier")
                .help("Carrier text")
                .takes_value(true),
        )
        .arg(
            Arg::with_name("password")
                .short("p")
                .long("password")
                .help("Password for encryption")
                .takes_value(true),
        )
        .get_matches();

    // Initialize logger
    let log_level = if matches.is_present("verbose") {
        LevelFilter::Debug
    } else {
        LevelFilter::Info
    };
    Builder::new().filter_level(log_level).init();

    let encode_mode = matches.is_present("encode");
    let decode_mode = matches.is_present("decode");

    if encode_mode && decode_mode {
        error!("Cannot specify both encode and decode modes");
        return Ok(());
    }

    if !encode_mode && !decode_mode {
        error!("Must specify either encode or decode mode");
        return Ok(());
    }

    if encode_mode {
        let message = matches.value_of("message").ok_or("Message required for encode mode")?;
        let carrier = matches.value_of("carrier").ok_or("Carrier text required for encode mode")?;
        let password = matches.value_of("password");

        debug!("Encoding message: {}", message);
        debug!("Using carrier: {}", carrier);
        debug!("Using password: {}", password.unwrap_or("None"));

        let result = encode(message, carrier, password)?;
        debug!("Final encoded message: {}", result);
        println!("{}", result);
    }

    if decode_mode {
        let carrier = matches.value_of("carrier").ok_or("Carrier text required for decode mode")?;
        let password = matches.value_of("password");

        debug!("Decoding carrier: {}", carrier);
        debug!("Using password: {}", password.unwrap_or("None"));

        let result = decode(carrier, password)?;
        debug!("Decoded message: {}", result);
        println!("{}", result);
    }

    Ok(())
} 