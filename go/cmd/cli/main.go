package main

import (
	"flag"
	"fmt"
	"io"
	"os"

	"github.com/whitespace-stego/go"
)

func readInput(inputPath string) (string, error) {
	if inputPath == "-" {
		data, err := io.ReadAll(os.Stdin)
		if err != nil {
			return "", fmt.Errorf("failed to read from stdin: %w", err)
		}
		return string(data), nil
	}
	data, err := os.ReadFile(inputPath)
	if err != nil {
		return "", fmt.Errorf("failed to read file %s: %w", inputPath, err)
	}
	return string(data), nil
}

func writeOutput(outputPath string, content string) error {
	if outputPath == "-" {
		_, err := fmt.Print(content)
		return err
	}
	return os.WriteFile(outputPath, []byte(content), 0644)
}

func main() {
	encodeCmd := flag.NewFlagSet("encode", flag.ExitOnError)
	encodeInput := encodeCmd.String("i", "", "Input file (use '-' for stdin)")
	encodeOutput := encodeCmd.String("o", "", "Output file (use '-' for stdout)")
	encodeCarrier := encodeCmd.String("c", "", "Carrier text")
	encodePassword := encodeCmd.String("p", "", "Password for encryption")

	decodeCmd := flag.NewFlagSet("decode", flag.ExitOnError)
	decodeInput := decodeCmd.String("i", "", "Input file (use '-' for stdin)")
	decodeOutput := decodeCmd.String("o", "", "Output file (use '-' for stdout)")
	decodePassword := decodeCmd.String("p", "", "Password for decryption")

	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <encode|decode> [options]\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "\nCommands:\n")
		fmt.Fprintf(os.Stderr, "  encode [message] [-i <input>] [-o <output>] [-c <carrier>] [-p <password>]\n")
		fmt.Fprintf(os.Stderr, "  decode [encoded] [-i <input>] [-o <output>] [-p <password>]\n")
		fmt.Fprintf(os.Stderr, "\nOptions:\n")
		fmt.Fprintf(os.Stderr, "  -i, --input <file>   Input file (use '-' for stdin)\n")
		fmt.Fprintf(os.Stderr, "  -o, --output <file>  Output file (use '-' for stdout)\n")
		fmt.Fprintf(os.Stderr, "  -c, --carrier <text> Carrier text (encode only)\n")
		fmt.Fprintf(os.Stderr, "  -p, --password <pwd> Password for encryption/decryption\n")
		os.Exit(1)
	}

	switch os.Args[1] {
	case "encode":
		encodeCmd.Parse(os.Args[2:])
		
		var message string
		var err error
		if *encodeInput != "" {
			message, err = readInput(*encodeInput)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Error: %v\n", err)
				os.Exit(1)
			}
		} else if encodeCmd.NArg() > 0 {
			if encodeCmd.Arg(0) == "-" {
				message, err = readInput("-")
				if err != nil {
					fmt.Fprintf(os.Stderr, "Error: %v\n", err)
					os.Exit(1)
				}
			} else {
				message = encodeCmd.Arg(0)
			}
		} else {
			fmt.Fprintf(os.Stderr, "Error: message required (provide as argument, -i/--input, or '-' for stdin)\n")
			os.Exit(1)
		}

		var carrier *string
		if *encodeCarrier != "" {
			carrier = encodeCarrier
		}

		var password *string
		if *encodePassword != "" {
			password = encodePassword
		}

		encoded, err := whitespacestego.Encode(message, carrier, password)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}

		outputContent := encoded
		if *encodeOutput != "" {
			outputContent += "\n"
		}

		if *encodeOutput != "" {
			if err := writeOutput(*encodeOutput, outputContent); err != nil {
				fmt.Fprintf(os.Stderr, "Error: %v\n", err)
				os.Exit(1)
			}
		} else {
			fmt.Println(encoded)
		}

	case "decode":
		decodeCmd.Parse(os.Args[2:])
		
		var encodedText string
		var err error
		if *decodeInput != "" {
			encodedText, err = readInput(*decodeInput)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Error: %v\n", err)
				os.Exit(1)
			}
		} else if decodeCmd.NArg() > 0 {
			if decodeCmd.Arg(0) == "-" {
				encodedText, err = readInput("-")
				if err != nil {
					fmt.Fprintf(os.Stderr, "Error: %v\n", err)
					os.Exit(1)
				}
			} else {
				encodedText = decodeCmd.Arg(0)
			}
		} else {
			fmt.Fprintf(os.Stderr, "Error: encoded text required (provide as argument, -i/--input, or '-' for stdin)\n")
			os.Exit(1)
		}

		var password *string
		if *decodePassword != "" {
			password = decodePassword
		}

		decoded, err := whitespacestego.Decode(encodedText, password)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}

		outputContent := decoded
		if *decodeOutput != "" {
			outputContent += "\n"
		}

		if *decodeOutput != "" {
			if err := writeOutput(*decodeOutput, outputContent); err != nil {
				fmt.Fprintf(os.Stderr, "Error: %v\n", err)
				os.Exit(1)
			}
		} else {
			fmt.Println(decoded)
		}

	default:
		fmt.Fprintf(os.Stderr, "Unknown command: %s\n", os.Args[1])
		os.Exit(1)
	}
}

