/**
 * @file utils.h
 * @brief Utility functions for whitespace steganography
 */

#ifndef WHITESPACE_STEGO_UTILS_H
#define WHITESPACE_STEGO_UTILS_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

/**
 * @brief Base64 encode binary data
 * 
 * @param input Input binary data
 * @param input_len Length of input data
 * @param output Output buffer for base64 string
 * @param output_len Length of output buffer
 * @return size_t Length of encoded string, or 0 on error
 */
size_t base64_encode(const uint8_t* input, size_t input_len, char* output, size_t output_len);

/**
 * @brief Base64 decode string to binary data
 * 
 * @param input Input base64 string
 * @param input_len Length of input string
 * @param output Output buffer for binary data
 * @param output_len Length of output buffer
 * @return size_t Length of decoded data, or 0 on error
 */
size_t base64_decode(const char* input, size_t input_len, uint8_t* output, size_t output_len);

/**
 * @brief Convert binary data to zero-width whitespace
 * 
 * @param input Input binary data
 * @param input_len Length of input data
 * @param output Output buffer for zero-width string
 * @param output_len Length of output buffer
 * @return size_t Length of output string, or 0 on error
 */
size_t binary_to_zerowidth(const uint8_t* input, size_t input_len, char* output, size_t output_len);

/**
 * @brief Convert zero-width whitespace to binary data
 * 
 * @param input Input zero-width string
 * @param input_len Length of input string
 * @param output Output buffer for binary data
 * @param output_len Length of output buffer
 * @return size_t Length of decoded data, or 0 on error
 */
size_t zerowidth_to_binary(const char* input, size_t input_len, uint8_t* output, size_t output_len);

/**
 * @brief XOR encrypt/decrypt data with password
 * 
 * @param data Data to encrypt/decrypt
 * @param data_len Length of data
 * @param password Password to use
 * @param password_len Length of password
 * @return bool true on success, false on error
 */
bool xor_encrypt(uint8_t* data, size_t data_len, const char* password, size_t password_len);

/**
 * @brief Read entire file into memory
 * 
 * @param filename Name of file to read
 * @param data Pointer to store allocated data
 * @param size Pointer to store size of data
 * @return bool true on success, false on error
 */
bool read_file(const char* filename, uint8_t** data, size_t* size);

/**
 * @brief Write data to file
 * 
 * @param filename Name of file to write
 * @param data Data to write
 * @param size Size of data
 * @return bool true on success, false on error
 */
bool write_file(const char* filename, const uint8_t* data, size_t size);

#endif /* WHITESPACE_STEGO_UTILS_H */ 
