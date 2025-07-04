#ifndef CARRIER_HPP
#define CARRIER_HPP

#include <string>

/**
 * @class Carrier
 * @brief Handles carrier text for steganography.
 */
class Carrier {
public:
    Carrier(const std::string& text = "");
    ~Carrier();

    // Load carrier text from a file
    static std::string loadFromFile(const std::string& filename);

    // Save carrier text to a file
    static void saveToFile(const std::string& filename, const std::string& data);

    // Get the carrier text
    const std::string& getText() const;
    void setText(const std::string& text);

private:
    std::string text_;
};

#endif // CARRIER_HPP 