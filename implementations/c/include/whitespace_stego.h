/*
<<<<<<< HEAD
 * Whitespace Steganography Library Header
 * 
 * Common definitions and structures for whitespace steganography
 */

=======
 * MISRA C Compliance: whitespace_stego.h
 * This file has been refactored for MISRA C:2012 compliance.
 * - No <stdbool.h>; use int for boolean (0/1)
 * - All functions and logic blocks documented
 */
>>>>>>> 92b3c39d6dc84306d706a192eafe0a81e720e625
#ifndef WHITESPACE_STEGO_H
#define WHITESPACE_STEGO_H

#include <stddef.h>

<<<<<<< HEAD
// Common buffer sizes for different implementations
#define MAX_BUFFER_SIZE_TINY     (4 * 1024)        // 4 KiB
#define MAX_BUFFER_SIZE_SMALL    (1024 * 1024)     // 1 MiB
#define MAX_BUFFER_SIZE_STANDARD (4ULL * 1024 * 1024 * 1024)  // 4 GiB
#define MAX_BUFFER_SIZE_LARGE    (4ULL * 1024 * 1024 * 1024)  // 4 GiB

// Maximum number of messages for multi-message decoding
#define MAX_MESSAGES_TINY        10
#define MAX_MESSAGES_SMALL       100
#define MAX_MESSAGES_STANDARD    1000
#define MAX_MESSAGES_LARGE       1000

// Common return codes
#define WHITESPACE_STEGO_SUCCESS 1
#define WHITESPACE_STEGO_ERROR   0

// Common error handling
extern char* whitespace_stego_last_error(void);
=======
/**
 * @brief Encode a message into carrier text using whitespace steganography
 *
 * @param carrier The carrier text to encode into
 * @param carrier_len Length of the carrier text in bytes
 * @param message The message to encode
 * @param password Optional password for encryption (NULL if not used)
 * @param result Pointer to store the resulting encoded text
 * @return 1 if encoding was successful, 0 otherwise
 */
int whitespace_stego_encode(const char* carrier, size_t carrier_len, const char* message, 
                           const char* password, char** result);

/**
 * @brief Decode a message from carrier text using whitespace steganography
 *
 * @param carrier The carrier text containing the encoded message
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param result Pointer to store the decoded message
 * @return 1 if decoding was successful, 0 otherwise
 */
int whitespace_stego_decode(const char* carrier, size_t carrier_len, const char* password, 
                           char** result);

/**
 * @brief Decode all messages from carrier text using whitespace steganography
 *
 * @param carrier The carrier text containing the encoded messages
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param results Pointer to store array of decoded messages
 * @param result_count Pointer to store the number of decoded messages
 * @return 1 if decoding was successful, 0 otherwise
 */
int whitespace_stego_decode_all(const char* carrier, size_t carrier_len, const char* password, 
                                char*** results, size_t* result_count);

/**
 * @brief Free memory allocated by encode/decode functions
 *
 * @param ptr Pointer to the memory to free
 */
void whitespace_stego_free(char* ptr);

/**
 * @brief Free memory allocated by decode_all function
 *
 * @param results Array of message pointers to free
 * @param count Number of messages in the array
 */
void whitespace_stego_free_all(char** results, size_t count);

/**
 * @brief Get the last error message from encode/decode
 *
 * @return Pointer to a static error message string
 */
const char* whitespace_stego_last_error(void);
>>>>>>> 92b3c39d6dc84306d706a192eafe0a81e720e625

#endif // WHITESPACE_STEGO_H 