#!/usr/bin/env python3
"""
Pytest plugin for generating markdown test reports.

This plugin integrates with the existing markdown report generation system
and provides hooks for pytest to automatically generate reports.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import pytest
from _pytest.config import Config
from _pytest.terminal import TerminalReporter
from _pytest.reports import TestReport


class MarkdownReportPlugin:
    """Pytest plugin for generating markdown test reports."""
    
    def __init__(self, config: Config):
        self.config = config
        self.results_dir = Path("results")
        self.results_dir.mkdir(exist_ok=True)
        
        # Report file paths
        self.json_file = self.results_dir / "test_results.json"
        self.md_file = self.results_dir / "test_results.md"
        self.summary_file = self.results_dir / "test_summary.md"
        
        # Test results storage
        self.test_results = []
        self.session_start_time = None
        self.session_end_time = None
        
    def pytest_sessionstart(self, session):
        """Called at the start of the test session."""
        self.session_start_time = datetime.now()
        
    def pytest_sessionfinish(self, session, exitstatus):
        """Called at the end of the test session."""
        self.session_end_time = datetime.now()
        # Only generate reports if md-report is enabled
        if self.config.getoption("--md-report", default=False):
            self._generate_reports()
        
    def pytest_runtest_logreport(self, report: TestReport):
        """Called for each test report."""
        if report.when == "call":  # Only process the actual test call
            test_result = {
                "nodeid": report.nodeid,
                "outcome": report.outcome,
                "duration": report.duration or 0.0,
                "call": {
                    "longrepr": str(report.longrepr) if report.longrepr else ""
                }
            }
            self.test_results.append(test_result)
            
    def _generate_reports(self):
        """Generate all markdown reports."""
        # Create the main JSON data structure
        data = {
            "tests": self.test_results,
            "summary": {
                "total": len(self.test_results),
                "passed": sum(1 for t in self.test_results if t["outcome"] == "passed"),
                "failed": sum(1 for t in self.test_results if t["outcome"] == "failed"),
                "skipped": sum(1 for t in self.test_results if t["outcome"] == "skipped"),
                "xfailed": sum(1 for t in self.test_results if t["outcome"] == "xfailed"),
                "xpassed": sum(1 for t in self.test_results if t["outcome"] == "xpassed"),
                "duration": sum(t["duration"] for t in self.test_results),
                "session_start": self.session_start_time.isoformat() if self.session_start_time else None,
                "session_end": self.session_end_time.isoformat() if self.session_end_time else None
            }
        }
        
        # Write JSON report
        with open(self.json_file, 'w') as f:
            json.dump(data, f, indent=2)
            
        # Generate detailed markdown report
        self._generate_detailed_markdown_report(data)
        
        # Generate summary markdown report
        self._generate_summary_markdown_report(data)
        
    def _generate_detailed_markdown_report(self, data: Dict[str, Any]):
        """Generate detailed markdown report."""
        from scripts.generate_markdown_report import generate_markdown_report
        generate_markdown_report(str(self.json_file), str(self.md_file))
        
    def _generate_summary_markdown_report(self, data: Dict[str, Any]):
        """Generate a concise summary markdown report for GitHub."""
        summary = data["summary"]
        total = summary["total"]
        passed = summary["passed"]
        failed = summary["failed"]
        skipped = summary["skipped"]
        duration = summary["duration"]
        
        # Calculate success rate
        success_rate = (passed / total * 100) if total > 0 else 0
        
        # Generate summary content
        content = [
            "# 🧪 Test Results Summary",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## 📊 Statistics",
            "",
            "| Metric | Count |",
            "|--------|-------|",
            f"| Total Tests | {total} |",
            f"| ✅ Passed | {passed} |",
            f"| ❌ Failed | {failed} |",
            f"| ⏭️ Skipped | {skipped} |",
            f"| ⏱️ Duration | {self._format_duration(duration)} |",
            "",
            f"**Success Rate:** {success_rate:.1f}%",
            "",
            "## 🎯 Status",
            ""
        ]
        
        # Add status badge
        if success_rate == 100:
            content.append("![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen)")
        elif success_rate >= 90:
            content.append("![Tests Mostly Passing](https://img.shields.io/badge/tests-mostly%20passing-yellow)")
        else:
            content.append("![Tests Failing](https://img.shields.io/badge/tests-failing-red)")
            
        content.extend([
            "",
            "## 📋 Recent Test Runs",
            "",
            "| Date | Total | Passed | Failed | Success Rate |",
            "|------|-------|--------|--------|--------------|",
            f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | {total} | {passed} | {failed} | {success_rate:.1f}% |",
            "",
            "---",
            "",
            "*This report is automatically generated by the pytest-md-report plugin.*",
            "",
            f"📄 [Detailed Report](test_results.md) | 📊 [JSON Data](test_results.json)"
        ])
        
        # Write summary file
        with open(self.summary_file, 'w') as f:
            f.write('\n'.join(content))
            
    def _format_duration(self, duration: float) -> str:
        """Format duration in seconds to a human-readable string."""
        if duration < 1:
            return f"{duration * 1000:.1f}ms"
        elif duration < 60:
            return f"{duration:.2f}s"
        else:
            minutes = int(duration // 60)
            seconds = duration % 60
            return f"{minutes}m {seconds:.1f}s"


def pytest_configure(config: Config):
    """Register the markdown report plugin."""
    config.pluginmanager.register(MarkdownReportPlugin(config), "md_report")


def pytest_addoption(parser):
    """Add command line options for the markdown report plugin."""
    group = parser.getgroup("markdown-report")
    group.addoption(
        "--md-report",
        action="store_true",
        default=False,
        help="Generate markdown test reports"
    )
    group.addoption(
        "--md-report-dir",
        action="store",
        default="results",
        help="Directory to store markdown reports (default: results)"
    )
    group.addoption(
        "--md-report-verbose",
        action="store",
        type=int,
        default=0,
        help="Verbosity level for markdown reports (0-2)"
    )
    group.addoption(
        "--md-report-color",
        action="store",
        default="auto",
        choices=["auto", "yes", "no"],
        help="Enable/disable color in markdown reports"
    ) 