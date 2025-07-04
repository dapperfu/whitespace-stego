#include <iostream>
#include <string>
#include "include/Message.hpp"
#include "include/Constants.hpp"

int main() {
    std::string message = "Secret message for testing";
    std::string carrier = "This is a test carrier text for steganography.";
    
    std::cout << "Testing Message class..." << std::endl;
    std::cout << "Message: " << message << std::endl;
    std::cout << "Carrier: " << carrier << std::endl;
    
    Message msg(message);
    std::string encoded = msg.encode(carrier, "");
    std::cout << "Encoded length: " << encoded.length() << std::endl;
    
    // Check if markers are present
    std::string start_marker = Constants::START_MARKER;
    std::string end_marker = Constants::END_MARKER;
    
    size_t start_pos = encoded.find(start_marker);
    size_t end_pos = encoded.find(end_marker);
    
    std::cout << "START_MARKER found at: " << start_pos << std::endl;
    std::cout << "END_MARKER found at: " << end_pos << std::endl;
    
    if (start_pos != std::string::npos && end_pos != std::string::npos) {
        std::cout << "Markers found! Message encoding successful." << std::endl;
    } else {
        std::cout << "Markers not found! Message encoding failed." << std::endl;
    }
    
    return 0;
} 