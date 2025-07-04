//! Analyze command implementation.
//!
//! This module provides the functionality for analyzing text for encoded messages.

use anyhow::{anyhow, Result};
use serde::Serialize;
use std::path::PathBuf;
use whitespace_stego_core::{
    get_encoded_message_position, get_encoded_message_size, has_encoded_message,
};

use crate::io::read_file_or_stdin;

#[derive(Serialize)]
struct AnalysisResult {
    has_encoded_message: bool,
    message_size: Option<usize>,
    position: Option<(usize, usize)>,
    text_length: usize,
}

/// Analyze text for encoded messages
pub fn analyze_command(text: Option<String>, file: Option<PathBuf>, format: String) -> Result<()> {
    // Validate input parameters
    if text.is_some() && file.is_some() {
        return Err(anyhow!("Cannot specify both --text and --file"));
    }

    // Read text
    let text_content = text
        .or_else(|| file.as_ref().and_then(|f| read_file_or_stdin(Some(f)).ok()))
        .ok_or_else(|| anyhow!("No text provided. Use --text or --file"))?;

    // Analyze text
    let has_message = has_encoded_message(&text_content);
    let message_size = get_encoded_message_size(&text_content);
    let position = get_encoded_message_position(&text_content);

    let result = AnalysisResult {
        has_encoded_message: has_message,
        message_size,
        position,
        text_length: text_content.len(),
    };

    // Output result
    match format.as_str() {
        "text" => output_text_format(&result, &text_content)?,
        "json" => output_json_format(&result)?,
        _ => return Err(anyhow!("Invalid format. Use 'text' or 'json'")),
    }

    Ok(())
}

fn output_text_format(result: &AnalysisResult, _text: &str) -> Result<()> {
    println!("Text Analysis Results:");
    println!("=====================");
    println!("Text length: {} characters", result.text_length);
    println!("Contains encoded message: {}", result.has_encoded_message);

    if result.has_encoded_message {
        if let Some(size) = result.message_size {
            println!("Encoded message size: {} bytes", size);
        }
        if let Some((start, end)) = result.position {
            println!("Message position: characters {} to {}", start, end);
        }
    } else {
        println!("No encoded message found in text");
    }

    Ok(())
}

fn output_json_format(result: &AnalysisResult) -> Result<()> {
    let json = serde_json::to_string_pretty(result)
        .map_err(|e| anyhow!("Failed to serialize result: {}", e))?;
    println!("{}", json);
    Ok(())
}
