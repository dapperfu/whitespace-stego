#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include "Message.hpp"
#include "Carrier.hpp"

void print_usage() {
    std::cout << "whitespace-stego-cpp - Zero-width character steganography tool\n\n";
    std::cout << "Usage:\n";
    std::cout << "  whitespace-stego-cpp <command> [options]\n\n";
    std::cout << "Commands:\n";
    std::cout << "  encode    Encode a message into carrier text\n";
    std::cout << "  decode    Decode messages from carrier text\n";
    std::cout << "  help      Show this help message\n\n";
    std::cout << "Encode options:\n";
    std::cout << "  -m, --message <text>       Message to encode (mutually exclusive with -mf/--message-file)\n";
    std::cout << "  -mf, --message-file <path> Message file path (mutually exclusive with -m/--message)\n";
    std::cout << "  -cf, --carrier-file <path> Carrier file path\n";
    std::cout << "  -o, --output <path>        Output file path (default: stdout)\n";
    std::cout << "  -p, --password <text>      Password for encryption\n\n";
    std::cout << "Decode options:\n";
    std::cout << "  -cf, --carrier-file <path> Carrier file path (required)\n";
    std::cout << "  -o, --output <path>        Output file path (default: stdout)\n";
    std::cout << "  -p, --password <text>      Password for decryption\n\n";
    std::cout << "Examples:\n";
    std::cout << "  whitespace-stego-cpp encode -m \"Hello, World!\" -cf carrier.txt -o encoded.txt\n";
    std::cout << "  whitespace-stego-cpp encode -mf message.txt -cf carrier.txt -o encoded.txt\n";
    std::cout << "  whitespace-stego-cpp encode -m \"Secret\" -cf carrier.txt -p \"mypassword\" -o encoded.txt\n";
    std::cout << "  whitespace-stego-cpp decode -cf encoded.txt\n";
    std::cout << "  whitespace-stego-cpp decode -cf encoded.txt -p \"mypassword\" -o decoded.txt\n";
}

std::string read_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("Failed to open file: " + path);
    return std::string((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
}

void write_file(const std::string& path, const std::string& data) {
    std::ofstream out(path);
    if (!out) throw std::runtime_error("Failed to write file: " + path);
    out << data;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage();
        return 1;
    }
    std::string command = argv[1];
    std::transform(command.begin(), command.end(), command.begin(), ::tolower);
    if (command == "help" || command == "--help" || command == "-h") {
        print_usage();
        return 0;
    }
    if (command == "encode") {
        std::string message, message_file, carrier_file, output_file, password;
        for (int i = 2; i < argc; ++i) {
            std::string arg = argv[i];
            if ((arg == "-m" || arg == "--message") && i + 1 < argc) {
                message = argv[++i];
            } else if ((arg == "-mf" || arg == "--message-file") && i + 1 < argc) {
                message_file = argv[++i];
            } else if ((arg == "-cf" || arg == "--carrier-file") && i + 1 < argc) {
                carrier_file = argv[++i];
            } else if ((arg == "-o" || arg == "--output") && i + 1 < argc) {
                output_file = argv[++i];
            } else if ((arg == "-p" || arg == "--password") && i + 1 < argc) {
                password = argv[++i];
            } else {
                std::cerr << "Unknown or incomplete option: " << arg << std::endl;
                print_usage();
                return 1;
            }
        }
        if (!message.empty() && !message_file.empty()) {
            std::cerr << "Cannot specify both -m/--message and -mf/--message-file." << std::endl;
            return 1;
        }
        if (message.empty() && !message_file.empty()) {
            message = read_file(message_file);
        }
        if (message.empty()) {
            std::cerr << "Message must not be empty." << std::endl;
            return 1;
        }
        if (carrier_file.empty()) {
            std::cerr << "Carrier file (-cf/--carrier-file) is required." << std::endl;
            return 1;
        }
        std::string carrier = read_file(carrier_file);
        Message msg(message);
        std::string encoded = msg.encode(carrier, password);
        if (!output_file.empty()) {
            write_file(output_file, encoded);
        } else {
            std::cout << encoded << std::endl;
        }
        return 0;
    } else if (command == "decode") {
        std::string carrier_file, output_file, password;
        for (int i = 2; i < argc; ++i) {
            std::string arg = argv[i];
            if ((arg == "-cf" || arg == "--carrier-file") && i + 1 < argc) {
                carrier_file = argv[++i];
            } else if ((arg == "-o" || arg == "--output") && i + 1 < argc) {
                output_file = argv[++i];
            } else if ((arg == "-p" || arg == "--password") && i + 1 < argc) {
                password = argv[++i];
            } else {
                std::cerr << "Unknown or incomplete option: " << arg << std::endl;
                print_usage();
                return 1;
            }
        }
        if (carrier_file.empty()) {
            std::cerr << "Carrier file (-cf/--carrier-file) is required." << std::endl;
            return 1;
        }
        std::string carrier = read_file(carrier_file);
        Message msg(""); // Create empty message for decoding
        std::vector<std::string> messages = msg.decode(carrier, password);
        std::string output;
        for (const auto& msg : messages) {
            output += msg + "\n";
        }
        if (!output_file.empty()) {
            write_file(output_file, output);
        } else {
            std::cout << output;
        }
        return 0;
    } else {
        std::cerr << "Unknown command: " << command << std::endl;
        print_usage();
        return 1;
    }
} 