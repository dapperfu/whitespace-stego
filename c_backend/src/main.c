/**
 * @file main.c
 * @brief Main program for whitespace steganography
 */

#include "decode.h"
#include "encode.h"
#include "utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFFER_SIZE (1024 * 1024)  // 1MB buffer

void print_usage(const char* program_name) {
    fprintf(stderr, "Usage: %s <command> [options]\n", program_name);
    fprintf(stderr, "\nCommands:\n");
    fprintf(stderr, "  encode    Encode a message into carrier text\n");
    fprintf(stderr, "  decode    Decode a message from carrier text\n");
    fprintf(stderr, "\nOptions:\n");
    fprintf(stderr, "  -m <msg>      Message to encode\n");
    fprintf(stderr, "  -c <text>     Carrier text\n");
    fprintf(stderr, "  --carrier-file <file>  Read carrier from file\n");
    fprintf(stderr, "  -o <file>     Output file\n");
    fprintf(stderr, "  -i <file>     Input file to decode\n");
    fprintf(stderr, "  -p <pass>     Optional password\n");
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }

    const char* command = argv[1];
    const char* message = NULL;
    const char* carrier = NULL;
    const char* carrier_file = NULL;
    const char* output_file = NULL;
    const char* input_file = NULL;
    const char* password = NULL;

    // Parse command line arguments
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 && i + 1 < argc) {
            message = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            carrier = argv[++i];
        } else if (strcmp(argv[i], "--carrier-file") == 0 && i + 1 < argc) {
            carrier_file = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) {
            output_file = argv[++i];
        } else if (strcmp(argv[i], "-i") == 0 && i + 1 < argc) {
            input_file = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0 && i + 1 < argc) {
            password = argv[++i];
        }
    }

    // Allocate buffers
    char* buffer = (char*)malloc(MAX_BUFFER_SIZE);
    if (!buffer) {
        fprintf(stderr, "Error: Failed to allocate memory\n");
        return 1;
    }

    int result = 0;

    if (strcmp(command, "encode") == 0) {
        // Validate encode arguments
        if (!message) {
            fprintf(stderr, "Error: Message (-m) is required for encoding\n");
            result = 1;
            goto cleanup;
        }

        if (!carrier && !carrier_file) {
            fprintf(
                stderr,
                "Error: Either carrier text (-c) or carrier file (--carrier-file) is required\n");
            result = 1;
            goto cleanup;
        }

        // Read carrier from file if specified
        if (carrier_file) {
            uint8_t* file_data;
            size_t file_size;
            if (!read_file(carrier_file, &file_data, &file_size)) {
                fprintf(stderr, "Error: Failed to read carrier file\n");
                result = 1;
                goto cleanup;
            }
            carrier = (char*)file_data;
        }

        // Encode message
        size_t message_len = strlen(message);
        size_t carrier_len = strlen(carrier);
        size_t output_len = calculate_encoded_size(message_len, carrier_len);

        if (output_len > MAX_BUFFER_SIZE) {
            fprintf(stderr, "Error: Output would exceed maximum buffer size\n");
            result = 1;
            goto cleanup;
        }

        size_t encoded_len = encode_message(message,
                                            message_len,
                                            carrier,
                                            carrier_len,
                                            buffer,
                                            MAX_BUFFER_SIZE,
                                            password,
                                            password ? strlen(password) : 0);

        if (encoded_len == 0) {
            fprintf(stderr, "Error: Failed to encode message\n");
            result = 1;
            goto cleanup;
        }

        // Write output
        if (output_file) {
            if (!write_file(output_file, (uint8_t*)buffer, encoded_len)) {
                fprintf(stderr, "Error: Failed to write output file\n");
                result = 1;
                goto cleanup;
            }
        } else {
            fwrite(buffer, 1, encoded_len, stdout);
        }

    } else if (strcmp(command, "decode") == 0) {
        // Validate decode arguments
        if (!input_file) {
            fprintf(stderr, "Error: Input file (-i) is required for decoding\n");
            result = 1;
            goto cleanup;
        }

        // Read input file
        uint8_t* input_data;
        size_t input_size;
        if (!read_file(input_file, &input_data, &input_size)) {
            fprintf(stderr, "Error: Failed to read input file\n");
            result = 1;
            goto cleanup;
        }

        // Decode message
        size_t decoded_len = decode_message((char*)input_data,
                                            input_size,
                                            buffer,
                                            MAX_BUFFER_SIZE,
                                            password,
                                            password ? strlen(password) : 0);

        free(input_data);

        if (decoded_len == 0) {
            fprintf(stderr, "Error: Failed to decode message\n");
            result = 1;
            goto cleanup;
        }

        // Write output
        if (output_file) {
            if (!write_file(output_file, (uint8_t*)buffer, decoded_len)) {
                fprintf(stderr, "Error: Failed to write output file\n");
                result = 1;
                goto cleanup;
            }
        } else {
            fwrite(buffer, 1, decoded_len, stdout);
        }

    } else {
        fprintf(stderr, "Error: Unknown command '%s'\n", command);
        print_usage(argv[0]);
        result = 1;
    }

cleanup:
    free(buffer);
    return result;
}
