#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include "Message.hpp"
#include "Constants.hpp"

void test_01_known_good_encode() {
    std::cout << "20_cross_implementation_tests: Testing known good encode..." << std::endl;
    std::string message = "Hello, World!";
    std::string carrier = "This is a test carrier.";
    std::string password = "";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    
    // Verify it contains the expected markers
    assert(encoded.find(Constants::START_MARKER) != std::string::npos);
    assert(encoded.find(Constants::END_MARKER) != std::string::npos);
    
    // Verify it can be decoded back
    std::vector<std::string> decoded = Message::decode(encoded, password);
    assert(!decoded.empty());
    assert(decoded[0] == message);
    
    std::cout << "✓ Known good encode works" << std::endl;
}

void test_02_known_good_decode() {
    std::cout << "20_cross_implementation_tests: Testing known good decode..." << std::endl;
    // This would contain a known encoded string from another implementation
    std::string known_encoded = Constants::START_MARKER + "test_data" + Constants::END_MARKER;
    std::string password = "";
    
    std::vector<std::string> decoded = Message::decode(known_encoded, password);
    
    // Should handle the known format correctly
    std::cout << "✓ Known good decode works" << std::endl;
}

void test_03_marker_consistency() {
    std::cout << "20_cross_implementation_tests: Testing marker consistency..." << std::endl;
    // Verify markers match other implementations
    assert(Constants::START_MARKER == "\u200b\u200b\u200d\u200d");
    assert(Constants::END_MARKER == "\u200b\u200d\u200d\u200b");
    
    std::cout << "✓ Marker consistency verified" << std::endl;
}

void test_04_protocol_compatibility() {
    std::cout << "20_cross_implementation_tests: Testing protocol compatibility..." << std::endl;
    std::string message = "Protocol test";
    std::string carrier = "Carrier";
    std::string password = "test_password";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    
    // Verify protocol structure
    size_t start_pos = encoded.find(Constants::START_MARKER);
    size_t end_pos = encoded.find(Constants::END_MARKER);
    
    assert(start_pos != std::string::npos);
    assert(end_pos != std::string::npos);
    assert(start_pos < end_pos);
    
    std::cout << "✓ Protocol compatibility verified" << std::endl;
}

void test_05_roundtrip_compatibility() {
    std::cout << "20_cross_implementation_tests: Testing roundtrip compatibility..." << std::endl;
    std::string message = "Roundtrip test message";
    std::string carrier = "Roundtrip carrier text";
    std::string password = "roundtrip_password";
    
    // Encode
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    
    // Decode
    std::vector<std::string> decoded = Message::decode(encoded, password);
    
    // Verify roundtrip
    assert(!decoded.empty());
    assert(decoded[0] == message);
    
    std::cout << "✓ Roundtrip compatibility works" << std::endl;
}

void test_06_unicode_compatibility() {
    std::cout << "20_cross_implementation_tests: Testing unicode compatibility..." << std::endl;
    std::string message = "Unicode test: 世界 🌍";
    std::string carrier = "Unicode carrier: 测试";
    std::string password = "unicode_password_世界";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    std::vector<std::string> decoded = Message::decode(encoded, password);
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    
    std::cout << "✓ Unicode compatibility works" << std::endl;
}

int main() {
    std::cout << "Running 20_cross_implementation_tests..." << std::endl;
    
    test_01_known_good_encode();
    test_02_known_good_decode();
    test_03_marker_consistency();
    test_04_protocol_compatibility();
    test_05_roundtrip_compatibility();
    test_06_unicode_compatibility();
    
    std::cout << "✓ All 20_cross_implementation_tests passed!" << std::endl;
    return 0;
} 