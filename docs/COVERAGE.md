# Test Coverage

This document describes the test coverage setup and usage for the whitespace-stego project.

## Overview

The project uses `pytest-cov` to measure test coverage of the Python code. Coverage reports are generated in multiple formats:

- **Terminal output**: Shows coverage percentage and missing lines
- **HTML report**: Interactive web-based coverage report
- **XML report**: Machine-readable coverage data

## Configuration

### pytest.ini
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

### .coveragerc
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

## Usage

### Makefile Targets

#### Run tests with coverage
```bash
make coverage
```
Runs all tests with coverage reporting, excluding CLI and WASM tests for parallel execution.

#### Generate coverage report from existing data
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

### HTML Report
The HTML coverage report is generated in `htmlcov/index.html` and provides:
- Interactive file browser
- Line-by-line coverage highlighting
- Coverage statistics by file and function
- Missing line indicators

### XML Report
The XML coverage report (`coverage.xml`) can be used by:
- CI/CD systems
- Coverage analysis tools
- IDE plugins

### Terminal Output
The terminal output shows:
- Overall coverage percentage
- Coverage by file
- Missing line numbers
- Coverage threshold status

## Current Coverage

As of the latest test run:
- **Overall coverage**: 90.97%
- **Coverage threshold**: 80% (passed)
- **Files with gaps**: `cli.py` (8 missing lines)

### Coverage by File
- `whitespace_stego/core.py`: 98% (2 missing lines)
- `whitespace_stego/cli.py`: 78% (26 missing lines)
- `whitespace_stego/decode.py`: 100%
- `whitespace_stego/encode.py`: 100%
- `whitespace_stego/logger.py`: 94% (1 missing line)
- `whitespace_stego_rust/__init__.py`: 100%

## Improving Coverage

### Identifying Gaps
Use the coverage analysis script to identify specific gaps:
```bash
make coverage-analyze
```

### Adding Tests
Focus on adding tests for:
1. Error handling paths
2. Edge cases
3. CLI argument combinations
4. Exception scenarios

### Excluding Code
To exclude code from coverage measurement:
1. Add `# pragma: no cover` comment to specific lines
2. Update `.coveragerc` exclude patterns
3. Use `# coverage: ignore` for larger blocks

## Integration

### CI/CD
Coverage reports are automatically generated during CI/CD runs and can be:
- Published as artifacts
- Used for quality gates
- Integrated with coverage services (Codecov, Coveralls)

### IDE Integration
Most IDEs can display coverage information:
- VS Code: Install coverage extension
- PyCharm: Built-in coverage support
- Vim/Emacs: Coverage plugins available

## Troubleshooting

### Common Issues

1. **Coverage not showing**: Ensure `pytest-cov` is installed
2. **Missing files**: Check `.coveragerc` omit patterns
3. **Low coverage**: Run `make coverage-analyze` to identify gaps
4. **Build failures**: Coverage threshold may be too high

### Debugging
```bash
# Check coverage data
.venv/bin/coverage debug data

# Show coverage configuration
.venv/bin/coverage debug config

# List measured files
.venv/bin/coverage debug sys
```

## Best Practices

1. **Maintain high coverage**: Aim for >90% coverage
2. **Test edge cases**: Don't just test happy paths
3. **Review gaps regularly**: Use `make coverage-analyze`
4. **Document exclusions**: Comment why code is excluded
5. **Update thresholds**: Adjust as codebase grows

## Dependencies

Coverage functionality requires:
- `pytest-cov>=4.0.0` (in `requirements-dev.txt`)
- `coverage` (installed with pytest-cov)
- Virtual environment setup

## Author

This coverage setup was implemented by Claude Sonnet 4 (claude-3-5-sonnet-20241022) via Cursor IDE (cursor.sh) with AI assistance. 