use clap::{Parser, Subcommand};
use std::fs;
use std::path::PathBuf;
use whitespace_stego_core::{decode, encode};

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Encode a message into a carrier text
    Encode {
        /// Message file path
        #[arg(short = 'm', long = "message-file", value_name = "FILE")]
        message_file: PathBuf,

        /// Carrier file path
        #[arg(short = 'c', long = "carrier-file", value_name = "FILE")]
        carrier_file: PathBuf,

        /// Output file path
        #[arg(short = 'o', long = "output", value_name = "FILE")]
        output: PathBuf,

        /// Password for encryption (optional)
        #[arg(short = 'p', long = "password")]
        password: Option<String>,
    },
    /// Decode a message from a carrier text
    Decode {
        /// Input file path
        #[arg(short = 'i', long = "input", value_name = "FILE")]
        input: PathBuf,

        /// Output file path
        #[arg(short = 'o', long = "output", value_name = "FILE")]
        output: PathBuf,

        /// Password for decryption (optional)
        #[arg(short = 'p', long = "password")]
        password: Option<String>,
    },
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Encode {
            message_file,
            carrier_file,
            output,
            password,
        } => {
            let message = fs::read_to_string(message_file)?;
            let carrier = fs::read_to_string(carrier_file)?;
            let encoded = encode(&carrier, &message, password.as_deref())?;
            fs::write(output, encoded)?;
        },
        Commands::Decode {
            input,
            output,
            password,
        } => {
            let carrier = fs::read_to_string(input)?;
            let decoded = decode(&carrier, password.as_deref())?;
            fs::write(output, decoded)?;
        },
    }

    Ok(())
}
