#include <stdlib.h>
#include <string.h>
#include "encode.h"
#include "base64.h"

#define CONTROL_START "\u2060"
#define CONTROL_END "\u2063"
#define BIT_0 "\u200b"
#define BIT_1 "\u200c"

char *encode_message(const char *message, const char *carrier) {
    char *b64 = base64_encode(message);
    size_t len = strlen(b64);
    size_t out_size = len * 8 * strlen(BIT_0) + strlen(carrier) + 100;
    char *output = malloc(out_size);
    if (!output) return NULL;

    strcpy(output, carrier);
    strcat(output, CONTROL_START);
    for (size_t i = 0; i < len; ++i) {
        for (int bit = 7; bit >= 0; --bit) {
            strcat(output, (b64[i] >> bit) & 1 ? BIT_1 : BIT_0);
        }
    }
    strcat(output, CONTROL_END);
    free(b64);
    return output;
}