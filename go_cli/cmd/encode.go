package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
	"github.com/whitespace-stego/go_cli/internal"
)

var (
	password   string
	carrier    string
	inputFile  string
	outputFile string
	message    string
)

var encodeCmd = &cobra.Command{
	Use:   "encode [message]",
	Short: "Encode a message using zero-width characters",
	Long: `Encode a message using zero-width characters. The message can be provided in three ways:
1. As a command-line argument
2. Via stdin (pipe or redirect)
3. From a file specified with --input

The encoded output can be written to:
1. stdout (default)
2. A file specified with --output`,
	RunE: func(cmd *cobra.Command, args []string) error {
		// Get input from the appropriate source
		var input []byte
		var err error

		// Check if we have a message from command line
		if len(args) > 0 {
			input = []byte(args[0])
		} else if message != "" {
			// Check if we have a message from --message flag
			input = []byte(message)
		} else if inputFile != "" {
			// Read from input file
			input, err = os.ReadFile(inputFile)
			if err != nil {
				return fmt.Errorf("failed to read input file: %w", err)
			}
		} else {
			// Read from stdin
			input, err = io.ReadAll(os.Stdin)
			if err != nil {
				return fmt.Errorf("failed to read input: %w", err)
			}
		}

		// Create encoder
		encoder := internal.NewEncoder(password)

		// Encode message
		encoded, err := encoder.EncodeWithLength(string(input), carrier)
		if err != nil {
			return fmt.Errorf("failed to encode message: %w", err)
		}

		// Write output
		if outputFile != "" {
			err = os.WriteFile(outputFile, []byte(encoded), 0644)
			if err != nil {
				return fmt.Errorf("failed to write output file: %w", err)
			}
		} else {
			_, err = fmt.Print(encoded)
			if err != nil {
				return fmt.Errorf("failed to write output: %w", err)
			}
		}

		return nil
	},
}

func init() {
	rootCmd.AddCommand(encodeCmd)

	encodeCmd.Flags().StringVarP(&password, "password", "p", "", "Password for encryption (optional)")
	encodeCmd.Flags().StringVarP(&carrier, "carrier", "c", "", "Carrier text to embed the message in (optional)")
	encodeCmd.Flags().StringVarP(&inputFile, "input", "i", "", "Input file (optional)")
	encodeCmd.Flags().StringVarP(&outputFile, "output", "o", "", "Output file (optional)")
	encodeCmd.Flags().StringVarP(&message, "message", "m", "", "Message to encode (optional)")
}
