#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/whitespace_stego.h"

int test_encode_decode() {
    const char *message = "Hello, World!";
    char output[1024];
    size_t output_len;
    int result;

    printf("Testing encode...\n");
    result = whitespace_encode(message, NULL, output, sizeof(output), &output_len);
    if (result != STEGO_SUCCESS) {
        printf("Encode failed: %s\n", whitespace_error_string(result));
        return 1;
    }
    printf("Encoded length: %zu\n", output_len);

    printf("Testing decode...\n");
    char decoded[1024];
    size_t decoded_len;
    result = whitespace_decode(output, decoded, sizeof(decoded), &decoded_len);
    if (result != STEGO_SUCCESS) {
        printf("Decode failed: %s\n", whitespace_error_string(result));
        return 1;
    }

    if (strcmp(decoded, message) != 0) {
        printf("Round-trip failed: expected '%s', got '%s'\n", message, decoded);
        return 1;
    }

    printf("Round-trip test passed!\n");
    return 0;
}

int main() {
    printf("Running whitespace-stego C tests...\n\n");

    if (test_encode_decode() != 0) {
        return 1;
    }

    printf("\nAll tests passed!\n");
    return 0;
}

