#include <stdlib.h>
#include <string.h>
#include "decode.h"

#define CONTROL_START "\u2060"
#define CONTROL_END "\u2063"
#define BIT_0 "\u200b"
#define BIT_1 "\u200c"

char *decode_message(const char *input) {
    const char *start = strstr(input, CONTROL_START);
    if (!start) return strdup("ERR: No start marker");
    start += strlen(CONTROL_START);
    const char *end = strstr(start, CONTROL_END);
    if (!end) return strdup("ERR: No end marker");

    size_t bits_len = end - start;
    char *bits = (char *)malloc(bits_len + 1);
    strncpy(bits, start, bits_len);
    bits[bits_len] = '\0';

    size_t msg_len = bits_len / 8;
    char *message = (char *)malloc(msg_len + 1);
    for (size_t i = 0; i < msg_len; ++i) {
        char c = 0;
        for (int b = 0; b < 8; ++b) {
            char *symbol = strndup(bits + i * 8 + b, strlen(BIT_0));
            if (strcmp(symbol, BIT_1) == 0) c |= (1 << (7 - b));
            free(symbol);
        }
        message[i] = c;
    }
    message[msg_len] = '\0';
    free(bits);
    return message;
}