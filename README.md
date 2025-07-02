![Project Logo](39e228c0-fefd-4bc1-82bf-fe581329754b.png)

# 🕵️‍♂️ Whitespace Steganography

> *"The best place to hide a tree is in a forest. The best place to hide a secret is in plain sight."* 🌲

A modern, multi-language toolkit for hiding secret messages in text using **invisible Unicode characters** — because sometimes the most obvious place to hide something is right under everyone's nose! 👀

Supports Python 🐍, Rust 🦀, C ⚡, and WebAssembly 🌐 backends. Because why choose one language when you can confuse everyone with four? 🤷‍♂️

---

## 🎯 What's This All About?

Ever wanted to send a secret message that looks like innocent text? Well, you've come to the right place! We use **zero-width Unicode characters** (those sneaky invisible little buggers) to hide your secrets in plain sight. It's like having a conversation in a crowded room where only you and your friend know you're actually speaking in code! 🕵️‍♀️

---

## ✨ Features That'll Make You Go "Ooooh!"

- **🔄 Multi-language Madness:** Python, Rust, C, and WASM implementations (because variety is the spice of life!)
- **🖥️ CLI & Web UI:** Command-line for hackers, browser interface for normies
- **🌍 Unicode & Emoji Friendly:** Works with any text, any language, any emoji (even the weird ones)
- **🔐 Password Protection:** Optional encryption because sometimes you need that extra layer of paranoia
- **🤝 Cross-compatibility:** Encode in Python, decode in Rust, confuse everyone in between
- **🧪 Comprehensive Testing:** 1300+ tests because we're not animals (we're developers!)

---

## 🚀 Quick Start (For the Impatient)

### 1. 🛠️ Install Everything (Python, Rust, C, WASM)

```bash
git clone <repo-url>
cd whitespace-stego3
make install  # Python + Rust backend
make rust     # Rust CLI
make c        # C CLI
make wasi-web # WebAssembly (browser UI)
```

### 2. 🎭 Encode/Decode Like a Pro (Python CLI)

```bash
# Encode your deepest secrets
python3 -m whitespace_stego.cli encode --message "Secret" --carrier "Innocent text" --output encoded.txt

# Decode and discover the truth
python3 -m whitespace_stego.cli decode --carrier-file encoded.txt
```

### 3. 🌐 Try the Web UI (For the Clicky Types)

```bash
make wasi-web
# Open http://localhost:8000 in your browser
# No command line required! 🎉
```

---

## 📝 Example (See the Magic in Action!)

Here's a simple example showing how whitespace steganography works. The secret message is hidden using invisible Unicode characters, but we can visualize them using debug methods:

**Message:** `Hello, World!`  
**Carrier:** `This is innocent text that contains a secret message.`

**Encoded Text (with visible whitespace):**
```
T[START][0][1][0][1][0][0][1][1][0][1][0][0][0][1][1][1][0][1][0][1][0][1][1][0][0][1][1][1][0][0][1][1][0][1][1][0][0][0][1][0][0][1][0][0][0][1][1][1][0][0][1][1][1][0][0][0][0][1][1][1][0][0][1][1][0][1][0][0][1][0][0][1][0][1][0][0][0][1][1][0][0][1][1][0][0][1][0][0][0][1][1][1][0][1][1][0][0][1][1][0][0][0][1][1][0][1][1][0][1][1][0][1][0][1][1][1][1][0][0][0][0][1][1][0][1][0][1][1][0][1][0][0][1][0][0][1][0][1][0][1][0][0][0][1][0][0][1][1][1][1][0][1][0][0][1][1][1][1][0][1][END]his[SPACE]is[SPACE]innocent[SPACE]text[SPACE]that[SPACE]contains[SPACE]a[SPACE]secret[SPACE]message.
```

**What's happening here?**
- `[START]` and `[END]` mark the beginning and end of the hidden data
- `[0]` and `[1]` represent the binary data (your message converted to bits)
- `[SPACE]` shows regular spaces in the carrier text
- The actual encoded text looks completely normal to the human eye!

**Try it yourself:**
```bash
# Save the encoded text to a file and decode it
echo "T​‍﻿‍﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿﻿‍﻿‍﻿‍﻿﻿‍‍﻿﻿﻿‍‍﻿﻿‍﻿﻿‍‍‍﻿‍‍﻿‍‍‍﻿﻿﻿‍‍﻿﻿﻿‍‍‍‍﻿﻿﻿‍‍﻿﻿‍﻿‍‍﻿‍‍﻿‍﻿‍‍‍﻿﻿‍‍﻿﻿‍‍﻿‍‍‍﻿﻿﻿‍﻿﻿‍‍﻿﻿‍‍‍﻿﻿‍﻿﻿‍﻿﻿‍﻿‍﻿﻿﻿﻿‍‍‍‍﻿﻿‍﻿‍﻿﻿‍﻿‍‍﻿‍‍﻿‍﻿‍﻿‍‍‍﻿‍‍﻿﻿﻿﻿‍﻿‍‍﻿﻿﻿﻿‍﻿‌his is innocent text that contains a secret message." > example.txt
python3 -m whitespace_stego.cli decode --carrier-file example.txt
```

---

## 🥚 Easter Egg Hunt! 

**Hidden Message Challenge:** Try decoding this innocent-looking "Hello World" message. You might discover something... *special*! 🕵️‍♂️

```bash
# Copy this text and save it to a file, then decode it:
H​‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍﻿‍‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍﻿‍‍‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍‍﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍‍﻿‍‍﻿﻿‍﻿‍‍‍﻿﻿‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍﻿‍﻿‍﻿‍‍﻿﻿‍﻿‍﻿‍‍‍﻿‍﻿﻿‍﻿‍﻿﻿‍﻿‍‍‍﻿‍﻿‍‍﻿﻿﻿﻿‍﻿‌ello World

# Then run:
python3 -m whitespace_stego.cli decode --carrier-file your_file.txt
```

*Hint: It's a classic gaming reference! 🎮*

---

## 📚 Documentation (For the Serious Folks)

- [📖 Usage & CLI/API Examples](docs/USAGE.md) - Because reading is fundamental
- [🔧 Installation Guide](docs/INSTALLATION.md) - Get up and running quickly
- [🏗️ System Architecture](docs/ARCHITECTURE.md) - Understand the system design
- [🐳 Docker Guide](docs/DOCKER.md) - Containerized builds and deployment
- [📋 API Reference](docs/API_REFERENCE.md) - Complete API documentation
- [🧪 Testing & Quality Assurance](docs/TESTING.md) - For the perfectionists
- [📓 Jupyter Notebooks Guide](docs/NOTEBOOKS.md) - For the data scientists
- [🔒 Security Notes](docs/SECURITY.md) - For the paranoid
- [🤝 Contributing](docs/CONTRIBUTING.md) - For the generous

---

## 🎭 Real-World Use Cases (Because We're Practical)

- **👥 Corporate Espionage:** Hide meeting notes in your lunch order (not that we condone this...)
- **💕 Secret Love Letters:** Send romantic messages that look like grocery lists
- **🎮 Gaming:** Hide cheat codes in your gaming forum posts (we see you!)
- **📝 Journaling:** Hide your deepest thoughts in your work emails (just kidding... or are we?)

---

## ⚠️ Disclaimer (Because Lawyers)

This tool is for educational and legitimate purposes only. We're not responsible if you use it to hide your grocery list in your resignation letter. That's on you! 😅

---

## 📄 License
MIT License. See [LICENSE](LICENSE). Because sharing is caring! ❤️

---

## 🌟 Final Thoughts

Remember: The best steganography is the kind that makes people think you're just bad at typing. Keep it subtle, keep it sneaky, and most importantly — keep it fun! 🎉

*"In a world full of visible secrets, be the invisible one."* ✨

## Python C Backend (ctypes)

A high-performance C backend is available for Python via ctypes. This backend uses the C implementation in `c/` and exposes it to Python for encoding and decoding.

### Building the C Shared Library

To use the C backend, you must first build the shared library:

```sh
cd c
make shared
```

This will produce `lib/libwhitespace_stego.so`.

### Using the C Backend in Python

You can use the C backend via:

```python
from whitespace_stego.c_backend import encode, decode, is_available

if is_available():
    encoded = encode("my message", "my carrier", password="secret")
    decoded = decode(encoded, password="secret")
    print(decoded)
else:
    print("C backend not available!")
```

You can also select the C backend in the CLI with `--backend c`.