"""
Template Generator Script
This script creates the initial project structure and necessary files for the Medical Chatbot project.
It ensures all required directories and files exist before starting development.
"""

import os
from pathlib import Path
import logging

# Configure logging to show timestamps with messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of essential files and directories required for the project
list_of_files = [
  "src/__init__.py",      # Python package initialization
  "src/helper.py",        # Helper functions and utilities
  "src/prompt.py",        # Prompt templates and management
  ".env",                 # Environment variables and secrets
  "setup.py",            # Project setup and package configuration
  "app.py",              # Main application entry point
  "research/trials.ipynb", # Research and experimentation notebook
]

# Create directories and files if they don't exist
for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)

  # Create directory if it doesn't exist
  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Creating directory: {filedir} for the file {filename}")

  # Create empty file if it doesn't exist or is empty
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    with open(filepath, "w") as f:
      pass
    logging.info(f"Creating empty file: {filepath}")

  else:
    logging.info(f"{filepath} is already exists")
