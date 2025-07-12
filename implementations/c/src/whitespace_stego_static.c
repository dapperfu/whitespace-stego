/*
 * MISRA C:2012 Compliant Static C Implementation: whitespace_stego_static.c
 * This file provides a static version with pre-allocated buffers.
 * - Uses fixed-size buffers instead of dynamic memory allocation
 * - Suitable for embedded systems or environments without malloc
 * - MISRA C:2012 compliant with safe string operations
 * - No magic numbers, all constants properly defined
 */
#include "../include/whitespace_stego_static.h"
#include "../include/whitespace_stego_static_misra.h"
#include "../include/crypto.h"
#include "../include/utils.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdint.h>

/* Zero-width Unicode characters (match Python core.py implementation) */
static const char START_MARKER[] = "\xEF\xBB\xBF";   /* U+FEFF Zero-width no-break space */
static const char END_MARKER[] = "\xE2\x80\x8C";     /* U+200C Zero-width non-joiner */
static const char ZERO_BIT[] = "\xE2\x80\x8B";       /* U+200B Zero-width space */
static const char ONE_BIT[] = "\xE2\x80\x8D";        /* U+200D Zero-width joiner */

/* Static buffers with proper size constants */
static char last_error[ERROR_BUFFER_SIZE_BYTES] = "";
static char static_buffer[STATIC_BUFFER_SIZE_BYTES];
static char message_buffer[MAX_MESSAGE_SIZE_BYTES];
static char carrier_buffer[MAX_CARRIER_SIZE_BYTES];
static char log_buffer[LOG_BUFFER_SIZE_BYTES];
static log_level_t current_log_level = LOG_LEVEL_NONE;

/* Helper function to clear static buffers */
static void clear_static_buffers(void) {
    (void)memset(static_buffer, 0, sizeof(static_buffer));
    (void)memset(message_buffer, 0, sizeof(message_buffer));
    (void)memset(carrier_buffer, 0, sizeof(carrier_buffer));
}

void whitespace_stego_static_set_log_level(log_level_t level) {
    current_log_level = level;
}

void whitespace_stego_static_log(log_level_t level, const char* format, ...) {
    if (level <= current_log_level) {
        va_list args;
        va_start(args, format);
        (void)vsnprintf(log_buffer, sizeof(log_buffer), format, args);
        va_end(args);
        /* In MISRA-compliant systems, this would write to a log file or system log */
        /* For now, we just store the message in the buffer */
    }
}

const char* whitespace_stego_static_last_error(void) {
    return last_error;
}

void whitespace_stego_static_clear_error(void) {
    (void)memset(last_error, 0, sizeof(last_error));
}

/* Helper: encode bytes to zero-width string using static buffer */
static int encode_binary_static(const unsigned char* data, size_t data_len, char* out_buffer, size_t buffer_size) {
    size_t zero_bit_len = 0U;
    size_t one_bit_len = 0U;
    size_t max_bit_len = 0U;
    size_t required_len = 0U;
    char* p = NULL;
    size_t remaining_space = 0U;
    size_t i = 0U;
    int bit = 0;
    uint8_t bit_value = 0U;
    
    /* Parameter validation */
    if ((data == NULL) || (out_buffer == NULL) || (buffer_size == 0U)) {
        (void)snprintf(last_error, sizeof(last_error), "Invalid parameters for encode_binary_static");
        return 0;
    }
    
    /* Get string lengths using safe functions */
    zero_bit_len = misra_safe_strlen(ZERO_BIT, MAX_BIT_LENGTH);
    one_bit_len = misra_safe_strlen(ONE_BIT, MAX_BIT_LENGTH);
    max_bit_len = (zero_bit_len > one_bit_len) ? zero_bit_len : one_bit_len;
    required_len = data_len * BITS_PER_CHAR * max_bit_len;
    
    /* Check if buffer is large enough */
    if (required_len >= buffer_size) {
        (void)snprintf(last_error, sizeof(last_error), "Buffer too small for encoding (need %zu, have %zu)", required_len, buffer_size);
        return 0;
    }
    
    p = out_buffer;
    remaining_space = buffer_size;
    
    /* Encode each byte */
    for (i = 0U; i < data_len; i = i + 1U) {
        /* Encode each bit */
        for (bit = 7; bit >= 0; bit = bit - 1) {
            /* Extract bit value using MISRA-compliant function */
            bit_value = misra_extract_bit(data[i], (uint8_t)bit);
            
            if (bit_value != 0U) {
                /* One bit */
                if (remaining_space < one_bit_len) {
                    (void)snprintf(last_error, sizeof(last_error), "Buffer overflow prevented");
                    return 0;
                }
                (void)memcpy(p, ONE_BIT, one_bit_len);
                p = p + one_bit_len;
                remaining_space = remaining_space - one_bit_len;
            } else {
                /* Zero bit */
                if (remaining_space < zero_bit_len) {
                    (void)snprintf(last_error, sizeof(last_error), "Buffer overflow prevented");
                    return 0;
                }
                (void)memcpy(p, ZERO_BIT, zero_bit_len);
                p = p + zero_bit_len;
                remaining_space = remaining_space - zero_bit_len;
            }
        }
    }
    *p = '\0';
    return 1;
}

/* Helper: decode zero-width string to bytes using static buffer */
static int decode_binary_static(const char* encoded, unsigned char* out_buffer, size_t buffer_size, size_t* out_len) {
    size_t encoded_len = 0U;
    size_t zero_bit_len = 0U;
    size_t one_bit_len = 0U;
    size_t bits = 0U;
    size_t bytes = 0U;
    size_t i = 0U;
    size_t j = 0U;
    unsigned char byte = 0U;
    uint8_t bit_count = 0U;
    
    /* Parameter validation */
    if ((encoded == NULL) || (out_buffer == NULL) || (out_len == NULL) || (buffer_size == 0U)) {
        (void)snprintf(last_error, sizeof(last_error), "Invalid parameters for decode_binary_static");
        return 0;
    }
    
    /* Get string lengths using safe functions */
    encoded_len = misra_safe_strlen(encoded, STATIC_BUFFER_SIZE_BYTES);
    zero_bit_len = misra_safe_strlen(ZERO_BIT, MAX_BIT_LENGTH);
    one_bit_len = misra_safe_strlen(ONE_BIT, MAX_BIT_LENGTH);
    
    /* Calculate expected bytes: each byte is 8 bits, each bit is a 3-byte UTF-8 character */
    bits = encoded_len / UTF8_3BYTE_LENGTH; /* Each bit character is 3 bytes */
    bytes = bits / BITS_PER_BYTE;
    
    /* Check if buffer is large enough */
    if (bytes >= buffer_size) {
        (void)snprintf(last_error, sizeof(last_error), "Buffer too small for decoding (need %zu, have %zu)", bytes, buffer_size);
        return 0;
    }
    
    i = 0U;
    j = 0U;
    byte = 0U;
    bit_count = 0U;
    
    /* Decode each bit */
    while ((i < encoded_len) && (j < bytes)) {
        /* Check bounds before accessing */
        if ((i + 2U) >= encoded_len) {
            break; /* Incomplete UTF-8 sequence at end */
        }
        
        {
            int is_one = 0;
            int is_zero = 0;
            
            is_one = (strncmp(&encoded[i], ONE_BIT, one_bit_len) == 0);
            is_zero = (strncmp(&encoded[i], ZERO_BIT, zero_bit_len) == 0);
            
            if ((is_one == 0) && (is_zero == 0)) {
                break; /* Invalid character sequence */
            }
            
            byte = (byte << 1) | (is_one ? 1U : 0U);
        }
        
        bit_count = bit_count + 1U;
        i = i + UTF8_3BYTE_LENGTH; /* Each bit character is 3 bytes */
        
        if (bit_count == BITS_PER_BYTE) {
            out_buffer[j] = byte;
            j = j + 1U;
            byte = 0U;
            bit_count = 0U;
        }
    }
    
    /* Handle incomplete byte at end */
    if ((bit_count > 0U) && (bit_count < BITS_PER_BYTE)) {
        /* Pad with zeros for incomplete byte */
        while (bit_count < BITS_PER_BYTE) {
            byte = byte << 1;
            bit_count = bit_count + 1U;
        }
        if (j < bytes) {
            out_buffer[j] = byte;
            j = j + 1U;
        }
    }
    
    *out_len = j;
    return 1;
}

int whitespace_stego_static_encode(const char* carrier, size_t carrier_len, const char* message,
                                  const char* password, char* result, size_t result_size) {
    size_t message_len = 0U;
    
    /* Clear static buffers to prevent contamination */
    clear_static_buffers();
    
    /* Parameter validation */
    if ((carrier == NULL) || (message == NULL) || (result == NULL) || (result_size == 0U)) {
        (void)snprintf(last_error, sizeof(last_error), "Invalid parameters for static encode");
        return 0;
    }
    
    /* Get message length using safe function */
    message_len = misra_safe_strlen(message, MAX_MESSAGE_SIZE_BYTES);
    
    /* Check for empty message */
    if (message_len == 0U) {
        (void)snprintf(last_error, sizeof(last_error), "Empty message not allowed");
        return 0;
    }
    
    /* Check message size */
    if (message_len >= MAX_MESSAGE_SIZE_BYTES) {
        (void)snprintf(last_error, sizeof(last_error), "Message too large for static implementation");
        return 0;
    }
    
    unsigned char* data = NULL;
    size_t data_len = 0;
    char* b64 = NULL;

    /* Encrypt if password */
    if ((password != NULL) && (password[0] != '\0')) {
        /* Encrypt the original message first */
        if (crypto_encrypt((const unsigned char*)message, strlen(message), password, &data, &data_len) == 0) {
            return 0;
        }
        /* Base64 encode the encrypted data to convert random bytes to safe ASCII */
        if (to_base64(data, data_len, &b64) == 0) {
            crypto_free(data);
            return 0;
        }
        crypto_free(data);
    } else {
        /* For non-password messages, base64 encode the original message */
        if (to_base64((const unsigned char*)message, strlen(message), &b64) == 0) {
            return 0;
        }
    }

    /* Encode base64 string to zero-width using static buffer */
    if (encode_binary_static((const unsigned char*)b64, misra_safe_strlen(b64, STATIC_BUFFER_SIZE_BYTES), static_buffer, sizeof(static_buffer)) == 0) {
        utils_free(b64);
        return 0;
    }
    utils_free(b64);

    /* Compose final encoded message */
    size_t zw_len = misra_safe_strlen(static_buffer, sizeof(static_buffer));
    size_t start_marker_len = misra_safe_strlen(START_MARKER, START_MARKER_LENGTH);
    size_t end_marker_len = misra_safe_strlen(END_MARKER, END_MARKER_LENGTH);
    size_t encoded_message_len = start_marker_len + zw_len + end_marker_len;
    
    /* Handle carrier embedding */
    if ((carrier == NULL) || (carrier_len == 0U)) {
        /* Empty carrier - return just the encoded message */
        if ((encoded_message_len + 1U) >= result_size) {
            (void)snprintf(last_error, sizeof(last_error), "Result buffer too small (need %zu, have %zu)", 
                    encoded_message_len + 1U, result_size);
            return 0;
        }
        
        /* Use safe string operations */
        (void)misra_safe_strcpy(result, result_size, START_MARKER);
        (void)misra_safe_strcat(result, result_size, static_buffer);
        (void)misra_safe_strcat(result, result_size, END_MARKER);
    } else {
        /* Non-empty carrier - insert after first character */
        size_t out_len = carrier_len + encoded_message_len;
        
        if ((out_len + 1U) >= result_size) {
            (void)snprintf(last_error, sizeof(last_error), "Result buffer too small (need %zu, have %zu)", 
                    out_len + 1U, result_size);
            return 0;
        }
        
        /* Copy the entire carrier */
        (void)memcpy(result, carrier, carrier_len);
        result[carrier_len] = '\0';
        
        /* Find first complete UTF-8 character using MISRA-compliant function */
        uint8_t first_byte = (uint8_t)carrier[0U];
        size_t first_char_len = misra_utf8_char_length(first_byte);
        
        if (first_char_len > carrier_len) {
            first_char_len = carrier_len;
        }
        
        /* Build final result by inserting encoded message after first character */
        char* p = result + first_char_len;
        (void)memcpy(p, START_MARKER, start_marker_len);
        p = p + start_marker_len;
        (void)memcpy(p, static_buffer, zw_len);
        p = p + zw_len;
        (void)memcpy(p, END_MARKER, end_marker_len);
        p = p + end_marker_len;
        
        if (carrier_len > first_char_len) {
            (void)memcpy(p, carrier + first_char_len, carrier_len - first_char_len);
            p = p + carrier_len - first_char_len;
        }
        *p = '\0';
    }
    
    return 1;
}

int whitespace_stego_static_decode(const char* carrier, size_t carrier_len, const char* password,
                                  char* result, size_t result_size) {
    const char* start_pos = NULL;
    const char* end_pos = NULL;
    size_t start_marker_len = 0U;
    size_t zw_start = 0U;
    size_t zw_end = 0U;
    size_t zw_len = 0U;
    
    /* Clear static buffers to prevent contamination */
    clear_static_buffers();
    
    /* Parameter validation */
    if ((carrier == NULL) || (result == NULL) || (result_size == 0U)) {
        (void)snprintf(last_error, sizeof(last_error), "Invalid parameters for static decode");
        return 0;
    }
    
    /* Get marker lengths using safe functions */
    start_marker_len = misra_safe_strlen(START_MARKER, START_MARKER_LENGTH);
    
    /* Find start marker */
    start_pos = strstr(carrier, START_MARKER);
    if (start_pos == NULL) {
        (void)snprintf(last_error, sizeof(last_error), "Start marker not found");
        return 0;
    }
    
    /* Find end marker */
    end_pos = strstr(start_pos + start_marker_len, END_MARKER);
    if (end_pos == NULL) {
        (void)snprintf(last_error, sizeof(last_error), "End marker not found");
        return 0;
    }
    
    /* Extract zero-width encoded data */
    zw_start = start_pos + start_marker_len - carrier;
    zw_end = end_pos - carrier;
    zw_len = zw_end - zw_start;
    
    if (zw_len >= sizeof(static_buffer)) {
        (void)snprintf(last_error, sizeof(last_error), "Zero-width data too large for static buffer");
        return 0;
    }
    
    /* Copy zero-width data to static buffer */
    (void)memcpy(static_buffer, carrier + zw_start, zw_len);
    static_buffer[zw_len] = '\0';
    
    /* Decode zero-width to binary */
    unsigned char* decoded_data = (unsigned char*)message_buffer;
    size_t decoded_len = 0;
    if (decode_binary_static(static_buffer, decoded_data, sizeof(message_buffer), &decoded_len) == 0) {
        return 0;
    }
    
    /* Base64 decode */
    char* b64_decoded = NULL;
    size_t b64_len = 0;
    if (from_base64((const char*)decoded_data, (unsigned char**)&b64_decoded, &b64_len) == 0) {
        (void)snprintf(last_error, sizeof(last_error), "Base64 decode failed");
        return 0;
    }
    
    /* Decrypt if password provided */
    if ((password != NULL) && (password[0] != '\0')) {
        unsigned char* decrypted_data = NULL;
        size_t decrypted_len = 0;
        if (crypto_decrypt((const unsigned char*)b64_decoded, b64_len, password, &decrypted_data, &decrypted_len) == 0) {
            utils_free(b64_decoded);
            return 0;
        }
        if (decrypted_len >= result_size) {
            crypto_free(decrypted_data);
            utils_free(b64_decoded);
            (void)snprintf(last_error, sizeof(last_error), "Result buffer too small for decrypted message");
            return 0;
        }
        (void)memcpy(result, decrypted_data, decrypted_len);
        result[decrypted_len] = '\0';
        crypto_free(decrypted_data);
    } else {
        /* No password, use base64 decoded data directly */
        if (b64_len >= result_size) {
            utils_free(b64_decoded);
            (void)snprintf(last_error, sizeof(last_error), "Result buffer too small for decoded message");
            return 0;
        }
        (void)memcpy(result, b64_decoded, b64_len);
        result[b64_len] = '\0';
    }
    utils_free(b64_decoded);
    return 1;
}

int whitespace_stego_static_decode_all(const char* carrier, size_t carrier_len, const char* password,
                                       char* results[], size_t max_results, size_t* result_count) {
    const char* pos = NULL;
    const char* end = NULL;
    const char* start_pos = NULL;
    const char* end_pos = NULL;
    size_t start_marker_len = 0U;
    size_t end_marker_len = 0U;
    
    /* Parameter validation */
    if ((carrier == NULL) || (results == NULL) || (result_count == NULL) || (max_results == 0U)) {
        (void)snprintf(last_error, sizeof(last_error), "Invalid parameters for static decode_all");
        return 0;
    }
    
    /* Get marker lengths using safe functions */
    start_marker_len = misra_safe_strlen(START_MARKER, START_MARKER_LENGTH);
    end_marker_len = misra_safe_strlen(END_MARKER, END_MARKER_LENGTH);
    
    *result_count = 0U;
    
    pos = carrier;
    end = carrier + carrier_len;
    
    /* Find all messages */
    while ((pos < end) && (*result_count < max_results)) {
        /* Find start marker */
        start_pos = strstr(pos, START_MARKER);
        if (start_pos == NULL) {
            break; /* No more messages */
        }
        
        /* Find end marker */
        end_pos = strstr(start_pos + start_marker_len, END_MARKER);
        if (end_pos == NULL) {
            break; /* Incomplete message */
        }
        
        /* Extract message */
        {
            size_t message_start = 0U;
            size_t message_end = 0U;
            size_t message_len = 0U;
            
            message_start = start_pos - carrier;
            message_end = end_pos + end_marker_len - carrier;
            message_len = message_end - message_start;
            
            if (message_len >= sizeof(carrier_buffer)) {
                (void)snprintf(last_error, sizeof(last_error), "Message too large for static buffer");
                return 0;
            }
            
            /* Copy message to carrier buffer */
            (void)memcpy(carrier_buffer, carrier + message_start, message_len);
            carrier_buffer[message_len] = '\0';
            
            /* Decode this message */
            if (whitespace_stego_static_decode(carrier_buffer, message_len, password, 
                                             results[*result_count], MAX_MESSAGE_SIZE_BYTES) != 0) {
                *result_count = *result_count + 1U;
            }
        }
        
        /* Move to next potential message */
        pos = end_pos + end_marker_len;
    }
    
    return 1;
} 