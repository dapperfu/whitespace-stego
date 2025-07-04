/*
 * MISRA C Compliance: crypto.h
 * This file has been refactored for MISRA C:2012 compliance.
 * - No <stdbool.h>; use int for boolean (0/1)
 * - All functions and logic blocks documented
 */
#ifndef CRYPTO_H
#define CRYPTO_H

#include <stddef.h>

/**
 * @brief Encrypt data using a password
 *
 * @param data Data to encrypt
 * @param data_len Length of data
 * @param password Password to use for encryption
 * @param result Pointer to store encrypted data
 * @param result_len Pointer to store length of encrypted data
 * @return 1 if encryption was successful, 0 otherwise
 */
int crypto_encrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len);

/**
 * @brief Decrypt data using a password
 *
 * @param data Encrypted data
 * @param data_len Length of encrypted data
 * @param password Password to use for decryption
 * @param result Pointer to store decrypted data
 * @param result_len Pointer to store length of decrypted data
 * @return 1 if decryption was successful, 0 otherwise
 */
int crypto_decrypt(const unsigned char* data, size_t data_len,
                   const char* password, unsigned char** result,
                   size_t* result_len);

/**
 * @brief Free memory allocated by encrypt/decrypt functions
 *
 * @param ptr Pointer to the memory to free
 */
void crypto_free(unsigned char* ptr);

#endif // CRYPTO_H 