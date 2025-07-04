#include "Decoder.hpp"
#include "Constants.hpp"
#include "Utils.hpp"
#include "Crypto.hpp"
#include <regex>
#include <stdexcept>

// Utility to escape regex special characters (C++ doesn't have std::regex_escape)
static std::string regex_escape(const std::string& s) {
    static const std::string metachars = R"(^$.*+?()[]{}|\\)";
    std::string out;
    for (char c : s) {
        if (metachars.find(c) != std::string::npos) out += '\\';
        out += c;
    }
    return out;
}

std::vector<std::string> Decoder::decode(const std::string& carrier, const std::string& password) {
    std::vector<std::string> messages;
    
    // Create regex pattern to find all encoded messages
    // Use [\s\S]*? for dotall behavior (matches across newlines)
    std::string pattern = regex_escape(Constants::START_MARKER) + 
                         "([\\s\\S]*?)" + 
                         regex_escape(Constants::END_MARKER);
    
    std::regex regex_pattern(pattern);
    std::sregex_iterator iter(carrier.begin(), carrier.end(), regex_pattern);
    std::sregex_iterator end;
    
    for (; iter != end; ++iter) {
        try {
            std::string zero_width_data = (*iter)[1].str();
            
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
            continue;
        }
    }
    
    if (messages.empty()) {
        throw std::runtime_error("No valid messages found");
    }
    
    return messages;
} 