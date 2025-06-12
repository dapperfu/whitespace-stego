package internal

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"errors"
	"fmt"
	"io"

	"golang.org/x/crypto/pbkdf2"
)

const (
	// Encryption parameters
	saltSize   = 16
	keySize    = 32 // AES-256
	iterations = 100000
	nonceSize  = 12 // GCM nonce size
	tagSize    = 16 // GCM tag size
)

// Encrypt encrypts data using AES-GCM with a password
func Encrypt(data []byte, password string) (string, error) {
	if len(password) == 0 {
		return string(data), nil
	}

	// Generate salt
	salt := make([]byte, saltSize)
	if _, err := io.ReadFull(rand.Reader, salt); err != nil {
		return "", fmt.Errorf("failed to generate salt: %w", err)
	}

	// Derive key
	key := pbkdf2.Key([]byte(password), salt, iterations, keySize, sha256.New)

	// Create cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return "", fmt.Errorf("failed to create cipher: %w", err)
	}

	// Create GCM
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return "", fmt.Errorf("failed to create GCM: %w", err)
	}

	// Generate nonce
	nonce := make([]byte, gcm.NonceSize())
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
		return "", fmt.Errorf("failed to generate nonce: %w", err)
	}

	// Encrypt
	ciphertext := gcm.Seal(nonce, nonce, data, nil)

	// Combine salt and ciphertext
	combined := make([]byte, 0, len(salt)+len(ciphertext))
	combined = append(combined, salt...)
	combined = append(combined, ciphertext...)

	// Base64 encode
	return base64.StdEncoding.EncodeToString(combined), nil
}

// Decrypt decrypts data using AES-GCM with a password
func Decrypt(encrypted string, password string) ([]byte, error) {
	if len(password) == 0 {
		return []byte(encrypted), nil
	}

	// Base64 decode
	combined, err := base64.StdEncoding.DecodeString(encrypted)
	if err != nil {
		return nil, fmt.Errorf("failed to decode base64: %w", err)
	}

	// Extract salt and ciphertext
	if len(combined) < saltSize {
		return nil, errors.New("encrypted data too short")
	}
	salt := combined[:saltSize]
	ciphertext := combined[saltSize:]

	// Derive key
	key := pbkdf2.Key([]byte(password), salt, iterations, keySize, sha256.New)

	// Create cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("failed to create cipher: %w", err)
	}

	// Create GCM
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, fmt.Errorf("failed to create GCM: %w", err)
	}

	// Extract nonce
	if len(ciphertext) < gcm.NonceSize() {
		return nil, errors.New("ciphertext too short")
	}
	nonce := ciphertext[:gcm.NonceSize()]
	ciphertext = ciphertext[gcm.NonceSize():]

	// Decrypt
	plaintext, err := gcm.Open(nil, nonce, ciphertext, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to decrypt: %w", err)
	}

	return plaintext, nil
}
