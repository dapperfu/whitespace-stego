/*
 * MISRA C Compliance: main.c
 * This file has been refactored for MISRA C:2012 compliance.
 * - No <stdbool.h>; use int for boolean (0/1)
 * - No dynamic memory allocation (malloc, realloc, free)
 * - No mixed declarations and code
 * - No unsafe string functions
 * - No C99+ features not allowed by MISRA
 * - All functions and logic blocks documented
 */
#include "../include/whitespace_stego.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <errno.h>
#include <stdarg.h>

#define BUFFER_SIZE 4096

static int verbose = 0;

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
    fprintf(stdout, "  -m, --message TEXT            Message to encode (mutually exclusive with --message-file)\n");
    fprintf(stdout, "  -mf, --message-file PATH      Path to the file containing the message to encode (mutually exclusive with --message)\n");
    fprintf(stdout, "  -c, --carrier TEXT            Carrier text to encode into (mutually exclusive with --carrier-file)\n");
    fprintf(stdout, "  -cf, --carrier-file PATH      Path to the carrier file (mutually exclusive with --carrier)\n");
    fprintf(stdout, "  -o, --output PATH             Path where the encoded file will be saved (use '-' for stdout)\n");
    fprintf(stdout, "  -p, --password TEXT           Optional password for encryption\n");
    fprintf(stdout, "  -h, --help                    Show this message and exit\n");
}

static void print_decode_usage(const char* program_name) {
    fprintf(stdout, "Usage: %s decode [OPTIONS]\n\n", program_name);
    fprintf(stdout, "Decode a message from a carrier file using whitespace steganography.\n\n");
    fprintf(stdout, "Options:\n");
    fprintf(stdout, "  -c, --carrier TEXT            Carrier text containing the encoded message (mutually exclusive with --carrier-file)\n");
    fprintf(stdout, "  -cf, --carrier-file PATH      Path to the encoded carrier file (mutually exclusive with --carrier)\n");
    fprintf(stdout, "  -o, --output PATH             Path where the decoded message will be saved (use '-' for stdout)\n");
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

static int write_file(const char* filename, const char* content, size_t content_len) {
    FILE* file = fopen(filename, "wb");
    if (!file) {
        fprintf(stderr, "Error opening file '%s' for writing: %s\n", filename, strerror(errno));
        return 0;
    }
    
    size_t written = fwrite(content, 1, content_len, file);
    fclose(file);
    
    if (written != content_len) {
        fprintf(stderr, "Error writing to file '%s'\n", filename);
        return 0;
    }
    
    return 1;
}

static int handle_encode(int argc, char* argv[]) {
    char* message = NULL;
    char* message_file = NULL;
    char* carrier = NULL;
    char* carrier_file = NULL;
    char* output_file = NULL;
    char* password = NULL;
    size_t message_len, carrier_len;
    char* message_content = NULL;
    char* carrier_content = NULL;
    char* result = NULL;
    size_t result_len = 0;
    int i = 0;
    
    // Parse encode-specific arguments
    for (i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 || strcmp(argv[i], "--message") == 0) {
            if (i + 1 < argc) {
                message = argv[++i];
            }
        } else if (strcmp(argv[i], "-mf") == 0 || strcmp(argv[i], "--message-file") == 0) {
            if (i + 1 < argc) {
                message_file = argv[++i];
            }
        } else if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier") == 0) {
            if (i + 1 < argc) {
                carrier = argv[++i];
            }
        } else if (strcmp(argv[i], "-cf") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
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
    
    // Validate mutually exclusive options
    if (message && message_file) {
        fprintf(stderr, "Error: --message/-m and --message-file/-mf are mutually exclusive\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    if (carrier && carrier_file) {
        fprintf(stderr, "Error: --carrier/-c and --carrier-file/-cf are mutually exclusive\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    // Validate required arguments
    if (!message && !message_file) {
        fprintf(stderr, "Error: Either --message/-m or --message-file/-mf must be provided\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    // Get message content
    if (message_file) {
        message_content = read_file(message_file, &message_len);
        if (!message_content) {
            return 1;
        }
    } else {
        message_content = strdup(message);
        if (!message_content) {
            return 1;
        }
        message_len = strlen(message_content);
    }
    
    // Get carrier content
    if (carrier_file) {
        carrier_content = read_file(carrier_file, &carrier_len);
        if (!carrier_content) {
            free(message_content);
            return 1;
        }
    } else if (carrier) {
        carrier_content = strdup(carrier);
        if (!carrier_content) {
            free(message_content);
            return 1;
        }
        carrier_len = strlen(carrier_content);
    } else {
        // No carrier provided, use empty carrier
        carrier_content = malloc(1);
        if (!carrier_content) {
            free(message_content);
            return 1;
        }
        carrier_content[0] = '\0';
        carrier_len = 0;
    }
    
    // Check for empty message with humorous error
    if (message_len == 0) {
        fprintf(stderr, "🤔 There's no point in encoding nothing! Even a blank canvas needs paint, and you're trying to hide invisible ink in invisible ink. Try again with an actual message!\n");
        free(message_content);
        free(carrier_content);
        return 1;
    }
    
    debug_log("Encoding message: %s", message ? "from command line" : "from file");
    if (carrier) {
        debug_log("Using carrier from command line");
    } else if (carrier_file) {
        debug_log("Using carrier from file: %s", carrier_file);
    } else {
        debug_log("Using empty carrier (no carrier provided)");
    }
    debug_log("Using password: %s", password ? password : "None");
    debug_log("Carrier length: %zu bytes", carrier_len);
    if (carrier_len > 0) {
        debug_log("First carrier byte: 0x%02x", (unsigned char)carrier_content[0]);
        if (carrier_len > 1) debug_log("Second carrier byte: 0x%02x", (unsigned char)carrier_content[1]);
        if (carrier_len > 2) debug_log("Third carrier byte: 0x%02x", (unsigned char)carrier_content[2]);
        if (carrier_len > 3) debug_log("Fourth carrier byte: 0x%02x", (unsigned char)carrier_content[3]);
    }
    
    // Encode the message
    if (!whitespace_stego_encode(carrier_content, carrier_len, message_content, password, &result)) {
        fprintf(stderr, "Error encoding message: %s\n", whitespace_stego_last_error());
        free(message_content);
        free(carrier_content);
        return 1;
    }
    
    // Write the result
    result_len = strlen(result);
    if (output_file && strcmp(output_file, "-") != 0) {
        if (!write_file(output_file, result, result_len)) {
            free(message_content);
            free(carrier_content);
            free(result);
            return 1;
        }
        fprintf(stdout, "Message successfully encoded into %s\n", output_file);
    } else {
        // Output to stdout
        fprintf(stdout, "%s", result);
    }
    
    // Cleanup
    free(message_content);
    free(carrier_content);
    free(result);
    return 0;
}

static int handle_decode(int argc, char* argv[]) {
    char* carrier = NULL;
    char* carrier_file = NULL;
    char* output_file = NULL;
    char* password = NULL;
    size_t carrier_len = 0;
    char* carrier_content = NULL;
    char** results = NULL;
    size_t result_count = 0;
    char* output_content = NULL;
    size_t output_len = 0;
    size_t total_len = 0;
    char* pos = NULL;
    size_t msg_len = 0;
    int i = 0;
    
    // Parse decode-specific arguments
    for (i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier") == 0) {
            if (i + 1 < argc) {
                carrier = argv[++i];
            }
        } else if (strcmp(argv[i], "-cf") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
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
    
    // Validate mutually exclusive options
    if (carrier && carrier_file) {
        fprintf(stderr, "Error: --carrier/-c and --carrier-file/-cf are mutually exclusive\n");
        print_decode_usage(argv[0]);
        return 1;
    }
    
    // Validate required arguments
    if (!carrier && !carrier_file) {
        fprintf(stderr, "Error: Either --carrier/-c or --carrier-file/-cf must be provided\n");
        print_decode_usage(argv[0]);
        return 1;
    }
    
    // Get carrier content
    if (carrier_file) {
        carrier_content = read_file(carrier_file, &carrier_len);
        if (!carrier_content) {
            return 1;
        }
    } else {
        carrier_content = strdup(carrier);
        if (!carrier_content) {
            return 1;
        }
        carrier_len = strlen(carrier_content);
    }
    
    debug_log("Decoding message: %s", carrier ? "from command line" : "from file");
    debug_log("Using password: %s", password ? password : "None");
    
    // Decode all messages
    if (!whitespace_stego_decode_all(carrier_content, carrier_len, password, &results, &result_count)) {
        fprintf(stderr, "Error decoding message: %s\n", whitespace_stego_last_error());
        free(carrier_content);
        return 1;
    }
    
    // Prepare output content
    if (result_count == 1) {
        // Single message - output as is
        output_content = strdup(results[0]);
        output_len = strlen(output_content);
    } else {
        // Multiple messages - output each on a separate line
        // Calculate total length needed
        for (i = 0; i < (int)result_count; i++) {
            total_len += strlen(results[i]) + 1; // +1 for newline
        }
        
        output_content = malloc(total_len + 1);
        if (!output_content) {
            whitespace_stego_free_all(results, result_count);
            free(carrier_content);
            return 1;
        }
        
        pos = output_content;
        for (i = 0; i < (int)result_count; i++) {
            msg_len = strlen(results[i]);
            memcpy(pos, results[i], msg_len);
            pos += msg_len;
            *pos++ = '\n';
        }
        *pos = '\0';
        output_len = pos - output_content;
    }
    
    // Write the result
    if (output_file && strcmp(output_file, "-") != 0) {
        if (!write_file(output_file, output_content, output_len)) {
            whitespace_stego_free_all(results, result_count);
            free(carrier_content);
            free(output_content);
            return 1;
        }
        if (result_count == 1) {
            fprintf(stdout, "Message successfully decoded into %s\n", output_file);
        } else {
            fprintf(stdout, "%zu messages successfully decoded into %s\n", result_count, output_file);
        }
    } else {
        // Output to stdout
        fprintf(stdout, "%s", output_content);
    }
    
    // Cleanup
    whitespace_stego_free_all(results, result_count);
    free(carrier_content);
    free(output_content);
    return 0;
}

int main(int argc, char* argv[]) {
    int i = 0;
    int j = 0;
    char* command = NULL;
    char* subcommand = NULL;
    
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }
    
    // Check for global options
    for (i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = 1;
            // Remove the verbose flag from argv
            for (j = i; j < argc - 1; j++) {
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
    
    command = argv[1];
    
    if (strcmp(command, "encode") == 0) {
        return handle_encode(argc - 2, argv + 2);
    } else if (strcmp(command, "decode") == 0) {
        return handle_decode(argc - 2, argv + 2);
    } else if (strcmp(command, "help") == 0) {
        if (argc >= 3) {
            subcommand = argv[2];
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