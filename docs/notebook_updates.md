# Notebook Updates for Current Codebase

## Overview
The Jupyter notebooks in this project are mostly up-to-date with the current codebase, but there are a few minor updates that could be made to better reflect the current state of the project.

## Current Notebook Status

### whitespace_stego_example.ipynb
- ✅ Correctly imports and uses the core module
- ✅ Demonstrates basic encoding/decoding functionality
- ✅ Shows password protection features
- ✅ Includes error handling examples
- ✅ Contains performance analysis
- ✅ Shows real-world applications
- ⚠️ Could add CLI usage examples
- ⚠️ Could demonstrate extract_encoded function

### whitespace_stego_backends_demo.ipynb
- ✅ Correctly demonstrates Python vs Rust backend comparison
- ✅ Shows cross-backend compatibility
- ✅ Includes performance comparisons
- ✅ Tests Unicode and special character handling
- ✅ Demonstrates password protection across backends
- ⚠️ Could mention C backend reference in CLI

## Recommended Updates

### 1. Add CLI Usage Examples to whitespace_stego_example.ipynb

Add a new cell after the installation section:

```python
## CLI Usage Examples

The library provides a command-line interface for easy integration into scripts and workflows.

# Example of CLI usage (this would be run in terminal)
print("=== CLI Usage Examples ===")
print()

print("1. Basic encoding:")
print("   python -m whitespace_stego.cli encode \\")
print("     --message 'Secret message' \\")
print("     --carrier 'Hello world!' \\")
print("     --output encoded.txt")
print()

print("2. Using different backends:")
print("   python -m whitespace_stego.cli --backend python encode \\")
print("     --message 'Secret message' \\")
print("     --carrier 'Hello world!' \\")
print("     --output encoded.txt")
print()

print("   python -m whitespace_stego.cli --backend rust encode \\")
print("     --message 'Secret message' \\")
print("     --carrier 'Hello world!' \\")
print("     --output encoded.txt")
print()

print("3. File-based operations:")
print("   python -m whitespace_stego.cli encode \\")
print("     --message-file message.txt \\")
print("     --carrier-file carrier.txt \\")
print("     --output encoded.txt")
```

### 2. Add extract_encoded Function Demonstration

Add a new cell after the password protection section:

```python
## Extracting Encoded Messages

The library provides a function to extract the encoded message and remaining carrier text separately.

# Example: Using extract_encoded function
message = "This is a hidden message"
carrier = "This is the carrier text that will contain the hidden message."

# Encode the message
encoded_carrier = core.encode(message, carrier)

print("Original carrier:")
print(f"'{carrier}'")
print()

print("Hidden message:")
print(f"'{message}'")
print()

# Extract the encoded message and remaining carrier
encoded_part, remaining_carrier = core.extract_encoded(encoded_carrier)

print("Extracted encoded part:")
print(f"'{encoded_part}'")
print(f"Length: {len(encoded_part)} characters")
print()

print("Remaining carrier text:")
print(f"'{remaining_carrier}'")
print()

# Verify we can reconstruct the original
reconstructed = remaining_carrier[:1] + encoded_part + remaining_carrier[1:]
print(f"✅ Reconstruction successful: {encoded_carrier == reconstructed}")
```

### 3. Update Backend Availability Information

Add a note about backend availability in both notebooks:

```python
# Note about backend availability
print("=== Backend Availability ===")
print()

print("✅ Python backend: Always available")
print("✅ Rust backend: Available when whitespace_stego_backend is installed")
print("⚠️  C backend: Referenced in CLI but not yet implemented")
print()

print("Note: To use the Rust backend, ensure the whitespace_stego_backend")
print("package is installed and available in your Python path.")
```

### 4. Update Conclusion Section

Update the conclusion in whitespace_stego_example.ipynb to mention CLI and multi-backend support:

```markdown
### Key Takeaways:

1. **Basic Functionality**: The library provides simple `encode()` and `decode()` functions for hiding messages in text
2. **Password Protection**: Optional encryption using Fernet (AES-128) for additional security
3. **Flexible Usage**: Can embed messages in carrier text or use standalone encoded strings
4. **Error Handling**: Robust error handling for various edge cases
5. **Practical Applications**: Useful for digital watermarking, secure communication, and document verification
6. **CLI Interface**: Command-line interface for easy integration into scripts and workflows
7. **Multi-backend Support**: Support for both Python and Rust backends

### Best Practices:

- Always use strong passwords for sensitive messages
- Be aware that zero-width characters can be detected by security software
- Consider the legal and ethical implications of steganography
- Test thoroughly in your specific use case
- Use the CLI for batch processing and automation
```

## Implementation Notes

1. The notebooks are currently functional and demonstrate the core functionality correctly
2. The main updates are to add CLI usage examples and demonstrate the extract_encoded function
3. The C backend is referenced in the CLI code but not yet implemented
4. The Rust backend requires proper installation to be available

## Testing the Updates

After making these updates, test the notebooks by:

1. Running all cells in whitespace_stego_example.ipynb
2. Running all cells in whitespace_stego_backends_demo.ipynb
3. Verifying that the CLI examples work when run in a terminal
4. Checking that the extract_encoded function works correctly

## Conclusion

The notebooks are already quite comprehensive and up-to-date. The suggested updates would add CLI usage examples and demonstrate additional functionality, making them even more useful for users learning about the library. 