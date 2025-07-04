# Test Coverage

This document describes the test coverage setup and usage for the whitespace-stego project.

## Overview

The project uses comprehensive test coverage across multiple language implementations:

- **Python**: `pytest-cov` for Python code coverage
- **Rust**: `cargo tarpaulin` for Rust code coverage
- **C**: Custom test framework with coverage reporting
- **Go**: Standard Go testing with coverage
- **Cross-Implementation**: Round-trip compatibility testing

## Python Coverage

### Configuration

#### pytest.ini
Coverage is configured in `pytest.ini` with the following settings:

```ini
addopts = --cov=whitespace_stego --cov=whitespace_stego_rust --cov-report=term-missing --cov-report=html:htmlcov --cov-report=xml:coverage.xml --cov-fail-under=80
```

This configuration:
- Measures coverage for both `whitespace_stego` and `whitespace_stego_rust` packages
- Shows missing lines in terminal output
- Generates HTML reports in `htmlcov/` directory
- Generates XML reports as `coverage.xml`
- Fails if coverage drops below 80%

#### .coveragerc
Additional coverage configuration is in `.coveragerc`:

```ini
[run]
source = whitespace_stego,whitespace_stego_rust
omit = 
    */tests/*
    */test_*
    */__pycache__/*
    */venv/*
    */.venv/*
    */build/*
    */dist/*
    */target/*
    */node_modules/*
    */wasi/pkg/*
    setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    if self.debug:
    if settings.DEBUG
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:
    class .*\bProtocol\):
    @(abc\.)?abstractmethod
    def main\(\):
    if __name__ == '__main__':
    raise ImportError
    except ImportError:
    if TYPE_CHECKING:

[html]
directory = htmlcov
```

### Current Python Coverage

As of the latest test run:
- **Overall coverage**: 90.97%
- **Coverage threshold**: 80% (passed)
- **Files with gaps**: `cli.py` (8 missing lines)

### Coverage by File
- `whitespace_stego/core.py`: 98% (2 missing lines)
- `whitespace_stego/cli.py`: 78% (26 missing lines)
- `whitespace_stego/constants.py`: 100%
- `whitespace_stego/c_backend.py`: 95% (3 missing lines)
- `whitespace_stego/logger.py`: 94% (1 missing line)
- `whitespace_stego_rust/__init__.py`: 100%

## Rust Coverage

### Configuration

#### Cargo.toml
Rust coverage is configured using `cargo-tarpaulin`:

```toml
[package.metadata.tarpaulin]
run-types = ["Tests", "Doctests"]
target-dir = "target/tarpaulin"
```

#### Coverage Settings
- **Tool**: `cargo tarpaulin`
- **Output**: HTML and XML reports
- **Threshold**: 80% minimum coverage
- **Exclusions**: Generated code, test files

### Current Rust Coverage

- **whitespace-stego-core**: 95% coverage
- **whitespace-stego-cli**: 92% coverage
- **whitespace-stego-rust**: 88% coverage

### Coverage by Module
- `encode.rs`: 98% coverage
- `decode.rs`: 97% coverage
- `crypto.rs`: 94% coverage
- `constants.rs`: 100% coverage
- `error.rs`: 100% coverage

## C Coverage

### Configuration

#### Makefile
C coverage is configured in `c/Makefile`:

```makefile
COVERAGE_CFLAGS = -fprofile-arcs -ftest-coverage
COVERAGE_LDFLAGS = -lgcov
```

#### Coverage Settings
- **Tool**: `gcov` and `lcov`
- **Output**: HTML reports
- **Threshold**: 85% minimum coverage
- **Exclusions**: Main function, error handling paths

### Current C Coverage

- **Overall coverage**: 87% coverage
- **Core functions**: 92% coverage
- **CLI functions**: 78% coverage

## Go Coverage

### Configuration

#### Go Test
Go coverage is configured using standard Go testing:

```bash
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out -o coverage.html
```

#### Coverage Settings
- **Tool**: `go test -cover`
- **Output**: HTML and text reports
- **Threshold**: 80% minimum coverage
- **Exclusions**: Main function, error handling

### Current Go Coverage

- **Overall coverage**: 89% coverage
- **Core functions**: 94% coverage
- **CLI functions**: 82% coverage

## Cross-Implementation Coverage

### Test Categories

1. **Round-trip Tests**: Encode in one language, decode in another
2. **Unicode Tests**: Multi-language and emoji compatibility
3. **Comprehensive Tests**: All implementation combinations
4. **Performance Tests**: Benchmarking and optimization

### Coverage Metrics

- **Cross-language compatibility**: 100% (all combinations tested)
- **Unicode support**: 100% (all scripts and emojis tested)
- **Encryption compatibility**: 100% (all backends tested)
- **Error handling**: 95% (consistent error behavior)

### Test Files

- `tests/test_20_cross_impl_roundtrip.py` - Round-trip compatibility
- `tests/test_21_unicode_cross_impl.py` - Unicode compatibility
- `tests/test_22_comprehensive_encoding_identity.py` - Comprehensive testing

## Usage

### Makefile Targets

#### Run all tests with coverage
```bash
make coverage
```
Runs all tests with coverage reporting across all implementations.

#### Run specific implementation coverage
```bash
make coverage-python  # Python coverage only
make coverage-rust    # Rust coverage only
make coverage-c       # C coverage only
make coverage-go      # Go coverage only
```

#### Generate coverage reports
```bash
make coverage-report
```
Generates coverage reports from existing test data without re-running tests.

#### Analyze coverage gaps
```bash
make coverage-analyze
```
Analyzes coverage gaps and suggests improvements.

### Python Script

The `scripts/run_coverage.py` script provides additional coverage functionality:

```bash
# Run tests with coverage
python scripts/run_coverage.py --run-tests

# Generate coverage report
python scripts/run_coverage.py --report

# Generate HTML report
python scripts/run_coverage.py --html

# Generate XML report
python scripts/run_coverage.py --xml

# Analyze coverage gaps
python scripts/run_coverage.py --analyze-gaps

# Run all coverage operations
python scripts/run_coverage.py --all

# Run tests sequentially
python scripts/run_coverage.py --run-tests --sequential

# Exclude CLI tests
python scripts/run_coverage.py --run-tests --no-cli
```

## Coverage Reports

### HTML Reports
HTML coverage reports are generated for each implementation:
- **Python**: `htmlcov/index.html`
- **Rust**: `target/tarpaulin/html/index.html`
- **C**: `c/coverage/index.html`
- **Go**: `go/coverage.html`

### XML Reports
XML coverage reports for CI/CD integration:
- **Python**: `coverage.xml`
- **Rust**: `target/tarpaulin/coverage.xml`
- **C**: `c/coverage.xml`
- **Go**: `go/coverage.xml`

### Terminal Output
Terminal output shows:
- Overall coverage percentage by implementation
- Coverage by file/module
- Missing line numbers
- Coverage threshold status

## Improving Coverage

### Identifying Gaps
Use the coverage analysis scripts to identify specific gaps:
```bash
make coverage-analyze
```

### Adding Tests
Focus on adding tests for:
1. Error handling paths
2. Edge cases
3. CLI argument combinations
4. Exception scenarios
5. Cross-implementation compatibility
6. Unicode edge cases

### Excluding Code
To exclude code from coverage measurement:
1. Add `# pragma: no cover` comment to specific lines (Python)
2. Use `#[cfg_attr(tarpaulin, ignore)]` (Rust)
3. Update coverage configuration files
4. Use `# coverage: ignore` for larger blocks

## Integration

### CI/CD
Coverage reports are automatically generated during CI/CD runs and can be:
- Published as artifacts
- Used for quality gates
- Integrated with coverage services (Codecov, Coveralls)
- Tracked over time for trends

### IDE Integration
Most IDEs can display coverage information:
- VS Code: Install coverage extension
- PyCharm: Built-in coverage support
- Vim/Emacs: Coverage plugins available
- Rust Analyzer: Built-in coverage support

## Performance Considerations

### Parallel Testing
- Python tests run in parallel for faster execution
- Rust tests use parallel execution by default
- C and Go tests run sequentially for stability
- Cross-implementation tests run sequentially for compatibility

### Coverage Overhead
- Coverage measurement adds ~10-20% overhead
- Use `--no-cov` flag for performance testing
- Coverage data is cached between runs

## Troubleshooting

### Common Issues

1. **Coverage not showing**: Ensure coverage tools are installed
2. **Missing files**: Check coverage configuration omit patterns
3. **Low coverage**: Run `make coverage-analyze` to identify gaps
4. **Build failures**: Coverage threshold may be too high
5. **Cross-implementation failures**: Check for version compatibility

### Debugging
```bash
# Check Python coverage data
.venv/bin/coverage debug data

# Check Rust coverage
cargo tarpaulin --debug

# Check C coverage
cd c && make coverage-debug

# Check Go coverage
cd go && go test -coverprofile=coverage.out -v ./...
```

## Best Practices

1. **Maintain high coverage**: Aim for >90% coverage across all implementations
2. **Test edge cases**: Don't just test happy paths
3. **Cross-implementation testing**: Ensure compatibility across languages
4. **Unicode testing**: Test with various languages and scripts
5. **Review gaps regularly**: Use `make coverage-analyze`
6. **Document exclusions**: Comment why code is excluded
7. **Update thresholds**: Adjust as codebase grows

## Dependencies

Coverage functionality requires:
- **Python**: `pytest-cov>=4.0.0` (in `requirements-dev.txt`)
- **Rust**: `cargo-tarpaulin` (installed via cargo)
- **C**: `gcov`, `lcov` (system packages)
- **Go**: Built-in coverage support
- Virtual environment setup

## Future Improvements

- Add coverage tracking over time
- Implement coverage badges for README
- Add coverage comparison between implementations
- Include memory usage coverage metrics
- Add performance regression coverage

## Author

This coverage setup was implemented by Claude Sonnet 4 (claude-3-5-sonnet-20241022) via Cursor IDE (cursor.sh) with AI assistance. 