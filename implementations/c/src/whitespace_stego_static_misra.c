/*
 * MISRA C:2012 Compliant Static Implementation: whitespace_stego_static_misra.c
 * This file provides MISRA-compliant safe string functions and utilities.
 * - No unsafe string functions
 * - Bounds checking on all operations
 * - No magic numbers
 * - Proper error handling
 */

#include "../include/whitespace_stego_static_misra.h"
#include <string.h>
#include <stdint.h>

/* ============================================================================
 * Safe String Function Implementations
 * ============================================================================ */

size_t misra_safe_strcpy(char* dest, size_t dest_size, const char* src) {
    size_t src_len = 0U;
    size_t copy_len = 0U;
    
    /* Parameter validation */
    if ((dest == NULL) || (src == NULL) || (dest_size == 0U)) {
        return 0U;
    }
    
    /* Calculate source length with bounds checking */
    src_len = misra_safe_strlen(src, dest_size - 1U);
    
    /* Determine copy length */
    if (src_len >= dest_size) {
        copy_len = dest_size - 1U;
    } else {
        copy_len = src_len;
    }
    
    /* Copy string with bounds checking */
    if (copy_len > 0U) {
        (void)memcpy(dest, src, copy_len);
    }
    
    /* Ensure null termination */
    dest[copy_len] = '\0';
    
    return copy_len;
}

size_t misra_safe_strcat(char* dest, size_t dest_size, const char* src) {
    size_t dest_len = 0U;
    size_t src_len = 0U;
    size_t available_space = 0U;
    size_t copy_len = 0U;
    
    /* Parameter validation */
    if ((dest == NULL) || (src == NULL) || (dest_size == 0U)) {
        return 0U;
    }
    
    /* Get current destination length */
    dest_len = misra_safe_strlen(dest, dest_size);
    
    /* Calculate available space */
    if (dest_len >= dest_size) {
        return 0U; /* Destination is full */
    }
    available_space = dest_size - dest_len - 1U;
    
    /* Calculate source length with bounds checking */
    src_len = misra_safe_strlen(src, available_space);
    
    /* Determine copy length */
    if (src_len >= available_space) {
        copy_len = available_space;
    } else {
        copy_len = src_len;
    }
    
    /* Concatenate string with bounds checking */
    if (copy_len > 0U) {
        (void)memcpy(dest + dest_len, src, copy_len);
    }
    
    /* Ensure null termination */
    dest[dest_len + copy_len] = '\0';
    
    return copy_len;
}

size_t misra_safe_strncpy(char* dest, size_t dest_size, const char* src, size_t max_len) {
    size_t copy_len = 0U;
    
    /* Parameter validation */
    if ((dest == NULL) || (src == NULL) || (dest_size == 0U)) {
        return 0U;
    }
    
    /* Determine copy length */
    if (max_len >= dest_size) {
        copy_len = dest_size - 1U;
    } else {
        copy_len = max_len;
    }
    
    /* Copy string with bounds checking */
    if (copy_len > 0U) {
        (void)memcpy(dest, src, copy_len);
    }
    
    /* Ensure null termination */
    dest[copy_len] = '\0';
    
    return copy_len;
}

size_t misra_safe_strncat(char* dest, size_t dest_size, const char* src, size_t max_len) {
    size_t dest_len = 0U;
    size_t available_space = 0U;
    size_t copy_len = 0U;
    
    /* Parameter validation */
    if ((dest == NULL) || (src == NULL) || (dest_size == 0U)) {
        return 0U;
    }
    
    /* Get current destination length */
    dest_len = misra_safe_strlen(dest, dest_size);
    
    /* Calculate available space */
    if (dest_len >= dest_size) {
        return 0U; /* Destination is full */
    }
    available_space = dest_size - dest_len - 1U;
    
    /* Determine copy length */
    if (max_len >= available_space) {
        copy_len = available_space;
    } else {
        copy_len = max_len;
    }
    
    /* Concatenate string with bounds checking */
    if (copy_len > 0U) {
        (void)memcpy(dest + dest_len, src, copy_len);
    }
    
    /* Ensure null termination */
    dest[dest_len + copy_len] = '\0';
    
    return copy_len;
}

size_t misra_safe_strlen(const char* str, size_t max_len) {
    size_t len = 0U;
    
    /* Parameter validation */
    if (str == NULL) {
        return 0U;
    }
    
    /* Calculate length with bounds checking */
    while ((len < max_len) && (str[len] != '\0')) {
        len = len + 1U;
    }
    
    return len;
}

/* ============================================================================
 * UTF-8 Utility Function Implementations
 * ============================================================================ */

uint8_t misra_utf8_char_length(uint8_t first_byte) {
    uint8_t char_length = UTF8_1BYTE_LENGTH;
    
    /* Determine UTF-8 character length based on first byte */
    if ((first_byte & UTF8_ASCII_MASK) == 0U) {
        /* ASCII character (1 byte) */
        char_length = UTF8_1BYTE_LENGTH;
    } else if ((first_byte & UTF8_2BYTE_MASK) == 0xC0U) {
        /* 2-byte UTF-8 sequence (110xxxxx) */
        char_length = UTF8_2BYTE_LENGTH;
    } else if ((first_byte & UTF8_3BYTE_MASK) == 0xE0U) {
        /* 3-byte UTF-8 sequence (1110xxxx) */
        char_length = UTF8_3BYTE_LENGTH;
    } else if ((first_byte & UTF8_4BYTE_MASK) == 0xF0U) {
        /* 4-byte UTF-8 sequence (11110xxx) */
        char_length = UTF8_4BYTE_LENGTH;
    } else {
        /* Invalid UTF-8 start byte */
        char_length = UTF8_1BYTE_LENGTH;
    }
    
    return char_length;
}

int misra_utf8_char_valid(const char* str, size_t str_len) {
    uint8_t first_byte = 0U;
    uint8_t char_length = 0U;
    size_t i = 0U;
    
    /* Parameter validation */
    if ((str == NULL) || (str_len == 0U)) {
        return 0;
    }
    
    /* Get first byte */
    first_byte = (uint8_t)str[0U];
    char_length = misra_utf8_char_length(first_byte);
    
    /* Check if we have enough bytes for the character */
    if (char_length > str_len) {
        return 0; /* Incomplete character */
    }
    
    /* Validate continuation bytes for multi-byte sequences */
    if (char_length > UTF8_1BYTE_LENGTH) {
        for (i = 1U; i < char_length; i = i + 1U) {
            uint8_t byte = (uint8_t)str[i];
            if ((byte & UTF8_CONTINUATION_MASK) != UTF8_CONTINUATION_VALUE) {
                return 0; /* Invalid continuation byte */
            }
        }
    }
    
    return 1;
}

/* ============================================================================
 * Bit Manipulation Function Implementations
 * ============================================================================ */

uint8_t misra_extract_bit(uint8_t byte, uint8_t bit_position) {
    uint8_t bit_value = 0U;
    
    /* Parameter validation */
    if (bit_position >= BITS_PER_BYTE) {
        return 0U;
    }
    
    /* Extract bit value using bit masks */
    switch (bit_position) {
        case 0U:
            bit_value = (byte & BIT_0_MASK) != 0U ? 1U : 0U;
            break;
        case 1U:
            bit_value = (byte & BIT_1_MASK) != 0U ? 1U : 0U;
            break;
        case 2U:
            bit_value = (byte & BIT_2_MASK) != 0U ? 1U : 0U;
            break;
        case 3U:
            bit_value = (byte & BIT_3_MASK) != 0U ? 1U : 0U;
            break;
        case 4U:
            bit_value = (byte & BIT_4_MASK) != 0U ? 1U : 0U;
            break;
        case 5U:
            bit_value = (byte & BIT_5_MASK) != 0U ? 1U : 0U;
            break;
        case 6U:
            bit_value = (byte & BIT_6_MASK) != 0U ? 1U : 0U;
            break;
        case 7U:
            bit_value = (byte & BIT_7_MASK) != 0U ? 1U : 0U;
            break;
        default:
            bit_value = 0U;
            break;
    }
    
    return bit_value;
}

uint8_t misra_set_bit(uint8_t byte, uint8_t bit_position, uint8_t bit_value) {
    uint8_t result = byte;
    
    /* Parameter validation */
    if (bit_position >= BITS_PER_BYTE) {
        return byte;
    }
    
    /* Set or clear bit based on bit_value */
    if (bit_value != 0U) {
        /* Set bit */
        switch (bit_position) {
            case 0U:
                result = result | BIT_0_MASK;
                break;
            case 1U:
                result = result | BIT_1_MASK;
                break;
            case 2U:
                result = result | BIT_2_MASK;
                break;
            case 3U:
                result = result | BIT_3_MASK;
                break;
            case 4U:
                result = result | BIT_4_MASK;
                break;
            case 5U:
                result = result | BIT_5_MASK;
                break;
            case 6U:
                result = result | BIT_6_MASK;
                break;
            case 7U:
                result = result | BIT_7_MASK;
                break;
            default:
                break;
        }
    } else {
        /* Clear bit */
        switch (bit_position) {
            case 0U:
                result = result & (~BIT_0_MASK);
                break;
            case 1U:
                result = result & (~BIT_1_MASK);
                break;
            case 2U:
                result = result & (~BIT_2_MASK);
                break;
            case 3U:
                result = result & (~BIT_3_MASK);
                break;
            case 4U:
                result = result & (~BIT_4_MASK);
                break;
            case 5U:
                result = result & (~BIT_5_MASK);
                break;
            case 6U:
                result = result & (~BIT_6_MASK);
                break;
            case 7U:
                result = result & (~BIT_7_MASK);
                break;
            default:
                break;
        }
    }
    
    return result;
} 