package whitespacestego

import (
	"testing"
)

func TestEncodeEmptyMessage(t *testing.T) {
	result, err := Encode("", nil)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}
	if len(result) == 0 {
		t.Error("Encoded result should not be empty")
	}
}

func TestEncodeSimpleMessage(t *testing.T) {
	message := "Hello, World!"
	result, err := Encode(message, nil)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}
	if len(result) == 0 {
		t.Error("Encoded result should not be empty")
	}
}

func TestRoundTrip(t *testing.T) {
	message := "Hello, World!"
	encoded, err := Encode(message, nil)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}
	decoded, err := Decode(encoded)
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}
	if decoded != message {
		t.Errorf("Round-trip failed: expected %q, got %q", message, decoded)
	}
}

func TestRoundTripUnicode(t *testing.T) {
	message := "Hello 🌍 你好"
	encoded, err := Encode(message, nil)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}
	decoded, err := Decode(encoded)
	if err != nil {
		t.Fatalf("Decode failed: %v", err)
	}
	if decoded != message {
		t.Errorf("Round-trip failed: expected %q, got %q", message, decoded)
	}
}

func TestEncodeWithCarrier(t *testing.T) {
	message := "Secret"
	carrier := "This is normal text."
	encoded, err := Encode(message, &carrier)
	if err != nil {
		t.Fatalf("Encode failed: %v", err)
	}
	if len(encoded) <= len(carrier) {
		t.Error("Encoded result should be longer than carrier")
	}
}

