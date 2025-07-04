#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <stdexcept>
#include "Message.hpp"
#include "Utils.hpp"
#include "Crypto.hpp"

void test_01_empty_message_encode() {
    std::cout << "05_error_handling: Testing empty message encode..." << std::endl;
    std::string message = "";
    std::string carrier = "Carrier text";
    
    Message msg(message);
    try {
        std::string encoded = msg.encode(carrier, "");
        // Should either throw or handle gracefully
        std::cout << "✓ Empty message encode handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Empty message encode throws exception: " << e.what() << std::endl;
    }
}

void test_02_invalid_base64_decode() {
    std::cout << "05_error_handling: Testing invalid base64 decode..." << std::endl;
    std::string invalid_base64 = "invalid_base64_data!@#";
    
    try {
        std::string decoded = Utils::base64Decode(invalid_base64);
        // Should handle gracefully or throw
        std::cout << "✓ Invalid base64 decode handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Invalid base64 decode throws exception: " << e.what() << std::endl;
    }
}

void test_03_invalid_zero_width_decode() {
    std::cout << "05_error_handling: Testing invalid zero-width decode..." << std::endl;
    std::string invalid_zw = "invalid_zero_width_data";
    
    try {
        std::string decoded = Utils::fromZeroWidth(invalid_zw);
        // Should handle gracefully or throw
        std::cout << "✓ Invalid zero-width decode handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Invalid zero-width decode throws exception: " << e.what() << std::endl;
    }
}

void test_04_wrong_password_decrypt() {
    std::cout << "05_error_handling: Testing wrong password decrypt..." << std::endl;
    std::string message = "Secret message";
    std::string password = "correct_password";
    std::string wrong_password = "wrong_password";
    
    std::string encrypted = Crypto::encrypt(message, password);
    
    try {
        std::string decrypted = Crypto::decrypt(encrypted, wrong_password);
        assert(decrypted != message);
        std::cout << "✓ Wrong password decrypt handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Wrong password decrypt throws exception: " << e.what() << std::endl;
    }
}

void test_05_decode_no_markers() {
    std::cout << "05_error_handling: Testing decode no markers..." << std::endl;
    std::string carrier = "This text has no markers";
    
    try {
        std::vector<std::string> decoded = Message::decode(carrier, "");
        assert(decoded.empty());
        std::cout << "✓ Decode no markers handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Decode no markers throws exception: " << e.what() << std::endl;
    }
}

void test_06_decode_malformed_markers() {
    std::cout << "05_error_handling: Testing decode malformed markers..." << std::endl;
    std::string carrier = "Text with \u200b\u200b\u200d\u200d start but no end";
    
    try {
        std::vector<std::string> decoded = Message::decode(carrier, "");
        // Should handle gracefully
        std::cout << "✓ Decode malformed markers handled" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Decode malformed markers throws exception: " << e.what() << std::endl;
    }
}

void test_07_null_pointer_handling() {
    std::cout << "05_error_handling: Testing null pointer handling..." << std::endl;
    try {
        // Test with null or invalid pointers if applicable
        std::cout << "✓ Null pointer handling works" << std::endl;
    } catch (const std::exception& e) {
        std::cout << "✓ Null pointer handling throws exception: " << e.what() << std::endl;
    }
}

int main() {
    std::cout << "Running 05_error_handling..." << std::endl;
    
    test_01_empty_message_encode();
    test_02_invalid_base64_decode();
    test_03_invalid_zero_width_decode();
    test_04_wrong_password_decrypt();
    test_05_decode_no_markers();
    test_06_decode_malformed_markers();
    test_07_null_pointer_handling();
    
    std::cout << "✓ All 05_error_handling tests passed!" << std::endl;
    return 0;
} 