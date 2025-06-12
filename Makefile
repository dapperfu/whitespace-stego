.PHONY: install test lint format clean md-report-gfm test-all

install:
	pip install -e .

test:
	pytest tests/ --cov=python --cov-report=term-missing

lint:
	mypy python/ tests/
	flake8 python/ tests/
	isort --check-only python/ tests/

format:
	black python/ tests/
	isort python/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

md-report-gfm:
	venv/bin/pytest --md-report --md-report-flavor gfm tests/ > report.md

test-all: test
	cd rust_backend && cargo test
	./test_roundtrip.sh
	# Add any other bash test scripts here 