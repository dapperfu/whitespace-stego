use pyo3::prelude::*;

mod encode;
mod decode;

/// A Python module implemented in Rust.
#[pymodule]
fn whitespace_stego_backend(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encode::encode, m)?)?;
    m.add_function(wrap_pyfunction!(decode::decode, m)?)?;
    Ok(())
} 