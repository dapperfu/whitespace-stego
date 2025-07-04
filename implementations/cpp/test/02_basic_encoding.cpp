#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include "Message.hpp"
#include "Carrier.hpp"

void test_01_simple_encode_decode() {
    std::cout << "02_basic_encoding: Testing simple encode/decode..." << std::endl;
    std::string message = "Hello, World!";
    std::string carrier = "This is the carrier text.";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    std::vector<std::string> decoded = Message::decode(encoded, "");
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Simple encode/decode works" << std::endl;
}

void test_02_empty_carrier() {
    std::cout << "02_basic_encoding: Testing empty carrier..." << std::endl;
    std::string message = "Test message";
    std::string carrier = "";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    std::vector<std::string> decoded = Message::decode(encoded, "");
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Empty carrier works" << std::endl;
}

void test_03_multiple_messages() {
    std::cout << "02_basic_encoding: Testing multiple messages..." << std::endl;
    std::string message1 = "First message";
    std::string message2 = "Second message";
    std::string carrier = "Carrier text";
    
    Message msg1(message1);
    std::string encoded1 = msg1.encode(carrier, "");
    
    Message msg2(message2);
    std::string encoded2 = msg2.encode(encoded1, "");
    
    std::vector<std::string> decoded = Message::decode(encoded2, "");
    
    assert(decoded.size() >= 2);
    assert(decoded[0] == message1);
    assert(decoded[1] == message2);
    std::cout << "✓ Multiple messages work" << std::endl;
}

void test_04_unicode_characters() {
    std::cout << "02_basic_encoding: Testing unicode characters..." << std::endl;
    std::string message = "Hello 世界! 🌍";
    std::string carrier = "Carrier with unicode: 测试";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    std::vector<std::string> decoded = Message::decode(encoded, "");
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Unicode characters work" << std::endl;
}

void test_05_long_message() {
    std::cout << "02_basic_encoding: Testing long message..." << std::endl;
    std::string message(1000, 'A');
    std::string carrier = "Short carrier";
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    std::vector<std::string> decoded = Message::decode(encoded, "");
    
    assert(!decoded.empty());
    assert(decoded[0] == message);
    std::cout << "✓ Long message works" << std::endl;
}

int main() {
    std::cout << "Running 02_basic_encoding..." << std::endl;
    
    test_01_simple_encode_decode();
    test_02_empty_carrier();
    test_03_multiple_messages();
    test_04_unicode_characters();
    test_05_long_message();
    
    std::cout << "✓ All 02_basic_encoding tests passed!" << std::endl;
    return 0;
} 