/*
 * Static C CLI Implementation: main_static.c
 * This file provides a command-line interface for the static implementation.
 * Uses pre-allocated buffers instead of dynamic memory allocation.
 */

#include "../include/whitespace_stego_static.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Buffer sizes for CLI operations
#define MAX_CARRIER_SIZE (4 * 1024 * 1024)  // 4MB
#define MAX_MESSAGE_SIZE (1024 * 1024)      // 1MB
#define MAX_RESULT_SIZE (4 * 1024 * 1024)   // 4MB

static char carrier_buffer[MAX_CARRIER_SIZE];
static char message_buffer[MAX_MESSAGE_SIZE];
static char result_buffer[MAX_RESULT_SIZE];

void print_usage(const char* program_name) {
    printf("Usage: %s [OPTIONS] COMMAND [ARGS]...\n\n", program_name);
    printf("Whitespace steganography tool for encoding and decoding messages.\n\n");
    printf("Options:\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Commands:\n");
    printf("  encode                         Encode a message into a carrier file\n");
    printf("  decode                         Decode a message from a carrier file\n");
    printf("  help                           Show this message or the help of the given subcommand\n\n");
    printf("Examples:\n");
    printf("  %s encode --message-file message.txt --carrier-file carrier.txt --output encoded.txt\n", program_name);
    printf("  %s encode --message \"Hello World\" --carrier-file carrier.txt --output encoded.txt\n", program_name);
    printf("  %s encode --message \"Secret\" --carrier-file carrier.txt --password \"mypass\" --output encoded.txt\n", program_name);
    printf("  %s decode --carrier-file encoded.txt --output decoded.txt\n", program_name);
    printf("  %s decode --carrier-file encoded.txt --password \"mypass\" --output decoded.txt\n", program_name);
}

void print_encode_usage(const char* program_name) {
    printf("Usage: %s encode [OPTIONS]\n\n", program_name);
    printf("Encode a message into a carrier file.\n\n");
    printf("Options:\n");
    printf("  -m, --message <text>           Message to encode (mutually exclusive with -mf/--message-file)\n");
    printf("  -mf, --message-file <path>     Message file path (mutually exclusive with -m/--message)\n");
    printf("  -cf, --carrier-file <path>     Carrier file path\n");
    printf("  -o, --output <path>            Output file path (default: stdout)\n");
    printf("  -p, --password <text>          Password for encryption\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Examples:\n");
    printf("  %s encode -m \"Hello World\" -cf carrier.txt -o encoded.txt\n", program_name);
    printf("  %s encode -mf message.txt -cf carrier.txt -o encoded.txt\n", program_name);
    printf("  %s encode -m \"Secret\" -cf carrier.txt -p \"mypassword\" -o encoded.txt\n", program_name);
}

void print_decode_usage(const char* program_name) {
    printf("Usage: %s decode [OPTIONS]\n\n", program_name);
    printf("Decode a message from a carrier file.\n\n");
    printf("Options:\n");
    printf("  -cf, --carrier-file <path>     Carrier file path (required)\n");
    printf("  -o, --output <path>            Output file path (default: stdout)\n");
    printf("  -p, --password <text>          Password for decryption\n");
    printf("  -v, --verbose                  Enable verbose output\n");
    printf("  -h, --help                     Show this message and exit\n\n");
    printf("Examples:\n");
    printf("  %s decode -cf encoded.txt -o decoded.txt\n", program_name);
    printf("  %s decode -cf encoded.txt -p \"mypassword\" -o decoded.txt\n", program_name);
}

int read_file(const char* filename, char* buffer, size_t buffer_size) {
    FILE* file = fopen(filename, "rb");
    if (!file) {
        fprintf(stderr, "Error: Cannot open file '%s'\n", filename);
        return 0;
    }
    
    size_t bytes_read = fread(buffer, 1, buffer_size - 1, file);
    fclose(file);
    
    if (bytes_read == 0) {
        fprintf(stderr, "Error: File '%s' is empty or cannot be read\n", filename);
        return 0;
    }
    
    buffer[bytes_read] = '\0';
    return 1;
}

int write_file(const char* filename, const char* data) {
    if (strcmp(filename, "-") == 0) {
        // Write to stdout
        printf("%s", data);
        return 1;
    }
    
    FILE* file = fopen(filename, "wb");
    if (!file) {
        fprintf(stderr, "Error: Cannot create file '%s'\n", filename);
        return 0;
    }
    
    size_t bytes_written = fwrite(data, 1, strlen(data), file);
    fclose(file);
    
    if (bytes_written != strlen(data)) {
        fprintf(stderr, "Error: Failed to write complete data to '%s'\n", filename);
        return 0;
    }
    
    return 1;
}

int encode_command(int argc, char* argv[]) {
    const char* message = NULL;
    const char* message_file = NULL;
    const char* carrier_file = NULL;
    const char* output_file = "-";  // Default to stdout
    const char* password = NULL;
    int verbose = 0;
    
    // Parse arguments
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0 || strcmp(argv[i], "--message") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing message text\n");
                return 1;
            }
            message = argv[++i];
        } else if (strcmp(argv[i], "-mf") == 0 || strcmp(argv[i], "--message-file") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing message file path\n");
                return 1;
            }
            message_file = argv[++i];
        } else if (strcmp(argv[i], "-cf") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing carrier file path\n");
                return 1;
            }
            carrier_file = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing output file path\n");
                return 1;
            }
            output_file = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0 || strcmp(argv[i], "--password") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing password\n");
                return 1;
            }
            password = argv[++i];
        } else if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = 1;
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_encode_usage(argv[0]);
            return 0;
        } else {
            fprintf(stderr, "Error: Unknown option '%s'\n", argv[i]);
            print_encode_usage(argv[0]);
            return 1;
        }
    }
    
    // Validate required arguments
    if (!carrier_file) {
        fprintf(stderr, "Error: Carrier file is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    if (!message && !message_file) {
        fprintf(stderr, "Error: Either message or message file is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    if (message && message_file) {
        fprintf(stderr, "Error: Cannot specify both message and message file\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    // Read carrier file
    if (!read_file(carrier_file, carrier_buffer, sizeof(carrier_buffer))) {
        return 1;
    }
    
    // Get message
    if (message_file) {
        if (!read_file(message_file, message_buffer, sizeof(message_buffer))) {
            return 1;
        }
        message = message_buffer;
    }
    
    if (verbose) {
        printf("Encoding message into carrier...\n");
        if (password) {
            printf("Using password encryption\n");
        }
    }
    
    // Encode message
    if (!whitespace_stego_static_encode(carrier_buffer, strlen(carrier_buffer), 
                                       message, password, result_buffer, sizeof(result_buffer))) {
        fprintf(stderr, "Error: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    // Write result
    if (!write_file(output_file, result_buffer)) {
        return 1;
    }
    
    if (verbose) {
        printf("Message successfully encoded\n");
    }
    
    return 0;
}

int decode_command(int argc, char* argv[]) {
    const char* carrier_file = NULL;
    const char* output_file = "-";  // Default to stdout
    const char* password = NULL;
    int verbose = 0;
    
    // Parse arguments
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "-cf") == 0 || strcmp(argv[i], "--carrier-file") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing carrier file path\n");
                return 1;
            }
            carrier_file = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0 || strcmp(argv[i], "--output") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing output file path\n");
                return 1;
            }
            output_file = argv[++i];
        } else if (strcmp(argv[i], "-p") == 0 || strcmp(argv[i], "--password") == 0) {
            if (i + 1 >= argc) {
                fprintf(stderr, "Error: Missing password\n");
                return 1;
            }
            password = argv[++i];
        } else if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = 1;
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_decode_usage(argv[0]);
            return 0;
        } else {
            fprintf(stderr, "Error: Unknown option '%s'\n", argv[i]);
            print_decode_usage(argv[0]);
            return 1;
        }
    }
    
    // Validate required arguments
    if (!carrier_file) {
        fprintf(stderr, "Error: Carrier file is required\n");
        print_decode_usage(argv[0]);
        return 1;
    }
    
    // Read carrier file
    if (!read_file(carrier_file, carrier_buffer, sizeof(carrier_buffer))) {
        return 1;
    }
    
    if (verbose) {
        printf("Decoding message from carrier...\n");
        if (password) {
            printf("Using password decryption\n");
        }
    }
    
    // Decode message
    if (!whitespace_stego_static_decode(carrier_buffer, strlen(carrier_buffer), 
                                       password, result_buffer, sizeof(result_buffer))) {
        fprintf(stderr, "Error: %s\n", whitespace_stego_static_last_error());
        return 1;
    }
    
    // Write result
    if (!write_file(output_file, result_buffer)) {
        return 1;
    }
    
    if (verbose) {
        printf("Message successfully decoded\n");
    }
    
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }
    
    if (strcmp(argv[1], "encode") == 0) {
        return encode_command(argc, argv);
    } else if (strcmp(argv[1], "decode") == 0) {
        return decode_command(argc, argv);
    } else if (strcmp(argv[1], "help") == 0) {
        if (argc > 2) {
            if (strcmp(argv[2], "encode") == 0) {
                print_encode_usage(argv[0]);
            } else if (strcmp(argv[2], "decode") == 0) {
                print_decode_usage(argv[0]);
            } else {
                fprintf(stderr, "Unknown command '%s'\n", argv[2]);
                print_usage(argv[0]);
                return 1;
            }
        } else {
            print_usage(argv[0]);
        }
        return 0;
    } else if (strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0) {
        print_usage(argv[0]);
        return 0;
    } else {
        fprintf(stderr, "Unknown command '%s'\n", argv[1]);
        print_usage(argv[0]);
        return 1;
    }
} 