# Whitespace Steganography WASI

A WebAssembly System Interface (WASI) implementation of whitespace steganography that allows you to hide messages in plain text using invisible Unicode characters.

## Features

- 🔐 **Message Encoding**: Hide secret messages within normal-looking text
- 🔓 **Message Decoding**: Extract hidden messages from encoded text
- 🔒 **Password Protection**: Optional encryption using Fernet (compatible with Python implementation)
- 🌐 **Web Interface**: Beautiful, responsive web UI for easy use
- 📋 **Copy to Clipboard**: One-click copying of results
- 📱 **Mobile Friendly**: Responsive design that works on all devices

## How It Works

This tool uses zero-width Unicode characters to encode binary data:
- `\u{200B}` (Zero-width space) - Start marker
- `\u{200C}` (Zero-width non-joiner) - End marker  
- `\u{200D}` (Zero-width joiner) - Represents bit 0
- `\u{FEFF}` (Zero-width no-break space) - Represents bit 1

The message is first Base64 encoded, then optionally encrypted with a password, and finally converted to these invisible characters.

## Prerequisites

- Rust (latest stable version)
- wasm-pack (will be installed automatically if missing)

## Building

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd whitespace-stego3/wasi
   ```

2. **Build the WASM module**:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

   This will:
   - Install wasm-pack if not present
   - Clean previous builds
   - Compile the Rust code to WebAssembly
   - Generate JavaScript bindings
   - Copy the HTML file to the output directory

## Running

After building, you can run the web application:

```bash
cd pkg
python3 -m http.server 8000
```

Then open your browser and navigate to `http://localhost:8000`

## Usage

### Encoding a Message

1. Enter your secret message in the "Secret Message" field
2. Enter the carrier text where you want to hide the message
3. Optionally enter a password for encryption
4. Click "🔒 Encode Message"
5. Copy the encoded text from the output area

### Decoding a Message

1. Paste the encoded text into the "Carrier Text" field
2. If the message was encrypted, enter the password
3. Click "🔓 Decode Message"
4. The hidden message will appear in the output area

## API Reference

The WASM module exposes the following functions:

### `encode(message: string, carrier: string, password?: string): string`

Encodes a message into carrier text.

- `message`: The secret message to hide
- `carrier`: The text where the message will be hidden
- `password`: Optional password for encryption

Returns the encoded text.

### `decode(carrier: string, password?: string): string`

Decodes a message from carrier text.

- `carrier`: The text containing the hidden message
- `password`: Optional password for decryption

Returns the decoded message.

### `has_encoded_data(text: string): boolean`

Checks if text contains encoded data.

- `text`: The text to check

Returns true if encoded data is found.

### `extract_carrier(text: string): string`

Extracts the original carrier text without encoded data.

- `text`: The text containing encoded data

Returns the carrier text without the hidden message.

## Security Notes

- The password protection uses Fernet encryption, which is compatible with the Python implementation
- Zero-width characters are invisible to the human eye but can be detected by software
- Always use strong passwords for sensitive messages
- The encoded text can be detected by analyzing Unicode character patterns

## Browser Compatibility

This application works in all modern browsers that support WebAssembly:
- Chrome 57+
- Firefox 52+
- Safari 11+
- Edge 16+

## Development

### Project Structure

```
wasi/
├── src/
│   └── lib.rs          # Main WASM library implementation
├── Cargo.toml          # Rust dependencies and configuration
├── index.html          # Web interface
├── build.sh            # Build script
└── README.md           # This file
```

### Modifying the Code

1. Edit `src/lib.rs` to modify the core functionality
2. Edit `index.html` to modify the web interface
3. Run `./build.sh` to rebuild the WASM module
4. Refresh your browser to see changes

### Testing

The web interface includes built-in validation and error handling. You can test the functionality by:

1. Encoding a simple message without a password
2. Decoding the result to verify it works
3. Testing with password protection
4. Testing with various Unicode characters and emojis

## License

This project is licensed under the MIT License - see the main project LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 