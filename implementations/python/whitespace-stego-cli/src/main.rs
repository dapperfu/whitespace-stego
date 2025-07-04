//! Command-line interface for whitespace steganography.
//!
//! This binary provides a full-featured command-line interface for encoding
//! and decoding messages using whitespace steganography.

use clap::{Parser, Subcommand};
use std::process;

mod commands;
mod io;
mod utils;

use commands::{decode, encode};
use utils::display;

/// Whitespace Steganography CLI.
///
/// A command-line tool for hiding messages in text using zero-width Unicode characters.
/// Supports optional encryption and various input/output methods.
///
/// # Examples
/// ```
/// // Encode a message
/// whitespace-stego encode -m "secret" -c "cover text" -o output.txt
///
/// // Decode a message
/// whitespace-stego decode -c "cover text with hidden message" -p "password"
/// ```
#[derive(Parser)]
#[command(
    name = "whitespace-stego",
    author,
    version,
    about,
    long_about = "A command-line tool for hiding messages in text using zero-width Unicode characters. \
                  Supports optional encryption and various input/output methods including files and stdin/stdout."
)]
struct Cli {
    /// Enable verbose output
    #[arg(short, long)]
    verbose: bool,

    /// Enable quiet mode (suppress non-error output)
    #[arg(short, long)]
    quiet: bool,

    /// Show progress indicators
    #[arg(long)]
    progress: bool,

    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
/// Available subcommands for the CLI.
enum Commands {
    /// Encode a message into carrier text
    Encode {
        /// Message to encode
        #[arg(short = 'm', long)]
        message: Option<String>,

        /// File containing message to encode
        #[arg(short = 'f', long = "message-file")]
        message_file: Option<std::path::PathBuf>,

        /// Carrier text
        #[arg(short = 'c', long)]
        carrier: Option<String>,

        /// File containing carrier text
        #[arg(short = 'F', long = "carrier-file")]
        carrier_file: Option<std::path::PathBuf>,

        /// Password for encryption
        #[arg(short = 'p', long)]
        password: Option<String>,

        /// Output file (use - for stdout)
        #[arg(short = 'o', long)]
        output: Option<std::path::PathBuf>,

        /// Interactive mode
        #[arg(short = 'i', long)]
        interactive: bool,
    },

    /// Decode a message from carrier text
    Decode {
        /// Carrier text
        #[arg(short = 'c', long)]
        carrier: Option<String>,

        /// File containing carrier text
        #[arg(short = 'F', long = "carrier-file")]
        carrier_file: Option<std::path::PathBuf>,

        /// Password for decryption
        #[arg(short = 'p', long)]
        password: Option<String>,

        /// Output file (use - for stdout)
        #[arg(short = 'o', long)]
        output: Option<std::path::PathBuf>,

        /// Interactive mode
        #[arg(short = 'i', long)]
        interactive: bool,
    },

    /// Analyze text for encoded messages
    Analyze {
        /// Text to analyze
        #[arg(short = 't', long)]
        text: Option<String>,

        /// File containing text to analyze
        #[arg(short = 'f', long = "file")]
        file: Option<std::path::PathBuf>,

        /// Output format (text, json)
        #[arg(short = 'F', long = "format", default_value = "text")]
        format: String,
    },

    /// Extract encoded message and remaining carrier
    Extract {
        /// Carrier text
        #[arg(short = 'c', long)]
        carrier: Option<String>,

        /// File containing carrier text
        #[arg(short = 'F', long = "carrier-file")]
        carrier_file: Option<std::path::PathBuf>,

        /// Output directory for extracted files
        #[arg(short = 'o', long = "output-dir")]
        output_dir: Option<std::path::PathBuf>,
    },
}

/// Main entry point for the CLI application.
///
/// Parses command-line arguments and dispatches to appropriate command handlers.
///
/// # Errors
/// Returns an error if command execution fails.
fn main() {
    let cli = Cli::parse();

    // Set up logging/verbosity
    if cli.verbose {
        display::set_verbose(true);
    }
    if cli.quiet {
        display::set_quiet(true);
    }
    if cli.progress {
        display::set_progress(true);
    }

    let result = match cli.command {
        Commands::Encode {
            message,
            message_file,
            carrier,
            carrier_file,
            password,
            output,
            interactive,
        } => {
            if interactive {
                encode::interactive_encode()
            } else {
                encode::encode_command(
                    message,
                    message_file,
                    carrier,
                    carrier_file,
                    password,
                    output,
                )
            }
        },

        Commands::Decode {
            carrier,
            carrier_file,
            password,
            output,
            interactive,
        } => {
            if interactive {
                decode::interactive_decode()
            } else {
                decode::decode_command(carrier, carrier_file, password, output)
            }
        },

        Commands::Analyze { text, file, format } => {
            commands::analyze::analyze_command(text, file, format)
        },

        Commands::Extract {
            carrier,
            carrier_file,
            output_dir,
        } => commands::extract::extract_command(carrier, carrier_file, output_dir),
    };

    if let Err(e) = result {
        display::error(&format!("Error: {}", e));
        process::exit(1);
    }
}
