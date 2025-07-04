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

# Source files
set(SOURCES
    src/whitespace_stego.c
    src/crypto.c
    src/utils.c
    src/main.c
)

# Main executable
add_executable(whitespace-stego-c ${SOURCES})
target_link_libraries(whitespace-stego-c OpenSSL::SSL OpenSSL::Crypto)

# Shared library (without main.c)
set(LIB_SOURCES
    src/whitespace_stego.c
    src/crypto.c
    src/utils.c
)

add_library(whitespace_stego SHARED ${LIB_SOURCES})
target_link_libraries(whitespace_stego OpenSSL::SSL OpenSSL::Crypto)

# Test executable
add_executable(test-c test/test-c.c ${LIB_SOURCES})
target_link_libraries(test-c OpenSSL::SSL OpenSSL::Crypto)

# Coverage test executable
add_executable(test-coverage test/test_gcov.c ${LIB_SOURCES})
target_compile_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)
target_link_libraries(test-coverage OpenSSL::SSL OpenSSL::Crypto)
target_link_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)

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

if(EXISTS "test/unity.h")
    set_tests_properties(whitespace_stego_unity_tests PROPERTIES
        TIMEOUT 300
        ENVIRONMENT "LC_ALL=C.UTF-8"
    )
endif()

# Install targets
install(TARGETS whitespace-stego-c whitespace_stego
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES include/whitespace_stego.h
    DESTINATION include
) 