cmake_minimum_required(VERSION 3.10)
project(whitespace_stego_c)

# Set C standard
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Compiler flags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -O2 -fPIC")

# Find required packages
find_package(OpenSSL REQUIRED)

# Include directories
include_directories(include)

# Load auto-generated buffer size configuration
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/config/buffer_sizes.cmake")
    include("${CMAKE_CURRENT_SOURCE_DIR}/config/buffer_sizes.cmake")
else()
    # Fallback to default sizes if configuration not found
    message(WARNING "Buffer size configuration not found. Run ./configure_buffer_sizes.sh first.")
    set(MAX_DETECTED_BUFFER_SIZE 16777216)  # 16 MiB default
    set(TINY_BUFFER_SIZE 4096)
    set(SMALL_BUFFER_SIZE 1048576)
    set(STANDARD_BUFFER_SIZE 16777216)
    set(LARGE_BUFFER_SIZE 16777216)
endif()

# Source files for static implementations
set(STATIC_SOURCES
    src/crypto.c
    src/utils.c
)

# Main executable (using static implementation)
# add_executable(whitespace-stego-c 
#     src/whitespace_stego_static.c
#     ${STATIC_SOURCES}
#     src/main_static.c
# )
# target_link_libraries(whitespace-stego-c OpenSSL::SSL OpenSSL::Crypto)

# Shared library (using static implementation)
set(LIB_SOURCES
    src/whitespace_stego_static.c
    ${STATIC_SOURCES}
)

add_library(whitespace_stego SHARED ${LIB_SOURCES})
target_link_libraries(whitespace_stego OpenSSL::SSL OpenSSL::Crypto)

# Source files for dynamic implementation
set(DYNAMIC_SOURCES
    src/whitespace_stego.c
    src/crypto.c
    src/utils.c
)

# Test executable (using dynamic implementation)
add_executable(test-c test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_link_libraries(test-c OpenSSL::SSL OpenSSL::Crypto)

# Coverage test executable (using dynamic implementation)
add_executable(test-coverage test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_compile_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)
target_link_libraries(test-coverage OpenSSL::SSL OpenSSL::Crypto)
target_link_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)

# 100% Coverage test executable
add_executable(test-100-coverage test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_compile_options(test-100-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)
target_link_libraries(test-100-coverage OpenSSL::SSL OpenSSL::Crypto)
target_link_options(test-100-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)

# Cross-test executable for static implementations (include all static sources)
add_executable(test-cross-static
    test/cross_test_static.c
    src/whitespace_stego_static.c
    src/whitespace_stego_static_small.c
    src/whitespace_stego_static_large.c
    src/crypto.c
    src/utils.c
)
target_link_libraries(test-cross-static OpenSSL::SSL OpenSSL::Crypto)

# Unity test executable (if Unity is available)
if(EXISTS "test/unity.h")
    add_executable(test-unity test/test_unity.c test/unity.c ${LIB_SOURCES})
    target_link_libraries(test-unity OpenSSL::SSL OpenSSL::Crypto)
endif()

# Enable testing
enable_testing()

# Add tests
add_test(NAME whitespace_stego_c_tests COMMAND test-c)
add_test(NAME whitespace_stego_coverage_tests COMMAND test-coverage)
add_test(NAME whitespace_stego_100_coverage_tests COMMAND test-100-coverage)
add_test(NAME whitespace_stego_cross_static_tests COMMAND test-cross-static)

if(EXISTS "test/unity.h")
    add_test(NAME whitespace_stego_unity_tests COMMAND test-unity)
endif()

# Set test properties
set_tests_properties(whitespace_stego_c_tests PROPERTIES
    TIMEOUT 300
    ENVIRONMENT "LC_ALL=C.UTF-8"
)

set_tests_properties(whitespace_stego_coverage_tests PROPERTIES
    TIMEOUT 300
    ENVIRONMENT "LC_ALL=C.UTF-8"
)

set_tests_properties(whitespace_stego_100_coverage_tests PROPERTIES
    TIMEOUT 300
    ENVIRONMENT "LC_ALL=C.UTF-8"
)

set_tests_properties(whitespace_stego_cross_static_tests PROPERTIES
    TIMEOUT 300
    ENVIRONMENT "LC_ALL=C.UTF-8"
)

if(EXISTS "test/unity.h")
    set_tests_properties(whitespace_stego_unity_tests PROPERTIES
        TIMEOUT 300
        ENVIRONMENT "LC_ALL=C.UTF-8"
    )
endif()

# Standard static implementation executable
add_executable(whitespace-stego-static
    src/whitespace_stego_static.c
    src/crypto.c
    src/utils.c
    src/main_static.c
)
target_link_libraries(whitespace-stego-static OpenSSL::SSL OpenSSL::Crypto)

# Small static implementation executable
add_executable(whitespace-stego-static-small
    src/whitespace_stego_static_small.c
    src/crypto.c
    src/utils.c
    src/main_static_small.c
)
target_link_libraries(whitespace-stego-static-small OpenSSL::SSL OpenSSL::Crypto)

# Tiny static implementation executable
add_executable(whitespace-stego-static-tiny
    src/whitespace_stego_static_small.c
    src/crypto.c
    src/utils.c
    src/main_static_tiny.c
)
target_link_libraries(whitespace-stego-static-tiny OpenSSL::SSL OpenSSL::Crypto)

# Large static implementation executable
add_executable(whitespace-stego-static-large
    src/whitespace_stego_static_large.c
    src/crypto.c
    src/utils.c
    src/main_static_large.c
)
target_link_libraries(whitespace-stego-static-large OpenSSL::SSL OpenSSL::Crypto)

# Optionally, make whitespace-stego-c an alias for the standard static
add_executable(whitespace-stego-c ALIAS whitespace-stego-static)

# Static library
add_library(whitespace_stego_static STATIC
    src/whitespace_stego_static.c
    src/crypto.c
    src/utils.c
)
target_link_libraries(whitespace_stego_static OpenSSL::SSL OpenSSL::Crypto)

# Install targets
install(TARGETS whitespace_stego whitespace-stego-static whitespace-stego-static-small whitespace-stego-static-tiny whitespace-stego-static-large
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES include/whitespace_stego.h include/whitespace_stego_static.h include/whitespace_stego_static_small.h include/whitespace_stego_static_large.h
    DESTINATION include
) 