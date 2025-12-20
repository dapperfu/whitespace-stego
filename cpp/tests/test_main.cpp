#include <iostream>
#include <cassert>
#include "../include/whitespace_stego.hpp"

using namespace whitespace_stego;

void test_encode_decode() {
    std::string message = "Hello, World!";
    
    std::cout << "Testing encode..." << std::endl;
    std::string encoded = WhitespaceStego::encode(message);
    assert(!encoded.empty());
    std::cout << "Encoded length: " << encoded.length() << std::endl;
    
    std::cout << "Testing decode..." << std::endl;
    std::string decoded = WhitespaceStego::decode(encoded);
    
    assert(decoded == message);
    std::cout << "Round-trip test passed!" << std::endl;
}

void test_unicode() {
    std::string message = "Hello 🌍 你好";
    
    std::string encoded = WhitespaceStego::encode(message);
    std::string decoded = WhitespaceStego::decode(encoded);
    
    assert(decoded == message);
    std::cout << "Unicode test passed!" << std::endl;
}

int main() {
    std::cout << "Running whitespace-stego C++ tests..." << std::endl << std::endl;
    
    try {
        test_encode_decode();
        test_unicode();
        std::cout << std::endl << "All tests passed!" << std::endl;
        return 0;
    } catch (const StegoException& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}

