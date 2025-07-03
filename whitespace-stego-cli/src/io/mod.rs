//! Input/Output utilities for the CLI.
//!
//! This module provides utilities for reading from files or stdin
//! and writing to files or stdout.

pub mod files;
pub mod streams;

pub use files::{read_file_or_stdin, write_file_or_stdout};
pub use streams::stream_processor;
