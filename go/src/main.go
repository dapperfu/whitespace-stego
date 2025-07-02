package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Define command-line flags
	var (
		message      = flag.String("m", "", "Message to encode/decode")
		messageFile  = flag.String("mf", "", "File containing message to encode/decode")
		carrier      = flag.String("c", "", "Carrier text")
		carrierFile  = flag.String("cf", "", "File containing carrier text")
		password     = flag.String("p", "", "Password for encryption/decryption")
		passwordFile = flag.String("pf", "", "File containing password")
		output       = flag.String("o", "", "Output file (use '-' for stdout)")
		operation    = flag.String("op", "", "Operation: encode or decode")
	)

	// Parse flags first
	flag.Parse()

	// Determine operation from remaining arguments
	args := flag.Args()
	if len(args) > 0 && *operation == "" {
		*operation = args[0]
	}

	if *operation == "" {
		fmt.Fprintf(os.Stderr, "Usage: %s [encode|decode] [options]\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "Options:\n")
		flag.PrintDefaults()
		os.Exit(1)
	}

	// Read message
	var messageText string
	if *message != "" {
		messageText = *message
	} else if *messageFile != "" {
		content, err := os.ReadFile(*messageFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading message file: %v\n", err)
			os.Exit(1)
		}
		messageText = strings.TrimSpace(string(content))
	}

	// Read carrier
	var carrierText string
	if *carrier != "" {
		carrierText = *carrier
	} else if *carrierFile != "" {
		content, err := os.ReadFile(*carrierFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading carrier file: %v\n", err)
			os.Exit(1)
		}
		carrierText = string(content)
	}

	// Read password
	var passwordText string
	if *password != "" {
		passwordText = *password
	} else if *passwordFile != "" {
		content, err := os.ReadFile(*passwordFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error reading password file: %v\n", err)
			os.Exit(1)
		}
		passwordText = strings.TrimSpace(string(content))
	}

	// Determine output
	var outputWriter *os.File
	if *output == "" || *output == "-" {
		outputWriter = os.Stdout
	} else {
		var err error
		outputWriter, err = os.Create(*output)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error creating output file: %v\n", err)
			os.Exit(1)
		}
		defer outputWriter.Close()
	}

	// Perform operation
	switch *operation {
	case "encode":
		if messageText == "" {
			fmt.Fprintf(os.Stderr, "Error: message is required for encoding\n")
			os.Exit(1)
		}

		result, err := Encode(messageText, carrierText, passwordText)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error encoding message: %v\n", err)
			os.Exit(1)
		}

		fmt.Fprint(outputWriter, result)

	case "decode":
		if carrierText == "" {
			fmt.Fprintf(os.Stderr, "Error: carrier is required for decoding\n")
			os.Exit(1)
		}

		messages, err := Decode(carrierText, passwordText)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error decoding messages: %v\n", err)
			os.Exit(1)
		}

		if len(messages) == 0 {
			fmt.Fprintf(os.Stderr, "No messages found in carrier\n")
			os.Exit(1)
		}

		// Output each message on a separate line
		for i, msg := range messages {
			if i > 0 {
				fmt.Fprintln(outputWriter)
			}
			fmt.Fprint(outputWriter, msg)
		}

	default:
		fmt.Fprintf(os.Stderr, "Error: unknown operation '%s'. Use 'encode' or 'decode'\n", *operation)
		os.Exit(1)
	}
}
