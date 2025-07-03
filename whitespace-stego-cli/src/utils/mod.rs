//! Utility functions for the CLI.
//!
//! This module provides utility functions for display, formatting,
//! and other common operations.
//!
//! ## Features
//! - Display utilities for user output
//! - Logging and verbosity control
//! - Error and info message formatting

pub mod display;

/// Re-export display utility functions.
pub use display::{error, info, verbose, warn};
