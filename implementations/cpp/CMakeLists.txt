cmake_minimum_required(VERSION 3.12)

# Project name and version
project(whitespace-stego-cpp VERSION 0.1.0 LANGUAGES CXX)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Coverage option
option(COVERAGE "Enable coverage reporting" OFF)

if(COVERAGE)
    if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
        message(STATUS "Building with coverage flags")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 --coverage")
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")
    endif()
endif()

# Output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Add include directory
include_directories(${CMAKE_SOURCE_DIR}/include)

# Gather source files (excluding main.cpp for tests)
file(GLOB ALL_SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp)
list(REMOVE_ITEM ALL_SOURCES ${CMAKE_SOURCE_DIR}/src/main.cpp)

# Main executable (includes main.cpp)
file(GLOB MAIN_SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp)
add_executable(whitespace-stego-cpp ${MAIN_SOURCES})
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

# Tests - build each test file as a separate executable
file(GLOB TEST_SOURCES ${CMAKE_SOURCE_DIR}/test/*.cpp)
foreach(TEST_SOURCE ${TEST_SOURCES})
    get_filename_component(TEST_NAME ${TEST_SOURCE} NAME_WE)
    add_executable(${TEST_NAME} ${TEST_SOURCE} ${ALL_SOURCES})
    target_include_directories(${TEST_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include)
    if(MSVC)
        target_compile_options(${TEST_NAME} PRIVATE /W4)
    else()
        target_compile_options(${TEST_NAME} PRIVATE -Wall -Wextra -pedantic)
    endif()
    set_target_properties(${TEST_NAME} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
    add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME})
endforeach()

# Print summary
message(STATUS "Project: ${PROJECT_NAME} v${PROJECT_VERSION}")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
if(COVERAGE)
    message(STATUS "Coverage: Enabled")
endif() 