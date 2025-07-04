#include "Decoder.hpp"
#include "Constants.hpp"
#include "Utils.hpp"
#include "Crypto.hpp"
#include <stdexcept>

std::vector<std::string> Decoder::decode(const std::string& carrier, const std::string& password) {
    std::vector<std::string> messages;
    const std::string& start_marker = Constants::START_MARKER;
    const std::string& end_marker = Constants::END_MARKER;
    size_t pos = 0;
    while (true) {
        size_t start = carrier.find(start_marker, pos);
        if (start == std::string::npos) break;
        start += start_marker.size();
        size_t end = carrier.find(end_marker, start);
        if (end == std::string::npos) break;
        std::string zero_width_data = carrier.substr(start, end - start);
        try {
            // Convert from zero-width to binary
            std::string binary_data = Utils::fromZeroWidth(zero_width_data);
            // Decrypt if password is provided
            std::string message = binary_data;
            if (!password.empty()) {
                message = Crypto::decrypt(binary_data, password);
            }
            messages.push_back(message);
        } catch (const std::exception& e) {
            // Skip invalid messages and continue
        }
        pos = end + end_marker.size();
    }
    if (messages.empty()) {
        throw std::runtime_error("No valid messages found");
    }
    return messages;
} 