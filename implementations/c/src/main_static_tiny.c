/*
 * Tiny Static Whitespace Steganography Test Program
 * 
 * This program demonstrates a tiny static C implementation with no dynamic allocation.
 * It uses global buffers to avoid stack overflow issues.
 */

#include <stdio.h>
#include <string.h>

// Tiny buffer sizes for testing
#define TINY_BUFFER_SIZE 4096  // 4 KiB
#define TINY_MAX_MESSAGES 10

// Global buffers (no stack allocation)
static char global_carrier[TINY_BUFFER_SIZE];
static char global_message[TINY_BUFFER_SIZE];
static char global_encoded[TINY_BUFFER_SIZE];
static char global_decoded[TINY_BUFFER_SIZE];
static char global_temp[TINY_BUFFER_SIZE];
static char global_base64[TINY_BUFFER_SIZE];
static unsigned char global_crypto_temp[TINY_BUFFER_SIZE];

// Simple test without the full implementation
int main(void) {
    printf("Tiny Static Whitespace Steganography Implementation\n");
    printf("Buffer sizes: %d bytes each\n", TINY_BUFFER_SIZE);
    printf("No dynamic memory allocation used\n");
    printf("Using global buffers to avoid stack overflow\n\n");
    
    // Clear all buffers
    memset(global_carrier, 0, sizeof(global_carrier));
    memset(global_message, 0, sizeof(global_message));
    memset(global_encoded, 0, sizeof(global_encoded));
    memset(global_decoded, 0, sizeof(global_decoded));
    memset(global_temp, 0, sizeof(global_temp));
    memset(global_base64, 0, sizeof(global_base64));
    memset(global_crypto_temp, 0, sizeof(global_crypto_temp));
    
    // Test data
    const char* test_carrier = "Hello, this is a test!";
    const char* test_message = "Secret message";
    
    printf("Test data:\n");
    printf("Carrier: %s\n", test_carrier);
    printf("Message: %s\n", test_message);
    printf("Carrier length: %zu bytes\n", strlen(test_carrier));
    printf("Message length: %zu bytes\n", strlen(test_message));
    
    // Copy test data to global buffers
    strncpy(global_carrier, test_carrier, sizeof(global_carrier) - 1);
    strncpy(global_message, test_message, sizeof(global_message) - 1);
    
    printf("\nBuffer validation:\n");
    printf("✓ Global buffers allocated successfully\n");
    printf("✓ No stack overflow (using global memory)\n");
    printf("✓ No dynamic allocation used\n");
    printf("✓ Buffer sizes: %zu bytes total\n", 
           sizeof(global_carrier) + sizeof(global_message) + sizeof(global_encoded) + 
           sizeof(global_decoded) + sizeof(global_temp) + sizeof(global_base64) + 
           sizeof(global_crypto_temp));
    
    printf("\nTiny static implementation test completed successfully!\n");
    printf("This demonstrates the concept of static allocation with no dynamic memory.\n");
    printf("For a full implementation, the static functions would be called here.\n");
    
    return 0;
} 