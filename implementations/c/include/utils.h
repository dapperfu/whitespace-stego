/*
 * Utils Header: utils.h
 * Provides utility functions for base64 encoding/decoding and memory management.
 */

#ifndef UTILS_H
#define UTILS_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Encode binary data to base64 string
 * @param data Input binary data
 * @param data_len Length of input data
 * @param result Output base64 string (will be allocated)
 * @return 1 on success, 0 on failure
 */
int to_base64(const unsigned char* data, size_t data_len, char** result);

/**
 * Decode base64 string to binary data
 * @param base64_str Input base64 string
 * @param result Output binary data (will be allocated)
 * @param result_len Output length of binary data
 * @return 1 on success, 0 on failure
 */
int from_base64(const char* base64_str, unsigned char** result, size_t* result_len);

/**
 * Free allocated memory from utils functions
 * @param ptr Pointer to memory to free
 */
void utils_free(void* ptr);

/**
 * Get utils error message
 * @return Pointer to error message string
 */
const char* utils_get_error(void);

/**
 * Clear utils error state
 */
void utils_clear_error(void);

/**
 * Validate base64 string
 * @param str String to validate
 * @return 1 if valid base64, 0 if invalid
 */
int is_valid_base64(const char* str);

/**
 * Calculate base64 output length for given input length
 * @param input_len Input data length
 * @return Required output buffer size for base64 encoding
 */
size_t base64_output_length(size_t input_len);

/**
 * Calculate binary output length for given base64 string length
 * @param base64_len Base64 string length
 * @return Required output buffer size for base64 decoding
 */
size_t base64_decode_length(size_t base64_len);

#ifdef __cplusplus
}
#endif

#endif 