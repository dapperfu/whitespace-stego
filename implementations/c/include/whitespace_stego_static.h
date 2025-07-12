/*
 * Static C Implementation Header: whitespace_stego_static.h
 * This header provides the interface for the static version with pre-allocated buffers.
 * - MISRA C:2012 compliant logging system
 */

#ifndef WHITESPACE_STEGO_STATIC_H
#define WHITESPACE_STEGO_STATIC_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * MISRA-compliant logging levels
 */
typedef enum {
    LOG_LEVEL_NONE = 0,
    LOG_LEVEL_ERROR = 1,
    LOG_LEVEL_WARN = 2,
    LOG_LEVEL_INFO = 3,
    LOG_LEVEL_DEBUG = 4
} log_level_t;

/**
 * Set the logging level for MISRA-compliant debug output
 * @param level The logging level to set
 */
void whitespace_stego_static_set_log_level(log_level_t level);

/**
 * MISRA-compliant log function (no printf, uses snprintf to buffer)
 * @param level The logging level
 * @param format The format string (limited to safe format specifiers)
 * @param ... Variable arguments
 */
void whitespace_stego_static_log(log_level_t level, const char* format, ...);

/**
 * Get the last error message from static implementation
 * @return Pointer to error message string
 */
const char* whitespace_stego_static_last_error(void);

/**
 * Encode a message into carrier text using static buffers
 * @param carrier The carrier text
 * @param carrier_len Length of carrier text
 * @param message The message to encode
 * @param password Optional password for encryption (NULL for no encryption)
 * @param result Output buffer for encoded result
 * @param result_size Size of result buffer
 * @return 1 on success, 0 on failure
 */
int whitespace_stego_static_encode(const char* carrier, size_t carrier_len, const char* message,
                                  const char* password, char* result, size_t result_size);

/**
 * Decode a message from carrier text using static buffers
 * @param carrier The carrier text containing encoded message
 * @param carrier_len Length of carrier text
 * @param password Optional password for decryption (NULL for no decryption)
 * @param result Output buffer for decoded result
 * @param result_size Size of result buffer
 * @return 1 on success, 0 on failure
 */
int whitespace_stego_static_decode(const char* carrier, size_t carrier_len, const char* password,
                                  char* result, size_t result_size);

/**
 * Decode all messages from carrier text using static buffers
 * @param carrier The carrier text containing encoded messages
 * @param carrier_len Length of carrier text
 * @param password Optional password for decryption (NULL for no decryption)
 * @param results Array of output buffers for decoded results
 * @param max_results Maximum number of results to decode
 * @param result_count Output parameter for number of results found
 * @return 1 on success, 0 on failure
 */
int whitespace_stego_static_decode_all(const char* carrier, size_t carrier_len, const char* password,
                                       char* results[], size_t max_results, size_t* result_count);

#ifdef __cplusplus
}
#endif

#endif // WHITESPACE_STEGO_STATIC_H 