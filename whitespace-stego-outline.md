# whitespace-stego — Technical Project Outline

## 🧠 Purpose

Create a steganographic encoding system using **zero-width Unicode whitespace** to hide messages invisibly inside any text, with optional password protection. The system uses start/end control characters to delimit an entire hidden payload — not per-character.

---

## 🧱 How It Works

### 1. Password Protection (Optional)

- If a password is provided:
  - Encrypt the message using AES-256 or similar.
  - Key derived via PBKDF2, scrypt, or Argon2 from the password.
  - Output is then base64-encoded.
- If no password is given:
  - Message is directly base64-encoded.

---

### 2. Base64 Encoding

- Ensures compatibility and known character set for binary encoding.
- Example: `"Hi"` → `SGk=`

---

### 3. Binary Encoding via Zero-Width Characters

#### Binary Mapping

- Each base64 character → 8-bit binary representation.
- Bits are encoded using:
  - `U+200B` (Zero-Width Space, `ZWSP`) → **bit 0**
  - `U+200C` (Zero-Width Non-Joiner, `ZWNJ`) → **bit 1**

**Example**

Base64 `"S"` → binary `01010011`  
Encoded as: `ZWSP ZWNJ ZWSP ZWNJ ZWSP ZWSP ZWNJ ZWNJ`

---

### 4. Framing the Hidden Message

Only one **start** and one **end** control character is used to mark the boundaries of the entire encoded message.

#### Control Characters

- Start: `U+2060` (Word Joiner) → `<`
- End: `U+2061` (Function Application) → `>`

#### Final Format

Encoded binary bitstream (made of ZWSP/ZWNJ) is wrapped once:
```
<binary_bitstream>
```

**Example**

Base64 message `"SGk="` → binary → long stream of ZWSP/ZWNJ  
Wrapped: `U+2060 [encoded bits] U+2061`

---

## 💬 Carrier Text Integration

The full encoded payload (`<binary>`) can be inserted into any position within a visible carrier message:

| Carrier Text      | Output Example                 |
|-------------------|--------------------------------|
| Empty             | `<[ZW binary]>`                |
| `"A"`             | `A<[ZW binary]>`               |
| `"Hello World"`   | `Hel<[ZW binary]>lo World`     |

**Insertion Strategies**

- At start
- After Nth character
- Randomly placed (with seed)
- Just before final punctuation

---

## 🔄 Decoding Flow

1. **Scan Input** for `U+2060` and `U+2061` (start and end).
2. **Extract** the binary payload between them.
3. **Translate** ZWSP/ZWNJ to binary (`0`/`1`), grouped by 8 bits.
4. **Reconstruct** base64 string from binary chunks.
5. **Base64-decode** to get original message or ciphertext.
6. **Decrypt** (if password-protected).

---

## 🧪 Example

### Input:
```plaintext
Hello<[ZWSP ZWNJ ZWSP ZWSP ...]>World
```

### Output:
```plaintext
Decoded message: "Hi" (if no password)
```

---

## 🗂 File Structure

```
whitespace-stego/
├── README.md
├── Makefile
├── common/
│   └── charset.py       # Maps and utils
├── python/
│   ├── encode.py
│   ├── decode.py
│   ├── crypto.py
│   └── cli.py
├── rust/
│   ├── src/
│   └── ...
└── tests/
    ├── test_encode.py
    └── test_decode.py
```

---

## ⚙️ CLI Usage

```bash
$ whitespace-stego encode -m "Secret" -p "hunter2" -i message.txt -o stego.txt
$ whitespace-stego decode -i stego.txt -p "hunter2"
```

---

## 🚧 Notes

- Detectability is possible with tools scanning for zero-width characters.
- Security comes from encryption, not the stego method.
- Future enhancement: obfuscation patterns, compression before base64, multiple fragments.

---
