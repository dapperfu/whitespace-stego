CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -O2 -fPIC
INCLUDES = -Iinclude
SRCDIR = src
OBJDIR = obj
LIBDIR = lib
BINDIR = ../bin

SOURCES = $(SRCDIR)/encoder.c $(SRCDIR)/decoder.c $(SRCDIR)/errors.c $(SRCDIR)/base64.c
OBJECTS = $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)
LIBRARY = $(LIBDIR)/libwhitespace_stego.a
CLI_BINARY = $(BINDIR)/whitespace-stego-c

.PHONY: all clean test cli

all: $(LIBRARY)

$(OBJDIR):
	mkdir -p $(OBJDIR)

$(LIBDIR):
	mkdir -p $(LIBDIR)

$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(LIBRARY): $(OBJECTS) | $(LIBDIR)
	ar rcs $@ $(OBJECTS)

clean:
	rm -rf $(OBJDIR) $(LIBDIR)
	rm -f $(CLI_BINARY)

test: $(LIBRARY)
	$(CC) $(CFLAGS) $(INCLUDES) tests/test_main.c -L$(LIBDIR) -lwhitespace_stego -o tests/test_main
	@if [ -f tests/test_main ]; then \
		./tests/test_main; \
	else \
		echo "Test binary not found, skipping tests"; \
	fi

cli: $(LIBRARY) | $(BINDIR)
	$(CC) $(CFLAGS) $(INCLUDES) examples/cli.c -L$(LIBDIR) -lwhitespace_stego -o $(CLI_BINARY)

$(BINDIR):
	mkdir -p $(BINDIR)

