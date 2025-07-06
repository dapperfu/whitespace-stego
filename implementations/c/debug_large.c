#include "../include/whitespace_stego_static.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char encoded[4 * 1024 * 1024];
    char decoded[1024 * 1024];
    
    // Create large test data
    char* large_message = malloc(10000);
    char* large_carrier = malloc(20000);
    
    // Fill with test data
    for (int i = 0; i < 9999; i++) {
        large_message[i] = 'A' + (i % 26);
    }
    large_message[9999] = '\0';
    
    for (int i = 0; i < 19999; i++) {
        large_carrier[i] = 'a' + (i % 26);
    }
    large_carrier[19999] = '\0';
    
    printf("Message length: %zu\n", strlen(large_message));
    printf("Carrier length: %zu\n", strlen(large_carrier));
    
    // Test encoding large data
    int result = whitespace_stego_static_encode(large_carrier, strlen(large_carrier), 
                                               large_message, "test123", 
                                               encoded, sizeof(encoded));
    
    printf("Encode result: %d\n", result);
    if (!result) {
        printf("Error: %s\n", whitespace_stego_static_last_error());
    }
    
    free(large_message);
    free(large_carrier);
    return 0;
} 