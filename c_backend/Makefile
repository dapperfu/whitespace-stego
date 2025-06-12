CC = clang
CFLAGS = -Wall -Wextra -Werror -std=c11 -pedantic
LDFLAGS = 

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
TEST_DIR = tests

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
TARGET = $(BIN_DIR)/whitespace_stego_c

TEST_SRC = $(TEST_DIR)/test_main.c
TEST_OBJ = $(TEST_DIR)/test_main.o
TEST_TARGET = $(BIN_DIR)/test_whitespace_stego

.PHONY: all clean test

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

$(TEST_TARGET): $(OBJS) $(TEST_OBJ)
	@mkdir -p $(BIN_DIR)
	$(CC) $(OBJS) $(TEST_OBJ) -o $@ $(LDFLAGS)

$(TEST_OBJ): $(TEST_SRC)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(TEST_OBJ) 