/**
 * @file decode.h
 * @brief Decoding functions for whitespace steganography
 */

#ifndef WHITESPACE_STEGO_DECODE_H
#define WHITESPACE_STEGO_DECODE_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

/**
 * @brief Decode a message from carrier text containing zero-width whitespace
 * 
 * @param input Input text containing encoded message
 * @param input_len Length of input text
 * @param output Output buffer for decoded message
 * @param output_len Length of output buffer
 * @param password Optional password for decryption
 * @param password_len Length of password
 * @return size_t Length of decoded message, or 0 on error
 */
size_t decode_message(
    const char* input,
    size_t input_len,
    char* output,
    size_t output_len,
    const char* password,
    size_t password_len
);

/**
 * @brief Calculate required buffer size for decoded output
 * 
 * @param input_len Length of input text
 * @return size_t Required buffer size
 */
size_t calculate_decoded_size(size_t input_len);

#endif /* WHITESPACE_STEGO_DECODE_H */ 