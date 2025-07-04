//! Decode command implementation.
//!
//! This module provides the functionality for decoding messages from carrier text.

use anyhow::{anyhow, Result};
use std::path::PathBuf;
use whitespace_stego_core::decode;

use crate::io::{read_file_or_stdin, write_file_or_stdout};
use crate::utils::display;

/// Decode a message from carrier text
pub fn decode_command(
    carrier: Option<String>,
    carrier_file: Option<PathBuf>,
    password: Option<String>,
    output: Option<PathBuf>,
) -> Result<()> {
    // Validate input parameters
    if carrier.is_some() && carrier_file.is_some() {
        return Err(anyhow!("Cannot specify both --carrier and --carrier-file"));
    }

    // Read carrier
    if let Some(ref carrier) = carrier {
        eprintln!("[DEBUG] Rust CLI decode carrier repr: {:?}", carrier);
        let codepoints: Vec<String> = carrier
            .chars()
            .take(40)
            .map(|c| format!("0x{:x}", c as u32))
            .collect();
        eprintln!(
            "[DEBUG] Rust CLI decode carrier codepoints: {:?}",
            codepoints
        );
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
        "Decoding carrier ({} chars)",
        carrier_content.len()
    ));
    display::verbose(&format!(
        "Using password: {}",
        password_content.unwrap_or("None")
    ));

    // Decode message
    let decoded = decode(&carrier_content, password_content)
        .map_err(|e| anyhow!("Decoding failed: {}", e))?;

    display::verbose("Message successfully decoded");

    // Write output
    write_file_or_stdout(&decoded, output.as_ref())?;

    display::info("Message decoded successfully");
    Ok(())
}

/// Interactive decode mode
pub fn interactive_decode() -> Result<()> {
    use std::io::{self, Write};

    print!("Enter carrier text: ");
    io::stdout().flush()?;

    let mut carrier = String::new();
    io::stdin().read_line(&mut carrier)?;
    let carrier = carrier.trim();

    if carrier.is_empty() {
        return Err(anyhow!("Carrier text cannot be empty"));
    }

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

    display::verbose(&format!("Decoding carrier ({} chars)", carrier.len()));
    display::verbose(&format!("Using password: {}", password.unwrap_or("None")));

    // Decode message
    let decoded = decode(carrier, password).map_err(|e| anyhow!("Decoding failed: {}", e))?;

    display::verbose("Message successfully decoded");

    // Output result
    println!("\nDecoded message:");
    println!("{}", decoded);

    display::info("Message decoded successfully");
    Ok(())
}
