//! File I/O utilities for the CLI.
//!
//! This module provides utilities for reading from files or stdin
//! and writing to files or stdout.

use anyhow::{anyhow, Result};
use std::fs;
use std::io::{self, Read, Write};
use std::path::PathBuf;

/// Read content from a file or stdin
///
/// # Arguments
/// * `path` - Optional file path. If None, reads from stdin
///
/// # Returns
/// The content as a string
///
/// # Errors
/// Returns an error if the file cannot be read or if stdin reading fails
pub fn read_file_or_stdin(path: Option<&PathBuf>) -> Result<String> {
    match path {
        Some(path) => fs::read_to_string(path)
            .map_err(|e| anyhow!("Failed to read file '{}': {}", path.display(), e)),
        None => {
            let mut buffer = String::new();
            io::stdin()
                .read_to_string(&mut buffer)
                .map_err(|e| anyhow!("Failed to read from stdin: {}", e))?;
            Ok(buffer)
        },
    }
}

/// Write content to a file or stdout
///
/// # Arguments
/// * `content` - The content to write
/// * `path` - Optional file path. If None or "-", writes to stdout
///
/// # Errors
/// Returns an error if the file cannot be written or if stdout writing fails
pub fn write_file_or_stdout(content: &str, path: Option<&PathBuf>) -> Result<()> {
    match path {
        Some(path) if path.to_str() != Some("-") => fs::write(path, content)
            .map_err(|e| anyhow!("Failed to write file '{}': {}", path.display(), e)),
        _ => {
            print!("{}", content);
            io::stdout()
                .flush()
                .map_err(|e| anyhow!("Failed to write to stdout: {}", e))
        },
    }
}

/// Check if a file exists and is readable
///
/// # Arguments
/// * `path` - The file path to check
///
/// # Returns
/// `true` if the file exists and is readable
pub fn file_exists_and_readable(path: &PathBuf) -> bool {
    path.exists() && path.is_file() && fs::metadata(path).is_ok()
}

/// Get file size in bytes
///
/// # Arguments
/// * `path` - The file path
///
/// # Returns
/// The file size in bytes, or None if the file doesn't exist
pub fn get_file_size(path: &PathBuf) -> Option<u64> {
    fs::metadata(path).ok().map(|metadata| metadata.len())
}

#[cfg(test)]
mod tests {
    use super::*;
    use tempfile::NamedTempFile;

    #[test]
    fn test_read_file_or_stdin_with_file() {
        let temp_file = NamedTempFile::new().unwrap();
        let content = "test content";
        fs::write(&temp_file, content).unwrap();

        let result = read_file_or_stdin(Some(&temp_file.path().to_path_buf())).unwrap();
        assert_eq!(result, content);
    }

    #[test]
    fn test_write_file_or_stdout_to_file() {
        let temp_file = NamedTempFile::new().unwrap();
        let content = "test content";

        write_file_or_stdout(content, Some(&temp_file.path().to_path_buf())).unwrap();

        let written_content = fs::read_to_string(temp_file.path()).unwrap();
        assert_eq!(written_content, content);
    }

    #[test]
    fn test_file_exists_and_readable() {
        let temp_file = NamedTempFile::new().unwrap();
        assert!(file_exists_and_readable(&temp_file.path().to_path_buf()));

        let non_existent = PathBuf::from("/non/existent/file");
        assert!(!file_exists_and_readable(&non_existent));
    }

    #[test]
    fn test_get_file_size() {
        let temp_file = NamedTempFile::new().unwrap();
        let content = "test content";
        fs::write(&temp_file, content).unwrap();

        let size = get_file_size(&temp_file.path().to_path_buf()).unwrap();
        assert_eq!(size, content.len() as u64);
    }
}
