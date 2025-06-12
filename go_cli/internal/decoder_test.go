package internal

import (
	"testing"
)

func TestDecoder_Decode(t *testing.T) {
	// Create test encoder
	encoder := NewEncoder("")

	tests := []struct {
		name     string
		message  string
		password string
		wantErr  bool
	}{
		{
			name:     "Simple ASCII message",
			message:  "Hello, World!",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Unicode message",
			message:  "Hello, 世界!",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Empty message",
			message:  "",
			password: "",
			wantErr:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// First encode the message
			encoded, err := encoder.Encode(tt.message, "")
			if err != nil {
				t.Fatalf("Failed to encode test message: %v", err)
			}

			// Then try to decode it
			decoder := NewDecoder(tt.password)
			decoded, err := decoder.Decode(encoded)
			if (err != nil) != tt.wantErr {
				t.Errorf("Decoder.Decode() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && decoded != tt.message {
				t.Errorf("Decoder.Decode() = %v, want %v", decoded, tt.message)
			}
		})
	}
}

func TestDecoder_DecodeWithLength(t *testing.T) {
	// Create test encoder
	encoder := NewEncoder("")

	tests := []struct {
		name     string
		message  string
		password string
		wantErr  bool
	}{
		{
			name:     "Simple ASCII message",
			message:  "Hello, World!",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Unicode message",
			message:  "Hello, 世界!",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Empty message",
			message:  "",
			password: "",
			wantErr:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// First encode the message
			encoded, err := encoder.EncodeWithLength(tt.message, "")
			if err != nil {
				t.Fatalf("Failed to encode test message: %v", err)
			}

			// Then try to decode it
			decoder := NewDecoder(tt.password)
			decoded, err := decoder.DecodeWithLength(encoded)
			if (err != nil) != tt.wantErr {
				t.Errorf("Decoder.DecodeWithLength() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && decoded != tt.message {
				t.Errorf("Decoder.DecodeWithLength() = %v, want %v", decoded, tt.message)
			}
		})
	}
}
