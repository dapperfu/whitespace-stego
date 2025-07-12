/*
 * Test file for MISRA-compliant static implementation (Fixed Version)
 * Tests that the static implementation works correctly with safe string operations
 * and proper constants instead of magic numbers
 */

#include "../include/whitespace_stego_static.h"
#include "../include/whitespace_stego_static_misra.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static char test_carrier[STATIC_BUFFER_SIZE_BYTES];
static char test_message[STATIC_BUFFER_SIZE_BYTES];
static char test_result[STATIC_BUFFER_SIZE_BYTES];
static char test_decoded[STATIC_BUFFER_SIZE_BYTES];

static int test_count = 0;
static int pass_count = 0;

static void run_test(const char* test_name, int (*test_func)(void)) {
    test_count = test_count + 1;
    printf("Running test: %s\n", test_name);
    
    /* Clear any previous error state */
    whitespace_stego_static_clear_error();
    
    if (test_func()) {
        printf("✅ PASS: %s\n", test_name);
        pass_count = pass_count + 1;
    } else {
        printf("❌ FAIL: %s\n", test_name);
        printf("   Error: %s\n", whitespace_stego_static_last_error());
    }
}

static int test_basic_encode_decode(void) {
    const char* carrier = "Hello World";
    const char* message = "Secret message";
    const char* password = "test123";
    
    /* Test encode */
    if (whitespace_stego_static_encode(carrier, misra_safe_strlen(carrier, STATIC_BUFFER_SIZE_BYTES), 
                                       message, password, test_result, sizeof(test_result)) == 0) {
        return 0;
    }
    
    /* Test decode */
    if (whitespace_stego_static_decode(test_result, misra_safe_strlen(test_result, sizeof(test_result)), 
                                       password, test_decoded, sizeof(test_decoded)) == 0) {
        return 0;
    }
    
    /* Verify result */
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_no_password_encode_decode(void) {
    const char* carrier = "Simple carrier text";
    const char* message = "Unencrypted message";
    
    /* Test encode without password */
    if (whitespace_stego_static_encode(carrier, misra_safe_strlen(carrier, STATIC_BUFFER_SIZE_BYTES), 
                                       message, NULL, test_result, sizeof(test_result)) == 0) {
        return 0;
    }
    
    /* Test decode without password */
    if (whitespace_stego_static_decode(test_result, misra_safe_strlen(test_result, sizeof(test_result)), 
                                       NULL, test_decoded, sizeof(test_decoded)) == 0) {
        return 0;
    }
    
    /* Verify result */
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_empty_carrier(void) {
    const char* message = "Message in empty carrier";
    const char* password = "password";
    
    /* Test encode with empty carrier */
    if (whitespace_stego_static_encode("", 0U, message, password, test_result, sizeof(test_result)) == 0) {
        return 0;
    }
    
    /* Test decode */
    if (whitespace_stego_static_decode(test_result, misra_safe_strlen(test_result, sizeof(test_result)), 
                                       password, test_decoded, sizeof(test_decoded)) == 0) {
        return 0;
    }
    
    /* Verify result */
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_unicode_carrier(void) {
    const char* carrier = "Hello 世界 World 🌍";
    const char* message = "Unicode test message";
    const char* password = "unicode123";
    
    /* Test encode with Unicode carrier */
    if (whitespace_stego_static_encode(carrier, misra_safe_strlen(carrier, STATIC_BUFFER_SIZE_BYTES), 
                                       message, password, test_result, sizeof(test_result)) == 0) {
        return 0;
    }
    
    /* Test decode */
    if (whitespace_stego_static_decode(test_result, misra_safe_strlen(test_result, sizeof(test_result)), 
                                       password, test_decoded, sizeof(test_decoded)) == 0) {
        return 0;
    }
    
    /* Verify result */
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

static int test_error_conditions(void) {
    /* Test with NULL parameters */
    if (whitespace_stego_static_encode(NULL, 0U, "test", NULL, test_result, sizeof(test_result)) != 0) {
        return 0; /* Should fail */
    }
    
    if (whitespace_stego_static_decode(NULL, 0U, NULL, test_decoded, sizeof(test_decoded)) != 0) {
        return 0; /* Should fail */
    }
    
    /* Test with empty message */
    if (whitespace_stego_static_encode("carrier", 7U, "", NULL, test_result, sizeof(test_result)) != 0) {
        return 0; /* Should fail */
    }
    
    return 1;
}

static int test_safe_string_functions(void) {
    char test_buffer[64U];
    size_t result = 0U;
    
    /* Test safe string copy */
    result = misra_safe_strcpy(test_buffer, sizeof(test_buffer), "Hello");
    if (result != 5U) {
        return 0;
    }
    
    /* Test safe string concatenation */
    result = misra_safe_strcat(test_buffer, sizeof(test_buffer), " World");
    if (result != 6U) {
        return 0;
    }
    
    /* Test safe string length */
    result = misra_safe_strlen(test_buffer, sizeof(test_buffer));
    if (result != 11U) {
        return 0;
    }
    
    return 1;
}

static int test_utf8_functions(void) {
    uint8_t ascii_char = 0x41U; /* 'A' */
    uint8_t utf8_2byte = 0xC3U; /* UTF-8 2-byte start */
    uint8_t utf8_3byte = 0xE0U; /* UTF-8 3-byte start */
    uint8_t utf8_4byte = 0xF0U; /* UTF-8 4-byte start */
    
    /* Test UTF-8 character length detection */
    if (misra_utf8_char_length(ascii_char) != UTF8_1BYTE_LENGTH) {
        printf("   DEBUG: ASCII char length test failed\n");
        return 0;
    }
    
    uint8_t result_2byte = misra_utf8_char_length(utf8_2byte);
    printf("   DEBUG: 2-byte test: 0xC3 returned %u, expected %u\n", result_2byte, UTF8_2BYTE_LENGTH);
    if (result_2byte != UTF8_2BYTE_LENGTH) {
        printf("   DEBUG: UTF-8 2-byte length test failed\n");
        return 0;
    }
    
    if (misra_utf8_char_length(utf8_3byte) != UTF8_3BYTE_LENGTH) {
        printf("   DEBUG: UTF-8 3-byte length test failed\n");
        return 0;
    }
    
    if (misra_utf8_char_length(utf8_4byte) != UTF8_4BYTE_LENGTH) {
        printf("   DEBUG: UTF-8 4-byte length test failed\n");
        return 0;
    }
    
    /* Test UTF-8 character validation */
    const char* valid_utf8 = "A"; /* Single ASCII character */
    if (misra_utf8_char_valid(valid_utf8, 1U) != 1) {
        printf("   DEBUG: UTF-8 validation test failed\n");
        return 0;
    }
    
    return 1;
}

static int test_bit_manipulation(void) {
    uint8_t test_byte = 0xAAU; /* 10101010 */
    uint8_t bit_value = 0U;
    uint8_t modified_byte = 0U;
    
    /* Test bit extraction */
    bit_value = misra_extract_bit(test_byte, 0U);
    if (bit_value != 0U) {
        return 0;
    }
    
    bit_value = misra_extract_bit(test_byte, 1U);
    if (bit_value != 1U) {
        return 0;
    }
    
    /* Test bit setting */
    modified_byte = misra_set_bit(test_byte, 0U, 1U);
    if (misra_extract_bit(modified_byte, 0U) != 1U) {
        return 0;
    }
    
    modified_byte = misra_set_bit(test_byte, 1U, 0U);
    if (misra_extract_bit(modified_byte, 1U) != 0U) {
        return 0;
    }
    
    return 1;
}

static int test_logging_system(void) {
    /* Test MISRA-compliant logging */
    whitespace_stego_static_set_log_level(LOG_LEVEL_DEBUG);
    whitespace_stego_static_log(LOG_LEVEL_INFO, "Test log message");
    whitespace_stego_static_log(LOG_LEVEL_DEBUG, "Debug message: %d", 42);
    
    /* Test that logging doesn't interfere with functionality */
    const char* carrier = "Test carrier";
    const char* message = "Test message";
    
    if (whitespace_stego_static_encode(carrier, misra_safe_strlen(carrier, STATIC_BUFFER_SIZE_BYTES), 
                                       message, NULL, test_result, sizeof(test_result)) == 0) {
        return 0;
    }
    
    if (whitespace_stego_static_decode(test_result, misra_safe_strlen(test_result, sizeof(test_result)), 
                                       NULL, test_decoded, sizeof(test_decoded)) == 0) {
        return 0;
    }
    
    if (strcmp(message, test_decoded) != 0) {
        return 0;
    }
    
    return 1;
}

int main(void) {
    printf("=== MISRA-Compliant Static Implementation Test (Fixed) ===\n\n");
    
    /* Run all tests */
    run_test("Basic encode/decode with password", test_basic_encode_decode);
    run_test("Encode/decode without password", test_no_password_encode_decode);
    run_test("Empty carrier test", test_empty_carrier);
    run_test("Unicode carrier test", test_unicode_carrier);
    run_test("Error condition tests", test_error_conditions);
    run_test("Safe string function tests", test_safe_string_functions);
    run_test("UTF-8 function tests", test_utf8_functions);
    run_test("Bit manipulation tests", test_bit_manipulation);
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