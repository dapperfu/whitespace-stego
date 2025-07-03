cmake_minimum_required(VERSION 3.10)
project(whitespace_stego_c_tests)

# Set C standard
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Compiler flags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -O2 -fPIC")

# Find required packages
find_package(OpenSSL REQUIRED)

# Include directories
include_directories(../include)

# Source files
set(SOURCES
    ../src/whitespace_stego.c
    ../src/crypto.c
    ../src/encode.c
    ../src/decode.c
    ../src/utils.c
)

# Test executable
add_executable(test-c test-c.c ${SOURCES})
target_link_libraries(test-c OpenSSL::SSL OpenSSL::Crypto)

# Enable testing
enable_testing()

# Add test
add_test(NAME whitespace_stego_c_tests COMMAND test-c)

# Set test properties
set_tests_properties(whitespace_stego_c_tests PROPERTIES
    TIMEOUT 300
    ENVIRONMENT "LC_ALL=C.UTF-8"
) 