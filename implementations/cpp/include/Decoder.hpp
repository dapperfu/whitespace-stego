#ifndef DECODER_HPP
#define DECODER_HPP

#include <string>
#include <vector>

/**
 * @class Decoder
 * @brief Decodes messages from carrier text using zero-width steganography.
 */
class Decoder {
public:
    Decoder() = default;
    ~Decoder() = default;

    // Decode messages from a carrier
    static std::vector<std::string> decode(const std::string& carrier, const std::string& password = "");
};

#endif // DECODER_HPP 