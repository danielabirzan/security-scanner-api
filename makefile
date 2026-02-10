PYTHON := python3
PIP := pip3
APP_DIR := app
TEST_DIR := tests

.PHONY: format lint fix test all run install clean help

# Auto-format code (Black + isort only)
format:
	@echo "Formatting code..."
	black $(APP_DIR) $(TEST_DIR)
	isort $(APP_DIR) $(TEST_DIR)
	@echo "Formatting complete"

# Auto-fix ALL issues (modern with ruff)
fix:
	@echo "Auto-fixing all issues..."
	@echo "  - Removing unused imports..."
	autoflake --in-place --recursive $(APP_DIR) $(TEST_DIR)
	@echo "  - Fixing code issues with ruff..."
	ruff check --fix $(APP_DIR) $(TEST_DIR)
	@echo "  - Formatting with Black..."
	black $(APP_DIR) $(TEST_DIR)
	@echo "  - Sorting imports..."
	isort $(APP_DIR) $(TEST_DIR)
	@echo "All fixes applied"

# Check code quality (no auto-fix)
lint:
	@echo "Running code quality checks..."
	black --check $(APP_DIR) $(TEST_DIR)
	isort --check-only $(APP_DIR) $(TEST_DIR)
	ruff check $(APP_DIR) $(TEST_DIR)
	mypy $(APP_DIR)
	@echo "All checks passed"

# Run tests with coverage
test:
	@echo "Running test suite..."
	pytest $(TEST_DIR) -v --cov=$(APP_DIR) --cov-report=html
	@echo "Coverage report: htmlcov/index.html"

# Run fix + lint + test
all: fix lint test
	@echo "All checks passed"

# Start development server
run:
	@echo "Starting development server..."
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Install dependencies
install:
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	pre-commit install
	@echo "Installation complete"

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov .coverage
	@echo "Cleanup complete"

# Show available commands
help:
	@echo "Available commands:"
	@echo "  make format   - Format code (Black + isort)"
	@echo "  make fix      - Auto-fix ALL issues (ruff + autoflake)"
	@echo "  make lint     - Check code quality"
	@echo "  make test     - Run tests with coverage"
	@echo "  make all      - Fix + Lint + Test"
	@echo "  make run      - Start development server"
	@echo "  make install  - Install dependencies"
	@echo "  make clean    - Remove temporary files"
