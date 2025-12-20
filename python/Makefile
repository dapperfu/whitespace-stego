BINDIR = ../bin
CLI_BINARY = $(BINDIR)/whitespace-stego-python
PYTHON = python3

.PHONY: all clean cli install-deps

all: cli

install-deps:
	@$(PYTHON) -m pip install --user --quiet pyinstaller 2>/dev/null || \
	 $(PYTHON) -m pip install --break-system-packages --quiet pyinstaller 2>/dev/null || \
	 echo "Warning: PyInstaller installation failed, trying without it"

cli: install-deps | $(BINDIR)
	@echo "Building Python binary with PyInstaller..."
	@if $(PYTHON) -m PyInstaller --version > /dev/null 2>&1; then \
		$(PYTHON) -m PyInstaller --onefile --name whitespace-stego-python \
			--hidden-import whitespace_stego \
			--hidden-import whitespace_stego.encoder \
			--hidden-import whitespace_stego.decoder \
			--hidden-import whitespace_stego.errors \
			--clean \
			cli.py && \
		cp dist/whitespace-stego-python $(CLI_BINARY) && \
		chmod +x $(CLI_BINARY) && \
		echo "Python binary built: $(CLI_BINARY)"; \
	else \
		echo "Error: PyInstaller not available. Install with: pip install pyinstaller"; \
		exit 1; \
	fi

$(BINDIR):
	mkdir -p $(BINDIR)

clean:
	rm -rf build dist *.spec __pycache__ .pytest_cache
	rm -f $(CLI_BINARY)

