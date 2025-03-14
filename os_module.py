"""
Topic: OS Module in Python

Explanation:
The `os` module provides functions for interacting with the operating system.
"""

import os

# Getting current working directory
print("Current Directory:", os.getcwd())

# Listing files in the current directory
print("Files in directory:", os.listdir())

# Creating and removing a directory
os.mkdir("test_folder")
os.rmdir("test_folder")

"""
Code Explanation:
- `os.getcwd()` gets the current working directory.
- `os.listdir()` lists files in a directory.
- `os.mkdir()` creates a directory, and `os.rmdir()` removes it.
"""
