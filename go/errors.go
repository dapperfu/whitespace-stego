package whitespacestego

import "fmt"

// StegoError represents an error in steganography operations
type StegoError struct {
	Type    string
	Message string
}

func (e *StegoError) Error() string {
	return fmt.Sprintf("%s: %s", e.Type, e.Message)
}

// NewEncodingError creates a new encoding error
func NewEncodingError(message string) *StegoError {
	return &StegoError{Type: "Encoding", Message: message}
}

// NewDecodingError creates a new decoding error
func NewDecodingError(message string) *StegoError {
	return &StegoError{Type: "Decoding", Message: message}
}

