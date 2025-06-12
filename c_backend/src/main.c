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
    fprintf(stderr, "  --message-file <file>  Read message from file ('-' for stdin)\n");
    fprintf(stderr, "  -c <text>     Carrier text\n");
    fprintf(stderr, "  --carrier-file <file>  Read carrier from file ('-' for stdin)\n");
    fprintf(stderr, "  -o <file>     Output file ('-' for stdout)\n");
    fprintf(stderr, "  --output-file <file>   Output file (long option, '-' for stdout)\n");
    fprintf(stderr, "  -i <file>     Input file to decode ('-' for stdin)\n");
    fprintf(stderr, "  --input-file <file>    Input file (long option, '-' for stdin)\n");
    fprintf(stderr, "  -p <pass>     Optional password\n");
}

bool read_text(const char* filename, char** text, size_t* size) {
    if (!text || !size) {
        return false;
    }

    FILE* file = filename ? fopen(filename, "r") : stdin;
    if (!file) {
        return false;
    }

    // Get file size
    if (filename) {
        fseek(file, 0, SEEK_END);
        long file_size = ftell(file);
        fseek(file, 0, SEEK_SET);

        if (file_size < 0) {
            if (filename) fclose(file);
            return false;
        }

        *size = file_size;
    } else {
        // For stdin, we'll read in chunks
        *size = 0;
        size_t capacity = 1024;
        *text = malloc(capacity);
        if (!*text) {
            return false;
        }

        char buffer[1024];
        size_t bytes_read;
        while ((bytes_read = fread(buffer, 1, sizeof(buffer), file)) > 0) {
            if (*size + bytes_read > capacity) {
                capacity *= 2;
                char* new_text = realloc(*text, capacity);
                if (!new_text) {
                    free(*text);
                    *text = NULL;
                    return false;
                }
                *text = new_text;
            }
            memcpy(*text + *size, buffer, bytes_read);
            *size += bytes_read;
        }

        if (filename) fclose(file);
        return true;
    }

    // Allocate memory
    *text = malloc(*size + 1);
    if (!*text) {
        if (filename) fclose(file);
        return false;
    }

    // Read file
    size_t bytes_read = fread(*text, 1, *size, file);
    if (filename) fclose(file);

    if (bytes_read != *size) {
        free(*text);
        *text = NULL;
        return false;
    }

    (*text)[*size] = '\0';
    return true;
}

bool write_text(const char* filename, const char* text, size_t size) {
    if (!text) {
        return false;
    }

    FILE* file = filename ? fopen(filename, "w") : stdout;
    if (!file) {
        return false;
    }

    size_t written = fwrite(text, 1, size, file);
    if (filename) fclose(file);

    return written == size;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }

    const char* command = argv[1];
    const char* message = NULL;
    const char* message_file = NULL;
    const char* carrier = NULL;
    const char* carrier_file = NULL;
    const char* output_file = NULL;
    const char* output_file_long = NULL;
    const char* input_file = NULL;
    const char* input_file_long = NULL;
    const char* password = NULL;

    // Parse command line arguments
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 && i + 1 < argc) {
            message = argv[++i];
        } else if (strcmp(argv[i], "--message-file") == 0 && i + 1 < argc) {
            message_file = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            carrier = argv[++i];
        } else if (strcmp(argv[i], "--carrier-file") == 0 && i + 1 < argc) {
            carrier_file = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) {
            output_file = argv[++i];
        } else if (strcmp(argv[i], "--output-file") == 0 && i + 1 < argc) {
            output_file_long = argv[++i];
        } else if (strcmp(argv[i], "-i") == 0 && i + 1 < argc) {
            input_file = argv[++i];
        } else if (strcmp(argv[i], "--input-file") == 0 && i + 1 < argc) {
            input_file_long = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0 && i + 1 < argc) {
            password = argv[++i];
        }
    }

    // Prefer long output/input file if both are set
    if (output_file_long) output_file = output_file_long;
    if (input_file_long) input_file = input_file_long;

    char* buffer = (char*)malloc(MAX_BUFFER_SIZE);
    if (!buffer) {
        fprintf(stderr, "Error: Failed to allocate memory\n");
        return 1;
    }

    int result = 0;

    if (strcmp(command, "encode") == 0) {
        // Read message
        char* msg_buf = NULL;
        size_t msg_len = 0;
        if (message_file) {
            if (!read_text(message_file, &msg_buf, &msg_len)) {
                fprintf(stderr, "Error: Failed to read message file\n");
                result = 1;
                goto cleanup;
            }
        } else if (message) {
            msg_buf = (char*)message;
            msg_len = strlen(message);
        } else {
            fprintf(stderr, "Error: Message (-m or --message-file) is required for encoding\n");
            result = 1;
            goto cleanup;
        }

        // Read carrier
        char* carrier_buf = NULL;
        size_t carrier_len = 0;
        if (carrier_file) {
            if (!read_text(carrier_file, &carrier_buf, &carrier_len)) {
                fprintf(stderr, "Error: Failed to read carrier file\n");
                result = 1;
                goto cleanup;
            }
        } else if (carrier) {
            carrier_buf = (char*)carrier;
            carrier_len = strlen(carrier);
        } else {
            carrier_buf = "";
            carrier_len = 0;
        }

        size_t output_len = calculate_encoded_size(msg_len, carrier_len);
        if (output_len > MAX_BUFFER_SIZE) {
            fprintf(stderr, "Error: Output would exceed maximum buffer size\n");
            result = 1;
            goto cleanup;
        }

        size_t encoded_len = encode_message(msg_buf,
                                            msg_len,
                                            carrier_buf,
                                            carrier_len,
                                            buffer,
                                            MAX_BUFFER_SIZE,
                                            password,
                                            password ? strlen(password) : 0);
        if (message_file) free(msg_buf);
        if (carrier_file) free(carrier_buf);

        if (encoded_len == 0) {
            fprintf(stderr, "Error: Failed to encode message\n");
            result = 1;
            goto cleanup;
        }

        // Write output
        if (!write_text(output_file, buffer, encoded_len)) {
            fprintf(stderr, "Error: Failed to write output\n");
            result = 1;
            goto cleanup;
        }

    } else if (strcmp(command, "decode") == 0) {
        // Read input
        char* input_buf = NULL;
        size_t input_len = 0;
        if (input_file) {
            if (!read_text(input_file, &input_buf, &input_len)) {
                fprintf(stderr, "Error: Failed to read input file\n");
                result = 1;
                goto cleanup;
            }
        } else {
            fprintf(stderr, "Error: Input file (-i or --input-file) is required for decoding\n");
            result = 1;
            goto cleanup;
        }

        // Decode message
        size_t decoded_len = decode_message((char*)input_buf,
                                            input_len,
                                            buffer,
                                            MAX_BUFFER_SIZE,
                                            password,
                                            password ? strlen(password) : 0);
        if (input_file) free(input_buf);

        if (decoded_len == 0) {
            fprintf(stderr, "Error: Failed to decode message\n");
            result = 1;
            goto cleanup;
        }

        // Write output
        if (!write_text(output_file, buffer, decoded_len)) {
            fprintf(stderr, "Error: Failed to write output\n");
            result = 1;
            goto cleanup;
        }
    } else {
        fprintf(stderr, "Error: Unknown command '%s'\n", command);
        result = 1;
    }

cleanup:
    free(buffer);
    return result;
}
