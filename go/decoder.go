package whitespacestego

import (
	"encoding/base64"
	"fmt"
	"strings"
)

// Decode decodes a message from invisible Unicode characters.
//
// Parameters:
//   - encodedText: Text containing the encoded message with control markers.
//
// Returns:
//   - Decoded original message
//   - Error if decoding fails
func Decode(encodedText string) (string, error) {
	// Find control markers
	startIdx := strings.Index(encodedText, controlStart)
	endIdx := strings.Index(encodedText, controlEnd)

	if startIdx == -1 {
		return "", fmt.Errorf("CONTROL_START marker (U+2060) not found")
	}
	if endIdx == -1 {
		return "", fmt.Errorf("CONTROL_END marker (U+2063) not found")
	}

	// Extract payload (between markers, excluding markers)
	payloadStart := startIdx + len(controlStart)
	payload := encodedText[payloadStart:endIdx]

	// Check if payload is empty
	if len(payload) == 0 {
		// Empty payload means empty message
		return "", nil
	}

	// Convert invisible characters to binary bits
	var binaryBits strings.Builder
	for _, char := range []rune(payload) {
		switch char {
		case []rune(bit0)[0]:
			binaryBits.WriteRune('0')
		case []rune(bit1)[0]:
			binaryBits.WriteRune('1')
		default:
			return "", fmt.Errorf("invalid character in payload: U+%04X. Only U+200B and U+200C are allowed", char)
		}
	}

	bitString := binaryBits.String()

	// Check if payload is complete (divisible by 8)
	if len(bitString)%8 != 0 {
		return "", fmt.Errorf("incomplete payload: %d bits (must be divisible by 8)", len(bitString))
	}

	// Group bits into 8-bit bytes
	bytesList := make([]byte, len(bitString)/8)
	for i := 0; i < len(bytesList); i++ {
		var byteValue byte
		for j := 0; j < 8; j++ {
			bit := bitString[i*8+j]
			if bit == '1' {
				byteValue |= 1 << (7 - j)
			} else if bit != '0' {
				return "", fmt.Errorf("invalid bit value: %c", bit)
			}
		}
		bytesList[i] = byteValue
	}

	// Convert bytes to Base64 string
	base64Str := string(bytesList)

	// Decode Base64 to UTF-8 bytes
	utf8Bytes, err := base64.StdEncoding.DecodeString(base64Str)
	if err != nil {
		return "", fmt.Errorf("Base64 decoding failed: %w", err)
	}

	// Decode UTF-8 bytes to original message
	message := string(utf8Bytes)
	return message, nil
}

