//! Command-line interface for whitespace steganography.

use whitespace_stego::{decode, encode};

fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: {} <encode|decode> [options]", args[0]);
        eprintln!("\nCommands:");
        eprintln!("  encode <message> [-c <carrier>]  Encode a message");
        eprintln!("  decode <encoded>                   Decode a message");
        std::process::exit(1);
    }

    let command = &args[1];

    match command.as_str() {
        "encode" => {
            if args.len() < 3 {
                eprintln!("Error: message required for encode");
                std::process::exit(1);
            }

            let message = &args[2];
            let carrier = args.iter().position(|x| x == "-c" || x == "--carrier")
                .and_then(|i| args.get(i + 1));

            match encode(message, carrier.map(|s| s.as_str())) {
                Ok(encoded) => println!("{}", encoded),
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            }
        }
        "decode" => {
            if args.len() < 3 {
                eprintln!("Error: encoded text required for decode");
                std::process::exit(1);
            }

            let encoded_text = &args[2];

            match decode(encoded_text) {
                Ok(decoded) => println!("{}", decoded),
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            }
        }
        _ => {
            eprintln!("Unknown command: {}", command);
            std::process::exit(1);
        }
    }
}

