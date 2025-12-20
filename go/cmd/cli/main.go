package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/whitespace-stego/go"
)

func main() {
	encodeCmd := flag.NewFlagSet("encode", flag.ExitOnError)
	encodeCarrier := encodeCmd.String("c", "", "Carrier text")

	decodeCmd := flag.NewFlagSet("decode", flag.ExitOnError)

	if len(os.Args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <encode|decode> [options]\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "\nCommands:\n")
		fmt.Fprintf(os.Stderr, "  encode <message> [-c <carrier>]  Encode a message\n")
		fmt.Fprintf(os.Stderr, "  decode <encoded>                   Decode a message\n")
		os.Exit(1)
	}

	switch os.Args[1] {
	case "encode":
		encodeCmd.Parse(os.Args[2:])
		if encodeCmd.NArg() < 1 {
			fmt.Fprintf(os.Stderr, "Error: message required for encode\n")
			os.Exit(1)
		}
		message := encodeCmd.Arg(0)

		var carrier *string
		if *encodeCarrier != "" {
			carrier = encodeCarrier
		}

		encoded, err := whitespacestego.Encode(message, carrier)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}
		fmt.Println(encoded)

	case "decode":
		decodeCmd.Parse(os.Args[2:])
		if decodeCmd.NArg() < 1 {
			fmt.Fprintf(os.Stderr, "Error: encoded text required for decode\n")
			os.Exit(1)
		}
		encodedText := decodeCmd.Arg(0)

		decoded, err := whitespacestego.Decode(encodedText)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}
		fmt.Println(decoded)

	default:
		fmt.Fprintf(os.Stderr, "Unknown command: %s\n", os.Args[1])
		os.Exit(1)
	}
}

