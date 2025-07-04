//! Display utilities for the CLI.
//!
//! This module provides utilities for displaying messages to the user
//! with different levels of verbosity and formatting.

use std::io::Write;
use std::sync::atomic::{AtomicBool, Ordering};

static VERBOSE: AtomicBool = AtomicBool::new(false);
static QUIET: AtomicBool = AtomicBool::new(false);
static PROGRESS: AtomicBool = AtomicBool::new(false);

/// Set verbose mode
pub fn set_verbose(enabled: bool) {
    VERBOSE.store(enabled, Ordering::Relaxed);
}

/// Set quiet mode
pub fn set_quiet(enabled: bool) {
    QUIET.store(enabled, Ordering::Relaxed);
}

/// Set progress mode
pub fn set_progress(enabled: bool) {
    PROGRESS.store(enabled, Ordering::Relaxed);
}

/// Check if verbose mode is enabled
pub fn is_verbose() -> bool {
    VERBOSE.load(Ordering::Relaxed)
}

/// Check if quiet mode is enabled
pub fn is_quiet() -> bool {
    QUIET.load(Ordering::Relaxed)
}

/// Check if progress mode is enabled
#[allow(dead_code)]
pub fn is_progress() -> bool {
    PROGRESS.load(Ordering::Relaxed)
}

/// Display an error message
pub fn error(message: &str) {
    if !is_quiet() {
        eprintln!("❌ Error: {}", message);
    }
}

/// Display an info message
pub fn info(message: &str) {
    if !is_quiet() {
        println!("ℹ️  {}", message);
    }
}

/// Display a warning message
#[allow(dead_code)]
pub fn warn(message: &str) {
    if !is_quiet() {
        eprintln!("⚠️  Warning: {}", message);
    }
}

/// Display a verbose message (only shown in verbose mode)
pub fn verbose(message: &str) {
    if is_verbose() && !is_quiet() {
        eprintln!("🔍 DEBUG: {}", message);
    }
}

/// Display a success message
#[allow(dead_code)]
pub fn success(message: &str) {
    if !is_quiet() {
        println!("✅ {}", message);
    }
}

/// Display a progress message
#[allow(dead_code)]
pub fn progress(message: &str) {
    if is_progress() && !is_quiet() {
        eprint!("\r🔄 {}", message);
        std::io::stderr().flush().ok();
    }
}

/// Clear the current line (useful for progress messages)
#[allow(dead_code)]
pub fn clear_line() {
    if is_progress() && !is_quiet() {
        eprint!("\r\x1B[K");
        std::io::stderr().flush().ok();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_verbose_mode() {
        set_verbose(false);
        assert!(!is_verbose());

        set_verbose(true);
        assert!(is_verbose());
    }

    #[test]
    fn test_quiet_mode() {
        set_quiet(false);
        assert!(!is_quiet());

        set_quiet(true);
        assert!(is_quiet());
    }

    #[test]
    fn test_progress_mode() {
        set_progress(false);
        assert!(!is_progress());

        set_progress(true);
        assert!(is_progress());
    }
}
