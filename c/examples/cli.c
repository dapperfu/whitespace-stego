#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/whitespace_stego.h"

#define MAX_BUFFER_SIZE 65536

int read_file(const char *filename, char *buffer, size_t buffer_size) {
    if (strcmp(filename, "-") == 0) {
        size_t total = 0;
        while (total < buffer_size - 1) {
            size_t n = fread(buffer + total, 1, buffer_size - total - 1, stdin);
            if (n == 0) break;
            total += n;
        }
        buffer[total] = '\0';
        return 0;
    }

    FILE *f = fopen(filename, "r");
    if (!f) {
        return -1;
    }
    size_t n = fread(buffer, 1, buffer_size - 1, f);
    buffer[n] = '\0';
    fclose(f);
    return 0;
}

int write_file(const char *filename, const char *content) {
    if (strcmp(filename, "-") == 0) {
        printf("%s", content);
        return 0;
    }

    FILE *f = fopen(filename, "w");
    if (!f) {
        return -1;
    }
    fprintf(f, "%s", content);
    fclose(f);
    return 0;
}

const char *get_arg(int argc, char *argv[], const char *flag) {
    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], flag) == 0 && i + 1 < argc) {
            return argv[i + 1];
        }
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <encode|decode> [options]\n", argv[0]);
        fprintf(stderr, "\nCommands:\n");
        fprintf(stderr, "  encode [message] [-i <input>] [-o <output>] [-c <carrier>] [-p <password>]\n");
        fprintf(stderr, "  decode [encoded] [-i <input>] [-o <output>] [-p <password>]\n");
        fprintf(stderr, "\nOptions:\n");
        fprintf(stderr, "  -i, --input <file>   Input file (use '-' for stdin)\n");
        fprintf(stderr, "  -o, --output <file>  Output file (use '-' for stdout)\n");
        fprintf(stderr, "  -c, --carrier <text> Carrier text (encode only)\n");
        fprintf(stderr, "  -p, --password <pwd> Password for encryption/decryption\n");
        return 1;
    }

    const char *command = argv[1];

    if (strcmp(command, "encode") == 0) {
        const char *input = get_arg(argc - 2, &argv[2], "-i");
        if (!input) input = get_arg(argc - 2, &argv[2], "--input");
        const char *output = get_arg(argc - 2, &argv[2], "-o");
        if (!output) output = get_arg(argc - 2, &argv[2], "--output");
        const char *carrier = get_arg(argc - 2, &argv[2], "-c");
        if (!carrier) carrier = get_arg(argc - 2, &argv[2], "--carrier");
        const char *password = get_arg(argc - 2, &argv[2], "-p");
        if (!password) password = get_arg(argc - 2, &argv[2], "--password");

        char message[MAX_BUFFER_SIZE];
        if (input) {
            if (read_file(input, message, sizeof(message)) != 0) {
                fprintf(stderr, "Error: failed to read input file\n");
                return 1;
            }
        } else if (argc >= 3 && strcmp(argv[2], "-") != 0) {
            strncpy(message, argv[2], sizeof(message) - 1);
            message[sizeof(message) - 1] = '\0';
        } else if (argc >= 3 && strcmp(argv[2], "-") == 0) {
            if (read_file("-", message, sizeof(message)) != 0) {
                fprintf(stderr, "Error: failed to read from stdin\n");
                return 1;
            }
        } else {
            fprintf(stderr, "Error: message required (provide as argument, -i/--input, or '-' for stdin)\n");
            return 1;
        }

        char output_buf[MAX_BUFFER_SIZE];
        size_t output_len;
        int result = whitespace_encode(message, carrier, password, output_buf, sizeof(output_buf), &output_len);

        if (result != STEGO_SUCCESS) {
            fprintf(stderr, "Error: %s\n", whitespace_error_string(result));
            return 1;
        }

        if (output) {
            char *output_str = malloc(output_len + 2);
            if (!output_str) {
                fprintf(stderr, "Error: memory allocation failed\n");
                return 1;
            }
            strcpy(output_str, output_buf);
            strcat(output_str, "\n");
            if (write_file(output, output_str) != 0) {
                fprintf(stderr, "Error: failed to write output file\n");
                free(output_str);
                return 1;
            }
            free(output_str);
        } else {
            printf("%s\n", output_buf);
        }
        return 0;

    } else if (strcmp(command, "decode") == 0) {
        const char *input = get_arg(argc - 2, &argv[2], "-i");
        if (!input) input = get_arg(argc - 2, &argv[2], "--input");
        const char *output = get_arg(argc - 2, &argv[2], "-o");
        if (!output) output = get_arg(argc - 2, &argv[2], "--output");
        const char *password = get_arg(argc - 2, &argv[2], "-p");
        if (!password) password = get_arg(argc - 2, &argv[2], "--password");

        char encoded_text[MAX_BUFFER_SIZE];
        if (input) {
            if (read_file(input, encoded_text, sizeof(encoded_text)) != 0) {
                fprintf(stderr, "Error: failed to read input file\n");
                return 1;
            }
        } else if (argc >= 3 && strcmp(argv[2], "-") != 0) {
            strncpy(encoded_text, argv[2], sizeof(encoded_text) - 1);
            encoded_text[sizeof(encoded_text) - 1] = '\0';
        } else if (argc >= 3 && strcmp(argv[2], "-") == 0) {
            if (read_file("-", encoded_text, sizeof(encoded_text)) != 0) {
                fprintf(stderr, "Error: failed to read from stdin\n");
                return 1;
            }
        } else {
            fprintf(stderr, "Error: encoded text required (provide as argument, -i/--input, or '-' for stdin)\n");
            return 1;
        }

        char output_buf[MAX_BUFFER_SIZE];
        size_t output_len;
        int result = whitespace_decode(encoded_text, password, output_buf, sizeof(output_buf), &output_len);

        if (result != STEGO_SUCCESS) {
            fprintf(stderr, "Error: %s\n", whitespace_error_string(result));
            return 1;
        }

        if (output) {
            char *output_str = malloc(output_len + 2);
            if (!output_str) {
                fprintf(stderr, "Error: memory allocation failed\n");
                return 1;
            }
            strcpy(output_str, output_buf);
            strcat(output_str, "\n");
            if (write_file(output, output_str) != 0) {
                fprintf(stderr, "Error: failed to write output file\n");
                free(output_str);
                return 1;
            }
            free(output_str);
        } else {
            printf("%s\n", output_buf);
        }
        return 0;

    } else {
        fprintf(stderr, "Unknown command: %s\n", command);
        return 1;
    }
}

