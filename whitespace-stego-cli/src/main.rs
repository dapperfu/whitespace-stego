use clap::{Parser, Subcommand};
use std::fs;
use std::io::{self, Read, Write};
use whitespace_stego_core::{encode, decode};

/// Whitespace Steganography CLI
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Encode a message into a carrier file
    Encode {
        /// Path to the carrier file
        #[arg(short, long)]
        carrier: String,
        /// Path to the message file
        #[arg(short, long)]
        message: String,
        /// Path to the output file
        #[arg(short, long)]
        output: String,
        /// Optional password
        #[arg(short, long)]
        password: Option<String>,
    },
    /// Decode a message from a carrier file
    Decode {
        /// Path to the carrier file
        #[arg(short, long)]
        carrier: String,
        /// Path to the output file
        #[arg(short, long)]
        output: String,
        /// Optional password
        #[arg(short, long)]
        password: Option<String>,
    },
}

fn main() {
    let cli = Cli::parse();
    match cli.command {
        Commands::Encode { carrier, message, output, password } => {
            let carrier_content = fs::read_to_string(&carrier)
                .expect("Failed to read carrier file");
            let message_content = fs::read_to_string(&message)
                .expect("Failed to read message file");
            let encoded = encode(&carrier_content, &message_content, password.as_deref())
                .expect("Encoding failed");
            fs::write(&output, encoded).expect("Failed to write output file");
        }
        Commands::Decode { carrier, output, password } => {
            let carrier_content = fs::read_to_string(&carrier)
                .expect("Failed to read carrier file");
            let decoded = decode(&carrier_content, password.as_deref())
                .expect("Decoding failed");
            fs::write(&output, decoded).expect("Failed to write output file");
        }
    }
} 