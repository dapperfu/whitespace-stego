#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include "../include/whitespace_stego.hpp"

using namespace whitespace_stego;

void print_usage(const char *program_name) {
    std::cerr << "Usage: " << program_name << " <encode|decode> [options]\n";
    std::cerr << "\nCommands:\n";
    std::cerr << "  encode [message] [-i <input>] [-o <output>] [-c <carrier>] [-p <password>]\n";
    std::cerr << "  decode [encoded] [-i <input>] [-o <output>] [-p <password>]\n";
    std::cerr << "\nOptions:\n";
    std::cerr << "  -i, --input <file>   Input file (use '-' for stdin)\n";
    std::cerr << "  -o, --output <file>  Output file (use '-' for stdout)\n";
    std::cerr << "  -c, --carrier <text> Carrier text (encode only)\n";
    std::cerr << "  -p, --password <pwd> Password for encryption/decryption\n";
}

std::string get_arg(int argc, char *argv[], const char *flag) {
    for (int i = 0; i < argc; i++) {
        if (std::string(argv[i]) == flag && i + 1 < argc) {
            return argv[i + 1];
        }
    }
    return "";
}

std::string read_input(const std::string& input_path) {
    if (input_path == "-") {
        std::stringstream buffer;
        buffer << std::cin.rdbuf();
        return buffer.str();
    }
    std::ifstream file(input_path);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to read file: " + input_path);
    }
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void write_output(const std::string& output_path, const std::string& content) {
    if (output_path == "-") {
        std::cout << content;
    } else {
        std::ofstream file(output_path);
        if (!file.is_open()) {
            throw std::runtime_error("Failed to write file: " + output_path);
        }
        file << content;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }

    std::string command = argv[1];

    try {
        if (command == "encode") {
            std::string input = get_arg(argc - 2, &argv[2], "-i");
            if (input.empty()) input = get_arg(argc - 2, &argv[2], "--input");
            std::string output = get_arg(argc - 2, &argv[2], "-o");
            if (output.empty()) output = get_arg(argc - 2, &argv[2], "--output");
            std::string carrier = get_arg(argc - 2, &argv[2], "-c");
            if (carrier.empty()) carrier = get_arg(argc - 2, &argv[2], "--carrier");
            std::string password = get_arg(argc - 2, &argv[2], "-p");
            if (password.empty()) password = get_arg(argc - 2, &argv[2], "--password");

            std::string message;
            if (!input.empty()) {
                message = read_input(input);
            } else if (argc >= 3) {
                if (std::string(argv[2]) == "-") {
                    message = read_input("-");
                } else {
                    message = argv[2];
                }
            } else {
                std::cerr << "Error: message required (provide as argument, -i/--input, or '-' for stdin)\n";
                return 1;
            }

            std::string encoded = WhitespaceStego::encode(message, carrier, password);
            
            if (!output.empty()) {
                write_output(output, encoded + "\n");
            } else {
                std::cout << encoded << std::endl;
            }
            return 0;

        } else if (command == "decode") {
            std::string input = get_arg(argc - 2, &argv[2], "-i");
            if (input.empty()) input = get_arg(argc - 2, &argv[2], "--input");
            std::string output = get_arg(argc - 2, &argv[2], "-o");
            if (output.empty()) output = get_arg(argc - 2, &argv[2], "--output");
            std::string password = get_arg(argc - 2, &argv[2], "-p");
            if (password.empty()) password = get_arg(argc - 2, &argv[2], "--password");

            std::string encoded_text;
            if (!input.empty()) {
                encoded_text = read_input(input);
            } else if (argc >= 3) {
                if (std::string(argv[2]) == "-") {
                    encoded_text = read_input("-");
                } else {
                    encoded_text = argv[2];
                }
            } else {
                std::cerr << "Error: encoded text required (provide as argument, -i/--input, or '-' for stdin)\n";
                return 1;
            }

            std::string decoded = WhitespaceStego::decode(encoded_text, password);
            
            if (!output.empty()) {
                write_output(output, decoded + "\n");
            } else {
                std::cout << decoded << std::endl;
            }
            return 0;

        } else {
            std::cerr << "Unknown command: " << command << std::endl;
            return 1;
        }
    } catch (const StegoException &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}

