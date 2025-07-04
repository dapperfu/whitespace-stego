/*
 * Static Buffer Size Test for Static Implementations
 * 
 * Tests different buffer sizes using ONLY static allocation (no malloc)
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Test different buffer sizes for static allocation
#define TEST_SIZES_COUNT 25
static const size_t test_sizes[TEST_SIZES_COUNT] = {
    1024,        // 1 KiB (known working)
    4096,        // 4 KiB
    16384,       // 16 KiB
    65536,       // 64 KiB
    131072,      // 128 KiB
    262144,      // 256 KiB
    524288,      // 512 KiB
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
    4026531840,  // 3.75 GiB
    4194304000,  // 3.9 GiB
    4294967295   // 4 GiB - 1 (max)
};

// Static buffer structure with variable size
typedef struct {
    char carrier[4294967295];  // Largest test size (4 GiB - 1)
    char message[4294967295];
    char encoded[4294967295];
    char decoded[4294967295];
    char temp[4294967295];
    char base64[4294967295];
    unsigned char crypto_temp[4294967295];
    size_t buffer_size;
    size_t carrier_len;
    size_t message_len;
    size_t encoded_len;
    size_t decoded_len;
    size_t temp_len;
    size_t base64_len;
    size_t crypto_temp_len;
} static_test_buffers_t;

// Global buffer (avoid stack allocation)
static static_test_buffers_t global_buffers;

// Initialize buffers with given size
int static_test_init(size_t size) {
    if (size > sizeof(global_buffers.carrier)) {
        return 0;  // Size too large
    }
    
    // Clear all buffers
    memset(&global_buffers, 0, sizeof(global_buffers));
    
    // Set buffer size
    global_buffers.buffer_size = size;
    
    return 1;
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
int static_test_encode(const char* carrier, const char* message, const char* password) {
    if (!message) return 0;
    
    // For this test, we'll just base64 encode the message and append it
    if (!simple_base64_encode((const unsigned char*)message, strlen(message), 
                             global_buffers.base64, global_buffers.buffer_size)) {
        return 0;
    }
    
    // Create encoded text: carrier + " " + base64_message
    snprintf(global_buffers.encoded, global_buffers.buffer_size, "%s %s", carrier, global_buffers.base64);
    global_buffers.encoded_len = strlen(global_buffers.encoded);
    
    return 1;
}

// Simple decode function
int static_test_decode(const char* encoded_text, const char* password) {
    if (!encoded_text) return 0;
    
    // Find the last space (separator between carrier and message)
    const char* last_space = strrchr(encoded_text, ' ');
    if (!last_space) return 0;
    
    // Extract the base64 part
    const char* base64_part = last_space + 1;
    
    // Decode base64
    size_t decoded_len = 0;
    if (!simple_base64_decode(base64_part, (unsigned char*)global_buffers.decoded, 
                             global_buffers.buffer_size, &decoded_len)) {
        return 0;
    }
    
    global_buffers.decoded[decoded_len] = '\0';
    global_buffers.decoded_len = decoded_len;
    
    return 1;
}

// Test a specific buffer size
int test_static_buffer_size(size_t buffer_size) {
    printf("Testing static buffer size: %zu bytes (%.2f MiB)... ", 
           buffer_size, (double)buffer_size / (1024.0 * 1024.0));
    
    // Try to initialize
    if (!static_test_init(buffer_size)) {
        printf("FAILED (size too large for static allocation)\n");
        return 0;
    }
    
    // Test data
    const char* carrier = "Hello, this is a test carrier text.";
    const char* message = "Secret message";
    
    // Test encode/decode
    if (!static_test_encode(carrier, message, NULL)) {
        printf("FAILED (encode failed)\n");
        return 0;
    }
    
    if (!static_test_decode(global_buffers.encoded, NULL)) {
        printf("FAILED (decode failed)\n");
        return 0;
    }
    
    if (strcmp(global_buffers.decoded, message) != 0) {
        printf("FAILED (round-trip failed)\n");
        return 0;
    }
    
    printf("PASSED\n");
    return 1;
}

int main() {
    printf("=== Static Buffer Size Test (No malloc) ===\n\n");
    
    printf("Testing different buffer sizes using ONLY static allocation...\n");
    printf("Total static memory used: %.2f MiB\n\n", 
           (double)sizeof(global_buffers) / (1024.0 * 1024.0));
    
    size_t largest_working = 0;
    
    for (int i = 0; i < TEST_SIZES_COUNT; i++) {
        size_t buffer_size = test_sizes[i];
        
        if (test_static_buffer_size(buffer_size)) {
            largest_working = buffer_size;
        } else {
            printf("Stopping at first failure (buffer size: %zu bytes)\n", buffer_size);
            break;
        }
    }
    
    printf("\n=== Results ===\n");
    if (largest_working > 0) {
        printf("✓ Largest working static buffer size: %zu bytes (%.2f MiB)\n", 
               largest_working, (double)largest_working / (1024.0 * 1024.0));
        
        if (largest_working >= 1024 * 1024) {
            printf("✓ This is %.2f GiB\n", (double)largest_working / (1024.0 * 1024.0 * 1024.0));
        }
    } else {
        printf("✗ No working static buffer sizes found\n");
    }
    
    printf("\nRecommendation: Use static buffer size <= %zu bytes for reliable operation\n", largest_working);
    printf("Note: This uses ONLY static allocation - no malloc/free\n");
    
    return 0;
} 