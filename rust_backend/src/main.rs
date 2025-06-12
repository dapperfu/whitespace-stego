use anyhow::{Context, Result};
use clap::{Parser, Subcommand};
use std::fs;
use std::path::PathBuf;
use whitespace_stego_rs::{encode, decode};

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Encode a message into carrier text
    Encode {
        /// Secret message to hide
        #[arg(short, long)]
        message: String,

        /// Carrier text
        #[arg(short, long)]
        carrier: Option<String>,

        /// File containing carrier content
        #[arg(long)]
        carrier_file: Option<PathBuf>,

        /// Output file for stego message
        #[arg(short, long)]
        output: PathBuf,

        /// Optional password for encryption
        #[arg(short, long)]
        password: Option<String>,
    },
    /// Decode a message from stego text
    Decode {
        /// Input file with hidden message
        #[arg(short, long)]
        input: PathBuf,

        /// Optional password for decryption
        #[arg(short, long)]
        password: Option<String>,
    },
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Encode {
            message,
            carrier,
            carrier_file,
            output,
            password,
        } => {
            let carrier_text = if let Some(carrier) = carrier {
                carrier
            } else if let Some(carrier_file) = carrier_file {
                fs::read_to_string(&carrier_file)
                    .with_context(|| format!("Failed to read carrier file: {:?}", carrier_file))?
            } else {
                String::new()
            };

            let encoded = encode(&message, &carrier_text, password.as_deref())?;
            fs::write(&output, encoded)
                .with_context(|| format!("Failed to write output file: {:?}", output))?;
        }
        Commands::Decode { input, password } => {
            let encoded = fs::read_to_string(&input)
                .with_context(|| format!("Failed to read input file: {:?}", input))?;
            let (decoded, _) = decode(&encoded, password.as_deref())?;
            println!("{}", decoded);
        }
    }

    Ok(())
} 