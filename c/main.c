#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "encode.h"
#include "decode.h"

void print_usage() {
    printf("Usage: whitespace-stego-c encode|decode -m <message> -c <carrier>\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        print_usage();
        return 1;
    }

    const char *mode = argv[1];
    const char *message = NULL;
    const char *carrier = "";

    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 && i + 1 < argc) {
            message = argv[++i];
        } else if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            carrier = argv[++i];
        }
    }

    if (!message && strcmp(mode, "decode") != 0) {
        print_usage();
        return 1;
    }

    if (strcmp(mode, "encode") == 0) {
        char *result = encode_message(message, carrier);
        printf("%s\n", result);
        free(result);
    } else if (strcmp(mode, "decode") == 0) {
        char *decoded = decode_message(message);
        printf("%s\n", decoded);
        free(decoded);
    } else {
        print_usage();
        return 1;
    }

    return 0;
}