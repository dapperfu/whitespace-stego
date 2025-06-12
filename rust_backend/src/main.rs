use anyhow::{Context, Result};
use clap::{Parser, Subcommand};
use std::fs;
use std::path::PathBuf;
use whitespace_stego_rs::{encode, decode};
use std::io::{self, Read, Write};

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
        message: Option<String>,

        /// File containing message
        #[arg(long)]
        message_file: Option<PathBuf>,

        /// Carrier text
        #[arg(short, long)]
        carrier: Option<String>,

        /// File containing carrier content
        #[arg(long)]
        carrier_file: Option<PathBuf>,

        /// Output file for stego message
        #[arg(short, long)]
        output: Option<PathBuf>,

        /// Output file (long option)
        #[arg(long)]
        output_file: Option<PathBuf>,

        /// Optional password for encryption
        #[arg(short, long)]
        password: Option<String>,
    },
    /// Decode a message from stego text
    Decode {
        /// Input as a string
        #[arg(short, long)]
        input: Option<String>,

        /// Input file
        #[arg(long)]
        input_file: Option<PathBuf>,

        /// Output file for decoded message
        #[arg(short, long)]
        output: Option<PathBuf>,

        /// Output file (long option)
        #[arg(long)]
        output_file: Option<PathBuf>,

        /// Optional password for decryption
        #[arg(short, long)]
        password: Option<String>,
    },
}

fn read_text_source(opt_str: &Option<String>, opt_file: &Option<PathBuf>) -> Result<String> {
    if let Some(file) = opt_file {
        if file.to_string_lossy() == "-" {
            let mut buf = String::new();
            io::stdin().read_to_string(&mut buf)?;
            Ok(buf)
        } else {
            Ok(std::fs::read_to_string(file)?)
        }
    } else if let Some(s) = opt_str {
        Ok(s.clone())
    } else {
        Ok(String::new())
    }
}

fn write_text_sink(opt_file: &Option<PathBuf>, content: &str) -> Result<()> {
    let file = opt_file.as_ref();
    if let Some(path) = file {
        if path.to_string_lossy() == "-" {
            print!("{}", content);
            io::stdout().flush()?;
        } else {
            std::fs::write(path, content)?;
        }
    } else {
        print!("{}", content);
        io::stdout().flush()?;
    }
    Ok(())
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Encode {
            message,
            message_file,
            carrier,
            carrier_file,
            output,
            output_file,
            password,
        } => {
            let msg = read_text_source(&message, &message_file)?;
            let carrier_text = read_text_source(&carrier, &carrier_file)?;
            let encoded = encode(&msg, &carrier_text, password.as_deref(), None)
                .map_err(|e| anyhow::anyhow!("{}", e))?;
            let out_file = output_file.or(output);
            write_text_sink(&out_file, &encoded)?;
        }
        Commands::Decode {
            input,
            input_file,
            output,
            output_file,
            password,
        } => {
            let text = read_text_source(&input, &input_file)?;
            let (decoded, _) = decode(&text, password.as_deref())
                .map_err(|e| anyhow::anyhow!("{}", e))?;
            let out_file = output_file.or(output);
            write_text_sink(&out_file, &decoded)?;
        }
    }

    Ok(())
} 