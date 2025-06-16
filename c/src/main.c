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
    fprintf(stderr, "Usage: %s [options]\n", program_name);
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -v, --verbose     Enable verbose output\n");
    fprintf(stderr, "  -e, --encode      Encode mode\n");
    fprintf(stderr, "  -d, --decode      Decode mode\n");
    fprintf(stderr, "  -m, --message     Message to encode\n");
    fprintf(stderr, "  -c, --carrier     Carrier text\n");
    fprintf(stderr, "  -p, --password    Password for encryption\n");
    fprintf(stderr, "  -h, --help        Show this help message\n");
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

static char* read_stdin(void) {
    char* buffer = NULL;
    size_t buffer_size = 0;
    size_t buffer_pos = 0;
    char temp[BUFFER_SIZE];
    size_t bytes_read;

    while ((bytes_read = fread(temp, 1, sizeof(temp), stdin)) > 0) {
        if (buffer_pos + bytes_read > buffer_size) {
            size_t new_size = buffer_size == 0 ? BUFFER_SIZE : buffer_size * 2;
            while (buffer_pos + bytes_read > new_size) {
                new_size *= 2;
            }
            char* new_buffer = realloc(buffer, new_size);
            if (!new_buffer) {
                free(buffer);
                return NULL;
            }
            buffer = new_buffer;
            buffer_size = new_size;
        }
        memcpy(buffer + buffer_pos, temp, bytes_read);
        buffer_pos += bytes_read;
    }

    if (buffer) {
        buffer[buffer_pos] = '\0';
    }
    return buffer;
}

int main(int argc, char* argv[]) {
    bool encode_mode = false;
    bool decode_mode = false;
    char* message = NULL;
    char* carrier = NULL;
    char* password = NULL;
    
    // Parse command line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) {
            verbose = true;
        } else if (strcmp(argv[i], "-e") == 0 || strcmp(argv[i], "--encode") == 0) {
            encode_mode = true;
        } else if (strcmp(argv[i], "-d") == 0 || strcmp(argv[i], "--decode") == 0) {
            decode_mode = true;
        } else if (strcmp(argv[i], "-m") == 0 || strcmp(argv[i], "--message") == 0) {
            if (i + 1 < argc) {
                message = argv[++i];
            }
        } else if (strcmp(argv[i], "-c") == 0 || strcmp(argv[i], "--carrier") == 0) {
            if (i + 1 < argc) {
                carrier = argv[++i];
            }
        } else if (strcmp(argv[i], "-p") == 0 || strcmp(argv[i], "--password") == 0) {
            if (i + 1 < argc) {
                password = argv[++i];
            }
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return 0;
        }
    }
    
    // Validate arguments
    if (encode_mode && decode_mode) {
        fprintf(stderr, "Error: Cannot specify both encode and decode modes\n");
        return 1;
    }
    
    if (!encode_mode && !decode_mode) {
        fprintf(stderr, "Error: Must specify either encode or decode mode\n");
        return 1;
    }
    
    if (encode_mode) {
        if (!message) {
            fprintf(stderr, "Error: Message required for encode mode\n");
            return 1;
        }
        
        debug_log("Encoding message: %s", message);
        debug_log("Using carrier: %s", carrier);
        debug_log("Using password: %s", password ? password : "None");
        
        char* result = NULL;
        if (!whitespace_stego_encode(message, carrier, password, &result)) {
            fprintf(stderr, "Error: %s\n", whitespace_stego_get_last_error());
            return 1;
        }
        
        debug_log("Final encoded message: %s", result);
        printf("%s\n", result);
        free(result);
        return 0;
    }
    
    if (decode_mode) {
        if (!carrier) {
            fprintf(stderr, "Error: Carrier text required for decode mode\n");
            return 1;
        }
        
        debug_log("Decoding carrier: %s", carrier);
        debug_log("Using password: %s", password ? password : "None");
        
        char* result = NULL;
        if (!whitespace_stego_decode(carrier, password, &result)) {
            fprintf(stderr, "Error: %s\n", whitespace_stego_get_last_error());
            return 1;
        }
        
        debug_log("Decoded message: %s", result);
        printf("%s\n", result);
        free(result);
        return 0;
    }
    
    return 0;
} 