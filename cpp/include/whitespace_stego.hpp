#ifndef WHITESPACE_STEGO_HPP
#define WHITESPACE_STEGO_HPP

#include <string>
#include <stdexcept>

namespace whitespace_stego {

/// Base exception for all steganography errors
class StegoException : public std::runtime_error {
public:
    explicit StegoException(const std::string& message)
        : std::runtime_error(message) {}
};

/// Encoding exception
class EncodingException : public StegoException {
public:
    explicit EncodingException(const std::string& message)
        : StegoException("Encoding error: " + message) {}
};

/// Decoding exception
class DecodingException : public StegoException {
public:
    explicit DecodingException(const std::string& message)
        : StegoException("Decoding error: " + message) {}
};

/// Main steganography class
class WhitespaceStego {
public:
    /// Encode a message into invisible Unicode characters
    ///
    /// @param message The message to encode
    /// @param carrier Optional carrier text (empty string for no carrier)
    /// @param password Optional password for XOR encryption (empty string for no encryption)
    /// @return Encoded string with invisible Unicode characters
    /// @throws EncodingException if encoding fails
    static std::string encode(const std::string& message,
                               const std::string& carrier = "",
                               const std::string& password = "");

    /// Decode a message from invisible Unicode characters
    ///
    /// @param encoded_text Text containing the encoded message
    /// @param password Optional password for XOR decryption (empty string for no decryption)
    /// @return Decoded original message
    /// @throws DecodingException if decoding fails
    static std::string decode(const std::string& encoded_text,
                              const std::string& password = "");
};

} // namespace whitespace_stego

#endif // WHITESPACE_STEGO_HPP

