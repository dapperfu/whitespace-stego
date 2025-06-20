# Practical Use Cases for Whitespace Steganography CLI

This document provides practical examples of how to use the whitespace steganography CLI in real-world scenarios.

## 🔐 Basic Message Hiding

### Hide a simple message in text
```bash
# Encode a message into carrier text
python3 -m whitespace_stego.cli encode \
  --message "Meet me at the coffee shop at 3 PM" \
  --carrier "This is a normal email about the quarterly report. Please review the attached documents and let me know your thoughts on the proposed changes."

# The encoded text looks normal but contains the hidden message
```

### Decode the hidden message
```bash
# Decode from the encoded text
python3 -m whitespace_stego.cli decode \
  --carrier-file encoded_text.txt
```

## 📁 File-based Operations

### Hide a message from a file
```bash
# Create a secret message file
echo "Top secret: Launch codes are 12345" > secret_message.txt

# Hide it in a carrier file
python3 -m whitespace_stego.cli encode \
  --message-file secret_message.txt \
  --carrier-file normal_document.txt \
  --output suspicious_document.txt
```

### Extract hidden message from file
```bash
python3 -m whitespace_stego.cli decode \
  --carrier-file suspicious_document.txt \
  --output extracted_secret.txt
```

## 🔒 Password Protection

### Encrypt a sensitive message
```bash
python3 -m whitespace_stego.cli encode \
  --message "Bank account: 1234-5678-9012-3456" \
  --carrier "Weekly newsletter content here..." \
  --password "mySecretPassword123" \
  --output encrypted_newsletter.txt
```

### Decrypt with password
```bash
python3 -m whitespace_stego.cli decode \
  --carrier-file encrypted_newsletter.txt \
  --password "mySecretPassword123"
```

## 🌍 International Content

### Hide Unicode messages
```bash
python3 -m whitespace_stego.cli encode \
  --message "你好世界 🌍 这是一个测试" \
  --carrier "This is a normal English document with some content." \
  --output international_doc.txt
```

### Decode Unicode content
```bash
python3 -m whitespace_stego.cli decode \
  --carrier-file international_doc.txt
```

## 🔗 Pipeline Operations

### Chain operations together
```bash
# Encode and immediately decode in a pipeline
python3 -m whitespace_stego.cli encode \
  --message "Quick test message" \
  --carrier "Test carrier text" | \
python3 -m whitespace_stego.cli decode \
  --carrier-file - \
  --output -
```

### Process multiple files
```bash
# Encode multiple messages
for i in {1..5}; do
  python3 -m whitespace_stego.cli encode \
    --message "Message $i" \
    --carrier "Carrier text $i" \
    --output "encoded_$i.txt"
done
```

## 📤 Stdout Integration

### Use in scripts
```bash
#!/bin/bash
# Get hidden message and use it in a script
HIDDEN_MSG=$(python3 -m whitespace_stego.cli decode \
  --carrier-file secret_file.txt)

echo "The hidden message is: $HIDDEN_MSG"
```

### Quick testing
```bash
# Quick encode/decode test without creating files
python3 -m whitespace_stego.cli encode \
  --message "Test" \
  --carrier "Carrier" \
  --output - | \
python3 -m whitespace_stego.cli decode \
  --carrier-file -
```

## 🔍 Debugging and Verbose Mode

### Debug encoding issues
```bash
python3 -m whitespace_stego.cli --verbose encode \
  --message "Debug message" \
  --carrier "Debug carrier" \
  --output debug_output.txt
```

### Check backend information
```bash
python3 -m whitespace_stego.cli --backend python --verbose encode \
  --message "test" \
  --carrier "test" \
  --output -
```

## 🚫 Error Handling Examples

### Handle missing options gracefully
```bash
# This will show a helpful error message
python3 -m whitespace_stego.cli encode --output test.txt
# Error: Either --message/-m or --message-file/-mf must be provided.
```

### Handle conflicting options
```bash
# This will show a helpful error message
python3 -m whitespace_stego.cli encode \
  --message "test" \
  --message-file test.txt \
  --carrier "carrier"
# Error: Illegal usage: `message` is mutually exclusive with options {'message_file'}.
```

## 📊 Batch Processing

### Process a directory of files
```bash
#!/bin/bash
# Encode all .txt files in a directory
for file in *.txt; do
  if [[ "$file" != *"encoded_"* ]]; then
    python3 -m whitespace_stego.cli encode \
      --message "Hidden in $file" \
      --carrier-file "$file" \
      --output "encoded_$file"
  fi
done
```

### Extract all hidden messages
```bash
#!/bin/bash
# Decode all encoded files
for file in encoded_*.txt; do
  echo "=== $file ==="
  python3 -m whitespace_stego.cli decode \
    --carrier-file "$file"
  echo ""
done
```

## 🔧 Advanced Usage

### Use different backends
```bash
# Use Python backend (default)
python3 -m whitespace_stego.cli --backend python encode \
  --message "test" \
  --carrier "carrier"

# Use Rust backend (if available)
python3 -m whitespace_stego.cli --backend rust encode \
  --message "test" \
  --carrier "carrier"
```

### Combine with other tools
```bash
# Encode and compress
python3 -m whitespace_stego.cli encode \
  --message "Large secret message" \
  --carrier "Carrier text" | gzip > encoded.gz

# Decompress and decode
gunzip -c encoded.gz | \
python3 -m whitespace_stego.cli decode \
  --carrier-file -
```

## 🛡️ Security Best Practices

### Use strong passwords
```bash
# Generate a strong password
PASSWORD=$(openssl rand -base64 32)

# Use it for encoding
python3 -m whitespace_stego.cli encode \
  --message "Sensitive data" \
  --carrier "Normal text" \
  --password "$PASSWORD" \
  --output secure_file.txt
```

### Clean up sensitive files
```bash
# Securely delete temporary files
python3 -m whitespace_stego.cli encode \
  --message "Secret" \
  --carrier "Carrier" \
  --output temp.txt

# Use the file
python3 -m whitespace_stego.cli decode --carrier-file temp.txt

# Securely delete
shred -u temp.txt
```

## 📝 Integration Examples

### With email clients
```bash
# Create an email with hidden content
python3 -m whitespace_stego.cli encode \
  --message "Secret meeting at 2 PM" \
  --carrier "Hi John, here's the quarterly report as requested..." \
  --output email_content.txt

# Send via email client
mail -s "Quarterly Report" john@company.com < email_content.txt
```

### With chat applications
```bash
# Quick encode for chat
python3 -m whitespace_stego.cli encode \
  --message "Emergency: Server down" \
  --carrier "Hey, how's it going? Just checking in." \
  --output -
```

These examples demonstrate the versatility and practical applications of the whitespace steganography CLI in various real-world scenarios. 