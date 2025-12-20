ASM = nasm
ASMFLAGS = -f elf64 -g
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -O2

OBJDIR = obj
SRCDIR = .
SOURCES = encoder.asm decoder.asm utils.asm
OBJECTS = $(SOURCES:%.asm=$(OBJDIR)/%.o)
LIBRARY = libwhitespace_stego_asm.a

.PHONY: all clean test

all: $(LIBRARY)

$(OBJDIR):
	mkdir -p $(OBJDIR)

$(OBJDIR)/%.o: $(SRCDIR)/%.asm | $(OBJDIR)
	$(ASM) $(ASMFLAGS) $< -o $@

$(LIBRARY): $(OBJECTS)
	ar rcs $@ $(OBJECTS)

clean:
	rm -rf $(OBJDIR) $(LIBRARY)

test: $(LIBRARY)
	$(CC) $(CFLAGS) -I../c/include test_main.c -L. -lwhitespace_stego_asm -o test_main
	./test_main

