package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		printUsageAndExit()
	}

	subcommand := os.Args[1]

	switch subcommand {
	case "encode":
		encodeCmd := flag.NewFlagSet("encode", flag.ExitOnError)
		message := encodeCmd.String("m", "", "Message to encode")
		messageFile := encodeCmd.String("mf", "", "File containing message to encode")
		carrier := encodeCmd.String("c", "", "Carrier text")
		carrierFile := encodeCmd.String("cf", "", "File containing carrier text")
		password := encodeCmd.String("p", "", "Password for encryption")
		passwordFile := encodeCmd.String("pf", "", "File containing password")
		output := encodeCmd.String("o", "", "Output file (use '-' for stdout)")

		encodeCmd.Parse(os.Args[2:])

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
		decodeCmd := flag.NewFlagSet("decode", flag.ExitOnError)
		carrier := decodeCmd.String("c", "", "Carrier text")
		carrierFile := decodeCmd.String("cf", "", "File containing carrier text")
		password := decodeCmd.String("p", "", "Password for decryption")
		passwordFile := decodeCmd.String("pf", "", "File containing password")
		output := decodeCmd.String("o", "", "Output file (use '-' for stdout)")

		decodeCmd.Parse(os.Args[2:])

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

		// Output each message on a separate line (except single message: no extra newline)
		for i, msg := range messages {
			if i > 0 {
				fmt.Fprintln(outputWriter)
			}
			fmt.Fprint(outputWriter, msg)
		}

	default:
		printUsageAndExit()
	}
}

func printUsageAndExit() {
	fmt.Fprintf(os.Stderr, "Usage: %s <encode|decode> [options]\n", os.Args[0])
	fmt.Fprintf(os.Stderr, "\nOptions for encode:\n")
	fmt.Fprintf(os.Stderr, "  -m   Message to encode\n")
	fmt.Fprintf(os.Stderr, "  -mf  File containing message to encode\n")
	fmt.Fprintf(os.Stderr, "  -c   Carrier text\n")
	fmt.Fprintf(os.Stderr, "  -cf  File containing carrier text\n")
	fmt.Fprintf(os.Stderr, "  -p   Password for encryption\n")
	fmt.Fprintf(os.Stderr, "  -pf  File containing password\n")
	fmt.Fprintf(os.Stderr, "  -o   Output file (use '-' for stdout)\n")
	fmt.Fprintf(os.Stderr, "\nOptions for decode:\n")
	fmt.Fprintf(os.Stderr, "  -c   Carrier text\n")
	fmt.Fprintf(os.Stderr, "  -cf  File containing carrier text\n")
	fmt.Fprintf(os.Stderr, "  -p   Password for decryption\n")
	fmt.Fprintf(os.Stderr, "  -pf  File containing password\n")
	fmt.Fprintf(os.Stderr, "  -o   Output file (use '-' for stdout)\n")
	os.Exit(1)
}
