#!/usr/bin/env python3
"""
Coverage analysis script for whitespace-stego project.

This script provides various coverage analysis options including:
- Running tests with coverage
- Generating coverage reports
- Analyzing coverage gaps
- Comparing coverage between different test runs

Author: Claude Sonnet 4 (claude-3-5-sonnet-20241022)
Generated via Cursor IDE (cursor.sh) with AI assistance
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional


def run_command(cmd: List[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {' '.join(cmd)}")
        print(f"   Exit code: {e.returncode}")
        if e.stdout:
            print(f"   Stdout: {e.stdout}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        return False


def run_coverage_tests(parallel: bool = True, include_cli: bool = True) -> bool:
    """Run tests with coverage reporting."""
    cmd = [".venv/bin/pytest"]
    
    if parallel:
        cmd.extend(["-n", "auto", "--dist", "loadfile"])
    else:
        cmd.extend(["-n", "0"])
    
    if not include_cli:
        cmd.extend(["-m", "not cli"])
    
    # Coverage options are already in pytest.ini
    return run_command(cmd, "Running tests with coverage")


def generate_coverage_report() -> bool:
    """Generate coverage report from existing data."""
    cmd = [".venv/bin/coverage", "report", "--show-missing"]
    return run_command(cmd, "Generating coverage report")


def generate_html_report() -> bool:
    """Generate HTML coverage report."""
    cmd = [".venv/bin/coverage", "html"]
    return run_command(cmd, "Generating HTML coverage report")


def generate_xml_report() -> bool:
    """Generate XML coverage report."""
    cmd = [".venv/bin/coverage", "xml"]
    return run_command(cmd, "Generating XML coverage report")


def analyze_coverage_gaps() -> bool:
    """Analyze coverage gaps and suggest improvements."""
    print("🔍 Analyzing coverage gaps...")
    
    # Read coverage data
    try:
        import coverage
        cov = coverage.Coverage()
        cov.load()
        
        # Get missing lines
        missing_lines = []
        for filename in cov.get_data().measured_files():
            if 'whitespace_stego' in filename:
                missing = cov.analysis2(filename)[2]  # Missing lines
                if missing:
                    missing_lines.append((filename, missing))
        
        if missing_lines:
            print("📊 Coverage gaps found:")
            for filename, lines in missing_lines:
                print(f"   {Path(filename).name}: {len(lines)} missing lines")
                if len(lines) <= 10:  # Show specific lines if not too many
                    print(f"      Lines: {', '.join(map(str, lines))}")
        else:
            print("✅ No coverage gaps found!")
        
        return True
    except Exception as e:
        print(f"❌ Error analyzing coverage gaps: {e}")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Run coverage analysis for whitespace-stego project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/run_coverage.py --run-tests
  python scripts/run_coverage.py --report
  python scripts/run_coverage.py --analyze-gaps
  python scripts/run_coverage.py --all
        """
    )
    
    parser.add_argument(
        "--run-tests",
        action="store_true",
        help="Run tests with coverage"
    )
    
    parser.add_argument(
        "--sequential",
        action="store_true",
        help="Run tests sequentially (not in parallel)"
    )
    
    parser.add_argument(
        "--no-cli",
        action="store_true",
        help="Exclude CLI tests"
    )
    
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate coverage report"
    )
    
    parser.add_argument(
        "--html",
        action="store_true",
        help="Generate HTML coverage report"
    )
    
    parser.add_argument(
        "--xml",
        action="store_true",
        help="Generate XML coverage report"
    )
    
    parser.add_argument(
        "--analyze-gaps",
        action="store_true",
        help="Analyze coverage gaps"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all coverage operations"
    )
    
    args = parser.parse_args()
    
    # Check if virtual environment exists
    if not Path(".venv").exists():
        print("❌ Virtual environment not found. Please run 'make venv' first.")
        sys.exit(1)
    
    success = True
    
    if args.all or args.run_tests:
        success &= run_coverage_tests(
            parallel=not args.sequential,
            include_cli=not args.no_cli
        )
    
    if args.all or args.report:
        success &= generate_coverage_report()
    
    if args.all or args.html:
        success &= generate_html_report()
    
    if args.all or args.xml:
        success &= generate_xml_report()
    
    if args.all or args.analyze_gaps:
        success &= analyze_coverage_gaps()
    
    if not any([args.run_tests, args.report, args.html, args.xml, args.analyze_gaps, args.all]):
        parser.print_help()
        return
    
    if success:
        print("\n🎉 Coverage analysis completed successfully!")
        print("📁 Reports available:")
        print("   - HTML: htmlcov/index.html")
        print("   - XML: coverage.xml")
        print("   - Terminal: See output above")
    else:
        print("\n❌ Coverage analysis completed with errors")
        sys.exit(1)


if __name__ == "__main__":
    main() 