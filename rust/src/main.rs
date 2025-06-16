use clap::{App, Arg};
use std::error::Error;
use whitespace_stego::{decode, encode};
use log::{debug, error, info, LevelFilter};
use env_logger::Builder;

fn main() -> Result<(), Box<dyn Error>> {
    let matches = App::new("whitespace-stego")
        .version("1.0")
        .author("Your Name")
        .about("Whitespace steganography tool")
        .arg(
            Arg::with_name("verbose")
                .short('v')
                .long("verbose")
                .help("Enable verbose output")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("encode")
                .short('e')
                .long("encode")
                .help("Encode mode")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("decode")
                .short('d')
                .long("decode")
                .help("Decode mode")
                .takes_value(false),
        )
        .arg(
            Arg::with_name("message")
                .short('m')
                .long("message")
                .help("Message to encode")
                .takes_value(true),
        )
        .arg(
            Arg::with_name("carrier")
                .short('c')
                .long("carrier")
                .help("Carrier text")
                .takes_value(true),
        )
        .arg(
            Arg::with_name("password")
                .short('p')
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