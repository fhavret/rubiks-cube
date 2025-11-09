# Local installation

install:
	@pip install '.[dev]'

clean:
	@echo Cleaning workspace 🧹
	@rm -rf dist/ build/ .mypy_cache/ .pytest_cache/ .ruff_cache/ 
	@find . -type d -regex '.*\.egg-info' | xargs rm -rf
	@find . -type d -name __pycache__ | xargs rm -rf

# Testing

lint:
	@ruff check --fix src tests
	@mypy src tests

format:
	@ruff format src tests

test:
	@PYTHONPATH=src pytest tests
