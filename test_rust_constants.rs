use whitespace_stego_core::constants::{START_MARKER, END_MARKER, ZERO_BIT, ONE_BIT};

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