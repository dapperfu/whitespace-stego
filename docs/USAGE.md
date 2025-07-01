# Usage Guide

## Command Line Interface (CLI)

### Python CLI

```bash
python3 -m whitespace_stego.cli encode --message "Secret" --carrier "Innocent text" --output encoded.txt
python3 -m whitespace_stego.cli decode --carrier-file encoded.txt
```

#### Options
- `--message`, `--message-file`: Message to hide (inline or file)
- `--carrier`, `--carrier-file`: Carrier text (inline or file)
- `--output`: Output file (or `-` for stdout)
- `--password`: Optional password for encryption
- `--backend`: Choose backend (python, rust, c)
- `--verbose`: Verbose logging

### Rust CLI

```bash
./rust/target/release/whitespace-stego-rs encode --mf message.txt --cf carrier.txt -o encoded.txt
./rust/target/release/whitespace-stego-rs decode --cf encoded.txt -o decoded.txt
```

#### Options
- `-m`, `--message`: Inline message
- `--mf`: Message file
- `-c`, `--carrier`: Inline carrier
- `--cf`: Carrier file
- `-o`, `--output`: Output file (or `-` for stdout)
- `-p`, `--password`: Password
- `--verbose`: Verbose logging

### C CLI

```bash
./whitespace-stego-c encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
./whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt
```

#### Options
- `--message-file`, `-m`: Message file
- `--carrier-file`, `-c`: Carrier file
- `--output`, `-o`: Output file
- `--password`, `-p`: Password
- `--verbose`, `-v`: Verbose

### WebAssembly (Browser UI)

```bash
make wasi-web
# Open http://localhost:8000
```
- Encode/decode messages in your browser
- Mobile-friendly, copy-to-clipboard, no server required

---

## API Usage

### Python
```python
from whitespace_stego.core import encode, decode
encoded = encode("Secret", "Carrier text", password="pw")
decoded = decode(encoded, password="pw")
```

### Rust
```rust
use whitespace_stego_core::{encode, decode};
let encoded = encode("Secret", "Carrier", Some("pw")).unwrap();
let decoded = decode(&encoded, Some("pw")).unwrap();
```

### WASM (JavaScript)
```js
import init, { encode, decode } from './whitespace_stego_wasi.js';
await init();
const encoded = encode("Secret", "Carrier");
const decoded = decode(encoded);
```

---

## Advanced Examples

- **Unicode/Emoji:**
  - Encode/decode messages with emojis and international text
- **Password Protection:**
  - Use `--password` or API `password` argument for encryption
- **Cross-backend:**
  - Encode in Python, decode in Rust or C, and vice versa
- **Pipeline Usage:**
  - `python3 -m whitespace_stego.cli encode ... | python3 -m whitespace_stego.cli decode --carrier-file -`
- **Verbose Debugging:**
  - Add `--verbose` to any CLI command

---

For more, see the [Jupyter Notebooks Guide](NOTEBOOKS.md) and [examples/practical_use_cases.md](../examples/practical_use_cases.md). 