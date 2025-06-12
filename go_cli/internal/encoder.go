package internal

import (
	"encoding/binary"
	"fmt"
)

const (
	// Zero-width characters used for encoding
	ZeroWidthSpace     = "\u200B" // Zero-width space
	ZeroWidthNonJoiner = "\u200C" // Zero-width non-joiner
	WordJoiner         = "\u2060" // Word joiner (start delimiter)
	InvisiblePlus      = "\u2061" // Invisible plus (end delimiter)
)

// Encoder handles the encoding of messages into zero-width characters
type Encoder struct {
	password string
}

// NewEncoder creates a new encoder instance
func NewEncoder(password string) *Encoder {
	return &Encoder{
		password: password,
	}
}

// Encode converts a message into zero-width characters
func (e *Encoder) Encode(message string, carrier string) (string, error) {
	// Encrypt the message if a password is provided
	var msgBytes []byte
	var err error
	if e.password != "" {
		encrypted, err := Encrypt([]byte(message), e.password)
		if err != nil {
			return "", fmt.Errorf("failed to encrypt message: %w", err)
		}
		msgBytes = []byte(encrypted)
	} else {
		msgBytes = []byte(message)
	}

	// Create the encoded string
	var encoded string

	// Add start delimiter
	encoded += WordJoiner

	// Encode each byte
	for _, b := range msgBytes {
		// Convert byte to binary string
		for i := 7; i >= 0; i-- {
			bit := (b >> i) & 1
			if bit == 1 {
				encoded += ZeroWidthSpace
			} else {
				encoded += ZeroWidthNonJoiner
			}
		}
	}

	// Add end delimiter
	encoded += InvisiblePlus

	// If carrier is provided, insert the encoded message into it
	if carrier != "" {
		// For now, just append to carrier
		// TODO: Implement proper carrier insertion logic
		encoded = carrier + encoded
	}

	return encoded, nil
}

// EncodeWithLength encodes a message and includes its length
func (e *Encoder) EncodeWithLength(message string, carrier string) (string, error) {
	// Convert message length to 4 bytes
	lengthBytes := make([]byte, 4)
	binary.BigEndian.PutUint32(lengthBytes, uint32(len(message)))

	// Encode length first
	lengthEncoded, err := e.Encode(string(lengthBytes), "")
	if err != nil {
		return "", fmt.Errorf("failed to encode length: %w", err)
	}

	// Encode message
	msgEncoded, err := e.Encode(message, "")
	if err != nil {
		return "", fmt.Errorf("failed to encode message: %w", err)
	}

	// Combine length and message
	encoded := lengthEncoded + msgEncoded

	// If carrier is provided, insert the encoded message into it
	if carrier != "" {
		// For now, just append to carrier
		// TODO: Implement proper carrier insertion logic
		encoded = carrier + encoded
	}

	return encoded, nil
}
