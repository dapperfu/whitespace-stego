/**
 * @file test_main.c
 * @brief Test suite for whitespace steganography
 */

#include "../src/encode.h"
#include "../src/decode.h"
#include "../src/utils.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

#define TEST_BUFFER_SIZE 1024

void test_encode_decode(const char* message, const char* carrier, const char* password) {
    char encoded[TEST_BUFFER_SIZE];
    char decoded[TEST_BUFFER_SIZE];
    size_t message_len = strlen(message);
    size_t carrier_len = strlen(carrier);
    size_t password_len = password ? strlen(password) : 0;

    // Encode message
    size_t encoded_len = encode_message(
        message,
        message_len,
        carrier,
        carrier_len,
        encoded,
        TEST_BUFFER_SIZE,
        password,
        password_len
    );
    assert(encoded_len > 0);

    // Decode message
    size_t decoded_len = decode_message(
        encoded,
        encoded_len,
        decoded,
        TEST_BUFFER_SIZE,
        password,
        password_len
    );
    assert(decoded_len > 0);

    // Verify decoded message matches original
    assert(decoded_len == message_len);
    assert(memcmp(decoded, message, message_len) == 0);
}

void test_ascii() {
    printf("Testing ASCII message...\n");
    test_encode_decode("Hello, World!", "This is a test.", NULL);
}

void test_unicode() {
    printf("Testing Unicode message...\n");
    test_encode_decode("Hello, 世界!", "This is a 测试.", NULL);
}

void test_emoji() {
    printf("Testing emoji message...\n");
    test_encode_decode("Hello 👋 World 🌍!", "This is a test 🎯.", NULL);
}

void test_password() {
    printf("Testing password protection...\n");
    test_encode_decode("Secret message", "Public text", "password123");
}

void test_empty_carrier() {
    printf("Testing empty carrier...\n");
    test_encode_decode("Message", "", NULL);
}

int main() {
    printf("Running whitespace steganography tests...\n\n");

    test_ascii();
    test_unicode();
    test_emoji();
    test_password();
    test_empty_carrier();

    printf("\nAll tests passed!\n");
    return 0;
} 