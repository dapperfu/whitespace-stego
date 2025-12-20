#include "whitespace_stego.hpp"
#include <sstream>
#include <algorithm>
#include <stdexcept>
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

// Base64 decoding
static int base64_char_index(char c) {
    if (c >= 'A' && c <= 'Z') return c - 'A';
    if (c >= 'a' && c <= 'z') return c - 'a' + 26;
    if (c >= '0' && c <= '9') return c - '0' + 52;
    if (c == '+') return 62;
    if (c == '/') return 63;
    return -1;
}

static std::vector<unsigned char> base64_decode(const std::string& encoded) {
    std::vector<unsigned char> ret;
    size_t input_len = encoded.length();
    size_t padding = 0;

    if (input_len % 4 != 0) {
        throw std::runtime_error("Invalid Base64 length");
    }

    if (input_len > 0 && encoded[input_len - 1] == '=') {
        padding++;
        if (input_len > 1 && encoded[input_len - 2] == '=') {
            padding++;
        }
    }

    size_t output_len = (input_len / 4) * 3 - padding;
    ret.reserve(output_len);

    for (size_t i = 0, j = 0; i < input_len; i += 4, j += 3) {
        int c1 = base64_char_index(encoded[i]);
        int c2 = base64_char_index(encoded[i + 1]);
        int c3 = (i + 2 < input_len && encoded[i + 2] != '=')
                     ? base64_char_index(encoded[i + 2])
                     : -1;
        int c4 = (i + 3 < input_len && encoded[i + 3] != '=')
                     ? base64_char_index(encoded[i + 3])
                     : -1;

        if (c1 < 0 || c2 < 0) {
            throw std::runtime_error("Invalid Base64 character");
        }

        ret.push_back((c1 << 2) | (c2 >> 4));
        if (c3 >= 0) {
            ret.push_back(((c2 & 0x0f) << 4) | (c3 >> 2));
            if (c4 >= 0) {
                ret.push_back(((c3 & 0x03) << 6) | c4);
            }
        }
    }

    return ret;
}

std::string WhitespaceStego::decode(const std::string& encoded_text) {
    try {
        // Find control markers (UTF-8 encoded)
        std::string control_start_utf8 = "\xE2\x81\xA0";  // U+2060
        std::string control_end_utf8 = "\xE2\x81\xA3";    // U+2063
        std::string bit0_utf8 = "\xE2\x80\x8B";           // U+200B
        std::string bit1_utf8 = "\xE2\x80\x8C";           // U+200C
        
        size_t start_idx = encoded_text.find(control_start_utf8);
        size_t end_idx = encoded_text.find(control_end_utf8);

        if (start_idx == std::string::npos) {
            throw DecodingException("CONTROL_START marker (U+2060) not found");
        }
        if (end_idx == std::string::npos) {
            throw DecodingException("CONTROL_END marker (U+2063) not found");
        }

        // Extract payload (between markers, excluding markers)
        size_t payload_start = start_idx + control_start_utf8.length();
        std::string payload = encoded_text.substr(payload_start, end_idx - payload_start);

        // Check if payload is empty
        if (payload.empty()) {
            return "";
        }

        // Convert invisible characters to binary bits
        std::string binary_bits;
        for (size_t i = 0; i < payload.length(); ) {
            if (i + bit0_utf8.length() <= payload.length() &&
                payload.substr(i, bit0_utf8.length()) == bit0_utf8) {
                binary_bits += '0';
                i += bit0_utf8.length();
            } else if (i + bit1_utf8.length() <= payload.length() &&
                       payload.substr(i, bit1_utf8.length()) == bit1_utf8) {
                binary_bits += '1';
                i += bit1_utf8.length();
            } else {
                throw DecodingException(
                    "Invalid character in payload. Only U+200B and U+200C are allowed.");
            }
        }

        // Check if payload is complete (divisible by 8)
        if (binary_bits.length() % 8 != 0) {
            throw DecodingException(
                "Incomplete payload: " + std::to_string(binary_bits.length()) +
                " bits (must be divisible by 8)");
        }

        // Group bits into 8-bit bytes
        std::vector<unsigned char> bytes_list;
        for (size_t i = 0; i < binary_bits.length(); i += 8) {
            unsigned char byte = 0;
            for (int j = 0; j < 8; j++) {
                char bit = binary_bits[i + j];
                if (bit == '1') {
                    byte |= (1 << (7 - j));
                } else if (bit != '0') {
                    throw DecodingException("Invalid bit value: " + std::string(1, bit));
                }
            }
            bytes_list.push_back(byte);
        }

        // Convert bytes to Base64 string
        std::string base64_str(bytes_list.begin(), bytes_list.end());

        // Decode Base64 to UTF-8 bytes
        std::vector<unsigned char> utf8_bytes = base64_decode(base64_str);

        // Decode UTF-8 bytes to original message
        std::string message(utf8_bytes.begin(), utf8_bytes.end());
        return message;
    } catch (const StegoException&) {
        throw;
    } catch (const std::exception& e) {
        throw DecodingException(std::string("Decoding failed: ") + e.what());
    }
}

} // namespace whitespace_stego

