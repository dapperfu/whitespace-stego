/* Error handling */

#include "whitespace_stego.h"

const char *whitespace_error_string(int error_code) {
    switch (error_code) {
        case STEGO_SUCCESS:
            return "Success";
        case STEGO_ERROR_ENCODING:
            return "Encoding error";
        case STEGO_ERROR_DECODING:
            return "Decoding error";
        case STEGO_ERROR_INVALID_PAYLOAD:
            return "Invalid payload";
        case STEGO_ERROR_MISSING_MARKER:
            return "Missing marker";
        case STEGO_ERROR_INVALID_BASE64:
            return "Invalid Base64";
        case STEGO_ERROR_INVALID_UTF8:
            return "Invalid UTF-8";
        case STEGO_ERROR_MEMORY:
            return "Memory error";
        default:
            return "Unknown error";
    }
}

