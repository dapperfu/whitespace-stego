/*
 * Static Whitespace Steganography CLI Implementation
 * 
 * This program provides a command-line interface for the static C implementation.
 * It uses pre-allocated 4MiB buffers with no dynamic memory allocation.
 */

#include "../include/whitespace_stego_static.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_INPUT_SIZE 4194304  // 4 MiB

static void print_usage(const char* program_name) {
    printf("Usage: %s [OPTIONS] COMMAND [ARGS]...\n\n", program_name);
    printf("Whitespace steganography tool for encoding and decoding messages.\n");
    printf("Static implementation with 4MiB pre-allocated buffers.\n\n");
    printf("Options:\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Commands:\n");
    printf("  encode                         Encode a message into a carrier file\n");
    printf("  decode                         Decode a message from a carrier file\n");
    printf("  help                           Show this message or the help of the given subcommand\n\n");
    printf("Examples:\n");
    printf("  %s encode carrier.txt message.txt output.txt\n", program_name);
    printf("  %s encode -p secret carrier.txt message.txt output.txt\n", program_name);
    printf("  %s decode carrier.txt output.txt\n", program_name);
    printf("  %s decode -p secret carrier.txt output.txt\n", program_name);
}

static void print_encode_help(const char* program_name) {
    printf("Usage: %s encode [OPTIONS] <carrier_file> <message_file> <output_file>\n\n", program_name);
    printf("Encode a message into a carrier file using whitespace steganography.\n\n");
    printf("Options:\n");
    printf("  -p, --password <password>      Password for encryption\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Arguments:\n");
    printf("  carrier_file                   Input carrier text file\n");
    printf("  message_file                   Input message file to encode\n");
    printf("  output_file                    Output file for encoded text\n");
}

static void print_decode_help(const char* program_name) {
    printf("Usage: %s decode [OPTIONS] <carrier_file> <output_file>\n\n", program_name);
    printf("Decode a message from a carrier file using whitespace steganography.\n\n");
    printf("Options:\n");
    printf("  -p, --password <password>      Password for decryption\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Arguments:\n");
    printf("  carrier_file                   Input carrier text file\n");
    printf("  output_file                    Output file for decoded message\n");
}

static int read_file(const char* filename, char* buffer, size_t buffer_size) {
    FILE* file = fopen(filename, "rb");
    if (!file) {
        fprintf(stderr, "Error: Cannot open file '%s'\n", filename);
        return -1;
    }
    
    size_t bytes_read = fread(buffer, 1, buffer_size - 1, file);
    buffer[bytes_read] = '\0';
    fclose(file);
    
    return bytes_read;
}

static int write_file(const char* filename, const char* data, size_t data_len) {
    FILE* file = fopen(filename, "wb");
    if (!file) {
        fprintf(stderr, "Error: Cannot create file '%s'\n", filename);
        return -1;
    }
    
    size_t bytes_written = fwrite(data, 1, data_len, file);
    fclose(file);
    
    if (bytes_written != data_len) {
        fprintf(stderr, "Error: Failed to write complete data to '%s'\n", filename);
        return -1;
    }
    
    return 0;
}

static int encode_command(int argc, char* argv[]) {
    const char* program_name = argv[0];
    const char* password = NULL;
    int verbose = 0;
    
    // Parse options
    int opt;
    while ((opt = getopt(argc, argv, "p:vh")) != -1) {
        switch (opt) {
            case 'p':
                password = optarg;
                break;
            case 'v':
                verbose = 1;
                break;
            case 'h':
                print_encode_help(program_name);
                return 0;
            default:
                print_encode_help(program_name);
                return 1;
        }
    }
    
    // Check arguments
    if (argc - optind != 3) {
        fprintf(stderr, "Error: encode command requires exactly 3 arguments\n\n");
        print_encode_help(program_name);
        return 1;
    }
    
    const char* carrier_file = argv[optind];
    const char* message_file = argv[optind + 1];
    const char* output_file = argv[optind + 2];
    
    if (verbose) {
        printf("Encoding message from '%s' into carrier '%s'\n", message_file, carrier_file);
        if (password) {
            printf("Using password protection\n");
        }
    }
    
    // Initialize static buffers
    static whitespace_stego_buffers_t buffers;
    if (!whitespace_stego_static_init(&buffers)) {
        fprintf(stderr, "Error: Failed to initialize buffers: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    // Read carrier file
    int carrier_len = read_file(carrier_file, buffers.carrier, sizeof(buffers.carrier));
    if (carrier_len < 0) {
        return 1;
    }
    
    // Read message file
    int message_len = read_file(message_file, buffers.message, sizeof(buffers.message));
    if (message_len < 0) {
        return 1;
    }
    
    if (verbose) {
        printf("Carrier size: %d bytes\n", carrier_len);
        printf("Message size: %d bytes\n", message_len);
    }
    
    // Encode the message
    size_t encoded_len = 0;
    if (!whitespace_stego_static_encode(&buffers, buffers.carrier, carrier_len,
                                       buffers.message, password, &encoded_len)) {
        fprintf(stderr, "Error: Encoding failed: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    if (verbose) {
        printf("Encoded successfully! Output size: %zu bytes\n", encoded_len);
    }
    
    // Write output file
    if (write_file(output_file, buffers.encoded, encoded_len) != 0) {
        return 1;
    }
    
    if (verbose) {
        printf("Encoded text written to '%s'\n", output_file);
    }
    
    return 0;
}

static int decode_command(int argc, char* argv[]) {
    const char* program_name = argv[0];
    const char* password = NULL;
    int verbose = 0;
    
    // Parse options
    int opt;
    while ((opt = getopt(argc, argv, "p:vh")) != -1) {
        switch (opt) {
            case 'p':
                password = optarg;
                break;
            case 'v':
                verbose = 1;
                break;
            case 'h':
                print_decode_help(program_name);
                return 0;
            default:
                print_decode_help(program_name);
                return 1;
        }
    }
    
    // Check arguments
    if (argc - optind != 2) {
        fprintf(stderr, "Error: decode command requires exactly 2 arguments\n\n");
        print_decode_help(program_name);
        return 1;
    }
    
    const char* carrier_file = argv[optind];
    const char* output_file = argv[optind + 1];
    
    if (verbose) {
        printf("Decoding message from carrier '%s'\n", carrier_file);
        if (password) {
            printf("Using password protection\n");
        }
    }
    
    // Initialize static buffers
    static whitespace_stego_buffers_t buffers;
    if (!whitespace_stego_static_init(&buffers)) {
        fprintf(stderr, "Error: Failed to initialize buffers: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    // Read carrier file
    int carrier_len = read_file(carrier_file, buffers.carrier, sizeof(buffers.carrier));
    if (carrier_len < 0) {
        return 1;
    }
    
    if (verbose) {
        printf("Carrier size: %d bytes\n", carrier_len);
    }
    
    // Decode the message
    size_t decoded_len = 0;
    if (!whitespace_stego_static_decode(&buffers, buffers.carrier, carrier_len,
                                       password, &decoded_len)) {
        fprintf(stderr, "Error: Decoding failed: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    if (verbose) {
        printf("Decoded successfully! Message size: %zu bytes\n", decoded_len);
    }
    
    // Write output file
    if (write_file(output_file, buffers.decoded, decoded_len) != 0) {
        return 1;
    }
    
    if (verbose) {
        printf("Decoded message written to '%s'\n", output_file);
    }
    
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }
    
    const char* command = argv[1];
    
    if (strcmp(command, "help") == 0) {
        if (argc > 2) {
            const char* subcommand = argv[2];
            if (strcmp(subcommand, "encode") == 0) {
                print_encode_help(argv[0]);
            } else if (strcmp(subcommand, "decode") == 0) {
                print_decode_help(argv[0]);
            } else {
                fprintf(stderr, "Unknown subcommand: %s\n", subcommand);
                print_usage(argv[0]);
                return 1;
            }
        } else {
            print_usage(argv[0]);
        }
        return 0;
    } else if (strcmp(command, "encode") == 0) {
        return encode_command(argc - 1, argv + 1);
    } else if (strcmp(command, "decode") == 0) {
        return decode_command(argc - 1, argv + 1);
    } else {
        fprintf(stderr, "Unknown command: %s\n", command);
        print_usage(argv[0]);
        return 1;
    }
} 