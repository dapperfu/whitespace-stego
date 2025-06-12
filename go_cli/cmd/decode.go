package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
	"github.com/whitespace-stego/go_cli/internal"
)

var decodeCmd = &cobra.Command{
	Use:   "decode [encoded_message]",
	Short: "Decode a message from zero-width characters",
	Long: `Decode a message from zero-width characters. The encoded message can be provided in three ways:
1. As a command-line argument
2. Via stdin (pipe or redirect)
3. From a file specified with --input

The decoded output can be written to:
1. stdout (default)
2. A file specified with --output`,
	RunE: func(cmd *cobra.Command, args []string) error {
		// Get input from the appropriate source
		var input []byte
		var err error

		// Check if we have a message from command line
		if len(args) > 0 {
			input = []byte(args[0])
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

		// Create decoder
		decoder := internal.NewDecoder(password)

		// Decode message
		decoded, err := decoder.DecodeWithLength(string(input))
		if err != nil {
			return fmt.Errorf("failed to decode message: %w", err)
		}

		// Write output
		if outputFile != "" {
			err = os.WriteFile(outputFile, []byte(decoded), 0644)
			if err != nil {
				return fmt.Errorf("failed to write output file: %w", err)
			}
		} else {
			_, err = fmt.Print(decoded)
			if err != nil {
				return fmt.Errorf("failed to write output: %w", err)
			}
		}

		return nil
	},
}

func init() {
	rootCmd.AddCommand(decodeCmd)

	decodeCmd.Flags().StringVarP(&password, "password", "p", "", "Password for decryption (optional)")
	decodeCmd.Flags().StringVarP(&inputFile, "input", "i", "", "Input file (optional)")
	decodeCmd.Flags().StringVarP(&outputFile, "output", "o", "", "Output file (optional)")
}
