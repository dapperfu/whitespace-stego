#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/whitespace_stego.h"

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <encode|decode> <text>\n", argv[0]);
        fprintf(stderr, "  encode: %s encode <message> [-c <carrier>]\n", argv[0]);
        fprintf(stderr, "  decode: %s decode <encoded_text>\n", argv[0]);
        return 1;
    }

    const char *command = argv[1];

    if (strcmp(command, "encode") == 0) {
        if (argc < 3) {
            fprintf(stderr, "Error: message required for encode\n");
            return 1;
        }

        const char *message = argv[2];
        const char *carrier = NULL;

        // Check for carrier option
        for (int i = 3; i < argc; i++) {
            if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier") == 0) {
                if (i + 1 < argc) {
                    carrier = argv[i + 1];
                }
            }
        }

        char output[4096];
        size_t output_len;
        int result = whitespace_encode(message, carrier, output, sizeof(output), &output_len);

        if (result != STEGO_SUCCESS) {
            fprintf(stderr, "Error: %s\n", whitespace_error_string(result));
            return 1;
        }

        printf("%s\n", output);
        return 0;

    } else if (strcmp(command, "decode") == 0) {
        if (argc < 3) {
            fprintf(stderr, "Error: encoded text required for decode\n");
            return 1;
        }

        const char *encoded_text = argv[2];
        char output[4096];
        size_t output_len;
        int result = whitespace_decode(encoded_text, output, sizeof(output), &output_len);

        if (result != STEGO_SUCCESS) {
            fprintf(stderr, "Error: %s\n", whitespace_error_string(result));
            return 1;
        }

        printf("%s\n", output);
        return 0;

    } else {
        fprintf(stderr, "Unknown command: %s\n", command);
        return 1;
    }
}

