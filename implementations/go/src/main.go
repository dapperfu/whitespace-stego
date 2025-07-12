package main

import (
	"flag"
	"fmt"
	"io"
	"os"

	"whitespace-stego-go/src/stego"
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
	var messageFile string
	var carrier string
	var carrierFile string
	var outputFile string
	var password string

	fs.StringVar(&message, "m", "", "Message to encode")
	fs.StringVar(&message, "message", "", "Message to encode")
	fs.StringVar(&messageFile, "mf", "", "Message file path")
	fs.StringVar(&messageFile, "message-file", "", "Message file path")
	fs.StringVar(&carrier, "c", "", "Carrier text")
	fs.StringVar(&carrier, "carrier", "", "Carrier text")
	fs.StringVar(&carrierFile, "cf", "", "Carrier file path")
	fs.StringVar(&carrierFile, "carrier-file", "", "Carrier file path")
	fs.StringVar(&outputFile, "o", "", "Output file path")
	fs.StringVar(&outputFile, "output", "", "Output file path")
	fs.StringVar(&password, "p", "", "Password for encryption")
	fs.StringVar(&password, "password", "", "Password for encryption")

	fs.Parse(os.Args[2:])

	// Check for mutual exclusivity between message and message-file
	if message != "" && messageFile != "" {
		fmt.Fprintf(os.Stderr, "Error: -m/-message and -mf/-message-file are mutually exclusive\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Check for mutual exclusivity between carrier and carrier-file
	if carrier != "" && carrierFile != "" {
		fmt.Fprintf(os.Stderr, "Error: -c/-carrier and -cf/-carrier-file are mutually exclusive\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Validate required arguments
	if message == "" && messageFile == "" {
		fmt.Fprintf(os.Stderr, "Error: either -m/-message or -mf/-message-file is required\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Validate that carrier is provided for encoding
	if carrier == "" && carrierFile == "" {
		fmt.Fprintf(os.Stderr, "Error: either -c/-carrier or -cf/-carrier-file is required for encoding\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Read message from file if message-file is provided
	if messageFile != "" {
		messageBytes, err := os.ReadFile(messageFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading message file: %v\n", err)
			os.Exit(1)
		}
		message = string(messageBytes)
	}

	// Read carrier text
	if carrierFile != "" {
		carrierBytes, err := os.ReadFile(carrierFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading carrier file: %v\n", err)
			os.Exit(1)
		}
		carrier = string(carrierBytes)
	}

	// Encode the message
	encoded, err := stego.Encode(message, carrier, password)
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

	var carrier string
	var carrierFile string
	var outputFile string
	var password string

	fs.StringVar(&carrier, "c", "", "Carrier text")
	fs.StringVar(&carrier, "carrier", "", "Carrier text")
	fs.StringVar(&carrierFile, "cf", "", "Carrier file path")
	fs.StringVar(&carrierFile, "carrier-file", "", "Carrier file path")
	fs.StringVar(&outputFile, "o", "", "Output file path")
	fs.StringVar(&outputFile, "output", "", "Output file path")
	fs.StringVar(&password, "p", "", "Password for decryption")
	fs.StringVar(&password, "password", "", "Password for decryption")

	fs.Parse(os.Args[2:])

	// Check for mutual exclusivity between carrier and carrier-file
	if carrier != "" && carrierFile != "" {
		fmt.Fprintf(os.Stderr, "Error: -c/-carrier and -cf/-carrier-file are mutually exclusive\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Validate required arguments
	if carrier == "" && carrierFile == "" {
		fmt.Fprintf(os.Stderr, "Error: either -c/-carrier or -cf/-carrier-file is required\n")
		fs.PrintDefaults()
		os.Exit(1)
	}

	// Read carrier text
	if carrierFile != "" {
		carrierBytes, err := os.ReadFile(carrierFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading carrier file: %v\n", err)
			os.Exit(1)
		}
		carrier = string(carrierBytes)
	}

	// Decode the message
	messages, err := stego.Decode(carrier, password)
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
  -m, -message <text>       Message to encode (mutually exclusive with -mf/-message-file)
  -mf, -message-file <path> Message file path (mutually exclusive with -m/-message)
  -c, -carrier <text>       Carrier text (mutually exclusive with -cf/-carrier-file)
  -cf, -carrier-file <path> Carrier file path (mutually exclusive with -c/-carrier)
  -o, -output <path>        Output file path (default: stdout)
  -p, -password <text>      Password for encryption

Decode options:
  -c, -carrier <text>       Carrier text (mutually exclusive with -cf/-carrier-file)
  -cf, -carrier-file <path> Carrier file path (mutually exclusive with -c/-carrier)
  -o, -output <path>        Output file path (default: stdout)
  -p, -password <text>      Password for decryption

Examples:
  whitespace-stego-go encode -m "Hello, World!" -c "This is carrier text" -o encoded.txt
  whitespace-stego-go encode -m "Hello, World!" -cf carrier.txt -o encoded.txt
  whitespace-stego-go encode -mf message.txt -cf carrier.txt -o encoded.txt
  whitespace-stego-go encode -m "Secret" -c "Carrier text" -p "mypassword" -o encoded.txt
  whitespace-stego-go decode -c "encoded text with hidden message"
  whitespace-stego-go decode -cf encoded.txt
  whitespace-stego-go decode -cf encoded.txt -p "mypassword" -o decoded.txt
`)
}
