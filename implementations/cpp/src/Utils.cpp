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
    std::string result;
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
    
    // Zero-width space: \u200b (3 bytes: 0xE2 0x80 0x8B)
    // Zero-width joiner: \u200d (3 bytes: 0xE2 0x80 0x8D)
    for (size_t i = 0; i < zwstr.length(); ++i) {
        if (i + 2 < zwstr.length() && 
            (unsigned char)zwstr[i] == 0xE2 && 
            (unsigned char)zwstr[i+1] == 0x80) {
            
            if ((unsigned char)zwstr[i+2] == 0x8B) {
                current_byte += '1';
                i += 2; // Skip the next 2 bytes
            } else if ((unsigned char)zwstr[i+2] == 0x8D) {
                current_byte += '0';
                i += 2; // Skip the next 2 bytes
            }
        }
        
        if (current_byte.length() == 8) {
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