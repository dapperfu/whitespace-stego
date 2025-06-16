use pyo3::prelude::*;
use base64;

const CONTROL_START: &str = "⁠";
const CONTROL_END: &str = "⁣";
const BIT_0: &str = "​";
const BIT_1: &str = "‌";

#[pyfunction]
fn encode_message(message: &str, carrier: &str) -> String {
    let b64 = base64::encode(message);
    let bits: String = b64.chars().flat_map(|c| format!("{:08b}", c as u8).chars()).collect();
    let encoded: String = bits.chars().map(|b| if b == '0' { BIT_0 } else { BIT_1 }).collect();
    if carrier.is_empty() {
        format!("{}{}{}", CONTROL_START, encoded, CONTROL_END)
    } else {
        let (head, tail) = carrier.split_at(1);
        format!("{}{}{}{}", head, CONTROL_START, encoded, CONTROL_END, tail)
    }
}

#[pyfunction]
fn decode_message(encoded: &str) -> PyResult<String> {
    let start = encoded.find(CONTROL_START).ok_or("Missing start marker")? + CONTROL_START.len();
    let end = encoded[start..].find(CONTROL_END).ok_or("Missing end marker")? + start;
    let payload = &encoded[start..end];
    let bits: String = payload.chars().map(|c| match c {
        c if c == BIT_0.chars().next().unwrap() => Ok('0'),
        c if c == BIT_1.chars().next().unwrap() => Ok('1'),
        _ => Err("Invalid character in payload")
    }).collect::<Result<_, _>>()?;
    let bytes: Vec<u8> = bits.as_bytes().chunks(8)
        .map(|chunk| std::str::from_utf8(chunk).unwrap())
        .map(|b| u8::from_str_radix(b, 2).unwrap())
        .collect();
    let decoded = base64::decode(&bytes).map_err(|_| "Base64 decode failed")?;
    Ok(String::from_utf8(decoded).map_err(|_| "UTF8 decode failed")?)
}

#[pymodule]
fn whitespace_stego_pyo3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode_message, m)?)?;
    m.add_function(wrap_pyfunction!(decode_message, m)?)?;
    Ok(())
}
