/*
 * Large Static Whitespace Steganography Implementation
 * 
 * This implementation uses only static memory allocation with calculated buffer sizes
 * based on available system RAM. No dynamic memory allocation (malloc, free, realloc) is used.
 * 
 * System Analysis:
 * - Available RAM: 61 GiB total, 50 GiB available
 * - Stack limit: 8 MiB
 * - Target: Use half of available RAM = ~30 GiB
 * - Individual buffer size: 4 GiB (safe for 64-bit systems)
 * 
 * Features:
 * - Maximum 4 GiB per buffer (total ~32 GiB across all buffers)
 * - No memory leaks or allocation errors
 * - Global allocation to avoid stack overflow
 * - MISRA C compliant
 * - Suitable for high-performance systems with large memory
 */

#ifndef WHITESPACE_STEGO_STATIC_LARGE_H
#define WHITESPACE_STEGO_STATIC_LARGE_H

#include <stddef.h>
#include <stdint.h>

/* Maximum buffer size: 4 GiB (calculated based on available RAM) */
#define MAX_BUFFER_SIZE_LARGE ((size_t)4294967296U)  // 4 GiB

/* Maximum number of messages that can be decoded at once */
#define MAX_MESSAGES_LARGE 1000

/* Buffer configuration - using global allocation to avoid stack overflow */
typedef struct {
    char* carrier;           /* 4 GiB buffer */
    char* message;           /* 4 GiB buffer */
    char* encoded;           /* 4 GiB buffer */
    char* decoded;           /* 4 GiB buffer */
    char* temp;              /* 4 GiB buffer */
    char* base64;            /* 4 GiB buffer */
    unsigned char* crypto_temp; /* 4 GiB buffer */
    char** message_array;    /* Array of pointers to message buffer */
    size_t carrier_len;
    size_t message_len;
    size_t encoded_len;
    size_t decoded_len;
    size_t temp_len;
    size_t base64_len;
    size_t crypto_temp_len;
    size_t message_count;
    int initialized;         /* Flag to track if buffers are allocated */
} whitespace_stego_buffers_large_t;

/**
 * @brief Initialize large static buffers for whitespace steganography operations
 * 
 * This function allocates global memory buffers of 4 GiB each.
 * Total memory usage: ~32 GiB (8 buffers × 4 GiB)
 *
 * @param buffers Pointer to buffer structure to initialize
 * @return 1 if initialization was successful, 0 otherwise
 */
int whitespace_stego_static_large_init(whitespace_stego_buffers_large_t* buffers);

/**
 * @brief Free large static buffers
 *
 * @param buffers Pointer to buffer structure to free
 */
void whitespace_stego_static_large_free(whitespace_stego_buffers_large_t* buffers);

/**
 * @brief Encode a message into carrier text using large static buffers
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
int whitespace_stego_static_large_encode(whitespace_stego_buffers_large_t* buffers,
                                        const char* carrier, size_t carrier_len,
                                        const char* message, const char* password,
                                        size_t* result_len);

/**
 * @brief Decode a message from carrier text using large static buffers
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
int whitespace_stego_static_large_decode(whitespace_stego_buffers_large_t* buffers,
                                        const char* carrier, size_t carrier_len,
                                        const char* password, size_t* result_len);

/**
 * @brief Decode all messages from carrier text using large static buffers
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
int whitespace_stego_static_large_decode_all(whitespace_stego_buffers_large_t* buffers,
                                            const char* carrier, size_t carrier_len,
                                            const char* password, size_t* result_count);

/**
 * @brief Get the last error message from encode/decode operations
 *
 * @return Pointer to a static error message string
 */
const char* whitespace_stego_static_large_last_error(void);

/**
 * @brief Check if a buffer size is within the allowed limits
 *
 * @param size The size to check
 * @return 1 if size is valid (<= MAX_BUFFER_SIZE_LARGE), 0 otherwise
 */
int whitespace_stego_static_large_validate_size(size_t size);

/**
 * @brief Get the maximum allowed buffer size
 *
 * @return The maximum buffer size (4 GiB)
 */
size_t whitespace_stego_static_large_max_size(void);

/**
 * @brief Get the total memory usage of the large static implementation
 *
 * @return Total memory usage in bytes (~32 GiB)
 */
size_t whitespace_stego_static_large_total_memory_usage(void);

#endif // WHITESPACE_STEGO_STATIC_LARGE_H 