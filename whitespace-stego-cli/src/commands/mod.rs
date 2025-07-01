//! Command implementations for the CLI.
//!
//! This module contains the implementation of all CLI commands,
//! organized into separate modules for maintainability.

pub mod analyze;
pub mod decode;
pub mod encode;
pub mod extract;

pub use analyze::analyze_command;
pub use decode::{decode_command, interactive_decode};
pub use encode::{encode_command, interactive_encode};
pub use extract::extract_command; 