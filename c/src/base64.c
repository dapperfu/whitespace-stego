/* Base64 encoding/decoding implementation (RFC 4648) */

#include <string.h>
#include <stdlib.h>

static const char base64_chars[] =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

static int base64_char_index(char c) {
    if (c >= 'A' && c <= 'Z') return c - 'A';
    if (c >= 'a' && c <= 'z') return c - 'a' + 26;
    if (c >= '0' && c <= '9') return c - '0' + 52;
    if (c == '+') return 62;
    if (c == '/') return 63;
    return -1;
}

size_t base64_encode(const unsigned char *input, size_t input_len,
                     char *output, size_t output_size) {
    size_t i, j;
    size_t output_len = ((input_len + 2) / 3) * 4;

    if (output_size < output_len + 1) {
        return 0;
    }

    for (i = 0, j = 0; i < input_len; i += 3, j += 4) {
        unsigned char b1 = input[i];
        unsigned char b2 = (i + 1 < input_len) ? input[i + 1] : 0;
        unsigned char b3 = (i + 2 < input_len) ? input[i + 2] : 0;

        output[j] = base64_chars[b1 >> 2];
        output[j + 1] = base64_chars[((b1 & 0x03) << 4) | (b2 >> 4)];
        output[j + 2] = (i + 1 < input_len)
                            ? base64_chars[((b2 & 0x0f) << 2) | (b3 >> 6)]
                            : '=';
        output[j + 3] = (i + 2 < input_len) ? base64_chars[b3 & 0x3f] : '=';
    }

    output[output_len] = '\0';
    return output_len;
}

size_t base64_decode(const char *input, size_t input_len,
                     unsigned char *output, size_t output_size) {
    size_t i, j;
    size_t padding = 0;

    if (input_len % 4 != 0) {
        return 0;
    }

    if (input_len > 0 && input[input_len - 1] == '=') {
        padding++;
        if (input_len > 1 && input[input_len - 2] == '=') {
            padding++;
        }
    }

    size_t output_len = (input_len / 4) * 3 - padding;

    if (output_size < output_len) {
        return 0;
    }

    for (i = 0, j = 0; i < input_len; i += 4, j += 3) {
        int c1 = base64_char_index(input[i]);
        int c2 = base64_char_index(input[i + 1]);
        int c3 = (i + 2 < input_len && input[i + 2] != '=')
                     ? base64_char_index(input[i + 2])
                     : -1;
        int c4 = (i + 3 < input_len && input[i + 3] != '=')
                     ? base64_char_index(input[i + 3])
                     : -1;

        if (c1 < 0 || c2 < 0) {
            return 0;
        }

        output[j] = (c1 << 2) | (c2 >> 4);
        if (c3 >= 0) {
            output[j + 1] = ((c2 & 0x0f) << 4) | (c3 >> 2);
            if (c4 >= 0) {
                output[j + 2] = ((c3 & 0x03) << 6) | c4;
            }
        }
    }

    return output_len;
}

