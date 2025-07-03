# Makefile for whitespace-stego-go

.PHONY: all clean build test

# Binary name
BINARY_NAME = whitespace-stego-go
BINARY_PATH = bin/$(BINARY_NAME)

# Source files
SRC_DIR = src
SRC_FILES = $(wildcard $(SRC_DIR)/*.go)

# Build flags
LDFLAGS = -ldflags "-s -w"

all: build

build: $(BINARY_PATH)

$(BINARY_PATH): $(SRC_FILES)
	@echo "Building $(BINARY_NAME)..."
	@mkdir -p bin
	go build $(LDFLAGS) -o $(BINARY_PATH) ./$(SRC_DIR)

clean:
	@echo "Cleaning..."
	@rm -rf bin/
	@go clean

test:
	@echo "Running tests..."
	@go test ./...

install: build
	@echo "Installing $(BINARY_NAME)..."
	@cp $(BINARY_PATH) /usr/local/bin/$(BINARY_NAME)

uninstall:
	@echo "Uninstalling $(BINARY_NAME)..."
	@rm -f /usr/local/bin/$(BINARY_NAME)

# Development targets
dev: build
	@echo "Running in development mode..."
	@./$(BINARY_PATH) help

# Show help
help:
	@echo "Available targets:"
	@echo "  build     - Build the binary"
	@echo "  clean     - Clean build artifacts"
	@echo "  test      - Run tests"
	@echo "  install   - Install to /usr/local/bin"
	@echo "  uninstall - Remove from /usr/local/bin"
	@echo "  dev       - Build and show help"
	@echo "  help      - Show this help" 