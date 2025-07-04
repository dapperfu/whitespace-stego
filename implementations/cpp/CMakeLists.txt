cmake_minimum_required(VERSION 3.12)

# Project name and version
project(whitespace-stego-cpp VERSION 0.1.0 LANGUAGES CXX)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Add include directory
include_directories(${CMAKE_SOURCE_DIR}/include)

# Gather all source files
file(GLOB SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp)

# Main executable
add_executable(whitespace-stego-cpp ${SOURCES})
set_target_properties(whitespace-stego-cpp PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

# Compiler warnings
if(MSVC)
    target_compile_options(whitespace-stego-cpp PRIVATE /W4)
else()
    target_compile_options(whitespace-stego-cpp PRIVATE -Wall -Wextra -pedantic)
endif()

# Build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Install target
install(TARGETS whitespace-stego-cpp DESTINATION bin)

# Tests (if any test sources exist)
file(GLOB TEST_SOURCES ${CMAKE_SOURCE_DIR}/test/*.cpp)
if(TEST_SOURCES)
    add_executable(whitespace-stego-cpp-tests ${TEST_SOURCES})
    target_include_directories(whitespace-stego-cpp-tests PRIVATE ${CMAKE_SOURCE_DIR}/include)
    if(MSVC)
        target_compile_options(whitespace-stego-cpp-tests PRIVATE /W4)
    else()
        target_compile_options(whitespace-stego-cpp-tests PRIVATE -Wall -Wextra -pedantic)
    endif()
    set_target_properties(whitespace-stego-cpp-tests PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
    add_test(NAME whitespace-stego-cpp-tests COMMAND whitespace-stego-cpp-tests)
endif()

# Print summary
message(STATUS "Project: ${PROJECT_NAME} v${PROJECT_VERSION}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}") 