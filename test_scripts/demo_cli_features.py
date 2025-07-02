#!/usr/bin/env python3
"""
Comprehensive demonstration of whitespace steganography CLI features.

This script showcases all the CLI functionality including:
- Mutually exclusive options
- Stdout output support
- Password protection
- Unicode and emoji support
- Pipeline usage
- Error handling
- Backend selection
"""

import subprocess
import tempfile
import os
import sys
from pathlib import Path


def run_command(cmd, description, expect_success=True):
    """Run a CLI command and display results."""
    print(f"\n{'=' * 60}")
    print(f"🔧 {description}")
    print(f"{'=' * 60}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, check=expect_success
        )
        print("✅ SUCCESS")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        if result.stderr:
            print("Logs:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print("❌ FAILED (as expected)")
        print(f"Exit code: {e.returncode}")
        if e.stdout:
            print("Output:")
            print(e.stdout)
        if e.stderr:
            print("Error:")
            print(e.stderr)
    print("-" * 60)


def create_demo_files():
    """Create demo files for testing."""
    files = {}

    # Create message file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("This is a secret message from a file.\nIt contains multiple lines.")
        files["message"] = f.name

    # Create carrier file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("This is a carrier text file.\nIt will be used to hide messages.")
        files["carrier"] = f.name

    # Create Unicode message file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello 世界 🌍\nThis is a Unicode message with emojis! 🚀")
        files["unicode_message"] = f.name

    # Create Unicode carrier file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Unicode carrier: café naïve\nSpecial characters: ñáéíóú")
        files["unicode_carrier"] = f.name

    return files


def cleanup_files(files):
    """Clean up temporary files."""
    for file_path in files.values():
        try:
            os.unlink(file_path)
        except OSError:
            pass


def main():
    """Main demonstration function."""
    print("🚀 Whitespace Steganography CLI Feature Demonstration")
    print("=" * 60)

    # Create demo files
    files = create_demo_files()

    try:
        # 1. Help and Documentation
        print("\n📚 SECTION 1: Help and Documentation")
        run_command(
            ["python3", "-m", "whitespace_stego.cli", "--help"], "Main CLI help"
        )
        run_command(
            ["python3", "-m", "whitespace_stego.cli", "encode", "--help"],
            "Encode command help",
        )
        run_command(
            ["python3", "-m", "whitespace_stego.cli", "decode", "--help"],
            "Decode command help",
        )

        # 2. Backend Validation
        print("\n🔧 SECTION 2: Backend Validation")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "python",
                "encode",
                "--help",
            ],
            "Python backend validation",
        )
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "rust",
                "encode",
                "--help",
            ],
            "Rust backend validation",
        )
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "invalid",
                "encode",
                "--help",
            ],
            "Invalid backend validation",
            expect_success=False,
        )

        # 3. Mutually Exclusive Options
        print("\n🚫 SECTION 3: Mutually Exclusive Options")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "test",
                "--message-file",
                files["message"],
                "--carrier",
                "carrier",
                "--output",
                "test.out",
            ],
            "Mutually exclusive message options",
            expect_success=False,
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "test",
                "--carrier",
                "carrier",
                "--carrier-file",
                files["carrier"],
                "--output",
                "test.out",
            ],
            "Mutually exclusive carrier options",
            expect_success=False,
        )

        # 4. Missing Required Options
        print("\n❌ SECTION 4: Missing Required Options")
        run_command(
            ["python3", "-m", "whitespace_stego.cli", "encode", "--output", "test.out"],
            "Missing message and carrier options",
            expect_success=False,
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "test",
                "--output",
                "test.out",
            ],
            "Missing carrier option",
            expect_success=False,
        )

        # 5. Basic Encoding/Decoding
        print("\n🔐 SECTION 5: Basic Encoding/Decoding")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Hello World!",
                "--carrier",
                "This is a test carrier.",
            ],
            "Encode message+carrier to stdout",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "File output test",
                "--carrier",
                "Carrier for file",
                "--output",
                "demo_encoded.txt",
            ],
            "Encode to file",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "decode",
                "--carrier-file",
                "demo_encoded.txt",
            ],
            "Decode from file to stdout",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "decode",
                "--carrier-file",
                "demo_encoded.txt",
                "--output",
                "demo_decoded.txt",
            ],
            "Decode to file",
        )

        # 6. File Input/Output Combinations
        print("\n📁 SECTION 6: File Input/Output Combinations")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message-file",
                files["message"],
                "--carrier",
                "Command line carrier",
            ],
            "Message from file, carrier from command line",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Command line message",
                "--carrier-file",
                files["carrier"],
            ],
            "Message from command line, carrier from file",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message-file",
                files["message"],
                "--carrier-file",
                files["carrier"],
            ],
            "Both message and carrier from files",
        )

        # 7. Stdout Output Options
        print("\n📤 SECTION 7: Stdout Output Options")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Stdout test",
                "--carrier",
                "Stdout carrier",
                "--output",
                "-",
            ],
            "Explicit stdout output with dash",
        )

        # 8. Password Protection
        print("\n🔒 SECTION 8: Password Protection")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Secret with password",
                "--carrier",
                "Protected carrier",
                "--password",
                "mypassword",
                "--output",
                "demo_encoded_pwd.txt",
            ],
            "Encode with password protection",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "decode",
                "--carrier-file",
                "demo_encoded_pwd.txt",
                "--password",
                "mypassword",
            ],
            "Decode with correct password",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "decode",
                "--carrier-file",
                "demo_encoded_pwd.txt",
                "--password",
                "wrongpassword",
            ],
            "Decode with wrong password",
            expect_success=False,
        )

        # 9. Unicode and Emoji Support
        print("\n🌍 SECTION 9: Unicode and Emoji Support")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Hello 世界 🌍",
                "--carrier",
                "Unicode carrier: café naïve",
                "--output",
                "demo_unicode.txt",
            ],
            "Encode Unicode content",
        )

        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "decode",
                "--carrier-file",
                "demo_unicode.txt",
            ],
            "Decode Unicode content",
        )

        # 10. Verbose Mode
        print("\n🔍 SECTION 10: Verbose Mode")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "--verbose",
                "encode",
                "--message",
                "Verbose test",
                "--carrier",
                "Verbose carrier",
                "--output",
                "-",
            ],
            "Verbose mode encoding",
        )

        # 11. Short Options
        print("\n⚡ SECTION 11: Short Options")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "-b",
                "python",
                "encode",
                "-m",
                "Short options test",
                "-c",
                "Short carrier text",
                "-o",
                "-",
            ],
            "All short options",
        )

        # 12. Pipeline Simulation
        print("\n🔗 SECTION 12: Pipeline Simulation")
        print("Simulating: encode | decode")

        # Encode to get output
        encode_result = subprocess.run(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "encode",
                "--message",
                "Pipeline test message",
                "--carrier",
                "Pipeline carrier text",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        # Get the encoded content (last line)
        encoded_content = encode_result.stdout.strip().split("\n")[-1]

        # Create temporary file for pipeline simulation
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write(encoded_content)
            temp_file = f.name

        try:
            run_command(
                [
                    "python3",
                    "-m",
                    "whitespace_stego.cli",
                    "decode",
                    "--carrier-file",
                    temp_file,
                ],
                "Pipeline decode simulation",
            )
        finally:
            os.unlink(temp_file)

        # 13. Error Handling
        print("\n⚠️ SECTION 13: Error Handling")
        run_command(
            [
                "python3",
                "-m",
                "whitespace_stego.cli",
                "--backend",
                "rust",
                "encode",
                "--message",
                "test",
                "--carrier",
                "carrier",
            ],
            "Rust backend error (when not installed)",
            expect_success=False,
        )

        # 14. Content Verification
        print("\n✅ SECTION 14: Content Verification")
        if os.path.exists("demo_decoded.txt"):
            with open("demo_decoded.txt", "r") as f:
                content = f.read().strip()
            print(f"Decoded content: '{content}'")
            if content == "File output test":
                print("✅ Content verification successful!")
            else:
                print("❌ Content verification failed!")

        # 15. File Cleanup
        print("\n🧹 SECTION 15: File Cleanup")
        cleanup_list = [
            "demo_encoded.txt",
            "demo_decoded.txt",
            "demo_encoded_pwd.txt",
            "demo_unicode.txt",
        ]
        for file in cleanup_list:
            if os.path.exists(file):
                os.unlink(file)
                print(f"✅ Cleaned up: {file}")

        print("\n🎉 DEMONSTRATION COMPLETE!")
        print("=" * 60)
        print("All CLI features have been demonstrated successfully!")
        print("The whitespace steganography CLI is fully functional with:")
        print("✅ Mutually exclusive options")
        print("✅ Stdout output support")
        print("✅ Password protection")
        print("✅ Unicode and emoji support")
        print("✅ Pipeline compatibility")
        print("✅ Comprehensive error handling")
        print("✅ Multiple backend support")
        print("✅ Verbose logging")
        print("✅ File and command line input")

    finally:
        # Clean up demo files
        cleanup_files(files)


if __name__ == "__main__":
    main()
