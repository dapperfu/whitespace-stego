/*
 * Buffer Size Test for Static Implementations
 * 
 * Tests different buffer sizes to find the largest working size
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Test different buffer sizes
#define TEST_SIZES_COUNT 20
static const size_t test_sizes[TEST_SIZES_COUNT] = {
    1024,        // 1 KiB (known working)
    4096,        // 4 KiB
    16384,       // 16 KiB
    65536,       // 64 KiB
    262144,      // 256 KiB
    1048576,     // 1 MiB
    2097152,     // 2 MiB
    4194304,     // 4 MiB
    8388608,     // 8 MiB
    16777216,    // 16 MiB
    33554432,    // 32 MiB
    67108864,    // 64 MiB
    134217728,   // 128 MiB
    268435456,   // 256 MiB
    536870912,   // 512 MiB
    1073741824,  // 1 GiB
    2147483648,  // 2 GiB
    3221225472,  // 3 GiB
    3758096384,  // 3.5 GiB
    4294967295   // 4 GiB - 1 (max)
};

// Buffer structure with variable size
typedef struct {
    char* carrier;
    char* message;
    char* encoded;
    char* decoded;
    char* temp;
    char* base64;
    unsigned char* crypto_temp;
    size_t buffer_size;
    size_t carrier_len;
    size_t message_len;
    size_t encoded_len;
    size_t decoded_len;
    size_t temp_len;
    size_t base64_len;
    size_t crypto_temp_len;
} test_buffers_t;

// Initialize buffers with given size
int test_init(test_buffers_t* buffers, size_t size) {
    if (!buffers || size == 0) return 0;
    
    // Allocate buffers
    buffers->carrier = malloc(size);
    buffers->message = malloc(size);
    buffers->encoded = malloc(size);
    buffers->decoded = malloc(size);
    buffers->temp = malloc(size);
    buffers->base64 = malloc(size);
    buffers->crypto_temp = malloc(size);
    
    // Check if all allocations succeeded
    if (!buffers->carrier || !buffers->message || !buffers->encoded || 
        !buffers->decoded || !buffers->temp || !buffers->base64 || !buffers->crypto_temp) {
        // Clean up on failure
        free(buffers->carrier);
        free(buffers->message);
        free(buffers->encoded);
        free(buffers->decoded);
        free(buffers->temp);
        free(buffers->base64);
        free(buffers->crypto_temp);
        return 0;
    }
    
    // Initialize
    buffers->buffer_size = size;
    memset(buffers->carrier, 0, size);
    memset(buffers->message, 0, size);
    memset(buffers->encoded, 0, size);
    memset(buffers->decoded, 0, size);
    memset(buffers->temp, 0, size);
    memset(buffers->base64, 0, size);
    memset(buffers->crypto_temp, 0, size);
    
    buffers->carrier_len = 0;
    buffers->message_len = 0;
    buffers->encoded_len = 0;
    buffers->decoded_len = 0;
    buffers->temp_len = 0;
    buffers->base64_len = 0;
    buffers->crypto_temp_len = 0;
    
    return 1;
}

// Clean up buffers
void test_cleanup(test_buffers_t* buffers) {
    if (!buffers) return;
    
    free(buffers->carrier);
    free(buffers->message);
    free(buffers->encoded);
    free(buffers->decoded);
    free(buffers->temp);
    free(buffers->base64);
    free(buffers->crypto_temp);
    
    buffers->carrier = NULL;
    buffers->message = NULL;
    buffers->encoded = NULL;
    buffers->decoded = NULL;
    buffers->temp = NULL;
    buffers->base64 = NULL;
    buffers->crypto_temp = NULL;
}

// Simple base64 encoding (for testing)
int simple_base64_encode(const unsigned char* data, size_t data_len, char* output, size_t output_size) {
    if (!data || !output || data_len == 0) return 0;
    
    const char* base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    size_t i = 0, j = 0;
    
    while (i < data_len && j < output_size - 4) {
        unsigned char b1 = data[i++];
        unsigned char b2 = (i < data_len) ? data[i++] : 0;
        unsigned char b3 = (i < data_len) ? data[i++] : 0;
        
        output[j++] = base64_chars[(b1 >> 2) & 0x3F];
        output[j++] = base64_chars[((b1 & 0x3) << 4) | ((b2 >> 4) & 0xF)];
        output[j++] = base64_chars[((b2 & 0xF) << 2) | ((b3 >> 6) & 0x3)];
        output[j++] = base64_chars[b3 & 0x3F];
    }
    
    output[j] = '\0';
    return 1;
}

// Simple base64 decoding (for testing)
int simple_base64_decode(const char* input, unsigned char* output, size_t output_size, size_t* decoded_len) {
    if (!input || !output || !decoded_len) return 0;
    
    const char* base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    size_t i = 0, j = 0;
    size_t input_len = strlen(input);
    
    while (i < input_len && j < output_size - 3) {
        char c1 = input[i++];
        char c2 = (i < input_len) ? input[i++] : 'A';
        char c3 = (i < input_len) ? input[i++] : 'A';
        char c4 = (i < input_len) ? input[i++] : 'A';
        
        // Find positions in base64 table
        const char* p1 = strchr(base64_chars, c1);
        const char* p2 = strchr(base64_chars, c2);
        const char* p3 = strchr(base64_chars, c3);
        const char* p4 = strchr(base64_chars, c4);
        
        if (!p1 || !p2 || !p3 || !p4) break;
        
        unsigned char b1 = (p1 - base64_chars) << 2 | ((p2 - base64_chars) >> 4);
        unsigned char b2 = ((p2 - base64_chars) & 0xF) << 4 | ((p3 - base64_chars) >> 2);
        unsigned char b3 = ((p3 - base64_chars) & 0x3) << 6 | (p4 - base64_chars);
        
        output[j++] = b1;
        if (c3 != '=') output[j++] = b2;
        if (c4 != '=') output[j++] = b3;
    }
    
    *decoded_len = j;
    return 1;
}

// Simple encode function
int test_encode(test_buffers_t* buffers, const char* carrier, const char* message, const char* password) {
    if (!buffers || !message) return 0;
    
    // For this test, we'll just base64 encode the message and append it
    if (!simple_base64_encode((const unsigned char*)message, strlen(message), 
                             buffers->base64, buffers->buffer_size)) {
        return 0;
    }
    
    // Create encoded text: carrier + " " + base64_message
    snprintf(buffers->encoded, buffers->buffer_size, "%s %s", carrier, buffers->base64);
    buffers->encoded_len = strlen(buffers->encoded);
    
    return 1;
}

// Simple decode function
int test_decode(test_buffers_t* buffers, const char* encoded_text, const char* password) {
    if (!buffers || !encoded_text) return 0;
    
    // Find the last space (separator between carrier and message)
    const char* last_space = strrchr(encoded_text, ' ');
    if (!last_space) return 0;
    
    // Extract the base64 part
    const char* base64_part = last_space + 1;
    
    // Decode base64
    size_t decoded_len = 0;
    if (!simple_base64_decode(base64_part, (unsigned char*)buffers->decoded, 
                             buffers->buffer_size, &decoded_len)) {
        return 0;
    }
    
    buffers->decoded[decoded_len] = '\0';
    buffers->decoded_len = decoded_len;
    
    return 1;
}

// Test a specific buffer size
int test_buffer_size(size_t buffer_size) {
    printf("Testing buffer size: %zu bytes (%.2f MiB)... ", 
           buffer_size, (double)buffer_size / (1024.0 * 1024.0));
    
    test_buffers_t buffers;
    
    // Try to initialize
    if (!test_init(&buffers, buffer_size)) {
        printf("FAILED (allocation failed)\n");
        return 0;
    }
    
    // Test data
    const char* carrier = "Hello, this is a test carrier text.";
    const char* message = "Secret message";
    
    // Test encode/decode
    if (!test_encode(&buffers, carrier, message, NULL)) {
        printf("FAILED (encode failed)\n");
        test_cleanup(&buffers);
        return 0;
    }
    
    if (!test_decode(&buffers, buffers.encoded, NULL)) {
        printf("FAILED (decode failed)\n");
        test_cleanup(&buffers);
        return 0;
    }
    
    if (strcmp(buffers.decoded, message) != 0) {
        printf("FAILED (round-trip failed)\n");
        test_cleanup(&buffers);
        return 0;
    }
    
    test_cleanup(&buffers);
    printf("PASSED\n");
    return 1;
}

int main() {
    printf("=== Buffer Size Test for Static Implementations ===\n\n");
    
    printf("Testing different buffer sizes to find the largest working size...\n\n");
    
    size_t largest_working = 0;
    
    for (int i = 0; i < TEST_SIZES_COUNT; i++) {
        size_t buffer_size = test_sizes[i];
        
        if (test_buffer_size(buffer_size)) {
            largest_working = buffer_size;
        } else {
            printf("Stopping at first failure (buffer size: %zu bytes)\n", buffer_size);
            break;
        }
    }
    
    printf("\n=== Results ===\n");
    if (largest_working > 0) {
        printf("✓ Largest working buffer size: %zu bytes (%.2f MiB)\n", 
               largest_working, (double)largest_working / (1024.0 * 1024.0));
        
        if (largest_working >= 1024 * 1024) {
            printf("✓ This is %.2f GiB\n", (double)largest_working / (1024.0 * 1024.0 * 1024.0));
        }
    } else {
        printf("✗ No working buffer sizes found\n");
    }
    
    printf("\nRecommendation: Use buffer size <= %zu bytes for reliable operation\n", largest_working);
    
    return 0;
} 