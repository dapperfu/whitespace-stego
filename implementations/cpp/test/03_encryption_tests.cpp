#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include "Message.hpp"
#include "Crypto.hpp"

void test_01_basic_encryption() {
    std::cout << "03_encryption_tests: Testing basic encryption..." << std::endl;
    std::string message = "Secret message";
    std::string password = "mypassword123";
    
    std::string encrypted = Crypto::encrypt(message, password);
    std::string decrypted = Crypto::decrypt(encrypted, password);
    
    assert(decrypted == message);
    assert(encrypted != message); // Should be different
    std::cout << "✓ Basic encryption works" << std::endl;
}

void test_02_empty_password() {
    std::cout << "03_encryption_tests: Testing empty password..." << std::endl;
    std::string message = "Test message";
    std::string password = "";
    
    std::string encrypted = Crypto::encrypt(message, password);
    std::string decrypted = Crypto::decrypt(encrypted, password);
    
    assert(decrypted == message);
    std::cout << "✓ Empty password works" << std::endl;
}

void test_03_wrong_password() {
    std::cout << "03_encryption_tests: Testing wrong password..." << std::endl;
    std::string message = "Secret message";
    std::string password = "correct_password";
    std::string wrong_password = "wrong_password";
    
    std::string encrypted = Crypto::encrypt(message, password);
    
    // Should throw or return different result
    std::string decrypted = Crypto::decrypt(encrypted, wrong_password);
    assert(decrypted != message);
    std::cout << "✓ Wrong password detection works" << std::endl;
}

void test_04_unicode_encryption() {
    std::cout << "03_encryption_tests: Testing unicode encryption..." << std::endl;
    std::string message = "Secret 世界! 🌍";
    std::string password = "password世界";
    
    std::string encrypted = Crypto::encrypt(message, password);
    std::string decrypted = Crypto::decrypt(encrypted, password);
    
    assert(decrypted == message);
    std::cout << "✓ Unicode encryption works" << std::endl;
}

void test_05_message_encryption_integration() {
    std::cout << "03_encryption_tests: Testing message encryption integration..." << std::endl;
    std::string message = "Secret message";
    std::string carrier = "Carrier text";
    std::string password = "mypassword123";
    
    Message msg(message);
    std::string encrypted = msg.encrypt(password);
    std::string decrypted = Message::decrypt(encrypted, password);
    
    assert(decrypted == message);
    std::cout << "✓ Message encryption integration works" << std::endl;
}

int main() {
    std::cout << "Running 03_encryption_tests..." << std::endl;
    
    test_01_basic_encryption();
    test_02_empty_password();
    test_03_wrong_password();
    test_04_unicode_encryption();
    test_05_message_encryption_integration();
    
    std::cout << "✓ All 03_encryption_tests passed!" << std::endl;
    return 0;
} 