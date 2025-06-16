use clap::{Parser, Subcommand};
use std::fs;
use std::io::{self, Read};
use std::path::PathBuf;
use whitespace_stego::{decode, encode, StegoError};

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
        /// Message to encode (use --message or -m)
        #[arg(short = 'm', long)]
        message: Option<String>,

        /// File containing message to encode (use --mf or -f)
        #[arg(short = 'f', long = "mf")]
        message_file: Option<PathBuf>,

        /// Carrier text (use --carrier or -c)
        #[arg(short = 'c', long)]
        carrier: Option<String>,

        /// File containing carrier text (use --cf or -F)
        #[arg(short = 'F', long = "cf")]
        carrier_file: Option<PathBuf>,

        /// Password for encryption (use --password or -p)
        #[arg(short = 'p', long)]
        password: Option<String>,

        /// Output file (use --output or -o, use - for stdout)
        #[arg(short = 'o', long)]
        output: Option<PathBuf>,
    },

    /// Decode a message from carrier text
    Decode {
        /// Carrier text (use --carrier or -c)
        #[arg(short = 'c', long)]
        carrier: Option<String>,

        /// File containing carrier text (use --cf or -F)
        #[arg(short = 'F', long = "cf")]
        carrier_file: Option<PathBuf>,

        /// Password for decryption (use --password or -p)
        #[arg(short = 'p', long)]
        password: Option<String>,

        /// Output file (use --output or -o, use - for stdout)
        #[arg(short = 'o', long)]
        output: Option<PathBuf>,
    },
}

fn read_file_or_stdin(path: Option<&PathBuf>) -> io::Result<String> {
    match path {
        Some(path) => fs::read_to_string(path),
        None => {
            let mut buffer = String::new();
            io::stdin().read_to_string(&mut buffer)?;
            Ok(buffer)
        }
    }
}

fn write_file_or_stdout(content: &str, path: Option<&PathBuf>) -> io::Result<()> {
    match path {
        Some(path) if path.to_str() != Some("-") => fs::write(path, content),
        _ => {
            print!("{}", content);
            Ok(())
        }
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Encode {
            message,
            message_file,
            carrier,
            carrier_file,
            password,
            output,
        } => {
            // Read message
            if message.is_some() && message_file.is_some() {
                return Err("Cannot specify both --message and --message-file".into());
            }
            let message_content = message
                .or_else(|| {
                    message_file
                        .as_ref()
                        .and_then(|f| read_file_or_stdin(Some(f)).ok())
                })
                .ok_or("No message provided")?;

            // Read carrier
            if carrier.is_some() && carrier_file.is_some() {
                return Err("Cannot specify both --carrier and --carrier-file".into());
            }
            let carrier_content = carrier
                .or_else(|| {
                    carrier_file
                        .as_ref()
                        .and_then(|f| read_file_or_stdin(Some(f)).ok())
                })
                .unwrap_or_default();

            // Read password
            let password_content = password.as_deref();

            // Encode message
            let encoded = encode(&message_content, &carrier_content, password_content)
                .map_err(|e| e.to_string())?;

            // Write output
            write_file_or_stdout(&encoded, output.as_ref())?;
        }

        Commands::Decode {
            carrier,
            carrier_file,
            password,
            output,
        } => {
            // Read carrier
            if carrier.is_some() && carrier_file.is_some() {
                return Err("Cannot specify both --carrier and --carrier-file".into());
            }
            let carrier_content = carrier
                .or_else(|| {
                    carrier_file
                        .as_ref()
                        .and_then(|f| read_file_or_stdin(Some(f)).ok())
                })
                .ok_or("No carrier provided")?;

            // Read password
            let password_content = password.as_deref();

            // Decode message
            let decoded = decode(&carrier_content, password_content).map_err(|e| e.to_string())?;

            // Write output
            write_file_or_stdout(&decoded, output.as_ref())?;
        }
    }

    Ok(())
}
