# Whitespace Steganography Benchmarks

This document provides comprehensive performance benchmarks for all whitespace steganography implementations.

## Overview

Multiple benchmarking scripts are available for performance testing:

1. **Comprehensive Benchmark** (`benchmark_all_implementations.py`) - 100 iterations, detailed analysis
2. **Quick Benchmark** (`quick_benchmark.py`) - 10 iterations, fast comparison
3. **Cross-Implementation Tests** - Round-trip compatibility testing
4. **Unicode Benchmark Tests** - Multi-language and emoji performance

## Performance Results

### CLI Benchmark Results (2024-12-19)

**Encode Performance:**
| Implementation | Throughput (ops/sec) | Avg Time (ms) | Std Dev (ms) | Iterations |
|----------------|---------------------|---------------|--------------|------------|
| go | 265.1 | 3.77 | 0.34 | 100 |
| c | 226.5 | 4.42 | 0.34 | 100 |
| cpp | 211.5 | 4.73 | 0.41 | 100 |
| rs | 202.6 | 4.93 | 0.39 | 100 |
| c-static | 116.7 | 8.57 | 0.57 | 100 |
| py | 5.5 | 183.36 | 3.75 | 10 |
| py-c | 5.5 | 183.01 | 1.47 | 10 |
| py-rs | 5.4 | 185.70 | 2.82 | 10 |

**Decode Performance:**
| Implementation | Throughput (ops/sec) | Avg Time (ms) | Std Dev (ms) | Iterations |
|----------------|---------------------|---------------|--------------|------------|
| go | 264.6 | 3.78 | 0.37 | 100 |
| c | 224.3 | 4.46 | 0.36 | 100 |
| cpp | 212.6 | 4.70 | 0.38 | 100 |
| c-static | 115.9 | 8.63 | 0.49 | 100 |
| rs | 98.2 | 10.19 | 0.47 | 100 |
| py | 5.5 | 181.02 | 1.63 | 10 |
| py-c | 5.4 | 183.87 | 1.64 | 10 |
| py-rs | 5.3 | 189.40 | 2.45 | 10 |

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

### Rust CLI Performance (New Implementation)

**Rust CLI vs Other Implementations:**
| Implementation | Encode (ops/sec) | Decode (ops/sec) | Memory Usage |
|----------------|------------------|------------------|--------------|
| rust-cli | 298.5 | 89.3 | ~1.2MB |
| go-standalone | 617.1 | 640.2 | ~1.5MB |
| c-standalone | 341.2 | 349.2 | ~0.8MB |
| python-cli | 11.8 | 12.3 | ~15MB |

### Unicode Performance Tests

**Multi-language and Emoji Support:**
| Test Case | Implementation | Encode Time (ms) | Decode Time (ms) | Success Rate |
|-----------|----------------|------------------|------------------|--------------|
| ASCII Only | All | 1.5-3.2 | 1.6-3.0 | 100% |
| Unicode Text | All | 1.8-3.8 | 1.9-3.5 | 100% |
| Emoji Mix | All | 2.1-4.2 | 2.3-4.0 | 100% |
| RTL Languages | All | 2.5-4.8 | 2.7-4.5 | 100% |
| Combining Chars | All | 2.8-5.1 | 3.0-4.9 | 100% |

## Key Findings

### Performance Rankings

1. **Go Implementation** - Fastest by significant margin
   - Encode: 265.1 ops/sec
   - Decode: 264.6 ops/sec
   - ~1.2x faster than C implementation
   - Excellent memory efficiency

2. **C Implementation** - Second fastest, very consistent
   - Encode: 226.5 ops/sec
   - Decode: 224.3 ops/sec
   - Low standard deviation indicates stable performance
   - Minimal memory footprint

3. **C++ Implementation** - Third fastest, consistent performance
   - Encode: 211.5 ops/sec
   - Decode: 212.6 ops/sec
   - Very balanced encode/decode performance
   - Good memory efficiency

4. **Rust Implementation** - Good encode, slower decode
   - Encode: 202.6 ops/sec
   - Decode: 98.2 ops/sec (significant drop from encode)
   - Decode performance ~2x slower than encode
   - CLI implementation shows good usability

5. **C-static Implementation** - Slower than regular C
   - Encode: 116.7 ops/sec
   - Decode: 115.9 ops/sec
   - ~2x slower than regular C implementation
   - Static linking overhead

6. **Python Implementations** - Significantly slower
   - All variants: ~5.5 ops/sec (py, py-c, py-rs)
   - 50x slower than Go implementation
   - Backend selection has minimal impact on performance
   - High memory usage due to interpreter overhead

### Performance Ratios (Relative to Fastest)

**Encode Performance Ratios:**
- go: 1.00x (baseline)
- c: 0.85x
- cpp: 0.80x
- rs: 0.76x
- c-static: 0.44x
- py: 0.02x
- py-c: 0.02x
- py-rs: 0.02x

**Decode Performance Ratios:**
- go: 1.00x (baseline)
- c: 0.85x
- cpp: 0.80x
- c-static: 0.44x
- rs: 0.37x
- py: 0.02x
- py-c: 0.02x
- py-rs: 0.02x

### Cross-Implementation Compatibility

All implementations maintain **bit-per-bit compatibility**:
- Messages encoded with any implementation can be decoded by any other
- Cross-implementation tests confirm full compatibility
- Unicode support is consistent across all implementations
- Encryption compatibility maintained across all backends

## Test Configuration

### CLI Benchmark
- **Iterations**: 100 for fast implementations, 10 for slow ones
- **Message length**: ~50 characters
- **Carrier length**: ~80 characters
- **Runtime**: ~30 seconds
- **Features**: Standard deviation, detailed analysis, JSON output
- **Script**: `scripts/benchmark_cli.py`

### Quick Benchmark
- **Iterations**: 10 per implementation
- **Message length**: ~80 characters
- **Carrier length**: ~50 characters
- **Runtime**: ~5 seconds
- **Features**: Fast comparison, simple summary

### Unicode Benchmark
- **Test cases**: ASCII, Unicode, Emoji, RTL, Combining characters
- **Message types**: Various language scripts and emoji combinations
- **Success criteria**: 100% round-trip compatibility
- **Performance**: Encoding/decoding time measurement

### Cross-Implementation Tests
- **Round-trip testing**: Encode in one language, decode in another
- **All combinations**: Every implementation pair tested
- **Success rate**: 100% compatibility achieved
- **Performance**: Cross-language performance comparison

## Implementation Features

### Go Implementation
- **Performance**: Fastest overall
- **Memory**: Efficient garbage collection
- **Compatibility**: Full cross-language support
- **CLI**: Simple command-line interface
- **Deployment**: Single binary distribution

### C Implementation
- **Performance**: Second fastest
- **Memory**: Minimal footprint
- **Compatibility**: Full cross-language support
- **CLI**: File-based operations
- **Deployment**: Static binary or shared library

### Rust Implementation
- **Performance**: Good encode, slower decode
- **Memory**: Safe memory management
- **Compatibility**: Full cross-language support
- **CLI**: Advanced subcommand architecture
- **Features**: Interactive mode, progress indicators

### Python Implementation
- **Performance**: Slowest but most flexible
- **Memory**: Higher overhead
- **Compatibility**: Full cross-language support
- **CLI**: Multiple backend support
- **Features**: Jupyter integration, extensive testing

## Usage

### Running Benchmarks

```bash
# CLI performance comparison (~30 seconds)
python scripts/benchmark_cli.py

# Quick performance comparison (~5 seconds)
python quick_benchmark.py

# Comprehensive analysis (~2 minutes)
python benchmark_all_implementations.py

# Cross-implementation compatibility tests
python tests/test_20_cross_impl_roundtrip.py

# Unicode compatibility tests
python tests/test_21_unicode_cross_impl.py
```

### Output Files

- `benchmark_results.json` - Detailed results in JSON format
- `results/test_results.json` - Test results and analysis
- `results/test_summary.md` - Human-readable summary
- Console output with formatted tables and rankings

## Recommendations

### For High-Performance Applications
- **Use Go implementation** for best performance
- **Use C implementation** as alternative with good performance
- **Avoid Python implementations** for performance-critical use cases
- **Consider Rust** for encode-heavy workloads

### For Development and Testing
- **Use Python CLI** with various backends for flexibility
- **Use Rust CLI** for advanced features and good performance
- **Use comprehensive benchmark** for detailed analysis
- **Use cross-implementation tests** for compatibility verification

### For Production Systems
- **Go implementation** provides best performance/compatibility balance
- **C implementation** offers good performance with proven stability
- **Rust implementation** provides safety and advanced features
- **Consider Python** only for prototyping or low-throughput scenarios

### For Unicode-Heavy Applications
- **All implementations** support full Unicode
- **Performance impact** is minimal for Unicode text
- **Cross-language compatibility** maintained for all scripts
- **Emoji support** is consistent across implementations

## Technical Notes

- All benchmarks run on Linux 6.8.0-53-generic
- Python 3.12.3 with virtual environment
- Standard deviation calculations show consistent performance
- Error handling ensures graceful failure recovery
- Temporary file cleanup for each test iteration
- Memory usage measurements included for new implementations
- Unicode normalization handled consistently across implementations

## Future Improvements

- Add memory usage measurements for all implementations
- Include CPU utilization metrics
- Test with larger message sizes (1MB+)
- Add concurrent operation benchmarks
- Include encryption performance tests
- Add streaming performance tests
- Include WebAssembly performance benchmarks
- Add mobile platform performance testing 