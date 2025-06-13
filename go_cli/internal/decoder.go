package internal

import (
	"encoding/base64"
	"encoding/binary"
	"fmt"
	"strings"
)

// Decoder handles the decoding of zero-width characters into messages
type Decoder struct {
	password string
}

// NewDecoder creates a new decoder instance
func NewDecoder(password string) *Decoder {
	return &Decoder{
		password: password,
	}
}

// Decode converts zero-width characters back into the original message
func (d *Decoder) Decode(encoded string) (string, error) {
	// Find the start and end delimiters
	startIdx := strings.Index(encoded, WordJoiner)
	if startIdx == -1 {
		return "", fmt.Errorf("start delimiter not found")
	}

	endIdx := strings.Index(encoded[startIdx:], InvisiblePlus)
	if endIdx == -1 {
		return "", fmt.Errorf("end delimiter not found")
	}
	endIdx += startIdx

	// Extract the encoded message
	encodedMsg := encoded[startIdx+len(WordJoiner) : endIdx]

	// Convert zero-width characters back to bytes
	var bytes []byte
	var currentByte byte
	var bitCount int

	for _, char := range encodedMsg {
		switch char {
		case '\u200B': // Zero-width space
			currentByte = (currentByte << 1) | 0
			bitCount++
		case '\u200C': // Zero-width non-joiner
			currentByte = (currentByte << 1) | 1
			bitCount++
		default:
			continue
		}

		if bitCount == 8 {
			bytes = append(bytes, currentByte)
			currentByte = 0
			bitCount = 0
		}
	}

	// Decrypt if password is set
	if d.password != "" {
		decrypted, err := Decrypt(string(bytes), d.password)
		if err != nil {
			return "", fmt.Errorf("failed to decrypt message: %w", err)
		}
		return string(decrypted), nil
	}

	// Try to decode as base64 first
	fmt.Printf("[DEBUG] Reconstructed base64: %q\n", string(bytes))
	decoded, err := base64.StdEncoding.DecodeString(string(bytes))
	if err == nil {
		return strings.TrimRight(string(decoded), "\n"), nil
	}

	// If base64 decoding fails, return raw bytes
	return string(bytes), nil
}

// DecodeWithLength decodes a message that includes its length
func (d *Decoder) DecodeWithLength(encoded string) (string, error) {
	// Try to find the first block (length)
	startIdx := strings.Index(encoded, WordJoiner)
	if startIdx == -1 {
		return "", fmt.Errorf("start delimiter for length not found")
	}
	endIdx := strings.Index(encoded, InvisiblePlus)
	if endIdx == -1 {
		return "", fmt.Errorf("end delimiter for length not found")
	}

	// Check if this is a single-block format (no length prefix)
	remaining := encoded[endIdx+len(InvisiblePlus):]
	if !strings.Contains(remaining, WordJoiner) {
		// Single-block format - decode directly
		messageBlock := encoded[startIdx : endIdx+len(InvisiblePlus)]
		return d.Decode(messageBlock)
	}

	// Two-block format - decode length first
	lengthBlock := encoded[startIdx : endIdx+len(InvisiblePlus)]
	lengthDecoded, err := d.Decode(lengthBlock)
	if err != nil {
		return "", fmt.Errorf("failed to decode length: %w", err)
	}
	if len(lengthDecoded) < 4 {
		return "", fmt.Errorf("invalid length encoding")
	}
	length := binary.BigEndian.Uint32([]byte(lengthDecoded[:4]))

	// Decode the message block
	startIdx2 := strings.Index(remaining, WordJoiner)
	if startIdx2 == -1 {
		return "", fmt.Errorf("start delimiter for message not found")
	}
	endIdx2 := strings.Index(remaining, InvisiblePlus)
	if endIdx2 == -1 {
		return "", fmt.Errorf("end delimiter for message not found")
	}
	messageBlock := remaining[startIdx2 : endIdx2+len(InvisiblePlus)]
	message, err := d.Decode(messageBlock)
	if err != nil {
		return "", fmt.Errorf("failed to decode message: %w", err)
	}
	if uint32(len(message)) != length {
		return "", fmt.Errorf("message length mismatch: expected %d, got %d", length, len(message))
	}
	return message, nil
}
