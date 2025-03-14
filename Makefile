.PHONY: run clean

# Python virtual environment path
VENV := .venv
PYTHON := $(VENV)/bin/python

# Ensure virtual environment exists
$(VENV):
	python -m venv $(VENV)

# Run the main script
run: $(VENV)
	$(PYTHON) main.py

# Clean up pyc files and __pycache__
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} + 