#ifndef UTILS_H
#define UTILS_H

#include <stdbool.h>
#include <stddef.h>

/**
 * @brief Check if a string contains only ASCII characters
 *
 * @param str String to check
 * @return true if string contains only ASCII characters, false otherwise
 */
bool is_ascii(const char* str);

/**
 * @brief Convert a string to base64
 *
 * @param data Data to convert
 * @param data_len Length of data
 * @param result Pointer to store base64 string
 * @return true if conversion was successful, false otherwise
 */
bool to_base64(const unsigned char* data, size_t data_len, char** result);

/**
 * @brief Convert a base64 string to binary data
 *
 * @param str Base64 string to convert
 * @param result Pointer to store binary data
 * @param result_len Pointer to store length of binary data
 * @return true if conversion was successful, false otherwise
 */
bool from_base64(const char* str, unsigned char** result, size_t* result_len);

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

#endif // UTILS_H 