#include "Carrier.hpp"
#include <fstream>
#include <stdexcept>

Carrier::Carrier(const std::string& text) : text_(text) {}
Carrier::~Carrier() {}

std::string Carrier::loadFromFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file: " + filename);
    }
    
    return std::string((std::istreambuf_iterator<char>(file)), 
                       std::istreambuf_iterator<char>());
}

void Carrier::saveToFile(const std::string& filename, const std::string& data) {
    std::ofstream file(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to create file: " + filename);
    }
    
    file << data;
}

const std::string& Carrier::getText() const {
    return text_;
}

void Carrier::setText(const std::string& text) {
    text_ = text;
} 