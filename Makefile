PYTHON := python3
PIP := pip3
APP_DIR := app
TEST_DIR := tests

.PHONY: format lint fix test all run install install-prod clean help

format:
	black $(APP_DIR) $(TEST_DIR)
	isort $(APP_DIR) $(TEST_DIR)

fix:
	autoflake --in-place --recursive $(APP_DIR) $(TEST_DIR)
	ruff check --fix $(APP_DIR) $(TEST_DIR)
	black $(APP_DIR) $(TEST_DIR)
	isort $(APP_DIR) $(TEST_DIR)

lint:
	black --check $(APP_DIR) $(TEST_DIR)
	isort --check-only $(APP_DIR) $(TEST_DIR)
	ruff check $(APP_DIR) $(TEST_DIR)
	mypy $(APP_DIR)

test:
	pytest $(TEST_DIR) -v --cov=$(APP_DIR) --cov-report=html --cov-report=term

all: format fix lint test

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	pre-commit install

install-prod:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov .coverage

help:
	@echo "Development:"
	@echo "  make install      - Install all dependencies"
	@echo "  make run          - Start dev server"
	@echo "  make format       - Format code"
	@echo "  make fix          - Auto-fix all issues"
	@echo "  make lint         - Check quality"
	@echo "  make test         - Run tests"
	@echo "  make all          - Fix + lint + test"
	@echo ""
	@echo "Production:"
	@echo "  make install-prod - Production deps only"
