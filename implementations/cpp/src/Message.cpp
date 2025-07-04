#include "Message.hpp"
#include "Encoder.hpp"
#include "Decoder.hpp"
#include "Crypto.hpp"

Message::Message(const std::string& text) : text_(text) {}
Message::~Message() {}

std::string Message::encode(const std::string& carrier, const std::string& password) {
    // TODO: Use Encoder and Crypto to encode this->text_ into carrier
    return Encoder::encode(text_, carrier, password);
}

std::vector<std::string> Message::decode(const std::string& carrier, const std::string& password) {
    // TODO: Use Decoder and Crypto to decode messages from carrier
    return Decoder::decode(carrier, password);
}

std::string Message::encrypt(const std::string& password) const {
    // TODO: Use Crypto to encrypt text_
    return Crypto::encrypt(text_, password);
}

std::string Message::decrypt(const std::string& encrypted, const std::string& password) {
    // TODO: Use Crypto to decrypt encrypted
    return Crypto::decrypt(encrypted, password);
}

const std::string& Message::getText() const {
    return text_;
}

void Message::setText(const std::string& text) {
    text_ = text;
} 