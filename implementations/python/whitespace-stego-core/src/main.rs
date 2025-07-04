//!
//! Example binary for inspecting whitespace steganography constants.
//!
//! Prints the Unicode code points for the start, end, zero, and one markers used in the core library.
//!
//! ## Usage
//! Run this binary to see the marker values and their Unicode code points.
//!
//! ## License
//! SPDX-License-Identifier: MIT

use whitespace_stego_core::constants::{END_MARKER, ONE_BIT, START_MARKER, ZERO_BIT};

/// Prints the Unicode code points for the steganography markers.
fn main() {
    println!("START_MARKER: {:?}", START_MARKER);
    println!("END_MARKER: {:?}", END_MARKER);
    println!("ZERO_BIT: {:?}", ZERO_BIT);
    println!("ONE_BIT: {:?}", ONE_BIT);

    println!("START_MARKER code: U+{:04X}", START_MARKER as u32);
    println!("END_MARKER code: U+{:04X}", END_MARKER as u32);
    println!("ZERO_BIT code: U+{:04X}", ZERO_BIT as u32);
    println!("ONE_BIT code: U+{:04X}", ONE_BIT as u32);
}
