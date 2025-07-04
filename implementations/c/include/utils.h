/*
 * MISRA C Compliance: utils.h
 * This file has been refactored for MISRA C:2012 compliance.
 * - No <stdbool.h>; use int for boolean (0/1)
 * - All functions and logic blocks documented
 */
#ifndef UTILS_H
#define UTILS_H

#include <stddef.h>

/**
 * @brief Check if a string contains only ASCII characters
 *
 * @param str String to check
 * @return 1 if string contains only ASCII characters, 0 otherwise
 */
int is_ascii(const char* str);

/**
 * @brief Convert a string to base64
 *
 * @param data Data to convert
 * @param data_len Length of data
 * @param result Pointer to store base64 string
 * @return 1 if conversion was successful, 0 otherwise
 */
int to_base64(const unsigned char* data, size_t data_len, char** result);

/**
 * @brief Convert a base64 string to binary data
 *
 * @param str Base64 string to convert
 * @param result Pointer to store binary data
 * @param result_len Pointer to store length of binary data
 * @return 1 if conversion was successful, 0 otherwise
 */
int from_base64(const char* str, unsigned char** result, size_t* result_len);

/**
 * @brief Free memory allocated by base64 functions
 *
 * @param ptr Pointer to the memory to free
 */
void utils_free(void* ptr);

/**
 * @brief Count the number of UTF-8 codepoints in a string
 *
 * @param str UTF-8 encoded string
 * @return Number of codepoints in the string
 */
size_t utf8_strlen(const char* str);

<<<<<<< HEAD
/**
 * @brief Convert a string to base64 with static buffer
 *
 * @param data Data to convert
 * @param data_len Length of data
 * @param result_buffer Static buffer to store base64 string
 * @param result_buffer_size Size of the result buffer
 * @param result_len Pointer to store length of base64 string
 * @return 1 if conversion was successful, 0 otherwise
 */
int to_base64_static(const unsigned char* data, size_t data_len, 
                     char* result_buffer, size_t result_buffer_size, size_t* result_len);

/**
 * @brief Convert a base64 string to binary data with static buffer
 *
 * @param data Base64 data to convert
 * @param data_len Length of base64 data
 * @param result_buffer Static buffer to store binary data
 * @param result_buffer_size Size of the result buffer
 * @param result_len Pointer to store length of binary data
 * @return 1 if conversion was successful, 0 otherwise
 */
int from_base64_static(const unsigned char* data, size_t data_len,
                       unsigned char* result_buffer, size_t result_buffer_size, size_t* result_len);

=======
>>>>>>> 92b3c39d6dc84306d706a192eafe0a81e720e625
#endif // UTILS_H 