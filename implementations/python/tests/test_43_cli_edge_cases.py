"""
Test 43: CLI Edge Cases

This test suite covers CLI error paths, mutually exclusive options, file I/O errors, Unicode, and output redirection.
"""

import pytest
from click.testing import CliRunner
from whitespace_stego.cli import cli

class TestCLIErrorPaths:
    def test_mutually_exclusive_message(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", "a", "--message-file", "file.txt"])
        assert result.exit_code != 0
        assert "mutually exclusive" in result.output
    def test_mutually_exclusive_carrier(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", "a", "--carrier", "b", "--carrier-file", "file.txt"])
        assert result.exit_code != 0
        assert "mutually exclusive" in result.output
    def test_file_io_error(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message-file", "nonexistent.txt"])
        assert result.exit_code != 0
    def test_unicode_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["encode", "--message", "世界🌍"])
        assert result.exit_code == 0
    def test_output_redirection(self, tmp_path):
        runner = CliRunner()
        out_file = tmp_path / "out.txt"
        result = runner.invoke(cli, ["encode", "--message", "test", "--output", str(out_file)])
        assert result.exit_code == 0
        assert out_file.read_text().strip() != "" 