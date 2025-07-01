#!/usr/bin/env python3
"""
Generate Markdown test reports from pytest JSON output.

This script reads pytest JSON output and generates a comprehensive markdown report
with test results, statistics, and detailed information about failures.
"""

import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path


def format_duration(duration: float) -> str:
    """Format duration in seconds to a human-readable string."""
    if duration < 1:
        return f"{duration * 1000:.1f}ms"
    elif duration < 60:
        return f"{duration:.2f}s"
    else:
        minutes = int(duration // 60)
        seconds = duration % 60
        return f"{minutes}m {seconds:.1f}s"


def format_test_name(test_id: str) -> str:
    """Format test ID to a readable test name."""
    # Remove file path and keep only the test function name
    if "::" in test_id:
        parts = test_id.split("::")
        if len(parts) >= 3:
            return f"{parts[-2]}::{parts[-1]}"
    return test_id


def get_test_status(result: Dict[str, Any]) -> str:
    """Get the status of a test result."""
    if result.get("outcome") == "passed":
        return "✅ PASS"
    elif result.get("outcome") == "failed":
        return "❌ FAIL"
    elif result.get("outcome") == "skipped":
        return "⏭️  SKIP"
    elif result.get("outcome") == "xfailed":
        return "⚠️  XFAIL"
    elif result.get("outcome") == "xpassed":
        return "⚠️  XPASS"
    else:
        return f"❓ {result.get('outcome', 'UNKNOWN').upper()}"


def generate_markdown_report(json_file: str, output_file: str) -> None:
    """Generate a markdown report from pytest JSON output."""
    
    # Read JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract test results
    test_results = data.get("tests", [])
    
    # Calculate statistics
    total_tests = len(test_results)
    passed = sum(1 for test in test_results if test.get("outcome") == "passed")
    failed = sum(1 for test in test_results if test.get("outcome") == "failed")
    skipped = sum(1 for test in test_results if test.get("outcome") == "skipped")
    xfailed = sum(1 for test in test_results if test.get("outcome") == "xfailed")
    xpassed = sum(1 for test in test_results if test.get("outcome") == "xpassed")
    
    # Calculate total duration
    total_duration = sum(test.get("duration", 0) for test in test_results)
    
    # Generate markdown content
    markdown_content = []
    
    # Header
    markdown_content.append("# Test Results Report")
    markdown_content.append("")
    markdown_content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    markdown_content.append("")
    
    # Summary
    markdown_content.append("## Summary")
    markdown_content.append("")
    markdown_content.append("| Metric | Count |")
    markdown_content.append("|--------|-------|")
    markdown_content.append(f"| Total Tests | {total_tests} |")
    markdown_content.append(f"| Passed | {passed} |")
    markdown_content.append(f"| Failed | {failed} |")
    markdown_content.append(f"| Skipped | {skipped} |")
    markdown_content.append(f"| Expected Failures | {xfailed} |")
    markdown_content.append(f"| Unexpected Passes | {xpassed} |")
    markdown_content.append(f"| Total Duration | {format_duration(total_duration)} |")
    markdown_content.append("")
    
    # Success rate
    if total_tests > 0:
        success_rate = (passed / total_tests) * 100
        markdown_content.append(f"**Success Rate:** {success_rate:.1f}%")
        markdown_content.append("")
    
    # Test Results
    markdown_content.append("## Test Results")
    markdown_content.append("")
    
    # Group tests by outcome
    outcomes = {
        "passed": [],
        "failed": [],
        "skipped": [],
        "xfailed": [],
        "xpassed": []
    }
    
    for test in test_results:
        outcome = test.get("outcome", "unknown")
        if outcome in outcomes:
            outcomes[outcome].append(test)
    
    # Display each outcome group
    for outcome, tests in outcomes.items():
        if not tests:
            continue
            
        outcome_title = outcome.upper()
        if outcome == "passed":
            outcome_title = "✅ PASSED"
        elif outcome == "failed":
            outcome_title = "❌ FAILED"
        elif outcome == "skipped":
            outcome_title = "⏭️  SKIPPED"
        elif outcome == "xfailed":
            outcome_title = "⚠️  EXPECTED FAILURES"
        elif outcome == "xpassed":
            outcome_title = "⚠️  UNEXPECTED PASSES"
        
        markdown_content.append(f"### {outcome_title} ({len(tests)})")
        markdown_content.append("")
        
        if outcome == "passed":
            # For passed tests, show a compact list
            markdown_content.append("| Test | Duration |")
            markdown_content.append("|------|----------|")
            for test in tests:
                test_name = format_test_name(test.get("nodeid", ""))
                duration = format_duration(test.get("duration", 0))
                markdown_content.append(f"| {test_name} | {duration} |")
        else:
            # For other outcomes, show more details
            for test in tests:
                test_name = format_test_name(test.get("nodeid", ""))
                duration = format_duration(test.get("duration", 0))
                
                markdown_content.append(f"**{test_name}** ({duration})")
                
                # Add error details for failed tests
                if outcome == "failed":
                    error_info = test.get("call", {}).get("longrepr", "")
                    if error_info:
                        markdown_content.append("")
                        markdown_content.append("```")
                        markdown_content.append(error_info)
                        markdown_content.append("```")
                        markdown_content.append("")
                
                # Add skip reason for skipped tests
                elif outcome == "skipped":
                    skip_reason = test.get("call", {}).get("longrepr", "")
                    if skip_reason:
                        markdown_content.append(f"*Reason: {skip_reason}*")
                        markdown_content.append("")
        
        markdown_content.append("")
    
    # Write the markdown file
    with open(output_file, 'w') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Markdown report generated: {output_file}")


def main():
    """Main function."""
    if len(sys.argv) != 3:
        print("Usage: python generate_markdown_report.py <json_file> <output_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(json_file):
        print(f"Error: JSON file '{json_file}' not found")
        sys.exit(1)
    
    try:
        generate_markdown_report(json_file, output_file)
    except Exception as e:
        print(f"Error generating markdown report: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 