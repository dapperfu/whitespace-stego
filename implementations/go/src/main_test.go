package main

import (
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"
)

// getExecutablePath returns the path to the compiled executable
func getExecutablePath(t *testing.T) string {
	// Try to find the executable in the bin directory
	exePath := filepath.Join("..", "bin", "whitespace-stego-go")
	if _, err := os.Stat(exePath); err == nil {
		return exePath
	}

	// If not found, try current directory
	exePath = "whitespace-stego-go"
	if _, err := os.Stat(exePath); err == nil {
		return exePath
	}

	t.Fatalf("Executable not found. Please run 'go build -o bin/whitespace-stego-go .' first")
	return ""
}

// runCommand runs the CLI with given arguments and returns output and error
func runCommand(t *testing.T, args ...string) (string, string, error) {
	exePath := getExecutablePath(t)
	cmd := exec.Command(exePath, args...)

	// Capture both stdout and stderr
	var stdout, stderr strings.Builder
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	err := cmd.Run()
	return stdout.String(), stderr.String(), err
}

// TestMutualExclusivityMessageOptions tests that -m and -mf are mutually exclusive
func TestMutualExclusivityMessageOptions(t *testing.T) {
	// Create temporary files for testing
	messageFile := filepath.Join(t.TempDir(), "message.txt")
	err := os.WriteFile(messageFile, []byte("Test message"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test message file: %v", err)
	}

	carrierFile := filepath.Join(t.TempDir(), "carrier.txt")
	err = os.WriteFile(carrierFile, []byte("Carrier text"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test carrier file: %v", err)
	}

	// Test that -m and -mf together causes error
	_, stderr, err := runCommand(t, "encode", "-m", "Direct message", "-mf", messageFile, "-cf", carrierFile)
	if err == nil {
		t.Fatalf("Expected error when using both -m and -mf, but command succeeded")
	}

	if !strings.Contains(stderr, "mutually exclusive") {
		t.Fatalf("Expected error about mutual exclusivity, got: %s", stderr)
	}
}

// TestMutualExclusivityCarrierOptions tests that -c and -cf are mutually exclusive
func TestMutualExclusivityCarrierOptions(t *testing.T) {
	// Create temporary files for testing
	messageFile := filepath.Join(t.TempDir(), "message.txt")
	err := os.WriteFile(messageFile, []byte("Test message"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test message file: %v", err)
	}

	carrierFile := filepath.Join(t.TempDir(), "carrier.txt")
	err = os.WriteFile(carrierFile, []byte("Carrier text"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test carrier file: %v", err)
	}

	// Test that -c and -cf together causes error
	_, stderr, err := runCommand(t, "encode", "-m", "Test message", "-c", "Direct carrier", "-cf", carrierFile)
	if err == nil {
		t.Fatalf("Expected error when using both -c and -cf, but command succeeded")
	}

	if !strings.Contains(stderr, "mutually exclusive") {
		t.Fatalf("Expected error about mutual exclusivity, got: %s", stderr)
	}
}

// TestMutualExclusivityCarrierOptionsDecode tests that -c and -cf are mutually exclusive in decode
func TestMutualExclusivityCarrierOptionsDecode(t *testing.T) {
	// Create temporary files for testing
	carrierFile := filepath.Join(t.TempDir(), "carrier.txt")
	err := os.WriteFile(carrierFile, []byte("Carrier text"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test carrier file: %v", err)
	}

	// Test that -c and -cf together causes error in decode
	_, stderr, err := runCommand(t, "decode", "-c", "Direct carrier", "-cf", carrierFile)
	if err == nil {
		t.Fatalf("Expected error when using both -c and -cf in decode, but command succeeded")
	}

	if !strings.Contains(stderr, "mutually exclusive") {
		t.Fatalf("Expected error about mutual exclusivity, got: %s", stderr)
	}
}

// TestMissingMessageOption tests that encode requires either -m or -mf
func TestMissingMessageOption(t *testing.T) {
	carrierFile := filepath.Join(t.TempDir(), "carrier.txt")
	err := os.WriteFile(carrierFile, []byte("Carrier text"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test carrier file: %v", err)
	}

	// Test that missing message option causes error
	_, stderr, err := runCommand(t, "encode", "-cf", carrierFile)
	if err == nil {
		t.Fatalf("Expected error when missing message option, but command succeeded")
	}

	if !strings.Contains(stderr, "required") {
		t.Fatalf("Expected error about required message option, got: %s", stderr)
	}
}

// TestMissingCarrierOption tests that encode requires either -c or -cf
func TestMissingCarrierOption(t *testing.T) {
	// Test that missing carrier option causes error
	_, stderr, err := runCommand(t, "encode", "-m", "Test message")
	if err == nil {
		t.Fatalf("Expected error when missing carrier option, but command succeeded")
	}

	if !strings.Contains(stderr, "required") {
		t.Fatalf("Expected error about required carrier option, got: %s", stderr)
	}
}

// TestMissingCarrierOptionDecode tests that decode requires either -c or -cf
func TestMissingCarrierOptionDecode(t *testing.T) {
	// Test that missing carrier option causes error in decode
	_, stderr, err := runCommand(t, "decode")
	if err == nil {
		t.Fatalf("Expected error when missing carrier option in decode, but command succeeded")
	}

	if !strings.Contains(stderr, "required") {
		t.Fatalf("Expected error about required carrier option, got: %s", stderr)
	}
}

// TestValidEncodeWithDirectOptions tests that encode works with direct options
func TestValidEncodeWithDirectOptions(t *testing.T) {
	outputFile := filepath.Join(t.TempDir(), "output.txt")

	// Test that encode works with direct message and carrier
	stdout, stderr, err := runCommand(t, "encode", "-m", "Test message", "-c", "Carrier text", "-o", outputFile)
	if err != nil {
		t.Fatalf("Encode failed: %v\nstdout: %s\nstderr: %s", err, stdout, stderr)
	}

	// Check that output file was created
	if _, err := os.Stat(outputFile); os.IsNotExist(err) {
		t.Fatalf("Output file was not created")
	}
}

// TestValidEncodeWithFileOptions tests that encode works with file options
func TestValidEncodeWithFileOptions(t *testing.T) {
	tempDir := t.TempDir()
	messageFile := filepath.Join(tempDir, "message.txt")
	carrierFile := filepath.Join(tempDir, "carrier.txt")
	outputFile := filepath.Join(tempDir, "output.txt")

	// Create test files
	err := os.WriteFile(messageFile, []byte("Test message"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test message file: %v", err)
	}

	err = os.WriteFile(carrierFile, []byte("Carrier text"), 0644)
	if err != nil {
		t.Fatalf("Failed to create test carrier file: %v", err)
	}

	// Test that encode works with file options
	stdout, stderr, err := runCommand(t, "encode", "-mf", messageFile, "-cf", carrierFile, "-o", outputFile)
	if err != nil {
		t.Fatalf("Encode failed: %v\nstdout: %s\nstderr: %s", err, stdout, stderr)
	}

	// Check that output file was created
	if _, err := os.Stat(outputFile); os.IsNotExist(err) {
		t.Fatalf("Output file was not created")
	}
}

// TestValidDecodeWithDirectCarrier tests that decode works with direct carrier
func TestValidDecodeWithDirectCarrier(t *testing.T) {
	// First encode a message
	tempDir := t.TempDir()
	outputFile := filepath.Join(tempDir, "encoded.txt")

	_, _, err := runCommand(t, "encode", "-m", "Test message", "-c", "Carrier text", "-o", outputFile)
	if err != nil {
		t.Fatalf("Failed to encode test message: %v", err)
	}

	// Read the encoded content
	encodedBytes, err := os.ReadFile(outputFile)
	if err != nil {
		t.Fatalf("Failed to read encoded file: %v", err)
	}
	encoded := string(encodedBytes)

	// Test that decode works with direct carrier
	stdout, stderr, err := runCommand(t, "decode", "-c", encoded)
	if err != nil {
		t.Fatalf("Decode failed: %v\nstdout: %s\nstderr: %s", err, stdout, stderr)
	}

	if !strings.Contains(stdout, "Test message") {
		t.Fatalf("Decoded output doesn't contain expected message. Got: %s", stdout)
	}
}

// TestValidDecodeWithFileCarrier tests that decode works with file carrier
func TestValidDecodeWithFileCarrier(t *testing.T) {
	// First encode a message
	tempDir := t.TempDir()
	outputFile := filepath.Join(tempDir, "encoded.txt")

	_, _, err := runCommand(t, "encode", "-m", "Test message", "-c", "Carrier text", "-o", outputFile)
	if err != nil {
		t.Fatalf("Failed to encode test message: %v", err)
	}

	// Test that decode works with file carrier
	stdout, stderr, err := runCommand(t, "decode", "-cf", outputFile)
	if err != nil {
		t.Fatalf("Decode failed: %v\nstdout: %s\nstderr: %s", err, stdout, stderr)
	}

	if !strings.Contains(stdout, "Test message") {
		t.Fatalf("Decoded output doesn't contain expected message. Got: %s", stdout)
	}
}

// TestUnknownCommand tests that unknown commands are handled properly
func TestUnknownCommand(t *testing.T) {
	_, stderr, err := runCommand(t, "unknown")
	if err == nil {
		t.Fatalf("Expected error for unknown command, but command succeeded")
	}

	if !strings.Contains(stderr, "Unknown command") {
		t.Fatalf("Expected error about unknown command, got: %s", stderr)
	}
}

// TestHelpCommand tests that help command works
func TestHelpCommand(t *testing.T) {
	stdout, stderr, err := runCommand(t, "help")
	if err != nil {
		t.Fatalf("Help command failed: %v\nstdout: %s\nstderr: %s", err, stdout, stderr)
	}

	if !strings.Contains(stdout, "Usage:") && !strings.Contains(stderr, "Usage:") {
		t.Fatalf("Help output doesn't contain usage information")
	}
}

// TestNoArguments tests that no arguments shows usage
func TestNoArguments(t *testing.T) {
	_, stderr, err := runCommand(t)
	if err == nil {
		t.Fatalf("Expected error for no arguments, but command succeeded")
	}

	if !strings.Contains(stderr, "Usage:") {
		t.Fatalf("Expected usage information for no arguments, got: %s", stderr)
	}
}
