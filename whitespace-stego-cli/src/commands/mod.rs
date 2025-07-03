//! Command implementations for the CLI.
//!
//! This module contains the implementation of all CLI commands,
//! organized into separate modules for maintainability.
//!
//! ## Available Commands
//! - `encode`: Encode messages into carrier text
//! - `decode`: Decode messages from carrier text
//! - `analyze`: Analyze text for encoded messages
//! - `extract`: Extract encoded messages and remaining carrier

pub mod analyze;
pub mod decode;
pub mod encode;
pub mod extract;

/// Re-export analyze command function.
pub use analyze::analyze_command;
/// Re-export decode command functions.
pub use decode::{decode_command, interactive_decode};
/// Re-export encode command functions.
pub use encode::{encode_command, interactive_encode};
/// Re-export extract command function.
pub use extract::extract_command;
