CC = gcc
CFLAGS = -Wall -Wextra -O2 -I./include -fPIC
LDFLAGS = -lcrypto
SHARED_LDFLAGS = -shared -lcrypto

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
TEST_DIR = test
LIB_DIR = lib

SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
TARGET = $(BIN_DIR)/whitespace-stego-c
SHARED_LIB = $(LIB_DIR)/libwhitespace_stego.so
TEST_C_TARGET = $(BIN_DIR)/test-c

.PHONY: all clean test test-c shared

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

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(LIB_DIR)

test: $(TARGET)
	@echo "Running basic tests..."
	@./test/run_tests.sh

test-c: $(TEST_C_TARGET)
	@echo "Running C implementation tests..."
	@./$(TEST_C_TARGET) 