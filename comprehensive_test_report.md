# Comprehensive Security and Edge Case Test Report

## Summary
- **Total Tests**: 180
- **Passed**: 112 (62.2%)
- **Failed**: 3 (1.7%)
- **Errors**: 65 (36.1%)

## Implementation Comparison
| Implementation | Passed | Failed | Errors | Success Rate |
|----------------|--------|--------|--------|--------------|
| cpp | 5 | 1 | 24 | 16.7% |
| c | 25 | 1 | 4 | 83.3% |
| go | 24 | 0 | 6 | 80.0% |
| python_core | 19 | 1 | 10 | 63.3% |
| python_rust | 19 | 0 | 11 | 63.3% |
| python_c | 20 | 0 | 10 | 66.7% |

## General Tests

### Empty message
- **cpp**: ❌ FAIL - Encode failed: No message provided.
 (0.00s)
- **c**: ❌ FAIL - Encode failed: 🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!
 (0.00s)
- **go**: ❌ FAIL - Encode failed: Error: either -m/-message or -mf/-message-file is required
  -carrier-file string
    	Carrier file path
  -cf string
    	Carrier file path
  -m string
    	Message to encode
  -message string
    	Message to encode
  -message-file string
    	Message file path
  -mf string
    	Message file path
  -o string
    	Output file path
  -output string
    	Output file path
  -p string
    	Password for encryption
  -password string
    	Password for encryption
 (0.00s)
- **python_core**: ❌ FAIL - Python test failed:  (0.06s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.06s)
- **python_c**: ❌ FAIL - Python test failed:  (0.06s)

### Empty carrier
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Single character
- **cpp**: ✅ PASS (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Single character carrier
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Very long message
- **cpp**: ✅ PASS (0.04s)
- **c**: ❌ FAIL - Encode failed: *** buffer overflow detected ***: terminated
 (0.16s)
- **go**: ✅ PASS (0.12s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)

### Very long carrier
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.01s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)

### Null bytes in message
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ❌ FAIL (0.01s)
- **go**: ❌ FAIL - Encode failed: embedded null byte (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Null bytes in carrier
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Emoji
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Combining characters
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0x80 in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Right-to-left text
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xc0 in position 4: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Zero-width characters
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Surrogate pairs
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Memory exhaustion attempt
- **cpp**: ✅ PASS - Encode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  Input too large: potential memory exhaustion attack
 (0.14s)
- **c**: ❌ FAIL - Encode failed: *** buffer overflow detected ***: terminated
 (0.42s)
- **go**: ❌ FAIL - Encode failed: [Errno 7] Argument list too long: './implementations/go/bin/whitespace-stego-go' (0.00s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.01s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.01s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.01s)

### Memory exhaustion carrier
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.02s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.03s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)

### Malicious UTF-8
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Control characters
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Long password
- **cpp**: ❌ FAIL - Decode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  No valid messages found
 (0.13s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Empty password
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Message with markers
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Carrier with markers
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xac in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.00s)
- **go**: ❌ FAIL - Decode failed: Error decoding message: no valid messages found in carrier text
 (0.00s)
- **python_core**: ❌ FAIL (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Mixed encoding
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Special whitespace
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Medium message
- **cpp**: ✅ PASS (0.02s)
- **c**: ✅ PASS (0.02s)
- **go**: ✅ PASS (0.06s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)

### Large message
- **cpp**: ✅ PASS (0.07s)
- **c**: ✅ PASS (0.07s)
- **go**: ❌ FAIL - Encode failed: [Errno 7] Argument list too long: './implementations/go/bin/whitespace-stego-go' (0.00s)
- **python_core**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)
- **python_c**: ❌ FAIL - Python test failed: [Errno 7] Argument list too long: 'python3' (0.00s)

### Special chars password
- **cpp**: ❌ FAIL - Decode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  No valid messages found
 (0.14s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Empty message encrypted
- **cpp**: ❌ FAIL - Encode failed: No message provided.
 (0.00s)
- **c**: ❌ FAIL - Encode failed: 🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!
 (0.00s)
- **go**: ❌ FAIL - Encode failed: Error: either -m/-message or -mf/-message-file is required
  -carrier-file string
    	Carrier file path
  -cf string
    	Carrier file path
  -m string
    	Message to encode
  -message string
    	Message to encode
  -message-file string
    	Message file path
  -mf string
    	Message file path
  -o string
    	Output file path
  -output string
    	Output file path
  -p string
    	Password for encryption
  -password string
    	Password for encryption
 (0.00s)
- **python_core**: ❌ FAIL - Python test failed:  (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.05s)
- **python_c**: ❌ FAIL - Python test failed:  (0.05s)

## Unicode Tests

### Basic Unicode
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xad in position 2: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Unicode password
- **cpp**: ❌ FAIL - 'utf-8' codec can't decode byte 0xf6 in position 4: invalid start byte (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

## Encryption Tests

### Simple encryption
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)
