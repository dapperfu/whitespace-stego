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
    fprintf(stderr, "Usage: %s [OPTIONS] COMMAND [ARGS]...\n\n", program_name);
    fprintf(stderr, "Whitespace steganography tool for encoding and decoding messages.\n\n");
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -v, --verbose                  Enable verbose output\n");
    fprintf(stderr, "  -h, --help                     Show this message and exit\n\n");
    fprintf(stderr, "Commands:\n");
    fprintf(stderr, "  encode                         Encode a message into a carrier file\n");
    fprintf(stderr, "  decode                         Decode a message from a carrier file\n");
    fprintf(stderr, "  help                           Show this message or the help of the given subcommand\n");
}

static void print_encode_usage(const char* program_name) {
    fprintf(stderr, "Usage: %s encode [OPTIONS]\n\n", program_name);
    fprintf(stderr, "Encode a message into a carrier file using whitespace steganography.\n\n");
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -m, --message-file PATH       Path to the file containing the message to encode [required]\n");
    fprintf(stderr, "  -c, --carrier-file PATH       Path to the carrier file [required]\n");
    fprintf(stderr, "  -o, --output PATH             Path where the encoded file will be saved [required]\n");
    fprintf(stderr, "  -p, --password TEXT           Optional password for encryption\n");
    fprintf(stderr, "  -h, --help                    Show this message and exit\n");
}

static void print_decode_usage(const char* program_name) {
    fprintf(stderr, "Usage: %s decode [OPTIONS]\n\n", program_name);
    fprintf(stderr, "Decode a message from a carrier file using whitespace steganography.\n\n");
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -c, --carrier-file PATH       Path to the encoded carrier file [required]\n");
    fprintf(stderr, "  -o, --output PATH             Path where the decoded message will be saved [required]\n");
    fprintf(stderr, "  -p, --password TEXT           Optional password for decryption\n");
    fprintf(stderr, "  -h, --help                    Show this message and exit\n");
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

static char* read_file(const char* filename) {
    FILE* file = fopen(filename, "r");
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

    if (buffer) {
        buffer[buffer_pos] = '\0';
    }
    fclose(file);
    return buffer;
}

static bool write_file(const char* filename, const char* content) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        fprintf(stderr, "Error opening file '%s' for writing: %s\n", filename, strerror(errno));
        return false;
    }
    
    size_t len = strlen(content);
    size_t written = fwrite(content, 1, len, file);
    fclose(file);
    
    if (written != len) {
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
    
    if (!carrier_file) {
        fprintf(stderr, "Error: --carrier-file is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    if (!output_file) {
        fprintf(stderr, "Error: --output is required\n");
        print_encode_usage(argv[0]);
        return 1;
    }
    
    // Read input files
    char* message = read_file(message_file);
    if (!message) {
        return 1;
    }
    
    char* carrier = read_file(carrier_file);
    if (!carrier) {
        free(message);
        return 1;
    }
    
    debug_log("Encoding message from file: %s", message_file);
    debug_log("Using carrier from file: %s", carrier_file);
    debug_log("Using password: %s", password ? password : "None");
    
    // Encode the message
    char* result = NULL;
    if (!whitespace_stego_encode(carrier, message, password, &result)) {
        fprintf(stderr, "Error encoding message: %s\n", whitespace_stego_last_error());
        free(message);
        free(carrier);
        return 1;
    }
    
    // Write the result
    if (!write_file(output_file, result)) {
        free(message);
        free(carrier);
        free(result);
        return 1;
    }
    
    printf("Message successfully encoded into %s\n", output_file);
    
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
    char* carrier = read_file(carrier_file);
    if (!carrier) {
        return 1;
    }
    
    debug_log("Decoding carrier from file: %s", carrier_file);
    debug_log("Using password: %s", password ? password : "None");
    
    // Decode the message
    char* result = NULL;
    if (!whitespace_stego_decode(carrier, password, &result)) {
        fprintf(stderr, "Error decoding message: %s\n", whitespace_stego_last_error());
        free(carrier);
        return 1;
    }
    
    // Write the result
    if (!write_file(output_file, result)) {
        free(carrier);
        free(result);
        return 1;
    }
    
    printf("Message successfully decoded to %s\n", output_file);
    
    free(carrier);
    free(result);
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage(argv[0]);
        return 1;
    }
    
    // Parse global options
    int global_argc = 0;
    char* global_argv[argc];
    
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = true;
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return 0;
        } else {
            global_argv[global_argc++] = argv[i];
        }
    }
    
    if (global_argc == 0) {
        print_usage(argv[0]);
        return 1;
    }
    
    // Handle subcommands
    if (strcmp(global_argv[0], "encode") == 0) {
        return handle_encode(global_argc - 1, global_argv + 1);
    } else if (strcmp(global_argv[0], "decode") == 0) {
        return handle_decode(global_argc - 1, global_argv + 1);
    } else if (strcmp(global_argv[0], "help") == 0) {
        if (global_argc > 1) {
            if (strcmp(global_argv[1], "encode") == 0) {
                print_encode_usage(argv[0]);
            } else if (strcmp(global_argv[1], "decode") == 0) {
                print_decode_usage(argv[0]);
            } else {
                print_usage(argv[0]);
            }
        } else {
            print_usage(argv[0]);
        }
        return 0;
    } else {
        fprintf(stderr, "Error: Unknown command '%s'\n", global_argv[0]);
        print_usage(argv[0]);
        return 1;
    }
} 