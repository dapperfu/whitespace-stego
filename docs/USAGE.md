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
- `--backend`: Choose backend (python, rust, c, go)
- `--verbose`: Verbose logging

### Rust CLI

```bash
./bin/whitespace-stego-rs encode --mf message.txt --cf carrier.txt -o encoded.txt
./bin/whitespace-stego-rs decode --cf encoded.txt -o decoded.txt
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
./bin/whitespace-stego-c encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt
./bin/whitespace-stego-c decode --carrier-file encoded.txt --output decoded.txt
```

#### Options
- `--message-file`, `-m`: Message file
- `--carrier-file`, `-c`: Carrier file
- `--output`, `-o`: Output file
- `--password`, `-p`: Password
- `--verbose`, `-v`: Verbose

### Go CLI

```bash
./bin/whitespace-stego-go encode -m "Secret" -cf carrier.txt -o encoded.txt -p password
./bin/whitespace-stego-go decode -cf encoded.txt -o decoded.txt -p password
```

#### Options
- `-m`: Message to encode
- `-cf`: Carrier file
- `-o`: Output file
- `-p`: Password for encryption/decryption
- `--verbose`: Verbose logging

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

### Go
```go
import "github.com/your-repo/whitespace-stego"
encoded, err := whitespace_stego.Encode("Secret", "Carrier", "pw")
decoded, err := whitespace_stego.Decode(encoded, "pw")
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
  - Encode in Python, decode in Rust, C, or Go, and vice versa
- **Pipeline Usage:**
  - `python3 -m whitespace_stego.cli encode ... | python3 -m whitespace_stego.cli decode --carrier-file -`
- **Verbose Debugging:**
  - Add `--verbose` to any CLI command
- **Cross-implementation Unicode:**
  - Encode with emojis in Go, decode in Python or Rust, and verify round-trip

---

For more, see the [Jupyter Notebooks Guide](NOTEBOOKS.md) and [examples/practical_use_cases.md](../examples/practical_use_cases.md). 