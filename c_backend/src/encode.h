/**
 * @file encode.h
 * @brief Encoding functions for whitespace steganography
 */

#ifndef WHITESPACE_STEGO_ENCODE_H
#define WHITESPACE_STEGO_ENCODE_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

/**
 * @brief Encode a message into carrier text using zero-width whitespace
 * 
 * @param message Message to encode
 * @param message_len Length of message
 * @param carrier Carrier text to use
 * @param carrier_len Length of carrier text
 * @param output Output buffer for encoded text
 * @param output_len Length of output buffer
 * @param password Optional password for encryption
 * @param password_len Length of password
 * @return size_t Length of encoded text, or 0 on error
 */
size_t encode_message(
    const char* message,
    size_t message_len,
    const char* carrier,
    size_t carrier_len,
    char* output,
    size_t output_len,
    const char* password,
    size_t password_len
);

/**
 * @brief Calculate required buffer size for encoded output
 * 
 * @param message_len Length of message to encode
 * @param carrier_len Length of carrier text
 * @return size_t Required buffer size
 */
size_t calculate_encoded_size(size_t message_len, size_t carrier_len);

#endif /* WHITESPACE_STEGO_ENCODE_H */ 