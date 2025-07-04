//! Stream processing utilities for the CLI.
//!
//! This module provides utilities for processing data streams,
//! including progress indicators and batch processing.

use anyhow::Result;
use indicatif::{ProgressBar, ProgressStyle};
use std::io::{self, BufRead, BufReader};

/// Process a stream of data with progress indication
///
/// # Arguments
/// * `input` - The input stream to process
/// * `processor` - Function to process each line
/// * `show_progress` - Whether to show progress bar
///
/// # Returns
/// The processed results
#[allow(dead_code)]
pub fn stream_processor<F, T>(
    input: Box<dyn io::Read>,
    processor: F,
    show_progress: bool,
) -> Result<Vec<T>>
where
    F: Fn(&str) -> Result<T>,
{
    let reader = BufReader::new(input);
    let lines: Vec<String> = reader.lines().collect::<io::Result<Vec<String>>>()?;

    let progress_bar = if show_progress {
        let pb = ProgressBar::new(lines.len() as u64);
        pb.set_style(
            ProgressStyle::default_bar()
                .template("[{elapsed_precise}] {bar:40.cyan/blue} {pos:>7}/{len:7} {msg}")
                .unwrap()
                .progress_chars("#>-"),
        );
        Some(pb)
    } else {
        None
    };

    let mut results = Vec::new();

    for (i, line) in lines.iter().enumerate() {
        let result = processor(line)?;
        results.push(result);

        if let Some(pb) = &progress_bar {
            pb.set_position((i + 1) as u64);
            pb.set_message(format!("Processing line {}", i + 1));
        }
    }

    if let Some(pb) = progress_bar {
        pb.finish_with_message("Processing complete");
    }

    Ok(results)
}

/// Process a file line by line with progress indication
///
/// # Arguments
/// * `file_path` - Path to the file to process
/// * `processor` - Function to process each line
/// * `show_progress` - Whether to show progress bar
///
/// # Returns
/// The processed results
#[allow(dead_code)]
pub fn process_file<F, T>(file_path: &str, processor: F, show_progress: bool) -> Result<Vec<T>>
where
    F: Fn(&str) -> Result<T>,
{
    let file = std::fs::File::open(file_path)?;
    stream_processor(Box::new(file), processor, show_progress)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_stream_processor() {
        let input = "line1\nline2\nline3".as_bytes();
        let processor = |line: &str| -> Result<String> { Ok(line.to_uppercase()) };

        let results = stream_processor(Box::new(input), processor, false).unwrap();
        assert_eq!(results, vec!["LINE1", "LINE2", "LINE3"]);
    }

    #[test]
    fn test_process_file() {
        use tempfile::NamedTempFile;

        let temp_file = NamedTempFile::new().unwrap();
        let content = "line1\nline2\nline3";
        std::fs::write(&temp_file, content).unwrap();

        let processor = |line: &str| -> Result<String> { Ok(line.to_uppercase()) };
        let results = process_file(temp_file.path().to_str().unwrap(), processor, false).unwrap();

        assert_eq!(results, vec!["LINE1", "LINE2", "LINE3"]);
    }
}
