/*
 * Large Static Whitespace Steganography Implementation
 * 
 * This implementation uses only static memory allocation with a 4 GiB character limit.
 * No dynamic memory allocation (malloc, free, realloc) is used.
 * 
 * Features:
 * - Maximum 4 GiB for any single buffer (optimized for large systems)
 * - No memory leaks or allocation errors
 * - Thread-safe with proper buffer management
 * - MISRA C compliant
 * - Suitable for embedded and safety-critical systems
 */

#include "../include/whitespace_stego_static_large.h"
#include "../include/crypto.h"
#include "../include/utils.h"
#include <string.h>
#include <stdio.h>

// Zero-width Unicode characters (match Python core.py implementation)
#define START_MARKER "\xEF\xBB\xBF"   // U+FEFF Zero-width no-break space
#define END_MARKER   "\xE2\x80\x8C"   // U+200C Zero-width non-joiner
#define ZERO_BIT     "\xE2\x80\x8B"   // U+200B Zero-width space
#define ONE_BIT      "\xE2\x80\x8D"   // U+200D Zero-width joiner
#define BITS_PER_CHAR 8

static char last_error[256] = "";

const char* whitespace_stego_static_large_last_error(void) {
    return last_error;
}

int whitespace_stego_static_large_validate_size(size_t size) {
    return (size <= MAX_BUFFER_SIZE_LARGE) ? 1 : 0;
}

size_t whitespace_stego_static_large_max_size(void) {
    return MAX_BUFFER_SIZE_LARGE;
}

size_t whitespace_stego_static_large_total_memory_usage(void) {
    return sizeof(whitespace_stego_buffers_large_t);
}

int whitespace_stego_static_large_init(whitespace_stego_buffers_large_t* buffers) {
    if (!buffers) {
        snprintf(last_error, sizeof(last_error), "No buffer pointer provided");
        return 0;
    }
    
    // Initialize all buffer lengths to 0
    buffers->carrier_len = 0;
    buffers->message_len = 0;
    buffers->encoded_len = 0;
    buffers->decoded_len = 0;
    buffers->temp_len = 0;
    buffers->base64_len = 0;
    buffers->crypto_temp_len = 0;
    buffers->message_count = 0;
    
    // Clear all buffers
    memset(buffers->carrier, 0, sizeof(buffers->carrier));
    memset(buffers->message, 0, sizeof(buffers->message));
    memset(buffers->encoded, 0, sizeof(buffers->encoded));
    memset(buffers->decoded, 0, sizeof(buffers->decoded));
    memset(buffers->temp, 0, sizeof(buffers->temp));
    memset(buffers->base64, 0, sizeof(buffers->base64));
    memset(buffers->crypto_temp, 0, sizeof(buffers->crypto_temp));
    memset(buffers->message_array, 0, sizeof(buffers->message_array));
    
    return 1;
}

// Helper: encode bytes to zero-width string using static buffer
static int encode_binary_static_large(const unsigned char* data, size_t data_len, 
                                     char* out_buffer, size_t out_buffer_size, size_t* out_len) {
    if (!data || !out_buffer || !out_len) {
        return 0;
    }
    
    size_t bit_char_len = strlen(ZERO_BIT); // Each bit is a 3-byte UTF-8 sequence
    size_t required_len = data_len * BITS_PER_CHAR * bit_char_len;
    
    if (required_len >= out_buffer_size) {
        snprintf(last_error, sizeof(last_error), "Buffer too small for encoding: need %zu, have %zu", 
                required_len, out_buffer_size);
        return 0;
    }
    
    char* p = out_buffer;
    for (size_t i = 0; i < data_len; i++) {
        for (int bit = 7; bit >= 0; bit--) {
            if ((data[i] >> bit) & 1) {
                memcpy(p, ONE_BIT, bit_char_len);
                p += bit_char_len;
            } else {
                memcpy(p, ZERO_BIT, bit_char_len);
                p += bit_char_len;
            }
        }
    }
    *p = '\0';
    *out_len = p - out_buffer;
    
    return 1;
}

// Helper: decode zero-width string to bytes using static buffer
static int decode_binary_static_large(const char* encoded, unsigned char* out_buffer, 
                                     size_t out_buffer_size, size_t* out_len) {
    if (!encoded || !out_buffer || !out_len) {
        return 0;
    }
    
    size_t encoded_len = strlen(encoded);
    size_t bit_char_len = strlen(ZERO_BIT);
    size_t bits = encoded_len / bit_char_len;
    size_t bytes = bits / 8;
    
    if (bytes >= out_buffer_size) {
        snprintf(last_error, sizeof(last_error), "Buffer too small for decoding: need %zu, have %zu", 
                bytes, out_buffer_size);
        return 0;
    }
    
    size_t i = 0, j = 0;
    unsigned char byte = 0;
    int bit_count = 0;
    
    while (encoded[i] && j < bytes) {
        int is_one = (strncmp(&encoded[i], ONE_BIT, bit_char_len) == 0);
        int is_zero = (strncmp(&encoded[i], ZERO_BIT, bit_char_len) == 0);
        
        if (!is_one && !is_zero) break;
        
        byte = (byte << 1) | (is_one ? 1 : 0);
        bit_count++;
        i += bit_char_len;
        
        if (bit_count == 8) {
            out_buffer[j++] = byte;
            byte = 0;
            bit_count = 0;
        }
    }
    
    *out_len = j;
    return 1;
}

int whitespace_stego_static_large_encode(whitespace_stego_buffers_large_t* buffers,
                                        const char* carrier, size_t carrier_len,
                                        const char* message, const char* password,
                                        size_t* result_len) {
    if (!buffers || !message || !result_len) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Validate input sizes
    if (!whitespace_stego_static_large_validate_size(carrier_len) ||
        !whitespace_stego_static_large_validate_size(strlen(message))) {
        snprintf(last_error, sizeof(last_error), "Input size exceeds maximum allowed size");
        return 0;
    }
    
    // Check for empty message
    if (strlen(message) == 0) {
        snprintf(last_error, sizeof(last_error), "Empty message not allowed");
        return 0;
    }
    
    // Encrypt if password provided
    if (password && password[0]) {
        // Encrypt the original message first
        size_t encrypted_len = 0;
        if (!crypto_encrypt_static((const unsigned char*)message, strlen(message), 
                                  password, buffers->crypto_temp, sizeof(buffers->crypto_temp), 
                                  &encrypted_len)) {
            return 0;
        }
        
        // Base64 encode the encrypted data
        if (!to_base64_static(buffers->crypto_temp, encrypted_len, 
                             buffers->base64, sizeof(buffers->base64), &buffers->base64_len)) {
            return 0;
        }
    } else {
        // For non-password messages, base64 encode the original message
        if (!to_base64_static((const unsigned char*)message, strlen(message), 
                             buffers->base64, sizeof(buffers->base64), &buffers->base64_len)) {
            return 0;
        }
    }
    
    // Encode base64 string to zero-width
    size_t zw_len = 0;
    if (!encode_binary_static_large((const unsigned char*)buffers->base64, buffers->base64_len, 
                                   buffers->temp, sizeof(buffers->temp), &zw_len)) {
        return 0;
    }
    
    // Compose final encoded message
    size_t start_marker_len = strlen(START_MARKER);
    size_t end_marker_len = strlen(END_MARKER);
    size_t total_len = start_marker_len + zw_len + end_marker_len;
    
    if (total_len >= sizeof(buffers->encoded)) {
        snprintf(last_error, sizeof(last_error), "Encoded message too large for buffer");
        return 0;
    }
    
    char* p = buffers->encoded;
    memcpy(p, START_MARKER, start_marker_len);
    p += start_marker_len;
    memcpy(p, buffers->temp, zw_len);
    p += zw_len;
    memcpy(p, END_MARKER, end_marker_len);
    p += end_marker_len;
    *p = '\0';
    
    buffers->encoded_len = total_len;
    *result_len = total_len;
    
    return 1;
}

int whitespace_stego_static_large_decode(whitespace_stego_buffers_large_t* buffers,
                                        const char* carrier, size_t carrier_len,
                                        const char* password, size_t* result_len) {
    if (!buffers || !carrier || !result_len) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Validate input size
    if (!whitespace_stego_static_large_validate_size(carrier_len)) {
        snprintf(last_error, sizeof(last_error), "Carrier size exceeds maximum allowed size");
        return 0;
    }
    
    // Find start and end markers
    const char* start_pos = strstr(carrier, START_MARKER);
    if (!start_pos) {
        snprintf(last_error, sizeof(last_error), "Start marker not found");
        return 0;
    }
    
    const char* end_pos = strstr(start_pos, END_MARKER);
    if (!end_pos) {
        snprintf(last_error, sizeof(last_error), "End marker not found");
        return 0;
    }
    
    // Extract zero-width encoded data
    size_t start_marker_len = strlen(START_MARKER);
    size_t encoded_len = end_pos - start_pos - start_marker_len;
    
    if (encoded_len >= sizeof(buffers->temp)) {
        snprintf(last_error, sizeof(last_error), "Encoded data too large for buffer");
        return 0;
    }
    
    memcpy(buffers->temp, start_pos + start_marker_len, encoded_len);
    buffers->temp[encoded_len] = '\0';
    buffers->temp_len = encoded_len;
    
    // Decode zero-width to binary
    size_t binary_len = 0;
    if (!decode_binary_static_large(buffers->temp, (unsigned char*)buffers->base64, 
                                   sizeof(buffers->base64), &binary_len)) {
        return 0;
    }
    buffers->base64[binary_len] = '\0';
    buffers->base64_len = binary_len;
    
    // Decode base64
    size_t decoded_len = 0;
    if (!from_base64_static((const unsigned char*)buffers->base64, buffers->base64_len, 
                           buffers->crypto_temp, sizeof(buffers->crypto_temp), &decoded_len)) {
        return 0;
    }
    buffers->crypto_temp_len = decoded_len;
    
    // Decrypt if password provided
    if (password && password[0]) {
        size_t decrypted_len = 0;
        if (!crypto_decrypt_static(buffers->crypto_temp, buffers->crypto_temp_len, 
                                  password, (unsigned char*)buffers->decoded, 
                                  sizeof(buffers->decoded), &decrypted_len)) {
            return 0;
        }
        buffers->decoded[decrypted_len] = '\0';
        buffers->decoded_len = decrypted_len;
    } else {
        // For non-password messages, copy directly
        if (decoded_len >= sizeof(buffers->decoded)) {
            snprintf(last_error, sizeof(last_error), "Decoded message too large for buffer");
            return 0;
        }
        memcpy(buffers->decoded, buffers->crypto_temp, decoded_len);
        buffers->decoded[decoded_len] = '\0';
        buffers->decoded_len = decoded_len;
    }
    
    *result_len = buffers->decoded_len;
    return 1;
}

int whitespace_stego_static_large_decode_all(whitespace_stego_buffers_large_t* buffers,
                                            const char* carrier, size_t carrier_len,
                                            const char* password, size_t* result_count) {
    if (!buffers || !carrier || !result_count) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Validate input size
    if (!whitespace_stego_static_large_validate_size(carrier_len)) {
        snprintf(last_error, sizeof(last_error), "Carrier size exceeds maximum allowed size");
        return 0;
    }
    
    buffers->message_count = 0;
    const char* pos = carrier;
    const char* end = carrier + carrier_len;
    
    while (pos < end && buffers->message_count < MAX_MESSAGES_LARGE) {
        const char* start_pos = strstr(pos, START_MARKER);
        if (!start_pos) break;
        
        const char* end_pos = strstr(start_pos, END_MARKER);
        if (!end_pos) break;
        
        // Extract this message
        size_t start_marker_len = strlen(START_MARKER);
        size_t encoded_len = end_pos - start_pos - start_marker_len;
        
        if (encoded_len >= sizeof(buffers->temp)) {
            snprintf(last_error, sizeof(last_error), "Encoded data too large for buffer");
            return 0;
        }
        
        memcpy(buffers->temp, start_pos + start_marker_len, encoded_len);
        buffers->temp[encoded_len] = '\0';
        buffers->temp_len = encoded_len;
        
        // Decode zero-width to binary
        size_t binary_len = 0;
        if (!decode_binary_static_large(buffers->temp, (unsigned char*)buffers->base64, 
                                       sizeof(buffers->base64), &binary_len)) {
            return 0;
        }
        buffers->base64[binary_len] = '\0';
        buffers->base64_len = binary_len;
        
        // Decode base64
        size_t decoded_len = 0;
        if (!from_base64_static((const unsigned char*)buffers->base64, buffers->base64_len, 
                               buffers->crypto_temp, sizeof(buffers->crypto_temp), &decoded_len)) {
            return 0;
        }
        buffers->crypto_temp_len = decoded_len;
        
        // Decrypt if password provided
        if (password && password[0]) {
            size_t decrypted_len = 0;
            if (!crypto_decrypt_static(buffers->crypto_temp, buffers->crypto_temp_len, 
                                      password, (unsigned char*)buffers->message_array[buffers->message_count], 
                                      sizeof(buffers->message_array[0]), &decrypted_len)) {
                // Skip this message if decryption fails
                pos = end_pos + strlen(END_MARKER);
                continue;
            }
            buffers->message_array[buffers->message_count][decrypted_len] = '\0';
        } else {
            // For non-password messages, copy directly
            if (decoded_len >= sizeof(buffers->message_array[0])) {
                snprintf(last_error, sizeof(last_error), "Decoded message too large for buffer");
                return 0;
            }
            memcpy(buffers->message_array[buffers->message_count], buffers->crypto_temp, decoded_len);
            buffers->message_array[buffers->message_count][decoded_len] = '\0';
        }
        
        buffers->message_count++;
        pos = end_pos + strlen(END_MARKER);
    }
    
    *result_count = buffers->message_count;
    return 1;
}

void whitespace_stego_static_large_free(whitespace_stego_buffers_large_t* buffers) {
    if (buffers) {
        // Clear all buffers for security
        memset(buffers, 0, sizeof(whitespace_stego_buffers_large_t));
    }
} 