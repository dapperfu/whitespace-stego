/* Decoding functions for whitespace steganography */

#include <string.h>
#include <stdlib.h>
#include "whitespace_stego.h"

extern size_t base64_decode(const char *input, size_t input_len,
                             unsigned char *output, size_t output_size);

/* Unicode control characters */
#define CONTROL_START "\xE2\x81\xA0"  /* U+2060 Word Joiner */
#define CONTROL_END "\xE2\x81\xA3"    /* U+2063 Invisible Separator */
#define BIT_0 "\xE2\x80\x8B"          /* U+200B Zero Width Space */
#define BIT_1 "\xE2\x80\x8C"          /* U+200C Zero Width Non-Joiner */

int whitespace_decode(const char *encoded_text, const char *password,
                      char *output, size_t output_size, size_t *output_len) {
    if (!encoded_text || !output || !output_len) {
        return STEGO_ERROR_DECODING;
    }

    if (password && strlen(password) == 0) {
        return STEGO_ERROR_DECODING;
    }

    /* Find control markers */
    char *start_ptr = strstr((char *)encoded_text, CONTROL_START);
    char *end_ptr = strstr((char *)encoded_text, CONTROL_END);

    if (!start_ptr) {
        return STEGO_ERROR_MISSING_MARKER;
    }
    if (!end_ptr) {
        return STEGO_ERROR_MISSING_MARKER;
    }

    /* Extract payload (between markers, excluding markers) */
    size_t payload_start = start_ptr - encoded_text + 3; /* 3 bytes for CONTROL_START */
    size_t payload_end = end_ptr - encoded_text;
    size_t payload_len = payload_end - payload_start;

    if (payload_len == 0) {
        /* Empty payload means empty message */
        if (output_size < 1) {
            return STEGO_ERROR_MEMORY;
        }
        output[0] = '\0';
        *output_len = 0;
        return STEGO_SUCCESS;
    }

    /* Convert invisible characters to binary bits */
    char *payload = malloc(payload_len + 1);
    if (!payload) {
        return STEGO_ERROR_MEMORY;
    }
    memcpy(payload, &encoded_text[payload_start], payload_len);
    payload[payload_len] = '\0';

    size_t binary_bits_len = payload_len / 3; /* Each invisible char is 3 bytes */
    char *binary_bits = malloc(binary_bits_len + 1);
    if (!binary_bits) {
        free(payload);
        return STEGO_ERROR_MEMORY;
    }

    size_t bit_idx = 0;
    for (size_t i = 0; i < payload_len; i += 3) {
        if (memcmp(&payload[i], BIT_0, 3) == 0) {
            binary_bits[bit_idx++] = '0';
        } else if (memcmp(&payload[i], BIT_1, 3) == 0) {
            binary_bits[bit_idx++] = '1';
        } else {
            free(payload);
            free(binary_bits);
            return STEGO_ERROR_INVALID_PAYLOAD;
        }
    }
    binary_bits[bit_idx] = '\0';

    /* Check if payload is complete (divisible by 8) */
    if (bit_idx % 8 != 0) {
        free(payload);
        free(binary_bits);
        return STEGO_ERROR_DECODING;
    }

    /* Group bits into 8-bit bytes */
    size_t bytes_len = bit_idx / 8;
    unsigned char *bytes_list = malloc(bytes_len);
    if (!bytes_list) {
        free(payload);
        free(binary_bits);
        return STEGO_ERROR_MEMORY;
    }

    for (size_t i = 0; i < bytes_len; i++) {
        unsigned char byte = 0;
        for (int j = 0; j < 8; j++) {
            char bit = binary_bits[i * 8 + j];
            if (bit == '1') {
                byte |= (1 << (7 - j));
            } else if (bit != '0') {
                free(payload);
                free(binary_bits);
                free(bytes_list);
                return STEGO_ERROR_DECODING;
            }
        }
        bytes_list[i] = byte;
    }

    /* Convert bytes to Base64 string */
    /* Base64 strings must be a multiple of 4 characters */
    if (bytes_len % 4 != 0) {
        free(payload);
        free(binary_bits);
        free(bytes_list);
        return STEGO_ERROR_INVALID_BASE64;
    }

    char *base64_str = malloc(bytes_len + 1);
    if (!base64_str) {
        free(payload);
        free(binary_bits);
        free(bytes_list);
        return STEGO_ERROR_MEMORY;
    }
    memcpy(base64_str, bytes_list, bytes_len);
    base64_str[bytes_len] = '\0';

    /* Validate Base64 string contains only valid characters */
    for (size_t i = 0; i < bytes_len; i++) {
        char c = base64_str[i];
        if (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') ||
              (c >= '0' && c <= '9') || c == '+' || c == '/' || c == '=')) {
            free(payload);
            free(binary_bits);
            free(bytes_list);
            free(base64_str);
            return STEGO_ERROR_INVALID_BASE64;
        }
    }

    /* Decode Base64 to UTF-8 bytes */
    size_t utf8_size = (bytes_len / 4) * 3 + 4; /* Overestimate */
    unsigned char *utf8_bytes = malloc(utf8_size);
    if (!utf8_bytes) {
        free(payload);
        free(binary_bits);
        free(bytes_list);
        free(base64_str);
        return STEGO_ERROR_MEMORY;
    }

    size_t utf8_len = base64_decode(base64_str, bytes_len, utf8_bytes, utf8_size);
    if (utf8_len == 0) {
        free(payload);
        free(binary_bits);
        free(bytes_list);
        free(base64_str);
        free(utf8_bytes);
        return STEGO_ERROR_INVALID_BASE64;
    }

    /* Apply XOR decryption if password is provided */
    if (password) {
        size_t password_len = strlen(password);
        for (size_t i = 0; i < utf8_len; i++) {
            utf8_bytes[i] ^= password[i % password_len];
        }
    }

    /* Check output size */
    if (output_size < utf8_len + 1) {
        free(payload);
        free(binary_bits);
        free(bytes_list);
        free(base64_str);
        free(utf8_bytes);
        return STEGO_ERROR_MEMORY;
    }

    /* Copy decoded message to output */
    memcpy(output, utf8_bytes, utf8_len);
    output[utf8_len] = '\0';
    *output_len = utf8_len;

    free(payload);
    free(binary_bits);
    free(bytes_list);
    free(base64_str);
    free(utf8_bytes);
    return STEGO_SUCCESS;
}

