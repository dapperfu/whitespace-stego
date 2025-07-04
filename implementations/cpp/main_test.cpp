#include <iostream>
#include <fstream>
#include <string>
#include "include/Message.hpp"

std::string read_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("Failed to open file: " + path);
    return std::string((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
}

void write_file(const std::string& path, const std::string& data) {
    std::ofstream out(path);
    if (!out) throw std::runtime_error("Failed to write file: " + path);
    out << data;
}

int main() {
    std::string output_file = "main_test_output.txt";
    
    std::cout << "Testing main.cpp logic with hardcoded strings..." << std::endl;
    
    // Use hardcoded strings like debug test
    std::string message = "Secret message for testing";
    std::string carrier = "This is a test carrier text for steganography.";
    
    std::cout << "Message: '" << message << "'" << std::endl;
    std::cout << "Carrier: '" << carrier << "'" << std::endl;
    
    // Encode
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    
    std::cout << "Encoded length: " << encoded.length() << std::endl;
    
    // Write to file
    write_file(output_file, encoded);
    
    std::cout << "Written to: " << output_file << std::endl;
    
    // Read back and check
    std::string read_back = read_file(output_file);
    std::cout << "Read back length: " << read_back.length() << std::endl;
    std::cout << "Read back matches: " << (read_back == encoded ? "YES" : "NO") << std::endl;
    
    return 0;
} 