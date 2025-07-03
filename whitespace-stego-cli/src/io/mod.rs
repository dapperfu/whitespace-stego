//! Input/Output utilities for the CLI.
//!
//! This module provides utilities for reading from files or stdin
//! and writing to files or stdout.
//!
//! ## Features
//! - File and stdin reading utilities
//! - File and stdout writing utilities
//! - Stream processing capabilities

pub mod files;
pub mod streams;

/// Re-export file reading and writing utilities.
pub use files::{read_file_or_stdin, write_file_or_stdout};
