CC = gcc
CFLAGS = -Wall -Wextra -O2 -I./include -fPIC
COVERAGE_CFLAGS = -Wall -Wextra -O0 -g -I./include -fPIC --coverage -fprofile-arcs -ftest-coverage
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

.PHONY: all clean test test-c test-unity test-coverage coverage-report shared

all: $(TARGET) $(SHARED_LIB)

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

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(LIB_DIR) $(COVERAGE_DIR)
	find . -name "*.gcno" -delete
	find . -name "*.gcda" -delete
	find . -name "*.gcov" -delete

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
	@gcov -r $(SRCS) -o $(OBJ_DIR)
	@lcov --capture --directory . --output-file $(COVERAGE_DIR)/coverage.info
	@genhtml $(COVERAGE_DIR)/coverage.info --output-directory $(COVERAGE_DIR)/html
	@echo "Coverage report generated in $(COVERAGE_DIR)/html/index.html"

# Run all tests
test-all: test test-c test-unity test-coverage
	@echo "All tests completed!"

# Install Unity framework (if not already installed)
install-unity:
	@echo "Installing Unity test framework..."
	@if [ ! -f "test/unity.h" ]; then \
		wget -O test/unity.h https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.h; \
		wget -O test/unity.c https://raw.githubusercontent.com/ThrowTheSwitch/Unity/master/src/unity.c; \
	fi 