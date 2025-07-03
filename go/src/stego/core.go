package stego

import (
	"errors"
	"fmt"
	"regexp"
	"strings"
	"unicode/utf8"
)

var zeroBitRune = []rune(ZERO_BIT)[0]
var oneBitRune = []rune(ONE_BIT)[0]

// encodeBinary converts bytes to zero-width characters
func encodeBinary(data []byte) string {
	var result strings.Builder
	for _, b := range data {
		for i := 7; i >= 0; i-- {
			if (b>>i)&1 == 1 {
				result.WriteRune(oneBitRune)
			} else {
				result.WriteRune(zeroBitRune)
			}
		}
	}
	return result.String()
}

// decodeBinary converts zero-width characters back to bytes
func decodeBinary(encoded string) ([]byte, error) {
	// Filter out non-zero-width characters
	var filtered strings.Builder
	for _, r := range encoded {
		if r == oneBitRune || r == zeroBitRune {
			filtered.WriteRune(r)
		}
	}

	// Convert to bitstring
	var bitstring strings.Builder
	for _, r := range filtered.String() {
		if r == oneBitRune {
			bitstring.WriteRune('1')
		} else {
			bitstring.WriteRune('0')
		}
	}

	// Convert bitstring to bytes
	bits := bitstring.String()
	if len(bits)%8 != 0 {
		// Truncate to multiple of 8
		bits = bits[:len(bits)-(len(bits)%8)]
	}

	if len(bits) == 0 {
		return nil, errors.New("no valid bits found")
	}

	result := make([]byte, len(bits)/8)
	for i := 0; i < len(bits); i += 8 {
		byteStr := bits[i : i+8]
		b := byte(0)
		for j, bit := range byteStr {
			if bit == '1' {
				b |= 1 << (7 - j)
			}
		}
		result[i/8] = b
	}

	return result, nil
}

// countMessagePairs counts the number of start/end marker pairs
func countMessagePairs(carrier string) int {
	startCount := strings.Count(carrier, START_MARKER)
	endCount := strings.Count(carrier, END_MARKER)
	if startCount < endCount {
		return startCount
	}
	return endCount
}

// findNextSlot finds the next available slot for encoding a message
func findNextSlot(carrier string) int {
	// Remove all encoded messages to get the original carrier
	pattern := regexp.MustCompile(regexp.QuoteMeta(START_MARKER) + ".*?" + regexp.QuoteMeta(END_MARKER))
	cleanedCarrier := pattern.ReplaceAllString(carrier, "")

	// Count how many messages are already encoded
	existingMessages := countMessagePairs(carrier)

	// If no existing messages, place after first character
	if existingMessages == 0 {
		if utf8.RuneCountInString(cleanedCarrier) > 1 {
			return 1
		}
		return 0
	}

	// For subsequent messages, place in slots between characters
	charCount := utf8.RuneCountInString(cleanedCarrier)
	if existingMessages < charCount-1 {
		return existingMessages + 1
	}
	// Place before the last visible character
	return charCount - 1
}

// insertMessageAtPosition inserts an encoded message at a specific position
func insertMessageAtPosition(carrier, encodedMessage string, position int) string {
	// Remove all encoded messages to get the original carrier
	pattern := regexp.MustCompile(regexp.QuoteMeta(START_MARKER) + ".*?" + regexp.QuoteMeta(END_MARKER))
	cleanedCarrier := pattern.ReplaceAllString(carrier, "")

	// Insert the encoded message at the correct position in the cleaned carrier
	var newCarrier string
	if position == 0 {
		newCarrier = encodedMessage + cleanedCarrier
	} else if position >= utf8.RuneCountInString(cleanedCarrier) {
		newCarrier = cleanedCarrier + encodedMessage
	} else {
		// Convert to rune slice for proper insertion
		runes := []rune(cleanedCarrier)
		var result strings.Builder
		for i, r := range runes {
			if i == position {
				result.WriteString(encodedMessage)
			}
			result.WriteRune(r)
		}
		newCarrier = result.String()
	}

	// Now, re-insert all previously encoded messages at their original positions
	result := newCarrier
	matches := pattern.FindAllStringIndex(carrier, -1)
	offset := 0

	for _, match := range matches {
		// Find the position in the cleaned carrier where this encoded message was originally
		pre := carrier[:match[0]]
		cleanedPre := pattern.ReplaceAllString(pre, "")
		insertPos := utf8.RuneCountInString(cleanedPre) + offset

		// Insert at the correct character position
		runes := []rune(result)
		var newResult strings.Builder
		for i, r := range runes {
			if i == insertPos {
				newResult.WriteString(carrier[match[0]:match[1]])
			}
			newResult.WriteRune(r)
		}
		if insertPos >= len(runes) {
			newResult.WriteString(carrier[match[0]:match[1]])
		}
		result = newResult.String()
		offset += utf8.RuneCountInString(carrier[match[0]:match[1]])
	}

	return result
}

// Encode encodes a message into carrier text using zero-width characters
func Encode(message, carrier, password string) (string, error) {
	// Check for empty message
	if message == "" {
		return "", errors.New("message must not be empty")
	}

	var data []byte

	// Encrypt if password provided, then base64 encode
	if password != "" {
		// Encrypt the original message first
		encrypted, err := encryptData([]byte(message), password)
		if err != nil {
			return "", fmt.Errorf("encryption failed: %w", err)
		}
		// Base64 encode the encrypted data to convert random bytes to safe ASCII
		data = []byte(base64Encode(encrypted))
	} else {
		// For non-password messages, base64 encode the original message
		data = []byte(base64Encode([]byte(message)))
	}

	// Convert to zero-width characters
	zeroWidth := encodeBinary(data)
	encodedMessage := START_MARKER + zeroWidth + END_MARKER

	// Handle carrier embedding
	if carrier == "" {
		return encodedMessage, nil
	}

	pos := findNextSlot(carrier)
	return insertMessageAtPosition(carrier, encodedMessage, pos), nil
}

// Decode decodes messages from carrier text using zero-width characters
func Decode(carrier, password string) ([]string, error) {
	// Find all start/end marker pairs
	pattern := regexp.MustCompile("(?s)" + regexp.QuoteMeta(START_MARKER) + "(.*?)" + regexp.QuoteMeta(END_MARKER))
	matches := pattern.FindAllStringSubmatch(carrier, -1)

	if len(matches) == 0 {
		return nil, errors.New("no valid messages found in carrier text")
	}

	var results []string
	passwordErrors := 0

	for _, match := range matches {
		zw := match[1]

		// Decode binary data
		data, err := decodeBinary(zw)
		if err != nil {
			continue
		}

		if password != "" {
			// Try to base64 decode and decrypt
			encrypted, err := base64Decode(string(data))
			if err != nil {
				passwordErrors++
				continue
			}

			decoded, err := decryptData(encrypted, password)
			if err != nil {
				passwordErrors++
				continue
			}

			// Ensure the result is valid UTF-8
			if !utf8.Valid(decoded) {
				passwordErrors++
				continue
			}

			results = append(results, string(decoded))
		} else {
			// Base64 decode the data directly
			decoded, _ := base64Decode(string(data))
			if !utf8.Valid(decoded) {
				continue
			}
			results = append(results, string(decoded))
		}
	}

	if len(results) == 0 {
		if password != "" && passwordErrors > 0 {
			return nil, errors.New("invalid password or no valid messages found in carrier text")
		}
		return nil, errors.New("no valid messages found in carrier text")
	}

	return results, nil
}

// HasEncodedMessage checks if the text contains encoded messages
func HasEncodedMessage(text string) bool {
	return strings.Contains(text, START_MARKER) && strings.Contains(text, END_MARKER)
}

// CountMessages counts the number of encoded messages in the text
func CountMessages(carrier string) int {
	return countMessagePairs(carrier)
}
