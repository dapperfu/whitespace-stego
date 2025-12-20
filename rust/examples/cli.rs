//! Command-line interface for whitespace steganography.

use std::fs;
use std::io::{self, Read, Write};
use whitespace_stego::{decode, encode};

fn get_arg_value(args: &[String], flags: &[&str]) -> Option<String> {
    for (i, arg) in args.iter().enumerate() {
        if flags.iter().any(|&flag| arg == flag) {
            return args.get(i + 1).cloned();
        }
    }
    None
}

fn read_input(input: Option<&str>, positional: Option<&str>) -> Result<String, String> {
    if let Some(input_path) = input {
        if input_path == "-" {
            let mut buffer = String::new();
            io::stdin().read_to_string(&mut buffer)
                .map_err(|e| format!("Failed to read from stdin: {}", e))?;
            Ok(buffer)
        } else {
            fs::read_to_string(input_path)
                .map_err(|e| format!("Failed to read file {}: {}", input_path, e))
        }
    } else if let Some(pos) = positional {
        if pos == "-" {
            let mut buffer = String::new();
            io::stdin().read_to_string(&mut buffer)
                .map_err(|e| format!("Failed to read from stdin: {}", e))?;
            Ok(buffer)
        } else {
            Ok(pos.to_string())
        }
    } else {
        Err("Input required (provide as argument, -i/--input, or '-' for stdin)".to_string())
    }
}

fn write_output(output: Option<&str>, content: &str) -> Result<(), String> {
    if let Some(output_path) = output {
        if output_path == "-" {
            print!("{}", content);
            io::stdout().flush()
                .map_err(|e| format!("Failed to write to stdout: {}", e))?;
        } else {
            fs::write(output_path, content)
                .map_err(|e| format!("Failed to write file {}: {}", output_path, e))?;
        }
    } else {
        println!("{}", content);
    }
    Ok(())
}

fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: {} <encode|decode> [options]", args[0]);
        eprintln!("\nCommands:");
        eprintln!("  encode [message] [-i <input>] [-o <output>] [-c <carrier>] [-p <password>]");
        eprintln!("  decode [encoded] [-i <input>] [-o <output>] [-p <password>]");
        eprintln!("\nOptions:");
        eprintln!("  -i, --input <file>   Input file (use '-' for stdin)");
        eprintln!("  -o, --output <file>  Output file (use '-' for stdout)");
        eprintln!("  -c, --carrier <text> Carrier text (encode only)");
        eprintln!("  -p, --password <pwd> Password for encryption/decryption");
        std::process::exit(1);
    }

    let command = &args[1];
    let cmd_args = &args[2..];

    match command.as_str() {
        "encode" => {
            let input = get_arg_value(cmd_args, &["-i", "--input"]);
            let output = get_arg_value(cmd_args, &["-o", "--output"]);
            let carrier = get_arg_value(cmd_args, &["-c", "--carrier"]);
            let password = get_arg_value(cmd_args, &["-p", "--password"]);
            let positional = cmd_args.iter()
                .find(|arg| !arg.starts_with('-') && 
                      !cmd_args.iter().any(|a| a == "-i" || a == "--input" || 
                                          a == "-o" || a == "--output" ||
                                          a == "-c" || a == "--carrier" ||
                                          a == "-p" || a == "--password"))
                .map(|s| s.as_str());

            let message = match read_input(input.as_deref(), positional) {
                Ok(m) => m,
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            };

            match encode(&message, carrier.as_deref(), password.as_deref()) {
                Ok(encoded) => {
                    let output_str = if output.is_some() { format!("{}\n", encoded) } else { encoded };
                    if let Err(e) = write_output(output.as_deref(), &output_str) {
                        eprintln!("Error: {}", e);
                        std::process::exit(1);
                    }
                }
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            }
        }
        "decode" => {
            let input = get_arg_value(cmd_args, &["-i", "--input"]);
            let output = get_arg_value(cmd_args, &["-o", "--output"]);
            let password = get_arg_value(cmd_args, &["-p", "--password"]);
            let positional = cmd_args.iter()
                .find(|arg| !arg.starts_with('-') && 
                      !cmd_args.iter().any(|a| a == "-i" || a == "--input" || 
                                          a == "-o" || a == "--output" ||
                                          a == "-p" || a == "--password"))
                .map(|s| s.as_str());

            let encoded_text = match read_input(input.as_deref(), positional) {
                Ok(t) => t,
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            };

            match decode(&encoded_text, password.as_deref()) {
                Ok(decoded) => {
                    let output_str = if output.is_some() { format!("{}\n", decoded) } else { decoded };
                    if let Err(e) = write_output(output.as_deref(), &output_str) {
                        eprintln!("Error: {}", e);
                        std::process::exit(1);
                    }
                }
                Err(e) => {
                    eprintln!("Error: {}", e);
                    std::process::exit(1);
                }
            }
        }
        _ => {
            eprintln!("Unknown command: {}", command);
            std::process::exit(1);
        }
    }
}

