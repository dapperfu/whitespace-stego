"""Setup script for the Rust backend package."""

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="whitespace-stego-backend",
    version="0.1.0",
    packages=["whitespace_stego_backend"],
    rust_extensions=[RustExtension("whitespace_stego_backend.whitespace_stego_backend")],
    install_requires=["setuptools-rust>=1.5.2"],
    setup_requires=["setuptools-rust>=1.5.2"],
    zip_safe=False,
) 