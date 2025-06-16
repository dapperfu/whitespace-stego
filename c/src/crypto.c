#include "../include/crypto.h"
#include "../include/utils.h"
#include "../include/whitespace_stego.h"
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/sha.h>

#define SALT_LEN 16
#define KEY_LEN 32
#define IV_LEN 16
#define TAG_LEN 16

static bool derive_key(const char* password, const unsigned char* salt,
                      unsigned char* key, unsigned char* iv) {
    if (!password || !salt || !key || !iv) {
        return false;
    }

    // Use PBKDF2 to derive key and IV
    if (PKCS5_PBKDF2_HMAC(password, strlen(password),
                          salt, SALT_LEN,
                          10000,  // iterations
                          EVP_sha256(),
                          KEY_LEN + IV_LEN,
                          key) != 1) {
        return false;
    }

    // Split the derived bytes into key and IV
    memcpy(iv, key + KEY_LEN, IV_LEN);
    return true;
}

bool crypto_encrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len) {
    if (!data || !password || !result || !result_len) {
        return false;
    }

    // Generate salt
    unsigned char salt[SALT_LEN];
    if (RAND_bytes(salt, SALT_LEN) != 1) {
        return false;
    }

    // Derive key and IV
    unsigned char key[KEY_LEN + IV_LEN];
    unsigned char* iv = key + KEY_LEN;
    if (!derive_key(password, salt, key, iv)) {
        return false;
    }

    // Create cipher context
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        return false;
    }

    // Initialize encryption
    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Calculate output size
    *result_len = SALT_LEN + data_len + EVP_MAX_BLOCK_LENGTH + TAG_LEN;
    *result = malloc(*result_len);
    if (!*result) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Copy salt to output
    memcpy(*result, salt, SALT_LEN);
    int out_len = SALT_LEN;

    // Encrypt data
    int len;
    if (EVP_EncryptUpdate(ctx, *result + out_len, &len, data, data_len) != 1) {
        free(*result);
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    out_len += len;

    // Finalize encryption
    if (EVP_EncryptFinal_ex(ctx, *result + out_len, &len) != 1) {
        free(*result);
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    out_len += len;

    // Get authentication tag
    if (EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, TAG_LEN, *result + out_len) != 1) {
        free(*result);
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    out_len += TAG_LEN;

    // Update final length
    *result_len = out_len;

    EVP_CIPHER_CTX_free(ctx);
    return true;
}

bool crypto_decrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len) {
    if (!data || !password || !result || !result_len || data_len < SALT_LEN + TAG_LEN) {
        return false;
    }

    // Extract salt
    const unsigned char* salt = data;
    const unsigned char* encrypted = data + SALT_LEN;
    size_t encrypted_len = data_len - SALT_LEN - TAG_LEN;

    // Derive key and IV
    unsigned char key[KEY_LEN + IV_LEN];
    unsigned char* iv = key + KEY_LEN;
    if (!derive_key(password, salt, key, iv)) {
        return false;
    }

    // Create cipher context
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        return false;
    }

    // Initialize decryption
    if (EVP_DecryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Set authentication tag
    if (EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_TAG, TAG_LEN,
                           (void*)(data + data_len - TAG_LEN)) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Allocate output buffer
    *result = malloc(encrypted_len);
    if (!*result) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Decrypt data
    int out_len;
    if (EVP_DecryptUpdate(ctx, *result, &out_len, encrypted, encrypted_len) != 1) {
        free(*result);
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    // Finalize decryption
    int len;
    if (EVP_DecryptFinal_ex(ctx, *result + out_len, &len) != 1) {
        free(*result);
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }

    *result_len = out_len + len;
    EVP_CIPHER_CTX_free(ctx);
    return true;
}

void crypto_free(unsigned char* ptr) {
    if (ptr) {
        free(ptr);
    }
} 