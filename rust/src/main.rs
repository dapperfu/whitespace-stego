use clap::{App, Arg, SubCommand};
use std::error::Error;
use log::{debug, error, info, LevelFilter};
use env_logger::Builder;
use base64::{Engine as _, engine::general_purpose::STANDARD_NO_PAD};
use fernet::{Fernet, DecryptionError};
use sha2::{Sha256, Digest};
use std::fs;
use std::io::{self, Read, Write};
use std::path::Path;

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
    let mut hasher = Sha256::new();
    hasher.update(password.as_bytes());
    let result = hasher.finalize();
    STANDARD_NO_PAD.encode(result)
}

fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, Box<dyn Error>> {
    info!("Encoding message: {}", message);
    info!("Using carrier: {}", carrier);
    if let Some(pwd) = password {
        info!("Using password: {}", pwd);
    }

    // Base64 encode the message with padding
    let encoded = base64::encode(message.as_bytes());

    // Fernet encrypt if password is provided
    let final_data = if let Some(pwd) = password {
        let key = derive_fernet_key(pwd);
        let fernet = Fernet::new(&key).ok_or("Invalid Fernet key")?;
        fernet.encrypt(&encoded)
    } else {
        encoded
    };

    let zero_width = encode_binary(final_data.as_bytes());
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
    let decoded = if let Some(pwd) = password {
        let key = derive_fernet_key(pwd);
        let fernet = Fernet::new(&key).ok_or("Invalid Fernet key")?;
        let encrypted_str = std::str::from_utf8(&data)?;
        fernet.decrypt(encrypted_str).map_err(|e| format!("Fernet decryption failed: {:?}", e))?
    } else {
        data
    };

    let result = String::from_utf8(base64::decode(&decoded)?)?;
    info!("Decoded message: {}", result);
    Ok(result)
}

fn main() -> Result<(), Box<dyn Error>> {
    env_logger::builder().filter_level(LevelFilter::Info).init();
    let matches = App::new("whitespace-stego-rs")
        .version("1.0")
        .author("Your Name")
        .about("Whitespace steganography tool")
        .subcommand(
            SubCommand::with_name("encode")
                .about("Encode a message into a carrier")
                .arg(Arg::with_name("message")
                    .short("m")
                    .long("message")
                    .takes_value(true)
                    .help("Message to encode"))
                .arg(Arg::with_name("message_file")
                    .long("mf")
                    .takes_value(true)
                    .help("File containing the message to encode"))
                .arg(Arg::with_name("carrier")
                    .short("c")
                    .long("carrier")
                    .takes_value(true)
                    .help("Carrier text"))
                .arg(Arg::with_name("carrier_file")
                    .long("cf")
                    .takes_value(true)
                    .help("File containing the carrier text"))
                .arg(Arg::with_name("password")
                    .short("p")
                    .long("password")
                    .takes_value(true)
                    .help("Password for encryption"))
                .arg(Arg::with_name("output")
                    .short("o")
                    .long("output")
                    .takes_value(true)
                    .help("Output file (default: stdout)")),
        )
        .subcommand(
            SubCommand::with_name("decode")
                .about("Decode a message from a carrier")
                .arg(Arg::with_name("carrier")
                    .short("c")
                    .long("carrier")
                    .takes_value(true)
                    .help("Carrier text"))
                .arg(Arg::with_name("carrier_file")
                    .long("cf")
                    .takes_value(true)
                    .help("File containing the carrier text"))
                .arg(Arg::with_name("password")
                    .short("p")
                    .long("password")
                    .takes_value(true)
                    .help("Password for decryption"))
                .arg(Arg::with_name("output")
                    .short("o")
                    .long("output")
                    .takes_value(true)
                    .help("Output file (default: stdout)")),
        )
        .get_matches();

    match matches.subcommand() {
        ("encode", Some(sub_m)) => {
            let message = if let Some(mf) = sub_m.value_of("message_file") {
                fs::read_to_string(mf)?
            } else if let Some(m) = sub_m.value_of("message") {
                m.to_string()
            } else {
                return Err("No message provided".into());
            };
            let carrier = if let Some(cf) = sub_m.value_of("carrier_file") {
                fs::read_to_string(cf)?
            } else if let Some(c) = sub_m.value_of("carrier") {
                c.to_string()
            } else {
                String::new()
            };
            let password = sub_m.value_of("password");
            let output = sub_m.value_of("output");
            let encoded = encode(&message, &carrier, password)?;
            if let Some(out) = output {
                fs::write(out, &encoded)?;
            } else {
                println!("{}", encoded);
            }
        }
        ("decode", Some(sub_m)) => {
            let carrier = if let Some(cf) = sub_m.value_of("carrier_file") {
                fs::read_to_string(cf)?
            } else if let Some(c) = sub_m.value_of("carrier") {
                c.to_string()
            } else {
                return Err("No carrier provided".into());
            };
            let password = sub_m.value_of("password");
            let output = sub_m.value_of("output");
            let decoded = decode(&carrier, password)?;
            if let Some(out) = output {
                fs::write(out, &decoded)?;
            } else {
                println!("{}", decoded);
            }
        }
        _ => {
            return Err("No subcommand provided. Use encode or decode.".into());
        }
    }
    Ok(())
} 