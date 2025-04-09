"""
Project Setup Configuration
This file contains the setup configuration for the Medical Chatbot project.
It defines the project metadata and package dependencies.
"""

from setuptools import find_packages, setup

# Configure project metadata and package information
setup(
  name='Generative AI Project',      # Project name
  version="0.0.0",                   # Project version
  author="Madhav Singh",             # Project author
  author_email="madhav26266@gmail.com", # Author's email
  packages=find_packages(),          # Automatically find all packages in the project
)
