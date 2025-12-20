#ifndef WHITESPACE_STEGO_H
#define WHITESPACE_STEGO_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Error codes */
#define STEGO_SUCCESS 0
#define STEGO_ERROR_ENCODING 1
#define STEGO_ERROR_DECODING 2
#define STEGO_ERROR_INVALID_PAYLOAD 3
#define STEGO_ERROR_MISSING_MARKER 4
#define STEGO_ERROR_INVALID_BASE64 5
#define STEGO_ERROR_INVALID_UTF8 6
#define STEGO_ERROR_MEMORY 7

/* Encode a message into invisible Unicode characters.
 *
 * Parameters:
 *   message: Input message to encode (UTF-8)
 *   carrier: Optional carrier text (NULL for no carrier)
 *   output: Output buffer (must be allocated by caller)
 *   output_size: Size of output buffer
 *   output_len: Pointer to receive actual output length
 *
 * Returns:
 *   STEGO_SUCCESS on success, error code on failure
 */
int whitespace_encode(const char *message, const char *carrier,
                      char *output, size_t output_size, size_t *output_len);

/* Decode a message from invisible Unicode characters.
 *
 * Parameters:
 *   encoded_text: Input encoded text
 *   output: Output buffer (must be allocated by caller)
 *   output_size: Size of output buffer
 *   output_len: Pointer to receive actual output length
 *
 * Returns:
 *   STEGO_SUCCESS on success, error code on failure
 */
int whitespace_decode(const char *encoded_text,
                      char *output, size_t output_size, size_t *output_len);

/* Get error message for error code */
const char *whitespace_error_string(int error_code);

#ifdef __cplusplus
}
#endif

#endif /* WHITESPACE_STEGO_H */

