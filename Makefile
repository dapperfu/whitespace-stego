.PHONY: install test lint format clean

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