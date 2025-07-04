#include <iostream>
#include <cassert>
#include <string>
#include "Message.hpp"
#include "Carrier.hpp"

void test_01_message_creation() {
    std::cout << "01_smoke_tests: Testing Message creation..." << std::endl;
    Message msg("Hello, World!");
    assert(msg.getText() == "Hello, World!");
    std::cout << "✓ Message creation works" << std::endl;
}

void test_02_carrier_creation() {
    std::cout << "01_smoke_tests: Testing Carrier creation..." << std::endl;
    Carrier carrier("This is carrier text");
    assert(carrier.getText() == "This is carrier text");
    std::cout << "✓ Carrier creation works" << std::endl;
}

void test_03_message_setter() {
    std::cout << "01_smoke_tests: Testing Message setter..." << std::endl;
    Message msg;
    msg.setText("New message");
    assert(msg.getText() == "New message");
    std::cout << "✓ Message setter works" << std::endl;
}

void test_04_carrier_setter() {
    std::cout << "01_smoke_tests: Testing Carrier setter..." << std::endl;
    Carrier carrier;
    carrier.setText("New carrier");
    assert(carrier.getText() == "New carrier");
    std::cout << "✓ Carrier setter works" << std::endl;
}

void test_05_empty_message() {
    std::cout << "01_smoke_tests: Testing empty message..." << std::endl;
    Message msg("");
    assert(msg.getText().empty());
    std::cout << "✓ Empty message works" << std::endl;
}

int main() {
    std::cout << "Running 01_smoke_tests..." << std::endl;
    
    test_01_message_creation();
    test_02_carrier_creation();
    test_03_message_setter();
    test_04_carrier_setter();
    test_05_empty_message();
    
    std::cout << "✓ All 01_smoke_tests passed!" << std::endl;
    return 0;
} 