#ifndef CONSTANTS_HPP
#define CONSTANTS_HPP

#include <string>

/**
 * @namespace Constants
 * @brief Protocol and marker constants for whitespace steganography.
 * 
 * These constants match the standard protocol used by Python, C, Rust, and Go implementations.
 */
namespace Constants {
    // Zero-width Unicode characters
    const std::string ZWSP = "\u200b";     // Zero-width space (U+200B)
    const std::string ZWJ = "\u200d";      // Zero-width joiner (U+200D)
    const std::string ZWNJ = "\u200c";     // Zero-width non-joiner (U+200C)
    const std::string ZWNBSP = "\ufeff";   // Zero-width no-break space (U+FEFF)
    
    // Protocol markers (single codepoints, canonical - matches C/Rust/Go implementations)
    const std::string ZERO_BIT = ZWSP;
    const std::string ONE_BIT = ZWJ;
    const std::string START_MARKER = ZWNBSP;  // Single character, not combination
    const std::string END_MARKER = ZWNJ;      // Single character, not combination
    
    const int BITS_PER_CHAR = 8;
}

#endif // CONSTANTS_HPP 