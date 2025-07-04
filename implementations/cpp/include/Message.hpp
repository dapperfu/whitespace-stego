#ifndef MESSAGE_HPP
#define MESSAGE_HPP

#include <string>
#include <vector>

/**
 * @class Message
 * @brief Represents a steganographic message with encode, decode, encrypt, and decrypt functionality.
 */
class Message {
public:
    Message(const std::string& text = "");
    ~Message();

    // Encode the message into a carrier
    std::string encode(const std::string& carrier, const std::string& password = "");

    // Decode a message from a carrier
    static std::vector<std::string> decode(const std::string& carrier, const std::string& password = "");

    // Encrypt the message with a password
    std::string encrypt(const std::string& password) const;

    // Decrypt the message with a password
    static std::string decrypt(const std::string& encrypted, const std::string& password);

    // Get the message text
    const std::string& getText() const;
    void setText(const std::string& text);

private:
    std::string text_;
};

#endif // MESSAGE_HPP 