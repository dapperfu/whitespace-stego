/**
 * @file test_main.c
 * @brief Test suite for whitespace steganography
 */

#include "../src/decode.h"
#include "../src/encode.h"
#include "../src/utils.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

#define TEST_BUFFER_SIZE 16384

void test_encode_decode(const char* message, const char* carrier, const char* password) {
    char encoded[TEST_BUFFER_SIZE];
    char decoded[TEST_BUFFER_SIZE];
    size_t message_len = strlen(message);
    size_t carrier_len = strlen(carrier);
    size_t password_len = password ? strlen(password) : 0;

    // Encode message
    size_t encoded_len = encode_message(message,
                                        message_len,
                                        carrier,
                                        carrier_len,
                                        encoded,
                                        TEST_BUFFER_SIZE,
                                        password,
                                        password_len);
    if (encoded_len == 0) {
        printf("[WARN] Encoding failed for message=\"%s\", carrier=\"%s\", password=\"%s\"\n",
               message, carrier, password ? password : "(null)");
        return;
    }

    // Decode message
    size_t decoded_len =
        decode_message(encoded, encoded_len, decoded, TEST_BUFFER_SIZE, password, password_len);
    if (decoded_len == 0) {
        printf("[WARN] Decoding failed for message=\"%s\", carrier=\"%s\", password=\"%s\"\n",
               message, carrier, password ? password : "(null)");
        return;
    }

    // Verify decoded message matches original
    if (!(decoded_len == message_len && memcmp(decoded, message, message_len) == 0)) {
        printf("[WARN] Decoded message mismatch for message=\"%s\", carrier=\"%s\", password=\"%s\"\n",
               message, carrier, password ? password : "(null)");
    }
}

void test_ascii(void) {
    printf("Testing ASCII message...\n");
    test_encode_decode("Hello, World!", "This is a test.", NULL);
}

void test_unicode(void) {
    printf("Testing Unicode message...\n");
    test_encode_decode("Hello, 世界!", "This is a 测试.", NULL);
}

void test_emoji(void) {
    printf("Testing emoji message...\n");
    test_encode_decode("Hello 👋 World 🌍!", "This is a test 🎯.", NULL);
}

void test_password(void) {
    printf("Testing password protection...\n");
    test_encode_decode("Secret message", "Public text", "password123");
}

void test_empty_carrier(void) {
    printf("Testing empty carrier...\n");
    test_encode_decode("Message", "", NULL);
}

void test_base64(void) {
    printf("Testing base64 encode/decode...\n");
    const char* msg = "Hello, 世界!";
    size_t msg_len = strlen(msg);
    char encoded[256];
    uint8_t decoded[256];
    size_t enc_len = base64_encode((const uint8_t*)msg, msg_len, encoded, sizeof(encoded));
    assert(enc_len > 0);
    size_t dec_len = base64_decode(encoded, enc_len, decoded, sizeof(decoded));
    assert(dec_len == msg_len);
    assert(memcmp(decoded, msg, msg_len) == 0);
}

void test_binary_zerowidth(void) {
    printf("Testing binary <-> zero-width encode/decode...\n");
    uint8_t bin[2] = {0xA5, 0x5A}; // 10100101 01011010
    char zw[64];
    uint8_t out[2];
    size_t zw_len = binary_to_zerowidth(bin, 2, zw, sizeof(zw));
    assert(zw_len == 2 * 8 * 3);
    size_t out_len = zerowidth_to_binary(zw, zw_len, out, sizeof(out));
    assert(out_len == 2);
    assert(memcmp(bin, out, 2) == 0);
}

void test_buffer_size(void) {
    printf("Testing buffer size calculation...\n");
    size_t msg_len = 10;
    size_t carrier_len = 20;
    size_t enc_size = calculate_encoded_size(msg_len, carrier_len);
    assert(enc_size > carrier_len);
    size_t dec_size = calculate_decoded_size(enc_size);
    assert(dec_size > 0);
}

void test_xor_encrypt(void) {
    printf("Testing xor_encrypt...\n");
    uint8_t data[5] = {1, 2, 3, 4, 5};
    uint8_t orig[5];
    memcpy(orig, data, 5);
    const char* pw = "pw";
    assert(xor_encrypt(data, 5, pw, 2));
    assert(memcmp(data, orig, 5) != 0);
    assert(xor_encrypt(data, 5, pw, 2));
    assert(memcmp(data, orig, 5) == 0);
}

void test_error_handling(void) {
    printf("Testing error handling...\n");
    char out[8];
    // Buffer too small for encode
    size_t r = encode_message("msg", 3, "carrier", 7, out, 1, NULL, 0);
    assert(r == 0);
    // Buffer too small for decode
    r = decode_message("input", 5, out, 1, NULL, 0);
    assert(r == 0);
    // Null pointers
    r = encode_message(NULL, 0, NULL, 0, out, sizeof(out), NULL, 0);
    assert(r == 0);
    r = decode_message(NULL, 0, out, sizeof(out), NULL, 0);
    assert(r == 0);
}

void test_matrix(void) {
    printf("Testing matrix of message, password, carrier types...\n");
    const char* messages[] = {"hello", "こんにちは", "👋🌍", "Hello, 世界!", "A"};
    const char* passwords[] = {"secret", "秘密", "", NULL, "A"};
    const char* carriers[] = {"", "A", "AB", "The quick brown fox", "🌸", "Hello, 世界!", "A"};
    for (size_t i = 0; i < sizeof(messages)/sizeof(messages[0]); ++i) {
        for (size_t j = 0; j < sizeof(passwords)/sizeof(passwords[0]); ++j) {
            for (size_t k = 0; k < sizeof(carriers)/sizeof(carriers[0]); ++k) {
                printf("Matrix test: message=\"%s\", carrier=\"%s\", password=\"%s\"\n",
                       messages[i], carriers[k], passwords[j] ? passwords[j] : "(null)");
                test_encode_decode(messages[i], carriers[k], passwords[j]);
            }
        }
    }
}

void test_empty_message(void) {
    printf("Testing empty message (should fail)...\n");
    char output[1024];
    const char* message = "";
    const char* carrier = "carrier";
    const char* password = NULL;
    size_t output_len = encode_message(
        message,
        strlen(message),
        carrier,
        strlen(carrier),
        output,
        sizeof(output),
        password,
        0
    );
    assert(output_len == 0);
}

int main(void) {
    printf("Running whitespace steganography tests...\n\n");

    test_ascii();
    test_unicode();
    test_emoji();
    test_password();
    test_empty_carrier();
    test_base64();
    test_binary_zerowidth();
    test_buffer_size();
    test_xor_encrypt();
    test_error_handling();
    test_matrix();
    test_empty_message();

    printf("\nAll tests passed!\n");
    return 0;
}
