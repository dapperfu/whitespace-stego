

# C Build
c-build:
	$(CC) -o whitespace-stego-c c/*.c

c-clean:
	rm -f whitespace-stego-c

	# OpenSSL support
	# Requires libssl-dev
c-openssl:
	$(CC) -o whitespace-stego-c c/*.c -lssl -lcrypto
