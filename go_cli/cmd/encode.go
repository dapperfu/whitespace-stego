package cmd

import (
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
	"github.com/whitespace-stego/go_cli/internal"
)

var (
	password string
	carrier  string
)

var encodeCmd = &cobra.Command{
	Use:   "encode",
	Short: "Encode a message using zero-width characters",
	Long: `Encode a message using zero-width characters. The message can be provided via stdin
or a file. The encoded output can be written to stdout or a file.`,
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

		// Create encoder
		encoder := internal.NewEncoder(password)

		// Encode message
		encoded, err := encoder.EncodeWithLength(string(input), carrier)
		if err != nil {
			return fmt.Errorf("failed to encode message: %w", err)
		}

		// Write output
		_, err = fmt.Print(encoded)
		if err != nil {
			return fmt.Errorf("failed to write output: %w", err)
		}

		return nil
	},
}

func init() {
	rootCmd.AddCommand(encodeCmd)

	encodeCmd.Flags().StringVarP(&password, "password", "p", "", "Password for encryption (optional)")
	encodeCmd.Flags().StringVarP(&carrier, "carrier", "c", "", "Carrier text to embed the message in (optional)")
}
