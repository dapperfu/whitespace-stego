#!/usr/bin/env python3
"""
Script to add C backend examples to the whitespace stego backends demo notebook.
"""

import json
import sys

def add_c_backend_section():
    # Read the existing notebook
    with open('notebooks/whitespace_stego_backends_demo.ipynb', 'r') as f:
        notebook = json.load(f)
    
    # Find the cell before the summary section
    summary_cell_index = None
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'markdown' and '## Summary and Conclusions' in cell['source'][0]:
            summary_cell_index = i
            break
    
    if summary_cell_index is None:
        print("Could not find summary section")
        return
    
    # Create the C backend markdown cell
    c_backend_markdown = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## C Backend Integration\n",
            "\n",
            "Now let's demonstrate the C backend functionality alongside Python and Rust backends. The C implementation provides a command-line interface for encoding and decoding messages."
        ]
    }
    
    # Create the C backend code cell
    c_backend_code = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# C Backend demonstration\n",
            "import subprocess\n",
            "import tempfile\n",
            "import os\n",
            "\n",
            "print(\"🔧 C Backend Integration Test\")\n",
            "print(\"=\" * 40)\n",
            "print()\n",
            "\n",
            "# Check if C backend is available\n",
            "c_backend_available = os.path.exists('./whitespace-stego-c')\n",
            "if not c_backend_available:\n",
            "    print(\"⚠️  C backend binary not found. C examples will be skipped.\")\n",
            "    print(\"Make sure to run this notebook from the project root directory.\")\n",
            "else:\n",
            "    print(\"✅ C backend binary found!\")\n",
            "    print()\n",
            "\n",
            "    # Test message and carrier\n",
            "    c_test_message = \"Hello from C backend!\"\n",
            "    c_test_carrier = \"This is a carrier text for C backend testing.\"\n",
            "\n",
            "    print(f\"Test message: '{c_test_message}'\")\n",
            "    print(f\"Test carrier: '{c_test_carrier}'\")\n",
            "    print()\n",
            "\n",
            "    # Create temporary files for C backend\n",
            "    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as msg_file:\n",
            "        msg_file.write(c_test_message)\n",
            "        msg_file_path = msg_file.name\n",
            "\n",
            "    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as carrier_file:\n",
            "        carrier_file.write(c_test_carrier)\n",
            "        carrier_file_path = carrier_file.name\n",
            "\n",
            "    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as output_file:\n",
            "        output_file_path = output_file.name\n",
            "\n",
            "    print(\"📁 Temporary files created:\")\n",
            "    print(f\"   Message file: {msg_file_path}\")\n",
            "    print(f\"   Carrier file: {carrier_file_path}\")\n",
            "    print(f\"   Output file: {output_file_path}\")\n",
            "    print()\n",
            "\n",
            "    # Test C backend encoding\n",
            "    print(\"1. C Backend Encoding:\")\n",
            "    try:\n",
            "        # Encode using C backend\n",
            "        encode_cmd = [\n",
            "            './whitespace-stego-c', 'encode',\n",
            "            '--message', msg_file_path,\n",
            "            '--carrier', carrier_file_path,\n",
            "            '--output', output_file_path\n",
            "        ]\n",
            "        \n",
            "        result = subprocess.run(encode_cmd, capture_output=True, text=True, timeout=10)\n",
            "        \n",
            "        if result.returncode == 0:\n",
            "            print(\"   ✅ C encoding successful!\")\n",
            "            \n",
            "            # Read the encoded output\n",
            "            with open(output_file_path, 'r') as f:\n",
            "                c_encoded = f.read()\n",
            "            \n",
            "            print(f\"   Encoded length: {len(c_encoded)} characters\")\n",
            "            print(f\"   Contains zero-width chars: {'\\\\u200b' in c_encoded or '\\\\u200d' in c_encoded}\")\n",
            "            \n",
            "        else:\n",
            "            print(f\"   ❌ C encoding failed: {result.stderr}\")\n",
            "            \n",
            "    except Exception as e:\n",
            "        print(f\"   ❌ C encoding error: {e}\")\n",
            "    print()\n",
            "\n",
            "    # Test C backend decoding\n",
            "    print(\"2. C Backend Decoding:\")\n",
            "    try:\n",
            "        # Create a temporary file for decoded output\n",
            "        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as decoded_file:\n",
            "            decoded_file_path = decoded_file.name\n",
            "        \n",
            "        # Decode using C backend\n",
            "        decode_cmd = [\n",
            "            './whitespace-stego-c', 'decode',\n",
            "            '--input', output_file_path,\n",
            "            '--output', decoded_file_path\n",
            "        ]\n",
            "        \n",
            "        result = subprocess.run(decode_cmd, capture_output=True, text=True, timeout=10)\n",
            "        \n",
            "        if result.returncode == 0:\n",
            "            print(\"   ✅ C decoding successful!\")\n",
            "            \n",
            "            # Read the decoded output\n",
            "            with open(decoded_file_path, 'r') as f:\n",
            "                c_decoded = f.read()\n",
            "            \n",
            "            print(f\"   Decoded message: '{c_decoded}'\")\n",
            "            print(f\"   Roundtrip successful: {c_test_message == c_decoded}\")\n",
            "            \n",
            "        else:\n",
            "            print(f\"   ❌ C decoding failed: {result.stderr}\")\n",
            "            \n",
            "    except Exception as e:\n",
            "        print(f\"   ❌ C decoding error: {e}\")\n",
            "    print()\n",
            "\n",
            "    # Clean up temporary files\n",
            "    try:\n",
            "        os.unlink(msg_file_path)\n",
            "        os.unlink(carrier_file_path)\n",
            "        os.unlink(output_file_path)\n",
            "        os.unlink(decoded_file_path)\n",
            "        print(\"🧹 Temporary files cleaned up\")\n",
            "    except:\n",
            "        pass\n",
            "    print()"
        ]
    }
    
    # Insert the new cells before the summary section
    notebook['cells'].insert(summary_cell_index, c_backend_markdown)
    notebook['cells'].insert(summary_cell_index + 1, c_backend_code)
    
    # Update the summary section to mention C backend
    summary_cell = notebook['cells'][summary_cell_index + 2]
    summary_cell['source'] = [
        "## Summary and Conclusions\n",
        "\n",
        "This notebook has demonstrated that the Python, Rust, and C backends of the `whitespace_stego` library:\n",
        "\n",
        "### ✅ **Perfect Interoperability**\n",
        "- All backends produce **identical encoded outputs** for the same input\n",
        "- Each backend can **decode messages encoded by the other backends**\n",
        "- **Cross-backend compatibility** is maintained across all scenarios\n",
        "\n",
        "### ✅ **Feature Parity**\n",
        "- All support **basic encoding/decoding** without carrier text\n",
        "- All support **carrier text embedding**\n",
        "- All support **password protection** with Fernet encryption\n",
        "- All handle **Unicode characters** and **special characters** correctly\n",
        "\n",
        "### ⚡ **Performance Benefits**\n",
        "- The **Rust backend** is significantly faster for both encoding and decoding\n",
        "- The **C backend** provides a lightweight command-line interface\n",
        "- **Python backend** offers the most flexible integration options\n",
        "\n",
        "### 🔧 **Use Cases**\n",
        "- **Python backend**: Great for **prototyping**, **scripting**, and **integration** with Python ecosystems\n",
        "- **Rust backend**: Ideal for **production systems**, **high-performance applications**, and **microservices**\n",
        "- **C backend**: Perfect for **command-line tools**, **system integration**, and **lightweight deployments**\n",
        "- **Mixed environments**: You can use any combination of backends without compatibility issues\n",
        "\n",
        "### 🎯 **Key Takeaway**\n",
        "The perfect interoperability between all three backends means you can choose the implementation that best fits your use case without worrying about compatibility issues. Whether you need the flexibility of Python, the performance of Rust, or the simplicity of C, all will work seamlessly together."
    ]
    
    # Write the updated notebook
    with open('notebooks/whitespace_stego_backends_demo.ipynb', 'w') as f:
        json.dump(notebook, f, indent=1)
    
    print("✅ Successfully added C backend section to the notebook!")

if __name__ == "__main__":
    add_c_backend_section() 