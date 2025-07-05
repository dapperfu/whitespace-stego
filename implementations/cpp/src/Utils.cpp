#include "Utils.hpp"
#include <sstream>
#include <iomanip>
#include <algorithm>

namespace Utils {

// Base64 encoding table
static const std::string base64_chars = 
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789+/";

std::string base64Encode(const std::string& input) {
    // Security: Limit input size to prevent memory exhaustion attacks
    // Base64 expansion: ~1.33x (4/3 ratio)
    const size_t MAX_INPUT_SIZE = 768 * 1024; // 768KB limit (allows up to 1MB output)
    if (input.length() > MAX_INPUT_SIZE) {
        throw std::runtime_error("Input too large: potential memory exhaustion attack");
    }
    
    std::string result;
    int val = 0, valb = -6;
    
    for (unsigned char c : input) {
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            result.push_back(base64_chars[(val >> valb) & 0x3F]);
            valb -= 6;
        }
    }
    
    if (valb > -6) {
        result.push_back(base64_chars[((val << 8) >> (valb + 8)) & 0x3F]);
    }
    
    while (result.size() % 4) {
        result.push_back('=');
    }
    
    return result;
}

std::string base64Decode(const std::string& input) {
    // Security: Limit input size to prevent memory exhaustion attacks
    // Base64 compression: ~0.75x (3/4 ratio)
    const size_t MAX_INPUT_SIZE = 1024 * 1024; // 1MB limit (allows up to 768KB output)
    if (input.length() > MAX_INPUT_SIZE) {
        throw std::runtime_error("Input too large: potential memory exhaustion attack");
    }
    
    std::string result;
    int val = 0, valb = -8;
    
    for (unsigned char c : input) {
        if (c == '=') break;
        
        auto pos = base64_chars.find(c);
        if (pos == std::string::npos) {
            throw std::runtime_error("Invalid base64 character");
        }
        
        val = (val << 6) + pos;
        valb += 6;
        
        if (valb >= 0) {
            result.push_back((val >> valb) & 0xFF);
            valb -= 8;
        }
    }
    
    return result;
}

std::string toZeroWidth(const std::string& binary) {
    // Security: Limit input size to prevent memory exhaustion attacks
    // Base64 expansion: ~1.33x, Zero-width expansion: 24x, Total: ~32x
    // For 1MB input, output could be up to 32MB
    const size_t MAX_INPUT_SIZE = 256 * 1024; // 256KB limit (allows up to 8MB output)
    if (binary.length() > MAX_INPUT_SIZE) {
        throw std::runtime_error("Input too large: potential memory exhaustion attack");
    }
    
    // Security: Calculate output size and check limits
    const size_t OUTPUT_SIZE = binary.length() * 8 * 3; // 8 bits per byte, 3 bytes per zero-width char
    const size_t MAX_OUTPUT_SIZE = 8 * 1024 * 1024; // 8MB limit (32x expansion from 256KB input)
    if (OUTPUT_SIZE > MAX_OUTPUT_SIZE) {
        throw std::runtime_error("Output would be too large: potential memory exhaustion attack");
    }
    
    std::string result;
    result.reserve(OUTPUT_SIZE); // Pre-allocate to prevent reallocation attacks
    
    for (unsigned char byte : binary) {
        for (int i = 7; i >= 0; --i) {
            if (byte & (1 << i)) {
                result += "\u200b"; // Zero-width space
            } else {
                result += "\u200d"; // Zero-width joiner
            }
        }
    }
    return result;
}

std::string fromZeroWidth(const std::string& zwstr) {
    std::string result;
    std::string current_byte;
    
    // Security: Limit input size to prevent memory exhaustion attacks
    // Zero-width compression: ~0.042x (1/24 ratio)
    const size_t MAX_INPUT_SIZE = 8 * 1024 * 1024; // 8MB limit (allows up to 256KB output)
    if (zwstr.length() > MAX_INPUT_SIZE) {
        throw std::runtime_error("Input too large: potential memory exhaustion attack");
    }
    
    // Security: Limit output size to prevent buffer overflow attacks
    const size_t MAX_OUTPUT_SIZE = 256 * 1024; // 256KB limit
    const size_t MAX_BYTES = MAX_OUTPUT_SIZE;
    
    // Zero-width space: \u200b (3 bytes: 0xE2 0x80 0x8B)
    // Zero-width joiner: \u200d (3 bytes: 0xE2 0x80 0x8D)
    for (size_t i = 0; i < zwstr.length(); ++i) {
        // Security: Check bounds before accessing next bytes
        if (i + 2 >= zwstr.length()) {
            // Incomplete UTF-8 sequence at end - skip it
            break;
        }
        
        // Security: Validate UTF-8 sequence bounds
        if ((unsigned char)zwstr[i] == 0xE2 && 
            (unsigned char)zwstr[i+1] == 0x80) {
            
            if ((unsigned char)zwstr[i+2] == 0x8B) {
                current_byte += '1';
                i += 2; // Skip the next 2 bytes
            } else if ((unsigned char)zwstr[i+2] == 0x8D) {
                current_byte += '0';
                i += 2; // Skip the next 2 bytes
            }
            // Security: If it's not a valid zero-width character, skip it
        }
        
        // Security: Check if we have a complete byte
        if (current_byte.length() == 8) {
            // Security: Check output size limit before adding more bytes
            if (result.length() >= MAX_BYTES) {
                throw std::runtime_error("Output too large: potential buffer overflow attack");
            }
            
            char byte = 0;
            for (int j = 0; j < 8; ++j) {
                if (current_byte[j] == '1') {
                    byte |= (1 << (7 - j));
                }
            }
            result += byte;
            current_byte.clear();
        }
    }
    
    // Security: Handle incomplete byte at end
    if (!current_byte.empty() && current_byte.length() < 8) {
        // Pad with zeros for incomplete byte
        while (current_byte.length() < 8) {
            current_byte += '0';
        }
        
        // Security: Final bounds check
        if (result.length() >= MAX_BYTES) {
            throw std::runtime_error("Output too large: potential buffer overflow attack");
        }
        
        char byte = 0;
        for (int j = 0; j < 8; ++j) {
            if (current_byte[j] == '1') {
                byte |= (1 << (7 - j));
            }
        }
        result += byte;
    }
    
    return result;
}

std::vector<std::string> split(const std::string& str, const std::string& delimiter) {
    std::vector<std::string> result;
    size_t start = 0;
    size_t end = str.find(delimiter);
    
    while (end != std::string::npos) {
        result.push_back(str.substr(start, end - start));
        start = end + delimiter.length();
        end = str.find(delimiter, start);
    }
    
    result.push_back(str.substr(start));
    return result;
}

} // namespace Utils 