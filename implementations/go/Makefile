# Makefile for whitespace-stego-go

.PHONY: all clean build test install uninstall help dev debug release coverage coverage-html coverage-xml lint fmt vet race bench

# Binary name
BINARY_NAME = whitespace-stego-go
BINARY_PATH = bin/$(BINARY_NAME)

# Build flags
LDFLAGS = -ldflags "-s -w"
DEV_LDFLAGS = -ldflags "-X main.version=dev -X main.buildTime=$(shell date -u '+%Y-%m-%d_%H:%M:%S')"
DEBUG_LDFLAGS = -ldflags "-X main.version=debug -X main.buildTime=$(shell date -u '+%Y-%m-%d_%H:%M:%S')"

# Go version
GO_VERSION = 1.21

# Default target
all: build

help:
	@echo "Whitespace Steganography - Go Implementation"
	@echo "==========================================="
	@echo ""
	@echo "Available targets:"
	@echo "  all             - Build the binary (default)"
	@echo "  help            - Show this help message"
	@echo "  build           - Build the binary"
	@echo "  dev             - Build with development flags"
	@echo "  debug           - Build with debug flags"
	@echo "  release         - Build optimized release version"
	@echo "  install         - Install to /usr/local/bin"
	@echo "  uninstall       - Remove from /usr/local/bin"
	@echo "  test            - Run tests"
	@echo "  test-verbose    - Run tests with verbose output"
	@echo "  test-race       - Run tests with race detection"
	@echo "  coverage        - Run tests with coverage"
	@echo "  coverage-html   - Generate HTML coverage report"
	@echo "  coverage-xml    - Generate XML coverage report"
	@echo "  lint            - Run linter"
	@echo "  fmt             - Format code"
	@echo "  vet             - Run go vet"
	@echo "  bench           - Run benchmarks"
	@echo "  clean           - Clean build artifacts"
	@echo "  distclean       - Clean all artifacts and dependencies"

build: $(BINARY_PATH)

$(BINARY_PATH): src/main.go src/stego/*.go
	@echo "Building $(BINARY_NAME)..."
	@mkdir -p bin
	go build $(LDFLAGS) -o $(BINARY_PATH) ./src/main.go

dev: LDFLAGS = $(DEV_LDFLAGS)
dev: $(BINARY_PATH)

debug: LDFLAGS = $(DEBUG_LDFLAGS)
debug: $(BINARY_PATH)

release: LDFLAGS = -ldflags "-s -w -X main.version=$(shell git describe --tags --always --dirty)"
release: $(BINARY_PATH)

install: build
	@echo "Installing $(BINARY_NAME)..."
	@sudo cp $(BINARY_PATH) /usr/local/bin/$(BINARY_NAME)
	@sudo chmod +x /usr/local/bin/$(BINARY_NAME)
	@echo "Installation complete!"

uninstall:
	@echo "Uninstalling $(BINARY_NAME)..."
	@sudo rm -f /usr/local/bin/$(BINARY_NAME)
	@echo "Uninstallation complete!"

test:
	@echo "Running tests..."
	@go test ./src/stego

test-verbose:
	@echo "Running tests with verbose output..."
	@go test -v ./src/stego

test-race:
	@echo "Running tests with race detection..."
	@go test -race ./src/stego

coverage:
	@echo "Running tests with coverage..."
	@go test -coverprofile=coverage.out -covermode=atomic ./src/stego
	@go tool cover -func=coverage.out

coverage-html: coverage
	@echo "Generating HTML coverage report..."
	@go tool cover -html=coverage.out -o coverage.html
	@echo "Coverage report generated: coverage.html"

coverage-xml: coverage
	@echo "Generating XML coverage report..."
	@if command -v gocover-cobertura >/dev/null 2>&1; then \
		gocover-cobertura < coverage.out > coverage.xml; \
		echo "XML coverage report generated: coverage.xml"; \
	else \
		echo "gocover-cobertura not available, install with: go install github.com/t-yuki/gocover-cobertura@latest"; \
	fi

lint:
	@echo "Running linter..."
	@if command -v golint >/dev/null 2>&1; then \
		golint ./src/...; \
	else \
		echo "golint not available, install with: go install golang.org/x/lint/golint@latest"; \
	fi

fmt:
	@echo "Formatting code..."
	@go fmt ./src/...

vet:
	@echo "Running go vet..."
	@go vet ./src/...

bench:
	@echo "Running benchmarks..."
	@go test -bench=. ./src/stego

clean:
	@echo "Cleaning..."
	@rm -rf bin/
	@rm -f coverage.out coverage.html coverage.xml coverage.txt
	@go clean

distclean: clean
	@echo "Cleaning all artifacts and dependencies..."
	@go clean -modcache
	@rm -rf go.sum

# Development targets
dev-run: dev
	@echo "Running in development mode..."
	@./$(BINARY_PATH) help

# Show version
version:
	@echo "Go version: $(shell go version)"
	@echo "Binary version: $(shell ./$(BINARY_PATH) version 2>/dev/null || echo 'Not built')"

# Check Go version
check-go:
	@echo "Checking Go version..."
	@if [ "$$(go version | grep -o 'go[0-9]\+\.[0-9]\+' | cut -c3-)" != "$(GO_VERSION)" ]; then \
		echo "Warning: Expected Go $(GO_VERSION), found $$(go version)"; \
	else \
		echo "Go version check passed: $$(go version)"; \
	fi 