/* Encoding functions for whitespace steganography */

#include <string.h>
#include <stdlib.h>
#include "whitespace_stego.h"

extern size_t base64_encode(const unsigned char *input, size_t input_len,
                             char *output, size_t output_size);

/* Unicode control characters */
#define CONTROL_START "\xE2\x81\xA0"  /* U+2060 Word Joiner */
#define CONTROL_END "\xE2\x81\xA3"    /* U+2063 Invisible Separator */
#define BIT_0 "\xE2\x80\x8B"          /* U+200B Zero Width Space */
#define BIT_1 "\xE2\x80\x8C"          /* U+200C Zero Width Non-Joiner */

int whitespace_encode(const char *message, const char *carrier, const char *password,
                      char *output, size_t output_size, size_t *output_len) {
    if (!message || !output || !output_len) {
        return STEGO_ERROR_ENCODING;
    }

    if (password && strlen(password) == 0) {
        return STEGO_ERROR_ENCODING;
    }

    size_t message_len = strlen(message);
    if (message_len == 0) {
        /* Empty message - return just markers */
        if (output_size < 6) {
            return STEGO_ERROR_MEMORY;
        }
        strcpy(output, CONTROL_START CONTROL_END);
        *output_len = 6;
        return STEGO_SUCCESS;
    }

    /* Convert message to UTF-8 bytes */
    unsigned char *utf8_bytes = malloc(message_len);
    if (!utf8_bytes) {
        return STEGO_ERROR_MEMORY;
    }
    memcpy(utf8_bytes, message, message_len);
    size_t utf8_len = message_len;

    /* Apply XOR encryption if password is provided */
    if (password) {
        size_t password_len = strlen(password);
        for (size_t i = 0; i < utf8_len; i++) {
            utf8_bytes[i] ^= password[i % password_len];
        }
    }

    /* Estimate Base64 output size */
    size_t base64_size = ((utf8_len + 2) / 3) * 4 + 1;
    char *base64_str = malloc(base64_size);
    if (!base64_str) {
        return STEGO_ERROR_MEMORY;
    }

    size_t base64_len = base64_encode(utf8_bytes, utf8_len, base64_str, base64_size);
    if (base64_len == 0) {
        free(base64_str);
        return STEGO_ERROR_ENCODING;
    }

    /* Convert Base64 to binary bits */
    size_t binary_bits_len = base64_len * 8;
    char *binary_bits = malloc(binary_bits_len + 1);
    if (!binary_bits) {
        free(base64_str);
        return STEGO_ERROR_MEMORY;
    }

    size_t bit_idx = 0;
    for (size_t i = 0; i < base64_len; i++) {
        unsigned char byte = (unsigned char)base64_str[i];
        for (int j = 7; j >= 0; j--) {
            binary_bits[bit_idx++] = ((byte >> j) & 1) ? '1' : '0';
        }
    }
    binary_bits[bit_idx] = '\0';

    /* Map bits to invisible Unicode characters */
    size_t payload_size = binary_bits_len * 3 + 1; /* Each char is 3 bytes UTF-8 */
    char *encoded_payload = malloc(payload_size);
    if (!encoded_payload) {
        free(base64_str);
        free(binary_bits);
        return STEGO_ERROR_MEMORY;
    }

    size_t payload_idx = 0;
    for (size_t i = 0; i < binary_bits_len; i++) {
        if (binary_bits[i] == '0') {
            strcpy(&encoded_payload[payload_idx], BIT_0);
            payload_idx += 3;
        } else if (binary_bits[i] == '1') {
            strcpy(&encoded_payload[payload_idx], BIT_1);
            payload_idx += 3;
        }
    }
    encoded_payload[payload_idx] = '\0';

    /* Wrap with control markers */
    size_t encoded_size = 3 + payload_idx + 3 + 1; /* START + payload + END + null */
    if (output_size < encoded_size) {
        free(base64_str);
        free(binary_bits);
        free(encoded_payload);
        return STEGO_ERROR_MEMORY;
    }

    strcpy(output, CONTROL_START);
    strcat(output, encoded_payload);
    strcat(output, CONTROL_END);

    /* If carrier text is provided, embed the encoded message */
    if (carrier && strlen(carrier) > 0) {
        /* Check if carrier contains control characters */
        if (strstr(carrier, CONTROL_START) || strstr(carrier, CONTROL_END)) {
            free(base64_str);
            free(binary_bits);
            free(encoded_payload);
            return STEGO_ERROR_ENCODING;
        }

        /* Insert after first character */
        size_t carrier_len = strlen(carrier);
        size_t total_size = 1 + encoded_size - 1 + carrier_len - 1 + 1;
        if (output_size < total_size) {
            free(base64_str);
            free(binary_bits);
            free(encoded_payload);
            return STEGO_ERROR_MEMORY;
        }

        char *final_output = malloc(total_size);
        if (!final_output) {
            free(base64_str);
            free(binary_bits);
            free(encoded_payload);
            return STEGO_ERROR_MEMORY;
        }

        final_output[0] = carrier[0];
        strcpy(&final_output[1], output);
        strcat(final_output, &carrier[1]);
        strcpy(output, final_output);
        free(final_output);
        *output_len = strlen(output);
    } else {
        *output_len = strlen(output);
    }

    free(utf8_bytes);
    free(base64_str);
    free(binary_bits);
    free(encoded_payload);
    return STEGO_SUCCESS;
}

