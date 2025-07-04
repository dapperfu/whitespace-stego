/*
 * Static Whitespace Steganography Test Program
 * 
 * This program demonstrates the static C implementation with no dynamic allocation.
 * It uses pre-allocated buffers with a 2^32 character limit.
 */

#include "../include/whitespace_stego_static.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    printf("Static Whitespace Steganography Implementation\n");
    printf("Maximum buffer size: %zu bytes (%.2f GiB)\n", 
           whitespace_stego_static_max_size(),
           (double)whitespace_stego_static_max_size() / (1024.0 * 1024.0 * 1024.0));
    printf("No dynamic memory allocation used\n\n");
    
    // Initialize static buffers
    whitespace_stego_buffers_t buffers;
    if (!whitespace_stego_static_init(&buffers)) {
        printf("Failed to initialize buffers: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    // Test data
    const char* carrier = "Hello, this is a test message! 世界! 🌟🎉";
    const char* message = "This is a secret message hidden in the carrier text.";
    const char* password = "my_secret_password";
    
    printf("Test 1: Encode without password\n");
    printf("Carrier: %s\n", carrier);
    printf("Message: %s\n", message);
    
    size_t encoded_len = 0;
    if (whitespace_stego_static_encode(&buffers, carrier, strlen(carrier), 
                                      message, NULL, &encoded_len)) {
        printf("Encoded successfully! Length: %zu bytes\n", encoded_len);
        printf("Encoded text: %s\n", buffers.encoded);
        
        // Decode
        size_t decoded_len = 0;
        if (whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                          NULL, &decoded_len)) {
            printf("Decoded successfully! Length: %zu bytes\n", decoded_len);
            printf("Decoded message: %s\n", buffers.decoded);
        } else {
            printf("Decode failed: %s\n", whitespace_stego_static_last_error());
        }
    } else {
        printf("Encode failed: %s\n", whitespace_stego_static_last_error());
    }
    
    printf("\nTest 2: Encode with password\n");
    printf("Carrier: %s\n", carrier);
    printf("Message: %s\n", message);
    printf("Password: %s\n", password);
    
    if (whitespace_stego_static_encode(&buffers, carrier, strlen(carrier), 
                                      message, password, &encoded_len)) {
        printf("Encoded successfully! Length: %zu bytes\n", encoded_len);
        printf("Encoded text: %s\n", buffers.encoded);
        
        // Decode with correct password
        size_t decoded_len = 0;
        if (whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                          password, &decoded_len)) {
            printf("Decoded successfully with correct password! Length: %zu bytes\n", decoded_len);
            printf("Decoded message: %s\n", buffers.decoded);
        } else {
            printf("Decode failed: %s\n", whitespace_stego_static_last_error());
        }
        
        // Try to decode with wrong password
        if (whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                          "wrong_password", &decoded_len)) {
            printf("WARNING: Decoded with wrong password! This should not happen.\n");
        } else {
            printf("Correctly rejected wrong password: %s\n", whitespace_stego_static_last_error());
        }
    } else {
        printf("Encode failed: %s\n", whitespace_stego_static_last_error());
    }
    
    printf("\nTest 3: Buffer size validation\n");
    printf("Testing size validation...\n");
    
    if (whitespace_stego_static_validate_size(1024)) {
        printf("✓ 1024 bytes: Valid\n");
    } else {
        printf("✗ 1024 bytes: Invalid\n");
    }
    
    if (whitespace_stego_static_validate_size(whitespace_stego_static_max_size())) {
        printf("✓ Max size (%zu bytes): Valid\n", whitespace_stego_static_max_size());
    } else {
        printf("✗ Max size (%zu bytes): Invalid\n", whitespace_stego_static_max_size());
    }
    
    if (whitespace_stego_static_validate_size(whitespace_stego_static_max_size() + 1)) {
        printf("✗ Max size + 1: Valid (should be invalid)\n");
    } else {
        printf("✓ Max size + 1: Invalid (correct)\n");
    }
    
    printf("\nStatic implementation test completed successfully!\n");
    printf("No memory leaks possible - all memory is statically allocated.\n");
    
    return 0;
} 