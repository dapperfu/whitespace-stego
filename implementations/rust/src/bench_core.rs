// Benchmark core encode/decode functions for Rust implementation.
//
// Build:
//   cargo run --release --bin bench_core
//
// (or: rustc -O src/bench_core.rs -o bench_core)
//
// Run:
//   ./target/release/bench_core
//
fn main() {
    use std::time::Instant;
    use whitespace_stego_core::{encode, decode_fast};

    const ITER: usize = 1000;
    const MSG_REPEAT: usize = 100;
    const CARRIER_REPEAT: usize = 100;

    let message = "Secret message".repeat(MSG_REPEAT);
    let carrier = "This is the carrier text.".repeat(CARRIER_REPEAT);
    let mut encoded = String::new();
    let mut decoded = String::new();

    // Benchmark encode
    let t0 = Instant::now();
    for _ in 0..ITER {
        match encode(&message, &carrier, None) {
            Ok(e) => encoded = e,
            Err(e) => { println!("[WARN] encode error: {}", e); break; }
        }
    }
    let elapsed = t0.elapsed().as_secs_f64();
    println!("Rust encode: {:.2} ms total, {:.2} us/call", elapsed*1000.0, elapsed/ITER as f64*1e6);

    // Benchmark decode with fast version (no debug logging)
    println!("\n=== DECODE PROFILING (FAST VERSION) ===");
    let t0 = Instant::now();
    for i in 0..ITER {
        let decode_start = Instant::now();
        match decode_fast(&encoded, None) {
            Ok(d) => {
                decoded = d;
                let decode_time = decode_start.elapsed();
                if i % 100 == 0 {
                    println!("Decode iteration {}: {:.2} ms", i, decode_time.as_secs_f64() * 1000.0);
                }
            },
            Err(e) => { 
                println!("[WARN] decode error: {}", e); 
                break; 
            }
        }
    }
    let elapsed = t0.elapsed().as_secs_f64();
    println!("Rust decode (fast): {:.2} ms total, {:.2} us/call", elapsed*1000.0, elapsed/ITER as f64*1e6);
    // Prevent optimization
    println!("Decoded length: {}", decoded.len());
    
    // Test single decode timing
    println!("\n=== SINGLE DECODE TEST (FAST VERSION) ===");
    let t0 = Instant::now();
    match decode_fast(&encoded, None) {
        Ok(d) => {
            let elapsed = t0.elapsed().as_secs_f64();
            println!("Single decode (fast): {:.2} ms", elapsed * 1000.0);
            println!("Decoded message length: {}", d.len());
        },
        Err(e) => println!("Single decode error: {}", e)
    }
} 