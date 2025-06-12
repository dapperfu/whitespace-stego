package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
	"github.com/whitespace-stego/go_cli/internal"
)

var decodeCmd = &cobra.Command{
	Use:   "decode",
	Short: "Decode a message from zero-width characters",
	Long: `Decode a message from zero-width characters. The encoded message can be provided via stdin
or a file. The decoded output can be written to stdout or a file.`,
	RunE: func(cmd *cobra.Command, args []string) error {
		// Read input
		var input []byte
		var err error
		if len(args) > 0 {
			input = []byte(args[0])
		} else {
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
		_, err = fmt.Print(decoded)
		if err != nil {
			return fmt.Errorf("failed to write output: %w", err)
		}

		return nil
	},
}

func init() {
	rootCmd.AddCommand(decodeCmd)

	decodeCmd.Flags().StringVarP(&password, "password", "p", "", "Password for decryption (optional)")
}
