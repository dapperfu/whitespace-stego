#include "whitespace_stego.hpp"
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>

namespace whitespace_stego {

// Unicode control characters
constexpr char32_t CONTROL_START = 0x2060;  // Word Joiner
constexpr char32_t CONTROL_END = 0x2063;    // Invisible Separator
constexpr char32_t BIT_0 = 0x200B;          // Zero Width Space
constexpr char32_t BIT_1 = 0x200C;          // Zero Width Non-Joiner

// Base64 encoding table
static const std::string base64_chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

static std::string base64_encode(const std::vector<unsigned char>& data) {
    std::string ret;
    int i = 0;
    int j = 0;
    unsigned char char_array_3[3];
    unsigned char char_array_4[4];

    for (size_t idx = 0; idx < data.size(); idx++) {
        char_array_3[i++] = data[idx];
        if (i == 3) {
            char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
            char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
            char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
            char_array_4[3] = char_array_3[2] & 0x3f;

            for (i = 0; i < 4; i++) {
                ret += base64_chars[char_array_4[i]];
            }
            i = 0;
        }
    }

    if (i) {
        for (j = i; j < 3; j++) {
            char_array_3[j] = '\0';
        }

        char_array_4[0] = (char_array_3[0] & 0xfc) >> 2;
        char_array_4[1] = ((char_array_3[0] & 0x03) << 4) + ((char_array_3[1] & 0xf0) >> 4);
        char_array_4[2] = ((char_array_3[1] & 0x0f) << 2) + ((char_array_3[2] & 0xc0) >> 6);
        char_array_4[3] = char_array_3[2] & 0x3f;

        for (j = 0; j < i + 1; j++) {
            ret += base64_chars[char_array_4[j]];
        }

        while (i++ < 3) {
            ret += '=';
        }
    }

    return ret;
}

std::string WhitespaceStego::encode(const std::string& message,
                                     const std::string& carrier) {
    try {
        // Convert message to UTF-8 bytes
        std::vector<unsigned char> utf8_bytes(message.begin(), message.end());

        // Encode to Base64
        std::string base64_str = base64_encode(utf8_bytes);

        // Convert Base64 string to binary representation
        std::string binary_bits;
        for (unsigned char byte : base64_str) {
            // Convert each byte to 8-bit binary (MSB to LSB)
            for (int j = 7; j >= 0; j--) {
                binary_bits += ((byte >> j) & 1) ? '1' : '0';
            }
        }

        // Map binary bits to invisible Unicode characters (UTF-8 encoded)
        std::string bit0_utf8 = "\xE2\x80\x8B";  // U+200B Zero Width Space
        std::string bit1_utf8 = "\xE2\x80\x8C";  // U+200C Zero Width Non-Joiner
        std::string control_start_utf8 = "\xE2\x81\xA0";  // U+2060 Word Joiner
        std::string control_end_utf8 = "\xE2\x81\xA3";    // U+2063 Invisible Separator
        
        std::string encoded_payload;
        for (char bit : binary_bits) {
            if (bit == '0') {
                encoded_payload += bit0_utf8;
            } else if (bit == '1') {
                encoded_payload += bit1_utf8;
            } else {
                throw EncodingException("Invalid bit value: " + std::string(1, bit));
            }
        }

        // Wrap payload with control markers
        std::string encoded_message;
        encoded_message += control_start_utf8;
        encoded_message += encoded_payload;
        encoded_message += control_end_utf8;

        // If carrier text is provided, embed the encoded message
        if (!carrier.empty()) {
            // Check if carrier contains control characters
            std::string control_start_utf8 = "\xE2\x81\xA0";
            std::string control_end_utf8 = "\xE2\x81\xA3";
            if (carrier.find(control_start_utf8) != std::string::npos ||
                carrier.find(control_end_utf8) != std::string::npos) {
                throw EncodingException(
                    "Carrier text contains control characters. "
                    "This may cause decoding issues.");
            }

            // Insert after first character
            if (carrier.length() > 0) {
                return carrier.substr(0, 1) + encoded_message + carrier.substr(1);
            }
        }

        return encoded_message;
    } catch (const StegoException&) {
        throw;
    } catch (const std::exception& e) {
        throw EncodingException(std::string("Encoding failed: ") + e.what());
    }
}

} // namespace whitespace_stego

