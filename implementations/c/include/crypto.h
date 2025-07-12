/*
 * Crypto Header: crypto.h
 * Provides encryption and decryption functionality for the whitespace steganography system.
 * Uses OpenSSL for cryptographic operations.
 */

#ifndef CRYPTO_H
#define CRYPTO_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Encrypt data using AES-256-CBC
 * @param data Input data to encrypt
 * @param data_len Length of input data
 * @param password Password for key derivation
 * @param encrypted_data Output buffer for encrypted data (will be allocated)
 * @param encrypted_len Output length of encrypted data
 * @return 1 on success, 0 on failure
 */
int crypto_encrypt(const unsigned char* data, size_t data_len, const char* password,
                   unsigned char** encrypted_data, size_t* encrypted_len);

/**
 * Decrypt data using AES-256-CBC
 * @param encrypted_data Input encrypted data
 * @param encrypted_len Length of encrypted data
 * @param password Password for key derivation
 * @param decrypted_data Output buffer for decrypted data (will be allocated)
 * @param decrypted_len Output length of decrypted data
 * @return 1 on success, 0 on failure
 */
int crypto_decrypt(const unsigned char* encrypted_data, size_t encrypted_len, const char* password,
                   unsigned char** decrypted_data, size_t* decrypted_len);

/**
 * Free allocated crypto data
 * @param data Pointer to data to free
 */
void crypto_free(unsigned char* data);

/**
 * Generate random initialization vector
 * @param iv Output IV buffer (16 bytes)
 * @return 1 on success, 0 on failure
 */
int generate_iv(unsigned char* iv);

/**
 * Validate password strength
 * @param password Password to validate
 * @return 1 if strong enough, 0 if too weak
 */
int validate_password_strength(const char* password);

/**
 * Get crypto error message
 * @return Pointer to error message string
 */
const char* crypto_get_error(void);

/**
 * Clear crypto error state
 */
void crypto_clear_error(void);

#ifdef __cplusplus
}
#endif

#endif 