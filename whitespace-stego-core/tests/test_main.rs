use std::process::Command;
use std::str::FromStr;

#[test]
fn test_main_binary_output() {
    // Build the binary
    let output = Command::new("cargo")
        .args(&["build", "--bin", "whitespace-stego-core"])
        .current_dir(".")
        .output()
        .expect("Failed to build binary");

    if !output.status.success() {
        panic!("Build failed: {}", String::from_utf8_lossy(&output.stderr));
    }

    // Run the binary and capture output
    let output = Command::new("cargo")
        .args(&["run", "--bin", "whitespace-stego-core"])
        .current_dir(".")
        .output()
        .expect("Failed to run binary");

    assert!(output.status.success(), "Binary execution failed");
    
    let stdout = String::from_utf8_lossy(&output.stdout);
    let lines: Vec<&str> = stdout.lines().collect();
    
    // Check that we have the expected number of output lines
    assert!(lines.len() >= 8, "Expected at least 8 lines of output");
    
    // Check for expected marker information
    assert!(lines.iter().any(|line| line.contains("START_MARKER")));
    assert!(lines.iter().any(|line| line.contains("END_MARKER")));
    assert!(lines.iter().any(|line| line.contains("ZERO_BIT")));
    assert!(lines.iter().any(|line| line.contains("ONE_BIT")));
    
    // Check for Unicode code point information
    assert!(lines.iter().any(|line| line.contains("U+FEFF")));
    assert!(lines.iter().any(|line| line.contains("U+200C")));
    assert!(lines.iter().any(|line| line.contains("U+200B")));
    assert!(lines.iter().any(|line| line.contains("U+200D")));
}

#[test]
fn test_main_binary_unicode_values() {
    // Run the binary and capture output
    let output = Command::new("cargo")
        .args(&["run", "--bin", "whitespace-stego-core"])
        .current_dir(".")
        .output()
        .expect("Failed to run binary");

    assert!(output.status.success());
    
    let stdout = String::from_utf8_lossy(&output.stdout);
    
    // Extract Unicode code points from output
    let lines: Vec<&str> = stdout.lines().collect();
    
    for line in lines {
        if line.contains("U+") {
            let parts: Vec<&str> = line.split("U+").collect();
            if parts.len() == 2 {
                let code_point = parts[1].trim();
                if let Ok(value) = u32::from_str_radix(code_point, 16) {
                    // Verify the code points match expected values
                    match value {
                        0xFEFF => assert!(line.contains("START_MARKER")),
                        0x200C => assert!(line.contains("END_MARKER")),
                        0x200B => assert!(line.contains("ZERO_BIT")),
                        0x200D => assert!(line.contains("ONE_BIT")),
                        _ => {} // Other code points are fine
                    }
                }
            }
        }
    }
} 