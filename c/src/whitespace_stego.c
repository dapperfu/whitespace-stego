#include "../include/whitespace_stego.h"
#include "../include/crypto.h"
#include "../include/utils.h"
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

// Zero-width Unicode characters (match Python core.py implementation)
#define START_MARKER "\xEF\xBB\xBF"   // U+FEFF Zero-width no-break space
#define END_MARKER   "\xE2\x80\x8C"   // U+200C Zero-width non-joiner
#define ZERO_BIT     "\xE2\x80\x8B"   // U+200B Zero-width space
#define ONE_BIT      "\xE2\x80\x8D"   // U+200D Zero-width joiner
#define BITS_PER_CHAR 8

static char last_error[256] = "";

const char* whitespace_stego_last_error(void) {
    return last_error;
}

// Helper: encode bytes to zero-width string
static char* encode_binary(const unsigned char* data, size_t data_len) {
    size_t out_len = data_len * BITS_PER_CHAR * strlen(ZERO_BIT); // Each bit is a multi-byte char
    char* out = malloc(out_len + 1);
    if (!out) return NULL;
    char* p = out;
    for (size_t i = 0; i < data_len; i++) {
        for (int bit = 7; bit >= 0; bit--) {
            if ((data[i] >> bit) & 1) {
                memcpy(p, ONE_BIT, strlen(ONE_BIT));
                p += strlen(ONE_BIT);
            } else {
                memcpy(p, ZERO_BIT, strlen(ZERO_BIT));
                p += strlen(ZERO_BIT);
            }
        }
    }
    *p = '\0';
    return out;
}

// Helper: decode zero-width string to bytes
static unsigned char* decode_binary(const char* encoded, size_t* out_len) {
    size_t encoded_len = strlen(encoded);
    size_t bit_char_len = strlen(ZERO_BIT); // All are 3 bytes except ONE_BIT (which is 3 bytes too)
    size_t bits = encoded_len / bit_char_len;
    size_t bytes = bits / 8;
    unsigned char* out = malloc(bytes + 1);
    if (!out) return NULL;
    size_t i = 0, j = 0;
    unsigned char byte = 0;
    int bit_count = 0;
    while (encoded[i]) {
        int is_one = (strncmp(&encoded[i], ONE_BIT, strlen(ONE_BIT)) == 0);
        int is_zero = (strncmp(&encoded[i], ZERO_BIT, strlen(ZERO_BIT)) == 0);
        if (!is_one && !is_zero) break;
        byte = (byte << 1) | (is_one ? 1 : 0);
        bit_count++;
        i += bit_char_len;
        if (bit_count == 8) {
            out[j++] = byte;
            byte = 0;
            bit_count = 0;
        }
    }
    *out_len = j;
    return out;
}

bool whitespace_stego_encode(const char* carrier, size_t carrier_len, const char* message,
                           const char* password, char** result) {
    if (!message || !result) {
        snprintf(last_error, sizeof(last_error), "No message or result pointer provided");
        return false;
    }
    
    // Check for empty message
    if (strlen(message) == 0) {
        snprintf(last_error, sizeof(last_error), "Empty message not allowed");
        return false;
    }
    unsigned char* data = NULL;
    size_t data_len = 0;
    char* b64 = NULL;

    // Encrypt if password
    if (password && password[0]) {
        if (!crypto_encrypt((const unsigned char*)message, strlen(message), password, &data, &data_len)) {
            return false;
        }
        // Base64 encode the Fernet token (same as Python/Rust)
        if (!to_base64(data, data_len, &b64)) {
            crypto_free(data);
            return false;
        }
        crypto_free(data);
    } else {
        if (!to_base64((const unsigned char*)message, strlen(message), &b64)) {
            return false;
        }
    }

    // Encode base64 string to zero-width
    char* zw = encode_binary((const unsigned char*)b64, strlen(b64));
    utils_free(b64);
    if (!zw) return false;

    // Compose final encoded message
    size_t zw_len = strlen(zw);
    size_t total_len = strlen(START_MARKER) + zw_len + strlen(END_MARKER) + 1;
    char* encoded_message = malloc(total_len);
    if (!encoded_message) { free(zw); return false; }
    strcpy(encoded_message, START_MARKER);
    strcat(encoded_message, zw);
    strcat(encoded_message, END_MARKER);
    free(zw);

    // Handle carrier embedding (match Python/Rust behavior)
    if (!carrier || carrier_len == 0) {
        // Empty carrier - return just the encoded message
        *result = encoded_message;
    } else {
        // Non-empty carrier - insert after first character
        size_t out_len = carrier_len + strlen(encoded_message) + 1;
        *result = malloc(out_len);
        if (!*result) { free(encoded_message); return false; }
        
        // Copy the entire carrier (it's already UTF-8 encoded)
        memcpy(*result, carrier, carrier_len);
        (*result)[carrier_len] = '\0';
        
        // Insert encoded message after the first character
        // For UTF-8, we need to find the first complete character
        size_t first_char_len = 0;
        if ((unsigned char)carrier[0] < 0x80) {
            // ASCII character - 1 byte
            first_char_len = 1;
        } else if ((unsigned char)carrier[0] < 0xE0) {
            // 2-byte UTF-8 sequence
            first_char_len = 2;
        } else if ((unsigned char)carrier[0] < 0xF0) {
            // 3-byte UTF-8 sequence
            first_char_len = 3;
        } else {
            // 4-byte UTF-8 sequence
            first_char_len = 4;
        }
        
        // Ensure we don't exceed carrier length
        if (first_char_len > carrier_len) {
            first_char_len = carrier_len;
        }
        
        // Create new result with encoded message inserted after first character
        size_t new_len = first_char_len + strlen(encoded_message) + (carrier_len - first_char_len) + 1;
        char* new_result = malloc(new_len);
        if (!new_result) { free(*result); free(encoded_message); return false; }
        
        // Copy first character
        memcpy(new_result, carrier, first_char_len);
        
        // Add encoded message
        strcpy(new_result + first_char_len, encoded_message);
        
        // Add rest of carrier
        if (carrier_len > first_char_len) {
            strcpy(new_result + first_char_len + strlen(encoded_message), carrier + first_char_len);
        }
        
        free(*result);
        free(encoded_message);
        *result = new_result;
    }
    return true;
}

bool whitespace_stego_decode(const char* carrier, size_t carrier_len, const char* password,
                           char** result) {
    if (!carrier || !result) {
        snprintf(last_error, sizeof(last_error), "No carrier or result pointer provided");
        return false;
    }
    
    // Use the multiple message decoder and return the first message
    char** results = NULL;
    size_t result_count = 0;
    
    if (!whitespace_stego_decode_all(carrier, carrier_len, password, &results, &result_count)) {
        return false;
    }
    
    if (result_count == 0) {
        snprintf(last_error, sizeof(last_error), "No valid messages found in carrier text");
        return false;
    }
    
    // Return the first message
    *result = results[0];
    
    // Free the array but keep the first message
    if (result_count > 1) {
        free(results);
    }
    
    return true;
}

bool whitespace_stego_decode_all(const char* carrier, size_t carrier_len, const char* password,
                                char*** results, size_t* result_count) {
    if (!carrier || !results || !result_count) {
        snprintf(last_error, sizeof(last_error), "No carrier or result pointers provided");
        return false;
    }
    
    // Create a null-terminated copy for string operations
    char* carrier_copy = malloc(carrier_len + 1);
    if (!carrier_copy) return false;
    memcpy(carrier_copy, carrier, carrier_len);
    carrier_copy[carrier_len] = '\0';
    
    // Find all start and end markers
    size_t* start_positions = NULL;
    size_t* end_positions = NULL;
    size_t start_count = 0;
    size_t end_count = 0;
    size_t max_markers = 1000; // Reasonable limit
    
    start_positions = malloc(max_markers * sizeof(size_t));
    end_positions = malloc(max_markers * sizeof(size_t));
    if (!start_positions || !end_positions) {
        free(carrier_copy);
        free(start_positions);
        free(end_positions);
        return false;
    }
    
    // Find all start markers
    const char* pos = carrier_copy;
    while ((pos = strstr(pos, START_MARKER)) != NULL) {
        if (start_count >= max_markers) break;
        start_positions[start_count++] = pos - carrier_copy;
        pos += strlen(START_MARKER);
    }
    
    // Find all end markers
    pos = carrier_copy;
    while ((pos = strstr(pos, END_MARKER)) != NULL) {
        if (end_count >= max_markers) break;
        end_positions[end_count++] = pos - carrier_copy;
        pos += strlen(END_MARKER);
    }
    
    // Allocate results array
    char** messages = malloc(max_markers * sizeof(char*));
    if (!messages) {
        free(carrier_copy);
        free(start_positions);
        free(end_positions);
        return false;
    }
    
    size_t message_count = 0;
    size_t start_idx = 0;
    size_t end_idx = 0;
    
    // Match start and end markers to extract messages
    while (start_idx < start_count && end_idx < end_count) {
        size_t start_pos = start_positions[start_idx];
        size_t end_pos = end_positions[end_idx];
        
        // Find the next valid pair (end after start)
        if (end_pos <= start_pos) {
            end_idx++;
            continue;
        }
        
        // Extract the encoded message
        size_t zw_len = end_pos - (start_pos + strlen(START_MARKER));
        char* zw = malloc(zw_len + 1);
        if (!zw) {
            // Cleanup and continue
            start_idx++;
            end_idx++;
            continue;
        }
        strncpy(zw, carrier_copy + start_pos + strlen(START_MARKER), zw_len);
        zw[zw_len] = '\0';
        
        // Decode zero-width to base64
        size_t b64_len = 0;
        unsigned char* b64_bytes = decode_binary(zw, &b64_len);
        free(zw);
        if (!b64_bytes) {
            start_idx++;
            end_idx++;
            continue;
        }
        
        // Convert base64 bytes to string
        char* b64_str = malloc(b64_len + 1);
        if (!b64_str) {
            free(b64_bytes);
            start_idx++;
            end_idx++;
            continue;
        }
        memcpy(b64_str, b64_bytes, b64_len);
        b64_str[b64_len] = '\0';
        free(b64_bytes);
        
        // Decrypt if password
        unsigned char* plain = NULL;
        size_t plain_len = 0;
        bool decrypt_success = true;
        
        if (password && password[0]) {
            unsigned char* encrypted = NULL;
            size_t encrypted_len = 0;
            if (!from_base64(b64_str, &encrypted, &encrypted_len)) {
                decrypt_success = false;
            } else if (!crypto_decrypt(encrypted, encrypted_len, password, &plain, &plain_len)) {
                decrypt_success = false;
                utils_free(encrypted);
            } else {
                utils_free(encrypted);
            }
        } else {
            if (!from_base64(b64_str, &plain, &plain_len)) {
                decrypt_success = false;
            }
        }
        
        free(b64_str);
        
        if (decrypt_success && plain) {
            // Copy to result as null-terminated string
            char* message = malloc(plain_len + 1);
            if (message) {
                memcpy(message, plain, plain_len);
                message[plain_len] = '\0';
                messages[message_count++] = message;
            }
            crypto_free(plain);
        }
        
        // Move to next pair
        start_idx++;
        end_idx++;
    }
    
    // Cleanup
    free(carrier_copy);
    free(start_positions);
    free(end_positions);
    
    if (message_count == 0) {
        free(messages);
        snprintf(last_error, sizeof(last_error), "No valid messages found in carrier text");
        return false;
    }
    
    // Resize the messages array to exact size
    char** final_messages = realloc(messages, message_count * sizeof(char*));
    if (!final_messages) {
        // Cleanup existing messages
        for (size_t i = 0; i < message_count; i++) {
            free(messages[i]);
        }
        free(messages);
        return false;
    }
    
    *results = final_messages;
    *result_count = message_count;
    return true;
}

void whitespace_stego_free(char* ptr) {
    if (ptr) {
        free(ptr);
    }
}

void whitespace_stego_free_all(char** results, size_t count) {
    if (results) {
        for (size_t i = 0; i < count; i++) {
            if (results[i]) {
                free(results[i]);
            }
        }
        free(results);
    }
} 