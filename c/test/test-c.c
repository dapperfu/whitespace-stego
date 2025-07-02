#include "../include/whitespace_stego.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>

// Test data definitions
static const char* EMPTY_MESSAGE = "";
static const char* SHORT_MESSAGE = "Hello";
static const char* LONG_MESSAGE = "This is a much longer message that contains multiple words and should test the encoding and decoding capabilities thoroughly. It includes various characters and punctuation marks!";

static const char* EMPTY_CARRIER = "";
static const char* SHORT_CARRIER = "Hi";
static const char* LONG_CARRIER = "This is a longer carrier text that provides more space for encoding messages. It contains multiple sentences and various punctuation marks.";

static const char* EMPTY_PASSWORD = "";
static const char* SHORT_PASSWORD = "pass";
static const char* LONG_PASSWORD = "this_is_a_very_long_password_for_testing";

// Unicode and Emoji test data
static const char* UNICODE_MESSAGE = "Hello, 世界! 🌍";
static const char* EMOJI_MESSAGE = "🚀🚁🚂🚃🚄🚅🚆🚇🚈🚉🚊🚋🚌🚍🚎🚏";
static const char* MIXED_UNICODE_MESSAGE = "Hello 世界! 🌍🚀 Test 123";

static const char* UNICODE_CARRIER = "你好世界! 🌟";
static const char* EMOJI_CARRIER = "🎉🎊🎋🎌🎍🎎🎏🎐🎑🎒🎓🎔🎕🎖🎗🎘";
static const char* MIXED_UNICODE_CARRIER = "Hello 世界! 🌟🎉 Test 456";

// Test counters
static int tests_run = 0;
static int tests_passed = 0;
static int tests_failed = 0;

// Test result tracking
static void test_result(bool passed, const char* test_name) {
    tests_run++;
    if (passed) {
        tests_passed++;
        printf("✅ PASS: %s\n", test_name);
    } else {
        tests_failed++;
        printf("❌ FAIL: %s\n", test_name);
    }
}

// Helper function to compare strings safely
static bool strings_equal(const char* a, const char* b) {
    if (a == NULL && b == NULL) return true;
    if (a == NULL || b == NULL) return false;
    return strcmp(a, b) == 0;
}

// Helper function to get string length safely
static size_t safe_strlen(const char* str) {
    return str ? strlen(str) : 0;
}

// Test function for round-trip encoding/decoding
static bool test_roundtrip(const char* message, const char* carrier, const char* password, const char* test_name) {
    char* encoded = NULL;
    char* decoded = NULL;
    bool success = false;
    
    // Encode
    bool encode_success = whitespace_stego_encode(carrier, safe_strlen(carrier), message, password, &encoded);
    
    if (!encode_success) {
        printf("    Encode failed: %s\n", whitespace_stego_last_error());
        goto cleanup;
    }
    
    // Decode
    bool decode_success = whitespace_stego_decode(encoded, strlen(encoded), password, &decoded);
    
    if (!decode_success) {
        printf("    Decode failed: %s\n", whitespace_stego_last_error());
        goto cleanup;
    }
    
    // Compare
    if (!strings_equal(message, decoded)) {
        printf("    Message mismatch!\n");
        printf("    Expected: '%s'\n", message);
        printf("    Got:      '%s'\n", decoded);
        goto cleanup;
    }
    
    success = true;
    
cleanup:
    if (encoded) whitespace_stego_free(encoded);
    if (decoded) whitespace_stego_free(decoded);
    return success;
}

// Test empty message (should fail)
static bool test_empty_message(const char* carrier, const char* password, const char* test_name) {
    char* encoded = NULL;
    bool success = false;
    
    // Encode should fail for empty message
    bool encode_success = whitespace_stego_encode(carrier, safe_strlen(carrier), EMPTY_MESSAGE, password, &encoded);
    
    if (encode_success) {
        printf("    Encode succeeded with empty message (should fail)\n");
        goto cleanup;
    }
    
    success = true;
    
cleanup:
    if (encoded) whitespace_stego_free(encoded);
    return success;
}

// Test wrong password
static bool test_wrong_password(const char* message, const char* carrier, const char* password, const char* test_name) {
    char* encoded = NULL;
    char* decoded = NULL;
    bool success = false;
    
    // Encode with correct password
    bool encode_success = whitespace_stego_encode(carrier, safe_strlen(carrier), message, password, &encoded);
    
    if (!encode_success) {
        printf("    Encode failed: %s\n", whitespace_stego_last_error());
        goto cleanup;
    }
    
    // Decode with wrong password
    const char* wrong_password = "wrong_password_123";
    bool decode_success = whitespace_stego_decode(encoded, strlen(encoded), wrong_password, &decoded);
    
    if (decode_success) {
        printf("    Decode succeeded with wrong password (should fail)\n");
        goto cleanup;
    }
    
    success = true;
    
cleanup:
    if (encoded) whitespace_stego_free(encoded);
    if (decoded) whitespace_stego_free(decoded);
    return success;
}

// Test all permutations
static void run_all_permutation_tests(void) {
    printf("\n=== Running All Permutation Tests ===\n");
    
    const char* messages[] = {SHORT_MESSAGE, LONG_MESSAGE, UNICODE_MESSAGE, EMOJI_MESSAGE, MIXED_UNICODE_MESSAGE};
    const char* carriers[] = {EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER, UNICODE_CARRIER, EMOJI_CARRIER, MIXED_UNICODE_CARRIER};
    const char* passwords[] = {EMPTY_PASSWORD, SHORT_PASSWORD, LONG_PASSWORD};
    
    const char* message_names[] = {"SHORT", "LONG", "UNICODE", "EMOJI", "MIXED_UNICODE"};
    const char* carrier_names[] = {"EMPTY", "SHORT", "LONG", "UNICODE", "EMOJI", "MIXED_UNICODE"};
    const char* password_names[] = {"EMPTY", "SHORT", "LONG"};
    
    int total_tests = 0;
    int permutation_tests = 0;
    
    // Test all valid permutations
    for (int m = 0; m < 5; m++) {  // Skip empty message
        for (int c = 0; c < 6; c++) {
            for (int p = 0; p < 3; p++) {
                char test_name[256];
                snprintf(test_name, sizeof(test_name), "Roundtrip_%s_%s_%s", 
                        message_names[m], carrier_names[c], password_names[p]);
                
                bool result = test_roundtrip(messages[m], carriers[c], passwords[p], test_name);
                test_result(result, test_name);
                total_tests++;
                if (result) permutation_tests++;
            }
        }
    }
    
    printf("\nPermutation Test Summary: %d/%d passed\n", permutation_tests, total_tests);
}

// Test empty message scenarios
static void run_empty_message_tests(void) {
    printf("\n=== Running Empty Message Tests ===\n");
    
    const char* carriers[] = {EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER, UNICODE_CARRIER, EMOJI_CARRIER, MIXED_UNICODE_CARRIER};
    const char* passwords[] = {EMPTY_PASSWORD, SHORT_PASSWORD, LONG_PASSWORD};
    const char* carrier_names[] = {"EMPTY", "SHORT", "LONG", "UNICODE", "EMOJI", "MIXED_UNICODE"};
    const char* password_names[] = {"EMPTY", "SHORT", "LONG"};
    
    int total_tests = 0;
    int empty_tests = 0;
    
    for (int c = 0; c < 6; c++) {
        for (int p = 0; p < 3; p++) {
            char test_name[256];
            snprintf(test_name, sizeof(test_name), "EmptyMessage_%s_%s", 
                    carrier_names[c], password_names[p]);
            
            bool result = test_empty_message(carriers[c], passwords[p], test_name);
            test_result(result, test_name);
            total_tests++;
            if (result) empty_tests++;
        }
    }
    
    printf("\nEmpty Message Test Summary: %d/%d passed\n", empty_tests, total_tests);
}

// Test wrong password scenarios
static void run_wrong_password_tests(void) {
    printf("\n=== Running Wrong Password Tests ===\n");
    
    const char* messages[] = {SHORT_MESSAGE, LONG_MESSAGE, UNICODE_MESSAGE, EMOJI_MESSAGE, MIXED_UNICODE_MESSAGE};
    const char* carriers[] = {EMPTY_CARRIER, SHORT_CARRIER, LONG_CARRIER, UNICODE_CARRIER, EMOJI_CARRIER, MIXED_UNICODE_CARRIER};
    const char* passwords[] = {SHORT_PASSWORD, LONG_PASSWORD};  // Skip empty password
    const char* message_names[] = {"SHORT", "LONG", "UNICODE", "EMOJI", "MIXED_UNICODE"};
    const char* carrier_names[] = {"EMPTY", "SHORT", "LONG", "UNICODE", "EMOJI", "MIXED_UNICODE"};
    const char* password_names[] = {"SHORT", "LONG"};
    
    int total_tests = 0;
    int wrong_password_tests = 0;
    
    for (int m = 0; m < 5; m++) {
        for (int c = 0; c < 6; c++) {
            for (int p = 0; p < 2; p++) {
                char test_name[256];
                snprintf(test_name, sizeof(test_name), "WrongPassword_%s_%s_%s", 
                        message_names[m], carrier_names[c], password_names[p]);
                
                bool result = test_wrong_password(messages[m], carriers[c], passwords[p], test_name);
                test_result(result, test_name);
                total_tests++;
                if (result) wrong_password_tests++;
            }
        }
    }
    
    printf("\nWrong Password Test Summary: %d/%d passed\n", wrong_password_tests, total_tests);
}

// Test edge cases
static void run_edge_case_tests(void) {
    printf("\n=== Running Edge Case Tests ===\n");
    
    // Test with very long message
    const char* very_long_message = "This is an extremely long message that contains many characters and should test the limits of the encoding system. "
                                   "It includes various types of content including numbers 123456789, special characters !@#$%^&*(), and multiple sentences. "
                                   "The message continues with more content to ensure we're testing the full range of capabilities. "
                                   "We want to make sure that the system can handle messages of substantial length without issues. "
                                   "This includes testing with various character encodings and ensuring proper handling of all edge cases.";
    
    bool result = test_roundtrip(very_long_message, LONG_CARRIER, LONG_PASSWORD, "VeryLongMessage");
    test_result(result, "VeryLongMessage");
    
    // Test with single character message
    result = test_roundtrip("A", SHORT_CARRIER, SHORT_PASSWORD, "SingleCharMessage");
    test_result(result, "SingleCharMessage");
    
    // Test with single character carrier
    result = test_roundtrip(SHORT_MESSAGE, "A", SHORT_PASSWORD, "SingleCharCarrier");
    test_result(result, "SingleCharCarrier");
    
    // Test with special characters in message
    const char* special_chars_message = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~";
    result = test_roundtrip(special_chars_message, SHORT_CARRIER, SHORT_PASSWORD, "SpecialCharsMessage");
    test_result(result, "SpecialCharsMessage");
    
    // Test with special characters in password
    const char* special_chars_password = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~";
    result = test_roundtrip(SHORT_MESSAGE, SHORT_CARRIER, special_chars_password, "SpecialCharsPassword");
    test_result(result, "SpecialCharsPassword");
    
    // Test with newlines in message
    const char* newline_message = "Line 1\nLine 2\nLine 3";
    result = test_roundtrip(newline_message, SHORT_CARRIER, SHORT_PASSWORD, "NewlineMessage");
    test_result(result, "NewlineMessage");
    
    // Test with tabs in message
    const char* tab_message = "Tab\tSeparated\tValues";
    result = test_roundtrip(tab_message, SHORT_CARRIER, SHORT_PASSWORD, "TabMessage");
    test_result(result, "TabMessage");
}

// Test Unicode and Emoji specific cases
static void run_unicode_specific_tests(void) {
    printf("\n=== Running Unicode-Specific Tests ===\n");
    
    // Test with various Unicode ranges
    const char* unicode_ranges[] = {
        "Basic Latin: Hello World!",
        "Latin-1: café résumé naïve",
        "Latin Extended: āēīōū",
        "Cyrillic: привет мир",
        "Greek: γεια κόσμε",
        "Arabic: مرحبا بالعالم",
        "Hebrew: שלום עולם",
        "Thai: สวัสดีโลก",
        "Chinese: 你好世界",
        "Japanese: こんにちは世界",
        "Korean: 안녕하세요 세계"
    };
    
    const char* test_names[] = {
        "BasicLatin", "Latin1", "LatinExtended", "Cyrillic", "Greek", 
        "Arabic", "Hebrew", "Thai", "Chinese", "Japanese", "Korean"
    };
    
    for (int i = 0; i < 11; i++) {
        bool result = test_roundtrip(unicode_ranges[i], SHORT_CARRIER, SHORT_PASSWORD, test_names[i]);
        test_result(result, test_names[i]);
    }
    
    // Test with various emoji categories
    const char* emoji_categories[] = {
        "Smileys: 😀😃😄😁😆😅😂🤣😊😇",
        "Animals: 🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯",
        "Food: 🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒",
        "Activities: ⚽🏀��⚾🎾🏐🏉🎱🏓🏸",
        "Travel: 🚗🚕🚙🚌🚎🏎🚓🚑🚒🚐",
        "Objects: 💻⌨️🖥🖨🖱🖲🕹🎮🎲🧩"
    };
    
    const char* emoji_names[] = {
        "Smileys", "Animals", "Food", "Activities", "Travel", "Objects"
    };
    
    for (int i = 0; i < 6; i++) {
        bool result = test_roundtrip(emoji_categories[i], SHORT_CARRIER, SHORT_PASSWORD, emoji_names[i]);
        test_result(result, emoji_names[i]);
    }
}

// Test null pointer handling
static void run_null_pointer_tests(void) {
    printf("\n=== Running Null Pointer Tests ===\n");
    
    char* result = NULL;
    
    // Test encode with null message
    bool encode_result = whitespace_stego_encode(SHORT_CARRIER, strlen(SHORT_CARRIER), NULL, SHORT_PASSWORD, &result);
    test_result(!encode_result, "EncodeNullMessage");
    if (result) whitespace_stego_free(result);
    
    // Test encode with null result pointer
    encode_result = whitespace_stego_encode(SHORT_CARRIER, strlen(SHORT_CARRIER), SHORT_MESSAGE, SHORT_PASSWORD, NULL);
    test_result(!encode_result, "EncodeNullResult");
    
    // Test decode with null carrier
    bool decode_result = whitespace_stego_decode(NULL, 0, SHORT_PASSWORD, &result);
    test_result(!decode_result, "DecodeNullCarrier");
    if (result) whitespace_stego_free(result);
    
    // Test decode with null result pointer
    decode_result = whitespace_stego_decode(SHORT_CARRIER, strlen(SHORT_CARRIER), SHORT_PASSWORD, NULL);
    test_result(!decode_result, "DecodeNullResult");
}

// Main test runner
int main(void) {
    printf("=== C Implementation Comprehensive Test Suite ===\n");
    printf("Testing all permutations of message, carrier, and password\n");
    printf("with UTF-8 and Unicode/Emoji support\n\n");
    
    // Run all test categories
    run_all_permutation_tests();
    run_empty_message_tests();
    run_wrong_password_tests();
    run_edge_case_tests();
    run_unicode_specific_tests();
    run_null_pointer_tests();
    
    // Print final summary
    printf("\n=== Final Test Summary ===\n");
    printf("Total tests run: %d\n", tests_run);
    printf("Tests passed: %d\n", tests_passed);
    printf("Tests failed: %d\n", tests_failed);
    printf("Success rate: %.1f%%\n", (double)tests_passed / tests_run * 100.0);
    
    if (tests_failed == 0) {
        printf("\n🎉 All tests passed!\n");
        return 0;
    } else {
        printf("\n❌ Some tests failed!\n");
        return 1;
    }
}
