package stego

import (
	"fmt"
	"os"
	"regexp"
	"strings"
	"testing"
)

func TestRegexFindsEncodedMessage(t *testing.T) {
	carrierBytes, err := os.ReadFile("/tmp/encoded_go.txt")
	if err != nil {
		t.Fatalf("Failed to read carrier: %v", err)
	}
	carrier := string(carrierBytes)
	pattern := regexp.MustCompile("(?s)" + regexp.QuoteMeta(START_MARKER) + "(.*?)" + regexp.QuoteMeta(END_MARKER))
	matches := pattern.FindAllStringSubmatch(carrier, -1)
	fmt.Printf("Found %d matches\n", len(matches))
	if len(matches) == 0 {
		t.Fatalf("No matches found by regex!")
	}
	fmt.Printf("First match (truncated): %q\n", matches[0][1][:min(40, len(matches[0][1]))])
}

func TestDebugDecode(t *testing.T) {
	// Test decoding the existing file with debug output
	carrierBytes, err := os.ReadFile("/tmp/encoded_go.txt")
	if err != nil {
		t.Fatalf("Failed to read carrier: %v", err)
	}
	carrier := string(carrierBytes)

	// First, run the regex manually
	pattern := regexp.MustCompile("(?s)" + regexp.QuoteMeta(START_MARKER) + "(.*?)" + regexp.QuoteMeta(END_MARKER))
	matches := pattern.FindAllStringSubmatch(carrier, -1)
	fmt.Printf("Regex found %d matches\n", len(matches))

	if len(matches) > 0 {
		// Try to decode the first match manually
		zw := matches[0][1]
		fmt.Printf("Zero-width data length: %d\n", len(zw))

		// Debug: print the first few characters
		fmt.Printf("First 10 chars: %q\n", zw[:min(10, len(zw))])
		fmt.Printf("ZERO_BIT: %q, ONE_BIT: %q\n", ZERO_BIT, ONE_BIT)

		// Check character filtering
		var filtered strings.Builder
		for i, r := range zw {
			if i < 10 { // Only check first 10 for debug
				fmt.Printf("Char %d: %q (rune: %d)\n", i, string(r), r)
				fmt.Printf("  Is ZERO_BIT? %v\n", r == rune(ZERO_BIT[0]))
				fmt.Printf("  Is ONE_BIT? %v\n", r == rune(ONE_BIT[0]))
			}
			if r == rune(ONE_BIT[0]) || r == rune(ZERO_BIT[0]) {
				filtered.WriteRune(r)
			}
		}
		fmt.Printf("Filtered length: %d\n", filtered.Len())

		// Decode binary data
		data, err := decodeBinary(zw)
		if err != nil {
			t.Fatalf("decodeBinary failed: %v", err)
		}
		fmt.Printf("Binary data length: %d\n", len(data))

		// Try to base64 decode and decrypt
		encrypted, err := base64Decode(string(data))
		if err != nil {
			t.Fatalf("base64Decode failed: %v", err)
		}
		fmt.Printf("Encrypted data length: %d\n", len(encrypted))

		decoded, err := decryptData(encrypted, "test_password_123")
		if err != nil {
			t.Fatalf("decryptData failed: %v", err)
		}
		fmt.Printf("Decrypted data length: %d\n", len(decoded))
		fmt.Printf("Decoded message: %q\n", string(decoded))
	}
}

func TestFullEncodeDecodeCycle(t *testing.T) {
	// Test the full cycle
	message := "Test message"
	carrier := "This is the carrier text for testing."
	password := "test_password_123"

	// Encode
	encoded, err := Encode(message, carrier, password)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	// Decode
	messages, err := Decode(encoded, password)
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}

	if len(messages) == 0 {
		t.Fatalf("No messages decoded")
	}

	if messages[0] != message {
		t.Fatalf("Decoded message doesn't match original. Expected: %q, Got: %q", message, messages[0])
	}

	fmt.Printf("✓ Full encode/decode cycle works\n")
}

func TestDecodeExistingFile(t *testing.T) {
	// Test decoding the existing file
	carrierBytes, err := os.ReadFile("/tmp/encoded_go.txt")
	if err != nil {
		t.Fatalf("Failed to read carrier: %v", err)
	}
	carrier := string(carrierBytes)

	// Try to decode
	messages, err := Decode(carrier, "test_password_123")
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}

	if len(messages) == 0 {
		t.Fatalf("No messages decoded from existing file")
	}

	fmt.Printf("✓ Decoded from existing file: %q\n", messages[0])
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
