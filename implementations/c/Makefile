# Build accelerator configuration
CCACHE ?= ccache
CCACHE_DIR_NAME ?= .ccache
CCACHE_MAXSIZE_VAL ?= 1G
CCACHE_COMPRESS_VAL ?= 1

# Detect if ccache is available and configure it
ifeq ($(shell which $(CCACHE) 2>/dev/null),)
    # ccache not found, use regular compiler
    CC_WRAPPER = $(CC)
    CCACHE_AVAILABLE = 0
else
    # ccache found, configure and use it
    CC_WRAPPER = $(CCACHE) $(CC)
    CCACHE_AVAILABLE = 1
    # Set ccache environment variables
    export CCACHE_DIR = $(CCACHE_DIR_NAME)
    export CCACHE_MAXSIZE = $(CCACHE_MAXSIZE_VAL)
    export CCACHE_COMPRESS = $(CCACHE_COMPRESS_VAL)
endif

CC = gcc
CFLAGS = -Wall -Wextra -O2 -I./include -fPIC
COVERAGE_CFLAGS = -Wall -Wextra -O0 -g -I./include -fPIC --coverage -fprofile-arcs -ftest-coverage -std=c99
LDFLAGS = -lcrypto
COVERAGE_LDFLAGS = -lcrypto --coverage -fprofile-arcs -ftest-coverage
SHARED_LDFLAGS = -shared -lcrypto

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
TEST_DIR = test
LIB_DIR = lib
COVERAGE_DIR = coverage

# Buffer size configuration
BUFFER_CONFIG_SCRIPT = ./configure_buffer_sizes.sh
BUFFER_CONFIG_DIR = config
BUFFER_CONFIG_HEADER = $(BUFFER_CONFIG_DIR)/buffer_sizes.h
BUFFER_CONFIG_CMAKE = $(BUFFER_CONFIG_DIR)/buffer_sizes.cmake

# Check if buffer configuration exists
ifeq ($(wildcard $(BUFFER_CONFIG_HEADER)),)
    $(warning Buffer size configuration not found. Run 'make configure-buffers' first.)
    # Default buffer sizes (fallback)
    TINY_BUFFER_SIZE := 4096
    SMALL_BUFFER_SIZE := 1048576
    STANDARD_BUFFER_SIZE := 16777216
    LARGE_BUFFER_SIZE := 16777216
else
    # Load buffer sizes from generated header (using shell to extract values)
    TINY_BUFFER_SIZE := $(shell grep "TINY_BUFFER_SIZE" $(BUFFER_CONFIG_HEADER) | sed 's/.*TINY_BUFFER_SIZE \([0-9]*\).*/\1/')
    SMALL_BUFFER_SIZE := $(shell grep "SMALL_BUFFER_SIZE" $(BUFFER_CONFIG_HEADER) | sed 's/.*SMALL_BUFFER_SIZE \([0-9]*\).*/\1/')
    STANDARD_BUFFER_SIZE := $(shell grep "STANDARD_BUFFER_SIZE" $(BUFFER_CONFIG_HEADER) | sed 's/.*STANDARD_BUFFER_SIZE \([0-9]*\).*/\1/')
    LARGE_BUFFER_SIZE := $(shell grep "LARGE_BUFFER_SIZE" $(BUFFER_CONFIG_HEADER) | sed 's/.*LARGE_BUFFER_SIZE \([0-9]*\).*/\1/')
endif

# Buffer configuration target
configure-buffers:
	@echo "Configuring buffer sizes..."
	@$(BUFFER_CONFIG_SCRIPT)
	@echo "Buffer configuration complete!"

# Ensure buffer configuration exists before building
$(BUFFER_CONFIG_HEADER): $(BUFFER_CONFIG_SCRIPT)
	@echo "Buffer configuration missing. Running configuration..."
	@$(BUFFER_CONFIG_SCRIPT)

# Core library source files (for coverage and shared library)
CORE_SRCS = $(SRC_DIR)/whitespace_stego.c $(SRC_DIR)/crypto.c $(SRC_DIR)/utils.c
CORE_OBJS = $(CORE_SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
CORE_COVERAGE_OBJS = $(CORE_SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%_coverage.o)

# All source files (for main executable)
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
COVERAGE_OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%_coverage.o)

TARGET = $(BIN_DIR)/whitespace-stego-c
SHARED_LIB = $(LIB_DIR)/libwhitespace_stego.so
TEST_C_TARGET = $(BIN_DIR)/test-c
TEST_UNITY_TARGET = $(BIN_DIR)/test-unity
TEST_COVERAGE_TARGET = $(BIN_DIR)/test-coverage
TEST_100_COVERAGE_TARGET = $(BIN_DIR)/test-100-coverage

CMAKE_BUILD_DIR = test/build
CMAKE_GENERATOR ?= "Unix Makefiles"
CMAKE_CCACHE_ARG = -DCMAKE_C_COMPILER_LAUNCHER=$(CCACHE)

.PHONY: all clean test test-c test-unity test-coverage coverage-report shared cmake-build cmake-test cmake-clean install-unity help install uninstall dev debug release ccache-setup ccache-stats ccache-clean ccache-show whitespace-stego-static whitespace-stego-static-small whitespace-stego-static-tiny whitespace-stego-static-large test-static test-static-small test-static-tiny test-static-large test-cross-static

# Default target builds all implementations
all: $(BUFFER_CONFIG_HEADER) cmake-build $(TARGET) $(SHARED_LIB) whitespace-stego-static whitespace-stego-static-small whitespace-stego-static-tiny whitespace-stego-static-large

help:
	@echo "Whitespace Steganography - C Implementation"
	@echo "=========================================="
	@echo ""
	@echo "Build Acceleration:"
	@echo "  ccache-setup    - Setup ccache for faster builds"
	@echo "  ccache-stats    - Show ccache statistics"
	@echo "  ccache-clean    - Clean ccache"
	@echo "  ccache-show     - Show ccache configuration"
	@echo ""
	@echo "CMake Integration:"
	@echo "  cmake-build     - Build using CMake (default=Release)"
	@echo "  cmake-debug     - Build using CMake (Debug profile)"
	@echo "  cmake-release   - Build using CMake (Release profile)"
	@echo "  cmake-test      - Run CMake-based tests"
	@echo "  cmake-clean     - Clean CMake build artifacts"
	@echo ""
	@echo "Available targets:"
	@echo "  all             - Build all implementations (default)"
	@echo "  help            - Show this help message"
	@echo "  build           - Build binary only"
	@echo "  shared          - Build shared library only"
	@echo "  install         - Install to /usr/local/bin"
	@echo "  uninstall       - Remove from /usr/local/bin"
	@echo ""
	@echo "Static Implementations:"
	@echo "  whitespace-stego-static        - Standard static implementation (4 GiB buffers)"
	@echo "  whitespace-stego-static-small  - Small static implementation (1 MiB buffers)"
	@echo "  whitespace-stego-static-tiny   - Tiny static implementation (4 KiB buffers)"
	@echo "  whitespace-stego-static-large  - Large static implementation (4 GiB, optimized)"
	@echo ""
	@echo "Testing:"
	@echo "  test            - Run basic tests"
	@echo "  test-c          - Run C implementation tests"
	@echo "  test-unity      - Run Unity framework tests"
	@echo "  test-coverage   - Run coverage tests"
	@echo "  test-100-coverage - Run 100%% coverage tests"
	@echo "  test-cross-static - Run cross-tests for static implementations"
	@echo "  test-all        - Run all tests (including static implementations)"
	@echo "  test-static     - Test standard static implementation"
	@echo "  test-static-small - Test small static implementation"
	@echo "  test-static-tiny - Test tiny static implementation"
	@echo "  test-static-large - Test large static implementation"
	@echo ""
	@echo "Coverage:"
	@echo "  coverage-report - Generate HTML coverage report"
	@echo "  coverage-summary - Show core library coverage summary"
	@echo ""
	@echo "Development:"
	@echo "  cmake-build     - Build using CMake"
	@echo "  cmake-test      - Run CMake tests"
	@echo "  cmake-clean     - Clean CMake build"
	@echo "  install-unity   - Install Unity test framework"
	@echo "  dev             - Build with debug flags"
	@echo "  debug           - Build with debug flags and symbols"
	@echo "  release         - Build optimized release version"
	@echo "  clean           - Remove all build artifacts"
	@echo "  distclean       - Remove all build artifacts and dependencies"

# ccache setup and management
ccache-setup:
	@if [ $(CCACHE_AVAILABLE) -eq 1 ]; then \
		echo "🚀 Setting up ccache for faster builds..."; \
		mkdir -p $(CCACHE_DIR_NAME); \
		$(CCACHE) -s; \
		echo "✅ ccache configured and ready!"; \
	else \
		echo "⚠️  ccache not found. Install ccache for faster builds:"; \
		echo "   Ubuntu/Debian: sudo apt-get install ccache"; \
		echo "   macOS: brew install ccache"; \
		echo "   CentOS/RHEL: sudo yum install ccache"; \
	fi

ccache-stats:
	@if [ $(CCACHE_AVAILABLE) -eq 1 ]; then \
		echo "📊 ccache statistics:"; \
		$(CCACHE) -s; \
	else \
		echo "❌ ccache not available"; \
	fi

ccache-clean:
	@if [ $(CCACHE_AVAILABLE) -eq 1 ]; then \
		echo "🧹 Cleaning ccache..."; \
		$(CCACHE) -C; \
		echo "✅ ccache cleaned!"; \
	else \
		echo "❌ ccache not available"; \
	fi

ccache-show:
	@if [ $(CCACHE_AVAILABLE) -eq 1 ]; then \
		echo "🔧 ccache configuration:"; \
		echo "CCACHE_DIR: $(CCACHE_DIR_NAME)"; \
		echo "CCACHE_MAXSIZE: $(CCACHE_MAXSIZE_VAL)"; \
		echo "CCACHE_COMPRESS: $(CCACHE_COMPRESS_VAL)"; \
		$(CCACHE) -p; \
	else \
		echo "❌ ccache not available"; \
	fi

build: ccache-setup $(TARGET) $(SHARED_LIB)

shared: ccache-setup $(SHARED_LIB)

$(TARGET): $(OBJS)
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking $(TARGET)..."
	$(CC_WRAPPER) $(OBJS) -o $@ $(LDFLAGS)

$(SHARED_LIB): $(CORE_OBJS)
	@mkdir -p $(LIB_DIR)
	@echo "🔗 Linking shared library $(SHARED_LIB)..."
	$(CC_WRAPPER) $(CORE_OBJS) -o $@ $(SHARED_LDFLAGS)

$(TEST_C_TARGET): $(CORE_OBJS) $(TEST_DIR)/test-c.c
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking test-c..."
	$(CC_WRAPPER) $(CFLAGS) $(TEST_DIR)/test-c.c $(CORE_OBJS) -o $@ $(LDFLAGS)

$(TEST_UNITY_TARGET): $(CORE_OBJS) $(TEST_DIR)/test_unity.c
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking test-unity..."
	$(CC_WRAPPER) $(CFLAGS) $(TEST_DIR)/test_unity.c $(CORE_OBJS) -o $@ $(LDFLAGS)

$(TEST_COVERAGE_TARGET): $(CORE_COVERAGE_OBJS) $(TEST_DIR)/test_gcov.c
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking test-coverage..."
	$(CC_WRAPPER) $(COVERAGE_CFLAGS) $(TEST_DIR)/test_gcov.c $(CORE_COVERAGE_OBJS) -o $@ $(COVERAGE_LDFLAGS)

$(TEST_100_COVERAGE_TARGET): $(CORE_COVERAGE_OBJS) $(TEST_DIR)/test_100_coverage.c
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking test-100-coverage..."
	$(CC_WRAPPER) $(COVERAGE_CFLAGS) $(TEST_DIR)/test_100_coverage.c $(CORE_COVERAGE_OBJS) -o $@ $(COVERAGE_LDFLAGS)

# Cross-test target
TEST_CROSS_STATIC_TARGET = $(BIN_DIR)/test-cross-static

$(TEST_CROSS_STATIC_TARGET): $(CORE_OBJS) $(TEST_DIR)/cross_test_static.c
	@mkdir -p $(BIN_DIR)
	@echo "🔗 Linking test-cross-static..."
	$(CC_WRAPPER) $(CFLAGS) $(TEST_DIR)/cross_test_static.c $(CORE_OBJS) -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	@echo "🔨 Compiling $<..."
	$(CC_WRAPPER) $(CFLAGS) -c $< -o $@

$(OBJ_DIR)/%_coverage.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	@echo "🔨 Compiling $< (coverage)..."
	$(CC_WRAPPER) $(COVERAGE_CFLAGS) -c $< -o $@

# Development targets
dev: CFLAGS += -g -DDEBUG
dev: ccache-setup $(TARGET)

debug: CFLAGS += -g -O0 -DDEBUG
debug: ccache-setup $(TARGET)

release: CFLAGS += -O3 -DNDEBUG
release: ccache-setup $(TARGET)

# Installation targets
install: $(TARGET)
	@echo "Installing whitespace-stego-c to /usr/local/bin..."
	@sudo cp $(TARGET) /usr/local/bin/
	@sudo chmod +x /usr/local/bin/whitespace-stego-c
	@echo "Installation complete!"

uninstall:
	@echo "Removing whitespace-stego-c from /usr/local/bin..."
	@sudo rm -f /usr/local/bin/whitespace-stego-c
	@echo "Uninstallation complete!"

# Test targets
test: $(TARGET)
	@echo "Running basic tests..."
	@./test/run_tests.sh

test-c: $(TEST_C_TARGET)
	@echo "Running C implementation tests..."
	@./$(TEST_C_TARGET)

test-unity: $(TEST_UNITY_TARGET)
	@echo "Running Unity framework tests..."
	@./$(TEST_UNITY_TARGET)

test-coverage: $(TEST_COVERAGE_TARGET)
	@echo "Running coverage tests..."
	@./$(TEST_COVERAGE_TARGET)

test-100-coverage: $(TEST_100_COVERAGE_TARGET)
	@echo "Running 100%% coverage tests..."
	@./$(TEST_100_COVERAGE_TARGET)

test-cross-static: $(TEST_CROSS_STATIC_TARGET)
	@echo "Running cross-tests for static implementations..."
	@./$(TEST_CROSS_STATIC_TARGET)

coverage-report: test-100-coverage
	@echo "Generating coverage report for core library files..."
	@mkdir -p $(COVERAGE_DIR)
	@gcov -r obj/crypto_coverage.gcda obj/utils_coverage.gcda obj/whitespace_stego_coverage.gcda
	@lcov --capture --directory . --output-file $(COVERAGE_DIR)/coverage.info
	@genhtml $(COVERAGE_DIR)/coverage.info --output-directory $(COVERAGE_DIR)/html
	@echo "Coverage report generated in $(COVERAGE_DIR)/html/index.html"
	@echo "📊 Core library coverage summary:"
	@gcov -r obj/crypto_coverage.gcda obj/utils_coverage.gcda obj/whitespace_stego_coverage.gcda | grep -E "(File|Lines|Branches)" | head -9

coverage-summary: test-100-coverage
	@echo "📊 Core Library Coverage Summary:"
	@echo "================================="
	@gcov -r obj/crypto_coverage.gcda obj/utils_coverage.gcda obj/whitespace_stego_coverage.gcda | grep -E "(File|Lines|Branches)" | head -9
	@echo ""
	@echo "🎯 Coverage Targets:"
	@echo "  - crypto.c: Target 100%% (currently ~37%%)"
	@echo "  - utils.c: Target 100%% (currently ~59%%)"
	@echo "  - whitespace_stego.c: Target 100%% (currently ~80%%)"

# Run all tests (original)
test-all-original: test test-c test-unity test-coverage test-100-coverage
	@echo "All tests completed!"

# Run all tests
test-all: test test-c test-unity test-coverage test-100-coverage test-cross-static test-static test-static-small test-static-tiny test-static-large
	@echo "All tests completed!"

# CMake integration targets
cmake-build: $(BUFFER_CONFIG_HEADER)
	@echo "Building with CMake (Release) using configured buffer sizes..."
	@mkdir -p $(CMAKE_BUILD_DIR)
	cd $(CMAKE_BUILD_DIR) && \
		cmake -G $(CMAKE_GENERATOR) -DCMAKE_BUILD_TYPE=Release $(if $(shell which $(CCACHE) 2>/dev/null),$(CMAKE_CCACHE_ARG),) ../.. && \
		cmake --build .

cmake-debug:
	@echo "Building with CMake (Debug)..."
	@mkdir -p $(CMAKE_BUILD_DIR)
	cd $(CMAKE_BUILD_DIR) && \
		cmake -G $(CMAKE_GENERATOR) -DCMAKE_BUILD_TYPE=Debug $(if $(shell which $(CCACHE) 2>/dev/null),$(CMAKE_CCACHE_ARG),) ../.. && \
		cmake --build .

cmake-release:
	@echo "Building with CMake (Release)..."
	@mkdir -p $(CMAKE_BUILD_DIR)
	cd $(CMAKE_BUILD_DIR) && \
		cmake -G $(CMAKE_GENERATOR) -DCMAKE_BUILD_TYPE=Release $(if $(shell which $(CCACHE) 2>/dev/null),$(CMAKE_CCACHE_ARG),) ../.. && \
		cmake --build .

cmake-test: cmake-build
	@echo "Running CMake-based tests..."
	cd $(CMAKE_BUILD_DIR) && ctest --verbose

cmake-clean:
	@echo "Cleaning CMake build..."
	@rm -rf $(CMAKE_BUILD_DIR)

# Install Unity framework (if not already installed)
install-unity:
	@echo "Installing Unity test framework..."
	@if [ ! -f "test/unity.h" ]; then \
		wget -O test/unity.h https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h; \
		wget -O test/unity.c https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c; \
	fi

# Clean targets
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(LIB_DIR) $(COVERAGE_DIR)
	find . -name "*.gcno" -delete
	find . -name "*.gcda" -delete
	find . -name "*.gcov" -delete

distclean: clean ccache-clean
	rm -f test/unity.h test/unity.c
	rm -rf test/build
	rm -rf $(CCACHE_DIR_NAME)

# Static implementation targets
whitespace-stego-static: bin/whitespace-stego-static

whitespace-stego-static-small: bin/whitespace-stego-static-small

whitespace-stego-static-tiny: bin/whitespace-stego-static-tiny

whitespace-stego-static-large: bin/whitespace-stego-static-large

# Individual build targets for static implementations
bin/whitespace-stego-static: bin
	cmake -B build -S .
	cmake --build build --target whitespace-stego-static
	cp build/whitespace-stego-static bin/

bin/whitespace-stego-static-small: bin
	cmake -B build -S .
	cmake --build build --target whitespace-stego-static-small
	cp build/whitespace-stego-static-small bin/

bin/whitespace-stego-static-tiny: bin
	cmake -B build -S .
	cmake --build build --target whitespace-stego-static-tiny
	cp build/whitespace-stego-static-tiny bin/

bin/whitespace-stego-static-large: bin
	cmake -B build -S .
	cmake --build build --target whitespace-stego-static-large
	cp build/whitespace-stego-static-large bin/

# whitespace-stego-c is now an alias for whitespace-stego-static
bin/whitespace-stego-c: bin/whitespace-stego-static
	ln -sf whitespace-stego-static bin/whitespace-stego-c

# Test targets for static implementations
test-static: bin/whitespace-stego-static
	./bin/whitespace-stego-static --help

test-static-small: bin/whitespace-stego-static-small
	./bin/whitespace-stego-static-small --help

test-static-tiny: bin/whitespace-stego-static-tiny
	./bin/whitespace-stego-static-tiny --help

test-static-large: bin/whitespace-stego-static-large
	./bin/whitespace-stego-static-large --help

# Update test-all to include static implementations
test-all: test test-c test-unity test-coverage test-100-coverage test-cross-static test-static test-static-small test-static-tiny test-static-large
	@echo "All tests completed!"
