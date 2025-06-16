#ifndef CRYPTO_H
#define CRYPTO_H

char *encrypt(const char *plaintext, const char *password);
char *decrypt(const char *ciphertext_b64, const char *password);

#endif