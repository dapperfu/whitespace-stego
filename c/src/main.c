#include "../include/whitespace_stego.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <errno.h>

#define BUFFER_SIZE 4096

static void print_usage(const char* program_name) {
    fprintf(stderr, "Usage: %s [OPTIONS] [CARRIER]\n", program_name);
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -e, --encode MESSAGE    Encode MESSAGE into carrier text\n");
    fprintf(stderr, "  -d, --decode           Decode message from carrier text\n");
    fprintf(stderr, "  -p, --password PASS    Use password for encryption/decryption\n");
    fprintf(stderr, "  -h, --help             Show this help message\n");
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
    const char* program_name = argv[0];
    const char* message = NULL;
    const char* password = NULL;
    bool decode_mode = false;
    char* carrier = NULL;
    char* result = NULL;
    int ret = 1;

    static struct option long_options[] = {
        {"encode", required_argument, 0, 'e'},
        {"decode", no_argument, 0, 'd'},
        {"password", required_argument, 0, 'p'},
        {"help", no_argument, 0, 'h'},
        {0, 0, 0, 0}
    };

    int opt;
    int option_index = 0;
    while ((opt = getopt_long(argc, argv, "e:dp:h", long_options, &option_index)) != -1) {
        switch (opt) {
            case 'e':
                message = optarg;
                break;
            case 'd':
                decode_mode = true;
                break;
            case 'p':
                password = optarg;
                break;
            case 'h':
                print_usage(program_name);
                return 0;
            default:
                print_usage(program_name);
                return 1;
        }
    }

    // Check for required arguments
    if (!message && !decode_mode) {
        fprintf(stderr, "Error: Either --encode or --decode must be specified\n");
        print_usage(program_name);
        return 1;
    }

    // Read carrier text
    if (optind < argc) {
        carrier = read_file(argv[optind]);
    } else {
        carrier = read_stdin();
    }

    if (!carrier) {
        fprintf(stderr, "Error: Failed to read carrier text\n");
        return 1;
    }

    // Process the text
    bool success;
    if (decode_mode) {
        success = whitespace_stego_decode(carrier, password, &result);
    } else {
        success = whitespace_stego_encode(carrier, message, password, &result);
    }

    if (success && result) {
        printf("%s", result);
        ret = 0;
    } else {
        fprintf(stderr, "Error: Failed to %s message\n", 
                decode_mode ? "decode" : "encode");
        const char* err = whitespace_stego_last_error();
        if (err && err[0]) {
            fprintf(stderr, "Details: %s\n", err);
        }
    }

    // Cleanup
    free(carrier);
    whitespace_stego_free(result);

    return ret;
} 