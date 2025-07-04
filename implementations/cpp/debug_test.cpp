#include <iostream>
#include <string>
#include "include/Encoder.hpp"
#include "include/Constants.hpp"

int main() {
    std::string message = "Secret message for testing";
    std::string carrier = "This is a test carrier text for steganography.";
    
    std::cout << "Testing Encoder..." << std::endl;
    std::cout << "Message: " << message << std::endl;
    std::cout << "Carrier: " << carrier << std::endl;
    
    std::string encoded = Encoder::encode(message, carrier, "");
    std::cout << "Encoded length: " << encoded.length() << std::endl;
    
    // Check if markers are present
    std::string start_marker = Constants::START_MARKER;
    std::string end_marker = Constants::END_MARKER;
    
    std::cout << "START_MARKER length: " << start_marker.length() << std::endl;
    std::cout << "END_MARKER length: " << end_marker.length() << std::endl;
    
    size_t start_pos = encoded.find(start_marker);
    size_t end_pos = encoded.find(end_marker);
    
    std::cout << "START_MARKER found at: " << start_pos << std::endl;
    std::cout << "END_MARKER found at: " << end_pos << std::endl;
    
    if (start_pos != std::string::npos && end_pos != std::string::npos) {
        std::cout << "Markers found! Encoding successful." << std::endl;
    } else {
        std::cout << "Markers not found! Encoding failed." << std::endl;
    }
    
    return 0;
} 