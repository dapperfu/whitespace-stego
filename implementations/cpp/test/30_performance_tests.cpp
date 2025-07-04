#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <chrono>
#include <iomanip>
#include "Message.hpp"
#include "Crypto.hpp"
#include "Utils.hpp"

void test_01_encoding_performance() {
    std::cout << "30_performance_tests: Testing encoding performance..." << std::endl;
    
    std::vector<size_t> sizes = {100, 1000, 10000, 100000};
    
    for (size_t size : sizes) {
        std::string message(size, 'A');
        std::string carrier(size / 2, 'B');
        
        auto start = std::chrono::high_resolution_clock::now();
        
        Message msg(message);
        std::string encoded = msg.encode(carrier, "");
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "  " << std::setw(6) << size << " bytes: " 
                  << std::setw(8) << duration.count() << " μs" << std::endl;
    }
    
    std::cout << "✓ Encoding performance test completed" << std::endl;
}

void test_02_decoding_performance() {
    std::cout << "30_performance_tests: Testing decoding performance..." << std::endl;
    
    std::vector<size_t> sizes = {100, 1000, 10000, 100000};
    
    for (size_t size : sizes) {
        std::string message(size, 'A');
        std::string carrier(size / 2, 'B');
        
        Message msg(message);
        std::string encoded = msg.encode(carrier, "");
        
        auto start = std::chrono::high_resolution_clock::now();
        
        std::vector<std::string> decoded = Message::decode(encoded, "");
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        assert(!decoded.empty());
        assert(decoded[0] == message);
        
        std::cout << "  " << std::setw(6) << size << " bytes: " 
                  << std::setw(8) << duration.count() << " μs" << std::endl;
    }
    
    std::cout << "✓ Decoding performance test completed" << std::endl;
}

void test_03_crypto_performance() {
    std::cout << "30_performance_tests: Testing crypto performance..." << std::endl;
    
    std::vector<size_t> sizes = {100, 1000, 10000, 100000};
    std::string password = "test_password";
    
    for (size_t size : sizes) {
        std::string message(size, 'A');
        
        auto start = std::chrono::high_resolution_clock::now();
        
        std::string encrypted = Crypto::encrypt(message, password);
        std::string decrypted = Crypto::decrypt(encrypted, password);
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        assert(decrypted == message);
        
        std::cout << "  " << std::setw(6) << size << " bytes: " 
                  << std::setw(8) << duration.count() << " μs" << std::endl;
    }
    
    std::cout << "✓ Crypto performance test completed" << std::endl;
}

void test_04_base64_performance() {
    std::cout << "30_performance_tests: Testing base64 performance..." << std::endl;
    
    std::vector<size_t> sizes = {100, 1000, 10000, 100000};
    
    for (size_t size : sizes) {
        std::string data(size, 'A');
        
        auto start = std::chrono::high_resolution_clock::now();
        
        std::string encoded = Utils::base64Encode(data);
        std::string decoded = Utils::base64Decode(encoded);
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        assert(decoded == data);
        
        std::cout << "  " << std::setw(6) << size << " bytes: " 
                  << std::setw(8) << duration.count() << " μs" << std::endl;
    }
    
    std::cout << "✓ Base64 performance test completed" << std::endl;
}

void test_05_zero_width_performance() {
    std::cout << "30_performance_tests: Testing zero-width performance..." << std::endl;
    
    std::vector<size_t> sizes = {100, 1000, 10000, 100000};
    
    for (size_t size : sizes) {
        std::string data(size, 'A');
        
        auto start = std::chrono::high_resolution_clock::now();
        
        std::string zw = Utils::toZeroWidth(data);
        std::string converted = Utils::fromZeroWidth(zw);
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        assert(converted == data);
        
        std::cout << "  " << std::setw(6) << size << " bytes: " 
                  << std::setw(8) << duration.count() << " μs" << std::endl;
    }
    
    std::cout << "✓ Zero-width performance test completed" << std::endl;
}

void test_06_memory_usage() {
    std::cout << "30_performance_tests: Testing memory usage..." << std::endl;
    
    // Simple memory usage test - in a real implementation you'd use platform-specific APIs
    // Reduced sizes to stay within security limits
    std::string large_message(500000, 'A'); // 500KB (reduced from 1MB)
    std::string large_carrier(250000, 'B');  // 250KB (reduced from 500KB)
    
    Message msg(large_message);
    std::string encoded = msg.encode(large_carrier, "");
    
    std::cout << "  Large message encoded successfully" << std::endl;
    std::cout << "  Original size: " << large_message.size() << " bytes" << std::endl;
    std::cout << "  Encoded size: " << encoded.size() << " bytes" << std::endl;
    
    std::cout << "✓ Memory usage test completed" << std::endl;
}

int main() {
    std::cout << "Running 30_performance_tests..." << std::endl;
    
    test_01_encoding_performance();
    test_02_decoding_performance();
    test_03_crypto_performance();
    test_04_base64_performance();
    test_05_zero_width_performance();
    test_06_memory_usage();
    
    std::cout << "✓ All 30_performance_tests passed!" << std::endl;
    return 0;
} 