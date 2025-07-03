use clap::{Arg, Command};
use env_logger;
use log::{info, LevelFilter};
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
        }
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
        }
        _ => {
            return Err("No subcommand provided. Use encode or decode.".into());
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode_decode_no_password() {
        let message = "Hello, World!";
        let carrier = "This is a test";
        let encoded = core_encode(message, carrier, None).unwrap();
        println!("Encoded (no password): {}", encoded);
        let decoded = core_decode(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_with_password() {
        let message = "Secret message";
        let carrier = "This is a test";
        let password = "test_password";
        let encoded = core_encode(message, carrier, Some(password)).unwrap();
        println!("Encoded (with password): {}", encoded);
        let decoded = core_decode(&encoded, Some(password)).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_empty_carrier() {
        let message = "Test message";
        let carrier = "";
        let encoded = core_encode(message, carrier, None).unwrap();
        let decoded = core_decode(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_encode_decode_single_char_carrier() {
        let message = "Test message";
        let carrier = "A";
        let encoded = core_encode(message, carrier, None).unwrap();
        let decoded = core_decode(&encoded, None).unwrap();
        assert_eq!(decoded, message);
    }

    #[test]
    fn test_decode_invalid_carrier() {
        let result = core_decode("Invalid carrier", None);
        assert!(result.is_err());
    }

    #[test]
    fn test_decode_wrong_password() {
        let message = "Secret message";
        let carrier = "Test carrier";
        let password = "correct_password";
        let wrong_password = "wrong_password";
        let encoded = core_encode(message, carrier, Some(password)).unwrap();
        let result = core_decode(&encoded, Some(wrong_password));
        assert!(result.is_err());
    }
}
