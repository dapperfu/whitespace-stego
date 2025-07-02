GO = go
GOFLAGS = -ldflags="-s -w"
BIN_DIR = bin
TARGET = $(BIN_DIR)/whitespace-stego-go
TEST_DIR = test

.PHONY: all clean test build

all: $(TARGET)

build: $(TARGET)

$(TARGET): src/*.go go.mod
	@mkdir -p $(BIN_DIR)
	$(GO) build $(GOFLAGS) -o $@ ./src

clean:
	rm -rf $(BIN_DIR)
	$(GO) clean

test: $(TARGET)
	@echo "Running Go implementation tests..."
	@cd $(TEST_DIR) && ./run_tests.sh

install: $(TARGET)
	@echo "Installing whitespace-stego-go..."
	@cp $(TARGET) ../whitespace-stego-go

# Development targets
dev-build:
	$(GO) build -o $(TARGET) ./src

dev-test:
	$(GO) test ./src

fmt:
	$(GO) fmt ./src

vet:
	$(GO) vet ./src

# Run with specific arguments for testing
run-encode: $(TARGET)
	@echo "Testing encode operation..."
	@echo "Hello" | $(TARGET) encode -m "Secret message" -c "Hello"

run-decode: $(TARGET)
	@echo "Testing decode operation..."
	@$(TARGET) decode -c "Hello" -o - 