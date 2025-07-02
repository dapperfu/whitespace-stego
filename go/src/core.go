// Package whitespace_stego provides core functionality for encoding and decoding messages
// using zero-width Unicode whitespace characters.
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"strings"
)

// Zero-width characters for encoding
const (
	ZERO_BIT     = "\u200b" // Zero-width space
	ONE_BIT      = "\u200d" // Zero-width joiner
	START_MARKER = "\ufeff" // Zero-width no-break space
	END_MARKER   = "\u200c" // Zero-width non-joiner
)

// encodeBinary encodes binary data into zero-width characters
func encodeBinary(data []byte) string {
	var result strings.Builder
	for _, b := range data {
		for i := 7; i >= 0; i-- {
			if (b>>i)&1 == 1 {
				result.WriteString(ONE_BIT)
			} else {
				result.WriteString(ZERO_BIT)
			}
		}
	}
	return result.String()
}

// decodeBinary decodes zero-width characters back to binary data
func decodeBinary(encoded string) ([]byte, error) {
	// Filter out only the zero-width characters we care about
	var filtered strings.Builder
	for _, char := range encoded {
		if char == rune(ZERO_BIT[0]) || char == rune(ONE_BIT[0]) {
			filtered.WriteRune(char)
		}
	}

	filteredStr := filtered.String()
	if len(filteredStr) == 0 {
		return nil, fmt.Errorf("no valid binary data found")
	}

	// Ensure the binary string length is a multiple of 8
	if len(filteredStr)%8 != 0 {
		filteredStr = filteredStr[:len(filteredStr)-(len(filteredStr)%8)]
	}

	if len(filteredStr) == 0 {
		return nil, fmt.Errorf("no valid binary data found after truncation")
	}

	// Convert to bytes
	result := make([]byte, len(filteredStr)/8)
	for i := 0; i < len(filteredStr); i += 8 {
		var b byte
		for j := 0; j < 8; j++ {
			if filteredStr[i+j] == ONE_BIT[0] {
				b |= 1 << (7 - j)
			}
		}
		result[i/8] = b
	}

	return result, nil
}

// deriveKey derives a 32-byte key from password (same as other implementations)
func deriveKey(password string) []byte {
	hash := sha256.Sum256([]byte(password))
	return hash[:]
}

// encryptData encrypts data using AES-256-CBC with PKCS7 padding
func encryptData(data []byte, password string) ([]byte, error) {
	key := deriveKey(password)

	// Generate random IV
	iv := make([]byte, aes.BlockSize)
	if _, err := rand.Read(iv); err != nil {
		return nil, fmt.Errorf("failed to generate IV: %w", err)
	}

	// Create cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("failed to create cipher: %w", err)
	}

	// PKCS7 padding
	padding := aes.BlockSize - (len(data) % aes.BlockSize)
	paddedData := make([]byte, len(data)+padding)
	copy(paddedData, data)
	for i := len(data); i < len(paddedData); i++ {
		paddedData[i] = byte(padding)
	}

	// Encrypt
	ciphertext := make([]byte, len(paddedData))
	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext, paddedData)

	// Return IV + ciphertext
	result := make([]byte, len(iv)+len(ciphertext))
	copy(result, iv)
	copy(result[len(iv):], ciphertext)

	return result, nil
}

// decryptData decrypts data using AES-256-CBC with PKCS7 padding
func decryptData(data []byte, password string) ([]byte, error) {
	if len(data) < aes.BlockSize {
		return nil, fmt.Errorf("invalid encrypted data: too short")
	}

	key := deriveKey(password)

	// Extract IV and ciphertext
	iv := data[:aes.BlockSize]
	ciphertext := data[aes.BlockSize:]

	// Create cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("failed to create cipher: %w", err)
	}

	// Decrypt
	if len(ciphertext)%aes.BlockSize != 0 {
		return nil, fmt.Errorf("invalid ciphertext length")
	}

	plaintext := make([]byte, len(ciphertext))
	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(plaintext, ciphertext)

	// Remove PKCS7 padding
	if len(plaintext) == 0 {
		return nil, fmt.Errorf("invalid plaintext")
	}

	padding := int(plaintext[len(plaintext)-1])
	if padding > aes.BlockSize || padding == 0 {
		return nil, fmt.Errorf("invalid padding")
	}

	// Verify padding
	for i := len(plaintext) - padding; i < len(plaintext); i++ {
		if plaintext[i] != byte(padding) {
			return nil, fmt.Errorf("invalid padding")
		}
	}

	return plaintext[:len(plaintext)-padding], nil
}

// countMessagePairs counts the number of start/end marker pairs in the carrier text
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
	existingMessages := countMessagePairs(carrier)

	// If no existing messages, place after first character
	if existingMessages == 0 {
		if len(carrier) > 0 {
			return 1
		}
		return 0
	}

	// For subsequent messages, place after the last character
	return len(carrier)
}

// insertMessageAtPosition inserts a message at a specific position in the carrier
func insertMessageAtPosition(carrier string, encodedMessage string, position int) string {
	if position == 0 {
		return encodedMessage + carrier
	}
	if position >= len(carrier) {
		return carrier + encodedMessage
	}
	return carrier[:position] + encodedMessage + carrier[position:]
}

// Encode encodes a message into a carrier using zero-width characters
func Encode(message string, carrier string, password string) (string, error) {
	// Base64 encode the message
	encodedBytes := base64.StdEncoding.EncodeToString([]byte(message))

	// Encrypt if password provided
	var finalData []byte
	var err error
	if password != "" {
		finalData, err = encryptData([]byte(encodedBytes), password)
		if err != nil {
			return "", fmt.Errorf("failed to encrypt data: %w", err)
		}
	} else {
		finalData = []byte(encodedBytes)
	}

	// Encode to binary
	binaryEncoded := encodeBinary(finalData)

	// Create the full encoded message with markers
	encodedMessage := START_MARKER + binaryEncoded + END_MARKER

	// Find insertion position
	position := findNextSlot(carrier)

	// Insert the message
	result := insertMessageAtPosition(carrier, encodedMessage, position)

	return result, nil
}

// BadPasswordError represents an error when the wrong password is used
type BadPasswordError struct {
	message string
}

func (e BadPasswordError) Error() string {
	return e.message
}

// Decode decodes messages from a carrier
func Decode(carrier string, password string) ([]string, error) {
	var messages []string

	// Find all start markers
	startPositions := make([]int, 0)
	for i := 0; i < len(carrier); {
		pos := strings.Index(carrier[i:], START_MARKER)
		if pos == -1 {
			break
		}
		startPositions = append(startPositions, i+pos)
		i += pos + len(START_MARKER)
	}

	// Find all end markers
	endPositions := make([]int, 0)
	for i := 0; i < len(carrier); {
		pos := strings.Index(carrier[i:], END_MARKER)
		if pos == -1 {
			break
		}
		endPositions = append(endPositions, i+pos)
		i += pos + len(END_MARKER)
	}

	// Process each message
	for i := 0; i < len(startPositions) && i < len(endPositions); i++ {
		startPos := startPositions[i]
		endPos := endPositions[i]

		if startPos >= endPos {
			continue
		}

		// Extract the encoded data between markers
		encodedData := carrier[startPos+len(START_MARKER) : endPos]

		// Decode binary
		decodedBytes, err := decodeBinary(encodedData)
		if err != nil {
			continue // Skip invalid messages
		}

		// Decrypt if password provided
		var finalData []byte
		if password != "" {
			finalData, err = decryptData(decodedBytes, password)
			if err != nil {
				// Try without password
				finalData = decodedBytes
			}
		} else {
			finalData = decodedBytes
		}

		// Base64 decode
		decodedBytes, err = base64.StdEncoding.DecodeString(string(finalData))
		if err != nil {
			continue // Skip invalid messages
		}

		messages = append(messages, string(decodedBytes))
	}

	return messages, nil
}

// HasEncodedMessage checks if a text contains encoded messages
func HasEncodedMessage(text string) bool {
	return strings.Contains(text, START_MARKER) && strings.Contains(text, END_MARKER)
}

// CountMessages counts the number of encoded messages in a carrier
func CountMessages(carrier string) int {
	return countMessagePairs(carrier)
}
