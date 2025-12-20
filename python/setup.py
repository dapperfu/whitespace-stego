"""Setup script for whitespace-stego package."""

from setuptools import setup, find_packages

setup(
    name="whitespace-stego",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
    },
)

