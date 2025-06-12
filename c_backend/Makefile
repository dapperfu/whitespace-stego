CC = clang
CFLAGS = -Wall -Wextra -Werror -std=c11 -pedantic
LDFLAGS = 

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
TEST_DIR = tests

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
LIB_OBJS = $(filter-out $(OBJ_DIR)/main.o, $(OBJS))
TARGET = $(BIN_DIR)/whitespace_stego_c

TEST_SRC = $(TEST_DIR)/test_main.c
TEST_OBJ = $(TEST_DIR)/test_main.o
TEST_TARGET = $(BIN_DIR)/test_whitespace_stego

.PHONY: all clean test format

all: $(TARGET)

$(TARGET): $(OBJS)
	@mkdir -p $(BIN_DIR)
	$(CC) $(OBJS) -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

test: $(TEST_TARGET)
	@echo "Running tests..."
	$(TEST_TARGET)

$(TEST_TARGET): $(LIB_OBJS) $(TEST_OBJ)
	@mkdir -p $(BIN_DIR)
	$(CC) $(LIB_OBJS) $(TEST_OBJ) -o $@ $(LDFLAGS)

$(TEST_OBJ): $(TEST_SRC)
	$(CC) $(CFLAGS) -c $< -o $@

format:
	@echo "Formatting source files..."
	clang-format-17 -i $(SRCS) $(TEST_SRC)

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(TEST_OBJ) 