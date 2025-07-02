#ifndef WHITESPACE_STEGO_H
#define WHITESPACE_STEGO_H

#include <stdbool.h>
#include <stddef.h>

/**
 * @brief Encode a message into carrier text using whitespace steganography
 *
 * @param carrier The carrier text to encode into
 * @param carrier_len Length of the carrier text in bytes
 * @param message The message to encode
 * @param password Optional password for encryption (NULL if not used)
 * @param result Pointer to store the resulting encoded text
 * @return true if encoding was successful, false otherwise
 */
bool whitespace_stego_encode(const char* carrier, size_t carrier_len, const char* message, 
                           const char* password, char** result);

/**
 * @brief Decode a message from carrier text using whitespace steganography
 *
 * @param carrier The carrier text containing the encoded message
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param result Pointer to store the decoded message
 * @return true if decoding was successful, false otherwise
 */
bool whitespace_stego_decode(const char* carrier, size_t carrier_len, const char* password, 
                           char** result);

/**
 * @brief Decode all messages from carrier text using whitespace steganography
 *
 * @param carrier The carrier text containing the encoded messages
 * @param carrier_len Length of the carrier text in bytes
 * @param password Optional password for decryption (NULL if not used)
 * @param results Pointer to store array of decoded messages
 * @param result_count Pointer to store the number of decoded messages
 * @return true if decoding was successful, false otherwise
 */
bool whitespace_stego_decode_all(const char* carrier, size_t carrier_len, const char* password, 
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

#endif // WHITESPACE_STEGO_H 