/**
 * @file encode.c
 * @brief Implementation of encoding functions for whitespace steganography
 */

#include "encode.h"
#include "utils.h"
#include <string.h>

// Start and stop markers for encoded messages
static const char START_MARKER = '\u200B'; // Zero-width space
static const char STOP_MARKER = '\uFEFF';  // Zero-width no-break space

size_t calculate_encoded_size(size_t message_len, size_t carrier_len) {
    // Base64 encoding expands data by 4/3
    size_t base64_len = ((message_len + 2) / 3) * 4;
    
    // Each byte becomes 8 zero-width characters
    size_t zerowidth_len = base64_len * 8;
    
    // Add start and stop markers
    size_t total_len = carrier_len + zerowidth_len + 2;
    
    return total_len;
}

size_t encode_message(
    const char* message,
    size_t message_len,
    const char* carrier,
    size_t carrier_len,
    char* output,
    size_t output_len,
    const char* password,
    size_t password_len
) {
    if (!message || !carrier || !output) {
        return 0;
    }

    // Calculate required buffer sizes
    size_t base64_len = ((message_len + 2) / 3) * 4;
    size_t zerowidth_len = base64_len * 8;
    size_t total_len = carrier_len + zerowidth_len + 2;

    if (output_len < total_len) {
        return 0;
    }

    // Allocate temporary buffers
    uint8_t* message_copy = (uint8_t*)malloc(message_len);
    if (!message_copy) {
        return 0;
    }
    memcpy(message_copy, message, message_len);

    // Apply password encryption if provided
    if (password && password_len > 0) {
        if (!xor_encrypt(message_copy, message_len, password, password_len)) {
            free(message_copy);
            return 0;
        }
    }

    // Base64 encode the message
    char* base64_buffer = (char*)malloc(base64_len);
    if (!base64_buffer) {
        free(message_copy);
        return 0;
    }

    size_t encoded_len = base64_encode(message_copy, message_len, base64_buffer, base64_len);
    free(message_copy);

    if (encoded_len == 0) {
        free(base64_buffer);
        return 0;
    }

    // Convert to zero-width characters
    char* zerowidth_buffer = (char*)malloc(zerowidth_len);
    if (!zerowidth_buffer) {
        free(base64_buffer);
        return 0;
    }

    size_t zw_len = binary_to_zerowidth((uint8_t*)base64_buffer, encoded_len, zerowidth_buffer, zerowidth_len);
    free(base64_buffer);

    if (zw_len == 0) {
        free(zerowidth_buffer);
        return 0;
    }

    // Construct final output
    size_t pos = 0;

    // Copy carrier text
    memcpy(output + pos, carrier, carrier_len);
    pos += carrier_len;

    // Add start marker
    output[pos++] = START_MARKER;

    // Add zero-width encoded message
    memcpy(output + pos, zerowidth_buffer, zw_len);
    pos += zw_len;

    // Add stop marker
    output[pos++] = STOP_MARKER;

    free(zerowidth_buffer);
    return pos;
} 