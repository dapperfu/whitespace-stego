#include "../include/whitespace_stego.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <errno.h>
#include <stdbool.h>
#include <stdarg.h>

#define BUFFER_SIZE 4096

static bool verbose = false;

static void print_usage(const char* program_name) {
    fprintf(stdout, "Usage: %s [OPTIONS] COMMAND [ARGS]...\n\n", program_name);
    fprintf(stdout, "Whitespace steganography tool for encoding and decoding messages.\n\n");
    fprintf(stdout, "Options:\n");
    fprintf(stdout, "  -v, --verbose                  Enable verbose output\n");
    fprintf(stdout, "  -h, --help                     Show this message and exit\n\n");
    fprintf(stdout, "Commands:\n");
    fprintf(stdout, "  encode                         Encode a message into a carrier file\n");
    fprintf(stdout, "  decode                         Decode a message from a carrier file\n");
    fprintf(stdout, "  help                           Show this message or the help of the given subcommand\n");
}

static void print_encode_usage(const char* program_name) {
    fprintf(stdout, "Usage: %s encode [OPTIONS]\n\n", program_name);
    fprintf(stdout, "Encode a message into a carrier file using whitespace steganography.\n\n");
    fprintf(stdout, "Options:\n");
    fprintf(stdout, "  -m, --message-file PATH       Path to the file containing the message to encode [required]\n");
    fprintf(stdout, "  -c, --carrier-file PATH       Path to the carrier file [optional, empty if not provided]\n");
    fprintf(stdout, "  -o, --output PATH             Path where the encoded file will be saved [required]\n");
    fprintf(stdout, "  -p, --password TEXT           Optional password for encryption\n");
    fprintf(stdout, "  -h, --help                    Show this message and exit\n");
}

static void print_decode_usage(const char* program_name) {
    fprintf(stdout, "Usage: %s decode [OPTIONS]\n\n", program_name);
    fprintf(stdout, "Decode a message from a carrier file using whitespace steganography.\n\n");
    fprintf(stdout, "Options:\n");
    fprintf(stdout, "  -c, --carrier-file PATH       Path to the encoded carrier file [required]\n");
    fprintf(stdout, "  -o, --output PATH             Path where the decoded message will be saved [required]\n");
    fprintf(stdout, "  -p, --password TEXT           Optional password for decryption\n");
    fprintf(stdout, "  -h, --help                    Show this message and exit\n");
}

static void debug_log(const char* format, ...) {
    if (!verbose) return;
    
    va_list args;
    va_start(args, format);
    fprintf(stderr, "DEBUG: ");
    vfprintf(stderr, format, args);
    fprintf(stderr, "\n");
    va_end(args);
}

static char* read_file(const char* filename, size_t* data_len) {
    FILE* file = fopen(filename, "rb");
    if (!file) {
        fprintf(stderr, "Error opening file '%s': %s\n", filename, strerror(errno));
        return NULL;
    }

    char* buffer = NULL;
    size_t buffer_size = 0;
    size_t buffer_pos = 0;
    char temp[BUFFER_SIZE];
    size_t bytes_read;

    while ((bytes_read = fread(temp, 1, sizeof(temp), file)) > 0) {
        if (buffer_pos + bytes_read > buffer_size) {
            size_t new_size = buffer_size == 0 ? BUFFER_SIZE : buffer_size * 2;
            while (buffer_pos + bytes_read > new_size) {
                new_size *= 2;
            }
            char* new_buffer = realloc(buffer, new_size);
            if (!new_buffer) {
                free(buffer);
                fclose(file);
                return NULL;
            }
            buffer = new_buffer;
            buffer_size = new_size;
        }
        memcpy(buffer + buffer_pos, temp, bytes_read);
        buffer_pos += bytes_read;
    }

    if (ferror(file)) {
        free(buffer);
        fclose(file);
        return NULL;
    }

    // Handle empty files - return empty buffer instead of NULL
    if (!buffer) {
        buffer = malloc(1);
        if (!buffer) {
            fclose(file);
            return NULL;
        }
        buffer_pos = 0;
    }
    
    *data_len = buffer_pos;
    fclose(file);
    return buffer;
}

static bool write_file(const char* filename, const char* content, size_t content_len) {
    FILE* file = fopen(filename, "wb");
    if (!file) {
        fprintf(stderr, "Error opening file '%s' for writing: %s\n", filename, strerror(errno));
        return false;
    }
    
    size_t written = fwrite(content, 1, content_len, file);
    fclose(file);
    
    if (written != content_len) {
        fprintf(stderr, "Error writing to file '%s'\n", filename);
        return false;
    }
    
    return true;
}

static int handle_encode(int argc, char* argv[]) {
    char* message_file = NULL;
    char* carrier_file = NULL;
    char* output_file = NULL;
    char* password = NULL;
    
    // Parse encode-specific arguments
    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 || strcmp(argv[i], "--message-file") == 0) {
            if (i + 1 < argc) {
                message_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
            if (i + 1 < argc) {
                carrier_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0) {
            if (i + 1 < argc) {
                output_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-p") == 0 || strcmp(argv[i], "--password") == 0) {
            if (i + 1 < argc) {
                password = argv[++i];
            }
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_encode_usage(argv[0]);
            return 0;
        }
    }
    
    // Validate required arguments
    if (!message_file) {
        fprintf(stderr, "Error: --message-file is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    if (!output_file) {
        fprintf(stderr, "Error: --output is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    // Read input files
    size_t message_len, carrier_len;
    char* message = read_file(message_file, &message_len);
    if (!message) {
        return 1;
    }
    
    char* carrier = NULL;
    if (carrier_file) {
        carrier = read_file(carrier_file, &carrier_len);
        if (!carrier) {
            free(message);
            return 1;
        }
    } else {
        // No carrier file provided, use empty carrier
        carrier = malloc(1);
        if (!carrier) {
            free(message);
            return 1;
        }
        carrier[0] = '\0';
        carrier_len = 0;
    }
    
    // Check for empty message with humorous error
    if (message_len == 0) {
        fprintf(stderr, "🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!\n");
        free(message);
        free(carrier);
        return 1;
    }
    
    debug_log("Encoding message from file: %s", message_file);
    if (carrier_file) {
        debug_log("Using carrier from file: %s", carrier_file);
    } else {
        debug_log("Using empty carrier (no carrier file provided)");
    }
    debug_log("Using password: %s", password ? password : "None");
    debug_log("Carrier length: %zu bytes", carrier_len);
    if (carrier_len > 0) {
        debug_log("First carrier byte: 0x%02x", (unsigned char)carrier[0]);
        if (carrier_len > 1) debug_log("Second carrier byte: 0x%02x", (unsigned char)carrier[1]);
        if (carrier_len > 2) debug_log("Third carrier byte: 0x%02x", (unsigned char)carrier[2]);
        if (carrier_len > 3) debug_log("Fourth carrier byte: 0x%02x", (unsigned char)carrier[3]);
    }
    
    // Encode the message
    char* result = NULL;
    if (!whitespace_stego_encode(carrier, carrier_len, message, password, &result)) {
        fprintf(stderr, "Error encoding message: %s\n", whitespace_stego_last_error());
        free(message);
        free(carrier);
        return 1;
    }
    
    // Write the result
    size_t result_len = strlen(result);
    if (!write_file(output_file, result, result_len)) {
        free(message);
        free(carrier);
        free(result);
        return 1;
    }
    
    fprintf(stdout, "Message successfully encoded into %s\n", output_file);
    
    // Cleanup
    free(message);
    free(carrier);
    free(result);
    return 0;
}

static int handle_decode(int argc, char* argv[]) {
    char* carrier_file = NULL;
    char* output_file = NULL;
    char* password = NULL;
    
    // Parse decode-specific arguments
    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
            if (i + 1 < argc) {
                carrier_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0) {
            if (i + 1 < argc) {
                output_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-p") == 0 || strcmp(argv[i], "--password") == 0) {
            if (i + 1 < argc) {
                password = argv[++i];
            }
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_decode_usage(argv[0]);
            return 0;
        }
    }
    
    // Validate required arguments
    if (!carrier_file) {
        fprintf(stderr, "Error: --carrier-file is required\n");
        print_decode_usage(argv[0]);
        return 1;
    }
    
    if (!output_file) {
        fprintf(stderr, "Error: --output is required\n");
        print_decode_usage(argv[0]);
        return 1;
    }
    
    // Read carrier file
    size_t carrier_len;
    char* carrier = read_file(carrier_file, &carrier_len);
    if (!carrier) {
        return 1;
    }
    
    debug_log("Decoding message from file: %s", carrier_file);
    debug_log("Using password: %s", password ? password : "None");
    
    // Decode all messages
    char** results = NULL;
    size_t result_count = 0;
    if (!whitespace_stego_decode_all(carrier, carrier_len, password, &results, &result_count)) {
        fprintf(stderr, "Error decoding message: %s\n", whitespace_stego_last_error());
        free(carrier);
        return 1;
    }
    
    // Prepare output content
    char* output_content = NULL;
    size_t output_len = 0;
    
    if (result_count == 1) {
        // Single message - output as is
        output_content = strdup(results[0]);
        output_len = strlen(output_content);
    } else {
        // Multiple messages - output each on a separate line
        // Calculate total length needed
        size_t total_len = 0;
        for (size_t i = 0; i < result_count; i++) {
            total_len += strlen(results[i]) + 1; // +1 for newline
        }
        
        output_content = malloc(total_len + 1);
        if (!output_content) {
            whitespace_stego_free_all(results, result_count);
            free(carrier);
            return 1;
        }
        
        char* pos = output_content;
        for (size_t i = 0; i < result_count; i++) {
            size_t msg_len = strlen(results[i]);
            memcpy(pos, results[i], msg_len);
            pos += msg_len;
            *pos++ = '\n';
        }
        *pos = '\0';
        output_len = pos - output_content;
    }
    
    // Write the result
    if (!write_file(output_file, output_content, output_len)) {
        whitespace_stego_free_all(results, result_count);
        free(carrier);
        free(output_content);
        return 1;
    }
    
    if (result_count == 1) {
        fprintf(stdout, "Message successfully decoded into %s\n", output_file);
    } else {
        fprintf(stdout, "%zu messages successfully decoded into %s\n", result_count, output_file);
    }
    
    // Cleanup
    whitespace_stego_free_all(results, result_count);
    free(carrier);
    free(output_content);
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }
    
    // Check for global options
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = true;
            // Remove the verbose flag from argv
            for (int j = i; j < argc - 1; j++) {
                argv[j] = argv[j + 1];
            }
            argc--;
            i--;
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return 0;
        }
    }
    
    // Parse command
    if (argc < 2) {
        fprintf(stderr, "Error: No command specified\n");
        print_usage(argv[0]);
        return 1;
    }
    
    char* command = argv[1];
    
    if (strcmp(command, "encode") == 0) {
        return handle_encode(argc - 2, argv + 2);
    } else if (strcmp(command, "decode") == 0) {
        return handle_decode(argc - 2, argv + 2);
    } else if (strcmp(command, "help") == 0) {
        if (argc >= 3) {
            char* subcommand = argv[2];
            if (strcmp(subcommand, "encode") == 0) {
                print_encode_usage(argv[0]);
                return 0;
            } else if (strcmp(subcommand, "decode") == 0) {
                print_decode_usage(argv[0]);
                return 0;
            }
        }
        print_usage(argv[0]);
        return 0;
    } else {
        fprintf(stderr, "Unknown command: %s\n", command);
        fprintf(stderr, "Use --help for usage information\n");
        return 1;
    }
} 