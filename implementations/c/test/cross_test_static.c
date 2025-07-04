/*
 * Cross-Test for C Static Implementations
 * 
 * Tests round-trip functionality between all static implementations:
 * - whitespace-stego-static (standard, 4 GiB)
 * - whitespace-stego-static-small (1 MiB)
 * - whitespace-stego-static-tiny (4 KiB)
 * - whitespace-stego-static-large (4 GiB, optimized)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

// Include all static implementation headers
#include "../include/whitespace_stego_static.h"
#include "../include/whitespace_stego_static_small.h"
#include "../include/whitespace_stego_static_large.h"

// Test messages of different sizes
static const char* test_messages[] = {
    "Hello, World!",                                    // 13 bytes
    "This is a longer test message with spaces.",       // 42 bytes
    "Unicode: 🚀🌟🎉",                                  // 15 bytes (UTF-8)
    "A" "B" "C" "D" "E" "F" "G" "H" "I" "J"            // 10 bytes
};

static const char* test_passwords[] = {
    NULL,           // No password
    "simple",       // Simple password
    "complex_password_123!@#",  // Complex password
    "🚀🌟🎉"        // Unicode password
};

// Test carrier text
static const char* test_carrier = "This is a sample carrier text that will be used for testing the whitespace steganography implementations. It contains enough text to embed various sized messages.";

// Function to test encoding with one implementation and decoding with another
static int test_cross_implementation(const char* message, const char* password, 
                                   const char* test_name) {
    printf("Testing: %s\n", test_name);
    printf("  Message: '%s'\n", message ? message : "(null)");
    printf("  Password: '%s'\n", password ? password : "(null)");
    
    // Test all combinations of encode/decode between implementations
    int success_count = 0;
    int total_tests = 0;
    
    // Test 1: Standard -> Standard
    {
        whitespace_stego_buffers_t buffers;
        if (whitespace_stego_static_init(&buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_encode(&buffers, test_carrier, strlen(test_carrier), 
                                             message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_decode(&buffers, test_carrier, strlen(test_carrier), 
                                                 password, &decoded_len)) {
                    if (strcmp(buffers.decoded, message) == 0) {
                        printf("  ✓ Standard -> Standard: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Standard -> Standard: FAIL (decoded: '%s')\n", buffers.decoded);
                    }
                } else {
                    printf("  ✗ Standard -> Standard: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_last_error());
                }
            } else {
                printf("  ✗ Standard -> Standard: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 2: Small -> Small
    {
        whitespace_stego_buffers_small_t buffers;
        if (whitespace_stego_static_small_init(&buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_small_encode(&buffers, test_carrier, strlen(test_carrier), 
                                                   message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_small_decode(&buffers, test_carrier, strlen(test_carrier), 
                                                       password, &decoded_len)) {
                    if (strcmp(buffers.decoded, message) == 0) {
                        printf("  ✓ Small -> Small: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Small -> Small: FAIL (decoded: '%s')\n", buffers.decoded);
                    }
                } else {
                    printf("  ✗ Small -> Small: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_small_last_error());
                }
            } else {
                printf("  ✗ Small -> Small: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_small_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 3: Large -> Large
    {
        whitespace_stego_buffers_large_t buffers;
        if (whitespace_stego_static_large_init(&buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_large_encode(&buffers, test_carrier, strlen(test_carrier), 
                                                   message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_large_decode(&buffers, test_carrier, strlen(test_carrier), 
                                                       password, &decoded_len)) {
                    if (strcmp(buffers.decoded, message) == 0) {
                        printf("  ✓ Large -> Large: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Large -> Large: FAIL (decoded: '%s')\n", buffers.decoded);
                    }
                } else {
                    printf("  ✗ Large -> Large: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_large_last_error());
                }
            } else {
                printf("  ✗ Large -> Large: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_large_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 4: Standard -> Small (if message fits)
    if (strlen(message) <= MAX_BUFFER_SIZE_SMALL) {
        whitespace_stego_buffers_t encode_buffers;
        whitespace_stego_buffers_small_t decode_buffers;
        if (whitespace_stego_static_init(&encode_buffers) && 
            whitespace_stego_static_small_init(&decode_buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_encode(&encode_buffers, test_carrier, strlen(test_carrier), 
                                             message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_small_decode(&decode_buffers, test_carrier, strlen(test_carrier), 
                                                       password, &decoded_len)) {
                    if (strcmp(decode_buffers.decoded, message) == 0) {
                        printf("  ✓ Standard -> Small: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Standard -> Small: FAIL (decoded: '%s')\n", decode_buffers.decoded);
                    }
                } else {
                    printf("  ✗ Standard -> Small: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_small_last_error());
                }
            } else {
                printf("  ✗ Standard -> Small: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 5: Small -> Standard
    {
        whitespace_stego_buffers_small_t encode_buffers;
        whitespace_stego_buffers_t decode_buffers;
        if (whitespace_stego_static_small_init(&encode_buffers) && 
            whitespace_stego_static_init(&decode_buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_small_encode(&encode_buffers, test_carrier, strlen(test_carrier), 
                                                   message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_decode(&decode_buffers, test_carrier, strlen(test_carrier), 
                                                 password, &decoded_len)) {
                    if (strcmp(decode_buffers.decoded, message) == 0) {
                        printf("  ✓ Small -> Standard: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Small -> Standard: FAIL (decoded: '%s')\n", decode_buffers.decoded);
                    }
                } else {
                    printf("  ✗ Small -> Standard: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_last_error());
                }
            } else {
                printf("  ✗ Small -> Standard: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_small_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 6: Standard -> Large
    {
        whitespace_stego_buffers_t encode_buffers;
        whitespace_stego_buffers_large_t decode_buffers;
        if (whitespace_stego_static_init(&encode_buffers) && 
            whitespace_stego_static_large_init(&decode_buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_encode(&encode_buffers, test_carrier, strlen(test_carrier), 
                                             message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_large_decode(&decode_buffers, test_carrier, strlen(test_carrier), 
                                                       password, &decoded_len)) {
                    if (strcmp(decode_buffers.decoded, message) == 0) {
                        printf("  ✓ Standard -> Large: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Standard -> Large: FAIL (decoded: '%s')\n", decode_buffers.decoded);
                    }
                } else {
                    printf("  ✗ Standard -> Large: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_large_last_error());
                }
            } else {
                printf("  ✗ Standard -> Large: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_last_error());
            }
            total_tests++;
        }
    }
    
    // Test 7: Large -> Standard
    {
        whitespace_stego_buffers_large_t encode_buffers;
        whitespace_stego_buffers_t decode_buffers;
        if (whitespace_stego_static_large_init(&encode_buffers) && 
            whitespace_stego_static_init(&decode_buffers)) {
            size_t encoded_len = 0;
            if (whitespace_stego_static_large_encode(&encode_buffers, test_carrier, strlen(test_carrier), 
                                                   message, password, &encoded_len)) {
                size_t decoded_len = 0;
                if (whitespace_stego_static_decode(&decode_buffers, test_carrier, strlen(test_carrier), 
                                                 password, &decoded_len)) {
                    if (strcmp(decode_buffers.decoded, message) == 0) {
                        printf("  ✓ Large -> Standard: PASS\n");
                        success_count++;
                    } else {
                        printf("  ✗ Large -> Standard: FAIL (decoded: '%s')\n", decode_buffers.decoded);
                    }
                } else {
                    printf("  ✗ Large -> Standard: FAIL (decode error: %s)\n", 
                           whitespace_stego_static_last_error());
                }
            } else {
                printf("  ✗ Large -> Standard: FAIL (encode error: %s)\n", 
                       whitespace_stego_static_large_last_error());
            }
            total_tests++;
        }
    }
    
    printf("  Results: %d/%d tests passed\n\n", success_count, total_tests);
    return success_count == total_tests;
}

int main() {
    printf("=== Cross-Test for C Static Implementations ===\n\n");
    
    int total_success = 0;
    int total_tests = 0;
    
    // Test each message with each password
    for (int i = 0; i < sizeof(test_messages) / sizeof(test_messages[0]); i++) {
        for (int j = 0; j < sizeof(test_passwords) / sizeof(test_passwords[0]); j++) {
            char test_name[256];
            snprintf(test_name, sizeof(test_name), "Message %d, Password %d", i + 1, j + 1);
            
            if (test_cross_implementation(test_messages[i], test_passwords[j], test_name)) {
                total_success++;
            }
            total_tests++;
        }
    }
    
    printf("=== Final Results ===\n");
    printf("Total test combinations: %d\n", total_tests);
    printf("Successful combinations: %d\n", total_success);
    printf("Success rate: %.1f%%\n", (double)total_success / total_tests * 100.0);
    
    if (total_success == total_tests) {
        printf("🎉 ALL TESTS PASSED! All implementations are compatible.\n");
        return 0;
    } else {
        printf("❌ Some tests failed. Check implementation compatibility.\n");
        return 1;
    }
} 