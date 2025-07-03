//! Encode command implementation.
//!
//! This module provides the functionality for encoding messages into carrier text.

use anyhow::{anyhow, Result};
use std::path::PathBuf;
use whitespace_stego_core::encode;

use crate::io::{read_file_or_stdin, write_file_or_stdout};
use crate::utils::display;

/// Encode a message into carrier text
pub fn encode_command(
    message: Option<String>,
    message_file: Option<PathBuf>,
    carrier: Option<String>,
    carrier_file: Option<PathBuf>,
    password: Option<String>,
    output: Option<PathBuf>,
) -> Result<()> {
    // Validate input parameters
    if message.is_some() && message_file.is_some() {
        return Err(anyhow!("Cannot specify both --message and --message-file"));
    }
    if carrier.is_some() && carrier_file.is_some() {
        return Err(anyhow!("Cannot specify both --carrier and --carrier-file"));
    }

    // Read message
    let message_content = message
        .or_else(|| {
            message_file
                .as_ref()
                .and_then(|f| read_file_or_stdin(Some(f)).ok())
        })
        .ok_or_else(|| anyhow!("No message provided. Use --message or --message-file"))?;

    // Read carrier (default to empty if not provided)
    if let Some(ref carrier) = carrier {
        eprintln!("[DEBUG] Rust CLI encode carrier repr: {:?}", carrier);
    }
    let carrier_content = carrier
        .or_else(|| {
            carrier_file
                .as_ref()
                .and_then(|f| read_file_or_stdin(Some(f)).ok())
        })
        .ok_or_else(|| anyhow!("No carrier provided. Use --carrier or --carrier-file"))?;

    // Get password
    let password_content = password.as_deref();

    display::verbose(&format!(
        "Encoding message ({} chars)",
        message_content.len()
    ));
    display::verbose(&format!("Using carrier ({} chars)", carrier_content.len()));
    display::verbose(&format!(
        "Using password: {}",
        password_content.unwrap_or("None")
    ));

    // Encode message
    let encoded = encode(&message_content, &carrier_content, password_content)
        .map_err(|e| anyhow!("Encoding failed: {}", e))?;

    display::verbose("Message successfully encoded");

    // Write output
    write_file_or_stdout(&encoded, output.as_ref())?;

    display::info("Message encoded successfully");
    Ok(())
}

/// Interactive encode mode
pub fn interactive_encode() -> Result<()> {
    use std::io::{self, Write};

    print!("Enter message to encode: ");
    io::stdout().flush()?;

    let mut message = String::new();
    io::stdin().read_line(&mut message)?;
    let message = message.trim();

    if message.is_empty() {
        return Err(anyhow!("Message cannot be empty"));
    }

    print!("Enter carrier text (optional): ");
    io::stdout().flush()?;

    let mut carrier = String::new();
    io::stdin().read_line(&mut carrier)?;
    let carrier = carrier.trim();

    print!("Enter password (optional): ");
    io::stdout().flush()?;

    let mut password = String::new();
    io::stdin().read_line(&mut password)?;
    let password = password.trim();

    let password = if password.is_empty() {
        None
    } else {
        Some(password)
    };

    display::verbose(&format!("Encoding message ({} chars)", message.len()));
    display::verbose(&format!("Using carrier ({} chars)", carrier.len()));
    display::verbose(&format!("Using password: {}", password.unwrap_or("None")));

    // Encode message
    let encoded =
        encode(message, carrier, password).map_err(|e| anyhow!("Encoding failed: {}", e))?;

    display::verbose("Message successfully encoded");

    // Output result
    println!("\nEncoded text:");
    println!("{}", encoded);

    display::info("Message encoded successfully");
    Ok(())
}
