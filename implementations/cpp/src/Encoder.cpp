#include "Encoder.hpp"
#include "Constants.hpp"
#include "Utils.hpp"
#include "Crypto.hpp"
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
    // Strategy: insert after the first character for better compatibility
    // This matches the behavior of other implementations
    if (carrier.empty()) {
        return 0;
    }
    
    // For UTF-8, we need to find the first complete character
    size_t first_char_len = 0;
    unsigned char first_byte = static_cast<unsigned char>(carrier[0]);
    
    if (first_byte < 0x80) {
        // ASCII character - 1 byte
        first_char_len = 1;
    } else if (first_byte < 0xE0) {
        // 2-byte UTF-8 sequence
        first_char_len = 2;
    } else if (first_byte < 0xF0) {
        // 3-byte UTF-8 sequence
        first_char_len = 3;
    } else {
        // 4-byte UTF-8 sequence
        first_char_len = 4;
    }
    
    // Ensure we don't exceed carrier length
    if (first_char_len > carrier.length()) {
        first_char_len = carrier.length();
    }
    
    return first_char_len;
} 