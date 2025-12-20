#include <iostream>
#include <string>
#include "../include/whitespace_stego.hpp"

using namespace whitespace_stego;

void print_usage(const char *program_name) {
    std::cerr << "Usage: " << program_name << " <encode|decode> [options]\n";
    std::cerr << "\nCommands:\n";
    std::cerr << "  encode <message> [-c <carrier>]  Encode a message\n";
    std::cerr << "  decode <encoded>                   Decode a message\n";
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }

    std::string command = argv[1];

    try {
        if (command == "encode") {
            if (argc < 3) {
                std::cerr << "Error: message required for encode\n";
                return 1;
            }

            std::string message = argv[2];
            std::string carrier;

            // Check for carrier option
            for (int i = 3; i < argc; i++) {
                std::string arg = argv[i];
                if ((arg == "-c" || arg == "--carrier") && i + 1 < argc) {
                    carrier = argv[i + 1];
                    break;
                }
            }

            std::string encoded = WhitespaceStego::encode(message, carrier);
            std::cout << encoded << std::endl;
            return 0;

        } else if (command == "decode") {
            if (argc < 3) {
                std::cerr << "Error: encoded text required for decode\n";
                return 1;
            }

            std::string encoded_text = argv[2];
            std::string decoded = WhitespaceStego::decode(encoded_text);
            std::cout << decoded << std::endl;
            return 0;

        } else {
            std::cerr << "Unknown command: " << command << std::endl;
            return 1;
        }
    } catch (const StegoException &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}

