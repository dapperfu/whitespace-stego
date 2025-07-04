/*
 * Whitespace Steganography Library Header
 * 
 * Common definitions and structures for whitespace steganography
 */

#ifndef WHITESPACE_STEGO_H
#define WHITESPACE_STEGO_H

#include <stddef.h>

// Common buffer sizes for different implementations
#define MAX_BUFFER_SIZE_TINY     (4 * 1024)        // 4 KiB
#define MAX_BUFFER_SIZE_SMALL    (1024 * 1024)     // 1 MiB
#define MAX_BUFFER_SIZE_STANDARD (4ULL * 1024 * 1024 * 1024)  // 4 GiB
#define MAX_BUFFER_SIZE_LARGE    (4ULL * 1024 * 1024 * 1024)  // 4 GiB

// Maximum number of messages for multi-message decoding
#define MAX_MESSAGES_TINY        10
#define MAX_MESSAGES_SMALL       100
#define MAX_MESSAGES_STANDARD    1000
#define MAX_MESSAGES_LARGE       1000

// Common return codes
#define WHITESPACE_STEGO_SUCCESS 1
#define WHITESPACE_STEGO_ERROR   0

// Common error handling
extern char* whitespace_stego_last_error(void);

#endif // WHITESPACE_STEGO_H 