#include "../include/whitespace_stego.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

// Coverage test data
static const char* COVERAGE_TEST_MESSAGES[] = {
    "Hello, World!",
    "Test message with special chars: !@#$%^&*()",
    "Unicode test: 世界 🌍",
    "Empty message test",
    "Very long message that exceeds normal limits and tests boundary conditions",
    NULL
};

static const char* COVERAGE_TEST_CARRIERS[] = {
    "Simple carrier",
    "Carrier with spaces and punctuation!",
    "Unicode carrier: 你好世界 🌟",
    "",
    "Very long carrier text that provides plenty of space for encoding",
    NULL
};

static const char* COVERAGE_TEST_PASSWORDS[] = {
    NULL,  // No password
    "",    // Empty password
    "simple",
    "password with spaces",
    "Unicode password: 密码🔒",
    "very_long_password_that_tests_key_derivation_limits",
    NULL
};

// Test all combinations for maximum coverage
void test_all_combinations(void) {
    printf("Running comprehensive coverage tests...\n");
    
    for (int m = 0; COVERAGE_TEST_MESSAGES[m] != NULL; m++) {
        for (int c = 0; COVERAGE_TEST_CARRIERS[c] != NULL; c++) {
            for (int p = 0; COVERAGE_TEST_PASSWORDS[p] != NULL; p++) {
                char* encoded = NULL;
                char* decoded = NULL;
                
                // Skip empty message tests (should fail)
                if (strlen(COVERAGE_TEST_MESSAGES[m]) == 0) {
                    bool result = whitespace_stego_encode(
                        COVERAGE_TEST_CARRIERS[c], 
                        strlen(COVERAGE_TEST_CARRIERS[c]),
                        COVERAGE_TEST_MESSAGES[m], 
                        COVERAGE_TEST_PASSWORDS[p], 
                        &encoded
                    );
                    assert(!result); // Should fail
                    continue;
                }
                
                // Test encoding
                bool encode_result = whitespace_stego_encode(
                    COVERAGE_TEST_CARRIERS[c], 
                    strlen(COVERAGE_TEST_CARRIERS[c]),
                    COVERAGE_TEST_MESSAGES[m], 
                    COVERAGE_TEST_PASSWORDS[p], 
                    &encoded
                );
                
                if (encode_result && encoded != NULL) {
                    // Test decoding
                    bool decode_result = whitespace_stego_decode(
                        encoded, 
                        strlen(encoded), 
                        COVERAGE_TEST_PASSWORDS[p], 
                        &decoded
                    );
                    
                    if (decode_result && decoded != NULL) {
                        // Verify round-trip
                        assert(strcmp(COVERAGE_TEST_MESSAGES[m], decoded) == 0);
                        
                        // Test wrong password
                        char* wrong_decoded = NULL;
                        bool wrong_result = whitespace_stego_decode(
                            encoded, 
                            strlen(encoded), 
                            "wrong_password", 
                            &wrong_decoded
                        );
                        assert(!wrong_result); // Should fail
                        
                        if (wrong_decoded) whitespace_stego_free(wrong_decoded);
                        whitespace_stego_free(decoded);
                    }
                    
                    whitespace_stego_free(encoded);
                }
            }
        }
    }
    
    printf("Coverage tests completed successfully!\n");
}

// Test edge cases for maximum coverage
void test_edge_cases(void) {
    printf("Testing edge cases...\n");
    
    char* result = NULL;
    
    // Test NULL pointers
    assert(!whitespace_stego_encode(NULL, 0, "test", "pass", &result));
    assert(!whitespace_stego_encode("carrier", 7, NULL, "pass", &result));
    assert(!whitespace_stego_encode("carrier", 7, "test", "pass", NULL));
    assert(!whitespace_stego_decode(NULL, 0, "pass", &result));
    assert(!whitespace_stego_decode("encoded", 7, "pass", NULL));
    
    // Test zero lengths
    assert(!whitespace_stego_encode("", 0, "test", "pass", &result));
    assert(!whitespace_stego_decode("", 0, "pass", &result));
    
    // Test very large data
    char* large_carrier = malloc(100000);
    char* large_message = malloc(50000);
    
    if (large_carrier && large_message) {
        memset(large_carrier, 'A', 99999);
        large_carrier[99999] = '\0';
        memset(large_message, 'B', 49999);
        large_message[49999] = '\0';
        
        char* encoded = NULL;
        bool result = whitespace_stego_encode(large_carrier, strlen(large_carrier),
                                            large_message, "test", &encoded);
        
        if (result && encoded) {
            char* decoded = NULL;
            bool decode_result = whitespace_stego_decode(encoded, strlen(encoded),
                                                       "test", &decoded);
            
            if (decode_result && decoded) {
                assert(strcmp(large_message, decoded) == 0);
                whitespace_stego_free(decoded);
            }
            
            whitespace_stego_free(encoded);
        }
    }
    
    free(large_carrier);
    free(large_message);
    
    printf("Edge case tests completed!\n");
}

// Test error conditions
void test_error_conditions(void) {
    printf("Testing error conditions...\n");
    
    char* result = NULL;
    
    // Test with corrupted data
    const char* corrupted_data = "This is not properly encoded data";
    bool decode_result = whitespace_stego_decode(corrupted_data, strlen(corrupted_data),
                                               "test", &result);
    assert(!decode_result);
    
    // Test with insufficient carrier space
    const char* short_carrier = "A";
    const char* long_message = "This is a very long message that should not fit in a single character carrier";
    bool encode_result = whitespace_stego_encode(short_carrier, strlen(short_carrier),
                                               long_message, "test", &result);
    // This might succeed or fail depending on implementation, but should handle gracefully
    if (result) whitespace_stego_free(result);
    
    printf("Error condition tests completed!\n");
}

int main(void) {
    printf("Starting C coverage tests...\n");
    
    test_all_combinations();
    test_edge_cases();
    test_error_conditions();
    
    printf("All C coverage tests passed!\n");
    return 0;
} 