BINDIR = ../bin
CLI_BINARY = $(BINDIR)/whitespace-stego-go

.PHONY: all clean cli

all: cli

cli: | $(BINDIR)
	@command -v go > /dev/null && go build -o $(CLI_BINARY) ./cmd/cli || (echo "go not found" && exit 1)

$(BINDIR):
	mkdir -p $(BINDIR)

clean:
	rm -f $(CLI_BINARY)

