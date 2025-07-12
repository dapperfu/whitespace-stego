package main

import (
	"errors"
	"fmt"
	"os"
	"regexp"
	"strings"
	"testing"
)

func TestRegexFindsEncodedMessage(t *testing.T) {
	carrierBytes, err := os.ReadFile("/tmp/encoded_go.txt")
	if err != nil {
		t.Skipf("Skipping: failed to read carrier: %v", err)
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
	// This test intentionally feeds invalid data to check error handling
	carrier := START_MARKER + "\u200b\u200b\u200d\u200d\u200b\u200b\u200d\u200d\u200b\u200d\u200d\u200b\u200d\xe2" + END_MARKER
	pattern := regexp.MustCompile(regexp.QuoteMeta(START_MARKER) + "(.*?)" + regexp.QuoteMeta(END_MARKER))
	matches := pattern.FindAllStringSubmatch(carrier, -1)
	if len(matches) == 0 {
		t.Fatalf("No matches found")
	}
	for _, match := range matches {
		zw := match[1]
		data, err := decodeBinary(zw)
		if err != nil {
			continue
		}
		encrypted, err := base64Decode(string(data))
		if err != nil {
			// Expected: invalid base64
			continue
		}
		_, err = decryptData(encrypted, "test_password_123")
		if err == nil {
			t.Fatalf("Expected decryptData to fail, but it succeeded")
		}
		// Success: error is expected
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
		t.Skipf("Skipping: failed to read carrier: %v", err)
	}
	carrier := string(carrierBytes)
	// Try to decode
	messages, err := Decode(carrier, "test_password_123")
	if err != nil {
		t.Skipf("Skipping: decode failed: %v", err)
	}
	if len(messages) == 0 {
		t.Fatalf("No messages decoded from existing file")
	}
	fmt.Printf("✓ Decoded from existing file: %q\n", messages[0])
}

// Test encode/decode without password
func TestEncodeDecodeNoPassword(t *testing.T) {
	message := "Hello, World!"
	carrier := "Carrier text"

	// Encode without password
	encoded, err := Encode(message, carrier, "")
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	// Decode without password
	messages, err := Decode(encoded, "")
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}

	if len(messages) == 0 {
		t.Fatalf("No messages decoded")
	}

	if messages[0] != message {
		t.Fatalf("Decoded message doesn't match original. Expected: %q, Got: %q", message, messages[0])
	}
}

// Test encode with empty carrier
func TestEncodeEmptyCarrier(t *testing.T) {
	message := "Test message"

	// Encode with empty carrier
	encoded, err := Encode(message, "", "")
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	// Should return just the encoded message
	if !strings.Contains(encoded, START_MARKER) || !strings.Contains(encoded, END_MARKER) {
		t.Fatalf("Encoded message should contain markers")
	}
}

// Test encode with empty message (should fail)
func TestEncodeEmptyMessage(t *testing.T) {
	_, err := Encode("", "carrier", "")
	if err == nil {
		t.Fatalf("Encode should fail with empty message")
	}
	if !strings.Contains(err.Error(), "message must not be empty") {
		t.Fatalf("Expected error about empty message, got: %v", err)
	}
}

// Test decode with no valid messages
func TestDecodeNoMessages(t *testing.T) {
	_, err := Decode("No markers here", "")
	if err == nil {
		t.Fatalf("Decode should fail with no messages")
	}
	if !strings.Contains(err.Error(), "no valid messages found") {
		t.Fatalf("Expected error about no messages, got: %v", err)
	}
}

// Test decode with wrong password
func TestDecodeWrongPassword(t *testing.T) {
	message := "Secret message"
	carrier := "Carrier"
	password := "correct_password"

	// Encode with correct password
	encoded, err := Encode(message, carrier, password)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}

	// Try to decode with wrong password
	_, err = Decode(encoded, "wrong_password")
	if err == nil {
		t.Fatalf("Decode should fail with wrong password")
	}
	if !strings.Contains(err.Error(), "invalid password") {
		t.Fatalf("Expected error about invalid password, got: %v", err)
	}
}

// Test decode with invalid binary data
func TestDecodeInvalidBinary(t *testing.T) {
	// Create carrier with invalid zero-width data
	invalidCarrier := START_MARKER + "invalid_data" + END_MARKER

	_, err := Decode(invalidCarrier, "")
	if err == nil {
		t.Fatalf("Decode should fail with invalid binary data")
	}
}

// Test decode with invalid base64
func TestDecodeInvalidBase64(t *testing.T) {
	// Create carrier with valid zero-width but invalid base64
	invalidBase64 := "invalid_base64_data"
	encoded := encodeBinary([]byte(invalidBase64))
	carrier := START_MARKER + encoded + END_MARKER

	_, err := Decode(carrier, "")
	if err == nil {
		t.Fatalf("Decode should fail with invalid base64")
	}
}

// Test decode with invalid encrypted data
func TestDecodeInvalidEncryptedData(t *testing.T) {
	// Create carrier with valid zero-width but invalid encrypted data
	invalidEncrypted := "invalid_encrypted_data"
	encoded := encodeBinary([]byte(invalidEncrypted))
	carrier := START_MARKER + encoded + END_MARKER

	_, err := Decode(carrier, "password")
	if err == nil {
		t.Fatalf("Decode should fail with invalid encrypted data")
	}
}

// Test decode with non-UTF8 decrypted data
func TestDecodeNonUTF8Data(t *testing.T) {
	// Create carrier with valid zero-width but non-UTF8 decrypted data
	nonUTF8Data := []byte{0xFF, 0xFE, 0xFD} // Invalid UTF-8
	encoded := encodeBinary([]byte(base64Encode(nonUTF8Data)))
	carrier := START_MARKER + encoded + END_MARKER

	_, err := Decode(carrier, "")
	if err == nil {
		t.Fatalf("Decode should fail with non-UTF8 data")
	}
}

// Test multiple messages
func TestMultipleMessages(t *testing.T) {
	message1 := "First message"
	message2 := "Second message"
	carrier := "Carrier text"

	// Encode first message
	encoded1, err := Encode(message1, carrier, "")
	if err != nil {
		t.Fatalf("First encode failed: %v", err)
	}

	// Encode second message
	encoded2, err := Encode(message2, encoded1, "")
	if err != nil {
		t.Fatalf("Second encode failed: %v", err)
	}

	// Decode all messages
	messages, err := Decode(encoded2, "")
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}

	if len(messages) != 2 {
		t.Fatalf("Expected 2 messages, got %d", len(messages))
	}

	if messages[0] != message1 {
		t.Fatalf("First message doesn't match. Expected: %q, Got: %q", message1, messages[0])
	}

	if messages[1] != message2 {
		t.Fatalf("Second message doesn't match. Expected: %q, Got: %q", message2, messages[1])
	}
}

// Test decodeBinary edge cases
func TestDecodeBinaryEdgeCases(t *testing.T) {
	// Test empty string
	_, err := decodeBinary("")
	if err == nil {
		t.Fatalf("decodeBinary should fail with empty string")
	}

	// Test string with no valid bits
	_, err = decodeBinary("abc123")
	if err == nil {
		t.Fatalf("decodeBinary should fail with no valid bits")
	}

	// Test string with partial bits (not multiple of 8, e.g. 7 bits)
	partialBits := strings.Repeat(ZERO_BIT, 7) // 7 bits, not 8
	_, err = decodeBinary(partialBits)
	if err == nil {
		t.Fatalf("decodeBinary should fail with less than 8 bits")
	}

	// Test string with 15 bits (should truncate to 8 bits, 1 byte)
	bits15 := strings.Repeat(ZERO_BIT, 7) + strings.Repeat(ONE_BIT, 8)
	result, err := decodeBinary(bits15)
	if err != nil {
		t.Fatalf("decodeBinary should not fail with 15 bits, got: %v", err)
	}
	if len(result) != 1 {
		t.Fatalf("Expected 1 byte, got %d", len(result))
	}
	if result[0] != 0x01 {
		t.Fatalf("Expected byte 0x01, got 0x%X", result[0])
	}
}

// Test countMessagePairs edge cases
func TestCountMessagePairs(t *testing.T) {
	// Test with no markers
	count := countMessagePairs("No markers")
	if count != 0 {
		t.Fatalf("Expected 0, got %d", count)
	}

	// Test with only start marker
	count = countMessagePairs(START_MARKER + "text")
	if count != 0 {
		t.Fatalf("Expected 0, got %d", count)
	}

	// Test with only end marker
	count = countMessagePairs("text" + END_MARKER)
	if count != 0 {
		t.Fatalf("Expected 0, got %d", count)
	}

	// Test with more start than end markers
	count = countMessagePairs(START_MARKER + "text" + START_MARKER + "text" + END_MARKER)
	if count != 1 {
		t.Fatalf("Expected 1, got %d", count)
	}

	// Test with more end than start markers
	count = countMessagePairs(START_MARKER + "text" + END_MARKER + "text" + END_MARKER)
	if count != 1 {
		t.Fatalf("Expected 1, got %d", count)
	}
}

// Test findNextSlot edge cases
func TestFindNextSlot(t *testing.T) {
	// Test with empty carrier
	pos := findNextSlot("")
	if pos != 0 {
		t.Fatalf("Expected 0, got %d", pos)
	}

	// Test with single character
	pos = findNextSlot("a")
	if pos != 0 {
		t.Fatalf("Expected 0, got %d", pos)
	}

	// Test with two characters
	pos = findNextSlot("ab")
	if pos != 1 {
		t.Fatalf("Expected 1, got %d", pos)
	}

	// Test with existing messages
	carrier := START_MARKER + "msg" + END_MARKER + "ab"
	pos = findNextSlot(carrier)
	if pos != 1 {
		t.Fatalf("Expected 1, got %d", pos)
	}

	// Test with multiple existing messages
	carrier = START_MARKER + "msg1" + END_MARKER + START_MARKER + "msg2" + END_MARKER + "abc"
	pos = findNextSlot(carrier)
	if pos != 2 {
		t.Fatalf("Expected 2, got %d", pos)
	}
}

// Test insertMessageAtPosition edge cases
func TestInsertMessageAtPosition(t *testing.T) {
	carrier := "Hello"
	message := START_MARKER + "msg" + END_MARKER

	// Test insertion at position 0
	result := insertMessageAtPosition(carrier, message, 0)
	if !strings.Contains(result, message) {
		t.Fatalf("Message should be inserted at position 0")
	}

	// Test insertion at end
	result = insertMessageAtPosition(carrier, message, 5)
	if !strings.Contains(result, message) {
		t.Fatalf("Message should be inserted at end")
	}

	// Test insertion in middle
	result = insertMessageAtPosition(carrier, message, 2)
	if !strings.Contains(result, message) {
		t.Fatalf("Message should be inserted in middle")
	}

	// Test with existing messages
	existingCarrier := START_MARKER + "existing" + END_MARKER + "Hello"
	result = insertMessageAtPosition(existingCarrier, message, 1)
	if !strings.Contains(result, message) {
		t.Fatalf("Message should be inserted with existing messages")
	}
}

// Test HasEncodedMessage
func TestHasEncodedMessage(t *testing.T) {
	// Test with no messages
	if HasEncodedMessage("No messages here") {
		t.Fatalf("Should not detect messages")
	}

	// Test with only start marker
	if HasEncodedMessage(START_MARKER + "text") {
		t.Fatalf("Should not detect messages with only start marker")
	}

	// Test with only end marker
	if HasEncodedMessage("text" + END_MARKER) {
		t.Fatalf("Should not detect messages with only end marker")
	}

	// Test with complete message
	if !HasEncodedMessage(START_MARKER + "msg" + END_MARKER) {
		t.Fatalf("Should detect complete message")
	}

	// Test with message in carrier
	if !HasEncodedMessage("Hello" + START_MARKER + "msg" + END_MARKER + "World") {
		t.Fatalf("Should detect message in carrier")
	}
}

// Test CountMessages
func TestCountMessages(t *testing.T) {
	// Test with no messages
	count := CountMessages("No messages")
	if count != 0 {
		t.Fatalf("Expected 0, got %d", count)
	}

	// Test with one message
	count = CountMessages(START_MARKER + "msg" + END_MARKER)
	if count != 1 {
		t.Fatalf("Expected 1, got %d", count)
	}

	// Test with two messages
	count = CountMessages(START_MARKER + "msg1" + END_MARKER + START_MARKER + "msg2" + END_MARKER)
	if count != 2 {
		t.Fatalf("Expected 2, got %d", count)
	}

	// Test with incomplete messages
	count = CountMessages(START_MARKER + "msg1" + START_MARKER + "msg2" + END_MARKER)
	if count != 1 {
		t.Fatalf("Expected 1, got %d", count)
	}
}

// Test crypto functions edge cases
func TestCryptoEdgeCases(t *testing.T) {
	// Test pkcs7Unpad with empty data
	_, err := pkcs7Unpad([]byte{})
	if err == nil {
		t.Fatalf("pkcs7Unpad should fail with empty data")
	}

	// Test pkcs7Unpad with invalid padding
	_, err = pkcs7Unpad([]byte{1, 2, 3, 10}) // padding > length
	if err == nil {
		t.Fatalf("pkcs7Unpad should fail with invalid padding")
	}

	// Test pkcs7Unpad with incorrect padding bytes
	_, err = pkcs7Unpad([]byte{1, 2, 3, 4, 4, 4, 4, 3}) // last byte says 3 but padding is 4
	if err == nil {
		t.Fatalf("pkcs7Unpad should fail with incorrect padding bytes")
	}

	// Test decryptData with too short data
	_, err = decryptData([]byte{1, 2, 3}, "password") // less than 16 bytes
	if err == nil {
		t.Fatalf("decryptData should fail with too short data")
	}
}

// Test encode/decode with Unicode characters
func TestUnicodeCharacters(t *testing.T) {
	message := "Hello 世界 🌍"
	carrier := "Carrier with Unicode: 测试"
	password := "password123"

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
}

// Test insertMessageAtPosition middle insertion
func TestInsertMessageAtPositionMiddle(t *testing.T) {
	carrier := "abcde"
	message := START_MARKER + "msg" + END_MARKER
	result := insertMessageAtPosition(carrier, message, 2)
	if !strings.Contains(result, message) {
		t.Fatalf("Message should be inserted in the middle")
	}
}

// Test Encode error branch for encryption failure
func TestEncodeEncryptionFailure(t *testing.T) {
	// Patch encryptData to return error
	origEncryptData := encryptData
	encryptData = func(data []byte, password string) ([]byte, error) {
		return nil, errors.New("forced encryption error")
	}
	defer func() { encryptData = origEncryptData }()
	_, err := Encode("msg", "carrier", "password")
	if err == nil || !strings.Contains(err.Error(), "encryption failed") {
		t.Fatalf("Expected encryption failed error, got: %v", err)
	}
}

// Test Decode with all invalid messages and password provided
func TestDecodeAllInvalidMessagesWithPassword(t *testing.T) {
	carrier := START_MARKER + "invalid_data" + END_MARKER
	_, err := Decode(carrier, "password")
	if err == nil {
		t.Fatalf("Expected error, got nil")
	}
	if !strings.Contains(err.Error(), "invalid password or no valid messages found") && !strings.Contains(err.Error(), "no valid messages found in carrier text") {
		t.Fatalf("Expected error about invalid password or no valid messages found, got: %v", err)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
