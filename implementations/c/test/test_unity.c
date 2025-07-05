#include "unity.h"
#include "../include/whitespace_stego_static.h"
#include <string.h>
#include <stdlib.h>

// Test data
static const char* TEST_MESSAGE = "Hello, World!";
static const char* TEST_CARRIER = "This is a test carrier text.";
static const char* TEST_PASSWORD = "test123";
static const char* UNICODE_MESSAGE = "Hello, 世界! 🌍";
static const char* UNICODE_CARRIER = "你好世界! 🌟";

void setUp(void) {
    // Setup code before each test
}

void tearDown(void) {
    // Cleanup code after each test
}

void test_basic_encode_decode(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len, decoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Test encoding
    TEST_ASSERT_TRUE(whitespace_stego_static_encode(&buffers, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                   TEST_MESSAGE, TEST_PASSWORD, &encoded_len));
    
    // Test decoding
    TEST_ASSERT_TRUE(whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                                   TEST_PASSWORD, &decoded_len));
    
    // Verify round-trip
    TEST_ASSERT_EQUAL_STRING(TEST_MESSAGE, buffers.decoded);
}

void test_encode_decode_no_password(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len, decoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Test encoding without password
    TEST_ASSERT_TRUE(whitespace_stego_static_encode(&buffers, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                   TEST_MESSAGE, NULL, &encoded_len));
    
    // Test decoding without password
    TEST_ASSERT_TRUE(whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                                   NULL, &decoded_len));
    
    // Verify round-trip
    TEST_ASSERT_EQUAL_STRING(TEST_MESSAGE, buffers.decoded);
}

void test_wrong_password(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len, decoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Encode with correct password
    TEST_ASSERT_TRUE(whitespace_stego_static_encode(&buffers, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                   TEST_MESSAGE, TEST_PASSWORD, &encoded_len));
    
    // Try to decode with wrong password
    TEST_ASSERT_FALSE(whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                                    "wrong_password", &decoded_len));
}

void test_empty_message(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Encode should fail with empty message
    TEST_ASSERT_FALSE(whitespace_stego_static_encode(&buffers, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                    "", TEST_PASSWORD, &encoded_len));
}

void test_unicode_support(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len, decoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Test encoding with Unicode
    TEST_ASSERT_TRUE(whitespace_stego_static_encode(&buffers, UNICODE_CARRIER, strlen(UNICODE_CARRIER), 
                                                   UNICODE_MESSAGE, TEST_PASSWORD, &encoded_len));
    
    // Test decoding with Unicode
    TEST_ASSERT_TRUE(whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                                   TEST_PASSWORD, &decoded_len));
    
    // Verify round-trip
    TEST_ASSERT_EQUAL_STRING(UNICODE_MESSAGE, buffers.decoded);
}

void test_null_pointers(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
    // Test with NULL carrier
    TEST_ASSERT_FALSE(whitespace_stego_static_encode(&buffers, NULL, 0, TEST_MESSAGE, TEST_PASSWORD, &encoded_len));
    
    // Test with NULL message
    TEST_ASSERT_FALSE(whitespace_stego_static_encode(&buffers, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                    NULL, TEST_PASSWORD, &encoded_len));
    
    // Test with NULL buffer pointer
    TEST_ASSERT_FALSE(whitespace_stego_static_encode(NULL, TEST_CARRIER, strlen(TEST_CARRIER), 
                                                    TEST_MESSAGE, TEST_PASSWORD, &encoded_len));
}

void test_large_data(void) {
    whitespace_stego_buffers_t buffers;
    size_t encoded_len, decoded_len;
    
    // Initialize buffers
    TEST_ASSERT_TRUE(whitespace_stego_static_init(&buffers));
    
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
    
    // Test encoding large data
    TEST_ASSERT_TRUE(whitespace_stego_static_encode(&buffers, large_carrier, strlen(large_carrier), 
                                                   large_message, TEST_PASSWORD, &encoded_len));
    
    // Test decoding large data
    TEST_ASSERT_TRUE(whitespace_stego_static_decode(&buffers, buffers.encoded, encoded_len, 
                                                   TEST_PASSWORD, &decoded_len));
    
    // Verify round-trip
    TEST_ASSERT_EQUAL_STRING(large_message, buffers.decoded);
    
    // Cleanup
    free(large_message);
    free(large_carrier);
}

int main(void) {
    UNITY_BEGIN();
    
    RUN_TEST(test_basic_encode_decode);
    RUN_TEST(test_encode_decode_no_password);
    RUN_TEST(test_wrong_password);
    RUN_TEST(test_empty_message);
    RUN_TEST(test_unicode_support);
    RUN_TEST(test_null_pointers);
    RUN_TEST(test_large_data);
    
    return UNITY_END();
} 