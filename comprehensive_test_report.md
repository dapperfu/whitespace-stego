# Comprehensive Security and Edge Case Test Report

## Summary
- **Total Tests**: 180
- **Passed**: 128 (71.1%)
- **Failed**: 4 (2.2%)
- **Errors**: 48 (26.7%)

## Implementation Comparison
| Implementation | Passed | Failed | Errors | Success Rate |
|----------------|--------|--------|--------|--------------|
| cpp | 30 | 0 | 0 | 100.0% |
| c | 0 | 0 | 30 | 0.0% |
| go | 25 | 1 | 4 | 83.3% |
| python_core | 24 | 2 | 4 | 80.0% |
| python_rust | 24 | 0 | 6 | 80.0% |
| python_c | 25 | 1 | 4 | 83.3% |

## General Tests

### Empty message
- **cpp**: ✅ PASS - Encode failed: Message must not be empty.
 (0.00s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
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
- **python_c**: ❌ FAIL - Python test failed:  (0.06s)

### Empty carrier
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.06s)

### Single character
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Single character carrier
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Very long message
- **cpp**: ✅ PASS (0.05s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.11s)
- **python_core**: ✅ PASS (0.33s)
- **python_rust**: ✅ PASS (8.34s)
- **python_c**: ✅ PASS (0.08s)

### Very long carrier
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.01s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.81s)
- **python_c**: ✅ PASS (0.05s)

### Null bytes in message
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ❌ FAIL - Encode failed: embedded null byte (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Null bytes in carrier
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Emoji
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Combining characters
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Right-to-left text
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Zero-width characters
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Surrogate pairs
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Memory exhaustion attempt
- **cpp**: ✅ PASS - Encode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  Input too large: potential memory exhaustion attack
 (0.13s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ❌ FAIL (1.04s)
- **python_core**: ❌ FAIL (3.03s)
- **python_rust**: ❌ FAIL - Python test failed: Command timed out (30.05s)
- **python_c**: ❌ FAIL (0.45s)

### Memory exhaustion carrier
- **cpp**: ✅ PASS (0.02s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.02s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (7.84s)
- **python_c**: ✅ PASS (0.06s)

### Malicious UTF-8
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Control characters
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Long password
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Empty password
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Message with markers
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Carrier with markers
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ❌ FAIL - Decode failed: Error decoding message: no valid messages found in carrier text
 (0.00s)
- **python_core**: ❌ FAIL (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Mixed encoding
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Special whitespace
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Medium message
- **cpp**: ✅ PASS (0.02s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.06s)
- **python_core**: ✅ PASS (0.19s)
- **python_rust**: ✅ PASS (4.55s)
- **python_c**: ✅ PASS (0.07s)

### Large message
- **cpp**: ✅ PASS (0.08s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.20s)
- **python_core**: ✅ PASS (0.62s)
- **python_rust**: ✅ PASS (17.82s)
- **python_c**: ✅ PASS (0.12s)

### Special chars password
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Empty message encrypted
- **cpp**: ✅ PASS - Encode failed: Message must not be empty.
 (0.00s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
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
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Unicode password
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

## Encryption Tests

### Simple encryption
- **cpp**: ✅ PASS (0.01s)
- **c**: ❌ FAIL - Encode failed: [Errno 2] No such file or directory: './implementations/c/bin/whitespace-stego-c' (0.00s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)
