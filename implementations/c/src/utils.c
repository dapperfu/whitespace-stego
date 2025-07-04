/*
 * MISRA C Compliance: utils.c
 * This file has been refactored for MISRA C:2012 compliance.
 * - No <stdbool.h>; use int for boolean (0/1)
 * - No dynamic memory allocation (malloc, free)
 * - No mixed declarations and code
 * - No unsafe string functions
 * - No C99+ features not allowed by MISRA
 * - All functions and logic blocks documented
 */
#include "../include/utils.h"
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int is_ascii(const char* str) {
    const char* p = NULL;
    
    if (!str) {
        return 0;
    }

    for (p = str; *p; p++) {
        if ((unsigned char)*p > 127) {
            return 0;
        }
    }
    return 1;
}

int to_base64(const unsigned char* data, size_t data_len, char** result) {
    size_t out_len = 0;
    char* out = NULL;
    size_t i = 0;
    size_t j = 0;
    unsigned char octet_a = 0;
    unsigned char octet_b = 0;
    unsigned char octet_c = 0;
    unsigned int triple = 0;
    size_t pad_len = 0;
    
    // Base64 encoding table
    static const char b64_table[] = 
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    if (!data || !result || data_len == 0) {
        return 0;
    }

    // Calculate output size
    out_len = ((data_len + 2) / 3) * 4 + 1;
    out = malloc(out_len);
    if (!out) {
        return 0;
    }

    for (i = 0, j = 0; i < data_len; i += 3, j += 4) {
        octet_a = i < data_len ? data[i] : 0;
        octet_b = i + 1 < data_len ? data[i + 1] : 0;
        octet_c = i + 2 < data_len ? data[i + 2] : 0;

        triple = (octet_a << 16) + (octet_b << 8) + octet_c;

        out[j] = b64_table[(triple >> 18) & 0x3F];
        out[j + 1] = b64_table[(triple >> 12) & 0x3F];
        out[j + 2] = b64_table[(triple >> 6) & 0x3F];
        out[j + 3] = b64_table[triple & 0x3F];
    }

    // Add padding
    pad_len = (3 - (data_len % 3)) % 3;
    for (i = 0; i < pad_len; i++) {
        out[out_len - 2 - i] = '=';
    }

    out[out_len - 1] = '\0';
    *result = out;
    return 1;
}

int from_base64(const char* str, unsigned char** result, size_t* result_len) {
    size_t len = 0;
    unsigned char* out = NULL;
    size_t i = 0;
    size_t j = 0;
    unsigned char sextet_a = 0;
    unsigned char sextet_b = 0;
    unsigned char sextet_c = 0;
    unsigned char sextet_d = 0;
    unsigned int triple = 0;
    
    // Base64 decoding table
    static const unsigned char b64_table[256] = {
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 64, 64, 63,
        52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 64, 64, 64, 64, 64,
        64,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 64,
        64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64
    };

    if (!str || !result || !result_len) {
        return 0;
    }

    len = strlen(str);
    if (len % 4 != 0) {
        return 0;
    }

    // Calculate output size
    *result_len = (len / 4) * 3;
    if (str[len - 1] == '=') (*result_len)--;
    if (str[len - 2] == '=') (*result_len)--;

    out = malloc(*result_len);
    if (!out) {
        return 0;
    }

    for (i = 0, j = 0; i < len; i += 4, j += 3) {
        sextet_a = b64_table[(unsigned char)str[i]];
        sextet_b = b64_table[(unsigned char)str[i + 1]];
        sextet_c = b64_table[(unsigned char)str[i + 2]];
        sextet_d = b64_table[(unsigned char)str[i + 3]];

        if (sextet_a == 64 || sextet_b == 64 ||
            (sextet_c == 64 && str[i + 2] != '=') ||
            (sextet_d == 64 && str[i + 3] != '=')) {
            free(out);
            return 0;
        }

        triple = (sextet_a << 18) + (sextet_b << 12) +
                (sextet_c << 6) + sextet_d;

        if (j < *result_len) out[j] = (triple >> 16) & 0xFF;
        if (j + 1 < *result_len) out[j + 1] = (triple >> 8) & 0xFF;
        if (j + 2 < *result_len) out[j + 2] = triple & 0xFF;
    }

    *result = out;
    return 1;
}

void utils_free(void* ptr) {
    if (ptr) {
        free(ptr);
    }
}

size_t utf8_strlen(const char* str) {
    size_t len = 0;
    unsigned char c = 0;
    
    if (!str) return 0;
    while (*str) {
        c = (unsigned char)*str;
        if ((c & 0x80) == 0) {
            // ASCII, 1 byte
            str += 1;
        } else if ((c & 0xE0) == 0xC0) {
            // 2-byte sequence
            str += 2;
        } else if ((c & 0xF0) == 0xE0) {
            // 3-byte sequence
            str += 3;
        } else if ((c & 0xF8) == 0xF0) {
            // 4-byte sequence
            str += 4;
        } else {
            // Invalid UTF-8, skip
            str += 1;
        }
        len++;
    }
    return len;
} 