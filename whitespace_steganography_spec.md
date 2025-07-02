# 🕵️‍♂️ Whitespace Steganography Project Specification 🕵️‍♀️

## 🎯 Overview

This project implements a sneaky steganography technique using invisible zero-width Unicode whitespace characters! 🥷 Think of it as hiding secret messages in plain sight - like a digital invisible ink that only the initiated can read! ✨

The encoder uses **four** distinct zero-width characters (because why not make things interesting? 🤷‍♂️):

- **2 control characters** 🎮: denote the **start** and **end** of each hidden message (like bookends for your secrets!)
- **2 data characters** 💾: encode binary digits **0** and **1** (the digital equivalent of Morse code, but invisible!)

Before binary encoding, the input message is **base64-encoded** to ensure consistent handling of Unicode characters. For example, the emoji 😀 becomes `8J+YgA==` (because even emojis need to be properly dressed for their secret mission! 🎭).

## 📋 Encoding Rules

- **Zero-character carrier** 🌀: Return the whitespace-encoded message directly (because empty space is the perfect hiding spot!)
- **Non-zero carrier** 📝: Embed the whitespace message **after the first character** of the carrier text (like slipping a note into a book after the first page!)
- **Multiple messages** 📚: Each message is encoded as a separate zero-width block, delimited by start and end markers. Multiple messages can be embedded sequentially in the same carrier (because one secret is never enough! 🎪).

## 🏗️ Required Implementations

The following implementations are required and must be kept in sync (like a well-choreographed dance troupe! 💃🕺):

1. **Pure Python module** 🐍 (the gold reference for all behavior and compatibility - the wise elder of the group!)
2. **Pure Rust implementation** 🦀 (the speed demon that never sleeps!)
3. **Rust-backed Python module** 🐍🦀 (via PyO3 + maturin - the best of both worlds!)
4. **Pure C implementation** ⚡ (the old-school master that still knows all the tricks!)

All implementations must:
- Support encoding and decoding of multiple messages per carrier (because variety is the spice of life! 🌶️).
- Output all decoded messages on separate lines in CLI mode (for maximum readability and dramatic effect! 📖).
- Be fully interoperable: encode in any, decode in any, for any number of messages, with or without password (like a universal translator for secrets! 🌍).

## 🎁 Deliverables

### Command-Line Interfaces

Four tools will be provided (because one tool is never enough for a proper spy kit! 🛠️):

1. **Python CLI (pure)** 🐍:
   - `whitespace-stego` with `--backend python`
2. **Rust-backed Python CLI** 🐍🦀 (via PyO3 + maturin):
   - `whitespace-stego` with `--backend rust`
3. **Pure Rust CLI** 🦀:
   - `whitespace-stego-rs`
4. **Pure C CLI** ⚡:
   - `whitespace-stego-c`

### CLI Arguments

- `-m/--message`, `-mf/--message-file` 📄: Message input (your secret sauce!)
- `-c/--carrier`, `-cf/--carrier-file` 📦: Carrier input (the innocent bystander that carries your secrets!)
- `-p/--password`, `-pf/--password-file` 🔐: Optional password protection (because some secrets need extra security!)
- `-o/--output` 📤: Output location. `-o -` writes to stdout (because sometimes you want to shout your secrets from the rooftops!)

### Examples

```bash
whitespace-stego encode --backend python --message "Hello" --carrier "Hi"
whitespace-stego encode --backend rust --message "Hello" --carrier "Hi"
whitespace-stego-rs encode --message "Hello" --carrier "Hi"
whitespace-stego-c encode -m message.txt -c carrier.txt -o encoded.txt
```

## ✨ Features

- Base64 encoding ensures proper Unicode handling (because even secrets need to be properly formatted! 📝)
- Message can be embedded even in an empty carrier (because empty space is the perfect canvas for secrets! 🎨)
- Password-based encryption (if provided) 🔐 (because some secrets are worth protecting!)
- CLI and file-based I/O 📁 (because flexibility is key!)
- **Multiple message support** 📚: Any number of messages can be encoded and decoded per carrier (because one secret is never enough!)
- **Interoperability** 🤝: All implementations must be able to decode messages produced by any other implementation (because secrets should be universal!)

## 🎪 Multi-Message Support and Output Format

- Multiple messages are encoded as separate zero-width blocks, each with its own start and end marker (like chapters in a secret book! 📖).
- When decoding via CLI, all messages are output on separate lines, in the order they are found (for maximum dramatic effect! 🎭).
- Single-message decode returns just the message (no extra newline) (because sometimes less is more! ✨).
- This behavior is required for all implementations (because consistency is the key to success! 🗝️).

## 🧪 Testing

The **Python implementation** is the gold reference and must include a comprehensive test suite using `pytest` and parameterization. All other implementations must be tested for full compatibility with the Python reference, including multi-message and password-protected scenarios (because quality control is everything! 🎯).

### Example Test

```python
@pytest.mark.parametrize("message", MESSAGES)
@pytest.mark.parametrize("password", PASSWORDS)
@pytest.mark.parametrize("carrier", CARRIERS)
def test_stego_encode_decode(message: str, password: str | None, carrier: str) -> None:
    ...
```

Additional tests must cover:
- Multiple message encode/decode (including cross-implementation) 🔄
- Password-protected and unprotected messages 🔐
- Unicode, emoji, and multilingual text 🌍
- CLI output format (one message per line) 📋

## 🤔 Why Use Steganography? Real-World Examples! 🎭

### 🕵️‍♂️ Corporate Espionage (The Fun Way!)
Hide your lunch plans in the company newsletter: "The quarterly report shows excellent growth" might secretly contain "Meet at the taco truck at noon - bring extra napkins!" 🌮

### 💕 Romantic Messages
Send love notes hidden in boring work emails: "Please review the attached spreadsheet" could secretly say "I love you more than spreadsheets!" 💖

### 🎮 Gaming Secrets
Share cheat codes or secret meeting locations in public chat: "Nice weather today!" might contain "The treasure is behind the waterfall in level 3!" 🎮

### 📚 Academic Shenanigans
Hide study notes in your professor's lecture notes: "The mitochondria is the powerhouse of the cell" could secretly contain "The exam is mostly about photosynthesis!" 🧬

### 🎪 Party Planning
Coordinate surprise parties in plain sight: "Don't forget to bring the quarterly reports" might secretly say "Don't forget the cake and balloons!" 🎂

### 🦹‍♂️ Superhero Communication
When you're a superhero with a secret identity, you need to communicate without revealing your true self: "The weather forecast looks cloudy" could secretly mean "Villain spotted downtown - need backup!" 🦸‍♂️

## 📝 Notes

- Use secure encryption algorithms for password-protected encoding (because some secrets are worth protecting with military-grade security! 🛡️).
- Ensure consistent handling of emojis, multilingual text, and special characters (because secrets come in all languages and flavors! 🌍).
- The **pure Python implementation is the gold reference** for all behavior and compatibility (the wise elder that all others must follow! 🧙‍♂️).
- All implementations must be interoperable (e.g., encode in Python, decode in Rust, C, or Rust-backed Python, and vice versa, for any number of messages) (because secrets should be universal! 🌍).

Remember: With great steganography power comes great responsibility! Use your invisible message powers for good, not evil! 🦸‍♀️✨
