use std::env;

const CONTROL_START: &str = "⁠";
const CONTROL_END: &str = "⁣";
const BIT_0: &str = "​";
const BIT_1: &str = "‌";

fn encode_message(message: &str) -> String {
    let b64 = base64::encode(message);
    let bits: String = b64.chars().flat_map(|c| {
        format!("{:08b}", c as u8).chars().collect::<Vec<_>>()
    }).collect();
    let encoded: String = bits.chars().map(|b| if b == '0' { BIT_0 } else { BIT_1 }).collect();
    format!("{}{}{}", CONTROL_START, encoded, CONTROL_END)
}

fn decode_message(text: &str) -> Result<String, String> {
    let start = text.find(CONTROL_START).ok_or("No start control")? + CONTROL_START.len();
    let end = text[start..].find(CONTROL_END).ok_or("No end control")? + start;
    let payload = &text[start..end];
    let bits: String = payload.chars().map(|c| match c {
        c if c == BIT_0.chars().next().unwrap() => '0',
        c if c == BIT_1.chars().next().unwrap() => '1',
        _ => return Err("Invalid char in payload".to_string())
    }).collect::<Result<_, _>>()?;
    let bytes: Vec<u8> = bits.as_bytes().chunks(8)
        .map(|chunk| std::str::from_utf8(chunk).unwrap())
        .map(|b| u8::from_str_radix(b, 2).unwrap())
        .collect();
    let decoded = base64::decode(&bytes).map_err(|_| "Base64 decode failed")?;
    Ok(String::from_utf8(decoded).map_err(|_| "UTF8 decode failed")?)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: encode|decode <text>");
        return;
    }
    match args[1].as_str() {
        "encode" => println!("{}", encode_message(&args[2])),
        "decode" => match decode_message(&args[2]) {
            Ok(s) => println!("{}", s),
            Err(e) => eprintln!("Error: {}", e),
        },
        _ => eprintln!("Unknown command"),
    }
}
