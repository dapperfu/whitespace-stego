#ifndef UTILS_HPP
#define UTILS_HPP

#include <string>
#include <vector>

/**
 * @namespace Utils
 * @brief Utility functions for encoding, decoding, and conversions.
 */
namespace Utils {
    // Base64 encode
    std::string base64Encode(const std::string& input);
    // Base64 decode
    std::string base64Decode(const std::string& input);

    // Convert binary data to zero-width string
    std::string toZeroWidth(const std::string& binary);
    // Convert zero-width string to binary data
    std::string fromZeroWidth(const std::string& zwstr);

    // Split string by delimiter
    std::vector<std::string> split(const std::string& str, const std::string& delimiter);
}

#endif // UTILS_HPP 