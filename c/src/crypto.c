#include "../include/crypto.h"
#include "../include/utils.h"
#include "../include/whitespace_stego.h"
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <time.h>

#define KEY_LEN 32
#define IV_LEN 16

// Derive key from password using SHA-256 (same as Python/Rust)
static bool derive_key(const char* password, unsigned char* key) {
    if (!password || !key) {
        return false;
    }
    
    // Use SHA-256 to derive a consistent 32-byte key from password
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password, strlen(password));
    SHA256_Final(key, &sha256);
    
    return true;
}

bool crypto_encrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len) {
    if (!data || !password || !result || !result_len) {
        return false;
    }
    
    // Derive key
    unsigned char key[KEY_LEN];
    if (!derive_key(password, key)) {
        return false;
    }
    
    // Generate random IV
    unsigned char iv[IV_LEN];
    if (RAND_bytes(iv, IV_LEN) != 1) {
        return false;
    }
    
    // Create cipher context
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        return false;
    }
    
    // Initialize encryption
    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    
    // Calculate output size
    *result_len = IV_LEN + data_len + EVP_MAX_BLOCK_LENGTH;
    *result = malloc(*result_len);
    if (!*result) {
        EVP_CIPHER_CTX_free(ctx);
        return false;
    }
    
    // Copy IV to output
    memcpy(*result, iv, IV_LEN);
    int out_len = IV_LEN;
    
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
    
    // Update final length
    *result_len = out_len;
    
    EVP_CIPHER_CTX_free(ctx);
    return true;
}

bool crypto_decrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len) {
    if (!data || !password || !result || !result_len || data_len < IV_LEN) {
        return false;
    }
    
    // Derive key
    unsigned char key[KEY_LEN];
    if (!derive_key(password, key)) {
        return false;
    }
    
    // Extract IV
    const unsigned char* iv = data;
    const unsigned char* encrypted = data + IV_LEN;
    size_t encrypted_len = data_len - IV_LEN;
    
    // Create cipher context
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) {
        return false;
    }
    
    // Initialize decryption
    if (EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
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