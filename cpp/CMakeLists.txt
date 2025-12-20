cmake_minimum_required(VERSION 3.10)
project(whitespace-stego VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Library
add_library(whitespace_stego STATIC
    src/encoder.cpp
    src/decoder.cpp
)

target_include_directories(whitespace_stego PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# CLI example
add_executable(whitespace-stego-cli
    examples/cli.cpp
)

target_link_libraries(whitespace-stego-cli
    whitespace_stego
)

# Copy CLI to bin directory after build
add_custom_command(TARGET whitespace-stego-cli POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory ${CMAKE_SOURCE_DIR}/../bin
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:whitespace-stego-cli> ${CMAKE_SOURCE_DIR}/../bin/whitespace-stego-cpp
    COMMENT "Copying CLI binary to bin/ directory"
)

# Tests
enable_testing()
add_executable(test_main
    tests/test_main.cpp
)

target_link_libraries(test_main
    whitespace_stego
)

add_test(NAME whitespace_stego_tests COMMAND test_main)

