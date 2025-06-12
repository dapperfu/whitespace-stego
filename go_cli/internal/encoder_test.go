package internal

import (
	"testing"
)

func TestEncoder_Encode(t *testing.T) {
	tests := []struct {
		name     string
		message  string
		carrier  string
		password string
		wantErr  bool
	}{
		{
			name:     "Simple ASCII message",
			message:  "Hello, World!",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Unicode message",
			message:  "Hello, 世界!",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Empty message",
			message:  "",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Message with carrier",
			message:  "Secret message",
			carrier:  "This is a carrier text",
			password: "",
			wantErr:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			encoder := NewEncoder(tt.password)
			encoded, err := encoder.Encode(tt.message, tt.carrier)
			if (err != nil) != tt.wantErr {
				t.Errorf("Encoder.Encode() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && encoded == "" {
				t.Error("Encoder.Encode() returned empty string")
			}
		})
	}
}

func TestEncoder_EncodeWithLength(t *testing.T) {
	tests := []struct {
		name     string
		message  string
		carrier  string
		password string
		wantErr  bool
	}{
		{
			name:     "Simple ASCII message",
			message:  "Hello, World!",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Unicode message",
			message:  "Hello, 世界!",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Empty message",
			message:  "",
			carrier:  "",
			password: "",
			wantErr:  false,
		},
		{
			name:     "Message with carrier",
			message:  "Secret message",
			carrier:  "This is a carrier text",
			password: "",
			wantErr:  false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			encoder := NewEncoder(tt.password)
			encoded, err := encoder.EncodeWithLength(tt.message, tt.carrier)
			if (err != nil) != tt.wantErr {
				t.Errorf("Encoder.EncodeWithLength() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !tt.wantErr && encoded == "" {
				t.Error("Encoder.EncodeWithLength() returned empty string")
			}
		})
	}
}
