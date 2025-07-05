# Comprehensive Security and Edge Case Test Report

## Summary
- **Total Tests**: 180
- **Passed**: 128 (71.1%)
- **Failed**: 26 (14.4%)
- **Errors**: 26 (14.4%)

## Implementation Comparison
| Implementation | Passed | Failed | Errors | Success Rate |
|----------------|--------|--------|--------|--------------|
| cpp | 5 | 21 | 4 | 16.7% |
| c | 25 | 1 | 4 | 83.3% |
| go | 25 | 1 | 4 | 83.3% |
| python_core | 24 | 2 | 4 | 80.0% |
| python_rust | 24 | 0 | 6 | 80.0% |
| python_c | 25 | 1 | 4 | 83.3% |

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
- **python_core**: ❌ FAIL - Python test failed:  (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.05s)
- **python_c**: ❌ FAIL - Python test failed:  (0.05s)

### Empty carrier
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Single character
- **cpp**: ✅ PASS (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Single character carrier
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Very long message
- **cpp**: ✅ PASS (0.03s)
- **c**: ❌ FAIL - Encode failed: *** buffer overflow detected ***: terminated
 (0.14s)
- **go**: ✅ PASS (0.11s)
- **python_core**: ✅ PASS (0.32s)
- **python_rust**: ✅ PASS (8.04s)
- **python_c**: ✅ PASS (0.08s)

### Very long carrier
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.01s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.75s)
- **python_c**: ✅ PASS (0.05s)

### Null bytes in message
- **cpp**: ❌ FAIL (0.01s)
- **c**: ❌ FAIL (0.01s)
- **go**: ❌ FAIL - Encode failed: embedded null byte (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Null bytes in carrier
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_rust**: ❌ FAIL - Python test failed: embedded null byte (0.00s)
- **python_c**: ❌ FAIL - Python test failed: embedded null byte (0.00s)

### Emoji
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Combining characters
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Right-to-left text
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Zero-width characters
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Surrogate pairs
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Memory exhaustion attempt
- **cpp**: ✅ PASS - Encode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  Input too large: potential memory exhaustion attack
 (0.13s)
- **c**: ❌ FAIL - Encode failed: *** buffer overflow detected ***: terminated
 (0.38s)
- **go**: ❌ FAIL (1.00s)
- **python_core**: ❌ FAIL (2.95s)
- **python_rust**: ❌ FAIL - Python test failed: Command timed out (30.05s)
- **python_c**: ❌ FAIL (0.43s)

### Memory exhaustion carrier
- **cpp**: ❌ FAIL (0.02s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.02s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (7.41s)
- **python_c**: ✅ PASS (0.06s)

### Malicious UTF-8
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Control characters
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Long password
- **cpp**: ❌ FAIL - Decode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  No valid messages found
 (0.11s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Empty password
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Message with markers
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Carrier with markers
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ❌ FAIL - Decode failed: Error decoding message: no valid messages found in carrier text
 (0.00s)
- **python_core**: ❌ FAIL (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Mixed encoding
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Special whitespace
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)

### Medium message
- **cpp**: ✅ PASS (0.02s)
- **c**: ✅ PASS (0.02s)
- **go**: ✅ PASS (0.06s)
- **python_core**: ✅ PASS (0.19s)
- **python_rust**: ✅ PASS (4.23s)
- **python_c**: ✅ PASS (0.06s)

### Large message
- **cpp**: ✅ PASS (0.06s)
- **c**: ✅ PASS (0.05s)
- **go**: ✅ PASS (0.20s)
- **python_core**: ✅ PASS (0.60s)
- **python_rust**: ✅ PASS (16.72s)
- **python_c**: ✅ PASS (0.11s)

### Special chars password
- **cpp**: ❌ FAIL - Decode failed: terminate called after throwing an instance of 'std::runtime_error'
  what():  No valid messages found
 (0.12s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Empty message encrypted
- **cpp**: ❌ FAIL - Encode failed: No message provided.
 (0.00s)
- **c**: ❌ FAIL - Encode failed: 🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!
 (0.00s)
- **go**: ❌ FAIL - [Errno 32] Broken pipe
- **python_core**: ❌ FAIL - Python test failed:  (0.05s)
- **python_rust**: ❌ FAIL - Python test failed:  (0.05s)
- **python_c**: ❌ FAIL - Python test failed:  (0.05s)

## Unicode Tests

### Basic Unicode
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

### Unicode password
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.05s)
- **python_rust**: ✅ PASS (0.06s)
- **python_c**: ✅ PASS (0.05s)

## Encryption Tests

### Simple encryption
- **cpp**: ❌ FAIL (0.01s)
- **c**: ✅ PASS (0.01s)
- **go**: ✅ PASS (0.00s)
- **python_core**: ✅ PASS (0.06s)
- **python_rust**: ✅ PASS (0.05s)
- **python_c**: ✅ PASS (0.05s)
