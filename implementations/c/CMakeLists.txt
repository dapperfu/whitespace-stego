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

# Fixed buffer size for static implementation (4 MiB = 4194304 bytes)
set(STATIC_BUFFER_SIZE 4194304)

# Source files for core functionality
set(CORE_SOURCES
    src/crypto.c
    src/utils.c
)

# Dynamic implementation (uses malloc/free)
set(DYNAMIC_SOURCES
    src/whitespace_stego.c
    ${CORE_SOURCES}
)

# Static implementation (uses pre-allocated 4MiB stack)
set(STATIC_SOURCES
    src/whitespace_stego_static.c
    ${CORE_SOURCES}
)

# Dynamic C implementation
add_executable(whitespace-stego-c-dynamic
    src/main.c
    ${DYNAMIC_SOURCES}
)
target_link_libraries(whitespace-stego-c-dynamic OpenSSL::SSL OpenSSL::Crypto)

# Static C implementation with 4MiB pre-allocated stack
add_executable(whitespace-stego-c-static
    src/main_static_cli.c
    ${STATIC_SOURCES}
)
target_link_libraries(whitespace-stego-c-static OpenSSL::SSL OpenSSL::Crypto)

# Create symlink for the main binary (points to static by default)
add_custom_command(TARGET whitespace-stego-c-static POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E create_symlink 
    whitespace-stego-c-static 
    ${CMAKE_BINARY_DIR}/whitespace-stego-c
)

# Shared library (using dynamic implementation)
add_library(whitespace_stego SHARED ${DYNAMIC_SOURCES})
target_link_libraries(whitespace_stego OpenSSL::SSL OpenSSL::Crypto)



# Test executables
add_executable(test-c test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_link_libraries(test-c OpenSSL::SSL OpenSSL::Crypto)

# Coverage test executable
add_executable(test-coverage test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_compile_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)
target_link_libraries(test-coverage OpenSSL::SSL OpenSSL::Crypto)
target_link_options(test-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)

# 100% Coverage test executable
add_executable(test-100-coverage test/test_100_coverage.c ${DYNAMIC_SOURCES})
target_compile_options(test-100-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)
target_link_libraries(test-100-coverage OpenSSL::SSL OpenSSL::Crypto)
target_link_options(test-100-coverage PRIVATE --coverage -fprofile-arcs -ftest-coverage)

# Cross-test executable for both implementations
add_executable(test-cross-impl
    test/cross_test_static.c
    ${DYNAMIC_SOURCES}
    ${STATIC_SOURCES}
)
target_link_libraries(test-cross-impl OpenSSL::SSL OpenSSL::Crypto)

# Unity test executable (if Unity is available)
if(EXISTS "test/unity.h")
    add_executable(test-unity test/test_unity.c test/unity.c ${DYNAMIC_SOURCES})
    target_link_libraries(test-unity OpenSSL::SSL OpenSSL::Crypto)
endif()

# Enable testing
enable_testing()

# Add tests
add_test(NAME whitespace_stego_c_tests COMMAND test-c)
add_test(NAME whitespace_stego_coverage_tests COMMAND test-coverage)
add_test(NAME whitespace_stego_100_coverage_tests COMMAND test-100-coverage)
add_test(NAME whitespace_stego_cross_impl_tests COMMAND test-cross-impl)

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

set_tests_properties(whitespace_stego_cross_impl_tests PROPERTIES
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
install(TARGETS whitespace-stego-c-dynamic whitespace-stego-c-static whitespace_stego
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES include/whitespace_stego.h include/whitespace_stego_static.h
    DESTINATION include
) 