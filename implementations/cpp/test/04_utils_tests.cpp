#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include "Utils.hpp"

void test_01_base64_encode_decode() {
    std::cout << "04_utils_tests: Testing base64 encode/decode..." << std::endl;
    std::string original = "Hello, World!";
    std::string encoded = Utils::base64Encode(original);
    std::string decoded = Utils::base64Decode(encoded);
    
    assert(decoded == original);
    assert(encoded != original); // Should be different
    std::cout << "✓ Base64 encode/decode works" << std::endl;
}

void test_02_base64_empty_string() {
    std::cout << "04_utils_tests: Testing base64 empty string..." << std::endl;
    std::string original = "";
    std::string encoded = Utils::base64Encode(original);
    std::string decoded = Utils::base64Decode(encoded);
    
    assert(decoded == original);
    std::cout << "✓ Base64 empty string works" << std::endl;
}

void test_03_zero_width_conversion() {
    std::cout << "04_utils_tests: Testing zero-width conversion..." << std::endl;
    std::string original = "Test data";
    std::string zw = Utils::toZeroWidth(original);
    std::string converted = Utils::fromZeroWidth(zw);
    
    assert(converted == original);
    assert(zw != original); // Should be different
    std::cout << "✓ Zero-width conversion works" << std::endl;
}

void test_04_zero_width_empty() {
    std::cout << "04_utils_tests: Testing zero-width empty..." << std::endl;
    std::string original = "";
    std::string zw = Utils::toZeroWidth(original);
    std::string converted = Utils::fromZeroWidth(zw);
    
    assert(converted == original);
    std::cout << "✓ Zero-width empty works" << std::endl;
}

void test_05_string_split() {
    std::cout << "04_utils_tests: Testing string split..." << std::endl;
    std::string input = "a,b,c,d";
    std::vector<std::string> result = Utils::split(input, ",");
    
    assert(result.size() == 4);
    assert(result[0] == "a");
    assert(result[1] == "b");
    assert(result[2] == "c");
    assert(result[3] == "d");
    std::cout << "✓ String split works" << std::endl;
}

void test_06_string_split_empty() {
    std::cout << "04_utils_tests: Testing string split empty..." << std::endl;
    std::string input = "";
    std::vector<std::string> result = Utils::split(input, ",");
    
    assert(result.size() == 1);
    assert(result[0] == "");
    std::cout << "✓ String split empty works" << std::endl;
}

void test_07_string_split_no_delimiter() {
    std::cout << "04_utils_tests: Testing string split no delimiter..." << std::endl;
    std::string input = "hello";
    std::vector<std::string> result = Utils::split(input, ",");
    
    assert(result.size() == 1);
    assert(result[0] == "hello");
    std::cout << "✓ String split no delimiter works" << std::endl;
}

int main() {
    std::cout << "Running 04_utils_tests..." << std::endl;
    
    test_01_base64_encode_decode();
    test_02_base64_empty_string();
    test_03_zero_width_conversion();
    test_04_zero_width_empty();
    test_05_string_split();
    test_06_string_split_empty();
    test_07_string_split_no_delimiter();
    
    std::cout << "✓ All 04_utils_tests passed!" << std::endl;
    return 0;
} 