#!/bin/bash

# Build script for Whitespace Steganography WASI project

set -e

echo "🔨 Building Whitespace Steganography WASI..."

# Check if wasm-pack is installed
if ! command -v wasm-pack &> /dev/null; then
    echo "❌ wasm-pack is not installed. Installing..."
    cargo install wasm-pack
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf pkg/
rm -rf target/

# Build the WASM module
echo "📦 Building WASM module..."
wasm-pack build --target web --out-dir pkg

# Copy the HTML file to the pkg directory for easy testing
echo "📄 Copying HTML file..."
cp index.html pkg/

echo "✅ Build completed successfully!"
echo "🌐 To test the application, run:"
echo "   cd pkg && python3 -m http.server 8000"
echo "   Then open http://localhost:8000 in your browser" 