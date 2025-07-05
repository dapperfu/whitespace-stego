/*
 * Static Whitespace Steganography Implementation
 * 
 * This implementation uses only static memory allocation with a 2^32 character limit.
 * No dynamic memory allocation (malloc, free, realloc) is used.
 * 
 * Features:
 * - Maximum 4 GiB (2^32 bytes) for any single buffer
 * - No memory leaks or allocation errors
 * - Thread-safe with proper buffer management
 * - MISRA C compliant
 * - Suitable for embedded and safety-critical systems
 */

#ifndef WHITESPACE_STEGO_STATIC_H
#define WHITESPACE_STEGO_STATIC_H

#include <stddef.h>
#include <stdint.h>

/* Include auto-generated buffer size configuration */
#include "../config/buffer_sizes.h"

/* Maximum buffer size: Use configured standard size to avoid stack overflow */
#define MAX_BUFFER_SIZE STANDARD_BUFFER_SIZE

/* Maximum number of messages that can be decoded at once */
#define MAX_MESSAGES 1000

/* Buffer configuration */
typedef struct {
    char carrier[MAX_BUFFER_SIZE];
    char message[MAX_BUFFER_SIZE];  /* Single message buffer for standard static */
    char encoded[MAX_BUFFER_SIZE];
    char decoded[MAX_BUFFER_SIZE];
    char temp[MAX_BUFFER_SIZE];
    char base64[MAX_BUFFER_SIZE];
    unsigned char crypto_temp[MAX_BUFFER_SIZE];  /* Use unsigned char for crypto operations */
    char* message_array[MAX_MESSAGES];
    size_t carrier_len;
    size_t message_len;
    size_t encoded_len;
    size_t decoded_len;
    size_t temp_len;
    size_t base64_len;
    size_t crypto_temp_len;
    size_t message_count;
} whitespace_stego_buffers_t;

/**
 * @brief Initialize static buffers for whitespace steganography operations
 *
 * @param buffers Pointer to buffer structure to initialize
 * @return 1 if initialization was successful, 0 otherwise
 */
int whitespace_stego_static_init(whitespace_stego_buffers_t* buffers);

/**
 * @brief Encode a message into carrier text using static buffers
 *
 * @param buffers Pre-allocated buffer structure
 * @param carrier The carrier text to encode into
 * @param carrier_len Length of the carrier text in bytes
 * @param message The message to encode
 * @param password Optional password for encryption (NULL if not used)
 * @param result_len Pointer to store the length of the encoded result
 * @return 1 if encoding was successful, 0 otherwise
 * 
 * Note: The encoded result is stored in buffers->encoded
 */
int whitespace_stego_static_encode(whitespace_stego_buffers_t* buffers,
                                  const char* carrier, size_t carrier_len,
                                  const char* message, const char* password,
                                  size_t* result_len);

/**
 * @brief Decode a message from carrier text using static buffers
 *
 * @param buffers Pre-allocated buffer structure
 * @param carrier The carrier text containing the encoded message
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param result_len Pointer to store the length of the decoded result
 * @return 1 if decoding was successful, 0 otherwise
 * 
 * Note: The decoded result is stored in buffers->decoded
 */
int whitespace_stego_static_decode(whitespace_stego_buffers_t* buffers,
                                  const char* carrier, size_t carrier_len,
                                  const char* password, size_t* result_len);

/**
 * @brief Decode all messages from carrier text using static buffers
 *
 * @param buffers Pre-allocated buffer structure
 * @param carrier The carrier text containing the encoded messages
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param result_count Pointer to store the number of decoded messages
 * @return 1 if decoding was successful, 0 otherwise
 * 
 * Note: The decoded messages are stored in buffers->message_array
 */
int whitespace_stego_static_decode_all(whitespace_stego_buffers_t* buffers,
                                      const char* carrier, size_t carrier_len,
                                      const char* password, size_t* result_count);

/**
 * @brief Get the last error message from encode/decode operations
 *
 * @return Pointer to a static error message string
 */
const char* whitespace_stego_static_last_error(void);

/**
 * @brief Check if a buffer size is within the allowed limits
 *
 * @param size The size to check
 * @return 1 if size is valid (<= MAX_BUFFER_SIZE), 0 otherwise
 */
int whitespace_stego_static_validate_size(size_t size);

/**
 * @brief Get the maximum allowed buffer size
 *
 * @return The maximum buffer size (2^32 - 1)
 */
size_t whitespace_stego_static_max_size(void);

#endif // WHITESPACE_STEGO_STATIC_H 