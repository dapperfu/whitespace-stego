package whitespacestego

import (
	"encoding/base64"
	"fmt"
	"strings"
)

// Unicode control characters
const (
	controlStart = "\u2060" // U+2060 Word Joiner
	controlEnd   = "\u2063" // U+2063 Invisible Separator
	bit0         = "\u200B" // U+200B Zero Width Space
	bit1         = "\u200C" // U+200C Zero Width Non-Joiner
)

// Encode encodes a message into invisible Unicode characters.
//
// Parameters:
//   - message: The message to encode. Can be any Unicode string.
//   - carrier: Optional carrier text to embed the encoded message in.
//     If provided, the encoded payload will be inserted after
//     the first character of the carrier text.
//
// Returns:
//   - Encoded string with invisible Unicode characters
//   - Error if encoding fails
func Encode(message string, carrier *string) (string, error) {
	// Convert message to UTF-8 bytes
	utf8Bytes := []byte(message)

	// Encode to Base64
	base64Str := base64.StdEncoding.EncodeToString(utf8Bytes)

	// Convert Base64 string to binary representation
	var binaryBits strings.Builder
	for _, byte := range []byte(base64Str) {
		// Convert each byte to 8-bit binary (MSB to LSB)
		binaryBits.WriteString(fmt.Sprintf("%08b", byte))
	}

	// Map binary bits to invisible Unicode characters
	var encodedPayload strings.Builder
	for _, bit := range binaryBits.String() {
		switch bit {
		case '0':
			encodedPayload.WriteString(bit0)
		case '1':
			encodedPayload.WriteString(bit1)
		default:
			return "", fmt.Errorf("invalid bit value: %c", bit)
		}
	}

	// Wrap payload with control markers
	encodedMessage := controlStart + encodedPayload.String() + controlEnd

	// If carrier text is provided, embed the encoded message
	if carrier != nil && len(*carrier) > 0 {
		// Check if carrier contains control characters
		if strings.Contains(*carrier, controlStart) || strings.Contains(*carrier, controlEnd) {
			return "", fmt.Errorf("carrier text contains control characters. This may cause decoding issues")
		}

		// Insert after first character
		firstChar := string(([]rune(*carrier))[0])
		rest := string(([]rune(*carrier))[1:])
		return firstChar + encodedMessage + rest, nil
	}

	return encodedMessage, nil
}

