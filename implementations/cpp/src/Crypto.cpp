#include "Crypto.hpp"
#include "Utils.hpp"
#include <algorithm>
#include <functional>
#include <stdexcept>

std::string Crypto::encrypt(const std::string& plaintext, const std::string& password) {
    if (password.empty()) {
        return plaintext; // No encryption if no password
    }
    
    // Simple XOR-based encryption with password
    std::string encrypted = plaintext;
    for (size_t i = 0; i < encrypted.length(); ++i) {
        encrypted[i] ^= password[i % password.length()];
    }
    
    // Convert to base64 for safe storage
    return Utils::base64Encode(encrypted);
}

std::string Crypto::decrypt(const std::string& ciphertext, const std::string& password) {
    if (password.empty()) {
        return ciphertext; // No decryption if no password
    }
    
    try {
        // Decode from base64
        std::string decoded = Utils::base64Decode(ciphertext);
        
        // XOR decrypt
        std::string decrypted = decoded;
        for (size_t i = 0; i < decrypted.length(); ++i) {
            decrypted[i] ^= password[i % password.length()];
        }
        
        return decrypted;
    } catch (const std::exception& e) {
        throw std::runtime_error("Decryption failed: invalid password or corrupted data");
    }
} 