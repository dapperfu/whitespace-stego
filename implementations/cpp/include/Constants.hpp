#ifndef CONSTANTS_HPP
#define CONSTANTS_HPP

#include <string>

/**
 * @namespace Constants
 * @brief Protocol and marker constants for whitespace steganography.
 */
namespace Constants {
    // Zero-width markers
    const std::string START_MARKER = "\u200b\u200b\u200d\u200d";
    const std::string END_MARKER   = "\u200b\u200d\u200d\u200b";
    // Add other protocol constants as needed
}

#endif // CONSTANTS_HPP 