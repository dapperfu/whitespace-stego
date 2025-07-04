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

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
COVERAGE_OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%_coverage.o)
TARGET = $(BIN_DIR)/whitespace-stego-c
SHARED_LIB = $(LIB_DIR)/libwhitespace_stego.so
TEST_C_TARGET = $(BIN_DIR)/test-c
TEST_UNITY_TARGET = $(BIN_DIR)/test-unity
TEST_COVERAGE_TARGET = $(BIN_DIR)/test-coverage

.PHONY: all clean test test-c test-unity test-coverage coverage-report shared cmake-build cmake-test cmake-clean install-unity help install uninstall dev debug release

# Default target
all: $(TARGET) $(SHARED_LIB)

help:
	@echo "Whitespace Steganography - C Implementation"
	@echo "=========================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all             - Build binary and shared library (default)"
	@echo "  help            - Show this help message"
	@echo "  build           - Build binary only"
	@echo "  shared          - Build shared library only"
	@echo "  install         - Install to /usr/local/bin"
	@echo "  uninstall       - Remove from /usr/local/bin"
	@echo "  test            - Run basic tests"
	@echo "  test-c          - Run C implementation tests"
	@echo "  test-unity      - Run Unity framework tests"
	@echo "  test-coverage   - Run coverage tests"
	@echo "  test-all        - Run all tests"
	@echo "  coverage-report - Generate HTML coverage report"
	@echo "  cmake-build     - Build using CMake"
	@echo "  cmake-test      - Run CMake tests"
	@echo "  cmake-clean     - Clean CMake build"
	@echo "  install-unity   - Install Unity test framework"
	@echo "  dev             - Build with debug flags"
	@echo "  debug           - Build with debug flags and symbols"
	@echo "  release         - Build optimized release version"
	@echo "  clean           - Remove all build artifacts"
	@echo "  distclean       - Remove all build artifacts and dependencies"

build: $(TARGET)

shared: $(SHARED_LIB)

$(TARGET): $(OBJS)
	@mkdir -p $(BIN_DIR)
	$(CC) $(OBJS) -o $@ $(LDFLAGS)

$(SHARED_LIB): $(filter-out $(OBJ_DIR)/main.o, $(OBJS))
	@mkdir -p $(LIB_DIR)
	$(CC) $(filter-out $(OBJ_DIR)/main.o, $(OBJS)) -o $@ $(SHARED_LDFLAGS)

$(TEST_C_TARGET): $(filter-out $(OBJ_DIR)/main.o, $(OBJS)) $(TEST_DIR)/test-c.c
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(TEST_DIR)/test-c.c $(filter-out $(OBJ_DIR)/main.o, $(OBJS)) -o $@ $(LDFLAGS)

$(TEST_UNITY_TARGET): $(filter-out $(OBJ_DIR)/main.o, $(OBJS)) $(TEST_DIR)/test_unity.c
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(TEST_DIR)/test_unity.c $(filter-out $(OBJ_DIR)/main.o, $(OBJS)) -o $@ $(LDFLAGS)

$(TEST_COVERAGE_TARGET): $(filter-out $(OBJ_DIR)/main_coverage.o, $(COVERAGE_OBJS)) $(TEST_DIR)/test_gcov.c
	@mkdir -p $(BIN_DIR)
	$(CC) $(COVERAGE_CFLAGS) $(TEST_DIR)/test_gcov.c $(filter-out $(OBJ_DIR)/main_coverage.o, $(COVERAGE_OBJS)) -o $@ $(COVERAGE_LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR)/%_coverage.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(COVERAGE_CFLAGS) -c $< -o $@

# Development targets
dev: CFLAGS += -g -DDEBUG
dev: $(TARGET)

debug: CFLAGS += -g -O0 -DDEBUG
debug: $(TARGET)

release: CFLAGS += -O3 -DNDEBUG
release: $(TARGET)

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

coverage-report: test-coverage
	@echo "Generating coverage report..."
	@mkdir -p $(COVERAGE_DIR)
	@gcov -r obj/crypto_coverage.gcda obj/utils_coverage.gcda obj/whitespace_stego_coverage.gcda
	@lcov --capture --directory . --output-file $(COVERAGE_DIR)/coverage.info
	@genhtml $(COVERAGE_DIR)/coverage.info --output-directory $(COVERAGE_DIR)/html
	@echo "Coverage report generated in $(COVERAGE_DIR)/html/index.html"

# Run all tests
test-all: test test-c test-unity test-coverage
	@echo "All tests completed!"

# CMake integration targets
cmake-build:
	@echo "Building with CMake..."
	@mkdir -p test/build
	@cd test/build && cmake .. && make

cmake-test: cmake-build
	@echo "Running CMake tests..."
	@cd test/build && ctest --verbose

cmake-clean:
	@echo "Cleaning CMake build..."
	@rm -rf test/build

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

distclean: clean
	rm -f test/unity.h test/unity.c
	rm -rf test/build 