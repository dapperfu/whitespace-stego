#include "Encoder.hpp"
#include "Constants.hpp"
#include "Utils.hpp"
#include "Crypto.hpp"
#include <regex>
#include <stdexcept>

std::string Encoder::encode(const std::string& message, const std::string& carrier, const std::string& password) {
    if (message.empty()) {
        throw std::runtime_error("Message must not be empty");
    }
    
    // Encrypt the message if password is provided
    std::string processed_message = message;
    if (!password.empty()) {
        processed_message = Crypto::encrypt(message, password);
    }
    
    // Convert to zero-width characters
    std::string zero_width_data = Utils::toZeroWidth(processed_message);
    
    // Create the encoded message with markers
    std::string encoded_message = Constants::START_MARKER + zero_width_data + Constants::END_MARKER;
    
    // If carrier is empty, return just the encoded message
    if (carrier.empty()) {
        return encoded_message;
    }
    
    // Find a good position to insert the message
    size_t insert_pos = findInsertPosition(carrier);
    
    // Insert the encoded message into the carrier
    std::string result = carrier;
    result.insert(insert_pos, encoded_message);
    
    return result;
}

size_t Encoder::findInsertPosition(const std::string& carrier) {
    // Simple strategy: insert after the first space or at the end
    size_t pos = carrier.find(' ');
    if (pos == std::string::npos) {
        return carrier.length();
    }
    return pos + 1;
} 