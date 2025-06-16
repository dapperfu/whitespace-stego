#include <openssl/evp.h>
#include <openssl/rand.h>
#include <stdlib.h>
#include <string.h>
#include "base64.h"
#include "crypto.h"

#define AES_KEYLEN 32
#define AES_IVLEN 16

char *encrypt(const char *plaintext, const char *password) {
    unsigned char key[AES_KEYLEN], iv[AES_IVLEN];
    PKCS5_PBKDF2_HMAC_SHA1(password, strlen(password), NULL, 0, 10000, AES_KEYLEN, key);
    RAND_bytes(iv, AES_IVLEN);

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    unsigned char *cipher = malloc(strlen(plaintext) + AES_IVLEN + AES_KEYLEN);
    int len, cipher_len;

    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);
    EVP_EncryptUpdate(ctx, cipher, &len, (unsigned char *)plaintext, strlen(plaintext));
    cipher_len = len;
    EVP_EncryptFinal_ex(ctx, cipher + len, &len);
    cipher_len += len;
    EVP_CIPHER_CTX_free(ctx);

    unsigned char *full = malloc(cipher_len + AES_IVLEN);
    memcpy(full, iv, AES_IVLEN);
    memcpy(full + AES_IVLEN, cipher, cipher_len);
    full[cipher_len + AES_IVLEN] = '\0';

    char *encoded = base64_encode((char *)full);
    free(cipher);
    free(full);
    return encoded;
}

char *decrypt(const char *ciphertext_b64, const char *password) {
    size_t decoded_len;
    char *decoded = base64_decode(ciphertext_b64, &decoded_len);
    if (decoded_len <= AES_IVLEN) return NULL;

    unsigned char key[AES_KEYLEN], iv[AES_IVLEN];
    PKCS5_PBKDF2_HMAC_SHA1(password, strlen(password), NULL, 0, 10000, AES_KEYLEN, key);
    memcpy(iv, decoded, AES_IVLEN);

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    unsigned char *plaintext = malloc(decoded_len);
    int len, pt_len;

    EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);
    EVP_DecryptUpdate(ctx, plaintext, &len, (unsigned char *)(decoded + AES_IVLEN), decoded_len - AES_IVLEN);
    pt_len = len;
    EVP_DecryptFinal_ex(ctx, plaintext + len, &len);
    pt_len += len;
    EVP_CIPHER_CTX_free(ctx);
    plaintext[pt_len] = '\0';
    free(decoded);
    return (char *)plaintext;
}