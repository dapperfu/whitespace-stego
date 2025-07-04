# Scripts

This directory contains utility scripts for testing, benchmarking, and development.

## Test Scripts

- **test_scripts/** - Cross-implementation test scripts
  - `comprehensive_test.sh` - Comprehensive test suite
  - `test_cross_roundtrip.sh` - Cross-implementation roundtrip tests
  - `test_standalone_binaries.sh` - Standalone binary tests

## Benchmark Scripts

- **benchmark_all_implementations.py** - Performance comparison of all implementations
- **quick_benchmark.py** - Quick performance tests

## Development Scripts

- **isolate_test.py** - Isolated test runner
- **whitespace_stego_main.py** - Main entry point for development
- **pytest_md_report.py** - Generate markdown test reports
- **run_coverage.py** - Coverage report generation
- **generate_markdown_report.py** - Documentation generation

## Usage

Most scripts can be run directly:

```bash
# Run benchmarks
python scripts/benchmark_all_implementations.py

# Run comprehensive tests
bash scripts/test_scripts/comprehensive_test.sh

# Generate coverage reports
python scripts/run_coverage.py
``` 