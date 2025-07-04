#!/usr/bin/env python3
"""
Setup script for whitespace-stego package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Get package data
def get_package_data():
    return {
        "whitespace_stego": ["*.so"],
    }

setup(
    name="whitespace-stego",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for encoding messages in text using zero-width Unicode characters",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dapperfu/whitespace-stego",
    packages=find_packages(),
    package_data=get_package_data(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "cryptography>=42.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "mypy>=1.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "build>=0.10.0",
            "twine>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "whitespace-stego=whitespace_stego.cli:main",
        ],
    },
    zip_safe=False,  # Required for binary extensions
) 