package internal

import (
	"encoding/binary"
	"fmt"
	"strings"
)

// Decoder handles the decoding of zero-width characters into messages
type Decoder struct {
	password []byte
}

// NewDecoder creates a new decoder instance
func NewDecoder(password string) *Decoder {
	return &Decoder{
		password: []byte(password),
	}
}

// Decode converts zero-width characters back into the original message
func (d *Decoder) Decode(encoded string) (string, error) {
	// Find the start and end delimiters
	startIdx := strings.Index(encoded, WordJoiner)
	if startIdx == -1 {
		return "", fmt.Errorf("start delimiter not found")
	}

	endIdx := strings.Index(encoded, InvisiblePlus)
	if endIdx == -1 {
		return "", fmt.Errorf("end delimiter not found")
	}

	// Extract the encoded message
	encodedMsg := encoded[startIdx+len(WordJoiner) : endIdx]

	// Convert zero-width characters back to bytes
	var bytes []byte
	var currentByte byte
	var bitCount int

	for _, char := range encodedMsg {
		switch char {
		case '\u200B': // Zero-width space
			currentByte = (currentByte << 1) | 1
			bitCount++
		case '\u200C': // Zero-width non-joiner
			currentByte = (currentByte << 1)
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

	return string(bytes), nil
}

// DecodeWithLength decodes a message that includes its length
func (d *Decoder) DecodeWithLength(encoded string) (string, error) {
	// First, find the length part
	lengthEncoded, err := d.Decode(encoded)
	if err != nil {
		return "", fmt.Errorf("failed to decode length: %w", err)
	}

	// Convert length bytes to uint32
	if len(lengthEncoded) < 4 {
		return "", fmt.Errorf("invalid length encoding")
	}
	length := binary.BigEndian.Uint32([]byte(lengthEncoded[:4]))

	// Decode the actual message
	message, err := d.Decode(encoded)
	if err != nil {
		return "", fmt.Errorf("failed to decode message: %w", err)
	}

	// Verify message length
	if uint32(len(message)) != length {
		return "", fmt.Errorf("message length mismatch: expected %d, got %d", length, len(message))
	}

	return message, nil
}
