#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <fstream>
#include <filesystem>
#include "Message.hpp"
#include "Carrier.hpp"
#include "Crypto.hpp"
#include "Utils.hpp"

void test_01_full_encode_decode_cycle() {
    std::cout << "10_integration_tests: Testing full encode/decode cycle..." << std::endl;
    std::string message = "This is a secret message";
    std::string carrier = "This is the carrier text that will contain the hidden message.";
    std::string password = "secret_password_123";
    
    // Encode
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    
    // Decode
    std::vector<std::string> decoded = Message::decode(encoded, password);
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Full encode/decode cycle works" << std::endl;
}

void test_02_file_io_integration() {
    std::cout << "10_integration_tests: Testing file I/O integration..." << std::endl;
    std::string message = "File I/O test message";
    std::string carrier = "Carrier text for file test";
    std::string temp_file = "temp_test_file.txt";
    
    // Write carrier to file
    Carrier::saveToFile(temp_file, carrier);
    
    // Read carrier from file
    std::string loaded_carrier = Carrier::loadFromFile(temp_file);
    assert(loaded_carrier == carrier);
    
    // Encode and decode
    Message msg(message);
    std::string encoded = msg.encode(loaded_carrier, "");
    std::vector<std::string> decoded = Message::decode(encoded, "");
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    
    // Cleanup
    std::filesystem::remove(temp_file);
    std::cout << "✓ File I/O integration works" << std::endl;
}

void test_03_multiple_layers_integration() {
    std::cout << "10_integration_tests: Testing multiple layers integration..." << std::endl;
    std::vector<std::string> messages = {"Layer 1", "Layer 2", "Layer 3"};
    std::string carrier = "Base carrier";
    
    std::string current_carrier = carrier;
    for (const auto& msg_text : messages) {
        Message msg(msg_text);
        current_carrier = msg.encode(current_carrier, "");
    }
    
    // Decode all layers
    std::vector<std::string> decoded = Message::decode(current_carrier, "");
    
    assert(decoded.size() >= messages.size());
    for (size_t i = 0; i < messages.size(); ++i) {
        assert(decoded[i] == messages[i]);
    }
    std::cout << "✓ Multiple layers integration works" << std::endl;
}

void test_04_unicode_integration() {
    std::cout << "10_integration_tests: Testing unicode integration..." << std::endl;
    std::string message = "Unicode message: 世界 🌍 🚀";
    std::string carrier = "Unicode carrier: 测试 文字";
    std::string password = "unicode_password_世界";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    std::vector<std::string> decoded = Message::decode(encoded, password);
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Unicode integration works" << std::endl;
}

void test_05_large_data_integration() {
    std::cout << "10_integration_tests: Testing large data integration..." << std::endl;
    std::string message(5000, 'A'); // 5KB message
    std::string carrier(1000, 'B'); // 1KB carrier
    std::string password = "large_data_password";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, password);
    std::vector<std::string> decoded = Message::decode(encoded, password);
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Large data integration works" << std::endl;
}

void test_06_crypto_integration() {
    std::cout << "10_integration_tests: Testing crypto integration..." << std::endl;
    std::string message = "Crypto integration test";
    std::string password = "crypto_test_password";
    
    // Test encryption/decryption
    std::string encrypted = Crypto::encrypt(message, password);
    std::string decrypted = Crypto::decrypt(encrypted, password);
    assert(decrypted == message);
    
    // Test with Message class
    Message msg(message);
    std::string msg_encrypted = msg.encrypt(password);
    std::string msg_decrypted = Message::decrypt(msg_encrypted, password);
    assert(msg_decrypted == message);
    
    std::cout << "✓ Crypto integration works" << std::endl;
}

int main() {
    std::cout << "Running 10_integration_tests..." << std::endl;
    
    test_01_full_encode_decode_cycle();
    test_02_file_io_integration();
    test_03_multiple_layers_integration();
    test_04_unicode_integration();
    test_05_large_data_integration();
    test_06_crypto_integration();
    
    std::cout << "✓ All 10_integration_tests passed!" << std::endl;
    return 0;
} 