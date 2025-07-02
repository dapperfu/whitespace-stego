# CLI Cross-Implementation Test Suite

This directory contains comprehensive shell scripts for testing all CLI implementations of the whitespace steganography project.

## Test Scripts

### 1. `test_cli_quick.sh` - Quick Verification
A fast test to verify that all CLI tools are working correctly.

**Usage:**
```bash
./test_cli_quick.sh
```

**What it tests:**
- Basic roundtrip functionality for each implementation
- Verifies CLI tools are available and working
- Quick sanity check before running comprehensive tests

### 2. `test_cli_basic.sh` - Basic Test Suite
A focused test suite that covers key functionality.

**Usage:**
```bash
./test_cli_basic.sh
```

**What it tests:**
- Same-implementation roundtrips for all CLI tools
- Key test cases: ASCII, Unicode, Emoji, Special characters, Newlines
- Error conditions (empty messages)
- Wrong password scenarios
- No password scenarios

### 3. `test_cli_comprehensive.sh` - Full Permutation Test
A comprehensive test that covers all permutations of messages, carriers, and passwords.

**Usage:**
```bash
./test_cli_comprehensive.sh
```

**What it tests:**
- Full permutation testing across all implementations
- 15 different message types (ASCII, Unicode, Emoji, etc.)
- 15 different carrier types
- 13 different password types
- Error conditions and edge cases
- Cross-implementation compatibility (limited)

## CLI Implementations Tested

### 1. Python CLI
```bash
python -m whitespace_stego.cli --backend python encode/decode
```

### 2. Rust CLI
```bash
./whitespace-stego-rs encode/decode
```

### 3. C CLI
```bash
./whitespace-stego-c encode/decode
```

## Test Data Coverage

### Messages Tested
- ASCII text
- ASCII with punctuation
- Cyrillic (Привет мир)
- Chinese (你好世界)
- Japanese (こんにちは世界)
- Korean (안녕하세요 세계)
- Arabic (مرحبا بالعالم)
- Hebrew (שלום עולם)
- Hindi (नमस्ते दुनिया)
- ASCII with emoji (Hello 🌍 World)
- Emoji heavy (🚀 Rocket to the moon! 🚀)
- Mixed emoji and text
- Greek Unicode (αβγδε)
- Special characters (!@#$%^&*())
- Multi-line text
- Very long text with emojis

### Carriers Tested
- All the same types as messages
- Various lengths and complexity levels
- Unicode and emoji support

### Passwords Tested
- Basic passwords
- Alphanumeric passwords
- Special character passwords
- Unicode passwords (Cyrillic, Chinese, Japanese, etc.)
- Emoji passwords
- Empty passwords

## Test Results

### Expected Behavior
- **Same-implementation roundtrips**: Should work 100%
- **Cross-implementation compatibility**: Limited due to different encoding schemes
- **Error handling**: Empty messages should be rejected (except Rust)
- **Password protection**: Wrong passwords should be rejected

### Known Limitations
1. **Cross-implementation compatibility**: Different implementations use different encoding schemes, so cross-implementation tests may fail
2. **Rust empty message handling**: Rust implementation accepts empty messages while others reject them
3. **Encoding scheme differences**: Each implementation may use slightly different whitespace encoding constants

## Running the Tests

### Prerequisites
1. All CLI tools must be built and available:
   - `./whitespace-stego-rs` (Rust CLI)
   - `./whitespace-stego-c` (C CLI)
   - `python -m whitespace_stego.cli` (Python CLI)

2. Python environment with the whitespace_stego package installed

### Quick Start
```bash
# Make scripts executable
chmod +x test_cli_*.sh

# Run quick test first
./test_cli_quick.sh

# Run basic test suite
./test_cli_basic.sh

# Run comprehensive test (may take a while)
./test_cli_comprehensive.sh
```

### Expected Output
- ✅ Green checkmarks for passing tests
- ❌ Red X marks for failing tests
- ℹ️ Blue info messages for test progress
- ⚠️ Yellow warnings for expected limitations

## Test Statistics

### Comprehensive Test Coverage
- **Total test cases**: ~3,000+ permutations
- **Message types**: 15 different types
- **Carrier types**: 15 different types  
- **Password types**: 13 different types
- **Implementations**: 3 (Python, Rust, C)
- **Test categories**: Same-implementation, Error handling, Password protection

### Performance
- **Quick test**: ~30 seconds
- **Basic test**: ~2-3 minutes
- **Comprehensive test**: ~10-15 minutes

## Troubleshooting

### Common Issues

1. **CLI tool not found**
   - Ensure all tools are built: `make` in respective directories
   - Check file permissions: `chmod +x whitespace-stego-*`

2. **Python module not found**
   - Install the package: `pip install -e .` in the Python directory
   - Activate virtual environment if using one

3. **Permission denied**
   - Make scripts executable: `chmod +x test_cli_*.sh`

4. **Cross-implementation failures**
   - This is expected behavior due to different encoding schemes
   - Focus on same-implementation roundtrips for validation

### Debug Mode
To see detailed CLI output, remove `2>/dev/null` from the script functions.

## Contributing

When adding new CLI implementations:

1. Add the new implementation to the `CLI_IMPLS` array
2. Add the appropriate command construction in `run_cli_encode()` and `run_cli_decode()`
3. Test with the quick script first
4. Run the comprehensive test suite
5. Update this README with any new limitations or behaviors

## Test Philosophy

These tests are designed to:

1. **Validate functionality**: Ensure each implementation works correctly
2. **Test edge cases**: Handle Unicode, emoji, special characters, etc.
3. **Verify security**: Password protection and error handling
4. **Document behavior**: Clear expectations for each implementation
5. **Enable regression testing**: Catch breaking changes in implementations

The focus is on **same-implementation roundtrips** rather than cross-implementation compatibility, as different implementations may use different encoding schemes while still being functionally correct. 