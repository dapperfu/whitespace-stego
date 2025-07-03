# Whitespace Steganography Benchmarks

This document provides comprehensive performance benchmarks for all whitespace steganography implementations.

## Overview

Two benchmarking scripts are available for performance testing:

1. **Comprehensive Benchmark** (`benchmark_all_implementations.py`) - 100 iterations, detailed analysis
2. **Quick Benchmark** (`quick_benchmark.py`) - 10 iterations, fast comparison

## Performance Results

### Comprehensive Benchmark Results (100 iterations each)

**Encode Performance:**
| Implementation | Backend | Throughput (ops/sec) | Avg Time (ms) | Std Dev (ms) |
|----------------|---------|---------------------|---------------|--------------|
| go-standalone | standalone | 617.1 | 1.62 | 0.23 |
| c-standalone | standalone | 341.2 | 2.93 | 0.27 |
| rust-standalone | standalone | 312.3 | 3.20 | 0.26 |
| python-cli-c | c | 12.9 | 77.43 | 7.22 |
| python-cli-rust | rust | 12.5 | 79.79 | 7.97 |
| python-cli-python | python | 11.8 | 84.54 | 8.57 |
| python-standalone | standalone | 3.5 | 287.06 | 36.93 |

**Decode Performance:**
| Implementation | Backend | Throughput (ops/sec) | Avg Time (ms) | Std Dev (ms) |
|----------------|---------|---------------------|---------------|--------------|
| go-standalone | standalone | 640.2 | 1.56 | 0.24 |
| c-standalone | standalone | 349.2 | 2.86 | 0.25 |
| rust-standalone | standalone | 91.2 | 10.97 | 1.34 |
| python-cli-c | c | 13.0 | 76.65 | 5.01 |
| python-cli-python | python | 12.3 | 81.54 | 16.32 |
| python-cli-rust | rust | 5.1 | 197.74 | 20.98 |
| python-standalone | standalone | 3.8 | 262.38 | 13.73 |

### Quick Benchmark Results (10 iterations each)

**Encode Performance:**
| Implementation | Throughput (ops/sec) | Avg Time (ms) |
|----------------|---------------------|---------------|
| go | 576.0 | 1.7 |
| c | 324.0 | 3.1 |
| rust | 293.6 | 3.4 |
| python | 3.9 | 259.2 |

**Decode Performance:**
| Implementation | Throughput (ops/sec) | Avg Time (ms) |
|----------------|---------------------|---------------|
| go | 583.8 | 1.7 |
| c | 333.8 | 3.0 |
| rust | 133.1 | 7.5 |
| python | 3.8 | 262.8 |

## Key Findings

### Performance Rankings

1. **Go Implementation** - Fastest by significant margin
   - Encode: 576-617 ops/sec
   - Decode: 584-640 ops/sec
   - ~1.8x faster than C implementation

2. **C Implementation** - Second fastest, very consistent
   - Encode: 324-341 ops/sec
   - Decode: 334-349 ops/sec
   - Low standard deviation indicates stable performance

3. **Rust Implementation** - Third fastest, decode performance issue
   - Encode: 294-312 ops/sec
   - Decode: 91-133 ops/sec (significant drop from encode)
   - Decode performance ~3x slower than encode

4. **Python Implementations** - Significantly slower
   - Standalone: 3.5-3.9 ops/sec
   - CLI with backends: 5.1-13.0 ops/sec
   - 150-200x slower than Go implementation

### Performance Ratios (Relative to Fastest)

**Encode Performance Ratios:**
- go-standalone: 1.00x (baseline)
- c-standalone: 0.55x
- rust-standalone: 0.51x
- python-cli-c: 0.02x
- python-cli-rust: 0.02x
- python-cli-python: 0.02x
- python-standalone: 0.01x

**Decode Performance Ratios:**
- go-standalone: 1.00x (baseline)
- c-standalone: 0.55x
- rust-standalone: 0.14x
- python-cli-c: 0.02x
- python-cli-python: 0.02x
- python-cli-rust: 0.01x
- python-standalone: 0.01x

## Test Configuration

### Comprehensive Benchmark
- **Iterations**: 100 per implementation
- **Message length**: 1,056 characters
- **Carrier length**: 500 characters
- **Runtime**: ~2 minutes
- **Features**: Standard deviation, detailed analysis, JSON output

### Quick Benchmark
- **Iterations**: 10 per implementation
- **Message length**: ~80 characters
- **Carrier length**: ~50 characters
- **Runtime**: ~5 seconds
- **Features**: Fast comparison, simple summary

## Implementation Compatibility

All implementations maintain **bit-per-bit compatibility**:
- Messages encoded with any implementation can be decoded by any other
- Cross-implementation tests confirm full compatibility
- Go implementation is fastest while maintaining compatibility

## Usage

### Running Benchmarks

```bash
# Quick performance comparison (~5 seconds)
python quick_benchmark.py

# Comprehensive analysis (~2 minutes)
python benchmark_all_implementations.py
```

### Output Files

- `benchmark_results.json` - Detailed results in JSON format
- Console output with formatted tables and rankings

## Recommendations

### For High-Performance Applications
- **Use Go implementation** for best performance
- **Use C implementation** as alternative with good performance
- **Avoid Python implementations** for performance-critical use cases

### For Development and Testing
- **Use Python CLI** with various backends for flexibility
- **Use Rust implementation** with caution (decode performance issue)
- **Use comprehensive benchmark** for detailed analysis

### For Production Systems
- **Go implementation** provides best performance/compatibility balance
- **C implementation** offers good performance with proven stability
- **Consider Python** only for prototyping or low-throughput scenarios

## Technical Notes

- All benchmarks run on Linux 6.8.0-53-generic
- Python 3.12.3 with virtual environment
- Standard deviation calculations show consistent performance
- Error handling ensures graceful failure recovery
- Temporary file cleanup for each test iteration

## Future Improvements

- Add memory usage measurements
- Include CPU utilization metrics
- Test with larger message sizes
- Add concurrent operation benchmarks
- Include encryption performance tests 