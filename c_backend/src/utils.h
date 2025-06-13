/**
 * @file utils.h
 * @brief Utility functions for whitespace steganography
 */

#ifndef WHITESPACE_STEGO_UTILS_H
#define WHITESPACE_STEGO_UTILS_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#ifdef _WIN32
    #ifdef WHITESPACE_STEGO_EXPORTS
        #define WHITESPACE_STEGO_API __declspec(dllexport)
    #else
        #define WHITESPACE_STEGO_API __declspec(dllimport)
    #endif
#else
    #define WHITESPACE_STEGO_API __attribute__((visibility("default")))
#endif

/**
 * @brief Base64 encode binary data
 * 
 * @param input Input binary data
 * @param input_len Length of input data
 * @param output Output buffer for base64 encoded data
 * @param output_len Length of output buffer
 * @return size_t Length of encoded data, or 0 on error
 */
WHITESPACE_STEGO_API size_t base64_encode(const uint8_t* input,
                                         size_t input_len,
                                         char* output,
                                         size_t output_len);

/**
 * @brief Base64 decode data
 * 
 * @param input Input base64 encoded data
 * @param input_len Length of input data
 * @param output Output buffer for decoded data
 * @param output_len Length of output buffer
 * @return size_t Length of decoded data, or 0 on error
 */
WHITESPACE_STEGO_API size_t base64_decode(const char* input,
                                         size_t input_len,
                                         uint8_t* output,
                                         size_t output_len);

/**
 * @brief Convert binary data to zero-width characters
 * 
 * @param input Input binary data
 * @param input_len Length of input data
 * @param output Output buffer for zero-width characters
 * @param output_len Length of output buffer
 * @return size_t Length of zero-width characters, or 0 on error
 */
WHITESPACE_STEGO_API size_t binary_to_zerowidth(const uint8_t* input,
                                               size_t input_len,
                                               char* output,
                                               size_t output_len);

/**
 * @brief Convert zero-width characters to binary data
 * 
 * @param input Input zero-width characters
 * @param input_len Length of input data
 * @param output Output buffer for binary data
 * @param output_len Length of output buffer
 * @return size_t Length of binary data, or 0 on error
 */
WHITESPACE_STEGO_API size_t zerowidth_to_binary(const char* input,
                                               size_t input_len,
                                               uint8_t* output,
                                               size_t output_len);

/**
 * @brief XOR encrypt/decrypt data with a password
 * 
 * @param data Data to encrypt/decrypt
 * @param data_len Length of data
 * @param password Password to use
 * @param password_len Length of password
 * @return bool true on success, false on error
 */
WHITESPACE_STEGO_API bool xor_encrypt(uint8_t* data,
                                     size_t data_len,
                                     const char* password,
                                     size_t password_len);

/**
 * @brief Read a file into memory
 * 
 * @param filename Name of file to read
 * @param data Pointer to store allocated memory
 * @param size Pointer to store file size
 * @return bool true on success, false on error
 */
WHITESPACE_STEGO_API bool read_file(const char* filename, uint8_t** data, size_t* size);

/**
 * @brief Write data to a file
 * 
 * @param filename Name of file to write
 * @param data Data to write
 * @param size Size of data
 * @return bool true on success, false on error
 */
WHITESPACE_STEGO_API bool write_file(const char* filename, const uint8_t* data, size_t size);

/**
 * @brief Strip zero-width and control characters from text
 * 
 * @param input Input text
 * @param output Output buffer
 */
WHITESPACE_STEGO_API void strip_zero_width_and_control(const char* input, char* output);

/**
 * @brief Check if carrier text is valid (contains no zero-width or control characters)
 * 
 * @param text Text to check
 * @param len Length of text
 * @return bool true if valid, false if invalid
 */
WHITESPACE_STEGO_API bool is_valid_carrier(const char* text, size_t len);

#endif /* WHITESPACE_STEGO_UTILS_H */ 
