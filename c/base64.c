#include <stdlib.h>
#include <string.h>
#include "base64.h"

static const char b64_table[] =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

char *base64_encode(const char *input) {
    size_t len = strlen(input);
    size_t out_len = 4 * ((len + 2) / 3);
    char *out = malloc(out_len + 1);
    if (!out) return NULL;

    size_t i, j;
    for (i = 0, j = 0; i < len;) {
        uint32_t octet_a = i < len ? (unsigned char)input[i++] : 0;
        uint32_t octet_b = i < len ? (unsigned char)input[i++] : 0;
        uint32_t octet_c = i < len ? (unsigned char)input[i++] : 0;

        uint32_t triple = (octet_a << 16) | (octet_b << 8) | octet_c;

        out[j++] = b64_table[(triple >> 18) & 0x3F];
        out[j++] = b64_table[(triple >> 12) & 0x3F];
        out[j++] = (i > len + 1) ? '=' : b64_table[(triple >> 6) & 0x3F];
        out[j++] = (i > len) ? '=' : b64_table[triple & 0x3F];
    }

    out[out_len] = '\0';
    return out;
}#include <stdlib.h>
#include <string.h>
#include "base64.h"

static const unsigned char d[] = {
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 64, 64, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 64, 64,  0, 64, 64,
    64,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 64,
    64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
};

char *base64_decode(const char *input, size_t *out_len) {
    size_t len = strlen(input);
    size_t pad = input[len - 1] == '=' ? (input[len - 2] == '=' ? 2 : 1) : 0;
    size_t decoded_len = (len / 4) * 3 - pad;
    unsigned char *output = malloc(decoded_len + 1);
    if (!output) return NULL;

    for (size_t i = 0, j = 0; i < len;) {
        uint32_t sextet_a = d[(unsigned char)input[i++] & 0x7F];
        uint32_t sextet_b = d[(unsigned char)input[i++] & 0x7F];
        uint32_t sextet_c = d[(unsigned char)input[i++] & 0x7F];
        uint32_t sextet_d = d[(unsigned char)input[i++] & 0x7F];

        uint32_t triple = (sextet_a << 18) + (sextet_b << 12) + (sextet_c << 6) + sextet_d;

        if (j < decoded_len) output[j++] = (triple >> 16) & 0xFF;
        if (j < decoded_len) output[j++] = (triple >> 8) & 0xFF;
        if (j < decoded_len) output[j++] = triple & 0xFF;
    }

    output[decoded_len] = '\0';
    if (out_len) *out_len = decoded_len;
    return (char *)output;
}