#ifndef ENCODER_HPP
#define ENCODER_HPP

#include <string>

/**
 * @class Encoder
 * @brief Encodes messages into carrier text using zero-width steganography.
 */
class Encoder {
public:
    Encoder() = default;
    ~Encoder() = default;

    // Encode a message into a carrier
    static std::string encode(const std::string& message, const std::string& carrier, const std::string& password = "");

private:
    // Find a good position to insert the message
    static size_t findInsertPosition(const std::string& carrier);
};

#endif // ENCODER_HPP 