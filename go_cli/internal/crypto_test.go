package internal

import (
	"testing"
)

func TestEncryptDecrypt(t *testing.T) {
	tests := []struct {
		name     string
		message  string
		password string
		wantErr  bool
	}{
		{
			name:     "Simple ASCII message",
			message:  "Hello, World!",
			password: "test123",
			wantErr:  false,
		},
		{
			name:     "Unicode message",
			message:  "Hello, 世界!",
			password: "test123",
			wantErr:  false,
		},
		{
			name:     "Empty message",
			message:  "",
			password: "test123",
			wantErr:  false,
		},
		{
			name:     "No password",
			message:  "Secret message",
			password: "",
			wantErr:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Encrypt
			encrypted, err := Encrypt([]byte(tt.message), tt.password)
			if (err != nil) != tt.wantErr {
				t.Errorf("Encrypt() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && encrypted == "" {
				t.Error("Encrypt() returned empty string")
			}

			// Decrypt
			decrypted, err := Decrypt(encrypted, tt.password)
			if (err != nil) != tt.wantErr {
				t.Errorf("Decrypt() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && string(decrypted) != tt.message {
				t.Errorf("Decrypt() = %v, want %v", string(decrypted), tt.message)
			}
		})
	}
}

func TestEncryptDecryptWrongPassword(t *testing.T) {
	message := "Secret message"
	password := "correct123"
	wrongPassword := "wrong123"

	// Encrypt
	encrypted, err := Encrypt([]byte(message), password)
	if err != nil {
		t.Fatalf("Encrypt() error = %v", err)
	}

	// Try to decrypt with wrong password
	_, err = Decrypt(encrypted, wrongPassword)
	if err == nil {
		t.Error("Decrypt() with wrong password should fail")
	}
}
