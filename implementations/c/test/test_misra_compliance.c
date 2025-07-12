/*
 * Test file for MISRA-compliant static implementation
 * Tests that the static implementation works correctly without printf statements
 */

#include "../include/whitespace_stego_static.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TEST_BUFFER_SIZE (1024 * 1024)
#define MAX_MESSAGE_SIZE (1024 * 1024)

static char test_carrier[TEST_BUFFER_SIZE];
static char test_message[TEST_BUFFER_SIZE];
static char test_result[TEST_BUFFER_SIZE];
static char test_decoded[TEST_BUFFER_SIZE];

static int test_count = 0;
static int pass_count = 0;

static void run_test(const char* test_name, int (*test_func)(void)) {
    test_count++;
    printf("Running test: %s\n", test_name);
    
    if (test_func()) {
        printf("✅ PASS: %s\n", test_name);
        pass_count++;
    } else {
        printf("❌ FAIL: %s\n", test_name);
        printf("   Error: %s\n", whitespace_stego_static_last_error());
    }
}

static int test_basic_encode_decode(void) {
    const char* carrier = "Hello World";
    const char* message = "Secret message";
    const char* password = "test123";
    
    // Test encode
    if (!whitespace_stego_static_encode(carrier, strlen(carrier), message, 
                                       password, test_result, sizeof(test_result))) {
        return 0;
    }
    
    // Test decode
    if (!whitespace_stego_static_decode(test_result, strlen(test_result), 
                                       password, test_decoded, sizeof(test_decoded))) {
        return 0;
    }
    
    // Verify result
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_no_password_encode_decode(void) {
    const char* carrier = "Simple carrier text";
    const char* message = "Unencrypted message";
    
    // Test encode without password
    if (!whitespace_stego_static_encode(carrier, strlen(carrier), message, 
                                       NULL, test_result, sizeof(test_result))) {
        return 0;
    }
    
    // Test decode without password
    if (!whitespace_stego_static_decode(test_result, strlen(test_result), 
                                       NULL, test_decoded, sizeof(test_decoded))) {
        return 0;
    }
    
    // Verify result
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_empty_carrier(void) {
    const char* message = "Message in empty carrier";
    const char* password = "password";
    
    // Test encode with empty carrier
    if (!whitespace_stego_static_encode("", 0, message, 
                                       password, test_result, sizeof(test_result))) {
        return 0;
    }
    
    // Test decode
    if (!whitespace_stego_static_decode(test_result, strlen(test_result), 
                                       password, test_decoded, sizeof(test_decoded))) {
        return 0;
    }
    
    // Verify result
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_unicode_carrier(void) {
    const char* carrier = "Hello 世界 World 🌍";
    const char* message = "Unicode test message";
    const char* password = "unicode123";
    
    // Test encode with Unicode carrier
    if (!whitespace_stego_static_encode(carrier, strlen(carrier), message, 
                                       password, test_result, sizeof(test_result))) {
        return 0;
    }
    
    // Test decode
    if (!whitespace_stego_static_decode(test_result, strlen(test_result), 
                                       password, test_decoded, sizeof(test_decoded))) {
        return 0;
    }
    
    // Verify result
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_error_conditions(void) {
    // Test with NULL parameters
    if (whitespace_stego_static_encode(NULL, 0, "test", NULL, test_result, sizeof(test_result))) {
        return 0; // Should fail
    }
    
    if (whitespace_stego_static_decode(NULL, 0, NULL, test_decoded, sizeof(test_decoded))) {
        return 0; // Should fail
    }
    
    // Test with empty message
    if (whitespace_stego_static_encode("carrier", 7, "", NULL, test_result, sizeof(test_result))) {
        return 0; // Should fail
    }
    
    return 1;
}

static int test_logging_system(void) {
    // Test MISRA-compliant logging
    whitespace_stego_static_set_log_level(LOG_LEVEL_DEBUG);
    whitespace_stego_static_log(LOG_LEVEL_INFO, "Test log message");
    whitespace_stego_static_log(LOG_LEVEL_DEBUG, "Debug message: %d", 42);
    
    // Test that logging doesn't interfere with functionality
    const char* carrier = "Test carrier";
    const char* message = "Test message";
    
    if (!whitespace_stego_static_encode(carrier, strlen(carrier), message, 
                                       NULL, test_result, sizeof(test_result))) {
        return 0;
    }
    
    if (!whitespace_stego_static_decode(test_result, strlen(test_result), 
                                       NULL, test_decoded, sizeof(test_decoded))) {
        return 0;
    }
    
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

int main(void) {
    printf("=== MISRA-Compliant Static Implementation Test ===\n\n");
    
    // Run all tests
    run_test("Basic encode/decode with password", test_basic_encode_decode);
    run_test("Encode/decode without password", test_no_password_encode_decode);
    run_test("Empty carrier test", test_empty_carrier);
    run_test("Unicode carrier test", test_unicode_carrier);
    run_test("Error condition tests", test_error_conditions);
    run_test("MISRA-compliant logging system", test_logging_system);
    
    printf("\n=== Test Summary ===\n");
    printf("Total tests: %d\n", test_count);
    printf("Passed: %d\n", pass_count);
    printf("Failed: %d\n", test_count - pass_count);
    printf("Success rate: %.1f%%\n", (double)pass_count / test_count * 100.0);
    
    if (pass_count == test_count) {
        printf("\n🎉 All MISRA compliance tests passed!\n");
        return 0;
    } else {
        printf("\n❌ Some tests failed!\n");
        return 1;
    }
} 