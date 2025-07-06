/*
 * Static C Implementation: whitespace_stego_static.c
 * This file provides a static version with pre-allocated buffers.
 * - Uses fixed-size buffers instead of dynamic memory allocation
 * - Suitable for embedded systems or environments without malloc
 * - 4MiB pre-allocated buffers for maximum message size
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

// Static buffer sizes (4MiB = 4194304 bytes)
#define STATIC_BUFFER_SIZE (4 * 1024 * 1024)
#define MAX_MESSAGE_SIZE (1024 * 1024)  // 1MB max message
#define MAX_CARRIER_SIZE (2 * 1024 * 1024)  // 2MB max carrier

static char last_error[256] = "";
static char static_buffer[STATIC_BUFFER_SIZE];
static char message_buffer[MAX_MESSAGE_SIZE];
static char carrier_buffer[MAX_CARRIER_SIZE];

// Helper function to clear static buffers
static void clear_static_buffers(void) {
    memset(static_buffer, 0, sizeof(static_buffer));
    memset(message_buffer, 0, sizeof(message_buffer));
    memset(carrier_buffer, 0, sizeof(carrier_buffer));
}

const char* whitespace_stego_static_last_error(void) {
    return last_error;
}

// Helper: encode bytes to zero-width string using static buffer
static int encode_binary_static(const unsigned char* data, size_t data_len, char* out_buffer, size_t buffer_size) {
    if (!data || !out_buffer || buffer_size == 0) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters for encode_binary_static");
        return 0;
    }
    
    size_t zero_bit_len = strlen(ZERO_BIT);
    size_t one_bit_len = strlen(ONE_BIT);
    size_t max_bit_len = (zero_bit_len > one_bit_len) ? zero_bit_len : one_bit_len;
    size_t required_len = data_len * BITS_PER_CHAR * max_bit_len;
    
    // Check if buffer is large enough
    if (required_len >= buffer_size) {
        snprintf(last_error, sizeof(last_error), "Buffer too small for encoding (need %zu, have %zu)", required_len, buffer_size);
        return 0;
    }
    
    char* p = out_buffer;
    size_t remaining_space = buffer_size;
    
    for (size_t i = 0; i < data_len; i++) {
        for (int bit = 7; bit >= 0; bit--) {
            if ((data[i] >> bit) & 1) {
                if (remaining_space < one_bit_len) {
                    snprintf(last_error, sizeof(last_error), "Buffer overflow prevented");
                    return 0;
                }
                memcpy(p, ONE_BIT, one_bit_len);
                p += one_bit_len;
                remaining_space -= one_bit_len;
            } else {
                if (remaining_space < zero_bit_len) {
                    snprintf(last_error, sizeof(last_error), "Buffer overflow prevented");
                    return 0;
                }
                memcpy(p, ZERO_BIT, zero_bit_len);
                p += zero_bit_len;
                remaining_space -= zero_bit_len;
            }
        }
    }
    *p = '\0';
    return 1;
}

// Helper: decode zero-width string to bytes using static buffer
static int decode_binary_static(const char* encoded, unsigned char* out_buffer, size_t buffer_size, size_t* out_len) {
    if (!encoded || !out_buffer || !out_len || buffer_size == 0) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters for decode_binary_static");
        return 0;
    }
    
    size_t encoded_len = strlen(encoded);
    size_t zero_bit_len = strlen(ZERO_BIT);
    size_t one_bit_len = strlen(ONE_BIT);
    
    // Calculate expected bytes: each byte is 8 bits, each bit is a 3-byte UTF-8 character
    size_t bits = encoded_len / 3; // Each bit character is 3 bytes
    size_t bytes = bits / 8;
    
    // Check if buffer is large enough
    if (bytes >= buffer_size) {
        snprintf(last_error, sizeof(last_error), "Buffer too small for decoding (need %zu, have %zu)", bytes, buffer_size);
        return 0;
    }
    
    size_t i = 0, j = 0;
    unsigned char byte = 0;
    int bit_count = 0;
    
    while (i < encoded_len && j < bytes) {
        // Check bounds before accessing
        if (i + 2 >= encoded_len) {
            break; // Incomplete UTF-8 sequence at end
        }
        
        int is_one = (strncmp(&encoded[i], ONE_BIT, one_bit_len) == 0);
        int is_zero = (strncmp(&encoded[i], ZERO_BIT, zero_bit_len) == 0);
        
        if (!is_one && !is_zero) {
            break; // Invalid character sequence
        }
        
        byte = (byte << 1) | (is_one ? 1 : 0);
        bit_count++;
        i += 3; // Each bit character is 3 bytes
        
        if (bit_count == 8) {
            out_buffer[j++] = byte;
            byte = 0;
            bit_count = 0;
        }
    }
    
    // Handle incomplete byte at end
    if (bit_count > 0 && bit_count < 8) {
        // Pad with zeros for incomplete byte
        while (bit_count < 8) {
            byte = (byte << 1) | 0;
            bit_count++;
        }
        if (j < bytes) {
            out_buffer[j++] = byte;
        }
    }
    
    *out_len = j;
    return 1;
}

int whitespace_stego_static_encode(const char* carrier, size_t carrier_len, const char* message,
                                  const char* password, char* result, size_t result_size) {
    // Clear static buffers to prevent contamination
    clear_static_buffers();
    
    if (!carrier || !message || !result || result_size == 0) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters for static encode");
        return 0;
    }
    
    // Check for empty message
    if (strlen(message) == 0) {
        snprintf(last_error, sizeof(last_error), "Empty message not allowed");
        return 0;
    }
    
    // Check message size
    if (strlen(message) >= MAX_MESSAGE_SIZE) {
        snprintf(last_error, sizeof(last_error), "Message too large for static implementation");
        return 0;
    }
    
    unsigned char* data = NULL;
    size_t data_len = 0;
    char* b64 = NULL;

    // Encrypt if password
    if (password && password[0]) {
        // Encrypt the original message first
        if (!crypto_encrypt((const unsigned char*)message, strlen(message), password, &data, &data_len)) {
            return 0;
        }
        // Base64 encode the encrypted data to convert random bytes to safe ASCII
        if (!to_base64(data, data_len, &b64)) {
            crypto_free(data);
            return 0;
        }
        crypto_free(data);
    } else {
        // For non-password messages, base64 encode the original message
        if (!to_base64((const unsigned char*)message, strlen(message), &b64)) {
            return 0;
        }
    }

    // Encode base64 string to zero-width using static buffer
    if (!encode_binary_static((const unsigned char*)b64, strlen(b64), static_buffer, sizeof(static_buffer))) {
        utils_free(b64);
        return 0;
    }
    utils_free(b64);

    // Compose final encoded message
    size_t zw_len = strlen(static_buffer);
    size_t encoded_message_len = strlen(START_MARKER) + zw_len + strlen(END_MARKER);
    
    // Handle carrier embedding
    if (!carrier || carrier_len == 0) {
        // Empty carrier - return just the encoded message
        if (encoded_message_len + 1 >= result_size) {
            snprintf(last_error, sizeof(last_error), "Result buffer too small (need %zu, have %zu)", 
                    encoded_message_len + 1, result_size);
            return 0;
        }
        
        strcpy(result, START_MARKER);
        strcat(result, static_buffer);
        strcat(result, END_MARKER);
    } else {
        // Non-empty carrier - insert after first character
        size_t out_len = carrier_len + encoded_message_len;
        
        if (out_len + 1 >= result_size) {
            snprintf(last_error, sizeof(last_error), "Result buffer too small (need %zu, have %zu)", 
                    out_len + 1, result_size);
            return 0;
        }
        
        // Copy the entire carrier
        memcpy(result, carrier, carrier_len);
        result[carrier_len] = '\0';
        
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
        
        // Build final result by inserting encoded message after first character
        char* p = result + first_char_len;
        memcpy(p, START_MARKER, strlen(START_MARKER));
        p += strlen(START_MARKER);
        memcpy(p, static_buffer, zw_len);
        p += zw_len;
        memcpy(p, END_MARKER, strlen(END_MARKER));
        p += strlen(END_MARKER);
        
        if (carrier_len > first_char_len) {
            memcpy(p, carrier + first_char_len, carrier_len - first_char_len);
            p += carrier_len - first_char_len;
        }
        *p = '\0';
    }
    
    return 1;
}

int whitespace_stego_static_decode(const char* carrier, size_t carrier_len, const char* password,
                                  char* result, size_t result_size) {
    // Clear static buffers to prevent contamination
    clear_static_buffers();
    
    printf("[DEBUG] decode: carrier_len=%zu, result_size=%zu\n", carrier_len, result_size);
    if (!carrier || !result || result_size == 0) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters for static decode");
        printf("[DEBUG] decode: invalid parameters\n");
        return 0;
    }
    
    // Find start marker
    const char* start_pos = strstr(carrier, START_MARKER);
    if (!start_pos) {
        snprintf(last_error, sizeof(last_error), "Start marker not found");
        printf("[DEBUG] decode: start marker not found\n");
        return 0;
    }
    
    // Find end marker
    const char* end_pos = strstr(start_pos + strlen(START_MARKER), END_MARKER);
    if (!end_pos) {
        snprintf(last_error, sizeof(last_error), "End marker not found");
        printf("[DEBUG] decode: end marker not found\n");
        return 0;
    }
    
    // Extract zero-width encoded data
    size_t zw_start = start_pos + strlen(START_MARKER) - carrier;
    size_t zw_end = end_pos - carrier;
    size_t zw_len = zw_end - zw_start;
    printf("[DEBUG] decode: zw_start=%zu, zw_end=%zu, zw_len=%zu\n", zw_start, zw_end, zw_len);
    
    if (zw_len >= sizeof(static_buffer)) {
        snprintf(last_error, sizeof(last_error), "Zero-width data too large for static buffer");
        printf("[DEBUG] decode: zero-width data too large\n");
        return 0;
    }
    
    // Copy zero-width data to static buffer
    memcpy(static_buffer, carrier + zw_start, zw_len);
    static_buffer[zw_len] = '\0';
    
    // Decode zero-width to binary
    unsigned char* decoded_data = (unsigned char*)message_buffer;
    size_t decoded_len = 0;
    if (!decode_binary_static(static_buffer, decoded_data, sizeof(message_buffer), &decoded_len)) {
        printf("[DEBUG] decode: decode_binary_static failed\n");
        return 0;
    }
    printf("[DEBUG] decode: decoded_len=%zu\n", decoded_len);
    
    // Base64 decode
    char* b64_decoded = NULL;
    size_t b64_len = 0;
    if (!from_base64((const char*)decoded_data, (unsigned char**)&b64_decoded, &b64_len)) {
        snprintf(last_error, sizeof(last_error), "Base64 decode failed");
        printf("[DEBUG] decode: base64 decode failed\n");
        return 0;
    }
    printf("[DEBUG] decode: b64_len=%zu\n", b64_len);
    
    // Decrypt if password provided
    if (password && password[0]) {
        unsigned char* decrypted_data = NULL;
        size_t decrypted_len = 0;
        if (!crypto_decrypt((const unsigned char*)b64_decoded, b64_len, password, &decrypted_data, &decrypted_len)) {
            utils_free(b64_decoded);
            printf("[DEBUG] decode: crypto_decrypt failed\n");
            return 0;
        }
        printf("[DEBUG] decode: decrypted_len=%zu\n", decrypted_len);
        if (decrypted_len >= result_size) {
            crypto_free(decrypted_data);
            utils_free(b64_decoded);
            snprintf(last_error, sizeof(last_error), "Result buffer too small for decrypted message");
            printf("[DEBUG] decode: result buffer too small for decrypted message\n");
            return 0;
        }
        memcpy(result, decrypted_data, decrypted_len);
        result[decrypted_len] = '\0';
        crypto_free(decrypted_data);
    } else {
        // No password, use base64 decoded data directly
        if (b64_len >= result_size) {
            utils_free(b64_decoded);
            snprintf(last_error, sizeof(last_error), "Result buffer too small for decoded message");
            printf("[DEBUG] decode: result buffer too small for decoded message\n");
            return 0;
        }
        memcpy(result, b64_decoded, b64_len);
        result[b64_len] = '\0';
    }
    printf("[DEBUG] decode: final result length=%zu\n", strlen(result));
    utils_free(b64_decoded);
    return 1;
}

int whitespace_stego_static_decode_all(const char* carrier, size_t carrier_len, const char* password,
                                       char* results[], size_t max_results, size_t* result_count) {
    if (!carrier || !results || !result_count || max_results == 0) {
        snprintf(last_error, sizeof(last_error), "Invalid parameters for static decode_all");
        return 0;
    }
    
    *result_count = 0;
    
    const char* pos = carrier;
    const char* end = carrier + carrier_len;
    
    while (pos < end && *result_count < max_results) {
        // Find start marker
        const char* start_pos = strstr(pos, START_MARKER);
        if (!start_pos) {
            break; // No more messages
        }
        
        // Find end marker
        const char* end_pos = strstr(start_pos + strlen(START_MARKER), END_MARKER);
        if (!end_pos) {
            break; // Incomplete message
        }
        
        // Extract message
        size_t message_start = start_pos - carrier;
        size_t message_end = end_pos + strlen(END_MARKER) - carrier;
        size_t message_len = message_end - message_start;
        
        if (message_len >= sizeof(carrier_buffer)) {
            snprintf(last_error, sizeof(last_error), "Message too large for static buffer");
            return 0;
        }
        
        // Copy message to carrier buffer
        memcpy(carrier_buffer, carrier + message_start, message_len);
        carrier_buffer[message_len] = '\0';
        
        // Decode this message
        if (whitespace_stego_static_decode(carrier_buffer, message_len, password, 
                                         results[*result_count], MAX_MESSAGE_SIZE)) {
            (*result_count)++;
        }
        
        // Move to next potential message
        pos = end_pos + strlen(END_MARKER);
    }
    
    return 1;
} 