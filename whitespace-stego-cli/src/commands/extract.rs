//! Extract command implementation.
//!
//! This module provides the functionality for extracting encoded messages
//! and remaining carrier text.

use anyhow::{anyhow, Result};
use std::fs;
use std::path::PathBuf;
use whitespace_stego_core::extract_encoded;

use crate::io::read_file_or_stdin;
use crate::utils::display;

/// Extract encoded message and remaining carrier
pub fn extract_command(
    carrier: Option<String>,
    carrier_file: Option<PathBuf>,
    output_dir: Option<PathBuf>,
) -> Result<()> {
    // Validate input parameters
    if carrier.is_some() && carrier_file.is_some() {
        return Err(anyhow!("Cannot specify both --carrier and --carrier-file"));
    }

    // Read carrier
    let carrier_content = carrier
        .or_else(|| {
            carrier_file
                .as_ref()
                .and_then(|f| read_file_or_stdin(Some(f)).ok())
        })
        .ok_or_else(|| anyhow!("No carrier provided. Use --carrier or --carrier-file"))?;

    display::verbose(&format!("Extracting from carrier ({} chars)", carrier_content.len()));

    // Extract encoded message and remaining carrier
    let (encoded_message, remaining_carrier) = extract_encoded(&carrier_content)
        .map_err(|e| anyhow!("Extraction failed: {}", e))?;

    display::verbose("Successfully extracted encoded message and remaining carrier");

    // Output results
    if let Some(output_dir) = output_dir {
        // Write to files in output directory
        fs::create_dir_all(&output_dir)?;
        
        let encoded_file = output_dir.join("encoded_message.txt");
        let carrier_file = output_dir.join("remaining_carrier.txt");
        
        fs::write(&encoded_file, &encoded_message)?;
        fs::write(&carrier_file, &remaining_carrier)?;
        
        display::info(&format!("Encoded message written to: {}", encoded_file.display()));
        display::info(&format!("Remaining carrier written to: {}", carrier_file.display()));
    } else {
        // Output to stdout
        println!("=== ENCODED MESSAGE ===");
        println!("{}", encoded_message);
        println!();
        println!("=== REMAINING CARRIER ===");
        println!("{}", remaining_carrier);
    }

    display::info("Extraction completed successfully");
    Ok(())
} 