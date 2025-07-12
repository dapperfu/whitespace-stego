/*
 * MISRA C:2012 Compliant Static Implementation Header: whitespace_stego_static_misra.h
 * This header provides MISRA-compliant constants and safe string functions.
 * - No magic numbers
 * - Safe string operations
 * - Proper constant definitions
 */

#ifndef WHITESPACE_STEGO_STATIC_MISRA_H
#define WHITESPACE_STEGO_STATIC_MISRA_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ============================================================================
 * MISRA-Compliant Constants
 * ============================================================================ */

/* Buffer size constants (powers of 2 for efficiency) */
#define STATIC_BUFFER_SIZE_BYTES     (4U * 1024U * 1024U)  /* 4 MiB */
#define MAX_MESSAGE_SIZE_BYTES       (1024U * 1024U)       /* 1 MiB */
#define MAX_CARRIER_SIZE_BYTES       (2U * 1024U * 1024U)  /* 2 MiB */
#define LOG_BUFFER_SIZE_BYTES        512U
#define ERROR_BUFFER_SIZE_BYTES      256U

/* UTF-8 encoding constants */
#define UTF8_ASCII_MASK              0x80U
#define UTF8_2BYTE_MASK              0xE0U
#define UTF8_3BYTE_MASK              0xF0U
#define UTF8_4BYTE_MASK              0xF8U
#define UTF8_CONTINUATION_MASK       0xC0U
#define UTF8_CONTINUATION_VALUE      0x80U

/* Bit manipulation constants */
#define BITS_PER_BYTE                8U
#define BITS_PER_CHAR                BITS_PER_BYTE
#define BYTE_MASK                    0xFFU
#define BIT_7_MASK                   0x80U
#define BIT_6_MASK                   0x40U
#define BIT_5_MASK                   0x20U
#define BIT_4_MASK                   0x10U
#define BIT_3_MASK                   0x08U
#define BIT_2_MASK                   0x04U
#define BIT_1_MASK                   0x02U
#define BIT_0_MASK                   0x01U

/* UTF-8 character length constants */
#define UTF8_1BYTE_LENGTH            1U
#define UTF8_2BYTE_LENGTH            2U
#define UTF8_3BYTE_LENGTH            3U
#define UTF8_4BYTE_LENGTH            4U

/* Zero-width Unicode character constants */
#define START_MARKER_LENGTH          3U
#define END_MARKER_LENGTH            3U
#define ZERO_BIT_LENGTH              3U
#define ONE_BIT_LENGTH               3U
#define MAX_BIT_LENGTH               3U

/* Base64 encoding constants */
#define BASE64_INPUT_GROUP_SIZE      3U
#define BASE64_OUTPUT_GROUP_SIZE     4U
#define BASE64_PADDING_CHAR          '='
#define BASE64_TABLE_SIZE            64U

/* Crypto constants */
#define KEY_LENGTH_BYTES             32U
#define IV_LENGTH_BYTES              16U
#define SHA256_DIGEST_LENGTH_BYTES   32U

/* ============================================================================
 * Safe String Function Declarations
 * ============================================================================ */

/**
 * Safe string copy with bounds checking
 * @param dest Destination buffer
 * @param dest_size Size of destination buffer
 * @param src Source string
 * @return Number of characters copied (excluding null terminator)
 */
size_t misra_safe_strcpy(char* dest, size_t dest_size, const char* src);

/**
 * Safe string concatenation with bounds checking
 * @param dest Destination buffer
 * @param dest_size Size of destination buffer
 * @param src Source string
 * @return Number of characters concatenated (excluding null terminator)
 */
size_t misra_safe_strcat(char* dest, size_t dest_size, const char* src);

/**
 * Safe string copy with length limit
 * @param dest Destination buffer
 * @param dest_size Size of destination buffer
 * @param src Source string
 * @param max_len Maximum number of characters to copy
 * @return Number of characters copied (excluding null terminator)
 */
size_t misra_safe_strncpy(char* dest, size_t dest_size, const char* src, size_t max_len);

/**
 * Safe string concatenation with length limit
 * @param dest Destination buffer
 * @param dest_size Size of destination buffer
 * @param src Source string
 * @param max_len Maximum number of characters to concatenate
 * @return Number of characters concatenated (excluding null terminator)
 */
size_t misra_safe_strncat(char* dest, size_t dest_size, const char* src, size_t max_len);

/**
 * Safe string length with bounds checking
 * @param str String to measure
 * @param max_len Maximum length to check
 * @return String length (capped at max_len)
 */
size_t misra_safe_strlen(const char* str, size_t max_len);

/* ============================================================================
 * UTF-8 Utility Functions
 * ============================================================================ */

/**
 * Get UTF-8 character length
 * @param first_byte First byte of UTF-8 character
 * @return Length of UTF-8 character in bytes
 */
uint8_t misra_utf8_char_length(uint8_t first_byte);

/**
 * Validate UTF-8 character
 * @param str Pointer to UTF-8 character
 * @param str_len Remaining string length
 * @return 1 if valid, 0 if invalid
 */
int misra_utf8_char_valid(const char* str, size_t str_len);

/* ============================================================================
 * Bit Manipulation Functions
 * ============================================================================ */

/**
 * Extract bit from byte
 * @param byte Source byte
 * @param bit_position Bit position (0-7)
 * @return Bit value (0 or 1)
 */
uint8_t misra_extract_bit(uint8_t byte, uint8_t bit_position);

/**
 * Set bit in byte
 * @param byte Source byte
 * @param bit_position Bit position (0-7)
 * @param bit_value Bit value (0 or 1)
 * @return Modified byte
 */
uint8_t misra_set_bit(uint8_t byte, uint8_t bit_position, uint8_t bit_value);

#ifdef __cplusplus
}
#endif

#endif 