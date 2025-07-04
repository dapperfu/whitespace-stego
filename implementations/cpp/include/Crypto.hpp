#ifndef CRYPTO_HPP
#define CRYPTO_HPP

#include <string>

/**
 * @class Crypto
 * @brief Provides encryption and decryption utilities for messages.
 */
class Crypto {
public:
    // Encrypt a string with a password
    static std::string encrypt(const std::string& plaintext, const std::string& password);

    // Decrypt a string with a password
    static std::string decrypt(const std::string& ciphertext, const std::string& password);
};

#endif // CRYPTO_HPP 