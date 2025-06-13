.PHONY: venv test clean rust-py rust-cli rust-test

venv:
	python3 -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -e .[dev]

test:
	.venv/bin/pytest --html=report.html --cov=whitespace_stego

rust-py:
	cd rust_py_backend && maturin develop

rust-cli:
	cd rust_backend && cargo build --release

rust-test:
	cd rust_backend && cargo test

clean:
	rm -rf .venv
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name "report.html" -delete
	cd rust_py_backend && cargo clean
	cd rust_backend && cargo clean 