/*
 * Benchmark core encode/decode functions for C implementation.
 *
 * Build:
 *   gcc -O2 -I../include -o bench_core bench_core.c ../src/whitespace_stego.c ../src/utils.c ../src/crypto.c -lcrypto -lssl
 *
 * Run:
 *   ./bench_core
 */
#include <stdio.h>
#include <string.h>
#include <time.h>
#include "whitespace_stego.h"

#define ITER 1000
#define MSG_REPEAT 100
#define CARRIER_REPEAT 100

int main(void) {
    char message[8192];
    char carrier[8192];
    char *encoded = NULL;
    char *decoded = NULL;
    int i, ret;
    struct timespec t0, t1;
    double elapsed;

    // Prepare message and carrier
    message[0] = '\0';
    carrier[0] = '\0';
    for (i = 0; i < MSG_REPEAT; ++i) strcat(message, "Secret message");
    for (i = 0; i < CARRIER_REPEAT; ++i) strcat(carrier, "This is the carrier text.");

    // Benchmark encode
    clock_gettime(CLOCK_MONOTONIC, &t0);
    for (i = 0; i < ITER; ++i) {
        ret = whitespace_stego_encode(carrier, strlen(carrier), message, NULL, &encoded);
        if (ret != 1) { 
            printf("[WARN] encode error at iter %d: %s\n", i, whitespace_stego_last_error()); 
            break; 
        }
        // Free the result for next iteration
        if (encoded) {
            whitespace_stego_free(encoded);
            encoded = NULL;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    elapsed = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) / 1e9;
    printf("C encode: %.2f ms total, %.2f us/call\n", elapsed*1000, elapsed/ITER*1e6);

    // Get one encoded result for decode benchmark
    ret = whitespace_stego_encode(carrier, strlen(carrier), message, NULL, &encoded);
    if (ret != 1) {
        printf("[ERROR] Failed to encode for decode benchmark: %s\n", whitespace_stego_last_error());
        return 1;
    }

    // Benchmark decode
    clock_gettime(CLOCK_MONOTONIC, &t0);
    for (i = 0; i < ITER; ++i) {
        ret = whitespace_stego_decode(encoded, strlen(encoded), NULL, &decoded);
        if (ret != 1) { 
            printf("[WARN] decode error at iter %d: %s\n", i, whitespace_stego_last_error()); 
            break; 
        }
        // Free the result for next iteration
        if (decoded) {
            whitespace_stego_free(decoded);
            decoded = NULL;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    elapsed = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) / 1e9;
    printf("C decode: %.2f ms total, %.2f us/call\n", elapsed*1000, elapsed/ITER*1e6);

    // Cleanup
    if (encoded) whitespace_stego_free(encoded);
    if (decoded) whitespace_stego_free(decoded);

    return 0;
} 