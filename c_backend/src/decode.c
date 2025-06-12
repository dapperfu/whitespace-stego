/**
 * @file decode.c
 * @brief Implementation of decoding functions for whitespace steganography
 */

#include "decode.h"
#include "utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Start and stop markers for encoded messages
static const char START_MARKER[] = "\u2060";  // Word Joiner
static const char STOP_MARKER[] = "\u2061";   // Function Application

size_t calculate_decoded_size(size_t input_len) {
    // Each 8 zero-width characters represent 1 byte
    // Base64 encoding expands data by 4/3
    return (input_len / 8) * 3 / 4;
}

size_t decode_message(const char* input,
                      size_t input_len,
                      char* output,
                      size_t output_len,
                      const char* password,
                      size_t password_len) {
    if (!input || !output || input_len == 0) {
        return 0;
    }

    // Find start and stop markers
    const char* start = strstr(input, START_MARKER);
    const char* stop = strstr(input, STOP_MARKER);

    if (!start || !stop || stop <= start || stop + strlen(STOP_MARKER) > input + input_len) {
        return 0;
    }

    // Calculate length of zero-width encoded data
    size_t zw_len = stop - start - strlen(START_MARKER);
    if (zw_len % 8 != 0) {
        return 0;
    }

    // Allocate temporary buffers
    uint8_t* binary_buffer = (uint8_t*)malloc(zw_len / 8);
    if (!binary_buffer) {
        return 0;
    }

    // Convert zero-width characters to binary
    size_t binary_len =
        zerowidth_to_binary(start + strlen(START_MARKER), zw_len, binary_buffer, zw_len / 8);
    if (binary_len == 0) {
        free(binary_buffer);
        return 0;
    }

    // Base64 decode
    size_t decoded_len =
        base64_decode((char*)binary_buffer, binary_len, (uint8_t*)output, output_len);
    free(binary_buffer);

    if (decoded_len == 0) {
        return 0;
    }

    // Apply password decryption if provided
    if (password && password_len > 0) {
        if (!xor_encrypt((uint8_t*)output, decoded_len, password, password_len)) {
            return 0;
        }
    }

    return decoded_len;
}
