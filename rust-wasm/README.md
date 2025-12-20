# Whitespace Steganography - WASM Demo

This directory contains the WebAssembly (WASM) implementation of whitespace steganography.

## Building

Build the WASM module:

```bash
wasm-pack build --target web --out-dir pkg
```

Or use the unified Makefile:

```bash
make build-rust-wasm
```

## Running the Web Demo

Start a local web server:

```bash
make serve
```

Then open http://localhost:8000 in your browser.

Alternatively, manually:

```bash
cd rust-wasm
python3 -m http.server 8000
```

## Files

- `src/lib.rs` - WASM bindings using wasm-bindgen
- `index.html` - Web demo interface
- `pkg/` - Generated WASM package (created by wasm-pack)

## API

The WASM module exposes:

- `encode_message(message: string, carrier?: string): string` - Encode a message
- `decode_message(encoded_text: string): string` - Decode a message
- `has_encoded_data(text: string): boolean` - Check if text contains encoded data

