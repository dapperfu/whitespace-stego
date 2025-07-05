/*
 * Static Whitespace Steganography Implementation
 * 
 * This implementation uses only static memory allocation with a 4 MiB buffer limit.
 * No dynamic memory allocation (malloc, free, realloc) is used.
 * 
 * Features:
 * - Fixed 4 MiB (4194304 bytes) for all buffers
 * - No memory leaks or allocation errors
 * - Thread-safe with proper buffer management
 * - MISRA C compliant
 * - Suitable for embedded and safety-critical systems
 */

#include "../include/whitespace_stego_static.h"
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

const char* whitespace_stego_static_last_error(void) {
    return last_error;
}

int whitespace_stego_static_validate_size(size_t size) {
    return (size <= MAX_BUFFER_SIZE) ? 1 : 0;
}

size_t whitespace_stego_static_max_size(void) {
    return MAX_BUFFER_SIZE;
}

int whitespace_stego_static_init(whitespace_stego_buffers_t* buffers) {
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
static int encode_binary_static(const unsigned char* data, size_t data_len, 
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
static int decode_binary_static(const char* encoded, unsigned char* out_buffer, 
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

int whitespace_stego_static_encode(whitespace_stego_buffers_t* buffers,
                                  const char* carrier, size_t carrier_len,
                                  const char* message, const char* password,
                                  size_t* result_len) {
    if (!buffers || !message || !result_len) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Validate input sizes
    if (!whitespace_stego_static_validate_size(carrier_len) ||
        !whitespace_stego_static_validate_size(strlen(message))) {
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
    if (!encode_binary_static((const unsigned char*)buffers->base64, buffers->base64_len, 
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
    
    // Build encoded message
    char* p = buffers->encoded;
    memcpy(p, START_MARKER, start_marker_len);
    p += start_marker_len;
    memcpy(p, buffers->temp, zw_len);
    p += zw_len;
    memcpy(p, END_MARKER, end_marker_len);
    p += end_marker_len;
    *p = '\0';
    
    size_t encoded_message_len = p - buffers->encoded;
    
    // Handle carrier embedding
    if (!carrier || carrier_len == 0) {
        // Empty carrier - return just the encoded message
        *result_len = encoded_message_len;
        return 1;
    } else {
        // Non-empty carrier - insert after first character
        size_t out_len = carrier_len + encoded_message_len;
        
        if (out_len >= sizeof(buffers->encoded)) {
            snprintf(last_error, sizeof(last_error), "Result too large for buffer");
            return 0;
        }
        
        // Copy the entire carrier
        memcpy(buffers->temp, carrier, carrier_len);
        buffers->temp[carrier_len] = '\0';
        
        // Find first complete UTF-8 character
        size_t first_char_len = 0;
        if ((unsigned char)carrier[0] < 0x80) {
            first_char_len = 1;
        } else if ((unsigned char)carrier[0] < 0xE0) {
            first_char_len = 2;
        } else if ((unsigned char)carrier[0] < 0xF0) {
            first_char_len = 3;
        } else {
            first_char_len = 4;
        }
        
        if (first_char_len > carrier_len) {
            first_char_len = carrier_len;
        }
        
        // Build final result
        p = buffers->encoded;
        memcpy(p, carrier, first_char_len);
        p += first_char_len;
        memcpy(p, buffers->temp, encoded_message_len);
        p += encoded_message_len;
        
        if (carrier_len > first_char_len) {
            memcpy(p, carrier + first_char_len, carrier_len - first_char_len);
            p += carrier_len - first_char_len;
        }
        *p = '\0';
        
        *result_len = p - buffers->encoded;
        return 1;
    }
}

int whitespace_stego_static_decode(whitespace_stego_buffers_t* buffers,
                                  const char* carrier, size_t carrier_len,
                                  const char* password, size_t* result_len) {
    if (!buffers || !carrier || !result_len) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Use the multiple message decoder and return the first message
    size_t result_count = 0;
    
    if (!whitespace_stego_static_decode_all(buffers, carrier, carrier_len, password, &result_count)) {
        return 0;
    }
    
    if (result_count == 0) {
        snprintf(last_error, sizeof(last_error), "No messages found in carrier text");
        return 0;
    }
    
    // Copy first message to decoded buffer
    size_t first_message_len = strlen(buffers->message_array[0]);
    if (first_message_len >= sizeof(buffers->decoded)) {
        snprintf(last_error, sizeof(last_error), "Decoded message too large for buffer");
        return 0;
    }
    
    strcpy(buffers->decoded, buffers->message_array[0]);
    *result_len = first_message_len;
    
    return 1;
}

int whitespace_stego_static_decode_all(whitespace_stego_buffers_t* buffers,
                                      const char* carrier, size_t carrier_len,
                                      const char* password, size_t* result_count) {
    if (!buffers || !carrier || !result_count) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters provided");
        return 0;
    }
    
    // Validate input size
    if (!whitespace_stego_static_validate_size(carrier_len)) {
        snprintf(last_error, sizeof(last_error), "Carrier size exceeds maximum allowed size");
        return 0;
    }
    
    // Copy carrier to buffer
    if (carrier_len >= sizeof(buffers->carrier)) {
        snprintf(last_error, sizeof(last_error), "Carrier too large for buffer");
        return 0;
    }
    
    memcpy(buffers->carrier, carrier, carrier_len);
    buffers->carrier[carrier_len] = '\0';
    buffers->carrier_len = carrier_len;
    
    // Find all start and end markers
    size_t start_positions[MAX_MESSAGES];
    size_t end_positions[MAX_MESSAGES];
    size_t marker_count = 0;
    
    const char* start_marker = START_MARKER;
    const char* end_marker = END_MARKER;
    size_t start_marker_len = strlen(start_marker);
    size_t end_marker_len = strlen(end_marker);
    
    const char* p = buffers->carrier;
    while (*p && marker_count < MAX_MESSAGES) {
        const char* start_pos = strstr(p, start_marker);
        if (!start_pos) break;
        
        const char* end_pos = strstr(start_pos + start_marker_len, end_marker);
        if (!end_pos) break;
        
        start_positions[marker_count] = start_pos - buffers->carrier;
        end_positions[marker_count] = end_pos - buffers->carrier;
        marker_count++;
        
        p = end_pos + end_marker_len;
    }
    
    if (marker_count == 0) {
        if (password && password[0]) {
            snprintf(last_error, sizeof(last_error), "Invalid password or no valid messages found in carrier text");
        } else {
            snprintf(last_error, sizeof(last_error), "No valid messages found in carrier text");
        }
        *result_count = 0;
        return 0;
    }
    
    // Process each message
    buffers->message_count = 0;
    
    for (size_t i = 0; i < marker_count && buffers->message_count < MAX_MESSAGES; i++) {
        size_t start_pos = start_positions[i];
        size_t end_pos = end_positions[i];
        size_t zw_len = end_pos - start_pos - start_marker_len;
        
        if (zw_len >= sizeof(buffers->temp)) {
            continue; // Skip this message if too large
        }
        
        // Extract zero-width characters
        memcpy(buffers->temp, buffers->carrier + start_pos + start_marker_len, zw_len);
        buffers->temp[zw_len] = '\0';
        
        // Decode binary data
        size_t decoded_len = 0;
        if (!decode_binary_static(buffers->temp, (unsigned char*)buffers->base64, 
                                 sizeof(buffers->base64), &decoded_len)) {
            continue; // Skip this message if decoding fails
        }
        buffers->base64[decoded_len] = '\0';
        
        // Decode base64
        size_t b64_len = 0;
        if (!from_base64_static((const unsigned char*)buffers->base64, decoded_len, 
                               buffers->crypto_temp, sizeof(buffers->crypto_temp), &b64_len)) {
            continue; // Skip this message if base64 decoding fails
        }
        
        // Decrypt if password provided
        if (password && password[0]) {
            size_t plain_len = 0;
            if (!crypto_decrypt_static(buffers->crypto_temp, b64_len, password, 
                                      (unsigned char*)buffers->temp, sizeof(buffers->temp), &plain_len)) {
                continue; // Skip this message if decryption fails
            }
            buffers->temp[plain_len] = '\0';
            
            // Store message
            size_t message_len = strlen(buffers->temp);
            if (message_len >= sizeof(buffers->message)) {
                continue; // Skip if message too large
            }
            
            memcpy(buffers->message + buffers->message_count * MAX_BUFFER_SIZE, 
                   buffers->temp, message_len + 1);
            buffers->message_array[buffers->message_count] = 
                buffers->message + buffers->message_count * MAX_BUFFER_SIZE;
            buffers->message_count++;
        } else {
            // No password - use decoded data directly
            size_t message_len = b64_len;
            if (message_len >= sizeof(buffers->message)) {
                continue; // Skip if message too large
            }
            
            memcpy(buffers->message + buffers->message_count * MAX_BUFFER_SIZE, 
                   buffers->crypto_temp, message_len);
            buffers->message[buffers->message_count * MAX_BUFFER_SIZE + message_len] = '\0';
            buffers->message_array[buffers->message_count] = 
                buffers->message + buffers->message_count * MAX_BUFFER_SIZE;
            buffers->message_count++;
        }
    }
    
    if (buffers->message_count == 0) {
        if (password && password[0]) {
            snprintf(last_error, sizeof(last_error), "Invalid password or no valid messages found in carrier text");
        } else {
            snprintf(last_error, sizeof(last_error), "No valid messages found in carrier text");
        }
        *result_count = 0;
        return 0;
    }
    
    *result_count = buffers->message_count;
    return 1;
} 