package main

import (
	"flag"
	"fmt"
	"io"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		printUsage()
		os.Exit(1)
	}

	command := os.Args[1]
	switch command {
	case "encode":
		encodeCommand()
	case "decode":
		decodeCommand()
	case "help":
		printUsage()
	default:
		fmt.Fprintf(os.Stderr, "Unknown command: %s\n", command)
		printUsage()
		os.Exit(1)
	}
}

func encodeCommand() {
	fs := flag.NewFlagSet("encode", flag.ExitOnError)

	var message string
	var carrierFile string
	var outputFile string
	var password string

	fs.StringVar(&message, "m", "", "Message to encode")
	fs.StringVar(&message, "message", "", "Message to encode")
	fs.StringVar(&carrierFile, "cf", "", "Carrier file path")
	fs.StringVar(&carrierFile, "carrier-file", "", "Carrier file path")
	fs.StringVar(&outputFile, "o", "", "Output file path")
	fs.StringVar(&outputFile, "output", "", "Output file path")
	fs.StringVar(&password, "p", "", "Password for encryption")
	fs.StringVar(&password, "password", "", "Password for encryption")

	fs.Parse(os.Args[2:])

	// Validate required arguments
	if message == "" {
		fmt.Fprintf(os.Stderr, "Error: message is required\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Read carrier text
	var carrier string
	if carrierFile != "" {
		carrierBytes, err := os.ReadFile(carrierFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading carrier file: %v\n", err)
			os.Exit(1)
		}
		carrier = string(carrierBytes)
	}

	// Encode the message
	encoded, err := Encode(message, carrier, password)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error encoding message: %v\n", err)
		os.Exit(1)
	}

	// Output the result
	if outputFile != "" {
		err := os.WriteFile(outputFile, []byte(encoded), 0644)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error writing output file: %v\n", err)
			os.Exit(1)
		}
	} else {
		fmt.Print(encoded)
	}
}

func decodeCommand() {
	fs := flag.NewFlagSet("decode", flag.ExitOnError)

	var carrierFile string
	var outputFile string
	var password string

	fs.StringVar(&carrierFile, "cf", "", "Carrier file path")
	fs.StringVar(&carrierFile, "carrier-file", "", "Carrier file path")
	fs.StringVar(&outputFile, "o", "", "Output file path")
	fs.StringVar(&outputFile, "output", "", "Output file path")
	fs.StringVar(&password, "p", "", "Password for decryption")
	fs.StringVar(&password, "password", "", "Password for decryption")

	fs.Parse(os.Args[2:])

	// Validate required arguments
	if carrierFile == "" {
		fmt.Fprintf(os.Stderr, "Error: carrier file is required\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Read carrier text
	carrierBytes, err := os.ReadFile(carrierFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading carrier file: %v\n", err)
		os.Exit(1)
	}
	carrier := string(carrierBytes)

	// Decode the message
	messages, err := Decode(carrier, password)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error decoding message: %v\n", err)
		os.Exit(1)
	}

	// Output the results
	var outputWriter io.Writer
	if outputFile != "" {
		file, err := os.Create(outputFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error creating output file: %v\n", err)
			os.Exit(1)
		}
		defer file.Close()
		outputWriter = file
	} else {
		outputWriter = os.Stdout
	}

	// Output each message on a separate line (except single message: no extra newline)
	// The Go CLI always writes decoded messages as UTF-8 text, never as raw bytes or with a BOM.
	for i, msg := range messages {
		if i > 0 {
			fmt.Fprintln(outputWriter)
		}
		fmt.Fprint(outputWriter, msg)
	}
}

func printUsage() {
	fmt.Fprintf(os.Stderr, `whitespace-stego-go - Zero-width character steganography tool

Usage:
  whitespace-stego-go <command> [options]

Commands:
  encode    Encode a message into carrier text
  decode    Decode messages from carrier text
  help      Show this help message

Encode options:
  -m, -message <text>       Message to encode (required)
  -cf, -carrier-file <path> Carrier file path
  -o, -output <path>        Output file path (default: stdout)
  -p, -password <text>      Password for encryption

Decode options:
  -cf, -carrier-file <path> Carrier file path (required)
  -o, -output <path>        Output file path (default: stdout)
  -p, -password <text>      Password for decryption

Examples:
  whitespace-stego-go encode -m "Hello, World!" -cf carrier.txt -o encoded.txt
  whitespace-stego-go encode -m "Secret" -cf carrier.txt -p "mypassword" -o encoded.txt
  whitespace-stego-go decode -cf encoded.txt
  whitespace-stego-go decode -cf encoded.txt -p "mypassword" -o decoded.txt
`)
}
