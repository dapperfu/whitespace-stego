/**
 * @file utils.c
 * @brief Implementation of utility functions for whitespace steganography
 */

#include "utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Base64 encoding table
static const char base64_table[] =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

// Zero-width whitespace characters (UTF-8 encoded)
static const char ZERO_WIDTH_NON_JOINER[] = "\xE2\x80\x8C";  // U+200C
static const char ZERO_WIDTH_JOINER[] = "\xE2\x80\x8D";      // U+200D

size_t base64_encode(const uint8_t* input, size_t input_len, char* output, size_t output_len) {
    if (!input || !output || output_len < ((input_len + 2) / 3) * 4) {
        return 0;
    }

    size_t i = 0;
    size_t j = 0;

    while (i < input_len) {
        uint32_t octet_a = i < input_len ? input[i++] : 0;
        uint32_t octet_b = i < input_len ? input[i++] : 0;
        uint32_t octet_c = i < input_len ? input[i++] : 0;

        uint32_t triple = (octet_a << 16) + (octet_b << 8) + octet_c;

        output[j++] = base64_table[(triple >> 18) & 0x3F];
        output[j++] = base64_table[(triple >> 12) & 0x3F];
        output[j++] = base64_table[(triple >> 6) & 0x3F];
        output[j++] = base64_table[triple & 0x3F];
    }

    // Add padding
    size_t padding = (3 - (input_len % 3)) % 3;
    for (size_t k = 0; k < padding; k++) {
        output[j - 1 - k] = '=';
    }

    return j;
}

size_t base64_decode(const char* input, size_t input_len, uint8_t* output, size_t output_len) {
    if (!input || !output || input_len % 4 != 0) {
        return 0;
    }

    size_t padding = 0;
    if (input_len > 0) {
        if (input[input_len - 1] == '=')
            padding++;
        if (input[input_len - 2] == '=')
            padding++;
    }

    size_t decoded_len = (input_len / 4) * 3 - padding;
    if (output_len < decoded_len) {
        return 0;
    }

    size_t i = 0;
    size_t j = 0;

    while (i < input_len) {
        uint32_t sextet_a = input[i] == '=' ? 0 : strchr(base64_table, input[i]) - base64_table;
        uint32_t sextet_b =
            input[i + 1] == '=' ? 0 : strchr(base64_table, input[i + 1]) - base64_table;
        uint32_t sextet_c =
            input[i + 2] == '=' ? 0 : strchr(base64_table, input[i + 2]) - base64_table;
        uint32_t sextet_d =
            input[i + 3] == '=' ? 0 : strchr(base64_table, input[i + 3]) - base64_table;

        uint32_t triple = (sextet_a << 18) + (sextet_b << 12) + (sextet_c << 6) + sextet_d;

        if (j < decoded_len)
            output[j++] = (triple >> 16) & 0xFF;
        if (j < decoded_len)
            output[j++] = (triple >> 8) & 0xFF;
        if (j < decoded_len)
            output[j++] = triple & 0xFF;

        i += 4;
    }

    return decoded_len;
}

size_t binary_to_zerowidth(const uint8_t* input,
                           size_t input_len,
                           char* output,
                           size_t output_len) {
    // For simplicity, use ZERO_WIDTH_JOINER for 1, ZERO_WIDTH_NON_JOINER for 0 (each 3 bytes)
    if (!input || !output || output_len < input_len * 8 * 3) {
        return 0;
    }

    size_t j = 0;
    for (size_t i = 0; i < input_len; i++) {
        uint8_t byte = input[i];
        for (int bit = 7; bit >= 0; bit--) {
            const char* zw = (byte & (1 << bit)) ? ZERO_WIDTH_JOINER : ZERO_WIDTH_NON_JOINER;
            memcpy(output + j, zw, 3);
            j += 3;
        }
    }

    return j;
}

size_t zerowidth_to_binary(const char* input,
                           size_t input_len,
                           uint8_t* output,
                           size_t output_len) {
    // Each zero-width char is 3 bytes, 8 bits per byte
    if (!input || !output || input_len % 24 != 0 || output_len < input_len / 24) {
        return 0;
    }

    size_t j = 0;
    for (size_t i = 0; i < input_len; i += 24) {
        uint8_t byte = 0;
        for (int bit = 0; bit < 8; bit++) {
            const char* zw = input + i + bit * 3;
            if (memcmp(zw, ZERO_WIDTH_JOINER, 3) == 0) {
                byte |= (1 << (7 - bit));
            }
        }
        output[j++] = byte;
    }

    return j;
}

bool xor_encrypt(uint8_t* data, size_t data_len, const char* password, size_t password_len) {
    if (!data || !password || password_len == 0) {
        return false;
    }

    for (size_t i = 0; i < data_len; i++) {
        data[i] ^= password[i % password_len];
    }

    return true;
}

bool read_file(const char* filename, uint8_t** data, size_t* size) {
    if (!filename || !data || !size) {
        return false;
    }

    FILE* file = fopen(filename, "rb");
    if (!file) {
        return false;
    }

    // Get file size
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    if (file_size < 0) {
        fclose(file);
        return false;
    }

    // Allocate memory
    *data = (uint8_t*)malloc(file_size);
    if (!*data) {
        fclose(file);
        return false;
    }

    // Read file
    size_t bytes_read = fread(*data, 1, file_size, file);
    fclose(file);

    if (bytes_read != (size_t)file_size) {
        free(*data);
        *data = NULL;
        return false;
    }

    *size = bytes_read;
    return true;
}

bool write_file(const char* filename, const uint8_t* data, size_t size) {
    if (!filename || !data) {
        return false;
    }

    FILE* file = fopen(filename, "wb");
    if (!file) {
        return false;
    }

    size_t bytes_written = fwrite(data, 1, size, file);
    fclose(file);

    return bytes_written == size;
}

void strip_zero_width_and_control(const char* input, char* output) {
    // UTF-8 encoded zero-width and control characters
    const char* zw_chars[] = {
        "\xE2\x80\x8C", // U+200C ZWNJ
        "\xE2\x80\x8B", // U+200B ZWSP
        "\xE2\x81\xA0", // U+2060 START_MARKER (Word Joiner)
        "\xE2\x81\xA1"  // U+2061 END_MARKER (Function Application)
    };
    size_t num_zw = sizeof(zw_chars) / sizeof(zw_chars[0]);
    const char* p = input;
    char* out = output;
    while (*p) {
        int matched = 0;
        for (size_t i = 0; i < num_zw; ++i) {
            size_t len = strlen(zw_chars[i]);
            if (strncmp(p, zw_chars[i], len) == 0) {
                p += len;
                matched = 1;
                break;
            }
        }
        if (!matched) {
            *out++ = *p++;
        }
    }
    *out = '\0';
}
