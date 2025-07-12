package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"errors"
	"fmt"
)

// deriveKey derives a 32-byte key from password using SHA-256
func deriveKey(password string) []byte {
	hash := sha256.Sum256([]byte(password))
	return hash[:]
}

// encryptData encrypts data using AES-256-CBC with PKCS7 padding
var encryptData = func(data []byte, password string) ([]byte, error) {
	key := deriveKey(password)

	// Create AES cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("failed to create cipher: %w", err)
	}

	// Generate random IV
	iv := make([]byte, aes.BlockSize)
	if _, err := rand.Read(iv); err != nil {
		return nil, fmt.Errorf("failed to generate IV: %w", err)
	}

	// Pad data to block size
	paddedData := pkcs7Pad(data, aes.BlockSize)

	// Encrypt
	ciphertext := make([]byte, len(paddedData))
	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext, paddedData)

	// Return IV + ciphertext
	result := make([]byte, 0, len(iv)+len(ciphertext))
	result = append(result, iv...)
	result = append(result, ciphertext...)

	return result, nil
}

// decryptData decrypts data using AES-256-CBC with PKCS7 padding
var decryptData = func(data []byte, password string) ([]byte, error) {
	if len(data) < aes.BlockSize {
		return nil, errors.New("invalid encrypted data: too short")
	}

	key := deriveKey(password)

	// Create AES cipher
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, fmt.Errorf("failed to create cipher: %w", err)
	}

	// Extract IV and ciphertext
	iv := data[:aes.BlockSize]
	ciphertext := data[aes.BlockSize:]

	// Decrypt
	plaintext := make([]byte, len(ciphertext))
	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(plaintext, ciphertext)

	// Remove padding
	unpadded, err := pkcs7Unpad(plaintext)
	if err != nil {
		return nil, fmt.Errorf("failed to remove padding: %w", err)
	}

	return unpadded, nil
}

// pkcs7Pad adds PKCS7 padding to data
func pkcs7Pad(data []byte, blockSize int) []byte {
	padding := blockSize - (len(data) % blockSize)
	padtext := make([]byte, padding)
	for i := range padtext {
		padtext[i] = byte(padding)
	}
	return append(data, padtext...)
}

// pkcs7Unpad removes PKCS7 padding from data
func pkcs7Unpad(data []byte) ([]byte, error) {
	length := len(data)
	if length == 0 {
		return nil, errors.New("invalid padding: empty data")
	}

	padding := int(data[length-1])
	if padding > length {
		return nil, errors.New("invalid padding: padding too large")
	}

	// Verify padding
	for i := length - padding; i < length; i++ {
		if data[i] != byte(padding) {
			return nil, errors.New("invalid padding: incorrect padding bytes")
		}
	}

	return data[:length-padding], nil
}

// base64Encode encodes data to base64 string
func base64Encode(data []byte) string {
	return base64.StdEncoding.EncodeToString(data)
}

// base64Decode decodes base64 string to bytes
func base64Decode(s string) ([]byte, error) {
	return base64.StdEncoding.DecodeString(s)
}
