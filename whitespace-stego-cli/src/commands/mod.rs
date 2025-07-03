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

