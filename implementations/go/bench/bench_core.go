// Benchmark core encode/decode functions for Go implementation.
//
// Build:
//
//	go build -o bench_core bench_core.go
//
// Run:
//
//	./bench_core
//
// NOTE: This file must use package 'main' to be runnable as an executable.
package main

import (
	"fmt"
	"strings"
	"time"

	"whitespace-stego-go/src/stego"
)

const (
	ITER           = 1000
	MSG_REPEAT     = 100
	CARRIER_REPEAT = 100
)

func main() {
	message := strings.Repeat("Secret message", MSG_REPEAT)
	carrier := strings.Repeat("This is the carrier text.", CARRIER_REPEAT)
	var encoded, decoded string
	var err error

	t0 := time.Now()
	for i := 0; i < ITER; i++ {
		encoded, err = stego.Encode(message, carrier, "")
		if err != nil {
			fmt.Printf("[WARN] encode error at iter %d\n", i)
			break
		}
	}
	t1 := time.Now()
	elapsed := t1.Sub(t0).Seconds()
	fmt.Printf("Go encode: %.2f ms total, %.2f us/call\n", elapsed*1000, elapsed/ITER*1e6)

	t0 = time.Now()
	for i := 0; i < ITER; i++ {
		var decodedArr []string
		decodedArr, err = stego.Decode(encoded, "")
		if err != nil || len(decodedArr) == 0 {
			fmt.Printf("[WARN] decode error at iter %d\n", i)
			break
		}
		decoded = decodedArr[0]
	}
	t1 = time.Now()
	elapsed = t1.Sub(t0).Seconds()
	fmt.Printf("Go decode: %.2f ms total, %.2f us/call\n", elapsed*1000, elapsed/ITER*1e6)
	// Prevent compiler from optimizing away 'decoded'
	fmt.Printf("Decoded length: %d\n", len(decoded))
}
