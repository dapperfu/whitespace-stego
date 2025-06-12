package cmd

import (
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "whitespace-stego-go",
	Short: "A CLI tool for encoding and decoding messages using zero-width characters",
	Long: `whitespace-stego-go is a command-line tool that allows you to encode and decode messages
using zero-width characters. It supports password-based encryption and can work with
both file input/output and stdin/stdout.`,
}

// Execute adds all child commands to the root command and sets flags appropriately.
func Execute() error {
	return rootCmd.Execute()
}

func init() {
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.
}
